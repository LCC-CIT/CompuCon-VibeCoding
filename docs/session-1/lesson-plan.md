# Session 1 — Make Something Work

**This is a standalone session for both age groups.** A student who attends only this session leaves with a working app they built, understands the loop that produced it, and could do it again. Nothing in this session assumes a Session 2.

---

## Timing

MS and HS run the same seven blocks. HS gets 35 more minutes, spent almost entirely on
independent build time and on the concepts blocks.

### Middle school — 85 min

| Time | Block | Mode |
|---|---|---|
| 0:00–0:08 | Hook: build an app in front of them | Instructor demo |
| 0:08–0:15 | What just happened | Short talk |
| 0:15–0:40 | Build #1: everyone builds Mad Libs | Guided, lockstep |
| 0:40–0:48 | The three moves: Ask, Run, Fix | Short talk + demo |
| 0:48–1:10 | Build #2: make it yours | Independent |
| 1:10–1:18 | The AI was wrong + break your app | Whole group |
| 1:18–1:25 | Showcase + take it home | Students demo |

> **No break is scheduled.** 85 minutes is the whole session. If your group needs one,
> take 5 at the 0:48 mark and cut Build #2 to 17 minutes — don't cut the 1:10 block.

### High school — 120 min

| Time | Block | Mode |
|---|---|---|
| 0:00–0:10 | Hook: build an app in front of them | Instructor demo |
| 0:10–0:22 | What just happened | Short talk |
| 0:22–0:50 | Build #1: everyone builds Mad Libs | Guided, lockstep |
| 0:50–1:05 | The three moves: Ask, Run, Fix | Short talk + demo |
| 1:05–1:40 | Build #2: pick your own app | Independent |
| 1:40–1:52 | The AI was wrong + break your app | Whole group |
| 1:52–2:00 | Showcase + take it home | Students demo |

---

## Hook (MS 8 min / HS 10 min)

**Do not explain anything first.** Open a terminal on the projector and build something.

```powershell
cd $HOME\Documents\Projects
mkdir demo
cd demo
cc-ds
```

Type your prompt out loud so they see you thinking:

> Build a dice roller in Python with a tkinter window. Big button that says ROLL, and
> when I click it, it shows a random number from 1 to 20 in huge text. Save it as
> `dice.py`.

Let it generate. Narrate what you see scroll by — "it's writing a file, it's showing me
the code." Then run it:

```powershell
python dice.py
```

Click the button a few times. Then, live:

> Make the number change color — green if it's 20, red if it's 1, black otherwise.

Run it again. Roll until you get a 20.

**Total elapsed: under 6 minutes.** Spend the remaining time letting them react, then:

> "That's the whole class. You describe, it builds, you run it, you fix it. Everything
> else today is getting good at those four things."

**MS/HS**
> **MS:** Take one request from the room for a third change. The visual payoff lands
> hard and it buys you their attention for the next 25 minutes.
> **HS:** After the demo, show them the actual `dice.py` file. Ask: "Anything in here
> surprise you? Anything you'd have done differently?" Sets up Session 2 verification.

---

## What Just Happened (MS 7 min / HS 12 min)

Keep this tight. Three ideas, no more.

### 1. You're the boss, not the typist

The AI writes the code. You decide what gets built, whether it's good, and what changes.
That's a real job — it's most of what senior engineers actually do.

### 2. The AI is a very fast guesser

It has read an enormous amount of code and it's very good at predicting what code
should come next. That's it. It is not thinking about your project. It doesn't know what
you meant unless you said it. **It will confidently produce something wrong**, and it
will look just as polished as something right.

> "It's like a genius intern on day one. Incredibly fast, knows every library, has no
> idea what you actually want, and will never tell you it's confused."

### 3. Running it is the only real test

Code that looks right and doesn't run is worth nothing. You'll run your app more times
today than you'd guess.

### The tool

Point at the terminal:

- `cc-ds` starts **Claude Code**, an AI that can read and write files in the folder
  you're in and run commands
- It's running on a model from a company called **DeepSeek** — the tool and the AI
  brain behind it are separate pieces
- **If you have your own Claude Pro account, type `cc` instead.** Same tool, different
  model behind it. Everything today works the same either way.
- It sees the folder you started it in. That's its whole world. Start it in your
  project folder.
- `Ctrl+C` gets you out. `cc-ds` (or `cc`) gets you back in.

> Say `cc-ds` for the rest of the session. Students on `cc` will follow along fine —
> don't say both every time.

**MS/HS**
> **MS:** Stop after the intern analogy and the tool basics. Skip the tool/model
> distinction entirely — it costs 3 minutes you don't have.
> **HS:** Worth 2 minutes on tool-vs-model. It's a genuinely useful mental model for how
> AI products are built, and it explains why different setups behave differently.

---

## Build #1: Everyone Builds Mad Libs (MS 25 min / HS 28 min)

Lockstep. Everyone builds the same thing so nobody is lost and everyone succeeds early.

### Setup (5 min)

