# Session 2 — Ask Better, Check Harder

Session 1 taught the loop. Session 2 makes them good at it: how much to specify, how to
say it, and how to actually verify what came back.

**HS also pitches and starts the capstone in this session.** HS's capstone build lives in
Sessions 2–3, because HS Session 4 is only 60 minutes and is demo-and-wrap-up only. MS
does not pitch a capstone until Session 4.

**If new students joined today:** run the 6-minute dice roller demo from Session 1 and
give them the four-question prompt template. They'll keep up.

---

## Timing

The first five blocks are shared. HS then adds a break, a longer build, and the capstone
pitch and kickoff.

### Middle school — 85 min

| Time | Block | Mode |
|---|---|---|
| 0:00–0:06 | Warm-up: same prompt, four ways | Whole group |
| 0:06–0:18 | How much to ask for at once | Talk + demo |
| 0:18–0:33 | Prompt lab: rewrite bad prompts | Pairs |
| 0:33–0:48 | How to check the AI's work | Talk + demo |
| 0:48–1:12 | Build: spec-first project | Independent |
| 1:12–1:25 | Swap and break | Pairs |

> **No break scheduled.** If your group needs one, take 5 at 0:48 and cut the build to
> 19 minutes.

### High school — 180 min

| Time | Block | Mode |
|---|---|---|
| 0:00–0:10 | Warm-up: same prompt, four ways | Whole group |
| 0:10–0:30 | How much to ask for at once | Talk + demo |
| 0:30–0:55 | Prompt lab: rewrite bad prompts | Pairs |
| 0:55–1:05 | **Break** | |
| 1:05–1:30 | How to check the AI's work | Talk + demo |
| 1:30–2:05 | Build: spec-first practice project | Independent |
| 2:05–2:20 | Swap and break | Pairs |
| 2:20–2:40 | Capstone pitch + scope check | Pairs → instructor |
| 2:40–3:00 | Capstone: plan and first build | Independent |

---

