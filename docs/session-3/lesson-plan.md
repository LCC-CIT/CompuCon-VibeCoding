# Session 3 — Make It Solid / Build Something Bigger

**This session is genuinely different for the two age groups.** Not paced differently —
different content.

- **MS (85 min): *Make It Solid.*** Save points, debugging, and hardening a single-file
  app. Multi-file projects are **cut entirely** for middle school — there isn't time to
  teach planning, splitting, and building in 85 minutes without doing all three badly.
- **HS (180 min): *Build Something Bigger.*** Multi-file projects and planning, applied
  directly to the capstone they pitched in Session 2. **The capstone must be finished by
  the end of this session** — Session 4 is 60 minutes of demos only.

Read your age group's section. They share the save-points block and the debugging
method; everything else differs.

---

## Timing

### Middle school — 85 min

| Time | Block | Mode |
|---|---|---|
| 0:00–0:12 | Save points: copy the folder | Demo + hands-on |
| 0:12–0:25 | When the AI makes it worse | Talk + demo |
| 0:25–0:40 | The debugging method | Whole group |
| 0:40–1:10 | Build: make your app good | Independent |
| 1:10–1:25 | Show one thing you fixed | Campers demo |

> **No break scheduled.** If your group needs one, take 5 at 0:40 and cut the build to
> 25 minutes.

### High school — 180 min

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

# MIDDLE SCHOOL — Make It Solid (85 min)

Campers bring the app they built in Session 2 (or Session 1 — either is fine). Today
isn't about building something new. It's about making one thing genuinely good.

> "Today we're not making your app bigger. We're making it *tougher*. By the end it
> should be very hard to break, and you should know how to get it back when you do."

---

## 0:00 — Save Points: Copy The Folder (12 min)

Frame this as save points in a game.

### The problem

You've been building for 30 minutes. It works. You ask for one more feature. It's now
broken in a way you can't undo, and the AI's attempts to fix it are making it worse.

Without a save point, you're rebuilding from scratch.

### The whole system

Two commands. That's it.

```powershell
cd $HOME\Documents\Projects
cd <Name>
Copy-Item -Recurse madlibs madlibs-working
```

That's your save point — a complete copy of the folder, frozen at a moment it worked.

To go back:

```powershell
cd $HOME\Documents\Projects
cd <Name>
Remove-Item -Recurse madlibs
Copy-Item -Recurse madlibs-working madlibs
```

> You can also do this entirely in File Explorer: right-click the folder → Copy →
> Paste → rename it. Show both. Some campers will find the visual version much easier,
> and it is exactly as valid.

### Practice right now, everyone

1. Make a save-point copy of your project folder
2. Ask the AI to break something on purpose:
   > Delete the part that shows the story and replace it with something wrong.
3. Run it. Confirm it's broken.
4. Restore from your copy
5. Run it. It's back.

The relief in the room when step 5 works is the lesson.

### The rule

> **Copy it every time it works. Not when you finish — every time it works.**

Name your copies so you can tell them apart: `madlibs-working`, `madlibs-colors-good`,
`madlibs-before-sounds`.

---

## 0:12 — When The AI Makes It Worse (13 min)

A specific, recognizable situation: you report a bug, the AI fixes it, something else
breaks. You report that, it fixes that, the first thing breaks again. Round and round.

This happens to professionals. It is not a sign that you're bad at this.

### The three escape hatches

**1. `/clear` and start the conversation over.**

```
/clear
```

This resets the *conversation*, not your files. Your code is untouched.

Why it works: the AI has been building up a theory about your bug, and the theory is
wrong. Every new message you send gets interpreted through that wrong theory. Clearing
it out and describing the problem fresh often fixes it immediately.

> "It's like a friend who's decided what your problem is and won't stop giving you
> advice for the wrong problem. Sometimes you just have to start the conversation over."

**2. Go back to your save point.** You have a copy that works. Use it. Then take a
smaller step.

**3. Delete the file and ask for it again.** With a better description this time. One
file is cheap to regenerate.

### The 10-minute rule

