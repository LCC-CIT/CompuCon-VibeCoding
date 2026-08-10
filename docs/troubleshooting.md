# Troubleshooting — Instructor Reference

Skim before Session 1. Keep open during sessions.

**Environment: Windows 11 laptops, PowerShell via Windows Terminal, `python` on PATH.**
All commands below assume that.

---

## Before Campers Arrive (every session)

Run this on one lab machine:

```powershell
python --version                # should print 3.x
python -c "import tkinter"      # must produce no output
claude                           # should launch and accept a prompt
```

No git check needed — campers don't use git. Save points are folder copies; see
"Save Point / Undo Problems" below.

### PowerShell gotchas worth knowing before you're in front of 25 kids

- **`&&` does not work in PowerShell 5.1.** Lab machines may run 5.1 or 7, and there's
  no reliable way to tell which from the outside — so write and teach every command
  one-per-line regardless of version. That syntax works on both.
- **Paths use backslashes** — `$HOME\Documents\Projects`, not `~/Documents/Projects`.
  `/` often works anyway, but the AI may generate either; both are fine in Python.
- **Execution policy** can block scripts. It won't affect anything in this curriculum
  (we only run `python file.py`), but if you hit it: `Get-ExecutionPolicy` to check.
- **`python` with no arguments** on some Windows setups opens the Microsoft Store instead
  of Python. If that happens, Python isn't properly installed on that image — swap the
  machine, don't debug it during class.

---

## Claude Code Problems

### `claude` doesn't start / hangs

1. `Ctrl+C`, run `claude` again — fixes most of them
2. Check the network — it needs to reach the model API
3. Move to a spare machine rather than debugging in front of the class

### `claude` prompts for a login

`claude` is the one command on every machine. If it asks to log in, that machine isn't
signed in — get every machine signed in during "Before Campers Arrive," and if one
still prompts, move the camper to a machine that's signed in. Don't debug logins in
front of the class.

### It's stuck thinking / no output for a long time

