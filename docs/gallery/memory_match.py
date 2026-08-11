"""Memory Match — a Tkinter concentration-style game.

A grid of face-down cards is laid out. The player flips two cards at a
time trying to find matching pairs: matches stay face up, mismatches
flip back over. A move counter tracks attempts until every pair is
found.
"""

import random
import tkinter as tk

# One symbol per pair; the deck is two of each, shuffled.
PAIRS = ["🍎", "🍌", "🍇", "🍉", "🍋", "🍓", "🍑", "🍒"]
COLS = 4

FACE_DOWN_BG = "#3b4a63"
FACE_UP_BG = "#e8eefb"
MATCHED_BG = "#cfe9d2"
MATCHED_FG = "#2e6b34"


class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Match")
        self.root.resizable(False, False)

        self.moves = 0
        self.revealed = []  # indices currently face up, pending a match
        self.matched = set()
        self.lock = False   # True during the flip-back delay

        self._build_ui()
        self.new_game()

    def _build_ui(self):
        title = tk.Label(
            self.root,
            text="Memory Match",
            font=("Segoe UI", 18, "bold"),
            pady=10,
        )
        title.pack()

        self.status_label = tk.Label(
            self.root,
            text="",
            font=("Segoe UI", 13),
        )
        self.status_label.pack(pady=(0, 6))

        self.board = tk.Frame(self.root)
        self.board.pack(padx=20, pady=6)

        self.buttons = []
        for i in range(len(PAIRS) * 2):
            btn = tk.Button(
                self.board,
                width=4,
                height=2,
                font=("Segoe UI Emoji", 20),
                bg=FACE_DOWN_BG,
                fg="white",
                activebackground=FACE_DOWN_BG,
                relief="raised",
                command=lambda idx=i: self.flip(idx),
            )
            btn.grid(row=i // COLS, column=i % COLS, padx=4, pady=4)
            self.buttons.append(btn)

        tk.Button(
            self.root,
            text="New Game",
            command=self.new_game,
        ).pack(pady=10)

    def new_game(self):
        self.moves = 0
        self.revealed = []
        self.matched = set()
        self.lock = False

        deck = PAIRS * 2
        random.shuffle(deck)
        self.deck = deck

        for btn in self.buttons:
            btn.config(
                text="?",
                bg=FACE_DOWN_BG,
                fg="white",
                state="normal",
                relief="raised",
                activebackground=FACE_DOWN_BG,
            )

        self.status_label.config(text="Moves: 0  —  Find all pairs!", fg="black")

    def flip(self, index):
        if self.lock:
            return
        if index in self.matched or index in self.revealed:
            return
        if len(self.revealed) >= 2:
            return

        self.revealed.append(index)
        self.buttons[index].config(text=self.deck[index], bg=FACE_UP_BG, fg="black")

        if len(self.revealed) == 2:
            self.moves += 1
            self.status_label.config(text=f"Moves: {self.moves}")
            self._check_pair()

    def _check_pair(self):
        i, j = self.revealed
        if self.deck[i] == self.deck[j]:
            self.matched.update(self.revealed)
            for k in self.revealed:
                self.buttons[k].config(
                    bg=MATCHED_BG,
                    fg=MATCHED_FG,
                    relief="sunken",
                    state="disabled",
                )
            self.revealed = []
            self._check_win()
        else:
            self.lock = True
            self.root.after(700, self._flip_back)

    def _flip_back(self):
        for k in self.revealed:
            self.buttons[k].config(text="?", bg=FACE_DOWN_BG, fg="white")
        self.revealed = []
        self.lock = False

    def _check_win(self):
        if len(self.matched) == len(self.buttons):
            self.status_label.config(
                text=f"🎉 You won in {self.moves} moves!",
                fg="#2e9e4f",
            )


def main():
    root = tk.Tk()
    MemoryGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