```powershell
cd $HOME\Documents\Projects
mkdir madlibs
cd madlibs
cc-ds
```

Walk the room. This is where setup problems surface — catch them now.

### Prompt 1 (MS 10 min / HS 10 min)

Put this on the projector. Students type it themselves (typing it makes them read it):

```
Build a Mad Libs generator in Python with a tkinter window.
Ask the user for 5 words: a noun, a verb, an adjective, a place, and a food.
Each one gets its own text box with a label.
When they click a "Make Story" button, show a funny story using their words.
Save it as story.py
```

Then:

```powershell
python story.py
```

**Everyone stops here until everyone's app runs.** Fast finishers help neighbors — this
is a real job too.

### Notice the prompt (MS 4 min / HS 5 min)

Put the prompt back up and mark it up:

- **What kind of program** — Python, tkinter window
- **What it does** — asks for 5 words, shows a story
- **What it looks like** — text boxes with labels, a button
- **Where it goes** — `story.py`

> "Four things: what kind of thing, what it does, what it looks like, where to put it.
> That's a good prompt. Notice what's *not* there — nothing about *how* to write the
> code. That's the AI's job."

### One change each (MS 6 min / HS 8 min)

Everyone makes one change of their own choosing. Suggestions on the board:

- "Make the window bigger and use a fun font"
- "Add a button that clears all the boxes"
- "Use three different story templates and pick one at random"
- "Change the background color to dark blue with white text"

Rule: **make the change, run it, then stop.** Hands up when yours works.

---

## The Three Moves (MS 8 min / HS 15 min)

This is the conceptual core of the session. Everything else is practice.

### Move 1: ASK

A good ask answers four questions:

| Question | Weak | Strong |
|---|---|---|
| What kind of thing? | "make a timer" | "a Python tkinter app" |
| What does it do? | "counts down" | "counts down from 25 minutes, beeps at zero" |
| What does it look like? | *(nothing)* | "big digits in the middle, Start and Reset buttons" |
| Where does it go? | *(nothing)* | "save it as `timer.py`" |

**The size rule.** The single most important thing today:

> **Ask for one thing at a time.**

Not because the AI can't do five things — it often can. Because when five things come
back at once and one is broken, you don't know which one. When you ask for one thing and
it breaks, you know exactly where to look.

**When you *should* ask for a lot at once:** the very first prompt. Starting from
nothing, describe the whole app. After that, one change at a time.

### Move 2: RUN

```powershell
python story.py
```

Run after every single change. Not "every few changes." Every one.

Three things can happen:

1. **It works** → good, next change
2. **It crashes** → copy the error message, paste the whole thing to the AI
3. **It runs but does the wrong thing** → the dangerous one

Number 3 is where humans matter. The computer can't tell you your Mad Libs story is
boring, that your timer counts *up*, or that your quiz says you got 3/5 when you got
4/5. Only you can.

### Move 3: FIX

How to report a problem, worst to best:

- ❌ "it's broken" — the AI has no idea what you mean
- ⚠️ "the button doesn't work" — better, still vague
- ✅ "When I click Make Story, nothing happens. No error in the terminal. The window
  just sits there."

> **Say what you did, what you expected, and what actually happened.**

That's not an AI trick — that's how you report a bug to any human on earth, forever.
It's a real professional skill and they're learning it today.

**MS/HS**
> **MS:** Cover the size rule and Move 3 properly; compress Move 2's three outcomes to
> "works / crashes / weird." Skip the four-question table as a table — just say the four
> things out loud while pointing at the Mad Libs prompt still on screen.
> **HS:** Full version, plus the demo: ask for five changes at once, let it come back
> tangled, then show the same five done one at a time. The difference is obvious and
> they'll remember it. Then push on outcome 3 — "How would you *know* your app is wrong?"

---

## Build #2 (MS 22 min / HS 35 min)

This is where the two age groups genuinely diverge in ambition.

**MS: make it yours.** Students keep working on `story.py` and customize it heavily —
their own story templates, inside jokes, colors, extra buttons, a random-story mode.
Anyone who finishes early and wants a fresh app may start one from
[`project-ideas.md`](../project-ideas.html), Starter tier only.

**HS: pick your own app.** Students choose from [`project-ideas.md`](../project-ideas.html)
or bring their own. Instructor approves the idea before they start — sanity check on
scope. Starter or Solid tier.

### Before they touch the keyboard (MS 3 min / HS 5 min)

Everyone writes their first prompt (or their next three changes, for MS) **on paper** and
gets it checked against the four questions. This catches the "make me a game" prompts
before they waste the whole block.

### Build (MS 15 min / HS 25 min)

Independent work. Instructor circulates.

**Checkpoints on the board:**

- [ ] It runs
- [ ] Made 3 changes, ran it after each one
- [ ] Something broke and I fixed it
- [ ] Made it look the way I want
- [ ] I can explain what my app does without looking at the code

**Instructor moves while circulating:**

