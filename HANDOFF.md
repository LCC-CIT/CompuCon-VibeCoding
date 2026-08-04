# Handoff Notes

State of the curriculum as of **4 August 2026**. Written at the end of the drafting
session so the reasoning doesn't live only in a chat log.

**Status: complete first draft, unreviewed and untaught.** Every session file is
finished and internally consistent. Nothing has been tested on a real machine or in
front of a real classroom.

---

## Decisions made, and why

Reversible, but don't reverse them by accident.

### Four days, Day 1 standalone

Day 1 carries the most design weight because it has to work for a student who never
comes back. It ends with a finished app, a showcase, and a take-home summary. Days 2–4
assume Day 1 but each opens with a way to absorb newcomers.

### Verification is the spine

The thing that makes this a curriculum rather than a demo. It escalates:

| Day | Verification content |
|---|---|
| 1 | "The AI was wrong" — a quiz scorer that runs perfectly and is wrong |
| 2 | The four checks; levels 0–4 of "checked"; swap-and-break with a partner |
| 3 | `git diff` as a verification tool; the debugging method |
| 4 | Testing built into the spec before code exists |

If time pressure forces cuts, cut elsewhere. This is the part students can't get from a
YouTube tutorial.

### Python + tkinter as the default

Zero install friction on the Windows image, and a window on screen inside 60 seconds.
The visual payoff matters enormously for holding a room of teenagers.

Students who already know another stack may use it (instructor's call, recorded in
`troubleshooting.md` with two conditions). Examples stay Python + tkinter.

### One curriculum, MS/HS callout boxes

Middle and high school run separately but the arc is identical — only ambition and
pacing change. Two full curricula would double maintenance for material that's ~85%
shared.

### Teaching Claude Code features only when they're needed

`/clear` and `CLAUDE.md` appear on Day 3, when projects are finally big enough for the
problems they solve to be real. A feature tour on Day 1 would be forgotten by Day 3.

### Blunt honesty about what students did and didn't do

Days 1 and 4 both end with a version of *"the AI wrote the code; here's what that does
and doesn't mean."* Deliberate — it heads off both overclaiming and the quiet suspicion
that they cheated. **Flagged for your review:** it's the most opinionated call in here
and the tone is yours to set.

---

## Unverified — treat as assumptions, not facts

Nothing below was tested. The workspace VM wouldn't boot during the drafting session, so
all verification was done by hand.

| Assumption | Risk if wrong |
|---|---|
| `cc-ds` launches and works on the lab image | Day 1 doesn't happen |
| `cc` works for Claude Pro students | Minor; they fall back to `cc-ds` |
| `python -c "import tkinter"` succeeds | Every example breaks |
| `git` is installed | Day 3's save-points block breaks |
| Git identity is preconfigured | First commit prompts, ~5 min of chaos |
| Windows PowerShell 5.1 is the default shell | Command syntax notes may be unnecessary |
| A 3-hour block actually has 3 hours of teaching time | Every timing table is off |

**Highest-value next action: run the Day 1 prep checklist on a real lab laptop.** It
takes ten minutes and de-risks most of the above.

That last row is worth thinking about. If the 3 hours includes arrival, attendance, or a
camp-wide activity, every day loses 10–20 minutes and the timing tables need rework.
Day 4's build blocks have the most slack.

---

## Known gaps

Things deliberately not done, so nobody "fixes" them by accident.

- **No slides.** Everything is instructor-read. If CompuCon wants slides, Day 1 is the
  only session that really warrants them.
- **No assessment or rubric.** Not clear the camp wants one. The showcase is the
  assessment.
- **No parent-facing summary.** Likely useful; not written.
- **No pre-written demo code.** Instructors generate `dice.py` live on Day 1. That's the
  point of the opening — but it means the instructor must be comfortable improvising.
- **Timing tables are theoretical.** Every block sums correctly, but no block has been
  run with real students. Expect the first delivery to run long.
- **The Day 2 six-bad-prompts handout and the spec sheet are inline in `day-2.md`,** not
  separate printable files.

---

## Suggested next steps, in order

1. **Verify the environment** on a real lab laptop (see the table above)
2. **Read Day 1 end to end out loud, with a timer.** It's the session most likely to run
   long and the only one that must land perfectly
3. **Decide the tone** of the "the AI wrote the code" talks — soften, sharpen, or keep
4. **Print `prompt-cheat-sheet.md`** double-sided and check it actually fits on one sheet
5. **Pull the Day 2 handouts into printable files** if you want them separate
6. Consider a dry run of the Day 1 opening demo — the 6-minute build is the hook for the
   entire track and it's live-coded

---

## Notes for whoever edits next

Read `CLAUDE.md` — it has the hard constraints and the writing conventions.

Two failure modes to watch for:

**Adding lecture.** The target is ~20% talking, 80% building. Every expansion instinct
pushes toward more explanation. Resist it; if something needs explaining, look for a way
to make students discover it instead.

**Breaking the timing tables.** They're the easiest thing to silently invalidate. If a
block grows, another shrinks, and the table gets updated. Check the arithmetic.

One more: the curriculum repeatedly tells students to cut scope, ship something small
that works, and test before adding more. Material that violates its own advice reads
badly to instructors. Keep additions small and verified.
