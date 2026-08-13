"""Wild West Hangman — a themed word-guessing game in a tkinter GUI.

The app picks a secret word. The user guesses one letter at a time; every
place that letter appears is filled in, and each wrong guess adds a new part
of a cowboy to the gallows. The game ends when the word is complete or the
cowboy has been drawn in full.
"""

import random
import tkinter as tk
from tkinter import messagebox

# ---------------------------------------------------------------------------
# Game rules
# ---------------------------------------------------------------------------

MAX_WRONG = 6  # hat, face, bandana, torso, arms, legs

WORDS = [
    "apple", "banana", "castle", "dragon", "elephant", "forest", "guitar",
    "hammer", "island", "jungle", "kangaroo", "lantern", "mountain", "needle",
    "orange", "pencil", "quartz", "river", "sandwich", "tunnel", "umbrella",
    "volcano", "window", "zebra", "keyboard", "bicycle", "chocolate", "dolphin",
    # wild-west flavour
    "cowboy", "sheriff", "outlaw", "saddle", "desert", "cactus", "saloon",
    "lasso", "holster", "rancher", "buffalo", "pistol", "badge", "mesa",
    "prairie", "wagon", "railroad", "bounty", "tumbleweed", "prospector",
]


def pick_word():
    return random.choice(WORDS)


# ---------------------------------------------------------------------------
# Wild-west palette
# ---------------------------------------------------------------------------

BG_DARK = "#3b2a1c"          # window background (leather/wood)
GOLD = "#f0c060"             # title / accents
CREAM = "#f5e6c8"            # revealed word text
TAN = "#c9b08a"              # secondary text
SIGN = "#20160b"             # word "sign board" background
BTN_BG = "#f0d9a0"           # letter buttons
BTN_FG = "#5b3a1e"
BTN_DISABLED = "#4a4032"
BTN_DISABLED_FG = "#9a8f78"
NEWGAME_BG = "#b0452d"
NEWGAME_ACTIVE = "#8e2a1f"
WIN_COLOR = "#6fcf6f"
LOSE_COLOR = "#e07050"

WOOD = "#7a5533"             # gallows timber
WOOD_DK = "#5b3d22"
ROPE = "#e6c887"
HAT = "#8a5a2b"              # cowboy colours
HAT_DK = "#5f3d1c"
SKIN = "#e8b48a"
SKIN_DK = "#b07a4a"
BANDANA = "#c0392b"
BANDANA_DK = "#8e2a1f"
JEANS = "#2e5fa3"
BOOT = "#5b3a1e"
CACTUS = "#2f5d3a"
CACTUS_DK = "#23492d"

CANVAS_W = 340
CANVAS_H = 320


# ---------------------------------------------------------------------------
# Cowboy drawing steps — one function per wrong guess
# ---------------------------------------------------------------------------

def _draw_hat(c):
    c.create_oval(121, 50, 179, 84, fill=HAT, outline=HAT_DK, width=2, tags="body")   # crown
    c.create_oval(106, 66, 194, 88, fill=HAT, outline=HAT_DK, width=2, tags="body")   # brim


def _draw_face(c):
    c.create_oval(130, 82, 170, 120, fill=SKIN, outline=SKIN_DK, width=2, tags="body")


def _draw_bandana(c):
    c.create_polygon(138, 118, 162, 118, 150, 138,
                     fill=BANDANA, outline=BANDANA_DK, width=2, tags="body")
    c.create_oval(135, 115, 143, 123, fill=BANDANA, outline=BANDANA_DK, tags="body")   # knots
    c.create_oval(157, 115, 165, 123, fill=BANDANA, outline=BANDANA_DK, tags="body")


def _draw_torso(c):
    c.create_line(150, 140, 150, 208, fill=JEANS, width=7, tags="body")


def _draw_arms(c):
    c.create_line(150, 158, 112, 190, fill=JEANS, width=6, tags="body")
    c.create_line(150, 158, 188, 190, fill=JEANS, width=6, tags="body")
    c.create_oval(108, 186, 116, 194, fill=SKIN, outline=SKIN_DK, width=1, tags="body")   # hands
    c.create_oval(184, 186, 192, 194, fill=SKIN, outline=SKIN_DK, width=1, tags="body")


def _draw_legs(c):
    c.create_line(150, 208, 124, 260, fill=JEANS, width=6, tags="body")
    c.create_line(150, 208, 176, 260, fill=JEANS, width=6, tags="body")
    c.create_line(116, 262, 132, 262, fill=BOOT, width=5, tags="body")   # boots
    c.create_line(168, 262, 184, 262, fill=BOOT, width=5, tags="body")


DRAW_STEPS = [_draw_hat, _draw_face, _draw_bandana, _draw_torso, _draw_arms, _draw_legs]