- Student stuck on the same bug for 8+ minutes → tell them to describe the bug out
  loud to you first. They'll often fix it mid-sentence.
- Student asking for huge changes → "What's the smallest version of that? Ask for that."
- Student who finishes fast → "Now try to break it. Type nothing in the boxes. Type a
  number where a word goes. Click the button 20 times."
- Student whose app got tangled → `Ctrl+C`, delete the file, start fresh with a better
  first prompt. Restarting is cheap and this is a valuable lesson.

### Land it (MS 4 min / HS 5 min)

Everyone stops building. Last change gets tested, and they write one sentence:
*"My app lets you ___."*

**MS/HS**
> **MS:** Pairs. Call a checkpoint at the halfway mark — "hands up if your app runs
> right now." Anyone with a hand down gets you next.
> **HS:** Solo. Add a checkbox: "I read the code and understood one part of it."

---

## The AI Was Wrong (MS 8 min / HS 12 min)

The most important block of the session. Do not cut this for time.

Put this on the projector — a real thing an AI will produce for "make a quiz app that
shows my score at the end":

```python
score = 0
for question in questions:
    answer = input(question["text"] + " ")
    if answer == question["correct"]:
        score += 1

print(f"You got {score} out of {len(questions)}!")
print(f"That's {score / len(questions) * 100}%!")
```

Ask the room: **"What's wrong with this?"**

Let them find it. Seed hints only if they stall:

- What if the answer is "Paris" and I type "paris"? *(case sensitivity — marked wrong)*
- What if I type " Paris" with a space? *(marked wrong)*
- What does the percentage print if I get 1 out of 3? *(`33.33333333333333%`)*

None of this crashes. It runs perfectly. It's just wrong, and it will hand a student a
score they didn't earn.

Then land the point:

> "The AI wrote code that runs. It didn't write code that's *right*. Nothing in your
> computer will ever tell you the difference. That's your job — and it's why this class
> exists."

Then, hands-on: **everyone spends the last few minutes trying to break their own app.**

- Leave every box empty and click the button
- Type a number where a word goes
- Type something 200 characters long
- Click the button 20 times fast
- Resize the window very small

Found something? Fix it. That's the last change of the day.

**MS/HS**
> **MS:** Do the breaking exercise *first* (it's fun and physical), then show the code
> example with only the case-sensitivity bug. Skip the percentage and whitespace bugs.
> **HS:** Ask them to write the *fix* for each bug before you show it. Then ask the
> better question: "How would you have caught this if I hadn't told you?" Answer:
> you test with the wrong input on purpose.

---

## Showcase + Take It Home (MS 7 min / HS 8 min)

### Showcase (MS 5 min / HS 5 min)

There is not time for everyone to present. Run a **gallery walk**: everyone leaves their
app running, students circulate for 3 minutes, then 3–4 volunteers show theirs to the
whole room for 45 seconds each.

Volunteers cover two things:

1. **Show it working** (don't describe it, run it)
2. **One thing that broke and how you fixed it**

Item 2 is non-optional. Making the struggle public normalizes the loop and defuses the
idea that anyone got it right the first time.

### Take it home (MS 2 min / HS 3 min)

Three things they leave with:

1. **The loop, on an index card:**
   > **Ask small → Run it → Say exactly what went wrong → Repeat**

2. **Their app.** It's theirs. It's on the machine, and if they have a USB stick or
   email, it's a single file they can take.

3. **The honest note.** Say this out loud:

> "You built something real today. Also — the AI wrote the code, and you should know
> what that does and doesn't mean. It means you can build things right now that would
> have taken you months to learn. It doesn't mean you know how the code works. If you
> want to *actually* get good at this, the next thing to do is read the code the AI
> wrote and figure out what each part does."

**MS/HS**
> **MS:** Trim the honest note to its first two sentences. Then: "You made a thing that
> works. Show somebody."
> **HS:** Full version, plus: "The people who can do both — steer the AI *and* read the
> code — are going to be unbelievably good at this."

If they're coming back for Session 2, tell them the teaser: **"Next time we find out how
to tell when the AI is lying to you."**

---

## Instructor Prep Checklist

- [ ] **Print camper notes** — `ms-camper-notes.md` or `hs-camper-notes.md`, one per
      camper. Hand out at the start; they're written to be followed along with.
- [ ] Test `cc-ds` on a lab machine the morning of
- [ ] Confirm the `Documents\Projects` folder exists on every lab machine — create it
      if it's missing
- [ ] Confirm tkinter is available: `python -c "import tkinter"` (no output = good)
- [ ] Know that students with Claude Pro can use `cc` — mention it once at the start
- [ ] Have `dice.py` demo working before students arrive
- [ ] Project the idea board and the prompt template
- [ ] Index cards for the take-home loop
- [ ] Know how to `Ctrl+C` out of a hung session and restart — you'll do it a dozen times
- [ ] Read [`troubleshooting.md`](../troubleshooting.html)
- [ ] **Decide your break policy for MS** before you start — see the note under the MS
      timing table
