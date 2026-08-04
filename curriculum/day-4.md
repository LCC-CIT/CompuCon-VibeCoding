# Day 4 — Make It Yours

**3 hours.** Mostly build time. Students ship a project of their own choosing and demo it
to the room.

Instructor talks for about 25 minutes all day. That's the design.

---

## Session Arc

| Time | Block | Mode |
|---|---|---|
| 0:00–0:20 | Pitch + scope check | Pairs → instructor |
| 0:20–1:05 | Build block 1 | Independent |
| 1:05–1:15 | **Break** | |
| 1:15–1:25 | Mid-build reset | Whole group |
| 1:25–2:10 | Build block 2 | Independent |
| 2:10–2:25 | Polish + demo prep | Independent |
| 2:25–2:50 | Showcase | Everyone |
| 2:50–3:00 | Where this goes next | Wrap |

---

## 0:00 — Pitch + Scope Check (20 min)

### Pitch to a partner (7 min)

Each student gets 3 minutes to pitch, using this:

```
I'm building ______.

You use it to ______.

The three things it has to do:
  1.
  2.
  3.

I'll know it works when:
  - If I ______, it ______
  - If I ______ (wrong input), it ______
```

Partner's job — ask these two questions:

1. **"What happens if I do the wrong thing?"**
2. **"Could you cut one of the three and still have something cool?"**

Question 2 is the important one. Almost everyone should cut one.

### Instructor scope check (13 min)

Every student gets a 30-second sign-off. You are looking for one thing:

> **Can this be built in 90 minutes by someone who has been doing this for three days?**

Common over-scopes and the cut:

| They pitched | Cut it to |
|---|---|
| Multiplayer online game | Two players, same keyboard |
| App with user accounts and logins | One user, saves to a text file |
| Website with a database | One page, data in a JSON file |
| "A whole RPG" | One battle, three enemies |
| Machine learning something | Rules-based version of the same idea |
| Discord/Instagram bot | Same logic, local app, no API |

Say the reasoning out loud, because it's the real lesson:

> "Cutting scope isn't giving up. It's the actual skill. A small thing that works beats
> a big thing that doesn't, every single time, forever, in every job you will ever have."

**MS/HS**
> **MS:** Two must-haves, not three. Instructor should aggressively pre-approve from the
> idea bank — "build the thing you built Tuesday but better" is a completely fine
> capstone.
> **HS:** Three is fine, four if they're strong. Push for something they'd actually use.
> "Would you open this again next week?" is a good filter.

---

## 0:20 — Build Block 1 (45 min)

### First 10 minutes, no code

Everyone does these four things before writing anything:

```bash
mkdir ~/vibe/capstone && cd ~/vibe/capstone
git init
cc-ds
```

1. Ask for a plan. Argue with it. Save as `PLAN.md`.
2. Write `CLAUDE.md`.
3. First commit.
4. Then build component 1.

### Then: build, run, check, commit

The rhythm from Day 3. Post it. Say it every 15 minutes.

**Instructor circulates.** Priorities in this order:

1. **Anyone with nothing running.** Get them to a working something, however small.
2. **Anyone who hasn't committed in 20 minutes.**
3. **Anyone quietly stuck.** The frustrated ones raise their hands; the quiet ones don't.
4. **Anyone cruising.** Push them: "what would make this genuinely good?"

### The half-time rule

At the 30-minute mark, announce:

> "You should have something running by now. Not finished — running. If you don't, come
> see me."

Not having a running app at halftime of block 1 is the single best early warning signal
you have. Catch those students here, not at 2:25.

---

## 1:05 — Break (10 min)

---

## 1:15 — Mid-Build Reset (10 min)

Everyone stops. This block exists to prevent the classic disaster where four students
spend the last hour on something that was never going to work.

### Three questions, answered on paper

```
1. Is my app running right now? (yes/no)

2. Of my must-haves, which are DONE and which are NOT?

3. What is the ONE thing I need to finish in the next 45 minutes?
```

### Then, out loud

- **Not running?** Come to the front. We're getting you to working, and we're probably
  cutting something.
- **Running with everything done?** Your next 45 minutes is polish and edge cases, not
  new features. Go make it survive wrong input.
- **Running, some done?** Question 3 is your whole afternoon. Everything else is cut.

Say the thing:

> "It's 1:15. You demo at 2:25. Everyone in this room is going to cut something, and the
> people who cut it *now* are going to have better demos than the people who cut it at
> 2:20."

**MS/HS**
> **MS:** Do this at the whiteboard as a group — call each student's name, get a yes/no,
> write their one thing on the board. Public commitment works well at this age.
> **HS:** On paper, then a 60-second stand-up in fours: what's done, what's next, what
> I'm stuck on. Standard engineering ritual, and worth naming it as such.

