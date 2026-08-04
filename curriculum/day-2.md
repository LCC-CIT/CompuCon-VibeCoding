# Day 2 — Ask Better, Check Harder

**3 hours.** Day 1 taught the loop. Day 2 makes them good at it: how much to specify,
how to say it, and how to actually verify what came back.

**If new students joined today:** run the 6-minute dice roller demo from Day 1 and give
them the four-question prompt template. They'll keep up.

---

## Session Arc

| Time | Block | Mode |
|---|---|---|
| 0:00–0:10 | Warm-up: same prompt, four ways | Whole group |
| 0:10–0:35 | How much to ask for at once | Talk + demo |
| 0:35–1:05 | Prompt lab: rewrite bad prompts | Pairs |
| 1:05–1:15 | **Break** | |
| 1:15–1:40 | How to check the AI's work | Talk + demo |
| 1:40–2:30 | Build: spec-first project | Independent |
| 2:30–2:50 | Swap and break | Pairs |
| 2:50–3:00 | Wrap | |

---

## 0:00 — Warm-Up: Same Prompt, Four Ways (10 min)

On the projector, four prompts for the same app. Ask which one they'd write, then ask
which one they'd *want to have written*.

```
A: make a study timer

B: make a pomodoro timer in python

C: Build a Pomodoro timer in Python with tkinter. 25-minute countdown,
   big digits, Start/Pause/Reset buttons. Beep when it hits zero.
   Save as pomodoro.py

D: Build a Pomodoro timer in Python with tkinter using a class-based
   architecture. Use threading.Timer for the countdown, not time.sleep.
   Store state in an enum. The label should use a monospace font at
   size 48 with grid geometry, and buttons should be in a frame below
   using pack. Handle the beep with winsound.Beep at 1000Hz. Include
   type hints and docstrings on every method. Save as pomodoro.py
```

Most will pick C, which is right. Then push:

- **What's wrong with A and B?** The AI will guess. It might guess right. It might build
  a command-line app when you wanted a window, or 5 minutes when you wanted 25. Guessing
  is fine when you don't care. It's a problem when you do.
- **What's wrong with D?** Nothing, technically — but every one of those decisions is a
  decision you now own. If `threading.Timer` is the wrong call, that's on you. And you
  spent five minutes writing a prompt to save two minutes of work.

> **Specify what you care about. Let the AI decide the rest.**

That's the whole lesson. The trick is knowing what you care about.

