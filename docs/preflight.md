# Preflight — Before You Teach This

Project status, not conventions. Constraints live in `CLAUDE.md`, in the repo root.

**Nothing here has been taught or tested on real hardware.** All five timing tables sum
correctly on paper, but no block has been run with real campers — expect the first
delivery to run long. Delete this file once the track has run once.

**Middle school is one session.** Session 1, 85 minutes, and it ends there. High school
runs all four. Sessions 2–4 are high school only.

---

## Contents

- [Before you teach — in order](#before-you-teach-in-order)
- [Still your call](#still-your-call)
- [Deliberately not done](#deliberately-not-done)

## Before you teach — in order

Each item names what breaks if you skip it.

1. **Verify the environment on a real lab laptop.** `claude` launches · `python -c
   "import tkinter"` is silent · `Documents\Projects` exists (create it if missing) ·
   note whether PowerShell is 5.1 or 7 · walk the full `Copy-Item` / `Remove-Item`
   save-point cycle · make a `<Name>` folder and confirm `mkdir` / `cd` work inside it
   — name folders are new, and every session's setup now depends on them.
   *If `claude` or tkinter fails, Session 1 doesn't happen. If the copy commands are
   blocked by lab permissions, the entire save-point system in Session 3 breaks. If
   `Documents\Projects` is missing, every session's setup fails on the first `cd`.*

2. **Confirm the Google Drive take-home link works on a lab machine.** Open the MS link
   (middle school) and the HS link (high school), and confirm every camper has a folder
   with their name in the right one. Campers copy their code to Drive before they leave —
   if the link is wrong or a folder is missing, that camper leaves with nothing. **This
   matters most for middle school**, who get exactly one chance at it.
   Local name folders should match the Drive folders: `Projects\<Name>\<project>`, first
   name, one word.
   - MS: <https://drive.google.com/drive/folders/1oNet8nYU7jCxaeuXWlM8ZIS7dL_IS2rY?usp=drive_link>
   - HS: <https://drive.google.com/drive/folders/1iNAG8vacKNsL3-c_1e_363R00ZxjgJPM?usp=drive_link>

3. **Read MS Session 1 aloud with a timer.** 85 minutes is the tightest budget in the
   track, and it is the entire middle school experience — there is no second session to
   recover in. It has to land the first time.

4. **Dry-run the Session 1 opening demo.** The 6-minute live build of `dice.py` is the
   hook for the whole track, and there's no script for it — you're improvising in front
   of the room. There is deliberately no pre-written demo file.

5. **Confirm class size.** HS Session 4 has 30 minutes of demo time; at 90 seconds each
   that's 20 campers with zero slack. Above ~20, cut to 60 seconds or run part of it as
   a gallery walk — decide before the day, not during it.

6. **Decide the MS break policy.** The MS session runs 85 minutes straight. Session 1
   notes where to take five minutes and what to cut for it; the call is yours.

7. **Check the live site.** Settings → Pages → Deploy from a branch, `main`, folder
   `/docs`. GitHub Pages renders the markdown there, so the curriculum `.md` files
   appear as `.html` pages. Then click through: home → Middle School → a session's
   notes → back. **Open it on a phone too** — campers will. Check the nav stacks and
   that the wide tables in `project-ideas.html` are usable.

8. **Scan the QR code with a phone.** The code on `about.html` is an image — nothing in
   the repo checks that it encodes the right address. Scan it from the screen, and from
   a printout if you're handing one out, and confirm it lands on the live site. Also
   confirm the URL printed under it still matches where Pages actually serves from.
   *If the code is wrong, every camper who scans it instead of typing lands nowhere.*

9. **Print one camper notes page from the browser and look at it.** The print stylesheet
   flips the dark theme to black-on-white and hides the nav, but it has never met a real
   printer. If it comes out dark, print from the markdown instead.

10. **Print the rest.** Camper notes, correct age group — one handout per middle school
   camper, one per session for high school. They're written to be kept and referred back
   to, not skimmed once. Plus the Session 2 bad-prompts handout, which lives inline in
   the lesson plan.

---

## Still your call

**The tone of the "the AI wrote the code" talks** at the end of Sessions 1 and 4. The
most opinionated thing in the curriculum. MS gets two sentences, HS the full paragraph.
Soften, sharpen, or keep. For middle school it's the last thing they hear all camp.

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
- **Lesson plans are public.** Each `docs/session-N/lesson-plan.md` renders to a
  `/session-N/lesson-plan.html` page, and `teacher.html` links all four. Anyone who
  finds the site can read them. Fine if the plans aren't secret — worth knowing if
  they are.
- **Curriculum pages don't inherit the site chrome.** GitHub Pages themes the rendered
  markdown with its default layout — no hand-authored nav or footer, no `style.css`.
  The pandoc template that used to wrap those pages in the site theme is gone. Known
  and accepted; if site-wide consistency ever matters, a Jekyll layout committed to
  the repo would fix it.

------

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/) This Vibe Coding Curriculum by [Brian Bird](https://profbird.dev), created in <time>2026</time> with AI assistance, is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
