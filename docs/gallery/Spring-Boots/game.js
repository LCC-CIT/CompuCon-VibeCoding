// ============================================================
// SPRING BOOTS PLATFORMER — a vertical tower-climb game
// ============================================================
// You control a character with spring-loaded boots.
// Hold SPACEBAR to compress the springs, release to launch.
// Use LEFT/RIGHT arrow keys to aim your launch direction.
// Land on the golden platform at the top to win the level.
// ============================================================

// Find the <canvas> element in the HTML page. This is where
// all the game graphics will be drawn.
const canvas = document.getElementById('gameCanvas');

// Get the "2D drawing context" from the canvas. Think of this
// as a paintbrush that lets us draw shapes, colors, and text
// onto the canvas surface.
const ctx = canvas.getContext('2d');

// ============================================================
// GAME CONSTANTS — numbers that control how the game feels
// ============================================================
// These are all in "pixels" (px) and "seconds" (s).
// Pixels are the tiny dots that make up the screen.
// The canvas is 800 pixels wide and 600 pixels tall.

const W = 800;                      // the width of the game screen, in pixels
const H = 600;                      // the height of the game screen, in pixels
const GRAVITY = 1100;               // how fast the character falls, in pixels per second squared
const MAX_CHARGE = 0.7;             // how many seconds you need to hold SPACE to reach full power
const MAX_LAUNCH = 750;             // the fastest speed you can launch, in pixels per second
const MIN_LAUNCH = 240;             // the slowest speed you can launch (just tapping SPACE)
const GRACE_TIME = 3.0;             // total seconds you can hold SPACE before the overcharge penalty starts
const FAIL_TIME = 6.0;              // total seconds you can hold SPACE before the spring breaks (no launch)
const OVERCHARGE_RAMP = FAIL_TIME - GRACE_TIME;  // the 3-second window where power fades (3.0 = 6.0 - 3.0)
const AIR_ACCEL = 320;              // how quickly you can steer left/right while flying through the air
const MAX_AIR_SPEED = 190;          // the fastest you can steer horizontally while airborne
const CRUMBLE_TIME = 3.0;           // how many seconds a cracking platform takes before it falls apart
const CRUMBLE_RESPAWN = 3.0;        // how many seconds before a fallen platform comes back
const MOVE_PAUSE = 0.5;             // how long a moving platform stops at each end before reversing
const BOUNCE_POWER = 1050;          // the launch speed when you land on a green bounce pad
const PLAYER_W = 30;                // the width of the character's body, in pixels
const PLAYER_H = 36;                // the height of the character's body (not counting the spring boots)
const WORLD_H = 3400;               // the total height of the game world, in pixels
const GROUND_Y = 3300;              // the Y position of the ground surface (Y increases going down)

// ============================================================
// KEYBOARD INPUT — tracks which keys the player is pressing
// ============================================================

// Create an empty object to store which keys are currently held down.
// Example: keys['Space'] = true means the spacebar is being pressed.
const keys = {};

// Listen for when ANY key on the keyboard is pressed down.
// This runs automatically every time a key goes down.
window.addEventListener('keydown', e => {
    // Mark this key as "currently pressed" in our keys object
    keys[e.code] = true;

    // For game-related keys, tell the browser NOT to do its normal thing.
    // Without this, pressing Space would scroll the page, and arrow keys
    // would move the scrollbar. We want those keys for our game instead.
    if (['Space','ArrowLeft','ArrowRight','ArrowUp','ArrowDown','KeyA','KeyD','KeyW','KeyS'].includes(e.code)) {
        e.preventDefault();  // stops the browser's default action for this key
    }
});

// Listen for when ANY key on the keyboard is released (let go).
window.addEventListener('keyup', e => {
    // Mark this key as "no longer pressed"
    keys[e.code] = false;

    // Also prevent default browser behavior for game keys when released
    if (['Space','ArrowLeft','ArrowRight','ArrowUp','ArrowDown','KeyA','KeyD','KeyW','KeyS'].includes(e.code)) {
        e.preventDefault();
    }
});

// ============================================================
// PLAYER STATE — everything we need to remember about the character
// ============================================================
// This is a single "object" (a bundle of related values) that
// describes the player's current situation at any moment.

let player = {
    // --- Position in the game world ---
    x: 385,                         // how far from the left edge of the world (pixels)
    y: GROUND_Y - PLAYER_H - 18,    // how far from the top of the world (pixels)
                                     // This formula places the character standing on the ground

    // --- Current speed (velocity) ---
    vx: 0,                          // horizontal speed: positive = moving right, negative = left
    vy: 0,                          // vertical speed: positive = falling down, negative = going up

    // --- Size of the character's collision box ---
    w: PLAYER_W,                    // width of the hitbox (30 pixels)
    h: PLAYER_H,                    // height of the hitbox (36 pixels, body only)

    // --- What is the character currently doing? ---
    grounded: false,                // true = standing on a platform, false = in the air
    charging: false,                // true = holding SPACE to compress the spring boots
    stunned: false,                 // true = recovering from landing on head (can't move)
    stunTimer: 0,                   // counts down from ~1 second while stunned

    // --- Spring boots charge level ---
    charge: 0,                      // how full the charge bar is (0 = empty, 0.7 = full)
    holdTime: 0,                    // total time SPACE has been held (keeps counting past full charge)

    // --- Which direction are we aiming? ---
    aimAngle: -Math.PI / 2,         // angle in radians: -PI/2 = straight up, 0 = right, PI/2 = down
                                     // (PI is about 3.14, so -PI/2 is about -1.57)

    // --- Ground rolling (spinning in place to inch forward) ---
    spinAccum: 0,                   // tracks how much we've rotated (builds up to a full 360°)
    rollTarget: null,               // the X position we're smoothly sliding to (null = not rolling)

    // --- Fall tracking (for detecting head-landings) ---
    fallPeakY: 0,                   // the highest point we reached since leaving the ground

    // --- Which platform are we standing on? ---
    platform: null,                 // points to the platform object we're currently on top of

    // --- Trampoline bounce counter ---
    bounceCount: 0,                 // how many times in a row we've bounced (resets on normal landing)
};

// ============================================================
// CAMERA — controls which part of the world is visible on screen
// ============================================================
// The game world is 3400 pixels tall, but the screen is only
// 600 pixels tall. The camera scrolls to follow the player.

let camY;                           // the world Y coordinate shown at the TOP of the screen

function resetCamera() {
    // Position the camera so the ground is visible at the bottom of the screen.
    // GROUND_Y is 3300, H is 600, so camY = 3300 + 40 - 600 = 2740.
    // This means the screen shows world Y from 2740 to 3340 (ground at 3300).
    camY = GROUND_Y + 40 - H;
}

// ============================================================
// LEVEL SYSTEM — generates the platforms and coins for each level
// ============================================================
// There are 5 levels. Each level introduces one new type of
// special platform (called a "modifier"). Level 1 has one-way
// platforms, level 2 adds crumbling platforms, etc.

let platforms = [];                 // list of all platform objects currently in the world
let currentLevel = 1;               // which level number we're playing (1, 2, 3, 4, or 5+)
let tutorialMsg = null;             // the tutorial popup text and position (null = no popup showing)
let tutorialTimer = 0;              // how many seconds the tutorial popup has been visible