def _draw_cactus(c, cx):
    """A small saguaro silhouette centred at horizontal position cx."""
    for x0, y0, x1, y1 in (
        (cx - 4, 258, cx + 4, 312),    # trunk
        (cx - 13, 270, cx - 4, 286),   # left arm
        (cx - 13, 266, cx - 9, 270),   # left elbow
        (cx + 4, 272, cx + 13, 288),   # right arm
        (cx + 9, 268, cx + 13, 272),   # right elbow
    ):
        c.create_rectangle(x0, y0, x1, y1, fill=CACTUS, outline=CACTUS_DK)


# ---------------------------------------------------------------------------
# Game logic (kept independent of the GUI so it is easy to test)
# ---------------------------------------------------------------------------

class HangmanGame:
    """Holds the state for one round of hangman."""

    def __init__(self, word):
        self.word = word.lower()
        self.correct = set()
        self.wrong = []
        self.max_wrong = MAX_WRONG

    # -- queries -----------------------------------------------------------

    @property
    def wrong_count(self):
        return len(self.wrong)

    @property
    def is_won(self):
        return all(letter in self.correct for letter in self.word)

    @property
    def is_lost(self):
        return self.wrong_count >= self.max_wrong

    @property
    def is_over(self):
        return self.is_won or self.is_lost

    def already_used(self, letter):
        return letter in self.correct or letter in self.wrong

    def display(self):
        """The word with hidden letters shown as underscores."""
        return " ".join(letter if letter in self.correct else "_" for letter in self.word)

    # -- actions -----------------------------------------------------------

    def guess(self, letter):
        """Try one letter. Returns ('correct'|'wrong'|'repeat', message)."""
        letter = letter.lower()
        if letter in self.wrong or letter in self.correct:
            return "repeat", f"'{letter}' was already tried."
        if letter in self.word:
            self.correct.add(letter)
            return "win" if self.is_won else "correct", ""
        self.wrong.append(letter)
        return "lose" if self.is_lost else "wrong", ""


# ---------------------------------------------------------------------------
# GUI
# ---------------------------------------------------------------------------

