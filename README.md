# CompuCon Vibe Coding Track

Four 3-hour sessions. Students build real, working apps by describing what they want to
an AI coding assistant, then testing, checking, and refining until it's right.

**Day 1 is standalone.** A student who shows up for one session leaves with a finished
app they built and can demo. Days 2–4 go deeper for students who stay.

---

## The One-Sentence Version

Vibe coding is *steering*, not typing. The skill we're teaching isn't syntax — it's
knowing what to ask for, how much to ask for at once, and how to tell whether you got it.

---

## Session Map

| Day | Theme | Students leave with |
|---|---|---|
| **1** | *Make Something Work* | A finished app + the build → run → fix loop |
| **2** | *Ask Better, Check Harder* | Prompting technique + the habit of verifying |
| **3** | *Build Something Bigger* | A multi-file project + planning before building |
| **4** | *Make It Yours* | A capstone project, demoed to the room |

Each file in `curriculum/` is a full instructor script for one session:

- [`day-1.md`](curriculum/day-1.md) — standalone session
- [`day-2.md`](curriculum/day-2.md)
- [`day-3.md`](curriculum/day-3.md)
- [`day-4.md`](curriculum/day-4.md)
- [`prompt-cheat-sheet.md`](curriculum/prompt-cheat-sheet.md) — one-page student handout
- [`project-ideas.md`](curriculum/project-ideas.md) — idea bank, sorted by difficulty
- [`troubleshooting.md`](curriculum/troubleshooting.md) — instructor-facing "when it breaks"

Plus [`HANDOFF.md`](HANDOFF.md) — decisions, open questions, and what's still unverified.

---

## Learning Goals Across the Track

By the end, students can:

1. **Describe** an app clearly enough that an AI can build it
2. **Run** what came back and read what happened
3. **Judge** whether the result is actually right — not just whether it ran
4. **Slice** a big idea into steps small enough to check one at a time
5. **Steer** an AI through a project that doesn't fit in a single file
6. **Name** what the AI is good at and where it needs a human

Goal 3 is the one that matters most and gets shortchanged most often. We hit it on
every single day.

---

## The Setup

**Windows 11 lab laptops, pre-configured.** Students open **PowerShell** (via Windows
Terminal) and type:

```powershell
cc-ds
```

This launches Claude Code wired to a DeepSeek model. Students never touch an API key.

**Students with their own Claude Pro account** can type `cc` instead, which runs Claude
Code on Anthropic's models. Both work identically for everything in this curriculum —
students should use whichever they have. Mention both on Day 1 and then stop
distinguishing.

**Instructors should know:** Claude Code is Anthropic's terminal coding agent. It can
read and write files in the current folder, run commands, and hold a conversation about
a codebase. On lab machines we run it against DeepSeek's models rather than Anthropic's
— same tool, different engine underneath. That `cc` and `cc-ds` behave the same while
running different models *is* the lesson: the interface and the model are separable
pieces. Worth surfacing on Day 2.

Each student works in their own folder:

```powershell
cd $HOME\Documents
mkdir my-project
cd my-project
cc-ds
```

Working in a project folder, not Documents itself, matters — that folder is the AI's
whole world, and a focused folder means focused attention.

> **PowerShell note for instructors:** Windows PowerShell 5.1 (the Windows 11 default)
> does **not** support `&&` for chaining commands. Every command in this curriculum is
> written one per line for that reason. If you rewrite any of them, keep them separate.

### The stack

Python + tkinter is the default and what every example uses. It's chosen deliberately:
zero install friction on the lab image, and a visible window in the first 60 seconds.

**Students who already know another stack may use it.** Web (HTML/CSS/JS) is the most
likely alternative and works fine. The curriculum's actual content — prompt sizing,
verification, scope cutting, save points — is stack-independent. Only the example code
changes.

---

## Middle School vs. High School

Same spine, different dials. Each session file has a **`MS/HS`** callout box wherever
the two diverge. The general pattern:

| | Middle School | High School |
|---|---|---|
| **Project scope** | Smaller, more visual, more immediate payoff | More features, more logic, more ambition |
| **Pacing** | More checkpoints, shorter work blocks (15–20 min) | Longer independent blocks (25–35 min) |
| **Concepts** | "The AI guessed wrong" | "The AI's context window doesn't include that" |
| **Verification** | Does it do the thing? Try to break it. | Edge cases, reading the code, does it match spec? |
| **Reading code** | Optional, encouraged for the curious | Expected by Day 3 |
| **Group work** | Pairs throughout | Solo with pair-debugging |

The demo apps and the arc are identical. Adjust ambition, not substance.

---

## What We Are Not Teaching

Worth being explicit with students, especially the older ones:

- **We're not teaching them to skip learning to code.** We're teaching a skill that
  works *alongside* it. The students who can read code will steer better, and we say so.
- **We're not claiming the AI is right.** Every session includes at least one moment
  where the AI produces something wrong or weird and students have to catch it. This is
  a feature of the curriculum, not an accident.
- **We're not doing a lecture course.** Target ratio is roughly 20% talking, 80% building.

---

## Standing Classroom Rules

Post these. Reference them constantly.

1. **Run it before you ask for the next thing.**
2. **One change at a time.**
3. **If it's been broken for 10 minutes, ask a human.**
4. **You have to be able to explain what your app does.**

Rule 4 is the anti-cheating rule and the anti-passivity rule at once. It's the whole
point of the track compressed into one sentence.