**MS/HS**
> **MS:** Use A vs. C only. D is noise for them.
> **HS:** All four. Then ask when D would actually be right. (Answer: when you have a
> real constraint — matching existing code, a library requirement, a teacher's rubric.)

---

## 0:10 — How Much To Ask For At Once (25 min)

### The two modes

**Mode 1: Starting from nothing → describe the whole thing.**

You want the AI to build a complete, coherent first version. It should know the shape of
the finished app so the pieces fit together. Ask for the whole thing.

**Mode 2: Changing something that exists → one thing at a time.**

Now the code exists and works. Every change risks breaking it. Ask for one, run it, and
only then ask for the next.

### Why one at a time (the real reason)

Draw this on the board:

```
Ask for 5 changes  →  run it  →  it's broken
                                  ↓
                     which of the 5 broke it?
                     could be any. could be two interacting.
                     you're now debugging blind.

Ask for 1 change   →  run it  →  it's broken
                                  ↓
                     it's that one. obviously.
                     undo it or fix it. 30 seconds.
```

> "Testing one change at a time isn't about being careful. It's about being **fast**.
> Every batch of changes you don't test is a debugging session you're saving up for
> later, with interest."

### Live demo — do this, don't just say it

Open a working app from yesterday. Ask for six things at once:

> Add a dark mode toggle, save the high score to a file, add sound effects, add a
> two-player mode, make the window resizable, and add a settings menu.

Let it produce something big. Run it. It will be broken or subtly wrong — and even if
it works, ask the room: **"Which part would you check first? How long would it take you
to check all six?"**

Then do one of the six properly. Run it. Works. Done in 90 seconds.

### The size test

> **Can you describe what should be different after this change in one sentence?**

Yes → good size. No → break it up.

| Too big | Right size |
|---|---|
| "Add multiplayer" | "Add a second score counter labeled Player 2" |
| "Make it look better" | "Make the background dark gray and the text white" |
| "Add saving" | "When I click Save, write the current list to `tasks.txt`" |

### The exception worth naming

Sometimes changes genuinely come as a set — if you're adding a second player you need a
score *and* a turn indicator *and* a way to switch. Fine. Ask for the set, but say so
explicitly, and expect to spend more time checking:

> Add two-player mode. That means: a second score counter, a label showing whose turn
> it is, and turns alternating after each roll. Those three things only.

Naming the pieces yourself gives you a checklist to verify against.

**MS/HS**
> **MS:** The one-sentence size test is the takeaway. Have them practice sizing out loud
> — you say a change, they call out "too big" or "just right."
> **HS:** Add: how do you *undo* a bad change? Introduce "keep a copy that works"
> (`cp app.py app_working.py`) as a poor man's version control. Sets up Day 3 git.

---

## 0:35 — Prompt Lab (30 min)

Pairs. Six bad prompts on a handout. For each: **say what's missing, then rewrite it.**

```
1. "make a game"

2. "build a website for my club"

3. "the colors are ugly, fix them"

4. "make a program that tracks stuff for my basketball team"

5. "add a leaderboard, dark mode, sound, and a tutorial screen"

6. "make it work on my phone"
```

Answer sketches for the instructor:

1. **What kind of game?** Missing everything. Needs: genre, input, win condition,
   platform.
2. **Website doing what?** Missing: pages, content, static or interactive, hosted where.
3. **Ugly how, and what do you want instead?** "Fix" isn't an instruction. Needs a
   target: "use a dark background with light text."
4. **"Stuff" is doing a lot of work.** Player names? Scores per game? Season totals?
   Needs a concrete list of what gets tracked and what you do with it.
5. **Four changes.** Split it. Ask for the leaderboard, run it, then dark mode.
6. **Ambiguous *and* huge.** "Work on my phone" could mean a website, an app, or
   responsive layout. Also this may be a rewrite, not a change — worth asking the AI
   "what would it take to..." before asking it to do it.

Then: **each pair writes a real first prompt for the app they'll build after break** and
trades with another pair. The other pair's job is to find the ambiguity — anywhere the
AI could reasonably guess wrong.

> "If your partner can find two ways to read your prompt, so can the AI."

---

## 1:05 — Break (10 min)

---

## 1:15 — How To Check The AI's Work (25 min)

The heart of the whole track. Day 1 planted the idea; today it becomes a method.

### It ran ≠ it's right

Four levels of "checked," weakest to strongest:

| Level | What you did | What it proves |
|---|---|---|
| 0 | It generated without an error | Nothing |
| 1 | It ran without crashing | The syntax is valid |
| 2 | You used it and it looked right | It works for the happy path |
| 3 | You tried to break it and couldn't | It probably holds up |
| 4 | You read the code and it does what you asked | You actually know |

> "Most people stop at level 1 and think they're at level 4. That gap is where every
> disaster lives."

### The four checks (put these on the wall)

**1. Does it do the thing?**
Use it the way it's meant to be used. Does it produce the right answer? Not "an answer"
— the *right* one. If it's a calculator, do the math yourself and compare.

**2. Does it survive the wrong thing?**
Empty input. Text where a number goes. A negative number. Clicking twice fast. Zero
items. A thousand items. This is where AI-written code fails most often, because the AI
optimizes for the case you described.

**3. Did it change anything you didn't ask for?**
Ask the AI directly: *"What did you change? List it."* Then check the list against what
you asked for. This is a real failure mode — you ask for a color change and it also
"helpfully" rewrites your scoring logic.

**4. Can you explain it?**
Point at a chunk of the code and ask: what does this do? If you can't say, ask the AI —
*"Explain what the function on line 40 does, like I'm 12."* It's very good at this, and
this is the single fastest way to actually learn to code while vibe coding.

### Making the AI check itself

Useful prompts to hand them:

```
What could go wrong with this? What inputs would break it?

What did you just change? List every change.

Explain what this function does in plain English.

I expected X but got Y. Why?

Is there a simpler way to do this?
```

The catch, and say it plainly: **the AI checking its own work is a hint, not a
guarantee.** It's the same guesser that wrote the bug. Use it to find candidate problems,
not to prove there aren't any.

### The 60-second demo

Ask for something with a hidden bug:

> Write a Python function that takes a list of test scores and returns the average.

You'll get something like:

```python
def average(scores):
    return sum(scores) / len(scores)
```

Ask the room to run the four checks. Level 2 passes fine. Level 3: **what if the list is
empty?** `ZeroDivisionError`. The AI wrote correct code for the case you described and
had nothing to say about the case you didn't.

> "It didn't make a mistake. It answered exactly what you asked. *You* left out the
> question."

**MS/HS**
> **MS:** Checks 1 and 2 only, hands-on. Frame check 2 as "be a jerk to your app."
> Skip the self-checking prompts except "explain this like I'm 12."
> **HS:** All four. Emphasize check 3 — unrequested changes are the failure mode that
> bites hardest on real projects. Have them diff by eye: keep a copy before the change,
> compare after.

---

## 1:40 — Build: Spec First (50 min)

Today's build has a rule: **write the spec before the prompt.**

### Spec sheet (10 min, on paper)

Every student fills this out before touching a keyboard:

```
APP NAME:

WHAT IT DOES (one sentence):

MUST HAVE (3 things, no more):
  1.
  2.
  3.

WHAT IT LOOKS LIKE:

HOW I'LL KNOW IT WORKS (3 specific tests):
  1. If I ______, it should ______
  2. If I ______, it should ______
  3. If I ______ (something wrong), it should ______
```

The last section is the new thing. **They write their tests before the code exists.** Test
3 must be a wrong-input test.

Instructor signs off on the spec before they start. Reject anything with more than 3
must-haves or a vague test.

### Build (35 min)

Work from the spec. First prompt is the whole app (Mode 1). Every change after is one
thing (Mode 2).

Board checklist:

- [ ] All 3 must-haves work
- [ ] All 3 of my tests pass
- [ ] I asked the AI "what did you change?" at least once and checked the answer
- [ ] I asked the AI to explain one part of the code and I understood it
- [ ] I tried three wrong inputs

**MS/HS**
> **MS:** 2 must-haves, 2 tests. Pairs — one drives, one runs the tests, swap halfway.
> The tester role makes verification a job, not an afterthought.
> **HS:** 4 must-haves allowed. Add a checkbox: "I found something the AI did that I
> didn't ask for."

### Land it (5 min)

Run all three of your own tests one last time and mark pass/fail on the spec sheet
honestly. **A failed test you can name is a better outcome than a passed test you didn't
really check.** Say this out loud — it sets the culture for Days 3 and 4.

---

## 2:30 — Swap And Break (20 min)

Pairs swap machines. Your job: **break your partner's app.** Ten minutes.

You may not look at the code. You may only use the app.

Rules of engagement:

- Empty everything
- Wrong type of thing in every box
- Extremes — 0, negative numbers, 999999, a paragraph of text
- Click everything twice, and out of order
- Resize the window to nothing

Write down every problem you find using the good bug-report format from Day 1: *what you
did, what you expected, what happened.*

Swap back. Ten minutes to fix the top bug your partner found.

> "Your partner found in five minutes what you missed in forty. That's not because
> they're better — it's because you were trying to make it work and they were trying to
> make it fail. Both are necessary. Professionals hire people whose whole job is the
> second one."

**MS/HS**
> **MS:** Frame as a competition — most bugs found wins. 8 min breaking, 8 min fixing,
> 4 min whole-group debrief on the funniest bug found.
> **HS:** Require the bug report in writing, formatted properly. Then have them paste
> that report straight to the AI — a well-written bug report is a well-written prompt,
> and that's not a coincidence.

---

## 2:50 — Wrap (10 min)

Two things on the board:

**How much to ask for:**
> New app → describe the whole thing. Existing app → one change at a time.
> If you can't say what should be different in one sentence, it's too big.

**How to check:**
> 1. Does it do the thing?
> 2. Does it survive the wrong thing?
> 3. Did it change something I didn't ask for?
> 4. Can I explain it?

Teaser for Day 3: **"Everything you've built today is one file. Tomorrow we build things
too big for one file — and you'll find out why that changes everything about how you
talk to the AI."**

---

## Instructor Prep Checklist

- [ ] Print the six bad prompts handout (one per pair)
- [ ] Print spec sheets (one per student, plus spares)
- [ ] Have a Day 1 app on hand for the six-changes-at-once demo
- [ ] Have the empty-list average bug ready to demo live
- [ ] Post the four checks on the wall — they stay up through Day 4
