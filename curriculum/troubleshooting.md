# Troubleshooting — Instructor Reference

Skim before Day 1. Keep open during sessions.

---

## Before Students Arrive (every day)

Run this on one lab machine:

```bash
python --version                # confirm it's python, not just python3
python -c "import tkinter"      # must produce no output
git --version
cc-ds                           # should launch and accept a prompt
```

If `python` isn't on PATH but `python3` is, **tell students that on the board** rather
than fixing 25 machines. Same for `pip`/`pip3`.

Git identity should be pre-set or the first commit prompts for it:

```bash
git config --global user.name "Student"
git config --global user.email "student@compucon.local"
```

---

## Claude Code Problems

### `cc-ds` doesn't start / hangs

1. `Ctrl+C`, run `cc-ds` again — fixes most of them
2. Check the network — it needs to reach the model API
3. Move to a spare machine rather than debugging in front of the class

### It's stuck thinking / no output for a long time

`Ctrl+C` and rerun. If it happens across the whole room at once, that's the API or the
network, not the students — go analog for a few minutes (spec sheets, prompt lab,
partner pitches) and retry.

### Responses got worse over a long session

Real, and worth naming as a lesson: the conversation is full of stale context.

```
/clear
```

Code is untouched. If there's a `CLAUDE.md`, the AI re-reads the project immediately.

### It's editing the wrong file / can't find the file

Almost always started in the wrong folder.

```bash
pwd     # where am I?
ls      # is my file here?
```

`Ctrl+C`, `cd` to the right folder, `cc-ds` again.

### It keeps "fixing" and making it worse

The conversation has locked onto a wrong theory. Escalate:

1. `/clear`, then describe the *problem* fresh — not the failed fixes
2. `git checkout .` back to working
3. Delete the broken file, ask for it again from scratch

### It wrote something in a language we're not using

Say the language and library in the prompt, or put it in `CLAUDE.md`:

```markdown
## Rules
- Python 3 and tkinter only. No other libraries.
```

### It's asking permission for everything and the student is confused

Explain once to the room: it's asking before it changes files or runs commands. Read
what it wants to do, then approve. Don't teach students to approve blindly — that's the
opposite of the whole curriculum.

---

## Python Problems

### `ModuleNotFoundError: No module named 'tkinter'`

Not installed. On Debian/Ubuntu lab images: `sudo apt install python3-tk`. Needs to
happen before Day 1, not during.

### `python: command not found`

Try `python3`. Put whichever works on the board.

### The tkinter window doesn't appear

- On a remote/SSH session there's no display — students must be at the physical machine
- The window may have opened behind the terminal — check the taskbar
- Missing `root.mainloop()` at the end. Tell the AI: *"The window doesn't appear when I
  run it."*

### The window opens and immediately closes

Same cause — missing `mainloop()`, or the script ends. Report it as a bug to the AI in
the standard format.

### `IndentationError` after a student hand-edits

Mixed tabs and spaces. Easiest fix: *"There's an indentation error on line 23, fix it."*

---

## Git Problems

### First commit asks for name and email

Pre-set it (above), or:

```bash
git config --global user.name "Student"
git config --global user.email "student@compucon.local"
```

### `git checkout .` didn't restore

They never committed. Nothing to restore to. Hard lesson, teaches itself — but soften it
and help them rebuild. Then have them commit immediately.

### It restored but the file's still broken

`git checkout .` only restores *tracked* files. A file created after the last commit is
untracked and survives. `git status` shows it. Delete it manually.

### They committed a broken version over a working one

```bash
git log --oneline          # find the good one
git checkout <hash> -- .   # restore files from it
```

Rare with students, but it happens.

---

## Classroom Problems

### One student is way ahead

Never "add more features." Instead:

- "Try to break it. Empty input, wrong type, click everything twice."
- "Ask the AI to explain the part of the code you understand least, then explain it to
  me."
- "Go help someone who's stuck." (Best option. Teaching is how they consolidate.)
- "Write a README so someone else could run it."

### One student is way behind

- Cut scope immediately and visibly. A working small thing beats a broken big thing.
- Pair them with someone who has a working app.
- Hand them a known-good prompt from the idea bank and let them start over. Restarting is
  cheap and they need a win.

### A student is just accepting everything without reading

The failure mode this whole curriculum exists to prevent. Interrupt with:

> "Show me what it just changed. What does this part do?"

If they can't answer, that's the teaching moment. Rule 4 exists for exactly this: *you
have to be able to explain what your app does.*

### A student is frustrated and shutting down

- Get them to a working state first — `git checkout .` or a fresh start. Do not debug
  with them while they're frustrated.
- Take the smallest possible next step. Any win.
- Name it honestly: "This is what it's actually like. Every professional has days like
  this."

### The whole room is stuck on the same thing

Stop everything and demo the fix on the projector. Ten minutes of your time beats
twenty-five students burning ten minutes each.

### Students racing to add features without testing

Halt the room. Pick a student's app, put it on the projector, and break it in 30 seconds
with empty input. This costs five minutes and resets the room's behavior for the rest of
the day.

---

## If The Network Or API Is Down

Have this ready. It's a real risk and it will happen at least once.

**Analog activities that still teach the actual skills:**

- **Prompt lab** — the six bad prompts from Day 2. Works entirely on paper.
- **Spec sheets** — write specs and tests for the next project.
- **Bug report drill** — instructor describes a broken app verbally; students write a
  proper what-I-did / what-I-expected / what-happened report.
- **Break the plan** — put an AI-generated project plan on the projector and have the
  room find three things wrong with it.
- **Read the code** — put a real code sample up and find the bugs. The empty-list average
  and the case-sensitive quiz checker both work great.
- **Paper demos** — sketch the app you'd build, pitch it to a partner, get scope-cut.

None of this is filler. Verification and scoping are the parts students are worst at, and
they don't need a computer.
