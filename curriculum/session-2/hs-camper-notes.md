# Session 2 — Ask Better, Check Harder

### Vibe Coding · High School · Keep this with you

---

## What you're doing today

Session 1 gave you the loop. Today you get precise about it — and you pitch the project
you'll be graded on by your peers at the showcase.

Three things:

1. **How much to specify** — and when specifying more makes things worse
2. **How to verify** — a real method, not just "it ran"
3. **Your capstone** — pitched and started today

**Important scheduling note:** your capstone has to be **finished by the end of Session
3**. Session 4 is 60 minutes and it's entirely demos — there is no build time. Plan
accordingly, which mostly means picking something smaller than you want to.

---

## Today's plan

| | Block |
|---|---|
| **1** | Warm-up: four ways to prompt the same app |
| **2** | How much to ask for at once |
| **3** | Prompt lab — diagnosing and rewriting bad prompts |
| **4** | Break |
| **5** | How to check the AI's work — the four checks |
| **6** | Build a practice project, spec written first |
| **7** | Swap machines, break your partner's app |
| **8** | **Capstone pitch + scope check** |
| **9** | **Capstone: plan and first build** |

---

## Starting up

```powershell
cd $HOME\Documents\Projects
mkdir myproject
cd myproject
cc-ds
```

`cc` if you have your own Claude Pro account. One command per line — 5.1 doesn't support
`&&`.

**Run it:** `python app.py`

---

## Four ways to ask for the same app

```
A: make a study timer

B: make a pomodoro timer in python

C: Build a Pomodoro timer in Python with tkinter. 25-minute countdown,
   big digits, Start/Pause/Reset buttons. Beep when it hits zero.
   Save as pomodoro.py

D: Build a Pomodoro timer in Python with tkinter using a class-based
   architecture. Use threading.Timer for the countdown, not time.sleep.
   Store state in an enum. Label in monospace at size 48 using grid
   geometry, buttons in a frame below using pack. Beep with
   winsound.Beep at 1000Hz. Type hints and docstrings on every method.
```

**C is right.** But understand *why* D is wrong, because it's the mistake people make once
they get comfortable:

Every implementation detail in D is a decision **you now own**. If `threading.Timer` is
the wrong call for this, that's on you, not the AI. You also spent five minutes writing a
prompt to save two minutes of work.

> **Specify what you care about. Let the AI decide the rest.**

D becomes correct when you have a real constraint — matching existing code, a required
library, a rubric. Not before.

---

## How much to ask for at once

**Starting from nothing → describe the whole app.** You want a coherent first version
where the pieces fit together.

**Changing working code → one thing at a time.**

```
5 changes → run → broken → which one? could be any. could be two
                            interacting. you're debugging blind.

1 change  → run → broken → it's that one. 30 seconds.
```

Not caution — **speed**. Every batch of untested changes is a debugging session you're
saving up for later, with interest.

**Size test:** can you describe what should be different in one sentence?

| Too big | Right size |
|---|---|
| "Add multiplayer" | "Add a second score counter labeled Player 2" |
| "Make it look better" | "Make the background dark gray, text white" |
| "Add saving" | "When I click Save, write the list to `tasks.txt`" |

### The legitimate exception

Some changes genuinely come as a set. Adding a second player needs a score *and* a turn
indicator *and* turn-switching. Fine — but name the pieces explicitly:

> Add two-player mode. That means: a second score counter, a label showing whose turn it
> is, and turns alternating after each roll. Those three things only.

Naming them yourself gives you a checklist to verify against afterward.

---

## The four checks

### It ran ≠ it's right

| Level | What you did | What it proves |
|---|---|---|
| 0 | It generated without an error | Nothing |
| 1 | It ran without crashing | The syntax is valid |
| 2 | You used it and it looked right | Works for the happy path |
| 3 | You tried to break it and couldn't | Probably holds up |
| 4 | You read the code and it does what you asked | You actually know |

> Most people stop at level 1 and believe they're at level 4. That gap is where every
> disaster lives.

### The checks themselves

**1. Does it do the thing?**
Not "an answer" — the *right* answer. Do the math yourself and compare.

**2. Does it survive the wrong thing?**
Empty input. Wrong types. Negatives. Zero items. A thousand items. Double-clicks. This is
where AI-written code fails most, because the AI optimizes for the case you described.

**3. Did it change anything you didn't ask for?**

```
What did you just change? List every change.
```

Then check that list against what you asked for. Real failure mode: you request a color
change, it also rewrites your scoring logic.

**4. Can you explain it?**

