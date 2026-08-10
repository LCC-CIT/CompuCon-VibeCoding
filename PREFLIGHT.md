# Preflight — Before You Teach This

Project status, not conventions. Constraints live in [`CLAUDE.md`](CLAUDE.md).

**Nothing here has been taught or tested on real hardware.** All eight timing tables sum
correctly on paper, but no block has been run with real students — expect the first
delivery to run long. Delete this file once the track has run once.

---

## Before you teach — in order

Each item names what breaks if you skip it.

1. **Verify the environment on a real lab laptop.** `cc-ds` launches · `python -c
   "import tkinter"` is silent · `Documents\Projects` exists (create it if missing) ·
   note whether PowerShell is 5.1 or 7 · walk the full `Copy-Item` / `Remove-Item`
   save-point cycle.
   *If `cc-ds` or tkinter fails, Session 1 doesn't happen. If the copy commands are
   blocked by lab permissions, the entire save-point system in Session 3 breaks. If
   `Documents\Projects` is missing, every session's setup fails on the first `cd`.*

2. **Read MS Session 1 aloud with a timer.** 85 minutes is the tightest budget in the
   track, and it's the one session that must land perfectly, since it stands alone.

3. **Dry-run the Session 1 opening demo.** The 6-minute live build of `dice.py` is the
   hook for the whole track, and there's no script for it — you're improvising in front
   of the room. There is deliberately no pre-written demo file.

4. **Confirm class size.** HS Session 4 has 30 minutes of demo time; at 90 seconds each
   that's 20 students with zero slack. Above ~20, cut to 60 seconds or run part of it as
   a gallery walk — decide before the day, not during it.

5. **Decide the MS break policy.** All four MS sessions are 85 minutes straight. Each
   file notes where to take five minutes and what to cut for it; the call is yours.

6. **Check the live site.** Settings → Pages → Deploy from a branch, `main`, folder
   `/docs`. Then click through: home → Middle School → a session's notes → back.
   **Open it on a phone too** — campers will. Check the nav stacks and that the wide
   tables in `project-ideas.html` are usable.

7. **Print one camper notes page from the browser and look at it.** The print stylesheet
   flips the dark theme to black-on-white and hides the nav, but it has never met a real
   printer. If it comes out dark, print from the markdown instead.

8. **Print the rest.** Camper notes: one per camper per session, correct age group —
   they're written to be kept and referred back to, not skimmed once. Plus the Session 2
   bad-prompts handout, which lives inline in the lesson plan.

---

## Still your call

**The tone of the "the AI wrote the code" talks** at the end of Sessions 1 and 4. The
most opinionated thing in the curriculum. MS gets two sentences, HS the full paragraph.
Soften, sharpen, or keep.

---

## Deliberately not done

So nobody "fixes" these by accident.

- **No slides.** Everything is instructor-read. Session 1 is the only one that would
  really warrant them.
- **No assessment or rubric.** The showcase is the assessment.
- **No parent-facing summary.** Likely useful; not written.
- **No registration or contact link on the site.** Enrolment is handled elsewhere.
- **Session 2's bad-prompts list is instructor-side only.** The spec sheet from that
  session *is* reproduced in the camper notes, so campers have that one.
- **Lesson plans are published but unlinked.** `docs/session-N/lesson-plan.html` is
  reachable by direct URL; nothing on the site links to it. Fine if the plans aren't
  secret — worth knowing if they are.
