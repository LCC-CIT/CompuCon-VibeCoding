# CompuCon Vibe Coding Track

Curriculum for a 4-day "vibe coding" track at CompuCon, a summer tech camp. Middle
school and high school run as **separate sessions** with the **same curriculum**.

**This repo contains teaching materials, not software.** There is no app to build, no
tests to run, no dependencies. Every file is Markdown meant to be read by an instructor
in front of a classroom or handed to a student.

---

## What's here

```
README.md                      Track overview — start here
HANDOFF.md                     Decisions, open questions, what's unverified
curriculum/
  day-1.md                     Standalone 3-hour session
  day-2.md                     Prompting + verification
  day-3.md                     Multi-file projects + Claude Code features
  day-4.md                     Capstone + showcase
  prompt-cheat-sheet.md        Student handout, printed double-sided
  project-ideas.md             Idea bank by difficulty
  troubleshooting.md           Instructor reference for when things break
```

---

## Hard constraints — do not change without asking

**Day 1 must stand alone.** Students can attend one session only. Day 1 has to deliver a
complete experience ending in a working app they built. Never add a Day 1 dependency on
later material.

**Each session is exactly 3 hours.** Every day file opens with a timing table that sums
to 3:00 with no gaps. If you add or expand a block, take the minutes from somewhere else
and update the table. Verify the arithmetic.

**Python + tkinter is the default stack.** Chosen for zero install friction on the
Windows lab image and a visible window inside 60 seconds. Students who already know
another stack may use it, but all examples stay Python + tkinter. Do not add examples
requiring pip installs, API keys, accounts, or network access.

**Windows 11 + PowerShell.** All commands must run in Windows PowerShell 5.1:

- **No `&&` chaining** — one command per line, always
- Backslash paths: `$HOME\Documents`, not `~/`
- `python` is the command, not `python3`
- No `sudo`, `apt`, or Unix-only tools

**Verification is the spine of the track.** "It ran ≠ it's right" recurs every day and
escalates. Any new material should reinforce it, not dilute it. If a block has to be cut
for time, cut something else.

**Roughly 20% instructor talking, 80% students building.** Check any addition against
this. The most common failure mode when expanding a curriculum is adding lecture.

---

## The tooling students use

- **`cc-ds`** — Claude Code on DeepSeek models, preconfigured on lab laptops. The default.
- **`cc`** — Claude Code on Anthropic models, for students with their own Claude Pro
  account. Functionally identical for this curriculum.

Mentioned once on Day 1, then treated as the same thing. Don't add material that
distinguishes them beyond the Day 2 "the interface and the model are separable" aside.

---

## Writing conventions

Match these when editing or adding files.

**Voice.** Direct, concrete, written for an instructor to say out loud. Short sentences.
No hedging. Analogies over abstractions.

**Instructor speech** goes in blockquotes:

> "It's like a genius intern on day one. Incredibly fast, knows every library, has no
> idea what you actually want, and will never tell you it's confused."

**Age differentiation** uses this exact callout format, placed at the end of the block it
modifies:

```markdown
**MS/HS**
> **MS:** What changes for middle school.
> **HS:** What changes for high school.
```

Not every block needs one. Only add where the two genuinely diverge.

**Session structure.** Each day file: title, one-line framing, timing table, then one
`## H:MM — Block Name (N min)` section per row. Instructor prep checklist at the end.

**Line width** wraps around 90 characters.

**Tables** for anything comparative. They're scannable mid-class, which is the actual
use case.

---

## Editing this repo

- **Read `HANDOFF.md` first.** It records why things are the way they are and what's
  still unverified. Several apparent gaps are deliberate.
- **Check timing tables after any edit to a day file.** This is the easiest thing to
  silently break.
- **Check cross-file links.** README links into `curriculum/`; files inside
  `curriculum/` link to each other with bare filenames.
- **Don't add a build step, package.json, or CI.** It's Markdown.
- The author is a professor running this camp. Treat pedagogical judgment as theirs —
  offer alternatives rather than rewriting the teaching approach unprompted.
