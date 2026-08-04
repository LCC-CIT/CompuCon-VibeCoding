# Day 3 — Build Something Bigger

**3 hours.** Days 1–2 were single files. Today: projects with multiple files, a plan
before the build, and the Claude Code features that exist because projects get big.

This is the day the tool stops being "a thing that writes a file" and becomes "a thing
that works in a codebase."

---

## Session Arc

| Time | Block | Mode |
|---|---|---|
| 0:00–0:15 | Why one file stops working | Demo + talk |
| 0:15–0:40 | Plan before you build | Talk + practice |
| 0:40–1:05 | Claude Code for real projects | Demo |
| 1:05–1:15 | **Break** | |
| 1:15–1:35 | Save points (a little git) | Demo + hands-on |
| 1:35–2:35 | Build: multi-file project | Independent |
| 2:35–2:55 | Debugging clinic | Whole group |
| 2:55–3:00 | Wrap + capstone pitch | |

---

## 0:00 — Why One File Stops Working (15 min)

Open a single-file app from Day 2 that's grown — 200+ lines. Scroll it slowly.

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

**MS/HS**
> **MS:** Three files max, and use obvious names (`game.py`, `words.py`, `screen.py`).
> Skip context windows — say "the AI does better with smaller files, same as you."
> **HS:** Context window is worth explaining properly. It also explains a real behavior
> they'll see: long sessions get worse, and `/clear` fixes it.

---

## 0:15 — Plan Before You Build (25 min)

### Ask for a plan, not code

The single highest-leverage move in this whole track:

```
I want to build a quiz game with multiple choice questions, a score,
and a results screen at the end.

Don't write any code yet. Tell me what files you'd create, what goes
in each one, and what order you'd build them in.
```

Do this live. You'll get a file breakdown and a build order back in seconds.

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

Run it. Check it. Then step 2. This is Day 2's one-at-a-time rule scaled up from
*changes* to *components*.

### The plan is your checklist

Keep the plan in a file. It's what you check finished work against — you have a written
list of what each file is supposed to do, so "did it do what I asked" has an actual
answer.

### Practice (10 min)

Pairs. Pick an idea from the Stretch tier and get a plan out of the AI. **Do not build
anything.** Read the plan and change at least two things about it. Be ready to say why.

**MS/HS**
> **MS:** Do this as one whole-group exercise on the projector, taking suggestions.
> Getting a plan and arguing with it is a genuinely new mode of thinking for this age.
> **HS:** Pairs, independently. Then have two pairs compare plans for the same app —
> different plans, both fine. Good moment about there being no single right answer.

---

## 0:40 — Claude Code For Real Projects (25 min)

Now that projects have multiple files, these features start earning their keep. Demo
each one live — no slides.

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

Have every student create one for their project after break. It takes two minutes and
the payoff is immediate.

### Ask before you commit

```
What would it take to add a timer to each question?

Would it be easier to store the scores in a text file or a spreadsheet?

Is there anything in this project that's going to cause problems later?
```

Free consulting. No code changes. Use it constantly.

### Reading what it did

After a change, scroll back through the output. It shows you the edits. If you skip
past that every time, you've given up your best verification tool for free.

**MS/HS**
> **MS:** Naming files and `/clear`. Do `CLAUDE.md` together on the projector, everyone
> copying — it's a great "the AI has notes about your project" moment. Skip the rest.
> **HS:** All of it. Add: point at an error message and paste the whole traceback, not
> just the last line. The stack tells the AI where to look.

---

## 1:05 — Break (10 min)

---

## 1:15 — Save Points (20 min)

Frame this as save points in a game, not as version control theory.

### The problem

You've been building for 40 minutes. It works. You ask for one more feature. It's now
broken in a way you can't undo, and the AI's attempts to fix it are making it worse.

Without save points, you're rebuilding from scratch.

### Minimum viable version control

Three commands. That's the whole lesson.

```powershell
git init                    # once, at the start

git add -A                  # SAVE POINT — these two together
git commit -m "working version with scoring"

git checkout .              # UNDO everything since the last save point
```

> Two separate lines for the save point. PowerShell 5.1 doesn't support `&&`.

Practice right now, everyone:

1. `git init` in your project folder
2. Commit your current working state
3. Ask the AI to break something on purpose:
   > Delete the scoring function and replace it with something wrong.
4. Run it. Confirm it's broken.
5. `git checkout .`
6. Run it. It's back.

The relief in the room when step 6 works is the lesson.

### The rule

> **Commit every time it works. Not when you finish — every time it works.**

You can also just let the AI do it:

```
Commit this with a message describing what we just added.
```