function buildLevel(levelNum) {
    // --- Reset everything for the new level ---
    platforms = [];                  // clear the list of platforms
    coins = [];                      // clear the list of coins
    score = 0;                       // reset the coin counter to zero
    tutorialMsg = null;              // remove any old tutorial popup
    tutorialTimer = 0;               // reset the tutorial timer
    currentLevel = levelNum;         // remember which level number this is

    // --- Create the ground platform ---
    // This is the wide brown platform at the very bottom of the world.
    // x=0 means it starts at the left edge, w=W means it spans the full 800-pixel width.
    // h=100 means it's 100 pixels thick (so the player can't fall through it).
    platforms.push({
        x: 0,                        // left edge of the ground
        y: GROUND_Y,                 // top surface of the ground (3300 pixels down)
        w: W,                        // width = full screen width (800 pixels)
        h: 100,                      // thickness = 100 pixels going down
        color: '#4a6b2a',            // dark green-brown color
        type: 'ground',              // special type so we can identify it later
        vx: 0,                       // doesn't move horizontally
        vy: 0,                       // doesn't move vertically
        startX: 0,                   // original X position (unused for ground)
        moveRange: 0                 // how far it can move (0 = stationary)
    });

    // --- Create the goal zone ---
    // A large golden area at the top of the level. Entering this zone
    // (not landing on a platform) triggers the win and pauses the game.
    platforms.push({
        x: 140,                      // left edge (centered: 800-520)/2 = 140
        y: 20,                       // 20 pixels from the top of the world
        w: 520,                      // 520 pixels wide (generous landing zone)
        h: 60,                       // 60 pixels tall (thick zone, easy to hit)
        color: '#ffd700',            // gold color
        type: 'goal',                // special type: winning zone
        oneway: true,                // doesn't block movement from any direction
        vx: 0, vy: 0,                // stationary
        startX: 0, moveRange: 0      // doesn't move
    });

    // --- Decide which modifier types are available in this level ---
    // Each level unlocks one new type. Level 5+ has everything including combos.
    const unlocked = [];             // list of modifier names available this level
    if (levelNum >= 1) unlocked.push('oneway');    // level 1+: platforms you can jump through
    if (levelNum >= 2) unlocked.push('crumble');   // level 2+: platforms that crack and fall
    if (levelNum >= 3) unlocked.push('bounce');    // level 3+: trampoline pads
    if (levelNum >= 4) unlocked.push('moving');    // level 4+: platforms that slide side to side
    const combosOk = levelNum >= 5;  // level 5+ allows combined modifiers (like moving+bounce)

    // The modifier that is NEW to this specific level (for showing the tutorial popup)
    const newMod = levelNum <= 4 ? unlocked[unlocked.length - 1] : null;

    // --- Generate 28 climbing platforms ---
    // We create a list of "definitions" first, then turn them into actual platform objects.
    // Each platform is about 108 pixels higher than the previous one.
    const levelDef = [];             // will hold {dy, cx, w, special} for each platform

    // Pre-made lists of X positions and widths for variety.
    // Each platform picks from these lists, cycling through them.
    const colX = [
        400, 320, 550, 200, 450, 120, 600, 350, 500, 180,
        650, 300, 550, 100, 400, 650, 250, 500, 130, 600,
        350, 200, 550, 400, 120, 600, 300, 500
    ];                               // 28 horizontal center positions (in pixels from left)

    const widths = [
        170, 150, 150, 140, 140, 150, 140, 160, 140, 140,
        150, 140, 160, 140, 140, 150, 130, 140, 150, 140,
        160, 140, 140, 150, 140, 160, 140, 150
    ];                               // 28 platform widths (in pixels)

    // Loop 28 times to create 28 platform definitions
    for (let i = 0; i < 28; i++) {
        const dy = 130 + i * 108;    // distance above ground: first is 130px, last is ~3046px
        const cx = colX[i % colX.length];    // pick the next X center from our list
        const w = widths[i % widths.length]; // pick the next width from our list

        // --- Calculate the chance of this platform being a modifier ---
        // Modifiers are RARE at the bottom and become MORE COMMON near the top.
        // This creates a natural difficulty curve: easy start, challenging finish.
        const heightFrac = i / 27;   // 0.0 at the bottom (i=0), 1.0 at the top (i=27)
        const rarity = heightFrac * 0.35 + (levelNum - 1) * 0.02;  // base curve + small level bonus
        const modChance = Math.min(rarity, 0.45);  // never exceed 45% chance (cap it)

        let special = null;          // will hold the modifier type(s) for this platform, or null

        // Roll the dice: should this platform have a modifier?
        if (Math.random() < modChance && unlocked.length > 0) {
            // Math.random() returns a random decimal between 0 and 1.
            // If it's less than modChance, this platform gets a modifier.

            // --- Weight the modifier selection by difficulty ---
            // Easy modifiers (bounce, oneway) should appear MORE at the BOTTOM.
            // Hard modifiers (crumble) should appear MORE at the TOP.
            // Neutral modifiers (moving) appear evenly throughout.
            const easyMods = ['bounce', 'oneway'];     // these help the player
            const hardMods = ['crumble'];               // these make it harder
            const easyW = Math.max(0.1, 1 - heightFrac);   // 1.0 at bottom → 0.1 at top
            const hardW = Math.max(0.1, heightFrac);        // 0.1 at bottom → 1.0 at top
            const neutralW = 0.5;                            // constant weight everywhere

            // Build a "weighted pool" where more likely modifiers appear more times.
            // Imagine a bag of marbles: easy marbles are more numerous at the bottom,
            // hard marbles are more numerous at the top.
            const weightedPool = [];
            for (const m of unlocked) {
                let w = neutralW;            // start with neutral weight (0.5)
                if (easyMods.includes(m)) w = easyW;    // override with easy weight if applicable
                if (hardMods.includes(m)) w = hardW;    // override with hard weight if applicable
                // Add w*8 copies of this modifier to the pool (at least 1 copy)
                for (let j = 0; j < Math.max(1, Math.round(w * 8)); j++) {
                    weightedPool.push(m);
                }
            }
            // Pick a random modifier from the weighted pool
            special = weightedPool[Math.floor(Math.random() * weightedPool.length)];

            // --- Small chance of a COMBO (two modifiers on one platform) ---
            // Only possible at level 5+. 15% chance if modifier was selected.
            if (combosOk && Math.random() < 0.15 && unlocked.length >= 2) {
                // Pick a second modifier that's different from the first one
                const others = weightedPool.filter(m => m !== special);
                const second = others[Math.floor(Math.random()
                    * Math.max(1, others.length))];
                if (second) special = [special, second];  // store as an array of two strings
            }
        }

        // --- Tutorial placement: force the new modifier to appear at least once ---
        // This ensures the player sees an example of the new modifier type.
        // Hard modifiers (crumble) are placed higher up so beginners encounter them later.
        const forceIdx = newMod === 'crumble' ? 6 : 3;  // crumble starts at platform 6, others at 3
        if (newMod && !tutorialMsg && i >= forceIdx && i <= forceIdx + 4) {
            special = newMod;        // override whatever was chosen with the tutorial modifier
        }

        // Add this platform definition to our list
        levelDef.push({ dy, cx, w, special });
    }

    // --- Now convert each definition into a real platform object ---
    let tutorialPlaced = false;      // ensures we only show one tutorial popup

    // Helper function: choose the right color for a platform based on its modifier tags
    function pickColor(def, tags) {
        // Combo colors (when two modifiers are combined)
        if (tags.includes('moving') && tags.includes('bounce')) return '#cc8844';   // orange
        if (tags.includes('moving') && tags.includes('crumble')) return '#cc6644';  // red-brown
        if (tags.includes('crumble') && tags.includes('bounce')) return '#aacc44';  // green-tan
        if (tags.includes('crumble') && tags.includes('oneway')) return '#b8a870';  // tan-teal
        // Single modifier colors
        if (tags.includes('moving')) return '#c94040';     // red for moving platforms
        if (tags.includes('crumble')) return '#b89860';    // tan for crumbling platforms
        if (tags.includes('bounce')) return '#44cc44';     // green for bounce pads
        if (tags.includes('oneway')) return '#6b8e8e';     // teal for one-way platforms
        // Plain platform colors cycle through three brown shades
        return (def.dy % 3 === 0) ? '#8b6914'             // dark brown (every 3rd)
            : ((def.dy % 3 === 1) ? '#7a5c3a'             // medium brown (every 3rd+1)
            : '#6b8e4e');                                   // light brown (every 3rd+2)
    }

    // Loop through each platform definition and create the actual platform
    for (const def of levelDef) {
        // Calculate world position from the definition
        const platY = GROUND_Y - def.dy;         // world Y: ground minus distance (going up)
        const platX = def.cx - def.w / 2;        // world X: center minus half width = left edge

        // Convert the "special" field into an array of modifier tags.
        // "special" could be: null (no modifier), "moving" (one modifier),
        // or ["moving","bounce"] (two modifiers).
        const tags = def.special
            ? (Array.isArray(def.special) ? def.special : [def.special])
            : [];                                // normalize to always be an array

        // Check which modifiers apply by looking for each tag in the array
        const isMoving = tags.includes('moving');      // does this platform slide side to side?
        const isCrumble = tags.includes('crumble');    // does this platform crack and fall?
        const isBounce = tags.includes('bounce');      // does this platform bounce the player?
        const isOneway = tags.includes('oneway');      // can the player jump through from below?

        // Build the platform object with all its properties
        const p = {
            // --- Position and size ---
            x: platX,                    // world X of the left edge
            y: platY,                    // world Y of the top surface
            w: def.w,                    // width in pixels
            h: 14,                       // thickness (all climbing platforms are 14px thick)
            startY: platY,               // remember original Y (for crumbling platform respawn)

            // --- Appearance ---
            color: pickColor(def, tags), // what color to draw it

            // --- Behavior type ---
            type: isCrumble ? 'crumble'        // if crumbling, type is 'crumble'
                : (isMoving ? 'moving'          // else if moving, type is 'moving'
                : 'platform'),                  // otherwise it's a plain 'platform'

            // --- Modifier flags (these can all be true at once for combos!) ---
            isMoving,                    // true if this is a moving platform
            isCrumble,                   // true if this is a crumbling platform
            isBounce,                    // true if this is a bounce pad
            oneway: isOneway,            // true if you can jump through from below

            // --- Movement properties ---
            vx: isMoving ? 70 : 0,       // horizontal speed: 70 px/s for moving, 0 for others
            vy: 0,                        // vertical speed: starts at 0 (crumbling uses this later)
            paused: false,                // true when a moving platform is resting at an endpoint
            pauseTimer: 0,                // counts down the 0.5-second pause
            startX: platX,                // original X position (center of oscillation range)
            moveRange: isMoving ? 90 : 0, // how far it can move left/right from startX

            // --- Crumbling state ---
            crumbling: false,             // true when the player is standing on it (timer started)
            crumbleTimer: 0,              // how long the player has been standing on it
            fallen: false,                // true after the platform has fallen off screen
        };
        platforms.push(p);               // add this platform to the global platforms array

        // --- Tutorial popup: show when the first platform with the new modifier appears ---
        if (newMod && !tutorialPlaced && tags.includes(newMod)) {
            // Pre-written explanations for each modifier type
            const tutorialTexts = {
                oneway:  '△ These dashed platforms can be jumped through from below!',
                crumble: '⚠ Cracked platforms will fall — get off quickly!',
                bounce:  '⌃ Green pads bounce you — each bounce gets weaker!',
                moving:  '⟷ Red platforms move side to side — time your landing!',
            };
            // Create the tutorial message at this platform's Y position
            tutorialMsg = { text: tutorialTexts[newMod], y: platY, dy: def.dy };
            tutorialPlaced = true;       // don't show another tutorial this level
        }

        // --- Place a coin between each pair of platforms ---
        // Skip the very first platform (dy=130) since there's nothing below it
        if (def.dy > 130) {
            const coinY = platY - 40;    // 40 pixels above the platform surface
            const coinX = def.cx + (def.dy % 2 === 0 ? -30 : 30);  // alternate left/right
            coins.push({ x: coinX, y: coinY, collected: false });  // add to coins array
        }
    }

    // ============================================================
    // POST-PROCESSING — fix any unfair platform arrangements
    // ============================================================
    // These rules run AFTER all platforms are generated to ensure
    // the level is fair and playable.

    // --- Rule 1: No more than ONE crumbling platform in the first 10 ---
    let earlyCrumble = 0;              // count how many crumbling platforms we've seen
    for (let i = 0; i < Math.min(10, platforms.length); i++) {
        // Check if this platform is crumbling (and not the ground)
        if (platforms[i].isCrumble && platforms[i].type !== 'ground') {
            earlyCrumble++;            // found another crumbling platform
            if (earlyCrumble > 1) {
                // Too many! Convert this one to a regular platform.
                const p = platforms[i];  // shorthand for the platform we're fixing
                p.isCrumble = false;     // remove crumbling behavior
                p.crumbling = false;     // not currently cracking
                p.crumbleTimer = 0;      // reset the crack timer
                p.fallen = false;        // hasn't fallen
                p.type = p.isMoving ? 'moving' : 'platform';  // update type
                // Pick an appropriate color based on remaining modifiers
                p.color = p.isMoving ? '#c94040'
                    : (p.oneway ? '#6b8e8e'
                    : (p.isBounce ? '#44cc44' : '#7a5c3a'));
                // If it has no modifiers left, make it a plain brown platform
                if (!p.isMoving && !p.isBounce && !p.oneway) p.color = '#7a5c3a';
            }
        }
    }

    // --- Rule 2: Every 6 consecutive platforms must have at least 1 regular one ---
    // This ensures the player always has a safe brown platform to land on.
    // The screen shows about 5-6 platforms at a time, so this guarantees
    // at least one safe spot is always visible.
    for (let i = 0; i < platforms.length - 5; i++) {
        // Take a "slice" of 6 platforms starting at position i.
        // Filter out the ground platform (it's always safe, doesn't count).
        const slice = platforms.slice(i, i + 6)
            .filter(p => p.type !== 'ground');

        // Check if ALL platforms in this slice are special (any modifier)
        const allSpecial = slice.every(p =>
            p.isMoving || p.isCrumble || p.isBounce || p.oneway);

        // If all 6 are special, and we have at least 5 non-ground platforms...
        if (allSpecial && slice.length >= 5) {
            // Convert the middle platform in the slice to plain.
            const mid = slice[Math.floor(slice.length / 2)];
            mid.isMoving = false;        // remove all modifier flags
            mid.isCrumble = false;
            mid.isBounce = false;
            mid.oneway = false;
            mid.type = 'platform';       // plain platform type
            mid.color = '#7a5c3a';       // medium brown color
            mid.vx = 0;                  // stop any movement
            mid.crumbling = false;       // reset crumbling state
            mid.fallen = false;
        }
    }
}

// ============================================================
// RESET PLAYER — send the character back to the starting position
// ============================================================
// Called when the player falls off the world or presses R to retry.

function resetPlayer() {
    player.x = 385;                      // center of the ground platform
    player.y = GROUND_Y - PLAYER_H - 18; // standing on top of the ground
    player.vx = 0;                       // not moving horizontally
    player.vy = 0;                       // not moving vertically
    player.grounded = false;             // will be set to true by collision detection next frame
    player.charging = false;             // not holding SPACE
    player.charge = 0;                   // empty charge bar
    player.holdTime = 0;                 // reset the hold timer
    player.aimAngle = -Math.PI / 2;      // aim straight up
    player.platform = null;              // not standing on any platform yet
    player.bounceCount = 0;              // reset trampoline bounce decay
    player.spinAccum = 0;                // reset rotation accumulator for ground roll
    player.rollTarget = null;            // cancel any in-progress roll animation
    player.stunned = false;              // not stunned
    player.stunTimer = 0;                // clear stun timer
    player.fallPeakY = 0;                // reset fall distance tracking
    resetCamera();                       // move camera back to show the ground
}

// ============================================================
// SHARED GAME STATE — variables used across multiple functions
// ============================================================

let won = false;            // true when the player has reached the golden goal platform
let particles = [];         // list of active particle effects (sparks, smoke, etc.)
let coins = [];             // list of all coins in the current level
let score = 0;              // how many coins the player has collected this level

