# Session 3 — Build Something Bigger

**High school only.** Middle school is a single 85-minute session — Session 1 — and ends
there.

Multi-file projects and planning, applied directly to the capstone they pitched in
Session 2. **The capstone must be finished by the end of this session** — Session 4 is
60 minutes of demos only.

---

## Contents

- [Timing — 180 min](#timing-180-min)
- [0:00 — Why One File Stops Working (12 min)](#000-why-one-file-stops-working-12-min)
  - [The two real problems](#the-two-real-problems)
  - [The fix](#the-fix)
- [0:12 — Plan Before You Build (20 min)](#012-plan-before-you-build-20-min)
  - [Ask for a plan, not code](#ask-for-a-plan-not-code)
  - [Build in order, verify each piece](#build-in-order-verify-each-piece)
  - [The plan is your checklist](#the-plan-is-your-checklist)
  - [Campers revise their own plan (8 min)](#campers-revise-their-own-plan-8-min)
- [0:32 — Claude Code For Real Projects (18 min)](#032-claude-code-for-real-projects-18-min)
  - [Point at files directly](#point-at-files-directly)
  - [`/clear` — start a fresh conversation](#clear-start-a-fresh-conversation)
  - [`CLAUDE.md` — notes the AI reads every time](#claudemd-notes-the-ai-reads-every-time)
  - [Ask before you commit](#ask-before-you-commit)
  - [Reading what it did](#reading-what-it-did)
- [0:50 — Break (10 min)](#050-break-10-min)
- [1:00 — Save Points: Copy The Folder (15 min)](#100-save-points-copy-the-folder-15-min)
  - [The system](#the-system)
  - [Practice (5 min)](#practice-5-min)
  - [The rule](#the-rule)
  - [Using copies to verify](#using-copies-to-verify)
- [1:15 — Capstone Build (75 min)](#115-capstone-build-75-min)
  - [Requirements](#requirements)
  - [The rhythm, on the board](#the-rhythm-on-the-board)
  - [Timed callouts](#timed-callouts)
  - [Instructor circulation](#instructor-circulation)
  - [The 20-minute rule](#the-20-minute-rule)
  - [For campers who finish early](#for-campers-who-finish-early)
- [2:30 — Debugging Clinic (18 min)](#230-debugging-clinic-18-min)
  - [The escape hatches](#the-escape-hatches)
- [2:48 — Demo Prep + Wrap (12 min)](#248-demo-prep-wrap-12-min)
  - [Make the safety copy (3 min)](#make-the-safety-copy-3-min)
  - [Plan the 90 seconds (7 min)](#plan-the-90-seconds-7-min)
  - [Today's three moves (2 min)](#todays-three-moves-2-min)
- [Instructor Prep Checklist](#instructor-prep-checklist)

## Timing — 180 min

| Time | Block | Mode |
|---|---|---|
| 0:00–0:12 | Why one file stops working | Demo + talk |
| 0:12–0:32 | Plan before you build | Talk + practice |
| 0:32–0:50 | Claude Code for real projects | Demo |
| 0:50–1:00 | **Break** | |
| 1:00–1:15 | Save points: copy the folder | Demo + hands-on |
| 1:15–2:30 | Capstone build | Independent |
| 2:30–2:48 | Debugging clinic | Whole group |
| 2:48–3:00 | Demo prep + wrap | |

---

Campers continue the capstone they pitched and planned in Session 2. **It has to be
finished by the end of today.** Session 4 is 60 minutes and is demos only — say this at
the start and again at the halfway mark.

---

## 0:00 — Why One File Stops Working (12 min)

Open a single-file app that's grown — 200+ lines. Scroll it slowly.

Ask: **"If I want to change how the score is calculated, where do I look?"**

Now try this live:

> Change the way the score is calculated so that a wrong answer subtracts a point.

Watch what happens. Frequently the AI touches something else — the display, the reset
logic — because in one long file everything is tangled together.

### The two real problems

**1. You can't find anything.** Not the AI's problem, yours. You can't verify what you
can't locate.

**2. The AI has to hold the whole file in its head to change one line.** Every AI has a
limited amount it can pay attention to at once — its **context window**. A 500-line file
eats a lot of that. A 2000-line file eats most of it, and quality drops noticeably.

> "It's not that the AI gets dumber. It's that it's reading a novel to answer a question
> about one paragraph. Give it the paragraph."

This also explains a behavior they've probably already seen: long sessions get worse, and
`/clear` fixes it.

### The fix

Split by *job*:

```
quiz/
  main.py        ← starts the app, wires things together
  questions.py   ← the question data
  scoring.py     ← how points work
  display.py     ← the window and buttons
```

Now "change the scoring" means the AI reads `scoring.py`. Faster, more accurate, and
**you know where to look to check it.** That second part is the point.

---

## 0:12 — Plan Before You Build (20 min)

Campers already have a `PLAN.md` from Session 2. Today they pressure-test it against
what they now know about file splitting.

### Ask for a plan, not code

The single highest-leverage move in this whole track:

```
I want to build a quiz game with multiple choice questions, a score,
and a results screen at the end.

Don't write any code yet. Tell me what files you'd create, what goes
in each one, and what order you'd build them in.
```

Do this live on the projector with a fresh example. You'll get a file breakdown and a
build order back in seconds.

Now the crucial part — **read it and argue with it.**

- "Do I need 6 files for this? Combine two."
- "Skip the database, use a text file."
- "Build the questions and scoring first, the window last."

> "You just made five architecture decisions in ninety seconds without writing a line of
> code. Changing a plan is free. Changing code is not."

### Build in order, verify each piece

Once the plan is agreed:

```
Let's build step 1 only: questions.py with 10 multiple choice questions.
Nothing else yet.
```

Run it. Check it. Then step 2. This is Session 2's one-at-a-time rule scaled up from
*changes* to *components*.

### The plan is your checklist

`PLAN.md` is what you check finished work against — you have a written list of what each
file is supposed to do, so "did it do what I asked" has an actual answer.

### Campers revise their own plan (8 min)

Everyone opens their `PLAN.md` and asks:

```
Given this plan, what files should this project have? Should any of
what you suggested be split or combined?
```

Change at least one thing. Save it. **This is the last planning you do today** — the rest
of the session is building.

---

## 0:32 — Claude Code For Real Projects (18 min)

Demo each one live — no slides.

### Point at files directly

```
Look at scoring.py and tell me what it does.

In display.py, make the score label bigger.

The bug is in main.py, not the other files.
```

Naming the file focuses the AI and saves it from reading everything. Faster and more
accurate.

### `/clear` — start a fresh conversation

Long sessions accumulate junk. Fifteen turns in, the AI is still carrying around the bug
you fixed an hour ago and the feature you abandoned.

```
/clear
```

Fresh start, same folder, same files. **Your code is untouched** — only the conversation
resets.

> "Rule of thumb: when you switch to a genuinely different task, `/clear` first."

### `CLAUDE.md` — notes the AI reads every time

Create a file called `CLAUDE.md` in the project folder. Claude Code reads it
automatically at the start of every session.

```markdown
## Quiz Game

A multiple-choice quiz in Python + tkinter.

## Files
- main.py — starts the app
- questions.py — question data, list of dicts
- scoring.py — 1 point right, -1 wrong, no negative totals
- display.py — the tkinter window

## Rules
- Python only, tkinter only. No extra libraries.
- Keep every file under 100 lines.
- Answer checking is case-insensitive.
```

Now you never re-explain your project. Every new session already knows.

> "This is the difference between an intern you brief every morning and one who read the
> handbook."

**Every camper writes one for their capstone before the build block.** Two minutes, and
the payoff is immediate.

### Ask before you commit

```
What would it take to add a timer to each question?

Is there anything in this project that's going to cause problems later?
```

Free consulting. No code changes. Use it constantly.

### Reading what it did

After a change, scroll back through the output. It shows you the edits. If you skip past
that every time, you've given up your best verification tool for free.

---

## 0:50 — Break (10 min)

---

## 1:00 — Save Points: Copy The Folder (15 min)

This is the one piece of housekeeping that pays for itself inside the same session. Move
briskly — it's fifteen minutes and they need every one of the seventy-five that follow.

### The system

```powershell
cd $HOME\Documents\Projects
cd <Name>
Copy-Item -Recurse capstone capstone-working
```

To restore:

```powershell
cd $HOME\Documents\Projects
cd <Name>
Remove-Item -Recurse capstone
Copy-Item -Recurse capstone-working capstone
```

### Practice (5 min)

Everyone: make a copy, ask the AI to break something, restore it, confirm it's back.

### The rule

> **Copy every time it works.** Name copies meaningfully — `capstone-scoring-works`,
> not `capstone2`.

### Using copies to verify

This is Session 2's check #3 — *"did it change anything I didn't ask for?"* — made
concrete.

Before a risky change, copy the folder. After the change, ask:

```
Compare the current version of scoring.py to what it was before my
last request. What actually changed?
```

You have the old copy on disk, so you can also just open both files side by side and
look. Two files, two windows. That's a diff, done by hand.

> "You now have the ability to answer 'what did it actually change?' with certainty
> instead of trust. Use it before anything that scares you."

---

## 1:15 — Capstone Build (75 min)

The biggest block in the track. This is where the capstone gets finished.

### Requirements

- **At least 3 files**, each with a clear job
- **A `CLAUDE.md`** describing the project
- **A revised `PLAN.md`**
- **A folder copy** every time it works
- **Built in order** — one component at a time, verified before the next

### The rhythm, on the board

```
build → run → check → copy
```

Say it out loud to the room every fifteen minutes.

### Timed callouts

- **At 0:30 into the block:** "You should have two components working. If you don't, come
  see me — we're cutting something."
- **25 min left:** "Last new feature starts now or not at all."
- **12 min left:** "No new features. Make what you have work properly."
- **5 min left:** "Make a folder copy of your working version. Right now."

Walk the room enforcing that last one. A copied working version means nobody demos a
broken app next session.

### Instructor circulation

| What you see | What to say |
|---|---|
| Building all files at once | "Stop. Which one do you have running right now? Just that one." |
| Hasn't copied in 25 min | "Copy your folder now." |
| Tangled and frustrated | "When did it last work? Restore the copy and take a smaller step." |
| One giant file again | "What are the three jobs in this file? Ask the AI to split it into three." |
| Cruising | "Ask the AI what's going to cause you problems later. Then fix one of them." |
| Behind schedule | Cut a must-have. Visibly. Now, not at 2:25. |

### The 20-minute rule

Anyone stuck on the same problem for 20 minutes: **restore the last working copy and
approach it differently.**

### For campers who finish early

- Try to break it, then fix what breaks
- Ask: *"What's confusing about this app for someone who's never seen it?"* Fix that
- Write a `README.md` explaining what it does and how to run it
- Help a neighbor who's stuck

---

## 2:30 — Debugging Clinic (18 min)

Whole group. Real bugs from the room — volunteers, screens up.

For each one, walk the same method out loud:

1. **What exactly happens?** Not "it's broken." What did you click, what did you expect,
   what did you get?
2. **Where could it be?** With multiple files, which one owns this behavior? Start there.
   This question is what separates people who can navigate a codebase from people who
   can't.
3. **When did it last work?** Which folder copy is the last good one? What changed since?
4. **Ask precisely:**
   > In scoring.py, when the answer is right the score goes down instead of up. Here's
   > the terminal output: [paste]. What's happening?
5. **Verify the fix.** Run it. Then run the thing that *used* to work and make sure it
   still does.

Step 5 is the one everybody skips.

### The escape hatches

- **`/clear`** and re-describe the problem fresh — the conversation may have a bad theory
  stuck in it
- **Restore the last working copy** and take a smaller step
- **Delete the broken file** and ask for it again from scratch. One file is cheap to
  regenerate — a real advantage of having split things up
- **Ask a human.** Twenty minutes is the limit.

---

## 2:48 — Demo Prep + Wrap (12 min)

**Session 4 is 60 minutes and it is entirely demos.** There is no build time. Whatever
runs at the end of today is what gets demoed.

### Make the safety copy (3 min)

Everyone, right now:

```powershell
cd $HOME\Documents\Projects
cd <Name>
Copy-Item -Recurse capstone capstone-demo
```

That's the version being demoed. If they tinker at home and break it, this one survives.

### Plan the 90 seconds (7 min)

```
1. What it is, in one sentence.
2. Show it working. (Practice the exact clicks. Twice.)
3. One thing that broke and how you fixed it.
4. One thing the AI got wrong that you caught.
5. What you'd add next.
```

**Practice the clicks.** The most common demo failure is a camper clicking around live,
hitting a bug they've never hit before, and losing their nerve. Rehearsing the path twice
fixes it.

Have a fallback ready: if it crashes on stage, say what it does and keep going.

### Today's three moves (2 min)

> **Plan before you build. Split by job. Copy every time it works.**

---

## Instructor Prep Checklist

- [ ] **Print camper notes**, one per camper
- [ ] Confirm the `Documents\Projects` folder exists on every lab machine
- [ ] Practice the `Copy-Item -Recurse` / `Remove-Item -Recurse` restore cycle yourself
      first — you'll be walking campers through it under time pressure
- [ ] Know the File Explorer version too (right-click → Copy → Paste → rename); some
      campers will need the visual route
- [ ] Recruit two volunteers with real bugs before the debugging block starts
- [ ] A grown 200+ line single-file app for the opening demo
- [ ] `CLAUDE.md` and `PLAN.md` templates ready to project
- [ ] Sample multi-file project to show the file split
- [ ] **Know which campers are behind before the build block starts.** They need scope
      cut today — there is no build time in Session 4.

------

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/) This Vibe Coding Curriculum by [Brian Bird](https://profbird.dev), created in <time>2026</time> with AI assistance, is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
