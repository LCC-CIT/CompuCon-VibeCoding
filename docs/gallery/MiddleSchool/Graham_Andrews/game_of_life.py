#!/usr/bin/env python3
"""
Conway's Game of Life — tkinter, zero dependencies.

- Resize the window to reveal more / less grid.
- Click cells to paint / erase the initial pattern.
- START / STOP toggles the simulation.
- STEP advances one generation.
- CLEAR wipes the board.
- RANDOM seeds random noise.
- SPEED slider controls the tick rate.
"""

import tkinter as tk
import random
import time

# --- Fixed settings ---
CELL_SIZE = 14
LINE_WIDTH = 1  # 0 = no grid lines

# Colors
COLOR_DEAD = "#1a1a2e"
COLOR_ALIVE = "#00ff88"
COLOR_GRID = "#2a2a3e"
BG = "#0f0f23"


class GameOfLife:
    def __init__(self):
        self.running = False
        self.speed_ms = 100
        self.gen_count = 0
        self.cols = 0
        self.rows = 0
        self.grid = []
        self._cooldown = []  # timestamp of last toggle per cell

        # --- Window ---
        self.root = tk.Tk()
        self.root.title("Conway's Game of Life")
        self.root.configure(bg=BG)
        self.root.geometry("600x500")
        self.root.minsize(300, 240)

        # --- Canvas (expands to fill the window) ---
        self.canvas = tk.Canvas(
            self.root,
            bg=COLOR_DEAD,
            highlightthickness=0,
        )
        self.canvas.pack(padx=10, pady=(10, 5), fill=tk.BOTH, expand=True)

        # Init grid from current canvas size once it appears
        self.canvas.bind("<Configure>", self._on_resize)

        # Bind mouse for drawing
        self.canvas.bind("<Button-1>", self._on_click)
        self.canvas.bind("<B1-Motion>", self._on_drag)

        # --- Controls ---
        controls = tk.Frame(self.root, bg=BG)
        controls.pack(pady=(0, 10))

        self.btn_start = tk.Button(
            controls, text="START", font=("Segoe UI", 11, "bold"),
            bg="#00cc66", fg="white", activebackground="#00ff88",
            relief="flat", padx=16, pady=4, cursor="hand2",
            command=self.toggle_run,
        )
        self.btn_start.pack(side="left", padx=4)

        tk.Button(
            controls, text="STEP", font=("Segoe UI", 11),
            bg="#333355", fg="white", activebackground="#444466",
            relief="flat", padx=14, pady=4, cursor="hand2",
            command=self.step,
        ).pack(side="left", padx=4)

        tk.Button(
            controls, text="RANDOM", font=("Segoe UI", 11),
            bg="#553388", fg="white", activebackground="#664499",
            relief="flat", padx=12, pady=4, cursor="hand2",
            command=self.randomize,
        ).pack(side="left", padx=4)

        tk.Button(
            controls, text="FILL", font=("Segoe UI", 11),
            bg="#3388cc", fg="white", activebackground="#4499dd",
            relief="flat", padx=14, pady=4, cursor="hand2",
            command=self.fill,
        ).pack(side="left", padx=4)

        tk.Button(
            controls, text="CLEAR", font=("Segoe UI", 11),
            bg="#883333", fg="white", activebackground="#994444",
            relief="flat", padx=14, pady=4, cursor="hand2",
            command=self.clear,
        ).pack(side="left", padx=4)

        # Speed slider
        tk.Label(controls, text="  Speed:", font=("Segoe UI", 10),
                 bg=BG, fg="#aaaacc").pack(side="left", padx=(14, 2))

        self.speed_var = tk.IntVar(value=self.speed_ms)
        tk.Scale(
            controls, from_=20, to=500, orient="horizontal",
            variable=self.speed_var, length=120, bg=BG, fg="white",
            troughcolor="#2a2a3e", activebackground="#00ff88",
            highlightthickness=0, bd=0, cursor="hand2",
            command=self._on_speed_change,
        ).pack(side="left")

        # Generation counter
        self.gen_label = tk.Label(
            self.root, text="Generation: 0",
            font=("Segoe UI", 10), bg=BG, fg="#aaaacc",
        )
        self.gen_label.pack(pady=(0, 10))

        # --- Tick loop ---
        self._resize_pending = None
        self._tick()

        self.root.mainloop()

    # ── Resize ────────────────────────────────────────────────────

    def _on_resize(self, event):
        """Canvas changed size — rebuild the grid to match."""
        # Debounce: only process the last event in a rapid-fire sequence
        if self._resize_pending is not None:
            self.canvas.after_cancel(self._resize_pending)
        self._resize_pending = self.canvas.after(80, self._apply_resize)

    def _apply_resize(self):
        self._resize_pending = None
        new_cols = max(3, self.canvas.winfo_width() // CELL_SIZE)
        new_rows = max(3, self.canvas.winfo_height() // CELL_SIZE)

        if new_cols == self.cols and new_rows == self.rows:
            return

        # Preserve existing cells, grow/shrink the grid
        old_grid = self.grid
        old_cols, old_rows = self.cols, self.rows

        self.cols, self.rows = new_cols, new_rows
        self.grid = [[False] * self.cols for _ in range(self.rows)]
        self._cooldown = [[0.0] * self.cols for _ in range(self.rows)]

        for r in range(min(old_rows, self.rows)):
            for c in range(min(old_cols, self.cols)):
                if old_grid[r][c]:
                    self.grid[r][c] = True

        self._redraw_all()

    # ── Grid helpers ──────────────────────────────────────────────

    def _draw_grid_lines(self):
        self.canvas.delete("grid")
        if LINE_WIDTH <= 0:
            return
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        for x in range(0, w + 1, CELL_SIZE):
            self.canvas.create_line(
                x, 0, x, h, fill=COLOR_GRID, width=LINE_WIDTH,
                tags="grid",
            )
        for y in range(0, h + 1, CELL_SIZE):
            self.canvas.create_line(
                0, y, w, y, fill=COLOR_GRID, width=LINE_WIDTH,
                tags="grid",
            )
        self.canvas.tag_lower("grid")

    def _draw_cell(self, r, c):
        x1 = c * CELL_SIZE + LINE_WIDTH
        y1 = r * CELL_SIZE + LINE_WIDTH
        x2 = x1 + CELL_SIZE - LINE_WIDTH
        y2 = y1 + CELL_SIZE - LINE_WIDTH
        color = COLOR_ALIVE if self.grid[r][c] else COLOR_DEAD
        self.canvas.create_rectangle(
            x1, y1, x2, y2, fill=color, outline="", tags="cell",
        )

    def _redraw_all(self):
        self.canvas.delete("cell")
        self._draw_grid_lines()
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c]:
                    self._draw_cell(r, c)

    # ── Simulation ────────────────────────────────────────────────

    def _count_neighbors(self, r, c):
        count = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr = (r + dr) % self.rows
                nc = (c + dc) % self.cols
                if self.grid[nr][nc]:
                    count += 1
        return count

    def step(self):
        """Advance one generation."""
        new = [[False] * self.cols for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                n = self._count_neighbors(r, c)
                if self.grid[r][c]:
                    new[r][c] = n == 2 or n == 3
                else:
                    new[r][c] = n == 3
        self.grid = new
        self.gen_count += 1
        self._redraw_all()
        self.gen_label.config(text=f"Generation: {self.gen_count}")

    def randomize(self):
        """Fill ~30% of cells randomly."""
        self.grid = [
            [random.random() < 0.3 for _ in range(self.cols)]
            for _ in range(self.rows)
        ]
        self.gen_count = 0
        self._redraw_all()
        self.gen_label.config(text="Generation: 0")

    def fill(self):
        """Make every cell alive."""
        self.grid = [[True] * self.cols for _ in range(self.rows)]
        self.gen_count = 0
        self._redraw_all()
        self.gen_label.config(text="Generation: 0")

    def clear(self):
        """Kill all cells."""
        self.grid = [[False] * self.cols for _ in range(self.rows)]
        self.gen_count = 0
        self._redraw_all()
        self.gen_label.config(text="Generation: 0")

    def toggle_run(self):
        self.running = not self.running
        if self.running:
            self.btn_start.config(text="STOP", bg="#cc4444",
                                  activebackground="#ff5555")
        else:
            self.btn_start.config(text="START", bg="#00cc66",
                                  activebackground="#00ff88")

    def _tick(self):
        if self.running:
            self.step()
        self.root.after(self.speed_ms, self._tick)

    def _on_speed_change(self, _val):
        self.speed_ms = self.speed_var.get()

    # ── Mouse drawing ─────────────────────────────────────────────

    def _toggle_cell(self, event_x, event_y):
        c = event_x // CELL_SIZE
        r = event_y // CELL_SIZE
        if 0 <= r < self.rows and 0 <= c < self.cols:
            now = time.monotonic()
            if now - self._cooldown[r][c] < 0.5:
                return  # still on cooldown, skip
            self._cooldown[r][c] = now
            self.grid[r][c] = not self.grid[r][c]
            self._draw_cell(r, c)

    def _on_click(self, event):
        self._toggle_cell(event.x, event.y)

    def _on_drag(self, event):
        self._toggle_cell(event.x, event.y)


if __name__ == "__main__":
    GameOfLife()
