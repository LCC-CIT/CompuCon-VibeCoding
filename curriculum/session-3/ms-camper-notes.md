# Session 3 — Make It Solid

### Vibe Coding · Middle School · Keep this with you

---

## What you're doing today

Not making your app **bigger**. Making it **tougher**.

By the end of today, your app should be hard to break — and when you *do* break it, you'll
know exactly how to get it back.

Three things:

1. **Save points** — so you can never lose your work
2. **What to do when the AI makes things worse** (it happens to everyone)
3. **Hardening your app** so weird input doesn't wreck it

Bring the app you built last session.

---

## Today's plan

| | What we're doing |
|---|---|
| **1** | Save points — copy the folder |
| **2** | When the AI makes it worse |
| **3** | How to actually debug something |
| **4** | Build time: make your app good |
| **5** | Show one thing you fixed |

---

## Starting up

Open **PowerShell**. Go to the project you built last session:

```powershell
cd $HOME\Documents\Projects
cd madlibs
cc-ds
```

(Use your own folder name. `cc` instead of `cc-ds` if you have a Claude Pro account.)

**Run your app:**

```powershell
python story.py
```

`Ctrl+C` quits the AI · one command per line, no `&&`

---

## Save points

### The problem

You've been building for half an hour. It works. You ask for one more feature — and now
it's broken in a way you can't undo. You ask the AI to fix it. It gets worse.

Without a save point, you start over from nothing.

### The whole system: copy the folder

**To SAVE** (do this every time your app works):

```powershell
cd $HOME\Documents\Projects
Copy-Item -Recurse madlibs madlibs-working
```

That makes a complete copy of your folder, frozen at a moment when it worked.

**To GO BACK:**

```powershell
cd $HOME\Documents\Projects
Remove-Item -Recurse madlibs
Copy-Item -Recurse madlibs-working madlibs
```

Line 2 throws away the broken version. Line 3 brings back the good one.

> **You can do exactly the same thing in File Explorer.** Right-click your project
> folder → Copy → Paste → rename the copy. Same result. Use whichever makes more sense
> to you — neither one is the "real" way.

### The rule

> ## Copy it every time it works.

Not when you're finished. **Every time it works.**

### Name your copies

Don't do this: `madlibs2`, `madlibs3`, `madlibs4`. In twenty minutes you won't know which
is which.

Do this: `madlibs-working`, `madlibs-colors-good`, `madlibs-before-sounds`.

### Two things that go wrong

**"Cannot remove item — being used by another process."** Your app is still running, or
the AI is still open in that folder. Close the app window, press `Ctrl+C` to quit the AI,
then try again.

**You copied the broken one over the good one.** The order matters:

```powershell
Copy-Item -Recurse FROM-HERE TO-HERE
```

Source first, destination second. Slow down on this one.

---

## When the AI makes it worse

Here's a thing that will happen to you, and it happens to professionals too:

You report a bug. The AI fixes it. Something *else* breaks. You report that. It fixes
that, and the first thing breaks again. Round and round.

**This is not you being bad at this.** Here's how to get out.

### Escape hatch 1: `/clear`

Type this into the AI:

```
/clear
```

This wipes the **conversation** — not your files. Your code is completely untouched.

Why it helps: the AI has built up a theory about what's wrong with your app, and the
theory is wrong. Every new thing you say gets filtered through that wrong idea. Clearing
it and describing the problem fresh often fixes it instantly.

> It's like a friend who's decided what your problem is and keeps giving you advice for
> the wrong problem. Sometimes you just start the conversation over.

### Escape hatch 2: go back to your save point

You have a copy that works. Use it. Then take a **smaller** step this time.

### Escape hatch 3: delete the file and ask again

With a better description. One file is cheap to rebuild.

### The 10-minute rule

> **Stuck on the same problem for 10 minutes? Stop.** Restore your save point and try a
> different way — or ask an instructor.

Grinding away at something that isn't working is a trap. Knowing when to back out is a
real skill.

---

## How to actually debug something

Four steps. In order. Every time.

### 1. What exactly happens?

Not "it's broken." What did you click? What did you expect? What did you get?

**Most bugs get solved right here.** Being forced to describe it precisely is often the
entire fix. Try saying it out loud to a person before you type anything.

### 2. When did it last work?

What changed since then? If more than one thing changed, that's your answer — you broke
the one-change-at-a-time rule and now you're paying for it.

### 3. Ask precisely

> When I click Make Story with all the boxes empty, the window freezes and I have to
> close it. Here's what the terminal says: [paste the whole thing]

### 4. Check the fix — AND check the old stuff still works

Run it. Then run the thing that *used* to work, and make sure it still does.

**Everybody skips step 4.** Fixing one bug by breaking something else is the oldest
mistake there is.

---

## Build time: make your app good

Three jobs, in this order.

### Job 1 — Make it unbreakable

Try every one of these on your own app. Fix what breaks. **Copy your folder after each
fix that works.**

- [ ] Leave every box empty and click the button
- [ ] Type a number where a word goes
- [ ] Type a word where a number goes
- [ ] Type something 200 characters long
- [ ] Click every button twice, fast
- [ ] Click buttons in the wrong order
- [ ] Shrink the window as small as it goes

### Job 2 — Make it look good

Colors, fonts, spacing, a window title, a friendlier message when something goes wrong.

One change at a time. Run it after each one.

### Job 3 — Understand one piece of it

Find the part of your code you understand least. Ask:

```
Explain what this part does, like I'm 12.
```

Be ready to tell the room what you found out.

---

## Show one thing you fixed

At the end, everyone shows **one bug they found and fixed**, in about 30 seconds:

1. Here's what broke it
2. Here's what it does now

> Every single person in this room found something wrong with their own app today. Not
> because you're bad at this — because *everybody's* first version has bugs. The
> difference between people who make good software and people who don't is entirely
> whether they went looking.

---

## The short version

**Save points:**
> Copy the folder every time it works. Name copies so you can tell them apart.

**When it goes wrong:**
> `/clear` · restore your copy · delete the file and start over · ask a human after 10 min

**Debugging:**
> What exactly happens? → When did it last work? → Ask precisely → Check the fix *and*
> the old stuff

---

## Next time

You pick something to build from scratch — your idea — and you demo it to everyone at the
end.

Think about two questions before then:

1. **What would you actually use?**
2. **What's the smallest version of that which is still cool?**
