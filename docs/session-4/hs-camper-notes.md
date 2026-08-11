# Session 4 — Demo Day

## Contents

- [Vibe Coding · High School · Keep this with you](#vibe-coding-high-school-keep-this-with-you)
- [What today is](#what-today-is)
- [Today's plan](#todays-plan)
- [Setup](#setup)
  - [If it doesn't run](#if-it-doesnt-run)
  - [Rehearse twice](#rehearse-twice)
- [Your demo — 90 seconds](#your-demo-90-seconds)
  - [If it crashes in front of everyone](#if-it-crashes-in-front-of-everyone)
  - [While others demo](#while-others-demo)
- [What you actually learned](#what-you-actually-learned)
- [The honest part](#the-honest-part)
- [Where to go next](#where-to-go-next)
  - [Keep what you've got](#keep-what-youve-got)
  - [Learn what's underneath](#learn-whats-underneath)
  - [Build for somebody else](#build-for-somebody-else)
- [The commands, one last time](#the-commands-one-last-time)
- [The whole course, in four lines](#the-whole-course-in-four-lines)

### Vibe Coding · High School · Keep this with you

---

## What today is

**60 minutes. Demos and wrap-up. No build time.**

Your capstone was finished last session. Today you show it, you hear what everyone else
made, and we talk about where this goes next.

The only coding that happens today is if your app won't launch and you need to restore a
working copy.

---

## Today's plan

| | Block | Time |
|---|---|---|
| **1** | Setup + last rehearsal | 10 min |
| **2** | Showcase — everyone demos | 30 min |
| **3** | What you actually learned | 12 min |
| **4** | Where this goes next | 8 min |

---

## Setup

Get your app running:

```powershell
cd $HOME\Documents\Projects
cd <Name>
cd capstone
python main.py
```

`<Name>` is your name — the folder you made in Session 1.

### If it doesn't run

Restore the demo copy you made at the end of last session:

```powershell
cd $HOME\Documents\Projects
cd <Name>
Remove-Item -Recurse capstone
Copy-Item -Recurse capstone-demo capstone
```

This is the payoff for all that copying. If it saves you today, that's not luck — that's a
habit you built on purpose.

**"Being used by another process"?** Your app is still running or the AI is open in that
folder. Close the window, `Ctrl+C`, retry.

### Rehearse twice

1. The exact clicks of your demo path
2. The one sentence that opens it

Do it twice. Not once.

---

## Your demo — 90 seconds

```
1. What it is, in one sentence.

2. Show it working.

3. One thing that broke and how you fixed it.

4. One thing the AI got wrong that you caught.

5. What you'd add next.
```

**Items 3 and 4 are required.** If you skip them, we'll ask.

Item 4 is the one that matters most. It's this entire course compressed into one sentence
per person — and hearing twenty of them in a row makes the point better than any lecture
could.

### If it crashes in front of everyone

Say what it's supposed to do and keep going. Every person in this room has had code break
on them this week.

### While others demo

Watch. Applaud — everyone, no exceptions. Ask one question or give one compliment.

Good questions to ask:

- "Why did you split it that way?"
- "What happens if I put a negative number in?"
- "What was the hardest part?"

---

## What you actually learned

Worth saying out loud, because you'll undersell it to yourself:

- How to **describe** something precisely enough that it can be built
- How to **break a big idea** into pieces small enough to check
- How to tell whether something is **right**, not just whether it runs
- How to **report a bug** properly
- How to **plan** before building, and **cut scope** when you have to
- How to use **save points** so mistakes aren't fatal
- How to **split a project** so you can find things — and so the AI works better

> Notice that almost none of that is about Python, and every one of them will still be
> true in twenty years, whatever tools exist by then.

---

## The honest part

The AI wrote most of the code you shipped this week.

What you did — deciding what to build, catching what was wrong, steering it — is real
work, and it's genuinely most of what senior engineers spend their time on.

But if you sat down with a blank file and no AI, most of you couldn't write these apps
yet.

**That's fine. That's where you are after four sessions.** The thing worth knowing is
which gap is which.

> The people who get really good at this are the ones who can *also* read the code.
> Because they catch what the AI gets wrong, and they know when it's giving them a bad
> answer confidently.

---

## Where to go next

### Keep what you've got

- **Get your project off this machine today** — save a copy to your Google Drive folder:
  open the [Google Drive link](https://drive.google.com/drive/folders/1iNAG8vacKNsL3-c_1e_363R00ZxjgJPM?usp=drive_link),
  find the folder with your name, and copy your project folder into it. Do it in the last
  block, not "later."
- Add one feature a week to what you built\*

<small>\* Doing this needs your own account with an AI coding tool. Claude Code, the
tool you used in class, is a paid product. Some tools have free options to start with —
see the [OpenCode Zen how-to](../session-1/opencode-zen-howto.html).</small>

### Learn what's underneath

The fastest way to actually learn to code while you're vibe coding:

```
Explain what this function does, like I'm 12.
```

Do it function by function through your own project. Then try the reverse: **write one
small function yourself first, then ask the AI to review it.** That flips who's checking
whom, and it's where real learning happens.

What your app is probably made of, if you want a starting list: variables, loops,
functions, lists, and conditionals. That's most of it.

### Build for somebody else

Best possible next project: **ask a family member what would make something easier for
them, then build that.**

Real users find real bugs. They use your app in ways you never imagined, and they'll tell
you things about your own interface you'd never have noticed. It's also just more
satisfying than building for yourself.

---

## The commands, one last time

```powershell
cd $HOME\Documents\Projects   # go to your Projects folder
cd <Name>                     # go into your name folder
mkdir myproject               # make a project folder
cd myproject                  # go into it
claude                        # start Claude Code

python app.py                 # run your app

cd $HOME\Documents\Projects   # back to Projects
cd <Name>                     # back to your name folder
Copy-Item -Recurse myproject myproject-working    # save point
```

`Ctrl+C` to quit the AI · `/clear` to reset the conversation without touching your code

**One command per line. No `&&`.**

---

## The whole course, in four lines

> **Ask small. Run it. Say exactly what went wrong. Repeat.**
>
> **It ran ≠ it's right.**
>
> **A small thing that works beats a big thing that doesn't.**
>
> **Copy it every time it works.**

---

> "You built something this week that didn't exist before you sat down. Whatever you do
> next — that's what it feels like. Go do it again."

------

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/) This Vibe Coding Curriculum by [Brian Bird](https://profbird.dev), created in <time>2026</time> with AI assistance, is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
