# CompuCon Vibe Coding Track

Curriculum for a "vibe coding" track at CompuCon, a summer tech camp. Middle school and
high school run as **separate sessions**, with the **same teaching spine** — but their
schedules are genuinely different, not just a pacing dial. See the schedule below.

**This repo contains teaching materials, not software.** There is no app to build, no
tests to run, no dependencies. The curriculum is Markdown, meant to be read by an
instructor in front of a classroom or handed to a student. `docs/` additionally holds a
small published website — see below.

**Current state: rebuilt against the real schedule, git removed throughout.** All four
session files carry separate MS and HS timing tables. Nothing has been taught yet — see
`PREFLIGHT.md` for what's still unverified.

---

## What's here

```
README.md                      Track overview — start here
PREFLIGHT.md                   Untested assumptions, known gaps, pre-teaching checklist
docs/                          PUBLISHED SITE — GitHub Pages serves from here
  index.html                   Landing page          ┐
  middle-school.html           MS session index      │ hand-authored,
  high-school.html             HS session index      │ see warning below
  faq.html                     Questions             ┘
  style.css                    Shared theme for the four pages above
  session-N/*.html             AUTO-GENERATED from curriculum/ — do not edit
  project-ideas.html           AUTO-GENERATED
  troubleshooting.html         AUTO-GENERATED
  .nojekyll                    Skips Jekyll processing; leave it alone
curriculum/
  session-1/
    lesson-plan.md             Instructor script — both age groups
    ms-camper-notes.md         Student handout, middle school
    hs-camper-notes.md         Student handout, high school
  session-2/                   (same three files)
  session-3/
  session-4/
  project-ideas.md             Idea bank by difficulty
  troubleshooting.md           Instructor reference for when things break
.github/
  pandoc/camper-notes.html     Template wrapping every generated page in the site theme
  workflows/
    markdown-to-html.yml       Converts changed curriculum markdown on push
    cleanup-deleted-markdown-html.yml   Full re-sync + deletes orphaned HTML
```

Every session folder has exactly three files: one lesson plan, two camper handouts.

Sessions 1–2 lesson plans use one block sequence with dual durations. Sessions 3–4 are
split into separate `# MIDDLE SCHOOL` and `# HIGH SCHOOL` sections because the content
genuinely differs.

**Terminology:** "Session N" everywhere — folders, filenames, and prose. The camp calls
them sessions, and MS/HS sessions aren't the same length, so "day" is misleading. There
is no `day-N.md` anymore.

**Camper notes are self-contained.** Each one repeats the commands and reminders needed
for that session, so a camper never needs a second document mid-class. There is no
separate cheat sheet — it was retired to stop two handouts from drifting apart. If you
add a command or a rule, check whether the camper notes for that session need it too.

**All HTML goes in `docs/`.** GitHub Pages serves from that folder, so a page anywhere
else won't be published. No CDN links and no build step — the camp network may block
outside requests. Relative local files (`style.css`) are fine; external requests aren't.

**`docs/` has two kinds of file, and they're handled completely differently:**

*Auto-generated* — `session-N/*.html`, `project-ideas.html`, `troubleshooting.html`. A
GitHub Action runs pandoc over `curriculum/**/*.md` on every push and rewrites these.
**Editing them directly is pointless; your changes get overwritten.** Edit the markdown.

Generated pages are wrapped in `.github/pandoc/camper-notes.html`, so they get the same
nav, footer, and `style.css` as the hand-authored pages. The workflow derives three
things per file: the page title (first `# ` heading), the relative path back to `docs/`
(so `style.css` resolves at any depth), and the "back" link — `ms-` files point to
Middle School, `hs-` files to High School, everything else to Home. It also rewrites
`.md` cross-links to `.html`, since the markdown links would 404 on the published site.

**Both workflows contain an identical copy of that `convert_md` function.** If you
change one, change the other, or pages will flip appearance depending on which workflow
ran last.

*Hand-authored* — `index.html`, `middle-school.html`, `high-school.html`, `faq.html`,
plus `style.css`. No markdown source. These are the public-facing pages.

> **⚠ Adding a new hand-authored page? You must add it to the `HANDWRITTEN` array in
> `.github/workflows/cleanup-deleted-markdown-html.yml`.** That workflow deletes any
> `.html` in `docs/` with no matching `.md` in `curriculum/`. It has already silently
> deleted `index.html` once. The array is the only thing preventing a repeat.

The four hand-authored pages share `style.css` rather than each inlining the theme, so a
colour or spacing change happens in one place. `index.html` keeps its terminal animation
as an inline `<script>`.

`style.css` is responsive and covers both the landing pages and the pandoc output
(`.prose` rules). Breakpoints: 900 / 860 / 700 / 640 / 600 / 520 / 480 / 420 / 360.
**Don't hide the nav on small screens** — it was `display:none` below 640px once, which
left `index.html` with no navigation at all, since that page has no in-body links. It
stacks now instead. There's also a print block that flips the whole palette to
black-on-white, because camper notes get printed as handouts.

