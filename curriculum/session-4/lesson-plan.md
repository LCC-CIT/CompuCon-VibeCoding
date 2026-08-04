# Session 4 — Make It Yours / Demo Day

**The two age groups are doing completely different things today.**

- **MS (85 min): *Make It Yours.*** A capstone built from scratch and demoed, all in one
  session. This is MS's first and only self-directed project.
- **HS (60 min): *Demo Day.*** No build time at all. The capstone was finished in
  Session 3. Today is demos, reflection, and where-to-next.

Read your age group's section.

---

## Timing

### Middle school — 85 min

| Time | Block | Mode |
|---|---|---|
| 0:00–0:12 | Pitch + scope check | Pairs → instructor |
| 0:12–0:50 | Build block | Independent |
| 0:50–1:00 | Polish + demo prep | Independent |
| 1:00–1:20 | Showcase | Everyone |
| 1:20–1:25 | Where this goes next | Wrap |

> **No break scheduled.** If your group needs one, take 5 at 0:50 and cut the build to
> 33 minutes.

### High school — 60 min

| Time | Block | Mode |
|---|---|---|
| 0:00–0:10 | Setup + last demo rehearsal | Independent |
| 0:10–0:40 | Showcase | Everyone |
| 0:40–0:52 | What you actually learned | Whole group |
| 0:52–1:00 | Where this goes next | Wrap |

---

# MIDDLE SCHOOL — Make It Yours (85 min)

38 minutes of build time. That is not much, and the scope check at the start is what
makes it work. Be ruthless there and the session lands; be generous and half the room
demos something broken.

---

## 0:00 — Pitch + Scope Check (12 min)

### Pitch to a partner (5 min)

Each student gets ~2 minutes to pitch:

```
I'm building ______.

You use it to ______.

The two things it has to do:
  1.
  2.

I'll know it works when:
  - If I ______, it ______
```

**Two must-haves, not three.** MS has 38 minutes of build time.

Partner asks one question:

> **"Could you cut one of the two and still have something cool?"**

### Instructor scope check (7 min)

Every student gets a ~15-second sign-off. You are looking for one thing:

> **Can this be built in 38 minutes by someone who has been doing this for three
> sessions?**

Default to **yes** on anything from the Starter tier of
[`project-ideas.md`](../project-ideas.md), and **cut hard** on anything else.

| They pitched | Cut it to |
|---|---|
| A whole game with levels | One screen, one goal, one way to win |
| Something that saves data | Skip saving. Make it work first. |
| Multiplayer anything | Two players, same keyboard, taking turns |
| "Like Minecraft but…" | Pick the one thing about it they like. Build that. |
| An app with menus and screens | One screen. |

Say the reasoning out loud:

> "Cutting is the actual skill. A small thing that works beats a big thing that doesn't
> — today, and forever, in every job you will ever have."

**A completely fine MS capstone:** "the app I built in Session 1, rebuilt better, with
the two features I wanted but didn't have time for." Pre-approve this for anyone
struggling to choose. Ownership matters more than novelty.

---

## 0:12 — Build Block (38 min)

### First 5 minutes, no code

```powershell
cd $HOME\Documents
mkdir capstone
cd capstone
cc-ds
```

1. Write the first prompt on paper — the whole app, answering the four questions
2. Get it checked by the instructor or a partner
3. *Then* type it in

The paper step feels slow and saves ten minutes of thrash.

### Then: build, run, check, copy

Post it. Say it every ten minutes.

```powershell
cd $HOME\Documents
Copy-Item -Recurse capstone capstone-working
```

### Timed callouts

- **At 0:30 (18 min in):** "You should have something running by now. Not finished —
  running. If you don't, come see me."
- **12 min left:** "Last new thing starts now or not at all."
- **6 min left:** "No new features. Make what you have work properly."
- **3 min left:** "Copy your working folder. Right now, whatever state it's in."

Walk the room enforcing the last one.

### The halftime rule

Not having a running app at the 18-minute mark is the single best early warning signal
you have. Catch those students there, not at 0:50.

### Instructor circulation, in priority order

1. **Anyone with nothing running.** Get them to a working something, however small.
2. **Anyone who hasn't copied their folder in 15 minutes.**
3. **Anyone quietly stuck.** The frustrated ones raise their hands; the quiet ones don't.
4. **Anyone cruising.** "Try to break it. What happens if you leave it empty?"

---

## 0:50 — Polish + Demo Prep (10 min)

### Five minutes of polish

Cosmetics only. Window title, colors, a friendlier message. **No new logic.**

### Five minutes of demo prep

Plan 45 seconds:

```
1. What it is, in one sentence.
2. Show it working. (Practice the exact clicks. Twice.)
3. One thing that broke and how you fixed it.
```

