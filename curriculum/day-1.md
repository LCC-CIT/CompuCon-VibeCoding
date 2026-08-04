# Day 1 — Make Something Work

**3 hours. Standalone.** A student who attends only this session leaves with a working
app they built, understands the loop that produced it, and could do it again at home.

Nothing in this session assumes a Day 2.

---

## Session Arc

| Time | Block | Mode |
|---|---|---|
| 0:00–0:15 | Hook: build an app in front of them | Instructor demo |
| 0:15–0:30 | What just happened | Short talk |
| 0:30–1:00 | Build #1: everyone builds the same app | Guided, lockstep |
| 1:00–1:10 | **Break** | |
| 1:10–1:25 | The three moves: Ask, Run, Fix | Short talk + demo |
| 1:25–2:20 | Build #2: pick your own app | Independent |
| 2:20–2:35 | The AI was wrong (planted bug exercise) | Whole group |
| 2:35–2:55 | Showcase | Students demo |
| 2:55–3:00 | Take it home | Wrap |

---

## 0:00 — Hook (15 min)

**Do not explain anything first.** Open a terminal on the projector and build something.

```bash
mkdir ~/vibe/demo && cd ~/vibe/demo
cc-ds
```

Type your prompt out loud so they see you thinking:

> Build a dice roller in Python with a tkinter window. Big button that says ROLL, and
> when I click it, it shows a random number from 1 to 20 in huge text. Save it as
> `dice.py`.

Let it generate. Narrate what you see scroll by — "it's writing a file, it's showing me
the code." Then run it:

```bash
python dice.py
```

Click the button a few times. Then, live:

> Make the number change color — green if it's 20, red if it's 1, black otherwise.

Run it again. Roll until you get a 20.

**Total elapsed: under 6 minutes.** Spend the remaining time letting them react, then:

> "That's the whole class. You describe, it builds, you run it, you fix it. Everything
> else today is getting good at those four things."

**MS/HS**
> **MS:** Do the color change as a second demo — the visual payoff lands hard. Take
> requests from the room for the third change.
> **HS:** After the demo, show them the actual `dice.py` file. Ask: "Anything in here
> surprise you? Anything you'd have done differently?" Sets up Day 2 verification.

---

## 0:15 — What Just Happened (15 min)

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
- It sees the folder you started it in. That's its whole world. Start it in your
  project folder.
- `Ctrl+C` gets you out. `cc-ds` gets you back in.

**MS/HS**
> **MS:** Stop after the intern analogy. Skip the tool/model distinction.
> **HS:** Worth 2 minutes on tool-vs-model — it's a genuinely useful mental model for how
> AI products are built, and it explains why different setups behave differently.

---

## 0:30 — Build #1: Everyone Builds Mad Libs (30 min)

Lockstep. Everyone builds the same thing so nobody is lost and everyone succeeds early.

### Setup (5 min)

```bash
mkdir ~/vibe/madlibs && cd ~/vibe/madlibs
cc-ds
```

Walk the room. This is where setup problems surface — catch them now.

### Prompt 1 (10 min)

Put this on the projector. Students type it themselves (typing it makes them read it):

```
Build a Mad Libs generator in Python with a tkinter window.
Ask the user for 5 words: a noun, a verb, an adjective, a place, and a food.
Each one gets its own text box with a label.
When they click a "Make Story" button, show a funny story using their words.
Save it as story.py
```

Then:

```bash
python story.py
```

**Everyone stops here until everyone's app runs.** Fast finishers help neighbors — this
is a real job too.

### Notice the prompt (5 min)

Put the prompt back up and mark it up:

- **What kind of program** — Python, tkinter window
- **What it does** — asks for 5 words, shows a story
- **What it looks like** — text boxes with labels, a button
- **Where it goes** — `story.py`

> "Four things: what kind of thing, what it does, what it looks like, where to put it.
> That's a good prompt. Notice what's *not* there — nothing about *how* to write the
> code. That's the AI's job."

### One change each (10 min)

Everyone makes one change of their own choosing. Suggestions on the board:

- "Make the window bigger and use a fun font"
- "Add a button that clears all the boxes"
- "Use three different story templates and pick one at random"
- "Change the background color to dark blue with white text"

Rule: **make the change, run it, then stop.** Hands up when yours works.

---

## 1:00 — Break (10 min)

---

## 1:10 — The Three Moves (15 min)

This is the conceptual core of the day. Everything else is practice.

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