These pages quote figures from the curriculum (session lengths, project examples, the
"genius intern" line). **If the schedule changes, update them too** — they're outside
every internal cross-check, so nothing else will catch it.

They're also written at roughly a 4th–6th grade reading level on purpose, since middle
schoolers are the youngest readers. Keep sentences short and gloss any jargon
(`prompt`, `capstone`, `multi-file`) on first use.

---

## Hard constraints — do not change without asking

**Session 1 must stand alone**, for both age groups. Students can attend one session
only. Session 1 has to deliver a complete experience ending in a working app they built.
Never add a Session 1 dependency on later material.

**The real schedule — MS and HS are structurally different, not just paced
differently:**

| | Session 1 | Session 2 | Session 3 | Session 4 | Total |
|---|---|---|---|---|---|
| **Middle school** | 85 min | 85 min | 85 min | 85 min | 340 min (5h40m) |
| **High school** | 120 min | 180 min | 180 min | 60 min | 540 min (9h) |

All of these numbers are **actual teaching time** — no arrival, attendance, or buffer
padding is baked in already. Every session file carries **two timing tables**, one per age
group, each summing exactly to its session length. Verify both after any edit.

Three structural facts the curriculum is built around. Don't undo them by accident:

- **MS total (340 min) is well under half of HS total (540 min).** MS is not "the same
  content, paced down." It has real cuts — most significantly, **MS does not do
  multi-file projects at all.** MS Session 3 is *Make It Solid* (save points, debugging,
  hardening one app). Treat `project-ideas.md`'s Starter tier as a hard ceiling for MS.
- **HS Session 4 is 60 minutes and contains no build time.** It is demos and wrap-up
  only. The HS capstone is pitched at the end of Session 2 and must be *finished* during
  Session 3. Don't add build activities to HS Session 4 — the 10-minute setup block
  exists only so a student can restore a working copy, not to code.
- **MS pitches and builds its capstone entirely within Session 4** (85 min, ~38 of which
  is build time). That's why the MS scope check is aggressive and why two must-haves is
  the cap.

**Python + tkinter is the default stack.** Chosen for zero install friction on the
Windows lab image and a visible window inside 60 seconds. Students who already know
another stack may use it, but all examples stay Python + tkinter. Do not add examples
requiring pip installs, API keys, accounts, or network access.

**No git.** Students do not use version control. "Save points" are manual folder copies:

```powershell
cd $HOME\Documents
Copy-Item -Recurse myproject myproject-working    # save
Remove-Item -Recurse myproject                    # undo, step 1
Copy-Item -Recurse myproject-working myproject    # undo, step 2
```

Taught in Session 3 for both age groups. Same concept as a commit, no new tool. Always
offer the File Explorer equivalent alongside the commands — some students need the
visual route. **Grep for `git` before calling any file finished.**

**Windows 11, PowerShell 5.1 or 7 — lab machines may run either.** Write every command
so it works on both:

- **No `&&` chaining, ever** — PowerShell 7 supports it but 5.1 doesn't, and you can't
  tell which one a given lab machine has. One command per line, no exceptions.
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

Mentioned once in Session 1, then treated as the same thing. Don't add material that
distinguishes them beyond the Session 2 "the interface and the model are separable"
aside (HS only).

**No git.** Not part of the toolset. See the no-git constraint above for the save-point
alternative.

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

**Session structure.** Each session file: title, one-line framing, timing table(s), then one
`## H:MM — Block Name (N min)` section per row. Instructor prep checklist at the end.
Since MS and HS no longer share session lengths, a session file needs either two timing
tables and two block sequences, or a clear split into an MS version and an HS version —
pick whichever reads cleaner per day, but don't fudge one table to loosely fit both.

**Line width** wraps around 90 characters.

**Tables** for anything comparative. They're scannable mid-class, which is the actual
use case.

---

## Editing this repo

- **Read `PREFLIGHT.md` first.** It records what's still unverified and what's missing
  on purpose. Several apparent gaps are deliberate — don't "fix" them.
- **Check timing tables after any edit to a session file** — for both MS and HS, since they
  no longer sum to the same total. This is the easiest thing to silently break.
- **Grep for `git` before treating a file as finished.** It should only appear inside an
  explanation of *why* it was removed, never as an instruction to students.
- **Check cross-file links.** README links into `curriculum/`; files inside
  `curriculum/` link to each other with bare `.md` filenames. That's correct — the
  workflow rewrites them to `.html` when it publishes, so don't "fix" them to `.html`
  in the markdown or they'll break for anyone reading the repo directly.
- **Don't add a package manager, bundler, or test framework.** The curriculum is
  Markdown and the site is hand-written HTML + one CSS file. The only automation is the
  two pandoc workflows described above — don't add a third pipeline.
- The author is a professor running this camp. Treat pedagogical judgment as theirs —
  offer alternatives rather than rewriting the teaching approach unprompted.
