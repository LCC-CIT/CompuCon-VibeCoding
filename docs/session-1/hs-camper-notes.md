# Session 1 — Make Something Work

### Vibe Coding · High School · Keep this with you

---

## What you're doing today

Building a real, working application — with a window, buttons, the whole thing — in about
two hours, without typing the code yourself.

You'll describe what you want to an AI. It writes the code. You run it, judge whether
it's actually right, and tell it what to change. Then you do that again, and again.

The skill being taught isn't syntax. It's **knowing what to ask for, how much to ask for
at once, and how to tell whether you got it.** That skill transfers to every tool that
comes after this one.

**By the end of today you'll have an app you built and can demo.**

---

## Today's plan

| | Block |
|---|---|
| **1** | Instructor builds an app live, in about 5 minutes |
| **2** | What just happened — how the AI actually works |
| **3** | Everyone builds the same thing: a Mad Libs generator |
| **4** | The three moves: **Ask**, **Run**, **Fix** |
| **5** | Build your own app, your choice |
| **6** | "The AI was wrong" — finding code that runs and is still broken |
| **7** | Showcase |

---

## Getting started

Open **PowerShell** (through Windows Terminal). One command per line:

```powershell
cd $HOME\Documents\Projects
mkdir <Name>
cd <Name>
mkdir madlibs
cd madlibs
claude
```

Put your name where it says `<Name>` — one word, like `maya`, so it works in the
commands. Your name folder is where all your projects live. `claude` launches
**Claude Code**.

**Exit:** `Ctrl+C` · **Restart:** `claude`

**Run your app** (in PowerShell, not inside the AI):

```powershell
python story.py
```

### One command per line

Lab machines run either PowerShell 5.1 or 7. 5.1 doesn't support `&&` for chaining, and
you can't tell which version you're on. Write everything one per line and it works either
way.

---

## What you're actually working with

`claude` starts an AI that can **read and write files in the folder you started it in**,
and run commands. That folder is its entire world — which is why you always start it
inside your project folder, not in the Projects folder.

### Two things worth understanding

**The tool and the model are separate.** Claude Code is the interface — the thing that
reads your files and edits them. The model is the intelligence behind it. Most AI
products are assembled this way, and knowing that makes the whole landscape less
mysterious.

**The model is a very fast, very well-read guesser.** It predicts what code should come
next based on an enormous amount of code it has read. It is not reasoning about your
project. It doesn't know your intent unless you stated it.

> Genius intern, first day. Extremely fast, knows every library, no idea what you actually
> want, and will never tell you it's confused.

**The consequence:** it will confidently produce code that runs perfectly and is wrong.
Nothing on your computer will flag that. Catching it is the human's job — and it's the
actual subject of this course.

---

## Writing a prompt that works

Answer four questions:

| Question | Weak | Strong |
|---|---|---|
| **What kind of thing?** | "make a timer" | "a Python tkinter app" |
| **What does it do?** | "counts down" | "counts down from 25 min, beeps at zero" |
| **What does it look like?** | *(nothing)* | "big digits, Start and Reset buttons" |
| **Where does it go?** | *(nothing)* | "save it as `timer.py`" |

Today's shared prompt, which answers all four:

```
Build a Mad Libs generator in Python with a tkinter window.
Ask the user for 5 words: a noun, a verb, an adjective, a place, and a food.
Each one gets its own text box with a label.
When they click a "Make Story" button, show a funny story using their words.
Save it as story.py
```

Note what's absent: any instruction about *how* to write the code. Architecture, loops,
function names — none of it. Specify what you care about; let the AI decide the rest.
Every implementation detail you specify is a decision you now own.

---

## How much to ask for at once

> ## Starting from nothing → describe the whole app.
> ## Changing something that works → one thing at a time.

The reason isn't caution, it's **speed**:

```
5 changes → run → broken → which one? could be any. could be two interacting.
                            you're debugging blind.

1 change  → run → broken → it's that one. fix it in 30 seconds.
```