Demo this. Ask for five changes at once, let it come back tangled, then show the same
five done one at a time. The difference is obvious and they'll remember it.

**When you *should* ask for a lot at once:** the very first prompt. Starting from
nothing, describe the whole app. After that, one change at a time.

### Move 2: RUN

```bash
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
> **MS:** Focus on Move 1 (size rule) and Move 3 (what happened vs. what you expected).
> Move 2's three outcomes can be simplified to "works / crashes / weird."
> **HS:** Push on outcome 3. Ask: "How would you *know* your app is wrong?" Get them to
> propose tests before running.

---

## 1:25 — Build #2: Your Own App (55 min)

Students pick from the idea board (see [`project-ideas.md`](project-ideas.md)) or bring
their own. Instructor approves the idea before they start — sanity check on scope.

### Before they touch the keyboard (5 min)

Everyone writes their first prompt **on paper** and gets it checked against the four
questions. Two minutes each. This catches the "make me a game" prompts before they waste
20 minutes.

### Build (40 min)

Independent work. Instructor circulates.

**Checkpoints on the board:**

- [ ] First version runs
- [ ] Made 3 changes, ran it after each one
- [ ] Something broke and I fixed it
- [ ] Made it look the way I want
- [ ] I can explain what my app does without looking at the code

**Instructor moves while circulating:**

- Student stuck on the same bug for 10+ minutes → tell them to describe the bug out
  loud to you first. They'll often fix it mid-sentence.
- Student asking for huge changes → "What's the smallest version of that? Ask for that."
- Student who finishes fast → "Now try to break it. Type nothing in the boxes. Type a
  number where a word goes. Click the button 20 times."
- Student whose app got tangled → `Ctrl+C`, delete the file, start fresh with a better
  first prompt. Restarting is cheap and this is a valuable lesson.

**MS/HS**
> **MS:** Pairs. Blocks of 15 with a stretch/share at each break. Steer toward the
> Starter tier of the idea list.
> **HS:** Solo, one 40-minute block. Push toward Stretch tier. Add a checkbox: "I read
> the code and understood one part of it."

### Land it (10 min)

Everyone stops building 10 minutes before showcase. Last change gets tested, and they
write one sentence: *"My app lets you ___."*

---

## 2:20 — The AI Was Wrong (15 min)

The most important 15 minutes of the day. Do not cut this for time.

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

Then, hands-on: **everyone spends 5 minutes trying to break their own app.**

- Leave every box empty and click the button
- Type a number where a word goes
- Type something 200 characters long
- Click the button 20 times fast
- Resize the window very small

Found something? Fix it. That's the last change of the day.

**MS/HS**
> **MS:** Do the breaking exercise first (it's fun and physical), then show the code
> example. Case sensitivity is the most graspable of the three bugs.
> **HS:** Ask them to write the *fix* for each bug before you show it. Then ask the
> better question: "How would you have caught this if I hadn't told you?" Answer:
> you test with the wrong input on purpose.

---

## 2:35 — Showcase (20 min)

Everyone demos. 60 seconds each, hard limit.

Format — three things, in this order:

1. **Show it working** (don't describe it, run it)
2. **One thing that broke and how you fixed it**
3. **One thing you'd add with more time**

Item 2 is non-optional. Making the struggle public is the point — it normalizes the
loop and defuses the idea that anyone got it right the first time.

**MS/HS**
> **MS:** 45 seconds. Do it as a gallery walk instead if the group is shy — everyone
> leaves their app running and circulates.
> **HS:** Add a fourth item: "One thing the AI got wrong that you had to correct."

---

## 2:55 — Take It Home (5 min)

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
> wrote and figure out what each part does. The people who can do both — steer the AI
> *and* read the code — are going to be unbelievably good at this."

If they're coming back for Day 2, tell them the teaser: **"Tomorrow we find out how to
tell when the AI is lying to you."**

---

## Instructor Prep Checklist

- [ ] Test `cc-ds` on a lab machine the morning of
- [ ] Confirm `python` (not `python3`) is on PATH, and tkinter is available:
      `python -c "import tkinter"`
- [ ] Have `dice.py` demo working before students arrive
- [ ] Project the idea board and the prompt template
- [ ] Index cards for the take-home loop
- [ ] Know how to `Ctrl+C` out of a hung session and restart — you'll do it a dozen times
- [ ] Read [`troubleshooting.md`](troubleshooting.md)