## Warm-Up: Same Prompt, Four Ways (MS 6 min / HS 10 min)

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
> **MS:** Use A vs. C only. D is noise for them and costs 4 minutes you don't have.
> **HS:** All four. Then ask when D would actually be right. (Answer: when you have a
> real constraint — matching existing code, a library requirement, a teacher's rubric.)

---

## How Much To Ask For At Once (MS 12 min / HS 20 min)

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
> **MS:** The one-sentence size test is the whole takeaway. Practice it out loud — you
> say a change, they call out "too big" or "just right." Skip the exception.
> **HS:** Full version, plus the live demo: open a working app, ask for six things at
> once, run it. Even if it works, ask "which part would you check first? How long would
> checking all six take?" Then do one of the six properly in 90 seconds.

---

## Prompt Lab (MS 15 min / HS 25 min)

Pairs. Bad prompts on a handout. For each: **say what's missing, then rewrite it.**

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

Then: **each pair writes a real first prompt for the app they'll build next** and trades
with another pair. The other pair's job is to find the ambiguity — anywhere the AI could
reasonably guess wrong.

> "If your partner can find two ways to read your prompt, so can the AI."

**MS/HS**
> **MS:** Prompts 1, 3, and 5 only. Do #1 together on the projector as a worked example
> before they try the other two in pairs.
> **HS:** All six, plus the trade-and-critique step.

---

## Break — HS only (10 min)

MS runs straight through. See the note under the MS timing table if your group needs a
pause.

---

## How To Check The AI's Work (MS 15 min / HS 25 min)

The heart of the whole track. Session 1 planted the idea; today it becomes a method.

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

### The four checks (put these on the wall — they stay up through Session 4)

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

Explain what this does in plain English.

I expected X but got Y. Why?
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
> **MS:** Checks 1 and 2 only, hands-on. Frame check 2 as "be a jerk to your app." Of
> the self-checking prompts, teach only "explain this like I'm 12." Skip the levels
> table — demo the empty-list bug instead, it lands better than the taxonomy.
> **HS:** All four checks and the levels table. Emphasize check 3 — unrequested changes
> are the failure mode that bites hardest on real projects.

---

## Build: Spec First (MS 24 min / HS 35 min)

This build has a rule: **write the spec before the prompt.**

For HS this is a practice project, not the capstone — the capstone gets pitched later in
this session. Keep it small on purpose.

### Spec sheet (MS 6 min / HS 10 min, on paper)

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

### Build (MS 15 min / HS 20 min)

Work from the spec. First prompt is the whole app (Mode 1). Every change after is one
thing (Mode 2).

Board checklist:

- [ ] All must-haves work
- [ ] All of my tests pass
- [ ] I asked the AI "what did you change?" at least once and checked the answer
- [ ] I tried three wrong inputs

### Land it (MS 3 min / HS 5 min)

Run all three of your own tests one last time and mark pass/fail on the spec sheet
honestly. **A failed test you can name is a better outcome than a passed test you didn't
really check.** Say this out loud — it sets the culture for the rest of the track.

**MS/HS**
> **MS:** 2 must-haves and 2 tests, not 3. Pairs — one drives, one runs the tests, swap
> halfway. The tester role makes verification a job, not an afterthought.
> **HS:** 3 must-haves. Add a checkbox: "I asked the AI to explain one part of the code
> and I understood it."

---

## Swap And Break (MS 13 min / HS 15 min)

Pairs swap machines. Your job: **break your partner's app.**

You may not look at the code. You may only use the app.

Rules of engagement:

- Empty everything
- Wrong type of thing in every box
- Extremes — 0, negative numbers, 999999, a paragraph of text
- Click everything twice, and out of order
- Resize the window to nothing

Write down every problem you find using the good bug-report format from Session 1: *what
you did, what you expected, what happened.*

Swap back. Fix the top bug your partner found.

> "Your partner found in five minutes what you missed in twenty. That's not because
> they're better — it's because you were trying to make it work and they were trying to
> make it fail. Both are necessary. Professionals hire people whose whole job is the
> second one."

**MS/HS**
> **MS:** Frame as a competition — most bugs found wins. 6 min breaking, 5 min fixing,
> 2 min whole-group callout of the funniest bug found.
> **HS:** 7 min breaking, 8 min fixing. Require the bug report in writing, formatted
> properly. Then have them paste that report straight to the AI — a well-written bug
> report is a well-written prompt, and that's not a coincidence.

---

## Capstone Pitch + Scope Check — HS only (20 min)

**MS does not do this today.** MS pitches in Session 4. Skip to the wrap.

HS's capstone build has to fit in the rest of this session plus Session 3, because
Session 4 is 60 minutes of demo and wrap-up with no build time. Students need to know
that now.

> "Your Session 4 is one hour, and it's all demos. That means your project has to be
> finished by the end of next session. Plan accordingly — and that mostly means picking
> something smaller than you want to."

### Pitch to a partner (8 min)

Each student gets 3 minutes to pitch, using this:

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

Partner's job — ask these two questions:

1. **"What happens if I do the wrong thing?"**
2. **"Could you cut one of the three and still have something cool?"**

Question 2 is the important one. Almost everyone should cut one.

### Instructor scope check (12 min)

Every student gets a ~30-second sign-off. You are looking for one thing:

> **Can this be built in the time left in this session plus one more session?**

Common over-scopes and the cut:

| They pitched | Cut it to |
|---|---|
| Multiplayer online game | Two players, same keyboard |
| App with user accounts and logins | One user, saves to a text file |
| Website with a database | One page, data in a JSON file |
| "A whole RPG" | One battle, three enemies |
| Machine learning something | Rules-based version of the same idea |
| Discord/Instagram bot | Same logic, local app, no API |

Say the reasoning out loud, because it's the real lesson:

> "Cutting scope isn't giving up. It's the actual skill. A small thing that works beats
> a big thing that doesn't, every single time, forever, in every job you will ever have."

---

## Capstone: Plan And First Build — HS only (20 min)

Set up the project properly. This 20 minutes is what makes Session 3 productive.

```powershell
cd $HOME\Documents
mkdir capstone
cd capstone
cc-ds
```

Four things, in order:

1. **Ask for a plan, not code:**
   ```
   I want to build [their app]. Don't write any code yet. Tell me what
   files you'd create, what goes in each one, and what order you'd
   build them in.
   ```
2. **Argue with the plan.** Change at least two things. Combine files, drop a feature,
   reorder the build. Changing a plan is free; changing code is not.
3. **Save the plan** as `PLAN.md` in the project folder.
4. **Build component 1 only.** Run it. Check it.

Full multi-file technique comes in Session 3 — this block is about getting a plan on
disk and one working piece before students leave.

### End of session

Everyone makes a save-point copy of their project folder before they leave:

```powershell
cd $HOME\Documents
Copy-Item -Recurse capstone capstone-working
```

That's the whole backup system, taught properly in Session 3. For now: **it works, so
copy it.**

---

## Wrap (built into the last block for both groups)

Two things on the board:

**How much to ask for:**
> New app → describe the whole thing. Existing app → one change at a time.
> If you can't say what should be different in one sentence, it's too big.

**How to check:**
> 1. Does it do the thing?
> 2. Does it survive the wrong thing?
> 3. Did it change something I didn't ask for?
> 4. Can I explain it?

Teaser for Session 3:

**MS:** "Next time: how to save your work so you can never lose it, and how to fix
things when the AI makes them worse."

**HS:** "Next time: your project gets too big for one file, and you finish your
capstone. Session 4 is demos only."

---

## Instructor Prep Checklist

- [ ] **Print camper notes** for the right age group, one per camper
- [ ] Print the bad-prompts handout (one per pair) — 3 prompts for MS, 6 for HS
- [ ] Print spec sheets (one per student, plus spares)
- [ ] Have a Session 1 app on hand for the six-changes-at-once demo (HS)
- [ ] Have the empty-list average bug ready to demo live
- [ ] Post the four checks on the wall — they stay up through Session 4
- [ ] **HS only:** print the scope-cut table for the pitch block
- [ ] **HS only:** be ready to sign off on ~25 capstone pitches in 12 minutes. Practice
      saying "cut one" quickly and kindly.
