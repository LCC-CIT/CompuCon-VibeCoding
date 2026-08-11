"""Rock, Paper, Scissors — a Tkinter game.

The user clicks a button to throw rock, paper, or scissors. The app
throws randomly, compares the two, and reports the winner. A scoreboard
in the window tracks wins, losses, and ties.
"""

import random
import tkinter as tk

CHOICES = ("rock", "paper", "scissors")

# What each choice beats. rock beats scissors, etc.
BEATS = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}


class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.resizable(False, False)

        self.wins = 0
        self.losses = 0
        self.ties = 0

        self._build_ui()

    def _build_ui(self):
        # Title
        title = tk.Label(
            self.root,
            text="Rock, Paper, Scissors",
            font=("Segoe UI", 18, "bold"),
            pady=10,
        )
        title.pack()

        # Instruction line
        instruction = tk.Label(
            self.root,
            text="Pick your move:",
            font=("Segoe UI", 11),
        )
        instruction.pack()

        # Move buttons
        button_frame = tk.Frame(self.root, padx=20)
        button_frame.pack(pady=10)
        for choice in CHOICES:
            tk.Button(
                button_frame,
                text=choice.capitalize(),
                width=10,
                command=lambda c=choice: self.play(c),
            ).pack(side="left", padx=5)

        # Result area
        self.throw_label = tk.Label(
            self.root,
            text="You: —    Computer: —",
            font=("Segoe UI", 12),
            pady=8,
        )
        self.throw_label.pack()

        self.result_label = tk.Label(
            self.root,
            text="Make a move to start!",
            font=("Segoe UI", 14, "bold"),
            pady=4,
        )
        self.result_label.pack()

        # Scoreboard
        score_frame = tk.Frame(self.root, padx=20, pady=12)
        score_frame.pack()
        self.score_label = tk.Label(
            score_frame,
            text=self._score_text(),
            font=("Segoe UI", 12),
        )
        self.score_label.pack()

        # Reset button
        tk.Button(
            self.root,
            text="Reset Score",
            command=self.reset,
        ).pack(pady=(0, 12))

    def _score_text(self):
        return f"Wins: {self.wins}   Losses: {self.losses}   Ties: {self.ties}"

    def play(self, player_choice):
        computer_choice = random.choice(CHOICES)
        self.throw_label.config(
            text=f"You: {player_choice.capitalize()}    Computer: {computer_choice.capitalize()}"
        )

        if player_choice == computer_choice:
            self.ties += 1
            self.result_label.config(text="It's a tie!", fg="#b58900")
        elif BEATS[player_choice] == computer_choice:
            self.wins += 1
            self.result_label.config(text="You win!", fg="#2e9e4f")
        else:
            self.losses += 1
            self.result_label.config(text="Computer wins!", fg="#c0392b")

        self.score_label.config(text=self._score_text())

    def reset(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.throw_label.config(text="You: —    Computer: —")
        self.result_label.config(text="Make a move to start!", fg="black")
        self.score_label.config(text=self._score_text())


def main():
    root = tk.Tk()
    RockPaperScissors(root)
    root.mainloop()


if __name__ == "__main__":
    main()