// ============================================================
// UPDATE FUNCTION — runs every frame, handles ALL game logic
// ============================================================
// This is the "brain" of the game. It's called ~60 times per second.
// Parameter dt = "delta time" = seconds since the last frame (usually ~0.016).

function update(dt) {
    if (won) return;                     // freeze everything when the level is complete

    // Clamp delta time to prevent physics explosions.
    // If the game lags and dt becomes huge (like 0.5 seconds),
    // characters could teleport through platforms. Capping at 0.05 prevents this.
    const dtc = Math.min(dt, 0.05);

    // ============================================================
    // PLATFORM MOVEMENT — update moving, crumbling, and fallen platforms
    // ============================================================
    for (const p of platforms) {         // loop through EVERY platform in the world

        // --- Moving platforms: slide back and forth, pausing at each end ---
        if (p.isMoving) {
            p.prevX = p.x;               // remember X position before moving (needed for delta)

            if (p.paused) {
                // The platform is resting at an endpoint. Count down the pause timer.
                p.pauseTimer -= dtc;     // subtract elapsed time from the pause countdown
                if (p.pauseTimer <= 0) {
                    // Pause is over! Resume moving in the opposite direction.
                    p.paused = false;    // no longer paused
                    p.vx = -p.vx;        // flip velocity: 70 becomes -70, or -70 becomes 70
                }
                p.deltaX = 0;            // no movement this frame (player won't be carried)
            } else {
                // The platform is moving normally. Slide it by its velocity.
                p.x += p.vx * dtc;       // new X = old X + (speed × time)
                p.deltaX = p.x - p.prevX; // how far it moved this frame

                // Check if the platform reached its range limit on the RIGHT side
                if (p.x >= p.startX + p.moveRange) {
                    p.x = p.startX + p.moveRange;  // snap to exact endpoint
                    p.paused = true;                // begin pause
                    p.pauseTimer = MOVE_PAUSE;      // set pause countdown to 0.5 seconds
                    p.vx = 0;                       // stop moving
                    p.deltaX = p.x - p.prevX;       // recalculate delta for this frame
                }
                // Check if the platform reached its range limit on the LEFT side
                else if (p.x <= p.startX - p.moveRange) {
                    p.x = p.startX - p.moveRange;  // snap to exact endpoint
                    p.paused = true;                // begin pause
                    p.pauseTimer = MOVE_PAUSE;      // set pause countdown to 0.5 seconds
                    p.vx = 0;                       // stop moving
                    p.deltaX = p.x - p.prevX;       // recalculate delta for this frame
                }
            }
        }

        // --- Crumbling platforms: crack while player stands on them ---
        if (p.isCrumble && p.crumbling && !p.fallen) {
            // If the player jumped off, the platform recovers (stops crumbling)
            if (player.platform !== p) {
                p.crumbling = false;     // stop crumbling
                p.crumbleTimer = 0;      // reset the crack timer
            } else {
                // Player is still standing here. Keep counting down.
                p.crumbleTimer += dtc;   // add elapsed time to the crack timer
                if (p.crumbleTimer >= CRUMBLE_TIME) {
                    // Time's up! The platform breaks and begins to fall.
                    p.fallen = true;     // mark as fallen
                    p.vy = 300;          // initial downward speed (pixels per second)
                }
            }
        }

        // --- Fallen crumbling platforms: accelerate downward, then respawn ---
        if (p.isCrumble && p.fallen) {
            p.y += p.vy * dtc;           // move the platform downward
            p.vy += 600 * dtc;           // apply gravity to the falling platform itself
            // Once it falls below the world, start the respawn countdown
            if (p.y > WORLD_H + 100) {
                p.respawnTimer = (p.respawnTimer || 0) + dtc;  // count up
                if (p.respawnTimer >= CRUMBLE_RESPAWN) {
                    // Respawn! Return to original position, good as new.
                    p.y = p.startY;      // back to original Y
                    p.vy = 0;            // stop falling
                    p.fallen = false;    // no longer fallen
                    p.crumbling = false; // not currently cracking
                    p.crumbleTimer = 0;  // reset crack timer
                    p.respawnTimer = 0;  // reset respawn timer
                }
            }
        }
    }

    // --- Moving platform carry: player rides along with the platform ---
    // If the player is standing on a moving platform, move the player
    // by the same amount the platform moved this frame.
    if (player.grounded && player.platform && player.platform.isMoving) {
        player.x += player.platform.deltaX;  // add the platform's movement to player's position
        // Keep the player inside the screen walls after being carried
        if (player.x < 0) player.x = 0;
        if (player.x + player.w > W) player.x = W - player.w;
    }

    // ============================================================
    // STUN — countdown the stun timer
    // ============================================================
    if (player.stunned) {
        player.stunTimer -= dtc;         // subtract elapsed time from stun countdown
        if (player.stunTimer <= 0) {
            player.stunned = false;      // stun is over! Player can move again.
        }
    }

    // ============================================================
    // AIM ROTATION — left/right arrow keys rotate the launch direction
    // ============================================================
    const aimSpeed = 3.5;                // rotation speed in radians per second (~200° per second)
    const prevAim = player.aimAngle;     // save current angle so we can calculate rotation amount
    if (!player.stunned) {               // can't aim while stunned (head-landing recovery)
        if (keys['ArrowLeft'] || keys['KeyA']) {
            player.aimAngle -= aimSpeed * dtc;   // rotate counter-clockwise
        }
        if (keys['ArrowRight'] || keys['KeyD']) {
            player.aimAngle += aimSpeed * dtc;   // rotate clockwise
        }
    }

    // ============================================================
    // GROUND ROLL — spinning in a full circle inches you forward
    // ============================================================
    const ROLL_PER_TURN = 12;            // pixels moved per complete 360° rotation
    if (!player.stunned && player.grounded && !player.charging) {
        // Add this frame's rotation to the accumulator.
        // (player.aimAngle - prevAim) is how much we rotated this frame.
        player.spinAccum += player.aimAngle - prevAim;

        // Check if we've accumulated a full clockwise rotation (360° = 2π ≈ 6.28 radians)
        if (player.spinAccum >= Math.PI * 2) {
            player.rollTarget = player.x + ROLL_PER_TURN;  // nudge 12 pixels to the RIGHT
            player.spinAccum -= Math.PI * 2;               // subtract one full rotation
        }
        // Check if we've accumulated a full counter-clockwise rotation
        else if (player.spinAccum <= -Math.PI * 2) {
            player.rollTarget = player.x - ROLL_PER_TURN;  // nudge 12 pixels to the LEFT
            player.spinAccum += Math.PI * 2;               // add back one full rotation
        }
    }

    // Smooth animation: slide the player toward the roll target over several frames.
    // This makes the nudge look smooth instead of an instant teleport.
    if (player.rollTarget !== null) {
        // Lerp (linear interpolation): move a fraction of the remaining distance each frame.
        // 12 * dtc ≈ 0.2 at 60fps, so we cover ~20% of the remaining gap per frame.
        player.x += (player.rollTarget - player.x) * Math.min(12 * dtc, 1);
        // When very close to the target, snap to it exactly
        if (Math.abs(player.rollTarget - player.x) < 0.3) {
            player.x = player.rollTarget;    // snap to exact target
            player.rollTarget = null;        // nudge animation is complete
        }
        // Keep within screen walls
        if (player.x < 0) player.x = 0;
        if (player.x + player.w > W) player.x = W - player.w;
    }

    // ============================================================
    // SPRING CHARGE — holding SPACEBAR compresses the boots
    // ============================================================
    // Player must be on the ground and not stunned to charge.
    if (keys['Space'] && player.grounded && !player.stunned) {
        if (!player.charging) {
            // Just started pressing SPACE this moment
            player.charging = true;      // begin charging state
            player.charge = 0;           // reset the charge bar display value
            player.holdTime = 0;         // reset the total hold timer
        }
        player.holdTime += dtc;          // keep counting total time SPACE has been held
        // The charge bar shows min(holdTime, MAX_CHARGE) — it caps at 0.7 seconds.
        // holdTime keeps going past MAX_CHARGE to track overcharge.
        player.charge = Math.min(player.holdTime, MAX_CHARGE);

        // --- Auto-fizzle: holding WAY too long makes the spring give out ---
        if (player.holdTime >= FAIL_TIME) {
            spawnFizzleParticles();      // sad brown particle puff
            player.charging = false;     // cancel the charge
            player.charge = 0;           // empty the charge bar
            player.holdTime = 0;         // reset the hold timer
            // No launch happens — the spring failed
        }
    }

    // ============================================================
    // LAUNCH — releasing SPACEBAR (or leaving the ground) fires the boots
    // ============================================================
    // This triggers when EITHER: Space is released, OR the player
    // walks off a platform while still holding Space.
    if (!keys['Space'] || !player.grounded) {
        if (player.charging) {
            // --- Step 1: Calculate the base launch power from charge level ---
            const ratio = player.charge / MAX_CHARGE;            // 0.0 (empty) to 1.0 (full)

            // Linearly interpolate between MIN_LAUNCH and MAX_LAUNCH based on ratio.
            // At ratio=0: basePower = MIN_LAUNCH (240). At ratio=1: basePower = MAX_LAUNCH (750).
            // At ratio=0.5: basePower = 240 + 0.5*(750-240) = 240 + 255 = 495.
            const basePower = MIN_LAUNCH + ratio * (MAX_LAUNCH - MIN_LAUNCH);

            // --- Step 2: Apply overcharge penalty (reverse-quadratic decay) ---
            let penalty = 0;             // starts at 0 (no penalty)
            if (player.holdTime > GRACE_TIME) {
                // t goes from 0.0 (just entered overcharge) to 1.0 (at FAIL_TIME).
                // t² means it starts slow and accelerates — a "reverse quadratic" curve.
                const t = (player.holdTime - GRACE_TIME) / OVERCHARGE_RAMP;
                penalty = Math.min(t * t, 1);  // clamp to maximum of 1.0 (100% penalty)
            }
            const power = basePower * (1 - penalty);  // effective speed: shrinks as penalty grows

            // --- Step 3: Split the power between horizontal and vertical ---
            // We use a "rebalanced" formula because simple sin/cos gives unfair
            // vertical advantage. Gravity makes horizontal travel harder, so we
            // compensate by boosting the horizontal component slightly.
            const aimX = Math.cos(player.aimAngle);  // cos of angle: 0 when aiming up, ±1 when sideways
            const aimY = Math.sin(player.aimAngle);  // sin of angle: -1 when aiming up, +1 when down
            const sideFrac = Math.abs(aimX);         // 0.0 = purely vertical, 1.0 = purely horizontal
            const upFrac = Math.abs(aimY);           // 1.0 = purely vertical, 0.0 = purely horizontal
            const signX = Math.sign(aimX) || 1;      // -1 for left, +1 for right (default +1 if exactly 0)
            const signY = aimY < 0 ? -1 : 1;         // -1 for upward, +1 for downward

            // Vertical speed: at least 25% of power, up to 100% when aiming straight up/down
            player.vy = signY * power * (0.25 + upFrac * 0.75);
            // Horizontal speed: scales with how sideways you aim, boosted by 0.68 factor
            player.vx = signX * power * sideFrac * 0.68;

            // --- Step 4: Update player state for being airborne ---
            player.grounded = false;     // no longer on a platform
            player.platform = null;      // not standing on anything
            player.charging = false;     // no longer charging
            spawnLaunchParticles(ratio, 1 - penalty);  // visual particle burst
            player.charge = 0;           // empty the charge bar
            player.holdTime = 0;         // reset the hold timer
        }
    }

    // ============================================================
    // PHYSICS — apply gravity and move the player
    // ============================================================
    player.vy += GRAVITY * dtc;          // gravity constantly pulls downward (increases vy)
    player.x += player.vx * dtc;         // move horizontally based on current vx
    player.y += player.vy * dtc;         // move vertically based on current vy

    // --- Screen walls: stop the player at the edges ---
    // Left wall: if the player's left edge is past x=0, push them back
    if (player.x < 0) { player.x = 0; player.vx = 0; }
    // Right wall: if the player's right edge is past x=800, push them back
    if (player.x + player.w > W) { player.x = W - player.w; player.vx = 0; }

    // ============================================================
    // COLLISION DETECTION — check the player against every platform
    // ============================================================
    player.grounded = false;             // assume airborne until a platform is found below
    player.platform = null;              // forget which platform we were on
    const footY = player.y + player.h;   // world Y coordinate of the player's feet

    for (const p of platforms) {         // check EVERY platform in the world
        if (p.isCrumble && p.fallen) continue;  // fallen crumble platforms don't exist anymore

        // Horizontal overlap check: do the player and platform overlap in X?
        // The player overlaps if their right edge > platform's left edge AND
        // their left edge < platform's right edge.
        const overlapX = player.x + player.w > p.x && player.x < p.x + p.w;
        if (!overlapX) continue;         // no horizontal overlap, skip this platform

        // ============================================================
        // TOP COLLISION — landing ON TOP of a platform
        // ============================================================
        // This checks if the player's feet passed through the platform's
        // top surface while moving downward.
        const prevFoot = footY - player.vy * dtc;  // where the feet were last frame
        if (prevFoot <= p.y + 5 && footY >= p.y - 2 && player.vy >= 0) {
            // YES — the player is landing on this platform!

            player.y = p.y - player.h;   // place player exactly on top of the platform
            player.vy = 0;               // stop falling
            player.vx = 0;               // stop any horizontal sliding
            player.grounded = true;      // mark as grounded
            player.platform = p;         // remember which platform we're standing on

            // --- Bounce pads: trampoline launch with decay ---
            if (p.isBounce) {
                player.bounceCount++;    // count this as another consecutive bounce
                // Each bounce is 72% as powerful as the previous one.
                // bounceCount=1: 100%. bounceCount=2: 72%. bounceCount=3: 52%. etc.
                const decay = Math.pow(0.72, player.bounceCount - 1);
                player.vy = -BOUNCE_POWER * decay;  // launch upward (negative = up)
                player.grounded = false;  // immediately airborne
                player.platform = null;   // not on a platform anymore
                spawnBounceParticles();   // green particle burst
            } else {
                // Landed on a non-bounce platform: reset the bounce counter
                player.bounceCount = 0;
            }

            // --- Head-landing stun: only from actual FALLS, not platform rotation ---
            // First, normalize the aim angle to the range -PI to +PI.
            // This handles the case where the player has spun multiple full rotations.
            let na = player.aimAngle % (Math.PI * 2);  // wrap to 0..2PI range
            if (na > Math.PI) na -= Math.PI * 2;       // shift to -PI..+PI range
            if (na < -Math.PI) na += Math.PI * 2;       // safety check

            // Calculate how far the player actually fell.
            // fallPeakY is the highest Y (smallest value) reached while airborne.
            // player.y is the current Y (landing point).
            // fallDist = how many pixels they dropped.
            const fallDist = player.fallPeakY > 0 ? player.y - player.fallPeakY : 0;

            // Trigger stun if ALL conditions are met:
            // 1. Not already stunned
            // 2. Fell more than 60 pixels (prevents stun from just rotating on a platform)
            // 3. Aiming within about 63 degrees of straight down (head-first landing)
            if (!player.stunned && fallDist > 60
                && Math.abs(na - Math.PI / 2) < Math.PI * 0.35) {
                player.stunned = true;   // begin stun
                // Stun duration scales with fall distance: 200px fall → 1 second stun.
                // Capped at 3 seconds maximum.
                player.stunTimer = Math.min(fallDist / 200, 3.0);
            }
            player.fallPeakY = 0;        // reset fall tracking (we've landed)

            // --- Start crumbling if this platform is the crumbling type ---
            if (p.isCrumble && !p.crumbling) {
                p.crumbling = true;      // begin the cracking process
                p.crumbleTimer = 0;      // start the countdown from zero
            }
        }

        // ============================================================
        // BOTTOM COLLISION — bonking head on the UNDERSIDE of solid platforms
        // ============================================================
        // Only applies to SOLID platforms (not one-way, not bounce pads).
        // One-way platforms let you pass through from below.
        if (player.vy < 0 && !p.oneway && !p.isBounce) {
            const headY = player.y;      // world Y of the player's head (top of collision box)
            const prevHead = headY - player.vy * dtc;  // where the head was last frame
            // Check if the head passed through the platform's BOTTOM edge while moving upward
            if (prevHead >= p.y + p.h - 2 && headY <= p.y + p.h + 2) {
                player.y = p.y + p.h;    // push the player down below the platform
                player.vy = 0;           // kill all upward momentum (bonk!)
                spawnBonkParticles();    // white spark burst at the head
            }
        }
    }

    // ============================================================
    // GOAL ZONE CHECK — entering the golden area at the top wins the level
    // ============================================================
    // Unlike regular platforms, the goal is an area: any overlap triggers
    // the win, the game pauses, and the level complete screen appears.
    for (const p of platforms) {
        if (p.type !== 'goal') continue;           // only check goal platforms
        // Check if the player's collision box overlaps the goal area at all
        if (player.x + player.w > p.x               // player right edge > goal left edge
            && player.x < p.x + p.w                 // player left edge < goal right edge
            && player.y + player.h > p.y            // player bottom > goal top
            && player.y < p.y + p.h) {              // player top < goal bottom
            won = true;                              // trigger the win!
            break;
        }
    }

    // ============================================================
    // AIR CONTROL — steer horizontally while airborne
    // ============================================================
    if (!player.grounded) {
        // Apply steering acceleration in the direction the player is pressing
        if (keys['ArrowLeft'] || keys['KeyA']) player.vx -= AIR_ACCEL * dtc;   // steer left
        if (keys['ArrowRight'] || keys['KeyD']) player.vx += AIR_ACCEL * dtc;  // steer right
        // Cap horizontal air speed to MAX_AIR_SPEED (190 px/s)
        player.vx = Math.max(-MAX_AIR_SPEED, Math.min(MAX_AIR_SPEED, player.vx));

        // --- Track the highest point reached during this flight ---
        // "Highest" means smallest Y value (Y increases downward).
        // This is used for calculating fall distance when the player lands.
        if (player.fallPeakY === 0 || player.y < player.fallPeakY) {
            player.fallPeakY = player.y;  // update peak to this new highest point
        }
    }

    // ============================================================
    // COIN COLLECTION — pick up coins by touching them
    // ============================================================
    for (const c of coins) {
        if (c.collected) continue;       // already picked up this coin, skip it
        const csy = c.y - camY;          // screen Y of the coin (skip if off-screen)
        if (csy < -20 || csy > H + 20) continue;

        // Calculate the distance between the player's center and the coin.
        // We use the Pythagorean theorem: distance² = dx² + dy².
        const dx = (player.x + player.w / 2) - c.x;   // horizontal distance
        const dy = (player.y + player.h / 2) - c.y;   // vertical distance
        // Check if the distance is less than 24 pixels (circular pickup radius)
        if (dx * dx + dy * dy < 24 * 24) {
            c.collected = true;          // mark this coin as collected
            score++;                     // increment the coin counter
        }
    }

    // ============================================================
    // DEATH — falling off the bottom of the world
    // ============================================================
    if (player.y > WORLD_H + 150) {      // 150 pixels below the world bottom
        spawnDeathParticles();           // red particle burst
        resetPlayer();                   // back to start position
        resetCamera();                   // camera back to ground level
    }

    // ============================================================
    // CAMERA — smoothly follow the player
    // ============================================================
    // We want the player to stay at about 40% from the top of the screen.
    // The camera uses "lerp" (linear interpolation) for smooth movement.
    const targetScreenY = H * 0.4;       // keep player at 40% from the top (240px down)
    const desiredCamY = player.y - targetScreenY;  // where the camera SHOULD be
    const lerpSpeed = 6;                 // how quickly the camera catches up (higher = snappier)
    // Move the camera a fraction of the way toward the desired position
    camY += (desiredCamY - camY) * Math.min(lerpSpeed * dtc, 1);
    // Clamp: never scroll past the world boundaries
    camY = Math.min(camY, GROUND_Y + 40 - H);   // don't go below the ground
    camY = Math.max(camY, -40);                  // don't go above the top of the world

    // ============================================================
    // PARTICLES — update all active particle effects
    // ============================================================
    // Loop backwards so we can safely remove particles while iterating.
    for (let i = particles.length - 1; i >= 0; i--) {
        const pt = particles[i];         // shorthand for the current particle
        pt.x += pt.vx * dtc;             // move particle horizontally
        pt.y += pt.vy * dtc;             // move particle vertically
        pt.vy += 300 * dtc;              // particles are affected by light gravity
        pt.life -= dtc;                  // reduce remaining life by elapsed time
        if (pt.life <= 0) {
            particles.splice(i, 1);      // remove dead particle from the array
        }
    }
}

