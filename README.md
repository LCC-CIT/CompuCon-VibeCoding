# CompuCon Vibe Coding Track

Four sessions. Students build real, working apps by describing what they want to
an AI coding assistant, then testing, checking, and refining until it's right.

**Session 1 is standalone.** A student who shows up for one session leaves with a
finished app they built and can demo. Later sessions go deeper for students who stay.

**Session lengths differ by age group, and so does the content:**

| | Session 1 | Session 2 | Session 3 | Session 4 | Total |
|---|---|---|---|---|---|
| **Middle school** | 85 min | 85 min | 85 min | 85 min | 5h40m |
| **High school** | 120 min | 180 min | 180 min | 60 min | 9h |

Two things follow from this and are baked into the curriculum:

- **HS Session 4 is demos only.** No build time. The HS capstone is pitched at the end
  of Session 2 and finished during Session 3.
- **MS drops multi-file projects entirely.** With 340 minutes total against HS's 540,
  MS Session 3 is "make one app solid" rather than "build something bigger." MS pitches
  its capstone in Session 4 and builds it that same session.

---

## The One-Sentence Version

Vibe coding is *steering*, not typing. The skill we're teaching isn't syntax — it's
knowing what to ask for, how much to ask for at once, and how to tell whether you got it.

---

## Session Map

| Session | Middle school (85 each) | High school |
|---|---|---|
| **1** | *Make Something Work* — first app, the build→run→fix loop | Same, 120 min |
| **2** | *Ask Better, Check Harder* — prompting + verification | Same + capstone pitch and kickoff, 180 min |
| **3** | *Make It Solid* — save points, debugging, hardening one app | *Build Something Bigger* — multi-file, capstone finished, 180 min |
| **4** | *Make It Yours* — capstone built and demoed | *Demo Day* — demos and wrap-up only, 60 min |

Sessions 1–2 share a block sequence across age groups with different durations. Sessions
3–4 split into separate MS and HS sections in the same file, because the content
genuinely differs.

Each file in `curriculum/` is a full instructor script:

Each session has its own folder containing an instructor lesson plan and a self-contained
handout for each age group:

| Session | Lesson plan | Camper notes |
|---|---|---|
| **1** | [plan](curriculum/session-1/lesson-plan.md) | [MS](curriculum/session-1/ms-camper-notes.md) · [HS](curriculum/session-1/hs-camper-notes.md) |
| **2** | [plan](curriculum/session-2/lesson-plan.md) | [MS](curriculum/session-2/ms-camper-notes.md) · [HS](curriculum/session-2/hs-camper-notes.md) |
| **3** | [plan](curriculum/session-3/lesson-plan.md) | [MS](curriculum/session-3/ms-camper-notes.md) · [HS](curriculum/session-3/hs-camper-notes.md) |
| **4** | [plan](curriculum/session-4/lesson-plan.md) | [MS](curriculum/session-4/ms-camper-notes.md) · [HS](curriculum/session-4/hs-camper-notes.md) |

Shared reference material:

- [`project-ideas.md`](curriculum/project-ideas.md) — idea bank, sorted by difficulty
- [`troubleshooting.md`](curriculum/troubleshooting.md) — instructor-facing "when it breaks"

**Camper notes are self-contained** — each one carries the commands, prompts, and
reminders for that session, so campers never juggle two documents. Print one per camper
per session.

Plus [`PREFLIGHT.md`](PREFLIGHT.md) — what's untested, what's deliberately missing, and
what to do before Session 1.

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
students should use whichever they have. Mention both in Session 1 and then stop
distinguishing.

**Instructors should know:** Claude Code is Anthropic's terminal coding agent. It can
read and write files in the current folder, run commands, and hold a conversation about
a codebase. On lab machines we run it against DeepSeek's models rather than Anthropic's
— same tool, different engine underneath. That `cc` and `cc-ds` behave the same while
running different models *is* the lesson: the interface and the model are separable
pieces. Worth surfacing in Session 2 (HS only — MS skips it for time).

Each student works in their own folder:

```powershell
cd $HOME\Documents
mkdir my-project
cd my-project
cc-ds
```

Working in a project folder, not Documents itself, matters — that folder is the AI's
whole world, and a focused folder means focused attention.

> **PowerShell note for instructors:** lab machines may run PowerShell 5.1 or 7, and
> 5.1 does **not** support `&&` for chaining commands. Since there's no reliable way to
> tell which version a given machine has, every command in this curriculum is written
> one per line — that syntax works on both. If you rewrite any of them, keep them
> separate.

### The stack

Python + tkinter is the default and what every example uses. It's chosen deliberately:
zero install friction on the lab image, and a visible window in the first 60 seconds.

**Students who already know another stack may use it.** Web (HTML/CSS/JS) is the most
likely alternative and works fine. The curriculum's actual content — prompt sizing,
verification, scope cutting, save points — is stack-independent. Only the example code
changes.

**No git.** Students don't use version control. "Save points" means copying the project
folder when it works and copying it back to undo — taught in
[Session 3](curriculum/session-3/lesson-plan.md) for both age groups.

---

## Middle School vs. High School

Same teaching philosophy, different structure. MS has 5h40m against HS's 9h, so this is
not a pacing dial — MS has real cuts (multi-file projects are gone entirely). Every
session file carries separate MS and HS timing tables, plus **`MS/HS`** callout boxes
wherever the content diverges within a shared block. The general pattern:

| | Middle School | High School |
|---|---|---|
| **Project scope** | Smaller, more visual, more immediate payoff | More features, more logic, more ambition |
| **Pacing** | More checkpoints, shorter work blocks (15–20 min) | Longer independent blocks (25–35 min) |
| **Concepts** | "The AI guessed wrong" | "The AI's context window doesn't include that" |
| **Verification** | Does it do the thing? Try to break it. | Edge cases, reading the code, does it match spec? |
| **Reading code** | Optional, encouraged for the curious | Expected by Session 3 |
| **Group work** | Pairs throughout | Solo with pair-debugging |

The demo apps and general arc are shared. Adjust ambition and scope, not the underlying
teaching content — but note MS's total time (5h40m) is well under half of HS's (9h), so
"adjust ambition" now means real cuts for MS, not just smaller steps.

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