---

## 1:25 — Build Block 2 (45 min)

Heads down. Instructor is a resource, not a lecturer.

**Timed callouts:**

- **20 min left:** "Twenty minutes. Last new feature starts *now* or not at all."
- **10 min left:** "Ten minutes. No new features. Make what you have work properly."
- **5 min left:** "Commit your working version. Right now, whatever state it's in."

That last one is non-negotiable and you should physically walk the room enforcing it.
A committed working version means nobody demos a broken app.

### For students who finish early

Not "add more features." Better options:

- Try to break it, then fix what breaks
- Make it look good — colors, spacing, fonts
- Ask: *"What's confusing about this app for someone who's never seen it?"* Fix that
- Read the code and ask the AI to explain the part you understand least
- Write a `README.md` explaining what it does and how to run it
- Help a neighbor who's stuck

---

## 2:10 — Polish + Demo Prep (15 min)

### Five minutes of polish only

Cosmetics and nothing else. Window title, colors, a friendlier message. No new logic.

### Ten minutes of demo prep

Plan the 90 seconds:

```
1. What it is, in one sentence.
2. Show it working. (Practice the exact clicks. Twice.)
3. One thing that broke and how you fixed it.
4. One thing the AI got wrong that you caught.
5. What you'd add next.
```

**Practice the clicks.** The most common demo failure is a student clicking around live,
hitting a bug they'd never hit before, and losing their nerve. Rehearsing the path twice
fixes it.

Have a fallback ready: if it crashes on stage, say what it does and keep going.

---

## 2:25 — Showcase (25 min)

90 seconds each, hard limit, visible timer.

**Rules for the room:**

- Everyone watches
- Applause for every single demo, no exceptions
- One question or one compliment per demo from the audience

**Instructor:** for each demo, name one specific thing that student did well. Not "great
job" — "you split that into three files and it made your bug obvious," "you caught that
the score could go negative." Specific praise for the *process*, not the output. It
teaches everyone watching what to value.

Items 3 and 4 in the demo format are required. If a student skips them, ask:
*"What broke?"* Never let a demo look effortless — that's how you get a room full of kids
who think they're the only one who struggled.

**MS/HS**
> **MS:** 60 seconds. Consider a gallery walk for larger groups — apps running, everyone
> circulates, then 4–5 volunteers present to the whole room.
> **HS:** 90 seconds plus one audience question. Encourage technical questions: "why did
> you split it that way?", "what happens if I put a negative number in?"

---

## 2:50 — Where This Goes Next (10 min)

### What they actually learned

Go through these out loud. They'll undersell it to themselves otherwise.

- How to describe a thing you want precisely enough that it can be built
- How to break a big idea into pieces small enough to check
- How to tell whether something is right, not just whether it runs
- How to report a bug well
- How to plan before building, and how to cut scope when you have to
- How to use save points so mistakes aren't fatal

> "Notice that almost none of that is about Python, and every one of them will still be
> true in twenty years, whatever tools exist by then."

### The honest part

Say this plainly:

> "The AI wrote most of the code you shipped this week. That's a real thing you did — you
> decided what to build, you caught what was wrong, you steered it. But if I sat you down
> with a blank file and no AI, most of you couldn't write these apps yet.
>
> That's fine. That's where you are, on day four. The thing I want you to know is which
> gap is which. The people who get really good at this are the ones who can *also* read
> the code — because they catch what the AI gets wrong, and they know when it's giving
> them a bad answer confidently."

### What to do next

**Keep going with what you have:**
- Your project is on this machine — get it on a USB stick or email it to yourself
- Claude Code is free to install; there are free model options too
- Add one feature a week to the thing you built today

**Learn what's underneath:**
- Open your own code and ask the AI to explain it, function by function
- Try writing one small function yourself first, then ask the AI to review it
- Python basics: variables, loops, functions, lists. That's most of what your app uses.

**Build for someone else:**
- Best possible next project: ask a family member what would make something easier for
  them, then build that. Real users find real bugs.

### Last thing

> "You built four things this week that didn't exist on Monday. Whatever you do next —
> that's what it feels like. Go do it again."

---

## Instructor Prep Checklist

- [ ] Visible countdown timer for the showcase
- [ ] Projector cable / screen-share tested for demos
- [ ] Scope-cut table printed for the pitch block
- [ ] Plan for getting projects off the machines — USB, email, or a shared folder
- [ ] Certificates or something to hand out, if CompuCon does that
- [ ] Know each student's project before the showcase so you can name something specific