```
Explain what the function on line 40 does, like I'm 12.
```

If you can't say what a chunk of your own code does, you're at level 1 pretending to be
level 4. This is also the fastest way to actually learn to code while building.

### Making the AI check itself

```
What could go wrong with this? What inputs would break it?
I expected X but got Y. Why?
Is there a simpler way to do this?
```

**The catch:** the AI checking its own work is a hint, not a guarantee. It's the same
guesser that wrote the bug. Use it to surface candidates, never to prove absence.

### Worked example

```python
def average(scores):
    return sum(scores) / len(scores)
```

Check 1: passes. Check 2: **empty list → `ZeroDivisionError`.**

> It didn't make a mistake. It answered exactly what you asked. *You* left out the
> question.

---

## Practice build: spec first

Before typing anything:

```
APP NAME:

WHAT IT DOES (one sentence):

MUST HAVE (3, no more):
  1.
  2.
  3.

WHAT IT LOOKS LIKE:

HOW I'LL KNOW IT WORKS (3 specific tests):
  1. If I ______, it should ______
  2. If I ______, it should ______
  3. If I ______ (something wrong), it should ______
```

**You're writing the tests before the code exists.** Test 3 must be a wrong-input test.

Keep this small — it's practice, not the capstone.

- [ ] All 3 must-haves work
- [ ] All 3 tests pass
- [ ] Asked "what did you change?" and checked the answer
- [ ] Asked the AI to explain one part, and understood it
- [ ] Tried three wrong inputs

Mark your tests honestly at the end. **A failed test you can name beats a passed test you
didn't really check.**

---

## Swap and break

Switch machines. Break your partner's app. No reading their code — use the app only.

Empty everything · wrong types everywhere · 0, negatives, 999999, paragraphs · everything
clicked twice and out of order · window shrunk to nothing.

Write each finding as a proper bug report:

> **What I did · What I expected · What actually happened**

Then swap back and fix the top one.

Now notice something: **paste that bug report straight into the AI as your prompt.** It
works. A well-written bug report and a well-written prompt are the same document, and
that's not a coincidence.

> Your partner finds in five minutes what you missed in forty — because you were trying to
> make it work and they were trying to make it fail. Both are necessary. Companies hire
> people whose entire job is the second one.

---

## Your capstone

### The pitch

```
I'm building ______.

You use it to ______.

The three things it has to do:
  1.
  2.
  3.

I'll know it works when:
  - If I ______, it ______
  - If I ______ (wrong input), it ______
```

Your partner asks you two questions:

1. **"What happens if I do the wrong thing?"**
2. **"Could you cut one of the three and still have something cool?"**

Almost everyone should cut one. Then an instructor signs off.

### Scope, honestly

You have the rest of today plus Session 3. That's it.

| If you pitched | Build this instead |
|---|---|
| Multiplayer online game | Two players, same keyboard |
| Anything with user accounts | One user, saves to a text file |
| Website with a database | One page, data in a JSON file |
| "A whole RPG" | One battle, three enemies |
| Machine learning anything | Rules-based version of the same idea |
| A Discord/Instagram bot | Same logic, local app, no API |

> Cutting scope isn't giving up. It's the actual skill. A small thing that works beats a
> big thing that doesn't — today, and in every job you will ever have.

### Setting it up

```powershell
cd $HOME\Documents\Projects
mkdir capstone
cd capstone
cc-ds
```

Four steps, in order:

**1. Ask for a plan, not code.**

```
I want to build [your app]. Don't write any code yet. Tell me what
files you'd create, what goes in each one, and what order you'd
build them in.
```

**2. Argue with the plan.** Change at least two things. Combine files, drop a feature,
reorder the build. Changing a plan is free. Changing code is not.

**3. Save it** as `PLAN.md` in your project folder.

**4. Build component 1 only.** Run it. Check it.

### Before you leave — make a save point

```powershell
cd $HOME\Documents\Projects
Copy-Item -Recurse capstone capstone-working
```

That's a complete copy of your folder, frozen at a moment it worked. You'll learn the
full system next session. For now: **it works, so copy it.**

---

## The short version

**How much to ask for:**
> New app → the whole thing. Existing app → one change at a time.
> If you can't say what should be different in one sentence, it's too big.

**How to check:**
> 1. Does it do the thing?
> 2. Does it survive the wrong thing?
> 3. Did it change something I didn't ask for?
> 4. Can I explain it?

---

## Next time

Your project gets too big for one file, and you finish your capstone. **Session 4 is
demos only.**