> **Stuck on the same problem for 10 minutes? Stop. Restore your save point and try a
> different way — or ask a human.**

Sunk cost is a real trap and this is the age to learn it.

---

## 0:25 — The Debugging Method (15 min)

Whole group. Ask for volunteers who are stuck right now, put their screen up. Two bugs,
walked slowly.

For each one, walk the same four steps out loud:

### 1. What exactly happens?

Not "it's broken." What did you click, what did you expect, what did you get?

Most middle-school bugs get solved at this step. Being forced to describe it precisely
is often the entire fix.

### 2. When did it last work?

What changed since then? If it's more than one change, that's your answer — you broke the
one-change-at-a-time rule and now you're paying for it.

### 3. Ask precisely

> When I click Make Story with all the boxes empty, the window freezes and I have to
> close it. Here's what the terminal says: [paste the whole thing].

### 4. Verify the fix — and check the old thing still works

Run it. Then run the thing that *used* to work and make sure it still does.

This step is the one everybody skips. Fixing a bug by breaking something else is the
oldest move in the book.

---

## 0:40 — Build: Make Your App Good (30 min)

Not "add features." Three jobs, in this order:

### Job 1: Make it unbreakable (15 min)

Try every one of these on your own app. Fix what breaks. **Copy the folder after each
fix that works.**

- Leave every box empty and click the button
- Type a number where a word goes, and a word where a number goes
- Type something 200 characters long
- Click every button twice, fast
- Click buttons in the wrong order
- Resize the window as small as it goes

Checklist on the board — campers tick off what they've tested.

### Job 2: Make it look good (10 min)

Colors, fonts, spacing, window title, a friendlier message when something goes wrong.
One change at a time, run after each.

### Job 3: Understand one piece of it (5 min)

Pick the part of your code you understand least. Ask:

```
Explain what this part does, like I'm 12.
```

Be ready to tell the room what you learned.

**Instructor circulation:**

| What you see | What to say |
|---|---|
| Hasn't made a copy in 15 min | "Copy your folder. Right now." |
| Adding features instead of hardening | "Not bigger. Tougher. What breaks it?" |
| Tangled and frustrated | "When did it last work? Restore your copy." |
| Cruising | "Ask the AI what inputs would break it. Then try those." |

---

## 1:10 — Show One Thing You Fixed (15 min)

Not a full demo. Each camper shows **one bug they found and fixed**, in about 30
seconds:

1. Here's what broke it
2. Here's what it does now

Go quickly. Aim to get through everyone.

> "Every single person in this room found something wrong with their own app today. Not
> because you're bad at this — because *everybody's* first version has these. The
> difference between people who ship good software and people who don't is entirely
> whether they went looking."

**Wrap (last 2 min).** Next session: you pick something to build from scratch, and you
demo it at the end.

Two questions to think about before then:

1. What would you actually use?
2. What's the smallest version of that which is still cool?

---

# HIGH SCHOOL — Build Something Bigger (180 min)

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
# Quiz Game

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

Same content as the MS block above — teach it the same way, faster.

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

### Using copies to verify (HS-only addition)

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

**Both groups:**

- [ ] **Print camper notes** for the right age group, one per camper

- [ ] Confirm the `Documents\Projects` folder exists on every lab machine
- [ ] Practice the `Copy-Item -Recurse` / `Remove-Item -Recurse` restore cycle yourself
      first — you'll be walking campers through it under time pressure
- [ ] Know the File Explorer version too (right-click → Copy → Paste → rename); some
      campers will need the visual route
- [ ] Recruit two volunteers with real bugs before the debugging block starts

**MS only:**

- [ ] Have the "make it unbreakable" checklist on the board before they arrive
- [ ] A Session 2 app of your own to demo the break-and-restore cycle on

**HS only:**

- [ ] A grown 200+ line single-file app for the opening demo
- [ ] `CLAUDE.md` and `PLAN.md` templates ready to project
- [ ] Sample multi-file project to show the file split
- [ ] **Know which campers are behind before the build block starts.** They need scope
      cut today — there is no build time in Session 4.