// ============================================================
// PARTICLE SPAWNING FUNCTIONS
// ============================================================
// Each function creates a bunch of small colored squares that
// fly outward and fade away, giving visual feedback for events.

// Burst of particles when the player launches from their spring boots.
// The color changes based on charge level: grey for weak, gold for strong, red for overcharged.
function spawnLaunchParticles(ratio, penalty) {
    const p = penalty !== undefined ? penalty : 1;  // use penalty if provided, default 1 (no penalty)
    // More particles at higher charge: 8 minimum, up to 24 at full charge (scaled by penalty)
    const count = Math.floor(8 + ratio * 16 * p);
    const cx = player.x + player.w / 2;   // burst from the center of the player (X)
    const cy = player.y + player.h;       // burst from the player's feet (Y)
    for (let i = 0; i < count; i++) {
        const spread = 1.0;               // how wide the particle cone is (in radians)
        // Random angle within the spread cone, centered on the aim direction
        const angle = player.aimAngle + (Math.random() - 0.5) * spread;
        // Speed varies: 60 minimum, up to 320 at full charge
        const speed = 60 + Math.random() * 260 * (0.3 + ratio * 0.7) * p;
        particles.push({
            x: cx,                         // starting X position
            y: cy,                         // starting Y position
            vx: Math.cos(angle) * speed,   // horizontal velocity from the angle
            vy: Math.sin(angle) * speed,   // vertical velocity from the angle
            life: 0.25 + Math.random() * 0.5,  // particle lives 0.25 to 0.75 seconds
            // Color coding: red if heavily penalized, gold if strong, grey if weak
            color: p < 0.6 ? '#ff6644'
                : (ratio > 0.7 ? '#ffaa00' : '#cccccc'),
        });
    }
}

// Red particle burst when the player falls off the bottom of the world.
function spawnDeathParticles() {
    const cx = player.x + player.w / 2;   // center of player (X)
    const cy = player.y + player.h / 2;   // center of player (Y)
    for (let i = 0; i < 15; i++) {        // 15 particles
        particles.push({
            x: cx, y: cy,
            vx: (Math.random() - 0.5) * 200,   // random horizontal velocity (-100 to +100)
            vy: (Math.random() - 0.5) * 200,   // random vertical velocity (-100 to +100)
            life: 0.3 + Math.random() * 0.4,   // lives 0.3 to 0.7 seconds
            color: '#ff6666',                    // red
        });
    }
}

