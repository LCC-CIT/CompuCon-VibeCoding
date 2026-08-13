"""
Chubby Car Racer  🚗
====================
A kid‑friendly top‑down racing game. Dodge the oncoming cars,
collect coins, and see how far you can go!

Controls:
  ← →  arrow keys  — steer
  P                 — pause / resume
  R                 — restart after game over

Python 3 + tkinter — no external dependencies.
"""

import tkinter as tk
from tkinter import messagebox
import random
import math

# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  Constants                                                              ║
# ╚══════════════════════════════════════════════════════════════════════════╝

CANVAS_W   = 480
CANVAS_H   = 640

ROAD_LEFT  = 80
ROAD_RIGHT = CANVAS_W - 80
ROAD_W     = ROAD_RIGHT - ROAD_LEFT
LANE_COUNT = 4
LANE_W     = ROAD_W // LANE_COUNT

PLAYER_W   = 52
PLAYER_H   = 78
ENEMY_W    = 48
ENEMY_H    = 72
COIN_R     = 12

FPS        = 60
FRAME_MS   = 1000 // FPS

# Colours  (bright, kid‑friendly palette)
BG          = "#2b5c2b"      # grass green
ROAD_CLR    = "#4a4a5a"      # dark asphalt
LINE_CLR    = "#e8e8c0"      # dashed lane markings
PLAYER_BODY = "#ff4444"      # bright red
PLAYER_TOP  = "#ff7777"      # lighter red (roof)
WHEEL_CLR   = "#222222"
WINDOW_CLR  = "#b8d8ff"
BUMPER_CLR  = "#cccccc"

# Enemy car palette  (randomly chosen)
ENEMY_COLORS = [
    ("#4488cc", "#77aadd"),   # blue
    ("#44aa44", "#77cc77"),   # green
    ("#cc8800", "#ddbb44"),   # orange
    ("#9944cc", "#bb77dd"),   # purple
    ("#cc4488", "#dd77aa"),   # pink
    ("#cccc44", "#dddd77"),   # yellow
]

COIN_CLR    = "#ffd700"
COIN_RING   = "#daa520"

# Speeds
BASE_SPEED  = 4.0
MAX_SPEED   = 10.0
SPEED_INC   = 0.3      # speed increase per 100 points


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  Drawing helpers                                                        ║
# ╚══════════════════════════════════════════════════════════════════════════╝

def _round_rect(canvas: tk.Canvas,
                x1: float, y1: float, x2: float, y2: float,
                r: float = 10, **kwargs) -> tuple:
    """Draw a rounded rectangle.  Returns the item ids."""
    ids = []
    # Main body (central rectangle + two end caps)
    ids.append(canvas.create_rectangle(x1 + r, y1, x2 - r, y2, **kwargs))
    ids.append(canvas.create_rectangle(x1, y1 + r, x2, y2 - r, **kwargs))
    # Four corner circles
    ids.append(canvas.create_oval(x1, y1, x1 + r * 2, y1 + r * 2, **kwargs))
    ids.append(canvas.create_oval(x2 - r * 2, y1, x2, y1 + r * 2, **kwargs))
    ids.append(canvas.create_oval(x1, y2 - r * 2, x1 + r * 2, y2, **kwargs))
    ids.append(canvas.create_oval(x2 - r * 2, y2 - r * 2, x2, y2, **kwargs))
    return tuple(ids)


