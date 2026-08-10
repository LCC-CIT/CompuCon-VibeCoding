# Session 1 — Make Something Work

### Vibe Coding · Middle School · Keep this with you

---

## What you're doing today

You're going to build a real app. Not a pretend one — a program with a window and buttons
that actually runs on this computer.

You won't type the code. You'll **describe what you want** to an AI, it writes the code,
and then you test it, find what's wrong, and tell it what to fix. Over and over until
it's good.

**By the end of today you will have an app that works, that you made.**

---

## Today's plan

| | What we're doing |
|---|---|
| **1** | Watch your instructor build an app in about 5 minutes |
| **2** | Learn what just happened |
| **3** | Everybody builds the same app: a Mad Libs story maker |
| **4** | Learn the three moves: **Ask**, **Run**, **Fix** |
| **5** | Make it yours — change it however you want |
| **6** | Try to break your own app (this is the fun part) |
| **7** | Show everybody what you made |

---

## How to start

Open **PowerShell**. Type these lines **one at a time**, pressing Enter after each:

```powershell
cd $HOME\Documents\Projects
mkdir madlibs
cd madlibs
claude
```

The first three lines get you into today's project folder. `Projects` is where
all your projects live. That last one, `claude`, starts the AI.

**To quit the AI:** hold `Ctrl` and press `C`.
**To start it again:** type `claude`.

**To run your app** (do this in PowerShell, not in the AI):

```powershell
python story.py
```

---

## Type one command per line

Don't put two commands on the same line with `&&`. It doesn't work on these computers.
One line, press Enter, next line.

---

## What the AI actually is

It's a very, very fast guesser.

It has read an enormous amount of code, and it's extremely good at guessing what code
should come next. That's what it does. It is **not** thinking about your project, and it
does not know what you meant unless you said it.

> Think of it like a genius intern on their first day. Unbelievably fast, knows every
> trick — and has no idea what you actually want. It will never tell you it's confused.
> It'll just confidently hand you something wrong.

**This is the most important thing today:** the AI can write code that runs perfectly and
is still completely wrong. Your computer will never tell you the difference.

That's your job. That's why you're here and not just watching a robot.

---

## How to ask for what you want

A good ask answers **four questions**:

| Question | Example |
|---|---|
| **What kind of thing?** | "a Python app with a window" |
| **What does it do?** | "asks for 5 words, then makes a funny story" |
| **What does it look like?** | "a text box for each word, and a big button" |
| **Where does it go?** | "save it as `story.py`" |

Here's today's first prompt. Notice it answers all four:

```
Build a Mad Libs generator in Python with a tkinter window.
Ask the user for 5 words: a noun, a verb, an adjective, a place, and a food.
Each one gets its own text box with a label.
When they click a "Make Story" button, show a funny story using their words.
Save it as story.py
```

See what's **not** in there? Anything about *how* to write the code. That's the AI's job.
Yours is deciding what gets built.

---

## The one rule that matters most

> ## Ask for ONE thing at a time.

Starting a brand new app? Describe the whole thing.

Changing an app that already works? **One change. Then run it. Then the next one.**

Here's why. If you ask for five changes and something breaks, you have no idea which one
broke it. If you ask for one change and something breaks — well, it was that one.
Obviously. You fix it in ten seconds.

This isn't about being careful. It's about being **fast**.

---

## The loop

> ### Ask small → Run it → Say exactly what went wrong → Repeat

That's the whole class. Everything else is practice.

---

## When something goes wrong

Three things can happen when you run your app:

1. **It works.** Great — next change.
2. **It crashes** and the terminal fills up with red text. **Copy all of it** and paste it
   to the AI.
3. **It runs, but does the wrong thing.** This is the sneaky one. No error, no crash — it
   just does something dumb. Only *you* can catch this.

### How to report a problem

Don't say "it's broken." The AI has no idea what that means.

Say **three things**:

> **What I did:** I clicked the Make Story button
> **What I expected:** a story should show up
> **What actually happened:** nothing happened, and there's no error

That's not an AI trick. That's how you report a problem to any human being, ever. It's a
real skill and you're learning it right now.

---

## Break your own app

Near the end of class, everyone tries to break their own app on purpose. Try all of
these:

- [ ] Leave **every box empty** and click the button
- [ ] Type a **number** where a word should go
- [ ] Type something **really, really long** (like 200 characters)
- [ ] Click the button **20 times fast**
- [ ] Make the window **as small as it goes**

Found something broken? Fix it. That's your last change of the day.

> Everybody's app breaks. Everybody's. Finding it is the win.

---

## If you get stuck

Try these in order:

1. **Say the problem out loud** to a person. Seriously — you'll often figure it out
   halfway through the sentence.
2. **Tell the AI exactly what happened** using the three things above.
3. **Start the file over.** Delete it, write a better prompt, go again. This is cheap and
   totally normal.
4. **Ask an instructor.** If you've been stuck 10 minutes, just ask.

---

## Words you'll hear today

| Word | What it means |
|---|---|
| **Prompt** | What you type to tell the AI what you want |
| **Terminal / PowerShell** | The black window where you type commands |
| **Run it** | Actually starting your app to see if it works |
| **Bug** | Something wrong with your program |
| **tkinter** | The Python tool that makes windows and buttons |
| **Crash** | Your program stops and shows an error |

---

## Showing your work

At the end you'll show what you made. Two things:

1. **Run it** — don't describe it, show it working
2. **Tell us one thing that broke** and how you fixed it

Number 2 is not optional! Everybody's app broke today. Saying so out loud is the point.

---

## Taking it home

Your app is a file on this computer. Ask an instructor how to email it to yourself or put
it on a USB stick.

**One last thing, and it's honest:** the AI wrote the code. You decided what to build, you
found what was wrong, and you fixed it — that's real, and it's most of what the job
actually is. But you don't know how the code works yet.

If you want to get properly good at this, here's the next step: open your own code and
ask the AI

```
Explain what this part does, like I'm 12.
```

The people who can *both* steer the AI and read the code are going to be incredibly good
at this.
