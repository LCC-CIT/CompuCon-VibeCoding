"""Two-player medieval combat in tkinter.

Choose a champion first - Knight (melee) or Mage (ranged firebolts).

Select screen:  P1 A/D pick, S ready     P2 <- -> pick, Down ready
Map screen:     P1 A/D choose map, S confirm (Arena / Forest / Market)
Fight:          P1 WASD      (A/D move, W jump, S attack)
                P2 arrow keys (Left/Right move, Up jump, Down attack)

R returns to the character select screen after a round.
"""

import math
import tkinter as tk

VIEW_W, VIEW_H = 800, 500
FLOOR_Y = 440
PLAYER_W, PLAYER_H = 24, 44

# maps: each has its own raised platforms and backdrop style
MAPS = {
    "arena": {
        "name": "Arena",
        "desc": "Castle courtyard",
        "raised": [(330, 350, 140, 16), (60, 400, 110, 16), (630, 400, 110, 16)],
    },
    "forest": {
        "name": "Forest",
        "desc": "Woodland clearing",
        "raised": [(330, 340, 130, 18), (90, 390, 100, 18), (590, 385, 100, 18),
                   (460, 320, 80, 16)],
    },
    "market": {
        "name": "Market Square",
        "desc": "Bustling square",
        "raised": [(300, 360, 120, 20), (80, 395, 100, 20), (620, 380, 110, 20),
                   (510, 325, 80, 16)],
    },
}
MAP_ORDER = ["arena", "forest", "market"]

# physics (per 60 fps frame)
GRAV = 0.5
JUMP_V = -11.5
ACCEL = 0.22

# combat
SWING_FRAMES = 14      # frames a knight's slash lasts
DAMAGE = 12
HIT_RANGE = 58         # horizontal reach of a slash
HITSTUN = 12
CAST_FRAMES = 8        # mage cast flash
MAGE_CD = 22           # frames between firebolts
MAGE_DMG = 10
PROJ_SPEED = 7.5

KNIGHT_HP, MAGE_HP = 100, 85
KNIGHT_SPEED, MAGE_SPEED = 4.0, 3.2

SKY_TOP = (110, 175, 220)
SKY_BOTTOM = (175, 215, 195)
STONE = "#8a7f6f"
STONE_DARK = "#5b5145"
GRASS = "#6a9c4a"

PAL1 = ("#3b6ea5", "#2b4a6f", "#7f1d1d", "#571414", "#c0392b", "#7cc4ff")
PAL2 = ("#4a7a3b", "#33582a", "#1f5ea8", "#153f73", "#e6b84d", "#a8e07a")


class Fighter:
    def __init__(self, name, spawn_x, facing, palette, controls, cls, game):
        self.name = name
        self.cls = cls                    # "knight" | "mage"
        self.game = game
        self.px, self.py = float(spawn_x), float(FLOOR_Y - PLAYER_H)
        self.vx, self.vy = 0.0, 0.0
        self.facing = facing
        self.max_hp = KNIGHT_HP if cls == "knight" else MAGE_HP
        self.hp = float(self.max_hp)
        self.max_speed = KNIGHT_SPEED if cls == "knight" else MAGE_SPEED
        self.grounded = False

        self.attack_timer = 0
        self.attack_cd = 0
        self.swing_phase = 0.0
        self.hit_applied = False
        self.hitstun = 0
        self.flash = 0
        self.attack_held = False

        self.tunic, self.tunic_dark, self.shield, self.shield_dark, self.plume, self.orb = palette
        self.left, self.right, self.jump, self.attack = controls

    def center(self):
        return (self.px + PLAYER_W / 2, self.py + PLAYER_H / 2)

    def try_attack(self):
        if self.attack_cd > 0 or self.hitstun > 0:
            return
        if self.cls == "knight":
            self.attack_cd = SWING_FRAMES
            self.attack_timer = SWING_FRAMES
            self.swing_phase = 0.0
            self.hit_applied = False
        else:
            self.attack_cd = MAGE_CD
            self.attack_timer = CAST_FRAMES
            self.game.spawn_projectile(self)

    def update(self, keys):
        self.attack_held = self.attack in keys

        if self.hitstun > 0:
            self.hitstun -= 1
            self.flash = max(0, self.flash - 1)
        else:
            move = (1 if self.right in keys else 0) - (1 if self.left in keys else 0)
            if move:
                self.facing = move
            self.vx += (move * self.max_speed - self.vx) * ACCEL
            if abs(self.vx) < 0.05:
                self.vx = 0.0
            if self.jump in keys and self.grounded:
                self.vy = JUMP_V
                self.grounded = False

        self.vy += GRAV
        if self.vy > 14:
            self.vy = 14

        # horizontal move + resolve
        self.px += self.vx
        self.px = max(8.0, min(VIEW_W - PLAYER_W - 8, self.px))
        for p in self.game.raised:
            if self._overlaps(p):
                if self.vx > 0:
                    self.px = p[0] - PLAYER_W
                elif self.vx < 0:
                    self.px = p[0] + p[2]
                self.vx = 0.0

        # vertical move + resolve
        self.py += self.vy
        self.grounded = False
        if self.vy >= 0 and self.py + PLAYER_H >= FLOOR_Y:
            self.py = FLOOR_Y - PLAYER_H
            self.vy = 0.0
            self.grounded = True
        for p in self.game.raised:
            if self._overlaps(p):
                if self.vy > 0:
                    self.py = p[1] - PLAYER_H
                    self.vy = 0.0
                    self.grounded = True
                elif self.vy < 0:
                    self.py = p[1] + p[3]
                    self.vy = 0.0

        # attack timing
        if self.attack_timer > 0:
            self.attack_timer -= 1
            if self.cls == "knight":
                self.swing_phase = 1 - self.attack_timer / SWING_FRAMES
                if self.attack_timer <= 0:
                    self.swing_phase = 0.0
        if self.attack_cd > 0:
            self.attack_cd -= 1
        elif self.attack_held and self.hitstun <= 0:
            self.try_attack()

    def _overlaps(self, p):
        eps = 2
        return (
            self.px + eps < p[0] + p[2]
            and self.px + PLAYER_W - eps > p[0]
            and self.py + eps < p[1] + p[3]
            and self.py + PLAYER_H - eps > p[1]
        )

    def apply_attack(self, other):
        """Knight melee: does the current slash land on `other`?"""
        if self.cls != "knight" or self.attack_timer <= 0 or self.hit_applied:
            return
        if not (0.3 < self.swing_phase < 0.8):
            return
        (ax, ay) = self.center()
        (bx, by) = other.center()
        dx, dy = bx - ax, by - ay
        if self.facing * dx < 0 or abs(dx) > HIT_RANGE:
            return
        if abs(dy) > 44:
            return
        self.hit_applied = True
        other.hp -= DAMAGE
        other.vx += self.facing * 5.5
        other.vy = min(other.vy, -3.5)
        other.hitstun = HITSTUN
        other.flash = 8
        self.game.add_hit_text(bx, by - 24, DAMAGE)

    def hit_projectile(self, other):
        other.hp -= MAGE_DMG
        other.vx += self.facing * 4.5
        other.vy = min(other.vy, -3.0)
        other.hitstun = HITSTUN
        other.flash = 8
        (cx, cy) = other.center()
        self.game.add_hit_text(cx, cy - 24, MAGE_DMG)