def draw_chubby_car(canvas: tk.Canvas,
                    cx: float, cy: float,
                    body_color: str, top_color: str, tag: str) -> None:
    """Draw a cute, chubby car centred at (cx, cy)."""
    w2 = PLAYER_W / 2
    h2 = PLAYER_H / 2

    # ── Body (the chubby main shape) ──
    _round_rect(canvas, cx - w2, cy - h2 + 6, cx + w2, cy + h2 - 4,
                r=16, fill=body_color, outline="#8b0000", width=2, tags=tag)

    # ── Roof / cabin ──
    roof_w, roof_h = 34, 28
    _round_rect(canvas, cx - roof_w / 2, cy - roof_h + 4,
                cx + roof_w / 2, cy + 2,
                r=8, fill=top_color, outline="#8b0000", width=1, tags=tag)

    # ── Windows ──
    win_w, win_h = 20, 14
    canvas.create_oval(cx - win_w / 2, cy - roof_h + 8,
                       cx + win_w / 2, cy - roof_h + 8 + win_h,
                       fill=WINDOW_CLR, outline="#555577", width=1, tags=tag)

    # ── Bumper / grille ──
    canvas.create_rectangle(cx - 10, cy + h2 - 6, cx + 10, cy + h2 - 2,
                            fill=BUMPER_CLR, outline="#999999", tags=tag)

    # ── Headlights ──
    for lx in (cx - 14, cx + 14):
        canvas.create_oval(lx - 4, cy - h2 + 10, lx + 4, cy - h2 + 18,
                           fill="#ffffcc", outline="#cccc00", tags=tag)

    # ── Wheels ──
    for wx in (cx - w2 + 4, cx + w2 - 4):
        for wy in (cy - h2 + 24, cy + h2 - 12):
            canvas.create_oval(wx - 7, wy - 7, wx + 7, wy + 7,
                               fill=WHEEL_CLR, outline="#111111", tags=tag)
            # Hubcap
            canvas.create_oval(wx - 3, wy - 3, wx + 3, wy + 3,
                               fill="#666666", tags=tag)

    # ── Exhaust pipe ──
    canvas.create_rectangle(cx + w2 - 4, cy + h2 - 10,
                            cx + w2 + 2, cy + h2 - 6,
                            fill="#888888", tags=tag)


def draw_enemy_car(canvas: tk.Canvas,
                   cx: float, cy: float,
                   body_color: str, top_color: str, tag: str) -> None:
    """Draw an enemy car (same chubby style, facing down)."""
    w2 = ENEMY_W / 2
    h2 = ENEMY_H / 2

    _round_rect(canvas, cx - w2, cy - h2 + 4, cx + w2, cy + h2 - 6,
                r=14, fill=body_color, outline="#333333", width=2, tags=tag)

    roof_w, roof_h = 30, 24
    _round_rect(canvas, cx - roof_w / 2, cy - 4,
                cx + roof_w / 2, cy + roof_h,
                r=7, fill=top_color, outline="#333333", width=1, tags=tag)

    win_w, win_h = 18, 12
    canvas.create_oval(cx - win_w / 2, cy + 2,
                       cx + win_w / 2, cy + 2 + win_h,
                       fill=WINDOW_CLR, outline="#555577", width=1, tags=tag)

    # Tail‑lights
    for lx in (cx - 12, cx + 12):
        canvas.create_oval(lx - 3, cy - h2 + 8, lx + 3, cy - h2 + 14,
                           fill="#ff4444", outline="#aa0000", tags=tag)

    for wx in (cx - w2 + 4, cx + w2 - 4):
        for wy in (cy - h2 + 22, cy + h2 - 14):
            canvas.create_oval(wx - 6, wy - 6, wx + 6, wy + 6,
                               fill=WHEEL_CLR, outline="#111111", tags=tag)
            canvas.create_oval(wx - 2, wy - 2, wx + 2, wy + 2,
                               fill="#666666", tags=tag)


def draw_coin(canvas: tk.Canvas, cx: float, cy: float, tag: str) -> None:
    """Draw a shiny coin."""
    canvas.create_oval(cx - COIN_R, cy - COIN_R, cx + COIN_R, cy + COIN_R,
                       fill=COIN_CLR, outline=COIN_RING, width=2, tags=tag)
    canvas.create_text(cx, cy, text="$", fill=COIN_RING,
                       font=("Arial", 12, "bold"), tags=tag)


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  Game                                                                    ║
# ╚══════════════════════════════════════════════════════════════════════════╝

