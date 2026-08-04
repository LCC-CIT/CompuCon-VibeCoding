# Vibe Coding Cheat Sheet

*Print double-sided. One per student.*

---

## The Loop

> ### Ask small → Run it → Say exactly what went wrong → Repeat

---

## Starting Up

Open **PowerShell** (Windows Terminal), then:

```powershell
cd $HOME\Documents      # go to Documents
mkdir my-project        # make a folder for your project
cd my-project           # go into it
cc-ds                   # start Claude Code
```

`Ctrl+C` to quit. `cc-ds` to come back.

**Got your own Claude Pro account?** Type `cc` instead of `cc-ds`. Everything else is
identical.

**Always start in your project folder.** That folder is the AI's whole world.

> One command per line. PowerShell doesn't let you chain them with `&&`.

---

## A Good First Prompt

Answer four questions:

| | Example |
|---|---|
| **What kind of thing?** | "a Python app with a tkinter window" |
| **What does it do?** | "counts down from 25 minutes and beeps at zero" |
| **What does it look like?** | "big digits in the middle, Start and Reset buttons" |
| **Where does it go?** | "save it as `timer.py`" |

```
Build a Pomodoro timer in Python with tkinter.
25-minute countdown, big digits, Start / Pause / Reset buttons.
Beep when it hits zero.
Save it as timer.py
```

---

## How Much To Ask For

| Situation | Ask for |
|---|---|
| **Starting from nothing** | The whole app. Describe all of it. |
| **Changing something that works** | ONE thing. Then run it. Then the next. |

**The size test:** can you say what should be different in one sentence?

- ✅ "Make the background dark gray" → one sentence, good
- ❌ "Make it look better" → not a sentence you can check
- ❌ "Add multiplayer" → that's five things

---

## When Something Breaks

Say three things:

> **What I did** — "I clicked Make Story"
> **What I expected** — "a story should appear"
> **What actually happened** — "nothing happened, no error in the terminal"

Crashed? **Paste the whole error message.** All of it, not just the last line.

---

## Check Your Work — The Four Checks

**1. Does it do the thing?**
Not "an answer" — the *right* answer. Do the math yourself and compare.

**2. Does it survive the wrong thing?**
Empty box. Text where a number goes. Negative numbers. Click twice fast. Zero items.

**3. Did it change something you didn't ask for?**
> `What did you just change? List every change.`

**4. Can you explain it?**
> `Explain what the function on line 40 does, like I'm 12.`

> **It ran ≠ it's right.** Nothing on your computer will ever tell you the difference.

---

## Prompts Worth Memorizing

```
Don't write code yet. Tell me what files you'd create and in what order.

What could go wrong with this? What inputs would break it?

What did you just change? List every change.

Explain what this does in plain English.

I expected X but got Y. Why?

What would it take to add ___?

Is there a simpler way to do this?

Commit this with a message describing what we added.
```

---

## Bigger Projects

**Split by job.** One file, one purpose.

```
game/
  main.py       ← starts it, wires it together
  logic.py      ← the rules
  display.py    ← the window
  data.py       ← the content
```

**Point at files.** "In `scoring.py`, make the score reset to zero." Faster, more
accurate, and you know where to check.

**`/clear`** when you switch to a different task. Resets the conversation, not your code.

**`CLAUDE.md`** — a file in your project folder the AI reads every session:

```markdown
# Quiz Game
Python + tkinter multiple-choice quiz.

## Files
- main.py — starts the app
- scoring.py — 1 point right, -1 wrong, never below zero

## Rules
- Python + tkinter only, no extra libraries
- Keep files under 100 lines
```

---

## Save Points

**SAVE — copy the whole folder every time your app works:**

```powershell
cd $HOME\Documents
Copy-Item -Recurse myproject myproject-working
```

**UNDO — throw away the broken version, copy the good one back:**

```powershell
cd $HOME\Documents
Remove-Item -Recurse myproject
Copy-Item -Recurse myproject-working myproject
```

You can do exactly the same thing in File Explorer: right-click the folder → Copy →
Paste → rename it.

> **Copy every time it works.** Not when you finish. Every time it works.

Give copies names that mean something — `quiz-scoring-works`, not `quiz2`.

---

## When You're Stuck

Try in this order:

1. **Describe the bug out loud** to a person. You'll often fix it mid-sentence.
2. **`/clear`** and describe the problem fresh — the conversation may have a bad theory
   stuck in it.
3. **Restore your last working copy.** Take a smaller step this time.
4. **Delete the broken file** and ask for it again with a better description.
5. **Ask a human.** After 20 minutes, always.

---

## Four Rules

1. Run it before you ask for the next thing.
2. One change at a time.
3. Broken for 10 minutes? Ask a human.
4. You have to be able to explain what your app does.
