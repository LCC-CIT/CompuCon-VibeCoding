"""WWE Memory Match — a themed concentration game in a Tkinter GUI.

Ten WWE Superstars are hidden across a grid of face-down cards. The player
flips two cards at a time; a matching pair stays face up, a mismatch flips
back over. A move counter tracks every pair of flips until all ten pairs
have been found.

The game launches full screen. Press Esc to switch to a windowed mode.
"""

import math
import os
import random
import threading
import tkinter as tk

# Pillow is used only to show real wrestler photos on the cards; the game
# still works without it (cards fall back to emoji).
try:
    from PIL import Image, ImageTk
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

# Windows sound support for the win celebration (works without any audio
# files: a built-in fanfare plays unless the real clip is present).
try:
    import winsound
    HAVE_SOUND = True
except ImportError:
    HAVE_SOUND = False

# OpenCV plays a user-supplied video of the title win inside the celebration
# (optional — without it, a static photo-and-belt scene is shown instead).
try:
    import cv2
    HAS_CV2 = True
except ImportError:
    HAS_CV2 = False


def _mci_play(path):
    """Play an MP3 through the Windows MCI API (no extra dependencies)."""
    try:
        import ctypes
        mci = ctypes.windll.winmm.mciSendStringW
        mci.restype = ctypes.c_uint
        if mci('open "{}" type mpegvideo alias wwewin'.format(path), None, 0, None) != 0:
            return False
        mci("play wwewin", None, 0, None)
        return True
    except Exception:
        return False


def _mci_stop():
    try:
        import ctypes
        ctypes.windll.winmm.mciSendStringW("stop wwewin", None, 0, None)
        ctypes.windll.winmm.mciSendStringW("close wwewin", None, 0, None)
    except Exception:
        pass

# ---------------------------------------------------------------------------
# Game data
# ---------------------------------------------------------------------------

# Each wrestler: (name, emoji, accent colour) — emoji is the no-photo fallback.
WRESTLERS = [
    ("Joe Hendry",     "🎵", "#e0a020"),
    ("Solo Sikoa",     "☝️", "#2f6db0"),
    ("The Undertaker", "⚰️", "#7a4aa0"),
    ("Ethan Page",     "🎬", "#e07020"),
    ("Seth Rollins",   "🏆", "#8a8a96"),
    ("Liv Morgan",     "💜", "#c060c8"),
    ("Bianca Belair",  "🦁", "#b0763a"),
    ("Becky Lynch",    "☘️", "#3fae5a"),
    ("Iyo Sky",        "🌙", "#2f9aa8"),
    ("Rhea Ripley",    "🖤", "#c8405a"),
]

NUM_PAIRS = len(WRESTLERS)

# ---------------------------------------------------------------------------
# Grid constants
# ---------------------------------------------------------------------------

COLS, ROWS = 5, 4
CARD_ASPECT = 132.0 / 150.0   # card width : height

# ---------------------------------------------------------------------------
# WWE palette
# ---------------------------------------------------------------------------

BG = "#0a0a0c"        # arena background
GLOW = "#5c0e16"      # soft red arena glow
ROPE = "#8a1218"      # ring-rope red
GOLD = "#f0c060"      # title / accents
GOLD_DARK = "#a87b1f"
FACE_BG = "#efe6d8"   # card face (cardboard-ish)
MISS = "#ff3b3b"      # mismatch flash

IMAGE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wwe_images")