// Green particle burst when the player bounces on a bounce pad.
function spawnBounceParticles() {
    const cx = player.x + player.w / 2;   // center of player (X)
    const cy = player.y + player.h;       // player's feet (Y)
    for (let i = 0; i < 14; i++) {        // 14 particles
        // Mostly upward direction with some spread
        const angle = -Math.PI / 2 + (Math.random() - 0.5) * 1.5;
        const speed = 100 + Math.random() * 300;  // 100 to 400 px/s
        particles.push({
            x: cx, y: cy,
            vx: Math.cos(angle) * speed,
            vy: Math.sin(angle) * speed,
            life: 0.2 + Math.random() * 0.4,   // lives 0.2 to 0.6 seconds
            color: '#44ff44',                    // bright green
        });
    }
}

// White spark burst when the player's head hits the underside of a solid platform.
function spawnBonkParticles() {
    const cx = player.x + player.w / 2;   // center of player (X)
    const cy = player.y;                   // top of player (head, Y)
    for (let i = 0; i < 8; i++) {          // 8 sparks
        particles.push({
            x: cx, y: cy,
            vx: (Math.random() - 0.5) * 120,   // small horizontal spread
            vy: Math.random() * 60,             // gentle downward drift
            life: 0.15 + Math.random() * 0.25,  // short-lived: 0.15 to 0.4 seconds
            color: '#ffffff',                    // white
        });
    }
}

// Sad brown puff when the spring is held too long and gives out (auto-fizzle).
function spawnFizzleParticles() {
    const cx = player.x + player.w / 2;   // center of player (X)
    const cy = player.y + player.h;       // player's feet (Y)
    for (let i = 0; i < 20; i++) {        // 20 particles (bigger puff)
        // Wide spread, mostly upward-ish
        const angle = -Math.PI / 2 + (Math.random() - 0.5) * Math.PI;
        const speed = 30 + Math.random() * 80;   // low energy: 30 to 110 px/s
        particles.push({
            x: cx, y: cy,
            vx: Math.cos(angle) * speed,
            vy: Math.sin(angle) * speed,
            life: 0.3 + Math.random() * 0.6,   // lives 0.3 to 0.9 seconds
            color: i % 2 === 0 ? '#aa8855' : '#887744',  // alternating brown tones
        });
    }
}

// ============================================================
// TRAJECTORY ARC — dotted preview of where the launch will land
// ============================================================
// While holding SPACE, this draws a dotted parabola showing the
// predicted flight path based on current aim angle and charge level.
// A crosshair marks the landing spot — yellow if on a platform,
// white if in mid-air.

function drawTrajectoryArc() {
    // --- Calculate the SAME velocity the actual launch would use ---
    // This must match the launch code exactly, or the preview will be wrong.
    const ratio = player.charge / MAX_CHARGE;            // charge progress 0 to 1
    const basePower = MIN_LAUNCH + ratio * (MAX_LAUNCH - MIN_LAUNCH);  // base launch speed

    // Apply the same overcharge penalty formula
    let penalty = 0;
    if (player.holdTime > GRACE_TIME) {
        const t = (player.holdTime - GRACE_TIME) / OVERCHARGE_RAMP;
        penalty = Math.min(t * t, 1);                    // reverse-quadratic decay
    }
    const power = basePower * (1 - penalty);             // effective launch speed right now

    // Apply the same velocity split formula
    const aimX = Math.cos(player.aimAngle);              // horizontal component of aim direction
    const aimY = Math.sin(player.aimAngle);              // vertical component of aim direction
    const sideFrac = Math.abs(aimX);                     // how sideways the aim is (0 to 1)
    const upFrac = Math.abs(aimY);                       // how vertical the aim is (0 to 1)
    const signX = Math.sign(aimX) || 1;                  // direction: -1 left, +1 right
    const signY = aimY < 0 ? -1 : 1;                     // direction: -1 up, +1 down
    const vx = signX * power * sideFrac * 0.68;          // predicted horizontal launch speed
    const vy = signY * power * (0.25 + upFrac * 0.75);   // predicted vertical launch speed

    // The launch starts from the player's current position (center, at foot level)
    const startX = player.x + player.w / 2;              // world X of launch origin
    const startY = player.y + player.h;                  // world Y of launch origin (feet)

    // --- March through time, plotting a dot at each step ---
    const dt = 0.03;                 // time between dots (30 milliseconds = ~33 dots per second)
    const maxSteps = 120;            // safety limit: at most 120 dots (~3.6 seconds of flight)
    let landX = startX;              // predicted landing X (updated each step)
    let landY = startY;              // predicted landing Y (updated each step)
    let landed = false;              // true if the arc hit a platform

    ctx.fillStyle = 'rgba(255,255,255,0.35)';  // semi-transparent white for the dots

    for (let i = 0; i < maxSteps; i++) {
        const t = dt * i;            // elapsed time since "launch" at this step

        // Projectile motion formula: position at time t
        // x(t) = startX + vx * t
        const px = startX + vx * t;
        // y(t) = startY + vy * t + 0.5 * gravity * t²
        const py = startY + vy * t + 0.5 * GRAVITY * t * t;

        // Stop drawing if the arc goes off the left or right edge of the screen
        if (px < 0 || px > W) break;

        // Stop drawing if the arc falls below the visible area
        if (py - camY > H + 30) break;

        // --- Check if this trajectory point hits a platform ---
        let hitPlatform = false;     // did we find a platform at this point?
        for (const p of platforms) {
            if (p.isCrumble && p.fallen) continue;   // fallen crumble platforms are gone
            if (p.type === 'ground') continue;        // skip ground for arc landing prediction
            if (p === player.platform) continue;      // skip the platform we're standing on

            // Is the trajectory point horizontally within this platform?
            if (px >= p.x && px <= p.x + p.w) {
                // Is the trajectory point at or just below the platform's top surface?
                if (py >= p.y && py <= p.y + p.h + 8) {
                    landX = px;          // predicted landing X
                    landY = p.y;         // snap to the platform's top surface
                    landed = true;       // we found a landing spot!
                    hitPlatform = true;  // exit the platform loop
                    break;
                }
            }
        }
        if (hitPlatform) break;          // stop drawing the arc (we hit something)

        // Draw a small square dot at this trajectory point.
        // Convert from world coordinates to screen coordinates.
        const sx = px;                   // screen X (same as world X, no horizontal scrolling)
        const sy = py - camY;            // screen Y = world Y minus camera offset
        if (sy > 0 && sy < H) {
            ctx.fillRect(sx - 1.5, sy - 1.5, 3, 3);  // 3×3 pixel dot
        }

        landX = px;                      // update last known position
        landY = py;
    }

    // --- Draw the landing crosshair at the predicted spot ---
    const lsx = landX;                   // screen X of landing point
    const lsy = landY - camY;            // screen Y of landing point
    // Only draw the crosshair if it's on screen (not too close to edges)
    if (lsy > 10 && lsy < H - 10 && lsx > 15 && lsx < W - 15) {
        // Yellow crosshair = landing on a platform. White = landing in open air.
        ctx.strokeStyle = landed
            ? 'rgba(255,255,100,0.8)'    // bright yellow (safe landing)
            : 'rgba(255,255,255,0.5)';   // dim white (no platform below)
        ctx.lineWidth = 2;               // thicker lines for visibility

        // Draw a circle (radius 8 pixels) at the landing spot
        ctx.beginPath();
        ctx.arc(lsx, lsy, 8, 0, Math.PI * 2);  // full circle (0 to 2π radians)
        ctx.stroke();

        // Draw crosshair lines: horizontal and vertical through the circle center
        ctx.beginPath();
        ctx.moveTo(lsx - 12, lsy);       // left end of horizontal line
        ctx.lineTo(lsx + 12, lsy);       // right end of horizontal line
        ctx.moveTo(lsx, lsy - 12);       // top end of vertical line
        ctx.lineTo(lsx, lsy + 12);       // bottom end of vertical line
        ctx.stroke();

        ctx.lineWidth = 1;               // reset line width for other drawings
    }
}

// ============================================================
// DRAWING FUNCTIONS — render everything to the canvas
// ============================================================

// Draw the zigzag spring coil between the character's body and the boot soles.
// sx: screen X of the character's left edge
// baseY: screen Y of the top of the spring (where it meets the belt)
// w: width of the character (for coil width)
// compress: 0.0 = fully extended, 1.0 = fully compressed
// Returns the actual height the spring was drawn (varies with compression).
function drawSpring(sx, baseY, w, compress) {
    const coils = 5;                     // number of zigzag segments (more = tighter coil)
    // Spring height: 16 pixels when extended, shrinks to 6.4 pixels when fully compressed
    const h = 16 * (1 - compress * 0.6);
    const left = sx + 5;                 // left edge of the zigzag pattern
    const right = sx + w - 5;            // right edge of the zigzag pattern

    // --- Shadow: offset 1 pixel down-right, darker version of the coil ---
    ctx.strokeStyle = 'rgba(0,0,0,0.3)'; // semi-transparent black
    ctx.lineWidth = 3;                   // thick line
    ctx.beginPath();                     // start a new path (a series of connected lines)
    for (let i = 0; i <= coils; i++) {
        const t = i / coils;             // progress from 0.0 (top) to 1.0 (bottom)
        const cy = baseY + t * h;        // Y position of this point on the coil
        // Alternate between left and right for the zigzag pattern
        const cx = i % 2 === 0 ? left : right;
        if (i === 0) ctx.moveTo(cx + 1, cy + 1);   // first point: move pen here (offset for shadow)
        else ctx.lineTo(cx + 1, cy + 1);            // subsequent points: draw line to here
    }
    ctx.stroke();                        // actually draw the path we built

    // --- Main coil: metallic gradient with rounded corners ---
    // Create a vertical gradient from light metal to dark to medium
    const grad = ctx.createLinearGradient(0, baseY, 0, baseY + h);
    grad.addColorStop(0, '#d8d8d8');     // light silver at the top
    grad.addColorStop(0.5, '#888');      // dark grey in the middle
    grad.addColorStop(1, '#aaa');        // medium grey at the bottom
    ctx.strokeStyle = grad;              // use the gradient as the line color
    ctx.lineWidth = 3;                   // thick line
    ctx.lineCap = 'round';               // rounded line ends (looks more like a coil)
    ctx.lineJoin = 'round';              // rounded corners where lines meet
    ctx.beginPath();                     // start a new path
    for (let i = 0; i <= coils; i++) {
        const t = i / coils;             // progress from top to bottom
        const cy = baseY + t * h;        // Y position
        const cx = i % 2 === 0 ? left : right;  // alternate left/right for zigzag
        if (i === 0) ctx.moveTo(cx, cy); // first point
        else ctx.lineTo(cx, cy);         // draw to each subsequent point
    }
    ctx.stroke();                        // render the coil

    // Reset drawing settings to defaults for other draw calls
    ctx.lineCap = 'butt';                // default: flat line ends
    ctx.lineJoin = 'miter';              // default: sharp corners
    ctx.lineWidth = 1;                   // default: thin lines

    return h;                            // tell the caller how tall the spring ended up
}

