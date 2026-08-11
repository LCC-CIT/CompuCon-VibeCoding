# Preflight — Before You Teach This

Project status, not conventions. Constraints live in `CLAUDE.md`, in the repo root.

**Session 1 has now been delivered to both age groups.** That makes the middle school
track complete — MS is Session 1 and ends there. High school still has Sessions 2, 3,
and 4 ahead, and none of those have been run with campers. This file is rewritten around
that split: what the first delivery settled, and what is still an estimate on paper.

Recorded 2026-08-10.

---

## Contents

- [What the first delivery settled](#what-the-first-delivery-settled)
- [The timing finding, and what it implies](#the-timing-finding-and-what-it-implies)
- [Fill these in while it's fresh](#fill-these-in-while-its-fresh)
- [Before you teach HS Session 2 — in order](#before-you-teach-hs-session-2-in-order)
- [Still your call](#still-your-call)
- [Deliberately not done](#deliberately-not-done)

## What the first delivery settled

Session 1 running at all means a whole column of assumptions came good. Don't re-verify
these from scratch — check them the morning of, out of habit, not out of doubt.

| Assumption | Status after Session 1 |
|---|---|
| `claude` launches on a lab machine | **Confirmed** — the session happened |
| `python -c "import tkinter"` works | **Confirmed** — campers got windows on screen |
| `Documents\Projects` exists / can be made | **Confirmed** |
| Name folders (`mkdir <Name>` / `cd <Name>`) | **Confirmed** — setup depended on them |
| The 6-minute `dice.py` opening demo | **Confirmed** — improvised live, it worked |
| Google Drive take-home, both age groups | **Confirmed as far as Session 1 goes** |
| MS Session 1 fits 85 minutes | **Confirmed** — ran the full 85, with a break, pacing judged right |
| `Copy-Item` / `Remove-Item` save-point cycle | **Still unverified** — Session 3 only |
| HS Session 4 demo pacing | **Still unverified** — Session 4 hasn't run |
| Session 2 bad-prompts handout in practice | **Still unverified** |

The save-point line is the one that matters. **Nothing in Session 1 exercised the folder
copy commands**, so the lab-permissions risk that could break the entire Session 3 save
point system is exactly as unverified as it was before you taught anything.

## The timing finding, and what it implies

The two deliveries disagree, and the disagreement is the useful part:

| | Planned | Actual |
|---|---|---|
| **MS Session 1** | 85 min | **85 min.** Fit, with a break. Pacing judged right. |
| **HS Session 1** | 120 min | **~60 min.** Half the budget. |

**The MS estimate was good. The HS estimate was inverted.** Session 1's plan assumed high
schoolers need about 1.4x the middle school durations for the same block sequence. They
actually got through it in about 0.7x — faster in absolute terms than the younger group,
not slower. The content wasn't wrong; the assumption that older campers consume more
clock was.

That matters for what's left, because Sessions 2 and 3 were estimated the same way. But
don't apply a flat discount — **the compression is in the talk and structured-exercise
blocks, not the build blocks.** A 75-minute build block is 75 minutes of building
regardless of age. What collapsed in Session 1 was the talking.

| Session | Planned | Where the risk is |
|---|---|---|
| HS 2 | 180 min | **The one to watch.** ~70 min of it is talk and lab (warm-up, prompt sizing, prompt lab, the four checks). Expect that front half to run well short. |
| HS 3 | 180 min | Lower risk — 75 min of it is capstone build, which will use its time. The opening 50 min of talk may compress. |
| HS 4 | 60 min | Demos scale with class size, not with the estimate. Unaffected. |

If Session 2's front half collapses you have an hour of dead room with campers who have
pitched a capstone and can't properly start it until Session 3. Have overflow ready
before you walk in — the [AI topics segment bank](session-1/ai-topics.html) was written
for exactly this, and any of its six segments drops into Session 2 as easily as
Session 1.

**Leave the MS timings alone.** They are the one set of numbers in this repo that has
been measured against real campers and come out right.

## Fill these in while it's fresh

These are the things only you know now, and they'll be gone in a month. Replace each
line with the answer.

- **Where in the MS session did you take the break?** We know one was taken and the
  session still fit 85 minutes. The block sequence assumes no break and suggests 0:48 if
  you need one — worth recording whether that's where it landed, and whether anything
  got cut to pay for it. →
- **Which HS block ran shortest against its estimate?** That's where the padding is
  concentrated, and it's the best predictor for Sessions 2 and 3. →
- **What broke that isn't in [`troubleshooting.html`](troubleshooting.html)?** Add it
  there, not here. →
- **Did the printed camper notes come out readable?** The print stylesheet flips the dark
  theme to black-on-white but had never met a real printer before this. →
- **Did anyone actually scan the QR code?** →

## Before you teach HS Session 2 — in order

Trimmed to what's genuinely still ahead. Each item names what breaks if you skip it.

1. **Walk the save-point cycle on a real lab laptop.** `Copy-Item -Recurse` to save,
   `Remove-Item -Recurse` then `Copy-Item -Recurse` back to undo, inside a `<Name>`
   folder. Do the File Explorer version too (right-click → Copy → Paste → rename).
   *This is the highest-risk unverified thing left in the track. If lab permissions
   block the copy commands, the entire save-point system in Session 3 breaks, and
   Session 3 is where the capstone has to be finished.* Session 2 also ends with campers
   making a `capstone-working` copy, so it fails there first.

2. **Confirm class size for HS.** Session 4 has 30 minutes of demo time; at 90 seconds
   each that's 20 campers with zero slack. Above ~20, cut to 60 seconds or run part of
   it as a gallery walk — decide before the day, not during it.

3. **Have the overflow material ready.** See [the timing finding](#the-timing-finding-and-what-it-implies)
   above. Pick your segments from the [topic bank](session-1/ai-topics.html) before the session,
   not from the front of a room with 40 minutes left.

4. **Confirm the HS Drive folders still have every camper's name folder.** Same check as
   Session 1, but the roster may have moved.
   - HS: <https://drive.google.com/drive/folders/1iNAG8vacKNsL3-c_1e_363R00ZxjgJPM?usp=drive_link>

5. **Print the Session 2 handouts.** Camper notes one per camper, the bad-prompts sheet
   one per pair (it lives inline in the lesson plan), and spec sheets one per camper plus
   spares.

6. **Re-check the live site if you've edited it since.** Settings → Pages → Deploy from
   a branch, `main`, folder `/docs`. Click through home → High School → a session's notes
   → back, and open it on a phone.

## Still your call

**The tone of the "the AI wrote the code" talks** at the end of Sessions 1 and 4. The
most opinionated thing in the curriculum. MS gets two sentences, HS the full paragraph.
You've now delivered the MS version once — if it landed, leave it alone.

**Whether the MS break becomes the default.** It's currently written as "no break
scheduled, take 5 at 0:48 if your group needs one." A break was taken, the session fit,
and the pacing was right — so the note arguably has it backwards. Flipping it means
editing the MS timing table, so it's your call, not a correction.

~~Whether MS gets a topic segment.~~ **Settled: no.** MS Session 1 ran its full 85
minutes and the workload was judged about right, so there is no slack to spend. The
[topic bank](session-1/ai-topics.html) stays HS-only. Anything added to MS displaces
something that's already earning its place.

## Deliberately not done

So nobody "fixes" these by accident.

- **No slides.** Everything is instructor-read.
- **No assessment or rubric.** The showcase is the assessment.
- **No parent-facing summary.** Likely useful; not written.
- **No registration or contact link on the site.** Enrolment is handled elsewhere.
- **Session 2's bad-prompts list is instructor-side only.** The spec sheet from that
  session *is* reproduced in the camper notes, so campers have that one.
- **The OpenCode Zen how-to is footnoted, not fully linked.** `session-1/opencode-zen-howto.md`
  covers using OpenCode's free models so campers can keep coding at home at no cost. As of
  2026-08-10, every "keep building at home" line on the site links to it via a `\*`
  footnote — `middle-school.html`, `session-3/hs-camper-notes.md`,
  `session-4/hs-camper-notes.md`. It is still **not** in `teacher.html`, the main nav, or
  any resource list — that's now a judgment call rather than something still blocked.
  **Update, 2026-08-11:** the free models turn out to need no account, no API key, and no
  provider setup at all — they're available the moment OpenCode is installed. That
  dissolves the earlier CLI-vs-desktop-app split; there's no connect flow to get wrong.
  Confirmed working on a personal Windows 11 machine (2026-08-10) and, this update, on an
  actual CompuCon lab machine (2026-08-11) — the one gating item left. **The only open
  question now is the usage cap:** one user reports hitting 200 requests in a 5-hour
  window, unconfirmed whether that's per-model or total. The doc still intentionally
  breaks the one-command rule (`opencode` vs `claude`), which is why it lives as a
  footnote rather than class material — but that's a smaller departure than before, since
  it no longer breaks the no-accounts / no-API-keys rules too.
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