`Ctrl+C` and rerun. If it happens across the whole room at once, that's the API or the
network, not the campers — go analog for a few minutes (spec sheets, prompt lab,
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
Get-Location    # where am I?
Get-ChildItem   # is my file here?
```

`Ctrl+C`, `cd` to the right folder, `claude` again.

### It keeps "fixing" and making it worse

The conversation has locked onto a wrong theory. Escalate:

1. `/clear`, then describe the *problem* fresh — not the failed fixes
2. Restore their last working folder copy
3. Delete the broken file, ask for it again from scratch

### It wrote something in a language we're not using

Say the language and library in the prompt, or put it in `CLAUDE.md`:

```markdown
## Rules
- Python 3 and tkinter only. No other libraries.
```

### It's asking permission for everything and the camper is confused

Explain once to the room: it's asking before it changes files or runs commands. Read
what it wants to do, then approve. Don't teach campers to approve blindly — that's the
opposite of the whole curriculum.

---

## Python Problems

### `ModuleNotFoundError: No module named 'tkinter'`

On Windows, tkinter ships with the standard python.org installer, so this means Python
was installed without the "tcl/tk and IDLE" option ticked. **Not a class-time fix** —
move the camper to another machine and reimage later.

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

### `IndentationError` after a camper hand-edits

Mixed tabs and spaces. Easiest fix: *"There's an indentation error on line 23, fix it."*

---

## Save Point / Undo Problems

Campers don't use git. Save points are folder copies — see Session 3. The reference
commands:

```powershell
cd $HOME\Documents\Projects
cd <Name>
Copy-Item -Recurse myproject myproject-working    # SAVE

Remove-Item -Recurse myproject                    # UNDO (two steps)
Copy-Item -Recurse myproject-working myproject
```

`<Name>` is the camper's name folder — each camper works inside their own, so
projects are `Projects\<Name>\<project>`.

### They never made a copy

Nothing to restore to. Hard lesson, teaches itself — but soften it and help them rebuild.
Then have them make a copy immediately, and check on them again in ten minutes.

### `Remove-Item -Recurse` asks for confirmation

On some setups it prompts per-item. Add `-Force`:

```powershell
Remove-Item -Recurse -Force myproject
```

Only teach `-Force` when it comes up — it's one more thing to explain, and it makes the
delete irreversible.

### "Cannot remove item — being used by another process"

The app is still running, or Claude Code is open in that folder. Close the tkinter
window, `Ctrl+C` out of `claude`, then retry.

This is the most common failure in the restore cycle. Check it first.

### They restored but it's still broken

Usually one of:

- **They copied the broken version over the good one** by reversing the argument order.
  `Copy-Item -Recurse SOURCE DESTINATION` — source first. If they've destroyed the good
  copy, check for an older one; campers often have several.
- **The copy they restored was never actually working.** They copied at a moment they
  assumed was good. Reinforce: run it, *then* copy.

### Copies are piling up and they can't tell them apart

Expected by mid-session. Have them name copies meaningfully — `quiz-scoring-works`, not
`quiz2`, `quiz3`, `quiz4`. Deleting old copies is fine once a newer one is confirmed
working.

### A camper is copying into the project folder instead of beside it

Produces `myproject\myproject-working\...`, which confuses both the camper and the AI —
Claude Code will read the nested copy as part of the project. Make sure they `cd
$HOME\Documents\Projects`, then `cd <Name>`, so copies sit *next to* the project, not
inside it.

Worth showing on the projector once. It's the mistake that generates the weirdest
downstream symptoms.

---

## Classroom Problems

### One camper is way ahead

Never "add more features." Instead:

- "Try to break it. Empty input, wrong type, click everything twice."
- "Ask the AI to explain the part of the code you understand least, then explain it to
  me."
- "Go help someone who's stuck." (Best option. Teaching is how they consolidate.)
- "Write a README so someone else could run it."

### A camper wants to use a language other than Python

Allowed — if they already know it. Say yes and set two conditions:

1. **It has to run on this laptop with no installs.** Web (HTML/CSS/JS in a browser) is
   the easy yes. Anything needing a toolchain, SDK, or account is a no today.
2. **They're on their own for language-specific bugs.** You're supporting 25 campers in
   Python. Be upfront and friendly about it.

Everything you're teaching still applies unchanged — prompt sizing, the four checks,
scope cutting, commits. Only the example code differs. A camper building in JS is
getting the same curriculum.

Watch for the camper who picks an unfamiliar language *because* it sounds impressive.
Ask: "have you written this before?" If no, steer to Python for today.

### One camper is way behind

- Cut scope immediately and visibly. A working small thing beats a broken big thing.
- Pair them with someone who has a working app.
- Hand them a known-good prompt from the idea bank and let them start over. Restarting is
  cheap and they need a win.

### A camper is just accepting everything without reading

The failure mode this whole curriculum exists to prevent. Interrupt with:

> "Show me what it just changed. What does this part do?"

If they can't answer, that's the teaching moment. Rule 4 exists for exactly this: *you
have to be able to explain what your app does.*

### A camper is frustrated and shutting down

- Get them to a working state first — restore a folder copy, or start fresh. Do not debug
  with them while they're frustrated.
- Take the smallest possible next step. Any win.
- Name it honestly: "This is what it's actually like. Every professional has days like
  this."

### The whole room is stuck on the same thing

Stop everything and demo the fix on the projector. Ten minutes of your time beats
twenty-five campers burning ten minutes each.

### Campers racing to add features without testing

Halt the room. Pick a camper's app, put it on the projector, and break it in 30 seconds
with empty input. This costs five minutes and resets the room's behavior for the rest of
the day.

---

## If The Network Or API Is Down

Have this ready. It's a real risk and it will happen at least once.

**Analog activities that still teach the actual skills:**

- **Prompt lab** — the bad prompts from Session 2 (six for HS, three for MS). Works
  entirely on paper.
- **Spec sheets** — write specs and tests for the next project.
- **Bug report drill** — instructor describes a broken app verbally; campers write a
  proper what-I-did / what-I-expected / what-happened report.
- **Break the plan** — put an AI-generated project plan on the projector and have the
  room find three things wrong with it.
- **Read the code** — put a real code sample up and find the bugs. The empty-list average
  and the case-sensitive quiz checker both work great.
- **Paper demos** — sketch the app you'd build, pitch it to a partner, get scope-cut.

None of this is filler. Verification and scoping are the parts campers are worst at, and
they don't need a computer.
