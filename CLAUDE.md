# CompuCon Vibe Coding Track

Curriculum for a "vibe coding" track at CompuCon, a summer tech camp. Middle school and
high school run as **separate sessions**, with the **same teaching spine** — but their
schedules are genuinely different, not just a pacing dial. **Middle school is one
85-minute session; high school is four sessions totalling nine hours.** See the schedule
below.

**This repo contains teaching materials, not software.** There is no app to build, no
tests to run, no dependencies. The curriculum is Markdown, meant to be read by an
instructor in front of a classroom or handed to a camper. `docs/` *is* the published
site — GitHub Pages renders the markdown there directly, so there is no separate HTML
to maintain.

**Current state: rebuilt against the real schedule, git removed throughout, middle school
cut to a single session.** Session 1 carries separate MS and HS timing tables; Sessions
2–4 are high school only and carry one each. **Session 1 has been delivered to both age
groups** (2026-08-10), so the MS track is complete and HS Sessions 2–4 are still ahead.
**MS ran its full 85 minutes and the pacing was right — don't touch the MS timings.**
HS Session 1 ran in ~60 minutes against a 120-minute plan, so treat the remaining HS
estimates with suspicion; the padding is in the talk blocks, not the build blocks. See
`preflight.md`.

---

## What's here

```
README.md                      Track overview — start here
docs/                          THE SITE — GitHub Pages serves from here
  index.html                   Landing page          ┐
  middle-school.html           MS page               │ hand-authored — no
  high-school.html             HS session index      │ markdown source,
  teacher.html                 Instructor hub         │ edit these directly
  faq.html                     Questions             │
  about.html                   What this is          │
  style.css                    Shared theme          ┘
  session-1/
    lesson-plan.md             Instructor script — both age groups
    ms-camper-notes.md         Camper handout, middle school
    hs-camper-notes.md         Camper handout, high school
    ai-topics.md               HS-only segment bank for when a group runs short (draft)
    opencode-zen-howto.md      Free-model how-to — confirmed working, no account needed
    local-models-howto.md      Self-hosted model how-to — draft, unverified end to end
  session-2/                   HS only — lesson-plan.md + hs-camper-notes.md
  session-3/                   HS only
  session-4/                   HS only
  project-ideas.md             Idea bank by difficulty
  troubleshooting.md           Instructor reference for when things break
  preflight.md                 What the first delivery settled, what's still unverified
```

Session 1 has six files: one lesson plan, two camper handouts, and three take-home /
overflow resources — `ai-topics.md` (an HS-only bank of short teach-then-build segments
for when a group finishes early, still draft), `opencode-zen-howto.md` (using a free
third-party model provider, confirmed working), and `local-models-howto.md` (running a
model on your own computer with Ollama or LM Studio, draft — see below). Sessions 2–4
have two: a lesson plan and the HS handout. **There is no `ms-camper-notes.md` outside
`session-1/`** — don't re-create one.

**`opencode-zen-howto.md` deliberately breaks one standing rule** — one command. It turns
out the free models need no account and no API key at all, so it no longer breaks those
two rules; installing and running `opencode` is the whole setup. It exists so campers can
keep coding **at home** for free, since the in-class tool costs money; it is an after-camp
path, not part of the Session 1 spine. Don't let its contents leak into the lesson plans
or camper notes.

**It is footnoted, not fully linked.** Added 2026-08-10: every place the site tells a
camper to keep building at home — `middle-school.html`, `session-3/hs-camper-notes.md`,
`session-4/hs-camper-notes.md` — carries a `\*` footnote pointing here. It is still
**not** in any primary navigation, resource list, or `teacher.html` — promoting it there
is now a judgment call, not something still blocked. **Confirmed 2026-08-11:** the free
models are available the moment OpenCode is installed — no signup, no API key, no
provider setup — tested on a personal Windows 11 machine (2026-08-10) and on an actual
CompuCon lab machine (2026-08-11). That resolves the earlier CLI-vs-desktop-app gap;
there's no connect flow left to get wrong. **The only open question now is the usage
cap:** one user reports hitting 200 requests in a 5-hour window, unconfirmed whether
that's per-model or total — treat it as a live caveat, not settled. If you add another
"keep building at home" line anywhere, footnote it the same way instead of leaving it
bare. Writing accurately about that provider's free models is correct and wanted; it does
not conflict with the rule against calling Claude Code free.