**MS/HS**
> **MS:** Do exactly the three commands and the break/restore drill. Nothing else — no
> branches, no history, no GitHub. The drill is what sticks.
> **HS:** Add `git log --oneline` to see history and `git diff` to see uncommitted
> changes. `git diff` is a verification tool: it's the literal answer to Day 2's check
> #3, "did it change anything I didn't ask for?"

---

## 1:35 — Build: Multi-File Project (60 min)

The biggest build block of the track. Students may extend a Day 2 project or start new.

### Requirements

- **At least 3 files**, each with a clear job
- **A `CLAUDE.md`** describing the project
- **A plan** from the AI, argued with and saved as `PLAN.md`
- **A git commit** every time it works
- **Built in order** — one component at a time, verified before the next

### Sequence on the board

```
1. Ask for a plan. Don't accept it as-is. Change something.
2. Save the plan as PLAN.md
3. Write CLAUDE.md
4. git init, first commit
5. Build component 1 → run → check → commit
6. Build component 2 → run → check → commit
7. Keep going
8. Wire it together → run → check → commit
```

Steps 5–7 are the rhythm. Say it out loud to the room every fifteen minutes:
**build, run, check, commit.**

### Instructor circulation

| What you see | What to say |
|---|---|
| Building all files at once | "Stop. Which one do you have running right now? Just that one." |
| Hasn't committed in 30 min | "Commit now. Right now." |
| Tangled and frustrated | "When did it last work? `git checkout .` and take a smaller step." |
| One giant file again | "What are the three jobs in this file? Ask the AI to split it into three." |
| Cruising | "Ask the AI what's going to cause you problems later. Then fix one of them." |

### The 20-minute rule

Anyone stuck on the same problem for 20 minutes: **`git checkout .` back to working and
approach it differently.** Sunk cost is a real trap and this is the age to learn it.

**MS/HS**
> **MS:** 3 files, hard cap. Instructor writes `PLAN.md` and `CLAUDE.md` templates on the
> projector for everyone to adapt. Checkpoint every 15 minutes: "hands up if you've
> committed since the last checkpoint."
> **HS:** 4–5 files fine. Require them to run `git diff` before at least one commit and
> say what changed. Encourage a real data file (JSON or CSV) as one component.

---

## 2:35 — Debugging Clinic (20 min)

Whole group. Real bugs from the room — ask for volunteers who are stuck, put their screen
up.

For each one, walk the same method out loud:

### The method

1. **What exactly happens?** Not "it's broken." What did you click, what did you expect,
   what did you get?
2. **Where could it be?** With multiple files, which one owns this behavior? Start there.
3. **When did it last work?** `git log` or memory. What changed since?
4. **Ask precisely:**
   > In scoring.py, when the answer is right the score goes down instead of up. Here's
   > the terminal output: [paste]. What's happening?
5. **Verify the fix.** Run it. Then run the thing that *used* to work and make sure it
   still does.

Step 5 is the one everybody skips. Fixing a bug by breaking something else is the
oldest move in the book.

### The escape hatches

When the AI's fixes are making it worse:

- **`/clear` and re-describe the problem fresh.** Often the conversation has accumulated
  a bad theory that the AI keeps returning to.
- **`git checkout .`** back to the last working state and take a smaller step.
- **Delete the broken file** and ask for it again from scratch with a better description.
  One file is cheap to regenerate. This is a real advantage of splitting things up.
- **Ask a human.** Twenty minutes is the limit.

**MS/HS**
> **MS:** Two bugs, walked slowly. Emphasize step 1 — most of their bugs get solved by
> being forced to describe them precisely.
> **HS:** Three or four bugs, faster. Push step 2 hard — "which file owns this?" is the
> question that separates people who can navigate a codebase from people who can't.

---

## 2:55 — Wrap + Capstone Pitch (5 min)

Today's three moves:

> **Plan before you build. Split by job. Commit every time it works.**

**Homework-ish:** think about what you want to build tomorrow. Day 4 is your project,
your choice, demoed to the room at the end.

Two questions to think about tonight:

1. What would you actually use?
2. What's the smallest version of that which is still cool?

---

## Instructor Prep Checklist

- [ ] A grown 200+ line single-file app for the opening demo
- [ ] `git` installed and confirmed on lab machines: `git --version`
- [ ] Git identity pre-set on lab machines, or students hit a prompt on first commit:
      `git config --global user.name "Student"` and `user.email "student@compucon.local"`
- [ ] `CLAUDE.md` and `PLAN.md` templates ready to project
- [ ] Sample multi-file project to show the file split
- [ ] Recruit two volunteers with real bugs before the clinic starts