// Draw the complete player character: body, head, goggles, spring boots, soles, charge bar.
function drawPlayer() {
    // --- Convert player's world position to screen position ---
    const sx = player.x;                 // screen X = world X (no horizontal camera movement)
    const sy = player.y - camY;          // screen Y = world Y minus camera offset
    // Charge ratio: 0.0 = not charging, 1.0 = fully charged
    const cRatio = player.charging ? player.charge / MAX_CHARGE : 0;

    // --- Calculate body dimensions (squishes when charging) ---
    const bodySquish = 1 - cRatio * 0.12;           // 1.0 normally, 0.88 when fully charged
    const bodyH = (player.h - 8) * bodySquish;       // body height in pixels (28px normally, ~25px charged)
    // Note: player.h is 36. Subtracting 8 accounts for head space.

    // --- Spring geometry: soles stay on the ground, spring compresses UPWARD ---
    // This means when you charge, your body presses DOWN into the spring.
    // The soles (boot bottoms) stay fixed on the platform surface.
    const FULL_SPRING = 16;                          // uncompressed spring height in pixels
    const springH = FULL_SPRING * (1 - cRatio * 0.6); // compressed spring height (16 → 6.4)
    const soleY = sy + player.h;                     // soles at collision bottom (platform surface)
    const pivotX = sx + player.w / 2;                // belt X = center of the character
    const pivotY = soleY - springH;                  // belt Y = soles minus spring height
    // When charging: springH shrinks → pivotY moves DOWN (closer to soles)
    // This makes the body look like it's pressing down on the springs.

    // --- Rotation angle: body leans to face the aim direction ---
    // rotAngle = 0 means body points straight UP (normal standing)
    // rotAngle = PI/2 means body points RIGHT (leaning right)
    // rotAngle = PI means body points DOWN (upside down!)
    const rotAngle = player.aimAngle + Math.PI / 2;

    // --- Spring shake during overcharge ---
    // Between 3 and 6 seconds of holding, the spring vibrates chaotically.
    let shakeX = 0;                      // horizontal shake offset in pixels
    const isOvercharging = player.charging && player.holdTime > GRACE_TIME;
    if (isOvercharging) {
        // t goes from 0 at GRACE_TIME to 1 at FAIL_TIME
        const t = (player.holdTime - GRACE_TIME) / OVERCHARGE_RAMP;
        const amp = t * t * 10;          // amplitude grows quadratically: 0 → 10 pixels
        const ht = player.holdTime;      // use holdTime for the sine wave input
        // Three overlapping sine waves at different frequencies for chaotic jitter
        shakeX = Math.sin(ht * 47) * amp           // fast jitter
               + Math.sin(ht * 73) * amp * 0.6     // medium jitter (60% strength)
               + Math.sin(ht * 19) * amp * 0.4;    // slow wobble (40% strength)
    }

    // --- Draw the spring coil (always vertical, below the belt pivot) ---
    // The shakeX offset makes it vibrate during overcharge.
    drawSpring(sx + shakeX, pivotY, player.w, cRatio);

    // --- Draw the boot soles (rubber bottoms of the boots) ---
    ctx.fillStyle = '#3a3a3a';           // dark grey rubber
    // Soles are slightly wider than the body, at the soleY position
    ctx.fillRect(sx - 2 + shakeX, soleY - 1, player.w + 4, 5);  // main sole
    ctx.fillStyle = '#555';              // lighter grey for tread detail
    ctx.fillRect(sx - 1 + shakeX, soleY - 1, player.w + 2, 2);  // tread highlight

    // --- Draw the ROTATED body and head ---
    // We save the current drawing state, translate to the belt pivot,
    // rotate, draw the body, then restore. This makes the body lean.
    ctx.save();                          // save current transform state
    ctx.translate(pivotX, pivotY);       // move origin to the belt (where body meets spring)
    ctx.rotate(rotAngle);                // rotate so "up" points in the aim direction

    // -- Torso: a blue rectangle with rounded corners --
    // The gradient goes from lighter blue (shoulders/top) to darker blue (belt/bottom).
    const bodyGrad = ctx.createLinearGradient(0, -bodyH, 0, 0);
    bodyGrad.addColorStop(0, '#5599ff'); // lighter blue at the top of the body
    bodyGrad.addColorStop(1, '#3366cc'); // darker blue at the belt
    ctx.fillStyle = bodyGrad;
    // body extends from -bodyH (above pivot) to 0 (at pivot)
    roundRect(-player.w / 2, -bodyH, player.w, bodyH, 5);  // 5px corner radius
    ctx.fill();                          // fill the rounded rectangle

    // -- Belt: a brown strap with a gold buckle at the pivot point --
    ctx.fillStyle = '#7a5c20';           // dark brown leather
    ctx.fillRect(-player.w / 2, -3, player.w, 4);  // strap across the full width
    ctx.fillStyle = '#c9a030';           // gold color
    ctx.fillRect(-4, -3, 8, 4);          // buckle in the center (8px wide)

    // -- Head: a skin-colored circle above the body --
    const headR = 9;                     // head radius in pixels
    const headCY = -bodyH - headR + 2;   // Y center of the head (above the body)
    ctx.fillStyle = '#ffcc99';           // skin color
    ctx.beginPath();                     // start a new shape
    ctx.arc(0, headCY, headR, 0, Math.PI * 2);  // full circle centered at (0, headCY)
    ctx.fill();                          // fill the circle

    // -- Eyes: two dark circles with white shine dots --
    const eyeY = headCY - 1;             // eyes are 1 pixel above head center
    ctx.fillStyle = '#222';              // near-black for the pupils
    ctx.beginPath();
    ctx.arc(-3, eyeY, 2, 0, Math.PI * 2);   // left eye (3px left of center, 2px radius)
    ctx.arc(4, eyeY, 2, 0, Math.PI * 2);    // right eye (4px right of center, 2px radius)
    ctx.fill();
    ctx.fillStyle = '#fff';              // white for the shine/reflection
    ctx.beginPath();
    ctx.arc(-2, eyeY - 0.8, 0.7, 0, Math.PI * 2);  // left eye shine
    ctx.arc(5, eyeY - 0.8, 0.7, 0, Math.PI * 2);   // right eye shine
    ctx.fill();

    // -- Goggles: dark grey rings around the eyes with a bridge --
    ctx.strokeStyle = '#555';            // dark grey
    ctx.lineWidth = 1.5;                 // slightly thicker than default
    ctx.beginPath();
    ctx.arc(-3, eyeY, 5.5, 0, Math.PI * 2);   // left goggle ring (5.5px radius)
    ctx.arc(4, eyeY, 5.5, 0, Math.PI * 2);    // right goggle ring
    ctx.stroke();                        // draw the outlines
    // Bridge: a short line connecting the two goggles
    ctx.beginPath();
    ctx.moveTo(2, eyeY);                 // inner edge of right goggle
    ctx.lineTo(-1, eyeY);                // inner edge of left goggle
    ctx.stroke();
    ctx.lineWidth = 1;                   // reset to default line width

    ctx.restore();                       // restore the transform (stop rotating)

    // --- Stunned stars: three rotating ★ symbols above the head ---
    if (player.stunned) {
        const starX = pivotX;            // roughly where the head is horizontally
        const starY = pivotY - bodyH - 14;  // above the head
        const t = performance.now() * 0.008;  // time-based rotation (slow)
        const colors = ['#ffff88', '#ffdd44', '#ffaa00'];  // three shades of yellow/gold
        ctx.font = '11px monospace';
        ctx.textAlign = 'center';        // center text at the given X position
        for (let i = 0; i < 3; i++) {
            const a = t + i * Math.PI * 2 / 3;   // each star is 120° apart
            const sx = starX + Math.cos(a) * 11;  // orbit radius 11px (horizontal)
            const sy = starY + Math.sin(a) * 7;   // orbit radius 7px (vertical, elliptical)
            ctx.fillStyle = colors[i];    // pick this star's color
            ctx.fillText('★', sx, sy);    // draw the star character
        }
        ctx.textAlign = 'start';          // reset text alignment
    }

    // --- Charge bar: shows above the player while holding SPACE ---
    if (player.charging) {
        const bw = 44;                   // bar width in pixels
        const bh = 6;                    // bar height in pixels
        const bx = sx + player.w / 2 - bw / 2;  // center the bar above the player
        const by = sy - 16;              // 16 pixels above the player's top edge
        // Dark background behind the bar
        ctx.fillStyle = '#1a1a1a';       // nearly black
        ctx.fillRect(bx - 1, by - 1, bw + 2, bh + 2);  // 1px border all around

        const isMaxed = cRatio >= 0.98;  // is the charge bar essentially full?
        const inGrace = isMaxed && player.holdTime <= GRACE_TIME;  // in the grace period?

        if (isOvercharging) {
            // --- Overcharging (3s-6s): RED shrinking bar ---
            // The bar visually shrinks as the quadratic penalty increases.
            const t = (player.holdTime - GRACE_TIME) / OVERCHARGE_RAMP;
            const qPenalty = Math.min(t * t, 1);  // 0 at 3s, 1 at 6s (quadratic)
            const remaining = bw * (1 - qPenalty); // bar width shrinks as penalty grows
            // Red gradient: bright red → dark red
            const cg = ctx.createLinearGradient(bx, 0, bx + remaining, 0);
            cg.addColorStop(0, '#ff2200');   // bright red at left
            cg.addColorStop(1, '#880000');   // dark red at right
            ctx.fillStyle = cg;
            ctx.fillRect(bx, by, remaining, bh);  // draw the shrinking bar
        } else if (inGrace) {
            // --- Grace period (0.7s-3s): full GOLD bar with pulsing glow ---
            const pulse = 0.7 + 0.3 * Math.sin(performance.now() * 0.008);
            // Gold gradient
            const cg = ctx.createLinearGradient(bx, 0, bx + bw, 0);
            cg.addColorStop(0, '#ffcc00');   // light gold
            cg.addColorStop(0.5, '#ffd700'); // pure gold at center
            cg.addColorStop(1, '#ffaa00');   // darker gold
            ctx.fillStyle = cg;
            ctx.fillRect(bx, by, bw, bh);    // full-width gold bar
            // Outer glow: semi-transparent gold rectangle behind the bar
            ctx.fillStyle = `rgba(255,215,0,${0.15 + pulse * 0.2})`;
            ctx.fillRect(bx - 2, by - 2, bw + 4, bh + 4);
            ctx.fillStyle = cg;              // redraw bar on top of glow
            ctx.fillRect(bx, by, bw, bh);
        } else {
            // --- Charging (0s-0.7s): ORANGE fill bar growing to full width ---
            const cg = ctx.createLinearGradient(bx, 0, bx + bw, 0);
            cg.addColorStop(0, '#ff5500');   // bright orange
            cg.addColorStop(0.6, '#ff9900'); // warm orange
            cg.addColorStop(1, '#ff3300');   // red-orange
            ctx.fillStyle = cg;
            ctx.fillRect(bx, by, bw * cRatio, bh);  // width = charge percentage
        }
    }
}

// Helper: create a rounded rectangle path (must call ctx.fill() after this).
// x, y = top-left corner. w, h = width and height. r = corner radius in pixels.
function roundRect(x, y, w, h, r) {
    ctx.beginPath();                     // start a new shape
    ctx.moveTo(x + r, y);                // start at the top edge, after the top-left curve
    ctx.lineTo(x + w - r, y);            // top edge (straight line)
    ctx.arcTo(x + w, y, x + w, y + r, r);  // top-right rounded corner
    ctx.lineTo(x + w, y + h - r);        // right edge (straight down)
    ctx.arcTo(x + w, y + h, x + w - r, y + h, r);  // bottom-right rounded corner
    ctx.lineTo(x + r, y + h);            // bottom edge (straight left)
    ctx.arcTo(x, y + h, x, y + h - r, r);  // bottom-left rounded corner
    ctx.lineTo(x, y + r);                // left edge (straight up)
    ctx.arcTo(x, y, x + r, y, r);        // top-left rounded corner
    ctx.closePath();                     // connect back to the starting point
}