Every batch of untested changes is a debugging session you're saving up for later, with
interest.

**Size test:** can you say what should be different in one sentence? Yes → good size.
No → break it up.

---

## The loop

> ### Ask small → Run it → Say exactly what went wrong → Repeat

---

## Running and reading the result

Three outcomes:

1. **It works** → next change
2. **It crashes** → copy the *entire* error, paste it to the AI. Not just the last line —
   the whole stack trace tells it where to look.
3. **It runs and does the wrong thing** → the dangerous one

Outcome 3 is where you matter. The computer cannot tell you your quiz scored 3/5 when it
should have been 4/5, or that your timer counts up. It has no idea what you intended.

### Reporting a bug

- ❌ "it's broken" — useless
- ⚠️ "the button doesn't work" — better, still vague
- ✅ "When I click Make Story, nothing happens. No error in the terminal. The window just
  sits there."

> **What you did · What you expected · What actually happened**

This is how you report a bug to any engineer anywhere. Learning to write it well is worth
more than anything else on this page — and a well-written bug report turns out to be a
well-written prompt, which is not a coincidence.

---

## Useful things to say to the AI

```
Explain what this function does in plain English.

What could go wrong with this? What inputs would break it?

What did you just change? List every change.

I expected X but got Y. Why?

Is there a simpler way to do this?
```

That third one matters more than it looks. The AI sometimes changes things you didn't ask
about — you request a color change and it also "helpfully" rewrites your scoring logic.
Ask what changed, then check the answer against what you actually asked for.

---

## Try to break it

Late in the session, everyone attacks their own app:

- [ ] Empty input in every field
- [ ] Wrong type — text where a number goes, and vice versa
- [ ] Extreme values — 0, negatives, 999999, a paragraph of text
- [ ] Every button clicked twice, fast, and out of order
- [ ] Window resized to nothing

This is where AI-written code fails most often, because the AI optimizes for the case you
described and ignores the ones you didn't.

Consider this example — real output for "make a quiz app that shows my score":

```python
score = 0
for question in questions:
    answer = input(question["text"] + " ")
    if answer == question["correct"]:
        score += 1
print(f"That's {score / len(questions) * 100}%!")
```

Runs perfectly. Three bugs: answers are case-sensitive (type "paris", get marked wrong),
leading spaces break it, and the percentage prints as `33.33333333333333%`. None of it
crashes. All of it is wrong.

> The AI didn't make a mistake. It answered exactly what was asked. The *question* was
> incomplete.

The way you'd catch this without being told: **test with wrong input on purpose.**

---

## When you're stuck

1. **Describe the bug out loud** to a person — you'll often solve it mid-sentence
2. **Report it properly** to the AI (what you did / expected / got)
3. **Delete the file and regenerate** with a better description. Restarting is cheap.
4. **Ask an instructor.** Ten minutes stuck is the limit.

---

## The showcase

90 seconds. Three things:

1. **Show it running** — don't describe it, demo it
2. **One thing that broke** and how you fixed it
3. **One thing you'd add** with more time

Number 2 is required. Everyone's app broke today; making that public is the point.

---

## Before you go

Get your file off this machine. Save a copy to your Google Drive folder:

1. Open the [Google Drive link](https://drive.google.com/drive/folders/1iNAG8vacKNsL3-c_1e_363R00ZxjgJPM?usp=drive_link)
2. Find the folder with your name
3. Copy your app file into it

**And the honest version of what happened today:** the AI wrote the code. What you did —
deciding what to build, catching what was wrong, steering it — is real work, and it's
most of what senior engineers actually spend their time on. But you don't yet know how
that code works.

That's fine for day one. The thing worth knowing is which gap is which. The people who
get genuinely good at this are the ones who can *also* read the code, because they catch
what the AI gets wrong and they know when it's being confidently useless.

Start here, on your own project:

```
Explain what the function on line 40 does, like I'm 12.
```

It's very good at that, and it's the fastest way to actually learn to code while you
build.