**`local-models-howto.md` is the third at-home option — partly tested.** It covers
running a model locally with Ollama or LM Studio, and using it from OpenCode or from
`claude` itself (via Ollama's Anthropic-compatible endpoint). Added 2026-08-11. **The
Claude Code half is confirmed** — the direct env-var connection to Ollama has been run
for real, on both a Mac and a Windows machine. **The OpenCode half is still unverified**,
built from OpenCode's provider docs rather than from running it. It is a bigger
departure from the track than the Zen page regardless: real hardware, a multi-gigabyte
install, and command-line setup, all outside the Session 1 spine — and it needs hardware
CompuCon's lab laptops don't have, so it's a home-only option, never something to point a
camper at in class. `faq.html` links to it (the "without the cloud" question); it is
still not in `teacher.html`, the main nav, or any resource list — treat that as a
judgment call, not something still blocked, now that the Claude Code path is confirmed.

Session 1's lesson plan uses one block sequence with dual MS/HS durations. Sessions 2–4
are single-audience and use plain durations. The `## MIDDLE SCHOOL` / `## HIGH SCHOOL`
section split is gone — nothing needs it anymore.

**Terminology:** "Session N" everywhere — folders, filenames, and prose. The camp calls
them sessions, and MS/HS sessions aren't the same length, so "day" is misleading. There
is no `day-N.md` anymore.

**Camper notes are self-contained.** Each one repeats the commands and reminders needed
for that session, so a camper never needs a second document mid-class. There is no
separate cheat sheet — it was retired to stop two handouts from drifting apart. If you
add a command or a rule, check whether the camper notes for that session need it too.

---

## How the site works — the only build step is GitHub Pages

**The curriculum markdown in `docs/` is the published site.** GitHub Pages builds from
the `docs/` folder and renders each `.md` file to an `.html` page (`session-N/*.md` →
`/session-N/*.html`, `project-ideas.md` → `/project-ideas.html`, and so on). There is no
generation script, no pandoc, no workflow — nothing in the repo converts markdown to
HTML. Edit the `.md` and the live page updates on the next Pages build. **Do not add a
`.nojekyll` file to `docs/`** — Jekyll is what performs that rendering, and `.nojekyll`
would serve the markdown as raw text instead.

Three consequences follow from this:

- **Cross-links between curriculum files are `.html`, not `.md`.** Pages serves
  `project-ideas.html`, so a `](troubleshooting.md)` link would 404 on the live site.
  Write `](troubleshooting.html)`. This flipped from the old convention, where a
  workflow rewrote `.md` links at build time — no rewrite happens now, and nothing will
  fix it for you.
- **The old pipeline is gone.** The two pandoc workflows and the
  `.github/pandoc/camper-notes.html` wrapper template were deleted when the curriculum
  moved into `docs/`. There is no `.github/` directory anymore. Don't re-create a
  markdown→HTML pipeline.
- **Rendered curriculum pages don't inherit the site chrome.** GitHub Pages themes the
  rendered markdown with its default layout — no hand-authored nav or footer, no
  `style.css`. The six hand-authored pages keep the full theme; the curriculum pages
  don't. Known and accepted for now — see `preflight.md`.

**Hand-authored pages** — `index.html`, `middle-school.html`, `high-school.html`,
`teacher.html`, `faq.html`, `about.html`, plus `style.css`. No markdown source; edit
them directly.
They share
`style.css` rather than each inlining the theme, so a colour or spacing change happens
in one place. `index.html` keeps its terminal animation as an inline `<script>`.

`style.css` is responsive and covers both the landing pages and the `.prose` content.
Breakpoints: 900 / 860 / 700 / 640 / 600 / 520 / 480 / 420 / 360.
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

**Session 1 must stand alone**, for both age groups. HS campers can attend one session
only, and for MS campers Session 1 *is* the track. It has to deliver a complete
experience ending in a working app they built. Never add a Session 1 dependency on later
material, and never tease Session 2 to the MS room.

**The real schedule — MS and HS are structurally different, not just paced
differently:**

| | Session 1 | Session 2 | Session 3 | Session 4 | Total |
|---|---|---|---|---|---|
| **Middle school** | 85 min | — | — | — | 85 min (1h25m) |
| **High school** | 120 min | 180 min | 180 min | 60 min | 540 min (9h) |

All of these numbers are **actual teaching time** — no arrival, attendance, or buffer
padding is baked in already. Session 1 carries **two timing tables**, one per age group;
Sessions 2–4 carry one. Each must sum exactly to its session length. Verify after any
edit.

Three structural facts the curriculum is built around. Don't undo them by accident:

- **MS is Session 1 and nothing else** — 85 minutes against HS's 540. It is not "the same
  content, paced down"; everything past the first session is simply not taught to them.
  **MS does no multi-file work, no capstone, and no save-point block.** Treat
  `project-ideas.md`'s Starter tier as a hard ceiling for MS.
- **Sessions 2–4 are high school only.** No MS timing table, no `MS/HS` callouts, no
  `ms-camper-notes.md` in those folders. If you find yourself adding MS material to one
  of them, stop — it belongs in Session 1 or nowhere.
- **HS Session 4 is 60 minutes and contains no build time.** It is demos and wrap-up
  only. The HS capstone is pitched at the end of Session 2 and must be *finished* during
  Session 3. Don't add build activities to HS Session 4 — the 10-minute setup block
  exists only so a camper can restore a working copy, not to code.

**Python + tkinter is the default stack.** Chosen for zero install friction on the
Windows lab image and a visible window inside 60 seconds. Campers who already know
another stack may use it, but all examples stay Python + tkinter. Do not add examples
requiring pip installs, API keys, accounts, or network access.

**No git.** Campers do not use version control. "Save points" are manual folder copies:

```powershell
cd $HOME\Documents\Projects
cd <Name>
Copy-Item -Recurse myproject myproject-working    # save
Remove-Item -Recurse myproject                    # undo, step 1
Copy-Item -Recurse myproject-working myproject    # undo, step 2
```

`<Name>` is the camper's name folder — every project lives at
`Projects\<Name>\<project>`, matching their Google Drive folder. Taught in Session 3,
which is high school only; MS never covers save points. Same concept as a commit, no new
tool. Always offer the File Explorer equivalent alongside the commands — some campers
need the visual route.
**Grep for `git` before calling any file finished.**

**Windows 11, PowerShell 5.1 or 7 — lab machines may run either.** Write every command
so it works on both:

- **No `&&` chaining, ever** — PowerShell 7 supports it but 5.1 doesn't, and you can't
  tell which one a given lab machine has. One command per line, no exceptions.
- Backslash paths: `$HOME\Documents`, not `~/`
- `python` is the command, not `python3`
- No `sudo`, `apt`, or Unix-only tools

**Verification is the spine of the track.** "It ran ≠ it's right" recurs in every session
and escalates. Any new material should reinforce it, not dilute it. If a block has to be cut
for time, cut something else.

**Roughly 20% instructor talking, 80% campers building.** Check any addition against
this. The most common failure mode when expanding a curriculum is adding lecture.

---

## The tooling campers use

**`claude`** — Claude Code. One command on every machine. The old two-command setup
(`cc-ds` on DeepSeek, `cc` for campers with their own Claude Pro account) was retired
because the launcher scripts couldn't be deployed to the college lab machines
(permission restrictions). Don't reintroduce a second command.

The Session 2 "the interface and the model are separable" aside (HS only) still stands —
the tool is separate from the model behind it. It just no longer has two commands to
point at.

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

**Session 1 only** — it's the only file with two audiences. Not every block there needs
one; only add where the two genuinely diverge. Sessions 2–4 have no MS reader, so a
callout in those files is a bug.

**Session structure.** Each session file: title, one-line framing, timing table(s), then
one `## Block Name (N min)` section per row — Session 1 uses `(MS n min / HS n min)`,
Sessions 2–4 a plain `(n min)`. Sessions 3–4 prefix each block with its clock position,
`## H:MM — Block Name (N min)`. Instructor prep checklist at the end. Session 1 carries
two timing tables and one block sequence with dual durations; don't fudge one table to
loosely fit both audiences.

**Line width** wraps around 90 characters.

**Tables** for anything comparative. They're scannable mid-class, which is the actual
use case.

---

## Editing this repo

- **Read `preflight.md` first.** It records what's still unverified and what's missing
  on purpose. Several apparent gaps are deliberate — don't "fix" them.
- **Check timing tables after any edit to a session file** — both tables in Session 1,
  the single table in Sessions 2–4. This is the easiest thing to silently break.
- **Grep for `git` before treating a file as finished.** It should only appear inside an
  explanation of *why* it was removed, never as an instruction to campers.
- **Check cross-file links.** README links into `docs/` with `.md` filenames (it's read
  on GitHub, not the site). Links *between* curriculum files are `.html` — that's the
  URL GitHub Pages serves, and nothing rewrites it, so a `.md` link would 404 on the
  published site. Don't "fix" the `.html` links back to `.md`.
- **Don't add a package manager, bundler, or test framework.** The curriculum is
  Markdown and the site is hand-written HTML + one CSS file. The only build step is
  GitHub Pages itself — don't add another pipeline.
- **Every curriculum `.md` file and `README.md` carries a `## Contents` section,
  generated by `add_toc.py`.** Run `python add_toc.py` (no arguments = all files)
  whenever headings are added, removed, or renamed. It lists `##`/`###` headings as
  anchor links, only ever edits the Contents section, and is idempotent — a deliberate
  maintenance tool, not a markdown→HTML pipeline. Keep `#` for the title alone; the
  script warns if another `#` heading appears — demote it to `##`.
- The author is a professor running this camp. Treat pedagogical judgment as theirs —
  offer alternatives rather than rewriting the teaching approach unprompted.