// Main draw function: renders the complete frame every ~16ms (60fps).
function draw() {
    // ============================================================
    // BACKGROUND: vertical sky gradient from dark blue to dark green
    // ============================================================
    const sg = ctx.createLinearGradient(0, 0, 0, H);  // vertical gradient
    sg.addColorStop(0, '#0a0a2e');       // deep dark blue at the very top
    sg.addColorStop(0.35, '#16164a');    // slightly lighter blue
    sg.addColorStop(0.65, '#252555');    // purplish transition
    sg.addColorStop(1, '#182a20');       // dark green at the bottom (ground glow)
    ctx.fillStyle = sg;
    ctx.fillRect(0, 0, W, H);            // fill entire canvas with the gradient

    // ============================================================
    // STARS: 90 tiny twinkling dots at fixed world positions
    // ============================================================
    ctx.fillStyle = '#ffffff';           // white stars
    for (let i = 0; i < 90; i++) {
        // Deterministic position: uses prime numbers as seeds so stars
        // always appear in the same place relative to the world.
        const sx = ((i * 137 + 50) % W);             // X position (0 to 799)
        const sy = ((i * 251 + 30) % WORLD_H) - camY; // world Y → screen Y
        if (sy < -5 || sy > H + 5) continue;          // skip if off-screen
        // Twinkle effect: brightness oscillates over time.
        // Each star has a unique phase (from i*73) and oscillates with sin().
        const twinkle = 0.25 + 0.75
            * Math.abs(Math.sin((i * 73 + performance.now() * 0.001) * 0.5));
        ctx.globalAlpha = twinkle * 0.85;  // vary opacity to create twinkling
        // Three star sizes: large (every 7th), medium (every 4th), small (rest)
        const sz = (i % 7 === 0) ? 2 : (i % 4 === 0 ? 1.4 : 0.8);
        ctx.fillRect(sx, sy, sz, sz);    // draw the star as a tiny square
    }
    ctx.globalAlpha = 1;                 // reset alpha to fully opaque

    // ============================================================
    // WALLS: dark gradient bars on the left and right edges
    // ============================================================
    const wallW = 14;                    // wall thickness in pixels
    const wallTop = -camY;               // screen Y of the top of the walls
    const wallBot = wallTop + WORLD_H;   // screen Y of the bottom of the walls
    // Left wall: gradient from darker (outer edge) to lighter (inner edge)
    const wallGradL = ctx.createLinearGradient(0, 0, wallW, 0);
    wallGradL.addColorStop(0, '#2a2a3a');    // darker at outer edge
    wallGradL.addColorStop(1, '#3a3a4a');    // lighter at inner edge
    ctx.fillStyle = wallGradL;
    ctx.fillRect(0, wallTop, wallW, wallBot - wallTop);
    // Right wall: gradient from lighter (inner edge) to darker (outer edge)
    const wallGradR = ctx.createLinearGradient(W - wallW, 0, W, 0);
    wallGradR.addColorStop(0, '#3a3a4a');    // lighter at inner edge
    wallGradR.addColorStop(1, '#2a2a3a');    // darker at outer edge
    ctx.fillStyle = wallGradR;
    ctx.fillRect(W - wallW, wallTop, wallW, wallBot - wallTop);
    // Thin highlight lines at the inner edge of each wall (subtle 3D effect)
    ctx.fillStyle = 'rgba(255,255,255,0.06)';  // very faint white
    ctx.fillRect(wallW, wallTop, 2, wallBot - wallTop);          // left wall highlight
    ctx.fillRect(W - wallW - 2, wallTop, 2, wallBot - wallTop);  // right wall highlight

    // ============================================================
    // PLATFORMS — draw all platforms with their modifier visuals
    // ============================================================
    for (const p of platforms) {
        const sy = p.y - camY;           // screen Y of the platform's top surface
        if (sy + p.h < -10 || sy > H + 10) continue;  // cull: skip if completely off-screen
        // Also skip fallen crumble platforms that are far below the screen
        if (p.isCrumble && p.fallen && sy > H + 50) continue;

        // --- Platform body: combo platforms get split into colored segments ---
        const comboCount = (p.isMoving ? 1 : 0)      // count how many modifier types
                         + (p.isCrumble ? 1 : 0)      // this platform has
                         + (p.isBounce ? 1 : 0);
        if (comboCount >= 2) {
            // Multi-modifier platform: draw it with split vertical segments
            const parts = [];            // collect the colors for each segment
            if (p.isMoving) parts.push('#c94040');   // red for moving
            if (p.isCrumble) parts.push('#b89860');  // tan for crumbling
            if (p.isBounce) parts.push('#44cc44');   // green for bounce
            const pw = p.w / parts.length;           // width of each segment
            for (let k = 0; k < parts.length; k++) {
                ctx.fillStyle = parts[k];            // use this segment's color
                ctx.fillRect(p.x + k * pw, sy, pw + 1, p.h);  // draw the segment
            }
        } else {
            // Single-modifier or plain platform: one solid color
            ctx.fillStyle = p.color;
            ctx.fillRect(p.x, sy, p.w, p.h);  // draw the full rectangle
        }

        const iconY = sy + 10;           // vertical center for drawing modifier icons

        // --- Crumbling platform: jagged top edge + ⚠ warning icon ---
        if (p.isCrumble) {
            ctx.fillStyle = '#8b6914';   // dark brown for the jagged edge
            // Draw staggered blocks along the top to look like a cracked surface
            for (let cx = p.x; cx < p.x + p.w; cx += 7) {
                ctx.fillRect(cx, sy - 2, 5, 2);      // upper blocks
                ctx.fillRect(cx + 2, sy - 1, 3, 1);  // lower staggered blocks
            }
            ctx.fillStyle = '#fff';      // white icon text
            ctx.font = 'bold 10px monospace';
            ctx.textAlign = 'center';    // center the text horizontally
            ctx.fillText('⚠', p.x + p.w / 2, iconY);  // warning triangle
            ctx.textAlign = 'start';     // reset text alignment
        }

        // --- Bounce pad: spring-coil squiggle along the top + ⌃ icon ---
        if (p.isBounce) {
            ctx.strokeStyle = '#fff';    // white squiggle line
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            const bw = Math.min(p.w - 6, 50);           // squiggle width (max 50px)
            const bx = p.x + (p.w - bw) / 2;             // center the squiggle
            for (let i = 0; i <= 8; i++) {
                const t = i / 8;                         // 0.0 to 1.0 along the squiggle
                const cx = bx + t * bw;                  // X position
                const cy = sy - 1 + (i % 2 === 0 ? -3 : 3);  // up-down wave pattern
                if (i === 0) ctx.moveTo(cx, cy);         // first point
                else ctx.lineTo(cx, cy);                  // connect to previous
            }
            ctx.stroke();                // draw the squiggle
            ctx.lineWidth = 1;           // reset line width
            ctx.fillStyle = '#fff';
            ctx.font = 'bold 10px monospace';
            ctx.textAlign = 'center';
            ctx.fillText('⌃', p.x + p.w / 2, iconY);     // upward spring icon
            ctx.textAlign = 'start';
        }

        // --- Moving platform: motion blur lines, or pause brackets when stopped ---
        if (p.isMoving) {
            if (p.paused) {
                // Paused at an endpoint: show solid brackets like [===]
                ctx.fillStyle = 'rgba(255,255,255,0.7)';
                ctx.fillRect(p.x + 2, sy + 2, 3, p.h - 4);           // left bracket
                ctx.fillRect(p.x + p.w - 5, sy + 2, 3, p.h - 4);     // right bracket
                ctx.fillStyle = '#fff';
                ctx.font = 'bold 10px monospace';
                ctx.textAlign = 'center';
                ctx.fillText('⏸', p.x + p.w / 2, iconY);              // pause icon
                ctx.textAlign = 'start';
            } else {
                // Moving: show motion blur lines on both sides
                ctx.fillStyle = 'rgba(255,255,255,0.4)';
                for (let i = 0; i < 3; i++) {
                    ctx.fillRect(p.x + 2 + i * 5, sy + 2, 2, p.h - 4);       // left motion lines
                    ctx.fillRect(p.x + p.w - 4 - i * 5, sy + 2, 2, p.h - 4); // right motion lines
                }
                ctx.fillStyle = '#fff';
                ctx.font = 'bold 10px monospace';
                ctx.textAlign = 'center';
                ctx.fillText('⟷', p.x + p.w / 2, iconY);              // horizontal arrows icon
                ctx.textAlign = 'start';
            }
        }

        // --- One-way platform: dashed top line + small up-arrows ---
        // Only shown on pure one-way platforms (not combos with other visual types)
        if (p.oneway && !p.isCrumble && !p.isBounce && !p.isMoving) {
            // Dashed line along the top surface
            ctx.fillStyle = 'rgba(255,255,255,0.5)';
            for (let cx = p.x + 3; cx < p.x + p.w - 6; cx += 10) {
                ctx.fillRect(cx, sy, 5, 1);  // 5px dash, 5px gap
            }
            // Up-arrow pattern
            ctx.fillStyle = 'rgba(255,255,255,0.35)';
            ctx.font = '9px monospace';
            ctx.textAlign = 'center';
            ctx.fillText('△ △ △', p.x + p.w / 2, iconY);  // three up triangles
            ctx.textAlign = 'start';
        }

        // --- Highlight: thin light line along the top edge (3D effect) ---
        if (!p.isCrumble) {
            ctx.fillStyle = 'rgba(255,255,255,0.1)';  // very faint white
            ctx.fillRect(p.x, sy, p.w, 3);             // 3px highlight strip
        }

        // --- Shadow: thin dark line along the bottom edge (3D effect) ---
        if (!(p.isCrumble && p.fallen)) {
            ctx.fillStyle = 'rgba(0,0,0,0.2)';         // semi-transparent black
            ctx.fillRect(p.x, sy + p.h - 2, p.w, 2);   // 2px shadow strip
        }

        // --- Crumbling cracks: grow and spread as the timer counts down ---
        if (p.isCrumble && p.crumbling && !p.fallen) {
            const prog = p.crumbleTimer / CRUMBLE_TIME;  // 0.0 (just started) to 1.0 (about to fall)
            // The platform shakes more as it gets closer to breaking
            const shake = Math.sin(performance.now() * 0.05) * prog * 3;
            ctx.strokeStyle = '#3a1a0a';   // very dark brown for the cracks
            ctx.lineWidth = 1.5;            // slightly thicker lines
            for (let c = 0; c < 3; c++) {   // three crack patterns across the platform
                const cx = p.x + p.w * (0.2 + c * 0.25) + shake;  // crack X position
                // First crack: spreads downward-left as prog increases
                ctx.beginPath();
                ctx.moveTo(cx, sy);                      // start at top surface
                ctx.lineTo(cx + 8 - prog * 4, sy + p.h); // spread to bottom
                ctx.stroke();
                // Second crack: spreads downward-right
                ctx.beginPath();
                ctx.moveTo(cx - 4, sy);
                ctx.lineTo(cx - 12 + prog * 6, sy + p.h);
                ctx.stroke();
            }
            ctx.lineWidth = 1;             // reset line width
        }

        // --- Goal zone: large golden area with pulsing border ---
        if (p.type === 'goal') {
            // Pulsing outer glow
            const glow = 0.2 + 0.15 * Math.sin(performance.now() * 0.003);
            ctx.fillStyle = `rgba(255, 215, 0, ${glow})`;
            ctx.fillRect(p.x - 6, sy - 4, p.w + 12, p.h + 8);   // outer glow
            // Semi-transparent golden fill (see-through, zone-like)
            ctx.fillStyle = 'rgba(255, 215, 0, 0.15)';
            ctx.fillRect(p.x, sy, p.w, p.h);
            // Dashed border to show it's a zone, not a solid platform
            ctx.strokeStyle = 'rgba(255, 215, 0, 0.8)';
            ctx.lineWidth = 2;
            ctx.setLineDash([8, 4]);                               // dashed line: 8px on, 4px off
            ctx.strokeRect(p.x + 1, sy + 1, p.w - 2, p.h - 2);    // dashed border
            ctx.setLineDash([]);                                   // reset to solid lines
            ctx.lineWidth = 1;
            // "★ GOAL ★" label in the center of the zone
            ctx.fillStyle = '#fff';
            ctx.font = 'bold 16px monospace';
            ctx.textAlign = 'center';
            const goalCY = sy + p.h / 2 + 6;                       // vertically centered
            ctx.fillText('★ GOAL ★', p.x + p.w / 2, goalCY);
            ctx.textAlign = 'start';
        }
    }

    // ============================================================
    // COINS — spinning gold diamonds that float gently up and down
    // ============================================================
    for (const c of coins) {
        if (c.collected) continue;       // don't draw already-collected coins
        const csy = c.y - camY;          // screen Y of the coin
        if (csy < -10 || csy > H + 10) continue;  // skip off-screen coins

        // Gentle bobbing motion: coin floats up and down by ±3 pixels
        const bob = Math.sin(performance.now() * 0.003 + c.x * 0.01) * 3;
        const cx = c.x;                  // screen X (same as world X)
        const cy = csy + bob;            // screen Y with bobbing offset
        const r = 7;                     // diamond radius (half-width)

        // Fake 3D rotation: we squish the X axis sinusoidally to make the
        // diamond appear to spin. When sx=1.0 it faces us, when sx=0.6 it's edge-on.
        const t = performance.now() * 0.004;  // slow time-based rotation
        const sx = Math.abs(Math.cos(t)) * 0.4 + 0.6;  // 0.6 to 1.0, oscillating

        ctx.save();                      // save drawing state
        ctx.translate(cx, cy);           // move origin to coin center
        ctx.scale(sx, 1);                // squish horizontally to simulate 3D spin

        // Outer diamond (gold)
        ctx.fillStyle = '#ffd700';       // bright gold
        ctx.beginPath();
        ctx.moveTo(0, -r);               // top point
        ctx.lineTo(r, 0);                // right point
        ctx.lineTo(0, r);                // bottom point
        ctx.lineTo(-r, 0);               // left point
        ctx.closePath();                 // back to top
        ctx.fill();

        // Inner diamond (lighter gold for depth/shine)
        ctx.fillStyle = '#ffee88';       // pale gold
        ctx.beginPath();
        ctx.moveTo(0, -r + 3);           // slightly smaller diamond
        ctx.lineTo(r - 3, 0);
        ctx.lineTo(0, r - 3);
        ctx.lineTo(-r + 3, 0);
        ctx.closePath();
        ctx.fill();

        ctx.restore();                   // restore drawing state
    }

    // ============================================================
    // PARTICLES — draw all active particle effects
    // ============================================================
    for (const pt of particles) {
        // Particles fade out as their life decreases
        ctx.globalAlpha = Math.max(0, pt.life * 2.5);  // 0 = fully transparent, 1 = fully opaque
        ctx.fillStyle = pt.color;        // this particle's color
        // Particles shrink as they age (larger when fresh, smaller when old)
        const s = 2 + pt.life * 3;       // size in pixels: 2px minimum, up to ~5px
        // Draw the particle as a small square, centered on its position
        ctx.fillRect(pt.x - s / 2, pt.y - camY - s / 2, s, s);
    }
    ctx.globalAlpha = 1;                 // reset alpha to fully opaque

    // ============================================================
    // TRAJECTORY ARC — show predicted flight path while charging
    // ============================================================
    if (player.charging) {
        drawTrajectoryArc();             // draw the dotted arc and landing crosshair
    }

    // ============================================================
    // PLAYER — draw the character on top of everything else
    // ============================================================
    drawPlayer();

    // ============================================================
    // HUD (Heads-Up Display) — info bar at the top of the screen
    // ============================================================
    ctx.fillStyle = 'rgba(0,0,0,0.45)';  // semi-transparent black background
    ctx.fillRect(0, 0, W, 56);           // 56 pixels tall (two rows)

    // --- Height climbed (converted to meters: 10px = 1 meter) ---
    ctx.fillStyle = '#fff';              // white text
    ctx.font = 'bold 15px monospace';
    const heightM = Math.max(0, Math.floor((GROUND_Y - player.y - player.h) / 10));
    ctx.fillText(`⬆ ${heightM}m`, 14, 24);  // e.g., "⬆ 42m"

    // --- Current level number ---
    ctx.font = '12px monospace';
    ctx.fillText(`Lv${currentLevel}`, 14, 49);  // e.g., "Lv3"

    // --- Grounded/Airborne status ---
    ctx.fillText(player.grounded ? '● Ready' : '○ Airborne', 130, 24);

    // --- Coin counter (gold colored) ---
    ctx.fillStyle = '#ffd700';           // gold
    ctx.fillText(`🪙 ${score}`, 420, 24);  // e.g., "🪙 12"

    // --- Aim direction indicator (compass) ---
    // Normalize the aim angle to 0-360 degrees
    let deg = Math.round(((player.aimAngle % (Math.PI * 2))
        + Math.PI * 2) % (Math.PI * 2) * (180 / Math.PI));
    // Map the angle to one of 8 compass directions (45° each)
    const dirs = ['↑', '↗', '→', '↘', '↓', '↙', '←', '↖'];
    const dirLabel = dirs[Math.round(deg / 45) % 8];  // pick the right arrow
    ctx.fillStyle = '#fff';
    ctx.fillText(`Aim: ${dirLabel}`, 310, 24);  // e.g., "Aim: ↗"

    // --- Platform modifier legend (color swatches with labels) ---
    const legY = 40;                     // Y position of the legend row
    const legColors = ['#c94040', '#b89860', '#44cc44', '#6b8e8e'];  // red, tan, green, teal
    const legIcons = ['⟷move', '⚠crumble', '⌃bounce', '△1way'];     // labels
    const legX = 400;                    // starting X position
    ctx.font = '10px monospace';
    for (let i = 0; i < legColors.length; i++) {
        const lx = legX + i * 92;        // 92px between each legend item
        ctx.fillStyle = legColors[i];    // use the modifier's color
        ctx.fillRect(lx, legY, 10, 5);   // draw a small color swatch (10×5px)
        ctx.fillStyle = '#ccc';          // light grey for the label text
        ctx.fillText(legIcons[i], lx + 13, legY + 5);  // label next to swatch
    }

    // ============================================================
    // TUTORIAL MESSAGE — floating popup explaining new modifier types
    // ============================================================
    if (tutorialMsg && tutorialTimer < 8) {   // show for 8 seconds total
        const msgY = tutorialMsg.y - camY;     // screen Y of the platform the message is about
        if (msgY > 30 && msgY < H - 30) {      // only draw if the platform is on screen
            // Fade in over 1 second, hold for 5 seconds, fade out over 2 seconds
            const alpha = tutorialTimer < 1 ? tutorialTimer          // 0→1 over first second
                : (tutorialTimer > 6 ? Math.max(0, (8 - tutorialTimer) / 2) : 1);  // 1→0 over last 2s
            // Dark background pill behind the text
            ctx.fillStyle = `rgba(0,0,0,${0.7 * alpha})`;  // semi-transparent black
            ctx.font = 'bold 13px monospace';
            const tw = ctx.measureText(tutorialMsg.text).width;  // measure text width
            const mw = tw + 24;            // add 12px padding on each side
            ctx.fillRect(W / 2 - mw / 2, msgY - 14, mw, 28);  // centered pill
            // White text on top
            ctx.fillStyle = `rgba(255,255,255,${alpha})`;
            ctx.textAlign = 'center';
            ctx.fillText(tutorialMsg.text, W / 2, msgY + 4);  // centered text
            ctx.textAlign = 'start';
        }
    }

    // ============================================================
    // WIN SCREEN — shown after reaching the golden goal platform
    // ============================================================
    if (won) {
        // Semi-transparent dark overlay covering the entire screen
        ctx.fillStyle = 'rgba(0,0,0,0.55)';
        ctx.fillRect(0, 0, W, H);

        // Pulsing gold "YOU WIN" text
        const pulse = 0.8 + 0.2 * Math.sin(performance.now() * 0.005);  // 0.6 to 1.0 oscillation
        ctx.fillStyle = '#ffd700';       // gold
        ctx.globalAlpha = pulse;         // apply the pulse to opacity
        ctx.font = 'bold 48px monospace';
        ctx.textAlign = 'center';        // center text horizontally
        ctx.fillText('★ YOU WIN! ★', W / 2, H / 2 - 20);
        ctx.globalAlpha = 1;             // reset opacity

        // Level completion text
        ctx.fillStyle = '#fff';          // white
        ctx.font = '18px monospace';
        ctx.fillText(`Level ${currentLevel} complete!`, W / 2, H / 2 + 20);

        // Control hints for next action
        ctx.font = '16px monospace';
        ctx.fillText('Press N for next level    Press R to retry', W / 2, H / 2 + 50);
        ctx.textAlign = 'start';         // reset text alignment
    }

    // ============================================================
    // INSTRUCTIONS BAR — controls reminder at the bottom of the screen
    // ============================================================
    ctx.fillStyle = 'rgba(0,0,0,0.4)';   // semi-transparent black background
    ctx.fillRect(0, H - 26, W, 26);      // 26 pixels tall at the very bottom
    ctx.fillStyle = 'rgba(255,255,255,0.45)';  // dim white text
    ctx.font = '12px monospace';
    ctx.textAlign = 'center';
    // All on one line: basic controls + overcharge warning
    ctx.fillText('← → Aim/Steer    SPACE Hold=Charge, Release=Launch'
        + '    Overcharge: 3s shake → 6s fizzle', W / 2, H - 9);
    ctx.textAlign = 'start';
}