class WweMemoryMatch:
    def __init__(self, root):
        self.root = root
        self.root.title("WWE Memory Match")
        self.root.configure(bg=BG)
        self.root.resizable(True, True)

        self.header_widgets = []
        self.canvas = None
        self.deck = []
        self.images = {}
        self.fullscreen = True
        self.matched = set()
        self.up = []
        self.moves = 0
        self.pairs_found = 0
        self.busy = False
        self.win_btn = None
        self.win_photo = None
        self.win_belt = None
        self.fanfare_stop = False
        self.confetti = []
        self.confetti_job = None
        self.cap = None
        self.video_job = None
        self.video_tkimg = None
        self.video_image_id = None
        self.video_w = 0
        self.video_h = 0

        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: self.toggle_fullscreen())

        self.best = self.load_best()
        self.is_record = False
        self.compute_layout()
        self.create_canvas()
        self.build_header()
        self.load_images()
        self.new_game()

    # ------------------------------------------------------------------
    # Layout (everything scales to fill the screen)
    # ------------------------------------------------------------------

    def compute_layout(self):
        self.root.update_idletasks()
        self.screen_w = self.root.winfo_screenwidth()
        self.screen_h = self.root.winfo_screenheight()

        if self.fullscreen:
            w, h = self.screen_w, self.screen_h
        else:
            w = self.root.winfo_width()
            h = self.root.winfo_height()
            if w < 100 or h < 100:      # window not mapped yet
                w, h = min(self.screen_w, 840), min(self.screen_h, 920)

        self.win_w, self.win_h = w, h
        pad = max(14, int(0.02 * w))

        # Header zones
        self.title_y = int(0.050 * h)
        self.sub_y = int(0.112 * h)
        self.stats_y = int(0.155 * h)
        grid_top = int(0.200 * h)
        bottom_pad = int(0.045 * h)

        # Size the 5x4 grid to fill the remaining space
        avail_w = w - 2 * pad
        avail_h = h - grid_top - bottom_pad
        gap_ratio = 0.09
        cw_from_w = avail_w / (COLS + (COLS - 1) * gap_ratio)
        cw_from_h = (avail_h / (ROWS + (ROWS - 1) * gap_ratio)) * CARD_ASPECT
        self.cw = max(60, int(min(cw_from_w, cw_from_h)))
        self.ch = int(self.cw / CARD_ASPECT)
        self.gap = int(self.cw * gap_ratio)

        grid_w = COLS * self.cw + (COLS - 1) * self.gap
        grid_h = ROWS * self.ch + (ROWS - 1) * self.gap
        self.margin_x = (w - grid_w) / 2
        self.margin_y = grid_top + (avail_h - grid_h) / 2
        self.name_strip = max(22, int(self.ch * 0.17))   # photo caption strip

        # Fonts scale with screen/card size
        self.font_title = ("Arial Black", max(20, min(64, int(0.030 * w))), "bold")
        self.font_sub = ("Arial", max(11, min(22, int(0.013 * w))))
        self.font_stat = ("Arial", max(13, min(28, int(0.017 * w))), "bold")
        self.font_btn = ("Arial", max(12, min(24, int(0.015 * w))), "bold")
        self.font_hint = ("Arial", max(9, min(16, int(0.010 * w))))
        self.font_emblem = ("Arial Black", max(8, int(self.cw * 0.11)), "bold")
        self.font_emoji = ("Segoe UI Emoji", max(16, int(self.ch * 0.32)))
        self.font_name = ("Arial", max(8, int(self.ch * 0.09)), "bold")
        self.font_mini = ("Arial Black", max(5, int(self.cw * 0.06)), "bold")
        self.font_star = ("Segoe UI Emoji", max(7, int(self.cw * 0.09)))
        self.font_water = ("Arial Black", max(14, int(self.cw * 0.85)), "bold")

    def create_canvas(self):
        # Canvas first so the header widgets sit above it
        self.canvas = tk.Canvas(self.root, width=self.win_w, height=self.win_h,
                                bg=BG, highlightthickness=0, bd=0)
        self.canvas.place(x=0, y=0)

    def build_header(self):
        h = self.win_h

        title_row = tk.Frame(self.root, bg=BG)
        title_row.place(relx=0.5, y=self.title_y, anchor="n")
        tk.Label(title_row, text="WWE ", font=self.font_title, fg="#d02222", bg=BG).pack(side="left")
        tk.Label(title_row, text="Memory Match", font=self.font_title, fg=GOLD, bg=BG).pack(side="left")

        sub = tk.Label(self.root, text=f"Flip two cards · find all {NUM_PAIRS} pairs",
                       font=self.font_sub, fg="#9a9a9a", bg=BG)
        sub.place(relx=0.5, y=self.sub_y, anchor="n")

        stats = tk.Frame(self.root, bg=BG)
        stats.place(relx=0.5, y=self.stats_y, anchor="n")
        self.moves_var = tk.StringVar(value="Moves: 0")
        self.pairs_var = tk.StringVar(value=f"Pairs: 0/{NUM_PAIRS}")
        self.best_var = tk.StringVar(value=self.best_text())
        tk.Label(stats, textvariable=self.moves_var, font=self.font_stat,
                 fg="#ffffff", bg=BG).pack(side="left", padx=14)
        tk.Label(stats, textvariable=self.pairs_var, font=self.font_stat,
                 fg="#ffffff", bg=BG).pack(side="left", padx=14)
        tk.Label(stats, textvariable=self.best_var, font=self.font_stat,
                 fg=GOLD, bg=BG).pack(side="left", padx=14)
        tk.Button(stats, text="↻ Reset", font=self.font_btn, fg=GOLD, bg="#1d1d24",
                  activeforeground=GOLD, activebackground="#2a2a33", relief="flat",
                  padx=12, pady=3, command=self.new_game, cursor="hand2").pack(side="left", padx=14)

        hint_text = "Press Esc to exit full screen" if self.fullscreen else "Press Esc for full screen"
        hint = tk.Label(self.root, text=hint_text, font=self.font_hint, fg="#55555e", bg=BG)
        hint.place(relx=0.5, rely=1.0, y=-int(0.018 * h), anchor="s")

        self.header_widgets = [title_row, sub, stats, hint]

    # ------------------------------------------------------------------
    # Arena background
    # ------------------------------------------------------------------

    def draw_background(self):
        c = self.canvas
        w, h = self.win_w, self.win_h
        c.delete("bg")
        c.create_rectangle(0, 0, w, h, fill=BG, outline="", tags="bg")

        # Soft red arena glows (stippled for a translucent look)
        gw = w * 0.30
        c.create_oval(-gw, -gw, w * 0.42, h * 0.30, fill=GLOW, stipple="gray50", outline="", tags="bg")
        c.create_oval(-gw * 0.5, -gw * 0.4, w * 0.32, h * 0.22, fill=GLOW, stipple="gray25", outline="", tags="bg")
        c.create_oval(w - w * 0.42, h - h * 0.30, w + gw, h + gw, fill=GLOW, stipple="gray50", outline="", tags="bg")
        c.create_oval(w - w * 0.32, h - h * 0.22, w + gw * 0.5, h + gw * 0.4, fill=GLOW, stipple="gray25", outline="", tags="bg")

        # Ring ropes framing the screen (top and bottom)
        rope_w = max(3, int(w * 0.003))
        pad = max(5, int(w * 0.004))
        for yy in (int(h * 0.008), int(h * 0.014)):
            c.create_line(4, yy, w - 4, yy, fill=ROPE, width=rope_w, tags="bg")
            c.create_rectangle(-2, yy - pad, 18, yy + pad, fill=GOLD_DARK, outline="", tags="bg")
            c.create_rectangle(w - 18, yy - pad, w + 2, yy + pad, fill=GOLD_DARK, outline="", tags="bg")
        for yy in (h - int(h * 0.014), h - int(h * 0.008)):
            c.create_line(4, yy, w - 4, yy, fill=ROPE, width=rope_w, tags="bg")
            c.create_rectangle(-2, yy - pad, 18, yy + pad, fill=GOLD_DARK, outline="", tags="bg")
            c.create_rectangle(w - 18, yy - pad, w + 2, yy + pad, fill=GOLD_DARK, outline="", tags="bg")

        # Faint wordmark watermark behind the cards
        c.create_text(w / 2, h / 2, text="★ WWE ★", font=self.font_water, fill="#17171f", tags="bg")

    # ------------------------------------------------------------------
    # Wrestler photos
    # ------------------------------------------------------------------

    def load_images(self):
        """Load and pre-size each wrestler's photo for the card faces."""
        self.images = {}
        if not HAS_PIL:
            return
        max_w = int(self.cw * 0.84)
        max_h = self.ch - self.name_strip - int(self.ch * 0.06)
        for name, _emoji, _accent in WRESTLERS:
            slug = name.lower().replace(" ", "_")
            path = os.path.join(IMAGE_DIR, slug + ".jpg")
            if not os.path.exists(path):
                path = os.path.join(IMAGE_DIR, slug + ".png")
            if os.path.exists(path):
                try:
                    self.images[name] = self.fit_photo(path, max_w, max_h)
                except Exception:
                    pass  # no photo -> that card falls back to its emoji

    def fit_photo(self, path, max_w, max_h):
        with Image.open(path) as im:
            im = im.convert("RGB")
            im.thumbnail((max_w, max_h), Image.LANCZOS)
            return ImageTk.PhotoImage(im)

    # ------------------------------------------------------------------
    # Card helpers
    # ------------------------------------------------------------------

    def card_rect(self, idx):
        col = idx % COLS
        row = idx // COLS
        x0 = self.margin_x + col * (self.cw + self.gap)
        y0 = self.margin_y + row * (self.ch + self.gap)
        return x0, y0, x0 + self.cw, y0 + self.ch

    def draw_card(self, idx, face_up, outline=None, outline_width=3):
        tag = f"c{idx}"
        c = self.canvas
        c.delete(tag)
        x0, y0, x1, y1 = self.card_rect(idx)
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        name, emoji, accent = self.deck[idx]

        if not face_up:
            # Face-down: dark card, gold border, WWE emblem
            c.create_rectangle(x0, y0, x1, y1, fill="#17171d", outline=GOLD_DARK,
                               width=outline_width, tags=tag)
            r = self.ch * 0.23
            c.create_oval(cx - r, cy - r, cx + r, cy + r, outline=GOLD, width=3, tags=tag)
            c.create_text(cx, cy, text="WWE", font=self.font_emblem, fill=GOLD, tags=tag)
            c.create_text(x0 + self.cw * 0.12, y0 + self.ch * 0.11, text="★",
                          font=self.font_star, fill=ROPE, tags=tag)
            c.create_text(x1 - self.cw * 0.12, y1 - self.ch * 0.11, text="★",
                          font=self.font_star, fill=ROPE, tags=tag)
        else:
            # Face-up: light card, wrestler photo + name
            c.create_rectangle(x0, y0, x1, y1, fill=FACE_BG, outline=outline or accent,
                               width=outline_width, tags=tag)
            photo = self.images.get(name)
            if photo is not None:
                # Photo sits above the name strip
                c.create_image(cx, y0 + self.ch * 0.06 + (self.ch - self.name_strip) / 2,
                               image=photo, tags=tag)
            else:
                # No photo available: show the wrestler emoji instead
                c.create_text(x0 + self.cw * 0.08, y0 + self.ch * 0.06, text="WWE",
                              font=self.font_mini, fill="#9c9c9c", anchor="nw", tags=tag)
                c.create_text(cx, y0 + self.ch * 0.38, text=emoji, font=self.font_emoji, tags=tag)
            c.create_text(cx, y1 - self.name_strip / 2, text=name, font=self.font_name,
                          fill=accent, tags=tag)

        c.tag_bind(tag, "<Button-1>", lambda e, i=idx: self.on_card_click(i))

    def animate_flip(self, idx, to_face_up):
        """Squash the card flat, swap its face, then expand it back."""
        tag = f"c{idx}"
        x0, y0, x1, y1 = self.card_rect(idx)
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2

        steps = 4
        squash = 0.35
        grow = 1.0 / squash

        def expand(k):
            if k > 0:
                self.canvas.scale(tag, cx, cy, grow, 1.0)
                self.root.after(15, expand, k - 1)
            else:
                self.draw_card(idx, to_face_up)  # redraw at exact coords

        def squash_stage(k):
            if k < steps:
                self.canvas.scale(tag, cx, cy, squash, 1.0)
                self.root.after(15, squash_stage, k + 1)
            else:
                self.draw_card(idx, to_face_up)  # swap content while flat
                self.root.after(15, expand, steps)

        squash_stage(0)

    # ------------------------------------------------------------------
    # Best-score record
    # ------------------------------------------------------------------

    def load_best(self):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wwe_memory_best.txt")
        try:
            with open(path, encoding="utf-8") as f:
                return int(f.read().strip())
        except Exception:
            return None

    def save_best(self):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wwe_memory_best.txt")
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(str(self.best))
        except Exception:
            pass

    def best_text(self):
        return f"Best: {self.best}" if self.best is not None else "Best: --"

    # ------------------------------------------------------------------
    # Game logic
    # ------------------------------------------------------------------

    def new_game(self):
        self.teardown_win()
        self.deck = [w for w in WRESTLERS for _ in range(2)]
        random.shuffle(self.deck)
        self.up = []                 # currently face-up (unresolved) card indices
        self.matched = set()         # indices that are permanently matched
        self.moves = 0
        self.pairs_found = 0
        self.busy = False
        self.draw_background()
        for i in range(len(self.deck)):
            self.draw_card(i, False)
        self.update_stats()

    def update_stats(self):
        self.moves_var.set(f"Moves: {self.moves}")
        self.pairs_var.set(f"Pairs: {self.pairs_found}/{NUM_PAIRS}")
        self.best_var.set(self.best_text())

    def on_card_click(self, idx):
        if self.busy or len(self.up) >= 2:
            return
        if idx in self.matched or idx in self.up:
            return
        self.up.append(idx)
        self.animate_flip(idx, True)

        if len(self.up) < 2:
            return

        i0, i1 = self.up
        self.moves += 1
        self.update_stats()

        if self.deck[i0][0] == self.deck[i1][0]:
            # Match — the pair stays face up
            self.matched.update([i0, i1])
            self.pairs_found += 1
            self.up.clear()
            self.update_stats()
            self.celebrate_match(i0, i1)
            if self.pairs_found == NUM_PAIRS:
                self.root.after(450, self.show_win)
        else:
            # Mismatch — flash red, then flip both back
            self.busy = True
            self.root.after(650, lambda: self.reveal_mismatch(i0, i1))

    def reveal_mismatch(self, i0, i1):
        for i in (i0, i1):
            self.draw_card(i, True, outline=MISS, outline_width=4)
        self.root.after(300, lambda: self.flip_back(i0, i1))

    def flip_back(self, i0, i1):
        self.animate_flip(i0, False)
        self.animate_flip(i1, False)
        self.up.clear()
        self.busy = False

    def celebrate_match(self, i0, i1):
        for i in (i0, i1):
            self.draw_card(i, True, outline=GOLD, outline_width=4)
        self.root.after(250, lambda: self.draw_card(i0, True))
        self.root.after(250, lambda: self.draw_card(i1, True))

    def show_win(self):
        self.is_record = self.best is None or self.moves < self.best
        if self.is_record:
            self.best = self.moves
            self.save_best()
        self.update_stats()
        self.draw_win_scene()
        self.start_confetti()
        self.play_win_sound()

    def draw_win_scene(self):
        """Joe Hendry's NXT Championship win — Wii Sports style."""
        c = self.canvas
        w, h = self.win_w, self.win_h

        # Dim the board behind the celebration
        c.create_rectangle(0, 0, w, h, fill="#000000", stipple="gray50", outline="", tags="win")

        # --- Wii Sports-style "You win!" banner ---
        bw = min(int(0.52 * w), 460)
        bh = int(0.11 * h)
        bx0, by0 = w / 2 - bw / 2, int(0.20 * h)
        bx1, by1 = bx0 + bw, by0 + bh
        c.create_rectangle(bx0, by0, bx1, by1, fill="#b02a2a", outline=GOLD,
                           width=max(4, int(w * 0.005)), tags="win")
        c.create_rectangle(bx0 + 8, by0 + 8, bx1 - 8, by1 - 8, fill="#c22a2a", outline="", tags="win")
        c.create_text(w / 2, by0 + bh / 2, text="You win!",
                      font=("Arial Black", int(0.052 * w), "bold"), fill="#ffffff", tags="win")
        c.create_text(bx0 + bw * 0.13, by0 + bh / 2, text="★",
                      font=("Segoe UI Emoji", int(0.045 * w)), fill=GOLD, tags="win")
        c.create_text(bx1 - bw * 0.13, by0 + bh / 2, text="★",
                      font=("Segoe UI Emoji", int(0.045 * w)), fill=GOLD, tags="win")

        # --- The title win: play the user's clip if present, else a static scene ---
        video = self.find_video()
        if not (video and HAS_CV2 and self.start_video(video, w, h)):
            photo = self.get_scene_photo(os.path.join(IMAGE_DIR, "joe_hendry.jpg"),
                                         int(0.22 * w), int(0.22 * h))
            if photo is not None:
                self.win_photo = photo
                pw, ph = photo.width(), photo.height()
                fx, fy = w / 2, int(0.42 * h)
                pad = 12
                c.create_rectangle(fx - pw / 2 - pad, fy - ph / 2 - pad, fx + pw / 2 + pad,
                                   fy + ph / 2 + pad, fill=GOLD, outline="#7a1414", width=4, tags="win")
                c.create_image(fx, fy, image=photo, tags="win")
            belt = self.get_scene_photo(os.path.join(IMAGE_DIR, "nxt_belt.png"),
                                        int(0.36 * w), int(0.13 * h))
            if belt is not None:
                self.win_belt = belt
                c.create_image(w / 2, int(0.60 * h), image=belt, tags="win")

        # --- NXT CHAMPION banner ---
        cy = int(0.67 * h)
        c.create_text(w / 2 + 2, cy + 2, text="★ NXT CHAMPION ★",
                      font=("Arial Black", int(0.030 * w), "bold"), fill="#000000", tags="win")
        c.create_text(w / 2, cy, text="★ NXT CHAMPION ★",
                      font=("Arial Black", int(0.030 * w), "bold"), fill=GOLD, tags="win")

        # --- NEW RECORD badge (when the player beats their best score) ---
        if self.is_record:
            byy = int(0.72 * h)
            bw2 = int(0.30 * w)
            bh2 = int(0.055 * h)
            c.create_oval(w / 2 - bw2 / 2, byy - bh2 / 2, w / 2 + bw2 / 2, byy + bh2 / 2,
                          fill=GOLD, outline=GOLD_DARK, width=3, tags="win")
            c.create_text(w / 2, byy, text="★ NEW RECORD! ★",
                          font=("Arial Black", int(0.020 * w), "bold"), fill="#5c0e16", tags="win")

        # --- result line ---
        c.create_text(w / 2, int(0.78 * h),
                      text=f"You found all {NUM_PAIRS} pairs in {self.moves} moves!",
                      font=("Arial", int(0.018 * w)), fill="#ffffff", tags="win")

        # --- Play Again button ---
        self.win_btn = tk.Button(self.root, text="▶  Play Again", font=self.font_btn,
                                 fg=GOLD, bg="#1d1d24", activeforeground=GOLD,
                                 activebackground="#2a2a33", relief="flat",
                                 padx=16, pady=4, command=self.new_game, cursor="hand2")
        self.win_btn.place(relx=0.5, y=int(0.82 * h), anchor="n")

    def get_scene_photo(self, path, max_w, max_h):
        if not HAS_PIL or not os.path.exists(path):
            return None
        try:
            with Image.open(path) as im:
                if im.mode not in ("RGB", "RGBA"):
                    im = im.convert("RGBA")
                im.thumbnail((max_w, max_h), Image.LANCZOS)
                return ImageTk.PhotoImage(im)
        except Exception:
            return None

    # ------------------------------------------------------------------
    # Title-win video (a clip the user drops next to the game)
    # ------------------------------------------------------------------

    def find_video(self):
        base = os.path.dirname(os.path.abspath(__file__))
        for name in ("joe_hendry_win.mp4", "joe_hendry_win.avi", "joe_hendry_win.mov",
                     "joe_hendry_win.mkv", "nxt_win.mp4", "joe_hendry_champion.mp4"):
            path = os.path.join(base, name)
            if os.path.exists(path):
                return path
        return None

    def start_video(self, path, w, h):
        """Open the clip and begin rendering its frames into the canvas."""
        try:
            self.cap = cv2.VideoCapture(path)
            if not self.cap.isOpened():
                self.cap = None
                return False
        except Exception:
            self.cap = None
            return False

        vw = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        vh = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        if vw <= 0 or vh <= 0:
            self.cap.release()
            self.cap = None
            return False

        scale = min((0.50 * w) / vw, (0.44 * h) / vh)
        self.video_w = max(120, int(vw * scale))
        self.video_h = max(90, int(vh * scale))

        ok, frame = self.cap.read()
        if not ok:
            self.cap.release()
            self.cap = None
            return False
        self.video_tkimg = self._frame_to_photo(frame)

        vc = (w / 2, int(0.44 * h))
        self.canvas.create_rectangle(
            vc[0] - self.video_w / 2 - 8, vc[1] - self.video_h / 2 - 8,
            vc[0] + self.video_w / 2 + 8, vc[1] + self.video_h / 2 + 8,
            fill="#000000", outline=GOLD, width=3, tags="win")
        self.video_image_id = self.canvas.create_image(vc[0], vc[1], image=self.video_tkimg, tags="win")
        self.video_job = self.root.after(33, self.video_tick)
        return True

    def _frame_to_photo(self, frame):
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        img = img.resize((self.video_w, self.video_h), Image.LANCZOS)
        return ImageTk.PhotoImage(img)

    def video_tick(self):
        if self.cap is None:
            self.video_job = None
            return
        ok, frame = self.cap.read()
        if not ok:
            self.stop_video()          # clip finished; keep the last frame up
            return
        self.video_tkimg = self._frame_to_photo(frame)
        self.canvas.itemconfig(self.video_image_id, image=self.video_tkimg)
        self.video_job = self.root.after(33, self.video_tick)

    def stop_video(self):
        if self.video_job is not None:
            self.root.after_cancel(self.video_job)
            self.video_job = None
        if self.cap is not None:
            try:
                self.cap.release()
            except Exception:
                pass
            self.cap = None

    # ------------------------------------------------------------------
    # Confetti
    # ------------------------------------------------------------------

    def start_confetti(self):
        if self.confetti_job is not None:
            return
        c = self.canvas
        colors = ["#d02222", GOLD, "#ffffff", "#e07020", "#7a4aa0", "#3fae5a", "#c060c8", "#2f6db0"]
        self.confetti = []
        for _ in range(70):
            size = random.randint(7, 15)
            x = random.randint(0, self.win_w)
            y = random.randint(-self.win_h, 0)
            col = random.choice(colors)
            roll = random.random()
            if roll < 0.5:
                it = c.create_rectangle(x, y, x + size, y + size * 0.6, fill=col, outline="", tags="win")
            elif roll < 0.8:
                it = c.create_oval(x, y, x + size, y + size, fill=col, outline="", tags="win")
            else:
                it = c.create_line(x, y, x + size, y + size * 0.8, fill=col, width=2, tags="win")
            self.confetti.append({"id": it, "amp": random.uniform(0.5, 1.6),
                                  "dy": random.uniform(2.5, 6.0), "t": random.uniform(0, 6.28)})
        self.confetti_job = self.root.after(30, self.confetti_tick)

    def confetti_tick(self):
        self.confetti_job = self.root.after(30, self.confetti_tick)
        c = self.canvas
        for p in self.confetti:
            it = p["id"]
            if not c.type(it):      # item was cleaned up
                continue
            c.move(it, p["amp"] * math.sin(p["t"]), p["dy"])
            p["t"] += 0.25
            if c.coords(it)[1] > self.win_h + 24:
                c.moveto(it, random.randint(0, self.win_w), random.randint(-120, -24))

    def stop_confetti(self):
        if self.confetti_job is not None:
            self.root.after_cancel(self.confetti_job)
            self.confetti_job = None
        self.confetti = []

    # ------------------------------------------------------------------
    # Win sound ("Here Comes the Money" if you drop the clip in)
    # ------------------------------------------------------------------

    def play_win_sound(self):
        if not HAVE_SOUND:
            return
        base = os.path.dirname(os.path.abspath(__file__))
        wav = os.path.join(base, "here_comes_the_money.wav")
        mp3 = os.path.join(base, "here_comes_the_money.mp3")
        if os.path.exists(wav):
            winsound.PlaySound(wav, winsound.SND_ASYNC | winsound.SND_FILENAME)
        elif os.path.exists(mp3):
            _mci_play(mp3)
        else:
            self.play_fanfare()

    def stop_win_sound(self):
        if not HAVE_SOUND:
            return
        try:
            winsound.PlaySound(None, winsound.SND_PURGE)
        except Exception:
            pass
        _mci_stop()
        self.fanfare_stop = True

    def play_fanfare(self):
        """Built-in victory jingle (used when the real clip isn't present)."""
        self.fanfare_stop = False
        notes = [(523, 140), (659, 140), (784, 140), (1047, 120), (784, 120), (1047, 160), (1319, 220)]

        def run():
            try:
                for freq, ms in notes:
                    if self.fanfare_stop:
                        break
                    winsound.Beep(freq, ms)
            except Exception:
                pass

        threading.Thread(target=run, daemon=True).start()

    # ------------------------------------------------------------------
    # Win teardown
    # ------------------------------------------------------------------

    def teardown_win(self):
        self.stop_video()
        self.stop_confetti()
        self.stop_win_sound()
        if self.win_btn is not None:
            try:
                self.win_btn.destroy()
            except Exception:
                pass
            self.win_btn = None
        if self.canvas is not None:
            self.canvas.delete("win")

    # ------------------------------------------------------------------
    # Full screen toggling
    # ------------------------------------------------------------------

    def toggle_fullscreen(self):
        self.set_fullscreen(not self.fullscreen)

    def set_fullscreen(self, on):
        self.fullscreen = on
        if on:
            self.root.attributes("-fullscreen", True)
        else:
            self.root.attributes("-fullscreen", False)
            ww = min(self.screen_w, 840)
            wh = min(self.screen_h, 920)
            self.root.geometry(f"{ww}x{wh}+{(self.screen_w - ww) // 2}+{(self.screen_h - wh) // 2}")
        self.rebuild()

    def rebuild(self):
        # Rebuild the screen layout, keeping the game state intact
        self.teardown_win()
        matched = set(self.matched)
        moves, pairs = self.moves, self.pairs_found

        for wgt in self.header_widgets:
            wgt.destroy()
        self.header_widgets = []
        if self.canvas is not None:
            self.canvas.destroy()

        self.compute_layout()
        self.create_canvas()
        self.build_header()
        self.draw_background()
        for i in range(len(self.deck)):
            self.draw_card(i, i in matched)

        self.matched = matched
        self.up.clear()
        self.busy = False
        self.moves, self.pairs_found = moves, pairs
        self.update_stats()


def main():
    root = tk.Tk()
    WweMemoryMatch(root)
    root.mainloop()


if __name__ == "__main__":
    main()
