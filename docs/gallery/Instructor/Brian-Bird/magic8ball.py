"""A simple Magic 8-Ball app built with tkinter.

Type a question, click "Ask", and get a random answer.
Add your own answers to the ANSWERS list below.
"""

import random
import tkinter as tk

# ---------------------------------------------------------------------------
# Add your own answers here. Each one is a string in the list.
# ---------------------------------------------------------------------------
ANSWERS = [
    "Yes",
    "No",
    "Ask again later",
    "Maybe",
    "Definitely",
    "Don't count on it",
    "Outlook not so good",
    "Signs point to yes",
    "Better not tell you now",
    "Cannot predict now",
    "Most likely",
    "My sources say no",
]


class Magic8BallApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("Magic 8-Ball")
        root.resizable(False, False)

        # The picture of the 8-ball, drawn at the top of the window.
        self.canvas = tk.Canvas(
            root, width=220, height=215, bg="#e8e8e8", highlightthickness=0
        )
        self.canvas.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 5))
        self.draw_ball()

        tk.Label(root, text="Ask the 8-Ball a question:", font=("Segoe UI", 12)).grid(
            row=1, column=0, columnspan=2, padx=20, pady=(5, 5)
        )

        self.question_var = tk.StringVar()
        entry = tk.Entry(root, textvariable=self.question_var, width=40, font=("Segoe UI", 11))
        entry.grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky="ew")
        entry.bind("<Return>", lambda _event: self.ask())
        entry.focus_set()

        tk.Button(root, text="Ask", width=15, command=self.ask).grid(
            row=3, column=0, columnspan=2, padx=20, pady=10
        )

        # Where the answer appears.
        self.answer_var = tk.StringVar()
        tk.Label(
            root, textvariable=self.answer_var, font=("Segoe UI", 16, "bold")
        ).grid(row=4, column=0, columnspan=2, padx=20, pady=(5, 20))

        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

    def draw_ball(self):
        """Draw a classic Magic 8-Ball: black sphere, white window with an 8, on a stand."""
        c = self.canvas
        cx, cy = 110, 100  # ball centre
        r = 68             # ball radius

        # Stand (grey triangle the ball rests in).
        c.create_polygon(
            cx - 55, cy + 62, cx + 55, cy + 62, cx, cy + 105,
            fill="#a8a8a8", outline="#707070",
        )

        # Black sphere.
        c.create_oval(
            cx - r, cy - r, cx + r, cy + r,
            fill="black", outline="#333333", width=2,
        )

        # Glossy highlights in the top-left corner so it looks round.
        c.create_oval(46, 36, 72, 62, fill="#4f4f4f", outline="")
        c.create_oval(54, 44, 66, 56, fill="#7a7a7a", outline="")

        # White window with the number 8.
        w = 36  # window radius
        c.create_oval(cx - w, cy - w, cx + w, cy + w,
                      fill="white", outline="#555555", width=3)
        c.create_text(cx, cy, text="8", font=("Segoe UI", 24, "bold"), fill="black")

    def ask(self):
        """Pick a random answer and show it. Pressing Enter also calls this."""
        question = self.question_var.get().strip()
        if not question:
            self.answer_var.set("Please type a question first.")
            return
        self.answer_var.set(random.choice(ANSWERS))


def main():
    root = tk.Tk()
    Magic8BallApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