// ============================================================
// GAME LOOP — the heartbeat of the game, runs ~60 times per second
// ============================================================
// requestAnimationFrame calls this function every time the browser
// is ready to draw a new frame (typically every ~16.7 milliseconds).
// The parameter "ts" is a high-precision timestamp in milliseconds.

let lastTime = 0;                        // timestamp of the previous frame
function gameLoop(ts) {
    // On the very first frame, there's no previous timestamp,
    // so we set dt (delta time) to 0 by making lastTime = ts.
    if (lastTime === 0) lastTime = ts;

    // Calculate how many seconds passed since the last frame.
    // ts and lastTime are in milliseconds, so we divide by 1000.
    const dt = (ts - lastTime) / 1000;   // delta time in seconds (usually ~0.016)
    lastTime = ts;                       // remember this frame's timestamp for next time

    // --- Handle level progression input (only active on win screen) ---
    if (won) {
        if (keys['KeyN']) {              // player pressed N = Next Level
            won = false;                 // clear the win state
            buildLevel(currentLevel + 1); // generate the next level
            resetPlayer();               // back to starting position
            resetCamera();               // camera back to ground
        }
        if (keys['KeyR']) {              // player pressed R = Retry
            won = false;                 // clear the win state
            buildLevel(currentLevel);    // rebuild the SAME level (new randomness)
            resetPlayer();               // back to starting position
            resetCamera();               // camera back to ground
        }
    }

    // --- Tutorial timer: counts up to 8 seconds ---
    // The tutorial popup fades in over 1s, stays for 5s, fades out over 2s.
    if (tutorialMsg && tutorialTimer < 8) {
        tutorialTimer += dt;             // add elapsed time to the tutorial timer
    }

    update(dt);                          // run all game logic (physics, collision, etc.)
    draw();                              // render everything to the canvas
    requestAnimationFrame(gameLoop);     // schedule the next frame (creates the loop)
}

// ============================================================
// START THE GAME — kick off the game loop
// ============================================================
buildLevel(1);                           // generate level 1 (easiest, only oneway modifiers)
resetPlayer();                           // place the player at the starting position
resetCamera();                           // position the camera to show the ground
requestAnimationFrame(gameLoop);         // begin the 60fps game loop!
