# Troubleshooting — Instructor Reference

Skim before Day 1. Keep open during sessions.

**Environment: Windows 11 laptops, PowerShell via Windows Terminal, `python` on PATH.**
All commands below assume that.

---

## Before Students Arrive (every day)

Run this on one lab machine:

```powershell
python --version                # should print 3.x
python -c "import tkinter"      # must produce no output
git --version
cc-ds                           # should launch and accept a prompt
```

Git identity should be pre-set or the first commit prompts for it:

```powershell
git config --global user.name "Student"
git config --global user.email "student@compucon.local"
```

### PowerShell gotchas worth knowing before you're in front of 25 kids

- **`&&` does not work** in Windows PowerShell 5.1 (the Windows 11 default). One command
  per line. If a student copies a chained command off the internet, this is why it failed.
- **Paths use backslashes** — `$HOME\Documents`, not `~/Documents`. `/` often works
  anyway, but the AI may generate either; both are fine in Python.
- **Execution policy** can block scripts. It won't affect anything in this curriculum
  (we only run `python file.py`), but if you hit it: `Get-ExecutionPolicy` to check.
- **`python` with no arguments** on some Windows setups opens the Microsoft Store instead
  of Python. If that happens, Python isn't properly installed on that image — swap the
  machine, don't debug it during class.

---

## Claude Code Problems

### `cc-ds` doesn't start / hangs

1. `Ctrl+C`, run `cc-ds` again — fixes most of them
2. Check the network — it needs to reach the model API
3. Move to a spare machine rather than debugging in front of the class

### A student is using `cc` and something differs

`cc` runs Claude Code on Anthropic's models via the student's own Claude Pro account;
`cc-ds` runs it on DeepSeek. The tool, commands, and everything in this curriculum are
identical. Differences you may see:

- **Slightly different code style or verbosity.** Not a problem. Don't chase it.
- **`cc` hits a usage limit.** Pro accounts have caps. Have them switch to `cc-ds` —
  the project folder is unchanged, so they just restart and keep going.
- **A student didn't log in.** `cc` will prompt for auth. If they don't have an account,
  `cc-ds` is the answer.

Don't let this become a topic. One mention on Day 1, then treat them as the same thing.

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

```powershell
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

On Windows, tkinter ships with the standard python.org installer, so this means Python
was installed without the "tcl/tk and IDLE" option ticked. **Not a class-time fix** —
move the student to another machine and reimage later.

### `python` opens the Microsoft Store

Windows' app-execution alias is intercepting it and real Python isn't on PATH. Swap
machines. Don't fix this during a session.

### The tkinter window doesn't appear

- **Check the taskbar** — it usually opened behind Windows Terminal. This is the answer
  most of the time.
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

```powershell
git config --global user.name "Student"
git config --global user.email "student@compucon.local"
```

### `git add -A && git commit -m "..."` fails

PowerShell 5.1 doesn't support `&&`. Two separate lines:

```powershell
git add -A
git commit -m "message here"
```

### `git checkout .` didn't restore

They never committed. Nothing to restore to. Hard lesson, teaches itself — but soften it
and help them rebuild. Then have them commit immediately.

### It restored but the file's still broken

`git checkout .` only restores *tracked* files. A file created after the last commit is
untracked and survives. `git status` shows it. Delete it manually.

### They committed a broken version over a working one

```powershell
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

### A student wants to use a language other than Python

Allowed — if they already know it. Say yes and set two conditions:

1. **It has to run on this laptop with no installs.** Web (HTML/CSS/JS in a browser) is
   the easy yes. Anything needing a toolchain, SDK, or account is a no today.
2. **They're on their own for language-specific bugs.** You're supporting 25 students in
   Python. Be upfront and friendly about it.

Everything you're teaching still applies unchanged — prompt sizing, the four checks,
scope cutting, commits. Only the example code differs. A student building in JS is
getting the same curriculum.

Watch for the student who picks an unfamiliar language *because* it sounds impressive.
Ask: "have you written this before?" If no, steer to Python for today.

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