class ChubbyRacer:
    """Top‑down car‑dodging game."""

    def __init__(self, canvas: tk.Canvas) -> None:
        self.canvas = canvas

        # Player position
        self.px = CANVAS_W / 2
        self.py = CANVAS_H - 100

        # Enemies and coins
        self.enemies: list[dict] = []
        self.coins: list[dict] = []

        # State
        self.score = 0
        self.coin_count = 0
        self.game_over = False
        self.paused = False

        # Road scroll offset
        self._scroll = 0.0

        # Timers
        self._spawn_timer = 0
        self._coin_timer = 0
        self._speed = BASE_SPEED
        self._after_id: str | None = None

        # Input
        self._left = False
        self._right = False

    # ── properties ───────────────────────────────────────────────────────

    @property
    def speed(self) -> float:
        return self._speed

    # ── input ────────────────────────────────────────────────────────────

    def steer_left(self, down: bool) -> None:
        self._left = down

    def steer_right(self, down: bool) -> None:
        self._right = down

    def toggle_pause(self) -> None:
        if self.game_over:
            return
        self.paused = not self.paused

    # ── update ───────────────────────────────────────────────────────────

    def tick(self) -> None:
        if self.game_over or self.paused:
            return

        self._speed = BASE_SPEED + (self.score // 100) * SPEED_INC
        if self._speed > MAX_SPEED:
            self._speed = MAX_SPEED

        # Player movement
        steer = 6.0
        if self._left:
            self.px -= steer
        if self._right:
            self.px += steer
        # Clamp to road
        half_w = PLAYER_W / 2
        if self.px - half_w < ROAD_LEFT:
            self.px = ROAD_LEFT + half_w
        if self.px + half_w > ROAD_RIGHT:
            self.px = ROAD_RIGHT - half_w

        # Road scroll
        self._scroll += self._speed
        self._scroll %= 60

        # Score
        self.score += int(self._speed)

        # Spawn enemies
        self._spawn_timer -= 1
        if self._spawn_timer <= 0:
            self._spawn_enemy()
            self._spawn_timer = random.randint(30, 80) - int(self._speed * 4)

        # Spawn coins
        self._coin_timer -= 1
        if self._coin_timer <= 0:
            self._spawn_coin()
            self._coin_timer = random.randint(40, 100)

        # Move enemies and coins
        for e in self.enemies:
            e["y"] += self._speed
        for c in self.coins:
            c["y"] += self._speed

        # Remove off‑screen
        self.enemies = [e for e in self.enemies if e["y"] < CANVAS_H + 100]
        self.coins = [c for c in self.coins if c["y"] < CANVAS_H + 50]

        # Collision: enemies
        for e in self.enemies:
            if self._collides(self.px, self.py, PLAYER_W, PLAYER_H,
                              e["x"], e["y"], ENEMY_W, ENEMY_H):
                self._crash()
                return

        # Collision: coins
        for c in self.coins:
            dist = math.hypot(self.px - c["x"], self.py - c["y"])
            if dist < COIN_R + PLAYER_W / 2:
                self.coin_count += 1
                c["y"] = -100  # mark for removal
        self.coins = [c for c in self.coins if c["y"] > -50]

    def _spawn_enemy(self) -> None:
        lane = random.randint(0, LANE_COUNT - 1)
        x = ROAD_LEFT + lane * LANE_W + LANE_W / 2
        # Jitter within lane
        x += random.randint(-16, 16)
        x = max(ROAD_LEFT + ENEMY_W / 2 + 4,
                min(ROAD_RIGHT - ENEMY_W / 2 - 4, x))
        body, top = random.choice(ENEMY_COLORS)
        self.enemies.append({"x": x, "y": -100.0, "body": body, "top": top})

    def _spawn_coin(self) -> None:
        x = random.uniform(ROAD_LEFT + 30, ROAD_RIGHT - 30)
        self.coins.append({"x": x, "y": -50.0})

    @staticmethod
    def _collides(x1: float, y1: float, w1: float, h1: float,
                  x2: float, y2: float, w2: float, h2: float) -> bool:
        """AABB overlap test with a margin for fairness."""
        m = 8  # small forgiveness margin
        return (abs(x1 - x2) < (w1 + w2) / 2 - m and
                abs(y1 - y2) < (h1 + h2) / 2 - m)

    def _crash(self) -> None:
        self.game_over = True

    def restart(self) -> None:
        self.px = CANVAS_W / 2
        self.py = CANVAS_H - 100
        self.enemies.clear()
        self.coins.clear()
        self.score = 0
        self.coin_count = 0
        self.game_over = False
        self.paused = False
        self._scroll = 0.0
        self._spawn_timer = 0
        self._coin_timer = 0
        self._speed = BASE_SPEED
        self._left = False
        self._right = False

    # ── render ───────────────────────────────────────────────────────────

    def render(self) -> None:
        """Draw the entire frame."""
        c = self.canvas
        c.delete("all")

        # Grass
        c.create_rectangle(0, 0, CANVAS_W, CANVAS_H, fill=BG, outline="")

        # Road
        c.create_rectangle(ROAD_LEFT, 0, ROAD_RIGHT, CANVAS_H,
                           fill=ROAD_CLR, outline="#333344", width=3)

        # Road edge lines (solid)
        c.create_line(ROAD_LEFT, 0, ROAD_LEFT, CANVAS_H,
                      fill="#ffffcc", width=4)
        c.create_line(ROAD_RIGHT, 0, ROAD_RIGHT, CANVAS_H,
                      fill="#ffffcc", width=4)

        # Dashed lane lines
        dash_len = 30
        gap = 30
        for lane in range(1, LANE_COUNT):
            lx = ROAD_LEFT + lane * LANE_W
            y = self._scroll
            while y < CANVAS_H + dash_len:
                if y + dash_len > 0:
                    seg_top = max(y, 0)
                    seg_bot = min(y + dash_len, CANVAS_H)
                    if seg_bot > seg_top:
                        c.create_line(lx, seg_top, lx, seg_bot,
                                      fill=LINE_CLR, width=2, dash=(12, 18))
                y += dash_len + gap

        # Actually, simpler dashed line approach:
        for lane in range(1, LANE_COUNT):
            lx = ROAD_LEFT + lane * LANE_W
            y = self._scroll - dash_len
            while y < CANVAS_H:
                y1 = max(y, 0)
                y2 = min(y + dash_len, CANVAS_H)
                if y2 > y1:
                    c.create_line(lx, y1, lx, y2,
                                  fill=LINE_CLR, width=2)
                y += dash_len + gap

        # Coins
        for coin in self.coins:
            draw_coin(c, coin["x"], coin["y"], "")

        # Enemy cars
        for e in self.enemies:
            draw_enemy_car(c, e["x"], e["y"], e["body"], e["top"], "")

        # Player car (on top)
        if not self.game_over:
            draw_chubby_car(c, self.px, self.py, PLAYER_BODY, PLAYER_TOP, "")

        # ── HUD ──
        # Score panel
        panel_x, panel_y = 10, 10
        c.create_rectangle(panel_x, panel_y, panel_x + 180, panel_y + 60,
                           fill="#2a2a3a", outline="", tags="hud")
        c.create_text(panel_x + 14, panel_y + 14, anchor="w",
                      text=f"🏆 Score: {self.score}",
                      fill="#ffffff", font=("Segoe UI", 13, "bold"),
                      tags="hud")
        c.create_text(panel_x + 14, panel_y + 38, anchor="w",
                      text=f"💰 Coins: {self.coin_count}",
                      fill="#ffd700", font=("Segoe UI", 13, "bold"),
                      tags="hud")

        # Speed gauge
        spd_pct = (self._speed - BASE_SPEED) / (MAX_SPEED - BASE_SPEED)
        gauge_x, gauge_y = CANVAS_W - 110, 18
        gauge_w = 90
        c.create_rectangle(gauge_x, gauge_y, gauge_x + gauge_w, gauge_y + 12,
                           fill="#222222", outline="#555555", tags="hud")
        c.create_rectangle(gauge_x + 2, gauge_y + 2,
                           gauge_x + 2 + (gauge_w - 4) * spd_pct,
                           gauge_y + 10,
                           fill="#44ff44" if spd_pct < 0.6 else
                                "#ffaa44" if spd_pct < 0.85 else "#ff4444",
                           outline="", tags="hud")
        c.create_text(gauge_x + gauge_w / 2, gauge_y - 8,
                      text=f"Speed: {int(self._speed * 10)}",
                      fill="#cccccc", font=("Segoe UI", 8), tags="hud")

        # Pause overlay
        if self.paused:
            c.create_rectangle(0, 0, CANVAS_W, CANVAS_H,
                               fill="#1a1a2e", tags="hud")
            c.create_text(CANVAS_W / 2, CANVAS_H / 2,
                          text="⏸  PAUSED\n\nPress P to resume",
                          fill="#ffffff", font=("Segoe UI", 22, "bold"),
                          justify="center", tags="hud")

        # Game‑over overlay
        if self.game_over:
            c.create_rectangle(0, 0, CANVAS_W, CANVAS_H,
                               fill="#1a1a2e", tags="hud")
            c.create_text(CANVAS_W / 2, CANVAS_H / 2 - 30,
                          text="💥  CRASH!",
                          fill="#ff4444", font=("Segoe UI", 28, "bold"),
                          tags="hud")
            c.create_text(CANVAS_W / 2, CANVAS_H / 2 + 20,
                          text=f"Score: {self.score}    Coins: {self.coin_count}",
                          fill="#ffffff", font=("Segoe UI", 14),
                          tags="hud")
            c.create_text(CANVAS_W / 2, CANVAS_H / 2 + 55,
                          text="Press  R  to race again!",
                          fill="#ffd700", font=("Segoe UI", 13, "bold"),
                          tags="hud")


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  App                                                                    ║
# ╚══════════════════════════════════════════════════════════════════════════╝

class App:
    """Main window + game loop."""

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Chubby Car Racer  🏎️")
        self.root.resizable(False, False)
        self.root.configure(bg="#111111")

        self.canvas = tk.Canvas(
            self.root, width=CANVAS_W, height=CANVAS_H,
            bg=BG, highlightthickness=0,
        )
        self.canvas.pack()

        self.game = ChubbyRacer(self.canvas)

        self._bind_keys()
        self._loop()

    def _bind_keys(self) -> None:
        r = self.root
        r.bind("<KeyPress-Left>",  lambda e: self.game.steer_left(True))
        r.bind("<KeyRelease-Left>", lambda e: self.game.steer_left(False))
        r.bind("<KeyPress-Right>", lambda e: self.game.steer_right(True))
        r.bind("<KeyRelease-Right>", lambda e: self.game.steer_right(False))
        r.bind("<KeyPress-a>", lambda e: self.game.steer_left(True))
        r.bind("<KeyRelease-a>", lambda e: self.game.steer_left(False))
        r.bind("<KeyPress-d>", lambda e: self.game.steer_right(True))
        r.bind("<KeyRelease-d>", lambda e: self.game.steer_right(False))
        r.bind("<KeyPress-p>", lambda e: self.game.toggle_pause())
        r.bind("<KeyPress-r>", lambda e: self.game.restart())

    def _loop(self) -> None:
        self.game.tick()
        self.game.render()
        self.root.after(FRAME_MS, self._loop)

    def run(self) -> None:
        self.root.geometry(f"{CANVAS_W}x{CANVAS_H}")
        self.root.mainloop()


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  Entry point                                                            ║
# ╚══════════════════════════════════════════════════════════════════════════╝

if __name__ == "__main__":
    App().run()