class Fight:
    def __init__(self, root):
        self.root = root
        root.title("Medieval Combat - P1: WASD  |  P2: Arrows")
        root.resizable(False, False)

        self.canvas = tk.Canvas(root, width=VIEW_W, height=VIEW_H, highlightthickness=0)
        self.canvas.pack()

        self.keys = set()
        root.bind("<KeyPress>", self._key_down)
        root.bind("<KeyRelease>", self._key_up)
        root.after(50, self.canvas.focus_set)

        self.sky_img = self._make_sky()
        self.clock = 0
        self.hit_texts = []
        self.projectiles = []
        self.map_idx = 0
        self.map_name = MAP_ORDER[0]
        self.raised = MAPS[self.map_name]["raised"]
        self._map_s_released = True

        # previews used on the select screen
        self._preview_knight = Fighter("knight", 0, 1, PAL1, ("left", "right", "up", "down"), "knight", self)
        self._preview_mage = Fighter("mage", 0, 1, PAL1, ("left", "right", "up", "down"), "mage", self)

        # select screen state
        self.phase = "select"              # "select" | "map" | "fight"
        self.p1_choice = "knight"
        self.p2_choice = "knight"
        self.p1_ready = self.p2_ready = False
        self.p1 = self.p2 = None
        self.game_over = False
        self.winner = None

        self.loop()

    # ------------------------------------------------------------- input
    def _key_down(self, e):
        k = e.keysym.lower()
        self.keys.add(k)
        if k == "r":
            if self.phase in ("fight", "map"):
                self.to_select()
            return "break"
        if self.phase == "select":
            self._select_key(k)
        elif self.phase == "map":
            self._map_key(k)
        return "break"

    def _key_up(self, e):
        k = e.keysym.lower()
        self.keys.discard(k)
        if k == "s":
            self._map_s_released = True

    def _select_key(self, k):
        if k == "a":
            self.p1_choice, self.p1_ready = "knight", False
        elif k == "d":
            self.p1_choice, self.p1_ready = "mage", False
        elif k == "s":
            self.p1_ready = not self.p1_ready
        elif k == "left":
            self.p2_choice, self.p2_ready = "knight", False
        elif k == "right":
            self.p2_choice, self.p2_ready = "mage", False
        elif k == "down":
            self.p2_ready = not self.p2_ready
        if self.p1_ready and self.p2_ready:
            self.go_to_map()

    def go_to_map(self):
        self.phase = "map"
        self._map_s_released = False

    def _map_key(self, k):
        if k in ("a", "d"):
            step = -1 if k == "a" else 1
            self.map_idx = (self.map_idx + step) % len(MAP_ORDER)
            self.map_name = MAP_ORDER[self.map_idx]
        elif k == "s" and self._map_s_released:
            self.start_fight()

    def start_fight(self):
        self.map_name = MAP_ORDER[self.map_idx]
        self.raised = MAPS[self.map_name]["raised"]
        self.p1 = Fighter("Player 1", 150, 1, PAL1, ("a", "d", "w", "s"), self.p1_choice, self)
        self.p2 = Fighter("Player 2", 630, -1, PAL2, ("left", "right", "up", "down"), self.p2_choice, self)
        self.projectiles = []
        self.hit_texts = []
        self.game_over = False
        self.winner = None
        self.phase = "fight"

    def to_select(self):
        self.phase = "select"
        self.p1_choice, self.p2_choice = "knight", "knight"
        self.p1_ready = self.p2_ready = False
        self.p1 = self.p2 = None
        self.projectiles = []
        self.hit_texts = []

    def add_hit_text(self, x, y, dmg):
        self.hit_texts.append({"x": x, "y": y, "age": 0, "dmg": dmg})

    def spawn_projectile(self, owner):
        fx = owner.px + PLAYER_W / 2 + owner.facing * 20
        fy = owner.py + PLAYER_H - 34
        self.projectiles.append({"x": fx, "y": fy, "vx": owner.facing * PROJ_SPEED,
                                 "owner": owner, "orb": owner.orb})

    # ---------------------------------------------------------------- sky
    def _make_sky(self):
        img = tk.PhotoImage(width=VIEW_W, height=VIEW_H)
        for y in range(VIEW_H):
            t = y / VIEW_H
            r = int(SKY_TOP[0] + (SKY_BOTTOM[0] - SKY_TOP[0]) * t)
            g = int(SKY_TOP[1] + (SKY_BOTTOM[1] - SKY_TOP[1]) * t)
            b = int(SKY_TOP[2] + (SKY_BOTTOM[2] - SKY_TOP[2]) * t)
            img.put("#%02x%02x%02x" % (r, g, b), to=(0, y, VIEW_W, y + 1))
        return img

    # --------------------------------------------------------------- loop
    def loop(self):
        if self.phase in ("select", "map"):
            self.draw()
            self.clock += 1
            self.root.after(16, self.loop)
            return

        if not self.game_over:
            self.p1.update(self.keys)
            self.p2.update(self.keys)
            self._separate(self.p1, self.p2)
            self.p1.apply_attack(self.p2)
            self.p2.apply_attack(self.p1)
            self._update_projectiles()
            self._check_game_over()
        self.draw()
        self.clock += 1
        self.root.after(16, self.loop)

    def _update_projectiles(self):
        for proj in self.projectiles[:]:
            proj["x"] += proj["vx"]
            if proj["x"] < 6 or proj["x"] > VIEW_W - 6 or proj["y"] > FLOOR_Y - 6:
                self.projectiles.remove(proj)
                continue
            other = self.p2 if proj["owner"] is self.p1 else self.p1
            if (other.px - 4 < proj["x"] < other.px + PLAYER_W + 4
                    and other.py - 4 < proj["y"] < other.py + PLAYER_H + 4):
                proj["owner"].hit_projectile(other)
                self.projectiles.remove(proj)

    def _separate(self, a, b):
        a1x, a1y, a2x, a2y = a.px, a.py, a.px + PLAYER_W, a.py + PLAYER_H
        b1x, b1y, b2x, b2y = b.px, b.py, b.px + PLAYER_W, b.py + PLAYER_H
        if a2x <= b1x or b2x <= a1x or a2y <= b1y or b2y <= a1y:
            return
        o = min(a2x - b1x, b2x - a1x)
        if a1x < b1x:
            a.px -= o / 2
            b.px += o / 2
        else:
            a.px += o / 2
            b.px -= o / 2
        for k in (a, b):
            k.px = max(8.0, min(VIEW_W - PLAYER_W - 8, k.px))

    def _check_game_over(self):
        if self.game_over:
            return
        dead1, dead2 = self.p1.hp <= 0, self.p2.hp <= 0
        if dead1 and dead2:
            self.game_over, self.winner = True, "Draw!"
        elif dead1:
            self.game_over, self.winner = True, "Player 2 wins!"
        elif dead2:
            self.game_over, self.winner = True, "Player 1 wins!"

    # -------------------------------------------------------------- draw
    def draw(self):
        c = self.canvas
        c.delete("all")
        if self.phase == "select":
            self._draw_select()
            return
        if self.phase == "map":
            self._draw_map_select()
            return
        self._draw_background()
        self._draw_raised()
        self._draw_projectiles()
        self._draw_hit_texts()
        self._draw_players()
        self._draw_hud()
        if self.game_over:
            self._draw_game_over()

    # ----------------------------------------------------- select screen
    def _draw_select(self):
        c = self.canvas
        self._draw_background()
        c.create_text(VIEW_W / 2, 40, text="Choose your champion",
                      fill="#2f2a22", font=("Segoe UI", 22, "bold"))
        self._draw_char_card(230, "knight")
        self._draw_char_card(570, "mage")
        c.create_text(VIEW_W / 2, VIEW_H - 8, anchor="s",
                      text="P1: A/D pick · S ready       P2: ← → pick · ↓ ready       Round starts when both are ready",
                      fill="#4a443a", font=("Segoe UI", 11))

    def _draw_char_card(self, cx, cls):
        c = self.canvas
        x1, x2 = cx - 115, cx + 115
        y1, y2 = 96, 410
        c.create_rectangle(x1, y1, x2, y2, fill="#f4ead6", outline="#c9b458", width=3)

        name = "KNIGHT" if cls == "knight" else "MAGE"
        c.create_text(cx, y1 + 26, text=name, fill="#2f2a22", font=("Segoe UI", 18, "bold"))
        desc = "Close-range slasher" if cls == "knight" else "Long-range caster"
        c.create_text(cx, y1 + 46, text=desc, fill="#6b6359", font=("Segoe UI", 10))
        stats = "HP 100  ·  Slash 12" if cls == "knight" else "HP 85  ·  Firebolt 10"
        c.create_text(cx, y1 + 62, text=stats, fill="#6b6359", font=("Segoe UI", 10))

        # player indicator bars
        if self.p1_choice == cls:
            c.create_rectangle(x1 + 8, y1 + 8, x2 - 8, y1 + 15, fill="#3b6ea5", outline="")
        if self.p2_choice == cls:
            c.create_rectangle(x1 + 8, y1 + 19, x2 - 8, y1 + 26, fill="#4a7a3b", outline="")

        # sprite preview
        if cls == "knight":
            self._draw_knight(c, cx, 320, 1, 0.0, False, self._preview_knight)
        else:
            self._draw_mage(c, cx, 320, 1, 0.0, False, self._preview_mage)

        # per-player status on their chosen card
        ty = 378
        if self.p1_choice == cls:
            text = "P1 READY" if self.p1_ready else "P1 - pick"
            c.create_text(cx, ty, text=text, fill="#3b6ea5", font=("Segoe UI", 12, "bold"))
            ty += 18
        if self.p2_choice == cls:
            text = "P2 READY" if self.p2_ready else "P2 - pick"
            c.create_text(cx, ty, text=text, fill="#4a7a3b", font=("Segoe UI", 12, "bold"))

    # ---------------------------------------------------- map select
    def _draw_map_select(self):
        c = self.canvas
        self._draw_background()          # preview the highlighted map behind the cards

        c.create_rectangle(0, 0, VIEW_W, 102, fill="#2f2a22", stipple="gray50", outline="")
        c.create_text(VIEW_W / 2, 40, text="Pick your battlefield",
                      fill="#ffffff", font=("Segoe UI", 24, "bold"))
        c.create_text(VIEW_W / 2, 74, text="Player 1: A / D to choose · S to confirm",
                      fill="#ffd766", font=("Segoe UI", 12, "bold"))

        for i, map_key in enumerate(MAP_ORDER):
            self._draw_map_card(150 + i * 250, map_key, selected=(i == self.map_idx))

        c.create_rectangle(0, VIEW_H - 34, VIEW_W, VIEW_H, fill="#2f2a22", stipple="gray50", outline="")
        c.create_text(VIEW_W / 2, VIEW_H - 8, anchor="s",
                      text="Player 1 picks the battlefield - P2, get ready!",
                      fill="#e8e2d8", font=("Segoe UI", 11))

    def _draw_map_card(self, cx, map_key, selected):
        c = self.canvas
        x1, x2 = cx - 120, cx + 120
        y1, y2 = 140, 352
        c.create_rectangle(x1, y1, x2, y2, fill="#f4ead6", outline="#c9b458", width=3)

        ty1, ty2 = y1 + 12, y1 + 122
        self._draw_map_thumbnail(cx, ty1, ty2, map_key)
        c.create_text(cx, ty2 + 26, text=MAPS[map_key]["name"], fill="#2f2a22",
                      font=("Segoe UI", 16, "bold"))
        c.create_text(cx, ty2 + 48, text=MAPS[map_key]["desc"], fill="#6b6359",
                      font=("Segoe UI", 10))

        if selected:
            c.create_rectangle(x1 + 5, y1 + 5, x2 - 5, y2 - 5, outline="#b08a2a", width=4)
            c.create_text(cx, y2 - 18, text="P1's pick", fill="#7f1d1d",
                          font=("Segoe UI", 13, "bold"))

    def _draw_map_thumbnail(self, cx, ty1, ty2, map_key):
        c = self.canvas
        c.create_rectangle(cx - 104, ty1, cx + 104, ty2, fill="#a8d4ea", outline="#a08a60")
        if map_key == "arena":
            c.create_rectangle(cx - 88, ty1 + 44, cx + 88, ty2, fill="#8b93a0", outline="")
            for t in (-84, -42, 0, 42, 84):
                c.create_rectangle(t - 9, ty1 + 32, t + 9, ty1 + 52, fill="#8b93a0", outline="")
            c.create_rectangle(cx - 12, ty1 + 18, cx + 12, ty2, fill="#6b4528", outline="")
        elif map_key == "forest":
            c.create_rectangle(cx - 88, ty1 + 62, cx + 88, ty2, fill="#4e7a3a", outline="")
            for tx in (-62, 0, 62):
                c.create_rectangle(tx - 6, ty1 + 44, tx + 6, ty2, fill="#5b4a33", outline="")
                c.create_oval(tx - 30, ty1 + 10, tx + 30, ty1 + 62, fill="#37702c", outline="")
        else:  # market
            c.create_rectangle(cx - 88, ty1 + 72, cx + 88, ty2, fill="#8d8274", outline="")
            for i in range(10):
                ax = cx - 86 + i * 18
                color = "#e6ded2" if i % 2 == 0 else "#a8322f"
                c.create_rectangle(ax, ty1 + 24, ax + 18, ty1 + 56, fill=color, outline="")
            c.create_rectangle(cx - 72, ty1 + 56, cx + 72, ty1 + 72, fill="#8a623f", outline="")

    # ------------------------------------------------------ background
    def _draw_background(self):
        if self.map_name == "forest":
            self._draw_bg_forest()
        elif self.map_name == "market":
            self._draw_bg_market()
        else:
            self._draw_bg_arena()

    def _draw_bg_arena(self):
        c = self.canvas
        c.create_image(0, 0, image=self.sky_img, anchor="nw")

        c.create_oval(680, 60, 764, 144, fill="#ffe9a3", outline="")
        c.create_oval(694, 74, 750, 130, fill="#ffd766", outline="")

        # castle wall
        c.create_rectangle(0, 120, VIEW_W, FLOOR_Y, fill="#8b93a0", outline="")
        for x in range(-16, VIEW_W + 16, 40):
            c.create_rectangle(x, 108, x + 24, 128, fill="#8b93a0", outline="")
        for wx in range(70, VIEW_W, 120):
            c.create_rectangle(wx, 200, wx + 30, 236, fill="#6f7680", outline="")
        for wx in range(130, VIEW_W, 120):
            c.create_rectangle(wx, 300, wx + 30, 336, fill="#6f7680", outline="")
        self._draw_banner(70, "#1f5ea8")
        self._draw_banner(VIEW_W - 104, "#7f1d1d")
        self._draw_torch(24)
        self._draw_torch(VIEW_W - 24)

        # stone courtyard floor
        c.create_rectangle(0, FLOOR_Y, VIEW_W, VIEW_H, fill="#7d7468", outline="")
        c.create_rectangle(0, FLOOR_Y, VIEW_W, FLOOR_Y + 6, fill="#5f574c", outline="")
        for x in range(0, VIEW_W, 40):
            c.create_line(x, FLOOR_Y + 6, x, VIEW_H, fill="#6b6356")
        for y in range(FLOOR_Y + 26, VIEW_H, 24):
            c.create_line(0, y, VIEW_W, y, fill="#6b6356")

    def _draw_bg_forest(self):
        c = self.canvas
        c.create_image(0, 0, image=self.sky_img, anchor="nw")

        # sun through the trees
        c.create_oval(660, 60, 744, 144, fill="#ffe9a3", outline="")
        c.create_oval(676, 76, 728, 128, fill="#ffd766", outline="")

        # two layered treelines with bumpy canopies (far, then near)
        self._draw_tree_line(FLOOR_Y - 64, "#779d5e", 14)
        self._draw_tree_line(FLOOR_Y, "#4e7a3a", 20)

        # framing trees standing on the ground
        self._draw_tree(-8, FLOOR_Y)
        self._draw_tree(VIEW_W - 10, FLOOR_Y)

        # grassy floor
        c.create_rectangle(0, FLOOR_Y, VIEW_W, VIEW_H, fill="#3d6b2f", outline="")
        c.create_rectangle(0, FLOOR_Y, VIEW_W, FLOOR_Y + 8, fill="#7ab34f", outline="")
        for (mx, my, r) in ((120, 470, 26), (360, 478, 20), (600, 466, 30), (700, 476, 18)):
            c.create_oval(mx - r, my - r, mx + r, my + r, fill="#2f5a26", outline="")
        for (mx, my, r) in ((220, 468, 18), (500, 472, 22)):
            c.create_oval(mx - r, my - r, mx + r, my + r, fill="#5b9446", outline="")

    def _draw_tree_line(self, y_base, color, bump):
        """A rolling treeline band: bumpy canopy top, filling down to the floor."""
        c = self.canvas
        pts = []
        for x in range(-20, VIEW_W + 40, 28):
            h = bump * (0.6 + 0.4 * math.sin(x * 0.02)) * (0.5 + 0.5 * math.sin(x * 0.07 + 1.5))
            pts.extend([x, y_base - h - 10])
        pts.extend([VIEW_W + 20, FLOOR_Y + 2, -20, FLOOR_Y + 2])
        c.create_polygon(pts, fill=color, outline="", smooth=True)

    def _draw_tree(self, x, base_y):
        c = self.canvas
        c.create_rectangle(x - 12, base_y - 120, x + 12, base_y, fill="#5b4a33", outline="#3d3020")
        c.create_oval(x - 46, base_y - 180, x + 46, base_y - 96, fill="#2e5a26", outline="")
        c.create_oval(x - 30, base_y - 160, x + 34, base_y - 86, fill="#37702c", outline="")
        c.create_oval(x - 12, base_y - 132, x + 16, base_y - 78, fill="#448a35", outline="")

    def _draw_bg_market(self):
        c = self.canvas
        c.create_image(0, 0, image=self.sky_img, anchor="nw")

        c.create_oval(680, 60, 764, 144, fill="#ffe9a3", outline="")
        c.create_oval(694, 74, 750, 130, fill="#ffd766", outline="")

        # back buildings sitting on the ground
        self._draw_building(20, FLOOR_Y - 150, 130, 150)
        self._draw_building(180, FLOOR_Y - 120, 110, 120)
        self._draw_building(470, FLOOR_Y - 140, 140, 140)
        self._draw_building(640, FLOOR_Y - 115, 120, 115)

        # market stalls with striped awnings
        for sx in (110, 400, 690):
            self._draw_stall(sx)

        # rope of hanging lanterns stretched across the square
        c.create_line(0, 130, VIEW_W, 130, fill="#3a2c1a", width=2)
        for lx in (95, 305, 520, 705):
            c.create_line(lx, 130, lx, 152, fill="#3a2c1a", width=2)
            c.create_oval(lx - 6, 152, lx + 6, 164, fill="#ffd766", outline="#b08a2a")

        # cobbled floor
        c.create_rectangle(0, FLOOR_Y, VIEW_W, VIEW_H, fill="#8d8274", outline="")
        c.create_rectangle(0, FLOOR_Y, VIEW_W, FLOOR_Y + 6, fill="#6b6155", outline="")
        for x in range(0, VIEW_W, 40):
            c.create_line(x, FLOOR_Y + 6, x, VIEW_H, fill="#7a7062")
        for y in range(FLOOR_Y + 26, VIEW_H, 24):
            c.create_line(0, y, VIEW_W, y, fill="#7a7062")

    def _draw_building(self, x, y, w, h):
        """A market building with its wall base sitting at y + h (= the floor)."""
        c = self.canvas
        wall_top = y + h // 3
        c.create_rectangle(x, wall_top, x + w, y + h, fill="#d8c39a", outline="#a08a60")
        c.create_polygon(x - 10, wall_top, x + w / 2, y - 30, x + w + 10, wall_top,
                         fill="#a54b2d", outline="#6e2f1a")
        c.create_rectangle(x + w / 2 - 12, y + h - 40, x + w / 2 + 12, y + h,
                           fill="#6b4528", outline="")
        for wx in (x + 16, x + w - 28):
            c.create_rectangle(wx, wall_top + 22, wx + 12, wall_top + 40,
                               fill="#c98b3a", outline="")
        # soft shadow where the wall meets the cobbles
        c.create_rectangle(x, y + h - 4, x + w, y + h, fill="#6b6155", outline="")

    def _draw_stall(self, x):
        c = self.canvas
        y_aw = FLOOR_Y - 140
        y_ctr = FLOOR_Y - 34
        c.create_line(x - 62, FLOOR_Y, x - 62, y_aw + 10, fill="#6b4a2f", width=6)
        c.create_line(x + 62, FLOOR_Y, x + 62, y_aw + 10, fill="#6b4a2f", width=6)
        c.create_rectangle(x - 66, y_ctr, x + 66, y_ctr + 22, fill="#8a623f", outline="#5a3a1e")
        for i in range(13):
            ax = x - 78 + i * 12
            color = "#e6ded2" if i % 2 == 0 else "#a8322f"
            c.create_rectangle(ax, y_aw, ax + 12, y_aw + 28, fill=color, outline="")
        for i in range(12):
            ax = x - 78 + i * 12
            color = "#e6ded2" if i % 2 == 0 else "#a8322f"
            c.create_oval(ax, y_aw + 20, ax + 12, y_aw + 32, fill=color, outline="")

    def _draw_banner(self, x, color):
        c = self.canvas
        wave = math.sin(self.clock * 0.08) * 3
        c.create_polygon(x, 132, x + 34, 132, x + 26 + wave, 200, x, 214,
                         fill=color, outline="")

    def _draw_torch(self, x):
        c = self.canvas
        c.create_line(x, FLOOR_Y, x, FLOOR_Y - 52, fill="#5b4a33", width=5)
        c.create_rectangle(x - 9, FLOOR_Y - 56, x + 9, FLOOR_Y - 48, fill="#4a3a26", outline="")
        fl = math.sin(self.clock * 0.3) * 2
        c.create_oval(x - 7, FLOOR_Y - 68 + fl, x + 7, FLOOR_Y - 54 + fl,
                      fill="#ff8c33", outline="")
        c.create_oval(x - 4, FLOOR_Y - 62 + fl, x + 4, FLOOR_Y - 57 + fl,
                      fill="#ffe08a", outline="")

    def _draw_raised(self):
        if self.map_name == "forest":
            self._draw_log_platforms()
        elif self.map_name == "market":
            self._draw_crate_platforms()
        else:
            self._draw_stone_platforms()

    def _draw_stone_platforms(self):
        c = self.canvas
        for (x, y, w, h) in self.raised:
            c.create_rectangle(x, y, x + w, y + h, fill=STONE, outline=STONE_DARK, width=1)
            c.create_rectangle(x, y, x + w, y + 8, fill=GRASS, outline="")
            c.create_line(x + w / 2, y + 12, x + w / 2, y + h - 4, fill="#77695a")

    def _draw_log_platforms(self):
        c = self.canvas
        for (x, y, w, h) in self.raised:
            c.create_rectangle(x, y, x + w, y + h, fill="#6b4a2f", outline="#4a3320", width=2)
            c.create_rectangle(x, y, x + w, y + 6, fill="#8a623f", outline="")
            for j in range(1, int(w // 22)):
                lx = x + j * 22
                c.create_line(lx, y + 8, lx + 4, y + h - 2, fill="#57391f")
            # end rings make it read as a log
            c.create_oval(x + 4, y + h - 10, x + 14, y, fill="#8a623f", outline="#4a3320")
            c.create_oval(x + w - 14, y + h - 10, x + w - 4, y, fill="#8a623f", outline="#4a3320")

    def _draw_crate_platforms(self):
        c = self.canvas
        for (x, y, w, h) in self.raised:
            c.create_rectangle(x, y, x + w, y + h, fill="#9c6b3f", outline="#6b4528", width=2)
            c.create_rectangle(x, y, x + w, y + 6, fill="#b5814e", outline="")
            c.create_line(x + 6, y + h - 2, x + w - 6, y + 6, fill="#6b4528")
            c.create_line(x + w - 6, y + h - 2, x + 6, y + 6, fill="#6b4528")

    # --------------------------------------------------- projectiles / fx
    def _draw_projectiles(self):
        c = self.canvas
        for proj in self.projectiles:
            x, y = proj["x"], proj["y"]
            orb = proj["orb"]
            c.create_line(x - proj["vx"] * 2.5, y, x, y, width=4, fill=orb)
            c.create_oval(x - 9, y - 9, x + 9, y + 9, fill=orb, outline="")
            c.create_oval(x - 4, y - 4, x + 4, y + 4, fill="#ffffff", outline="")

    def _draw_hit_texts(self):
        c = self.canvas
        keep = []
        for t in self.hit_texts:
            t["age"] += 1
            t["y"] -= 1.3
            if t["age"] <= 45:
                c.create_text(t["x"], t["y"], text=f"-{t['dmg']}", fill="#1a1a1a",
                              font=("Segoe UI", 15, "bold"))
                c.create_text(t["x"], t["y"] - 1, text=f"-{t['dmg']}", fill="#ffffff",
                              font=("Segoe UI", 15, "bold"))
                keep.append(t)
        self.hit_texts = keep

    # ---------------------------------------------------------- fighters
    def _draw_players(self):
        c = self.canvas
        for p in (self.p1, self.p2):
            cx = p.px + PLAYER_W / 2
            feet = p.py + PLAYER_H
            moving = abs(p.vx) > 0.3 and p.hitstun <= 0
            phase = self.clock * 0.25 if moving else 0.0
            c.create_oval(cx - 15, feet - 3, cx + 15, feet + 3, fill="#c9c2b4", outline="")
            if p.cls == "knight":
                self._draw_knight(c, cx, feet, p.facing, phase, moving, p,
                                  swing=self._swing_geom(p))
            else:
                self._draw_mage(c, cx, feet, p.facing, phase, moving, p,
                                casting=p.attack_timer > 0)

    def _swing_geom(self, p):
        if p.attack_timer <= 0:
            return None
        cx = p.px + PLAYER_W / 2
        feet = p.py + PLAYER_H
        hand_x = cx + p.facing * 11
        hand_y = feet - 30
        ang = -1.4 + 2.8 * p.swing_phase
        tip_x = hand_x + math.sin(ang) * 46 * p.facing
        tip_y = hand_y - math.cos(ang) * 46
        return (hand_x, hand_y, tip_x, tip_y)

    def _draw_knight(self, c, x, y, f, phase, moving, p, swing=None):
        bob = abs(math.sin(phase)) * 2 if moving else 0
        swing_legs = math.sin(phase) * 4 if moving else 0

        # sword on the back
        c.create_line(x + f * (-5), y - 30 + bob, x + f * (-16), y - 48 + bob,
                      fill="#cfd6dd", width=3)
        c.create_line(x + f * (-5), y - 30 + bob, x + f * (-8), y - 27 + bob,
                      fill="#e6b84d", width=3)

        # legs + boots
        leg1, leg2 = -5 + swing_legs, 5 - swing_legs
        for lx in (leg1, leg2):
            c.create_rectangle(x + lx - 3, y - 13 + bob, x + lx + 3, y - 2,
                               fill="#33344a", outline="#22232f")
            c.create_rectangle(x + lx - 3, y - 5, x + lx + 3, y,
                               fill="#6b4a2f", outline="#4a3320")

        # tunic + belt
        c.create_rectangle(x - 11, y - 30 + bob, x + 11, y - 14 + bob,
                           fill=p.tunic, outline=p.tunic_dark)
        c.create_rectangle(x - 11, y - 17 + bob, x + 11, y - 13 + bob,
                           fill="#7a4f2b", outline="#5a3a1e")

        # helmet + visor + plume
        c.create_rectangle(x - 8, y - 44 + bob, x + 8, y - 30 + bob,
                           fill="#aab4bd", outline="#6f7982")
        c.create_rectangle(x - 6 + f * 2, y - 40 + bob, x - 1 + f * 2, y - 35 + bob,
                           fill="#2a2a2a", outline="")
        c.create_rectangle(x - 5, y - 51 + bob, x + 5, y - 43 + bob,
                           fill=p.plume, outline="#7f1d1d")

        # shield
        c.create_oval(x + f * 7 - 7, y - 32 + bob, x + f * 7 + 7, y - 20 + bob,
                      fill=p.shield, outline=p.shield_dark)
        c.create_oval(x + f * 7 - 3, y - 28 + bob, x + f * 7 + 3, y - 24 + bob,
                      fill="#e6b84d", outline="")

        # slash blade
        if swing:
            hx, hy, tx, ty = swing
            c.create_line(hx, hy, tx, ty, fill="#dfe6ec", width=5)
            c.create_line(hx, hy, tx, ty, fill="#ffffff", width=2)
            c.create_oval(hx - 3, hy - 3, hx + 3, hy + 3, fill="#e6b84d", outline="")

        if p.flash > 0:
            c.create_rectangle(x - 12, y - 52 + bob, x + 12, y,
                               fill="#ffffff", stipple="gray50", outline="")

    def _draw_mage(self, c, x, y, f, phase, moving, p, casting=False):
        bob = abs(math.sin(phase)) * 2 if moving else 0

        # boots under the robe
        c.create_rectangle(x - 9, y - 4, x - 3, y, fill="#4a3320", outline="#33220f")
        c.create_rectangle(x + 3, y - 4, x + 9, y, fill="#4a3320", outline="#33220f")

        # robe
        c.create_polygon(x - 10, y - 28 + bob, x + 10, y - 28 + bob,
                         x + 15, y - 2, x - 15, y - 2,
                         fill=p.tunic, outline=p.tunic_dark)
        c.create_line(x - 15, y - 4, x + 15, y - 4, fill=p.tunic_dark)
        c.create_line(x - 8, y - 14 + bob, x + 8, y - 14 + bob, fill=p.tunic_dark)

        # face
        c.create_rectangle(x - 7, y - 42 + bob, x + 7, y - 28 + bob,
                           fill="#e8c39e", outline="#c9a17b")
        # hat
        c.create_rectangle(x - 11, y - 44 + bob, x + 11, y - 38 + bob,
                           fill=p.plume, outline=p.tunic_dark)
        c.create_polygon(x - 9, y - 41 + bob, x + 9, y - 41 + bob, x + 2, y - 58 + bob,
                         fill=p.plume, outline=p.tunic_dark)

        # staff + glowing orb
        sx = x + f * 8
        ox = x + f * 15
        oy = y - 56 + bob
        c.create_line(sx, y - 20 + bob, ox, oy + 2, fill="#6b4a2f", width=4)
        glow = 2 + (2 if casting else 0)
        c.create_oval(ox - 6 - glow, oy - 6 - glow, ox + 6 + glow, oy + 6 + glow,
                      fill="#e8f1ff" if casting else p.orb, outline="")
        c.create_oval(ox - 4, oy - 4, ox + 4, oy + 4,
                      fill="#ffffff" if casting else p.orb, outline="")

        if p.flash > 0:
            c.create_rectangle(x - 16, y - 58 + bob, x + 16, y,
                               fill="#ffffff", stipple="gray50", outline="")

    # --------------------------------------------------------------- HUD
    def _draw_hud(self):
        c = self.canvas
        w, h = 300, 18
        y0 = 20

        for label, x0, p, color in (("Player 1", 20, self.p1, "#3b6ea5"),
                                    ("Player 2", VIEW_W - 20 - w, self.p2, "#8a3b2f")):
            c.create_rectangle(x0, y0, x0 + w, y0 + h, fill="#3a342e", outline="#241f1a")
            fw = max(0.0, p.hp / p.max_hp) * w
            c.create_rectangle(x0, y0, x0 + fw, y0 + h, fill=color, outline="")
            c.create_text(x0 + w / 2, y0 - 5, text=label, fill=color,
                          font=("Segoe UI", 12, "bold"))
            c.create_text(x0 + w / 2, y0 + h + 8, text=p.cls.title(),
                          fill="#6b6359", font=("Segoe UI", 9))
            hp_x = x0 + 6 if label == "Player 1" else x0 + w - 6
            c.create_text(hp_x, y0 + h / 2, text=f"{max(0, int(p.hp))}",
                          anchor="w" if label == "Player 1" else "e",
                          fill="#ffffff", font=("Segoe UI", 10, "bold"))

        c.create_text(VIEW_W / 2, 12, text="vs", fill="#4a443a", font=("Segoe UI", 12, "bold"))
        c.create_text(VIEW_W / 2, 30, text=MAPS[self.map_name]["name"],
                      fill="#6b6359", font=("Segoe UI", 10))
        c.create_text(VIEW_W / 2, VIEW_H - 6, anchor="s",
                      text="P1: A/D move  W jump  S attack        P2: ← → move  ↑ jump  ↓ attack        R: pick new champion",
                      fill="#4a443a", font=("Segoe UI", 11))

    def _draw_game_over(self):
        c = self.canvas
        c.create_rectangle(0, 0, VIEW_W, VIEW_H, fill="#1a1a1a", stipple="gray50", outline="")
        c.create_rectangle(VIEW_W / 2 - 240, 160, VIEW_W / 2 + 240, 300,
                           fill="#fff8e1", outline="#c9b458", width=4)
        c.create_text(VIEW_W / 2, 205, text="⚔ " + self.winner + " ⚔",
                      fill="#7f1d1d", font=("Segoe UI", 26, "bold"))
        c.create_text(VIEW_W / 2, 255, text="Press R to pick new champions",
                      fill="#6b6359", font=("Segoe UI", 13))


def main():
    root = tk.Tk()
    Fight(root)
    root.mainloop()


if __name__ == "__main__":
    main()
