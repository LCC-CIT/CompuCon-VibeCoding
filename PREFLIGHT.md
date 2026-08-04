# Preflight — Before You Teach This

What's untested, what's deliberately missing, and what to do before Session 1.

**Constraints and conventions live in [`CLAUDE.md`](CLAUDE.md).** This file is only
project *status* — it should shrink as you verify things, and can be deleted once the
track has run once.

**Status as of 4 August 2026: complete draft, unreviewed, untaught.** All eight timing
tables (two per session file) sum correctly. Nothing has been tested on a real machine
or in front of a real classroom.

---

## Unverified — treat as assumptions, not facts

Nothing below was tested. Verification during drafting was done by hand.

| Assumption | Risk if wrong |
|---|---|
| `cc-ds` launches and works on the lab image | Session 1 doesn't happen |
| `cc` works for Claude Pro students | Minor; they fall back to `cc-ds` |
| `python -c "import tkinter"` succeeds | Every example breaks |
| Lab machines run PowerShell 5.1 or 7 | Command syntax notes need revisiting |
| `Copy-Item -Recurse` / `Remove-Item -Recurse` work under lab permissions | The entire save-point system breaks |
| Session lengths are exact and don't shrink in practice | Timing tables need rework |
| ~20 students per session | HS Session 4's showcase math breaks |

**Highest-value action: run the Session 1 prep checklist on a real lab laptop, and walk
the full save-point cycle yourself.** Ten minutes, de-risks most of this table.

The class-size row matters more than it looks. HS Session 4 has 30 minutes of demo time;
at 90 seconds each that's 20 students with zero slack. If sections run larger, cut to 60
seconds or run part of it as a gallery walk — decide before the day, not during it.

---

## Known gaps

Deliberately not done, so nobody "fixes" them by accident.

- **No slides.** Everything is instructor-read. If CompuCon wants slides, Session 1 is
  the only one that really warrants them.
- **No assessment or rubric.** The showcase is the assessment.
- **No parent-facing summary.** Likely useful; not written.
- **No pre-written demo code.** Instructors generate `dice.py` live in Session 1. That's
  the point of the opening, but it means being comfortable improvising.
- **Timing tables are theoretical.** Every block sums correctly; none has been run with
  real students. Expect the first delivery to run long.
- **MS has no scheduled breaks.** All four MS sessions are 85 minutes straight. Each file
  notes where to take five minutes and what to cut for it, but the call is the
  instructor's and should be made before the session.
- **Session 2's bad-prompts handout and spec sheet are inline in the lesson plan,** not
  separate printable files. The spec sheet is reproduced in the camper notes, so campers
  have it; the bad-prompts list is instructor-side only.

---

## Open decisions — yours to make

1. **The tone of the "the AI wrote the code" talks** (end of Sessions 1 and 4). The most
   opinionated call in the curriculum. MS gets two sentences, HS gets the full paragraph.
   Soften, sharpen, or keep.
2. **MS break policy** for all four sessions.
3. **Expected class size**, which determines HS Session 4's showcase format.

---

## Before Session 1 — do these in order

1. **Verify the environment** on a real lab laptop: `cc-ds`, tkinter, PowerShell version,
   and the full `Copy-Item` / `Remove-Item` save-point cycle
2. **Read MS Session 1 aloud with a timer.** 85 minutes is the tightest budget in the
   track and the one that must land perfectly, since it's standalone
3. **Confirm class size**; adjust HS Session 4's showcase format if above ~20
4. **Decide the MS break policy**
5. **Print the camper notes** — one per camper per session, correct age group. Check how
   many pages each runs at your printer settings; they're written to be kept and
   referred back to, not skimmed once
6. **Print the Session 2 bad-prompts handout** from the lesson plan — or pull it into a
   separate file first if you'd rather
7. **Dry-run the Session 1 opening demo.** The 6-minute live build is the hook for the
   entire track and there's no script for it
