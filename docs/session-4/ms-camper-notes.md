# Session 4 — Make It Yours

### Vibe Coding · Middle School · Keep this with you

---

## What you're doing today

**Your project. Your idea. Start to finish, today.**

Then you demo it to everyone.

This is the only session where you pick what to build with no restrictions from us — so
pick something you actually want to exist.

---

## Today's plan

| | What we're doing |
|---|---|
| **1** | Pitch your idea to a partner, then get it approved |
| **2** | Build it |
| **3** | Polish and practice your demo |
| **4** | Showcase — everybody shows what they made |
| **5** | Where to go from here |

---

## The most important thing on this page

You have about **38 minutes** to build.

That is not much time. It's enough to build something genuinely cool — as long as you pick
something small.

> ## A small thing that works beats a big thing that doesn't.
> Every time. Forever. In every job you will ever have.

**Two must-haves. That's the limit.** Not three. Two.

---

## Your pitch

Fill this in, then pitch it to a partner:

```
I'm building ________________________________

You use it to _______________________________

The TWO things it has to do:
  1. ______________________________________
  2. ______________________________________

I'll know it works when:
  If I ____________, it should ____________
```

Your partner asks you one question:

> **"Could you cut one of the two and still have something cool?"**

Then an instructor approves it. We might make you cut something. That's not us being
mean — it's the single most useful thing we can do for you right now.

### Ideas that are the right size

Mad Libs · dice roller · Magic 8-Ball · coin flip counter · compliment generator · random
team picker · color picker · countdown timer · rock paper scissors · unit converter ·
quiz with 5 questions · simple to-do list

### Ideas we'll ask you to shrink

| If you pitch | Build this instead |
|---|---|
| A game with levels | One screen, one goal, one way to win |
| Something that saves your data | Skip saving. Make it work first. |
| Multiplayer anything | Two players, same keyboard, taking turns |
| "Like Minecraft but…" | Pick the ONE thing you like about it |
| An app with menus and screens | One screen |

### Totally allowed

> **"The app I made in Session 1, rebuilt better, with the stuff I wanted but didn't have
> time for."**

That's a great capstone. Don't feel like you need a brand new idea.

---

## Getting set up

```powershell
cd $HOME\Documents\Projects
mkdir capstone
cd capstone
cc-ds
```

(`cc` instead of `cc-ds` if you have your own Claude Pro account. One command per line,
no `&&`.)

### Spend the first 5 minutes NOT coding

1. Write your first prompt **on paper** — the whole app, answering the four questions
2. Get a partner or instructor to check it
3. *Then* type it in

Feels slow. Saves you ten minutes of going in circles.

Remember the four questions:

| | |
|---|---|
| **What kind of thing?** | "a Python app with a window" |
| **What does it do?** | (your two must-haves) |
| **What does it look like?** | buttons, boxes, colors |
| **Where does it go?** | "save it as `app.py`" |

---

## While you build

> ## build → run → check → copy

**Run it:**

```powershell
python app.py
```

**Copy it every time it works:**

```powershell
cd $HOME\Documents\Projects
Copy-Item -Recurse capstone capstone-working
```

**Go back if you break it:**

```powershell
cd $HOME\Documents\Projects
Remove-Item -Recurse capstone
Copy-Item -Recurse capstone-working capstone
```

### Watch the clock

- **Halfway (about 18 min in):** you should have *something running*. Not finished —
  running. If you don't, get an instructor right now.
- **12 minutes left:** last new thing starts now or not at all
- **6 minutes left:** stop adding. Make what you have work properly.
- **3 minutes left:** copy your working folder, whatever state it's in

### If you get stuck

1. Say the problem out loud to a person
2. Tell the AI: what you did, what you expected, what happened
3. Restore your copy and try a smaller step
4. Ask an instructor — after 10 minutes, always

---

## Polish and demo prep

### Polish (5 min) — looks only, no new features

Window title · colors · fonts · a nicer message when something goes wrong

### Demo prep (5 min)

You get **45 seconds**. Plan three things:

```
1. What it is, in one sentence.
2. Show it working.
3. One thing that broke and how you fixed it.
```

**Practice the exact clicks. Twice.**

The most common demo disaster is clicking around live, hitting a bug you've never seen
before, and freezing up. Rehearsing fixes it.

If it crashes in front of everyone: say what it's supposed to do and keep going. It
happens to everybody.

---

## The showcase

45 seconds each. Everybody watches. Everybody claps for everybody.

**Number 3 in your demo is required** — the thing that broke. If you skip it we'll ask.

> Nobody in this room got it right the first time. Not one person. Saying that out loud
> is the whole point.

---

## What you actually learned this week

Not just "how to use an AI." You learned:

- How to **describe** something you want clearly enough that it can be built
- How to tell whether something is **right**, not just whether it ran
- How to say **exactly** what went wrong
- How to **save your work** so a mistake is never fatal
- How to **cut an idea down** to something you can actually finish

> Almost none of that is about Python. All of it will still be true in twenty years.

---

## Honestly, though

The AI wrote the code.

What you did was decide what to build, find what was wrong, and fix it. That's real — it's
most of what the job actually is.

But you don't know how the code works yet, and that's worth knowing about yourself.

**If you want to get properly good at this,** the next step is opening your own code and
asking:

```
Explain what this part does, like I'm 12.
```

Do that a few times and you'll start actually reading code. The people who can do
both — steer the AI *and* read what it wrote — are going to be unbelievably good at this.

---

## Take your stuff home

**Do this before you leave.** Ask an instructor to help you email your project to yourself
or put it on a USB stick.

Claude Code is free to install at home, and there are free models you can use with it.

### What to build next

Best idea we've got: **ask someone in your family what would make something easier for
them, and build that.** Real people find real bugs, and it's a lot more fun than building
for yourself.

> You built three things that didn't exist before you got here. Go build a fourth.
