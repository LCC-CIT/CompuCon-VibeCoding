# Session 2 — Ask Better, Check Harder

### Vibe Coding · Middle School · Keep this with you

---

## What you're doing today

Last time you learned the loop: **ask → run → fix**. Today you get good at it.

Two things:

1. **Asking better** — how much to ask for at once, and how to say it
2. **Checking harder** — how to tell if the AI actually did what you wanted

That second one is the real skill. Anybody can get an app to run. Not everybody can tell
whether it's *right*.

---

## Today's plan

| | What we're doing |
|---|---|
| **1** | Warm-up: two ways to ask for the same app |
| **2** | How much to ask for at once |
| **3** | Prompt lab — fixing bad prompts (with a partner) |
| **4** | The two checks |
| **5** | Build something new — but write the plan first |
| **6** | Swap computers and try to break your partner's app |

---

## Starting up

```powershell
cd $HOME\Documents\Projects
mkdir myproject
cd myproject
claude
```

**Run your app:**

```powershell
python app.py
```

One command per line. No `&&`.

---

## Bad prompt vs. good prompt

Same app. Which would you rather have written?

```
A:  make a study timer
```

```
C:  Build a Pomodoro timer in Python with tkinter.
    25-minute countdown, big digits, Start/Pause/Reset buttons.
    Beep when it hits zero.
    Save as pomodoro.py
```

**What's wrong with A?** The AI has to guess. It might guess a countdown of 5 minutes when
you wanted 25. It might build something with no window at all. Guessing is fine when you
don't care — it's a problem when you do.

> **Say what you care about. Let the AI figure out the rest.**

---

## How much to ask for at once

### Starting a brand new app → describe the whole thing

You want the AI to build a complete first version where all the pieces fit together. Tell
it everything.

### Changing an app that works → ONE thing at a time

The code already works. Every change might break it. Ask for one, run it, *then* ask for
the next.

### The size test

> **Can you say what should be different in one sentence?**

If yes, it's the right size. If no, break it up.

| Too big | Just right |
|---|---|
| "Add multiplayer" | "Add a second score counter that says Player 2" |
| "Make it look better" | "Make the background dark gray and the text white" |
| "Add saving" | "When I click Save, write the list to `tasks.txt`" |

---

## The two checks

After the AI changes something, **check it**. Every time.

### Check 1 — Does it do the thing?

Use your app the way it's supposed to be used. Does it give the **right** answer? Not
"an" answer — the right one.

If it's doing math, do the math yourself and compare. If it's a quiz, take the quiz and
count your score by hand.

### Check 2 — Does it survive the wrong thing?

Be a jerk to your app. On purpose.

- Leave boxes empty
- Type words where numbers go
- Type numbers where words go
- Click things twice, fast
- Type something enormous

**This is where AI code breaks most often.** The AI builds for the situation you
described. It doesn't think about the weird stuff you didn't mention.

### Here's a real example

Ask an AI for "a function that averages a list of test scores" and you'll get this:

```python
def average(scores):
    return sum(scores) / len(scores)
```

Looks right. Works fine. Now — what if the list is **empty**?

It crashes. Divide by zero.

> The AI didn't mess up. It answered exactly what you asked. *You* forgot to ask about
> the empty list.

---

## One question to memorize

After the AI makes a change, ask it:

```
What did you just change? List every change.
```

Then check that list against what you actually asked for. Sometimes it changes stuff you
never mentioned.

And when you don't understand a piece of your own code:

```
Explain what this does, like I'm 12.
```

It's really good at that.

---

## Today's build: write the plan FIRST

Before you type anything into the AI, fill this out on paper:

```
APP NAME: _______________________

WHAT IT DOES (one sentence):
_________________________________

MUST HAVE (2 things, that's the limit):
  1. _____________________________
  2. _____________________________

WHAT IT LOOKS LIKE:
_________________________________

HOW I'LL KNOW IT WORKS (2 tests):
  1. If I ____________, it should ____________
  2. If I ____________ (something WRONG), it should ____________
```

That last part is the new thing. **You're writing your tests before the app exists.**

Test 2 has to be a wrong-input test. That's the point.

Get an instructor to check your sheet before you start typing.

### While you build

- [ ] Both must-haves work
- [ ] Both of my tests pass
- [ ] I asked "what did you change?" at least once
- [ ] I tried three wrong inputs

At the end, run your own two tests and mark them honestly.

> **A failed test you can name beats a passed test you didn't really check.**

---

## Swap and break

You'll switch computers with a partner. Your job: **break their app.**

You may not look at their code. You can only use the app.

Try everything:

- [ ] Empty every box
- [ ] Wrong kind of thing in every box
- [ ] 0, negative numbers, 999999, a whole paragraph
- [ ] Click everything twice, and out of order
- [ ] Shrink the window to nothing

Write down each problem you find like this:

> **What I did:** ___
> **What I expected:** ___
> **What happened:** ___

Then swap back and fix the best bug your partner found.

> Your partner will find things in five minutes that you missed in twenty. Not because
> they're better — because you were trying to make it *work* and they were trying to make
> it *fail*. Both jobs matter. Some people get paid entirely to do the second one.

---

## If you get stuck

1. **Say the problem out loud** to a person
2. **Tell the AI** what you did, expected, and got
3. **Start the file over** with a better prompt — this is cheap and normal
4. **Ask an instructor** — after 10 minutes, always

---

## The short version

**How much to ask for:**
> New app → the whole thing. Existing app → one change at a time.
> Can't say it in one sentence? Too big.

**How to check:**
> 1. Does it do the thing — the *right* thing?
> 2. Does it survive the wrong thing?

---

## Next time

How to save your work so you can never lose it, and what to do when the AI keeps "fixing"
your app and making it worse.
