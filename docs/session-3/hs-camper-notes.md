# Session 3 — Build Something Bigger

## Contents

- [Vibe Coding · High School · Keep this with you](#vibe-coding-high-school-keep-this-with-you)
- [What you're doing today](#what-youre-doing-today)
- [Today's plan](#todays-plan)
- [Starting up](#starting-up)
- [Why one file stops working](#why-one-file-stops-working)
  - [The fix: split by job](#the-fix-split-by-job)
- [Plan before you build](#plan-before-you-build)
  - [Argue with it](#argue-with-it)
  - [Then build in order, one piece at a time](#then-build-in-order-one-piece-at-a-time)
  - [Your `PLAN.md` is your checklist](#your-planmd-is-your-checklist)
- [Claude Code for real projects](#claude-code-for-real-projects)
  - [Point at files directly](#point-at-files-directly)
  - [`/clear` — reset the conversation](#clear-reset-the-conversation)
  - [`CLAUDE.md` — notes the AI reads every time](#claudemd-notes-the-ai-reads-every-time)
  - [Ask before you commit to something](#ask-before-you-commit-to-something)
  - [Read what it did](#read-what-it-did)
- [Save points](#save-points)
  - [If restore fails](#if-restore-fails)
  - [Copies as a verification tool](#copies-as-a-verification-tool)
- [The capstone build](#the-capstone-build)
  - [Requirements](#requirements)
  - [The rhythm](#the-rhythm)
  - [Watch the clock](#watch-the-clock)
  - [If you finish early](#if-you-finish-early)
  - [If you get stuck](#if-you-get-stuck)
- [Debugging method](#debugging-method)
  - [Escape hatches](#escape-hatches)
- [Before you leave: demo prep](#before-you-leave-demo-prep)
  - [Make the demo copy](#make-the-demo-copy)
  - [Plan your 90 seconds](#plan-your-90-seconds)
- [The short version](#the-short-version)
- [Taking it home](#taking-it-home)

### Vibe Coding · High School · Keep this with you

---

## What you're doing today

Two things at once: learning to run a project that doesn't fit in a single file, and
**finishing your capstone**.

> ## Your capstone has to be done by the end of today.
> Session 4 is 60 minutes and it is entirely demos. There is no build time. Whatever
> runs when you leave today is what you demo.

Plan around that. If you're behind at the halfway mark, cut a feature — don't hope.

---

## Today's plan

| | Block |
|---|---|
| **1** | Why one file stops working |
| **2** | Plan before you build — revising your `PLAN.md` |
| **3** | Claude Code for real projects |
| **4** | Break |
| **5** | Save points — copy the folder |
| **6** | **Capstone build** (the big block) |
| **7** | Debugging clinic |
| **8** | Demo prep + wrap |

---

## Starting up

```powershell
cd $HOME\Documents\Projects
cd <Name>
cd capstone
claude
```

`<Name>` is your name — the folder you made in Session 1.

**Run it:** `python main.py`

`Ctrl+C` quits · `/clear` resets the conversation without touching your code · one
command per line, no `&&`

---

## Why one file stops working

Once an app passes ~200 lines, two things go wrong — and only one of them is the AI's
problem.

**1. You can't find anything.** That's yours. You cannot verify what you cannot locate.

**2. The AI has to hold the entire file in its head to change one line.** Every AI has a
limited amount it can attend to at once — its **context window**. A 500-line file eats a
lot of it. A 2000-line file eats most of it, and output quality visibly drops.

> It's not that the AI gets dumber. It's reading a novel to answer a question about one
> paragraph. Give it the paragraph.

This also explains something you've probably already noticed: long sessions get worse.
`/clear` fixes it.

### The fix: split by job

```
quiz/
  main.py        ← starts the app, wires things together
  questions.py   ← the question data
  scoring.py     ← how points work
  display.py     ← the window and buttons
```

Now "change the scoring" means the AI reads `scoring.py` — faster, more accurate, and
**you know exactly where to look to check it.** That second part is the real payoff.

---

## Plan before you build

The highest-leverage move in this entire course:

```
I want to build [your app].

Don't write any code yet. Tell me what files you'd create, what goes
in each one, and what order you'd build them in.
```

You'll get a file breakdown and a build order in seconds. Now the important part:

### Argue with it

- "Do I need six files for this? Combine two."
- "Skip the database, use a text file."
- "Build the scoring first, the window last."

> You just made five architecture decisions in ninety seconds without writing a line of
> code. **Changing a plan is free. Changing code is not.**

### Then build in order, one piece at a time

```
Let's build step 1 only: questions.py with 10 multiple choice questions.
Nothing else yet.
```

Run it. Check it. Then step 2. This is Session 2's one-change-at-a-time rule, scaled up
from *changes* to *components*.

### Your `PLAN.md` is your checklist

You wrote one last session. Open it and pressure-test it against what you now know about
splitting files:

```
Given this plan, what files should this project have? Should any of
what you suggested be split or combined?
```

Change at least one thing. Save it. **This is the last planning you do today** — the rest
of the session is building.

---

## Claude Code for real projects

### Point at files directly

```
Look at scoring.py and tell me what it does.
In display.py, make the score label bigger.
The bug is in main.py, not the other files.
```

Naming the file focuses the AI and saves it reading everything. Faster and more accurate.

### `/clear` — reset the conversation

```
/clear
```

Fresh conversation, same folder, same files. **Your code is untouched.**

> Rule of thumb: when you switch to a genuinely different task, `/clear` first.

### `CLAUDE.md` — notes the AI reads every time

Make a file called `CLAUDE.md` in your project folder. Claude Code reads it automatically
at the start of every session.

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

> The difference between an intern you brief every morning and one who read the handbook.

**Write one for your capstone before the build block.** Two minutes, immediate payoff.

### Ask before you commit to something

```
What would it take to add a timer to each question?
Is there anything in this project that's going to cause problems later?
```

Free consulting, no code changes. Use it constantly.

### Read what it did

After a change, scroll back through the output. It shows you the edits. Skipping past
that is throwing away your best verification tool.

---

## Save points

**SAVE** — every time it works:

```powershell
cd $HOME\Documents\Projects
cd <Name>
Copy-Item -Recurse capstone capstone-working
```

**RESTORE:**

```powershell
cd $HOME\Documents\Projects
cd <Name>
Remove-Item -Recurse capstone
Copy-Item -Recurse capstone-working capstone
```

Name copies meaningfully — `capstone-scoring-works`, not `capstone2`.

### If restore fails

**"Being used by another process"** → your app is still running or the AI is open in that
folder. Close the window, `Ctrl+C`, retry.

**Argument order** is `Copy-Item -Recurse SOURCE DESTINATION`. Reversing it copies the
broken version over your good one.

**Don't copy into the project folder.** `cd $HOME\Documents\Projects`, then
`cd <Name>`, so copies sit *beside* your project, not inside it. A copy inside the
folder gets read by the AI as part of your project and causes genuinely bizarre problems.

### Copies as a verification tool

This is check #3 from last session — *"did it change anything I didn't ask for?"* — made
concrete.

Before a risky change, copy the folder. Afterward, open the old file and the new file
side by side and compare. Two windows, and you have a diff done by hand.

You can also ask:

```
Compare the current version of scoring.py to what it was before my
last request. What actually changed?
```

> You now have the ability to answer "what did it actually change?" with **certainty**
> instead of trust. Use it before anything that scares you.

---

## The capstone build

### Requirements

- **At least 3 files**, each with a clear job
- **A `CLAUDE.md`** describing the project
- **A revised `PLAN.md`**
- **A folder copy** every time it works
- **Built in order** — one component at a time, verified before the next

### The rhythm

> ## build → run → check → copy

### Watch the clock

- **30 min in:** two components should be working. If not, get an instructor — you're
  cutting something.
- **25 min left:** last new feature starts now or not at all.
- **12 min left:** no new features. Make what you have work properly.
- **5 min left:** copy your working folder. Right now.

### If you finish early

- Try to break it, then fix what breaks
- Ask: *"What's confusing about this app for someone who's never seen it?"* Fix that
- Write a `README.md` explaining what it does and how to run it
- Help someone who's stuck

### If you get stuck

**20 minutes on the same problem = restore your last working copy and take a different
approach.** Sunk cost is real. Back out.

---

## Debugging method

1. **What exactly happens?** Not "it's broken." What did you click, expect, get?
2. **Where could it be?** With multiple files — which one owns this behavior? Start
   there. This question is what separates people who can navigate a codebase from people
   who can't.
3. **When did it last work?** Which copy is the last good one? What changed since?
4. **Ask precisely:**
   > In scoring.py, when the answer is right the score goes down instead of up. Terminal
   > output: [paste]. What's happening?
5. **Verify the fix** — and re-run the thing that used to work.

Step 5 is the one everybody skips.

### Escape hatches

- `/clear` and describe the problem fresh — the conversation may have a bad theory stuck
  in it
- Restore the last working copy, take a smaller step
- Delete the broken file and regenerate it. One file is cheap — a real advantage of
  having split things up.
- Ask a human. Twenty minutes is the limit.

---

## Before you leave: demo prep

**Session 4 is 60 minutes of demos with no build time.** Whatever runs now is what you
show.

### Make the demo copy

```powershell
cd $HOME\Documents\Projects
cd <Name>
Copy-Item -Recurse capstone capstone-demo
```

If you tinker at home\* and break something, this one survives.

<small>\* Tinkering at home needs your own account with an AI coding tool. Claude Code,
the tool you used in class, is a paid product. Some tools have free options to start
with — see the [OpenCode Zen how-to](../session-1/opencode-zen-howto.html).</small>

### Plan your 90 seconds

```
1. What it is, in one sentence.
2. Show it working. (Practice the exact clicks. Twice.)
3. One thing that broke and how you fixed it.
4. One thing the AI got wrong that you caught.
5. What you'd add next.
```

**Practice the clicks.** The most common demo failure is clicking around live, hitting a
bug you've never seen, and losing your nerve. Rehearsing the path twice fixes it.

If it crashes on stage: say what it does and keep going.

---

## The short version

> ## Plan before you build. Split by job. Copy every time it works.

---

## Taking it home

Your project is on this computer. Save a copy to your Google Drive folder:

1. Open the [Google Drive link](https://drive.google.com/drive/folders/1iNAG8vacKNsL3-c_1e_363R00ZxjgJPM?usp=drive_link)
2. Find the folder with your name
3. Copy your project folder into it

------

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/) This Vibe Coding Curriculum by [Brian Bird](https://profbird.dev), created in <time>2026</time> with AI assistance, is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