**Practice the clicks.** The most common demo failure is a student clicking around live,
hitting a bug they've never hit before, and freezing.

---

## 1:00 — Showcase (20 min)

45 seconds each, hard limit, visible timer.

**Rules for the room:**

- Everyone watches
- Applause for every single demo, no exceptions
- One compliment per demo from the audience

**Instructor:** for each demo, name one specific thing that student did well. Not "great
job" — "you caught that the score could go negative," "you tested that before you showed
it." Specific praise for the *process*, not the output. It teaches everyone watching what
to value.

Item 3 is required. If a student skips it, ask: *"What broke?"* Never let a demo look
effortless — that's how you get a room full of kids who think they're the only one who
struggled.

> If the group is large or shy, run a **gallery walk** for the first 10 minutes —
> everyone leaves their app running and circulates — then have 6–8 volunteers present to
> the whole room.

---

## 1:20 — Where This Goes Next (5 min)

### What they actually learned

Say these out loud. They'll undersell it to themselves otherwise.

- How to describe something you want precisely enough that it can be built
- How to tell whether something is right, not just whether it ran
- How to say exactly what went wrong
- How to save your work so a mistake is never fatal
- How to cut an idea down to something you can actually finish

> "Almost none of that is about Python. All of it will still be true in twenty years."

### The honest part

> "The AI wrote the code. That's real work you did — you decided what to build, you found
> what was wrong, you fixed it. And if you want to get properly good at this, the next
> step is reading the code and figuring out what each part does."

### Last thing

> "You built three things that didn't exist before you got here. Go build a fourth."

Make sure everyone gets their project off the machine — USB, email, or shared folder.

---

# HIGH SCHOOL — Demo Day (60 min)

**No build time.** The capstone was finished in Session 3. Anyone who shows up expecting
to code today was told twice last session that this wasn't happening — hold the line, or
demos run over and the wrap-up gets cut, which is the part that actually sticks.

The one exception: the 10-minute setup block exists so a student whose app won't launch
can restore their `capstone-demo` copy. That's recovery, not building.

---

## 0:00 — Setup + Last Rehearsal (10 min)

Everyone gets their app running and rehearses the demo path twice.

```powershell
cd $HOME\Documents
cd capstone
python main.py
```

**If it doesn't run:** restore the demo copy made at the end of Session 3.

```powershell
cd $HOME\Documents
Remove-Item -Recurse capstone
Copy-Item -Recurse capstone-demo capstone
```

This is the payoff for the save-point discipline. Point it out when it saves someone —
it will save someone.

Instructor: circulate and find the students whose app *doesn't* run. Those are the only
people who need you in this block. Get them to a working version even if it's an older
one with fewer features.

Rehearsal, twice through:

1. The exact clicks of the demo path
2. The one sentence that opens it

---

## 0:10 — Showcase (30 min)

90 seconds each, hard limit, visible timer. With ~20 students that's tight — keep it
moving and don't let questions expand.

**Format — five things:**

```
1. What it is, in one sentence.
2. Show it working.
3. One thing that broke and how you fixed it.
4. One thing the AI got wrong that you caught.
5. What you'd add next.
```

Items 3 and 4 are **required**. If a student skips them, ask: *"What broke?"* and
*"What did the AI get wrong?"* Never let a demo look effortless.

Item 4 is the one that matters most. It's the entire track compressed into one sentence
per student, and hearing twenty of them back to back makes the point better than any
lecture could.

**Rules for the room:**

- Everyone watches
- Applause for every demo, no exceptions
- One question or compliment per demo — encourage technical ones: *"why did you split it
  that way?"*, *"what happens if I put a negative number in?"*

**Instructor:** for each demo, name one specific thing that student did well. Process,
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

- Get your project off this machine — USB, email, or shared folder. Do it now, in this
  block, not later.
- Claude Code is free to install, and there are free model options
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

**Both groups:**

- [ ] **Print camper notes** for the right age group, one per camper. Session 4's notes
      end with take-home guidance, so campers should leave with them.

**MS:**

- [ ] Scope-cut table printed for the pitch block
- [ ] Pre-approve "rebuild my Session 1 app, better" for anyone who can't choose
- [ ] Visible countdown timer for the showcase
- [ ] Plan for getting projects off the machines — USB, email, or shared folder

**HS:**

- [ ] Visible countdown timer — 60 minutes with ~20 demos has no slack
- [ ] Know every student's project going in, so you can name something specific per demo
- [ ] Be ready to restore `capstone-demo` copies in the setup block
- [ ] Decide your cut order in advance if demos run long (item 5, then item 1 — never 3
      or 4)
- [ ] Write down the reflection answers; they're your notes for next year
- [ ] Certificates or something to hand out, if CompuCon does that