class HangmanApp:
    """The tkinter window."""

    def __init__(self, root):
        self.root = root
        root.title("Wild West Hangman")
        root.configure(bg=BG_DARK)
        root.resizable(False, False)

        self._build_widgets()
        self._build_background()
        self._build_gallows()
        self.new_game()

    # -- layout ------------------------------------------------------------

    def _build_widgets(self):
        pad = {"padx": 12, "pady": 6}

        self.title_label = tk.Label(
            self.root, text="Wild West Hangman",
            font=("Georgia", 20, "bold italic"), fg=GOLD, bg=BG_DARK,
        )
        self.title_label.grid(row=0, column=0, pady=(10, 0))

        frame = tk.Frame(self.root, bg=BG_DARK)
        frame.grid(row=1, column=0, padx=16, pady=(6, 12))

        # Canvas with the desert scene, gallows, and the cowboy being drawn.
        self.canvas = tk.Canvas(
            frame, width=CANVAS_W, height=CANVAS_H, bg="#d9b26a",
            highlightthickness=2, highlightbackground=WOOD_DK,
        )
        self.canvas.grid(row=0, column=0, rowspan=2, sticky="nw")

        # Right-hand column: word on a wooden sign, guessed letters, status.
        right = tk.Frame(frame, bg=BG_DARK)
        right.grid(row=0, column=1, sticky="n")

        sign = tk.Frame(right, bg=SIGN, bd=2, relief="groove")
        sign.pack(pady=(20, 8))
        self.word_label = tk.Label(
            sign, text="", font=("Consolas", 22, "bold"),
            fg=CREAM, bg=SIGN,
        )
        self.word_label.pack(padx=18, pady=8)

        self.guessed_label = tk.Label(
            right, text="Misses: (none)", font=("Segoe UI", 12),
            fg=TAN, bg=BG_DARK,
        )
        self.guessed_label.pack(pady=(0, 6))

        self.status_label = tk.Label(
            right, text="", font=("Segoe UI", 13, "bold"),
            fg=GOLD, bg=BG_DARK,
        )
        self.status_label.pack(pady=(0, 10))

        # On-screen letter buttons.
        letters = tk.Frame(frame, bg=BG_DARK)
        letters.grid(row=1, column=1, sticky="n", pady=(8, 0))
        self.letter_buttons = {}
        for i in range(26):
            letter = chr(ord("A") + i)
            btn = tk.Button(
                letters, text=letter, width=3, font=("Segoe UI", 11, "bold"),
                relief="raised", bd=1, bg=BTN_BG, fg=BTN_FG,
                activebackground="#e0c488",
                command=lambda l=letter: self.make_guess(l),
            )
            btn.grid(row=i // 6, column=i % 6, padx=2, pady=2)
            self.letter_buttons[letter.lower()] = btn

        self.new_game_btn = tk.Button(
            frame, text="New Game", font=("Segoe UI", 11, "bold"),
            bg=NEWGAME_BG, fg="#ffffff", bd=0, padx=14, pady=4,
            activebackground=NEWGAME_ACTIVE, activeforeground="#ffffff",
            command=self.new_game,
        )
        self.new_game_btn.grid(row=2, column=0, columnspan=2, pady=(10, 0))

        # Keyboard support: any letter key makes a guess.
        self.root.bind("<KeyPress>", self._on_key)
        self.root.focus_set()

    def _build_background(self):
        c = self.canvas
        W, H = CANVAS_W, CANVAS_H
        # Twilight sky as stacked bands for a desert sunset.
        for y0, y1, color in (
            (0, 80, "#2d2a5e"),
            (80, 150, "#6b3a63"),
            (150, 215, "#c2542e"),
            (215, 250, "#e8a33d"),
        ):
            c.create_rectangle(0, y0, W, y1, fill=color, outline="")
        # Setting sun with stylised stripes.
        c.create_oval(254, 160, 312, 218, fill="#f7d154", outline="#d9a03c")
        for y in (174, 189, 204):
            c.create_line(254, y, 312, y, fill="#e8a33d", width=3)
        # Distant mesas.
        c.create_polygon(-10, 250, 35, 205, 120, 205, 168, 250,
                         fill="#3d2b45", outline="")
        c.create_polygon(120, 250, 195, 195, 265, 250,
                         fill="#45304d", outline="")
        c.create_polygon(235, 250, 305, 202, 350, 250,
                         fill="#3d2b45", outline="")
        # Desert floor.
        c.create_rectangle(0, 250, W, H, fill="#cfa863", outline="")
        c.create_rectangle(0, 262, W, H, fill="#c49a5b", outline="")
        # Cacti at the edges.
        _draw_cactus(c, 16)
        _draw_cactus(c, CANVAS_W - 16)

    def _build_gallows(self):
        c = self.canvas
        c.create_rectangle(43, 50, 49, 270, fill=WOOD, outline=WOOD_DK)    # left post
        c.create_rectangle(246, 50, 252, 270, fill=WOOD, outline=WOOD_DK)  # right post
        c.create_rectangle(42, 42, 252, 49, fill=WOOD, outline=WOOD_DK)    # crossbeam
        c.create_line(150, 49, 150, 58, fill=ROPE, width=3)                # rope
        c.create_oval(146, 55, 154, 63, fill=ROPE, outline="#c9a15b")      # knot

    # -- game flow ---------------------------------------------------------

    def new_game(self):
        self.game = HangmanGame(pick_word())
        self.canvas.delete("body")
        for btn in self.letter_buttons.values():
            btn.configure(state="normal", bg=BTN_BG, fg=BTN_FG)
        self.status_label.configure(text="Guess a letter, partner.", fg=GOLD)
        self._refresh()

    def _on_key(self, event):
        if event.char.isalpha() and len(event.char) == 1:
            self.make_guess(event.char)

    def make_guess(self, letter):
        game = self.game
        if game.is_over:
            return

        result, message = game.guess(letter)
        button = self.letter_buttons.get(letter.lower())

        if result == "repeat":
            self.status_label.configure(text=message, fg=LOSE_COLOR)
            return

        # A used letter can no longer be clicked.
        if button:
            button.configure(state="disabled", bg=BTN_DISABLED, fg=BTN_DISABLED_FG)

        if result in ("correct", "wrong"):
            self.status_label.configure(
                text="Correct!" if result == "correct" else "Wrong guess.",
                fg=GOLD,
            )
            self._refresh()
            return

        # Game over.
        self._refresh()
        if result == "win":
            self.status_label.configure(text="You win, partner!", fg=WIN_COLOR)
        else:
            self.status_label.configure(text="You got strung up!", fg=LOSE_COLOR)
        self._end_game(result == "win")

    def _draw_wrong_parts(self):
        for draw in DRAW_STEPS[: self.game.wrong_count]:
            draw(self.canvas)

    def _refresh(self):
        n = len(self.game.word)
        size = 26 if n <= 7 else (22 if n <= 9 else 18)
        self.word_label.configure(font=("Consolas", size, "bold"),
                                  text=self.game.display())
        misses = ", ".join(letter.upper() for letter in self.game.wrong)
        self.guessed_label.configure(text=f"Misses: {misses or '(none)'}")
        self._draw_wrong_parts()

    def _end_game(self, won):
        # Reveal the word and pause the buttons.
        self.word_label.configure(text=" ".join(self.game.word.upper()))
        if won:
            message = f"You win, partner! The word was: {self.game.word.upper()}"
        else:
            message = f"Yer got strung up! The word was: {self.game.word.upper()}"
        messagebox.showinfo("Wild West Hangman", message, parent=self.root)
        self.new_game()


def main():
    root = tk.Tk()
    HangmanApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
