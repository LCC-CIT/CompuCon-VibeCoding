# Session 4 — Demo Day

**High school only.** Middle school is a single 85-minute session — Session 1 — and ends
there.

Sixty minutes, no build time at all. The capstone was finished in Session 3. Today is
demos, reflection, and where-to-next.

---

## Contents

- [Timing — 60 min](#timing-60-min)
- [0:00 — Setup + Last Rehearsal (10 min)](#000-setup-last-rehearsal-10-min)
- [0:10 — Showcase (30 min)](#010-showcase-30-min)
- [0:40 — What You Actually Learned (12 min)](#040-what-you-actually-learned-12-min)
  - [The honest part](#the-honest-part)
  - [One round of reflection (5 min)](#one-round-of-reflection-5-min)
- [0:52 — Where This Goes Next (8 min)](#052-where-this-goes-next-8-min)
  - [Last thing](#last-thing)
- [Instructor Prep Checklist](#instructor-prep-checklist)

## Timing — 60 min

| Time | Block | Mode |
|---|---|---|
| 0:00–0:10 | Setup + last demo rehearsal | Independent |
| 0:10–0:40 | Showcase | Everyone |
| 0:40–0:52 | What you actually learned | Whole group |
| 0:52–1:00 | Where this goes next | Wrap |

---

**No build time.** The capstone was finished in Session 3. Anyone who shows up expecting
to code today was told twice last session that this wasn't happening — hold the line, or
demos run over and the wrap-up gets cut, which is the part that actually sticks.

The one exception: the 10-minute setup block exists so a camper whose app won't launch
can restore their `capstone-demo` copy. That's recovery, not building.

---

## 0:00 — Setup + Last Rehearsal (10 min)

Everyone gets their app running and rehearses the demo path twice.

```powershell
cd $HOME\Documents\Projects
cd <Name>
cd capstone
python main.py
```

**If it doesn't run:** restore the demo copy made at the end of Session 3.

```powershell
cd $HOME\Documents\Projects
cd <Name>
Remove-Item -Recurse capstone
Copy-Item -Recurse capstone-demo capstone
```

This is the payoff for the save-point discipline. Point it out when it saves someone —
it will save someone.

Instructor: circulate and find the campers whose app *doesn't* run. Those are the only
people who need you in this block. Get them to a working version even if it's an older
one with fewer features.

Rehearsal, twice through:

1. The exact clicks of the demo path
2. The one sentence that opens it

---

## 0:10 — Showcase (30 min)

90 seconds each, hard limit, visible timer. With ~20 campers that's tight — keep it
moving and don't let questions expand.

**Format — five things:**

```
1. What it is, in one sentence.
2. Show it working.
3. One thing that broke and how you fixed it.
4. One thing the AI got wrong that you caught.
5. What you'd add next.
```

Items 3 and 4 are **required**. If a camper skips them, ask: *"What broke?"* and
*"What did the AI get wrong?"* Never let a demo look effortless.

Item 4 is the one that matters most. It's the entire track compressed into one sentence
per camper, and hearing twenty of them back to back makes the point better than any
lecture could.

**Rules for the room:**

- Everyone watches
- Applause for every demo, no exceptions
- One question or compliment per demo — encourage technical ones: *"why did you split it
  that way?"*, *"what happens if I put a negative number in?"*

**Instructor:** for each demo, name one specific thing that camper did well. Process,
not output — "you split that into three files and it made your bug obvious," "you caught
that before it bit you." You know each project from Session 3; use that.

**If you're running behind:** cut item 5 first, then item 1. Never cut 3 or 4.

---

## 0:40 — What You Actually Learned (12 min)

Go through these out loud. They'll undersell it to themselves otherwise.

- How to describe a thing you want precisely enough that it can be built
- How to break a big idea into pieces small enough to check
- How to tell whether something is right, not just whether it runs
- How to report a bug well
- How to plan before building, and how to cut scope when you have to
- How to use save points so mistakes aren't fatal
- How to split a project so you can find things — and so the AI works better

> "Notice that almost none of that is about Python, and every one of them will still be
> true in twenty years, whatever tools exist by then."

### The honest part

Say this plainly. It's the most important 90 seconds of the session.

> "The AI wrote most of the code you shipped this week. That's a real thing you did — you
> decided what to build, you caught what was wrong, you steered it. But if I sat you down
> with a blank file and no AI, most of you couldn't write these apps yet.
>
> That's fine. That's where you are, after four sessions. The thing I want you to know is
> which gap is which. The people who get really good at this are the ones who can *also*
> read the code — because they catch what the AI gets wrong, and they know when it's
> giving them a bad answer confidently."

### One round of reflection (5 min)

Go around the room. One sentence each:

> **"The thing I'll actually use again is ___."**

Fast, no discussion. It surfaces what landed, which is genuinely useful feedback for the
next time you run this track — write down what you hear.

---

## 0:52 — Where This Goes Next (8 min)

**Keep going with what you have:**

- Get your project into your Google Drive folder — link in the camper notes. Do it now,
  in this block, not later.
- Add one feature a week to the thing you built

**Learn what's underneath:**

- Open your own code and ask the AI to explain it, function by function
- Try writing one small function yourself first, then ask the AI to review it
- Python basics: variables, loops, functions, lists. That's most of what your app uses.

**Build for someone else:**

- Best possible next project: ask a family member what would make something easier for
  them, then build that. Real users find real bugs.

### Last thing

> "You built something this week that didn't exist before you sat down. Whatever you do
> next — that's what it feels like. Go do it again."

---

## Instructor Prep Checklist

- [ ] **Print camper notes**, one per camper. Session 4's notes end with take-home
      guidance, so campers should leave with them.
- [ ] Confirm the `Documents\Projects` folder exists on every lab machine
- [ ] Confirm every camper has a folder with their name in the HS Google Drive folder
- [ ] Visible countdown timer — 60 minutes with ~20 demos has no slack
- [ ] Know every camper's project going in, so you can name something specific per demo
- [ ] Be ready to restore `capstone-demo` copies in the setup block
- [ ] Decide your cut order in advance if demos run long (item 5, then item 1 — never 3
      or 4)
- [ ] Write down the reflection answers; they're your notes for next year
- [ ] Certificates or something to hand out, if CompuCon does that

------

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/) This Vibe Coding Curriculum by [Brian Bird](https://profbird.dev), created in <time>2026</time> with AI assistance, is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
