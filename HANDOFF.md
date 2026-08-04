# Handoff Notes

State of the curriculum as of **4 August 2026**. Written so the reasoning doesn't live
only in a chat log.

**Status: complete draft, rebuilt against the real schedule, unreviewed and untaught.**
All four session files have separate MS and HS timing tables that sum correctly. Git has
been removed throughout. Nothing has been tested on a real machine or in front of a real
classroom.

---

## The schedule this is built for

| | Session 1 | Session 2 | Session 3 | Session 4 | Total |
|---|---|---|---|---|---|
| **Middle school** | 85 min | 85 min | 85 min | 85 min | 340 min (5h40m) |
| **High school** | 120 min | 180 min | 180 min | 60 min | 540 min (9h) |

All figures are **actual teaching time** — arrival and attendance are already excluded.

An earlier draft assumed four uniform 3-hour sessions for both groups. That was wrong,
and correcting it forced three structural decisions, all now implemented:

**1. MS drops multi-file projects entirely.**
With 340 minutes against HS's 540, MS couldn't teach planning, file splitting, and
building in 85 minutes without doing all three badly. MS Session 3 became *Make It
Solid* — save points, debugging method, and hardening a single-file app against bad
input. The verification spine is preserved; the architecture content is gone.

**2. The HS capstone moved to Sessions 2–3.**
HS Session 4 is 60 minutes, which is not a build day. HS now pitches the capstone in the
last 40 minutes of Session 2 (after the prompting and verification content) and finishes
it during Session 3's 75-minute build block. Session 4 is demos, reflection, and
where-to-next, with a 10-minute setup block whose only purpose is letting a student
restore a working copy if their app won't launch.

**3. MS does its whole capstone inside Session 4.**
85 minutes: 12 for pitch and scope check, 38 to build, 10 to polish, 20 to demo, 5 to
wrap. The aggressive scope check at the start is what makes this work — two must-haves
maximum, and "rebuild my Session 1 app, better" is a pre-approved fallback.

### Git is out

Students don't use version control. Save points are folder copies:

```powershell
cd $HOME\Documents
Copy-Item -Recurse myproject myproject-working    # save
Remove-Item -Recurse myproject                    # undo, step 1
Copy-Item -Recurse myproject-working myproject    # undo, step 2
```

Taught in `day-3.md` to both age groups, with the File Explorer equivalent offered
alongside. `troubleshooting.md` has a "Save Point / Undo Problems" section covering the
failure modes — file locks, reversed argument order, copies nested inside the project.

For HS this doubles as a verification tool: keep the old copy, open both files side by
side, and you have a diff by hand. That's Session 2's check #3 made concrete.

### PowerShell

Lab machines may run 5.1 or 7. 5.1 doesn't support `&&` and there's no way to tell which
a given machine has, so every command in the curriculum is one per line. That syntax
works on both.

---

## How the files are organized

**Sessions 1–2** share one block sequence across age groups, with dual durations in each
heading (`## Hook (MS 8 min / HS 10 min)`) and `MS/HS` callouts where the content within
a block diverges. HS Session 2 has three extra blocks at the end (break, capstone pitch,
capstone kickoff) that MS skips.

**Sessions 3–4** split into `# MIDDLE SCHOOL` and `# HIGH SCHOOL` sections in the same
file, each with its own block sequence. The content differs too much for a shared
outline.

Both timing tables live at the top of each file. Check both after any edit.

---

## Decisions made, and why

Reversible, but don't reverse them by accident.

### Session 1 stands alone, for both age groups

It has to work for a student who never comes back. Ends with a working app, a gallery
walk, and a take-home summary. This is a tighter constraint under the new schedule than
the old one — MS has 85 minutes to deliver a complete experience.

### Verification is the spine

The thing that makes this a curriculum rather than a demo. It escalates:

| Session | MS | HS |
|---|---|---|
| 1 | "The AI was wrong" — a quiz scorer that runs and is wrong | Same, plus writing the fixes |
| 2 | Checks 1–2, "be a jerk to your app" | All four checks, levels 0–4, swap-and-break |
| 3 | Hardening block: break your own app systematically | Folder copies as a hand-rolled diff |
| 4 | Demo requires naming one thing that broke | Demo requires naming one thing the AI got wrong |

If time pressure forces cuts — and MS's 340-minute total means it will — cut elsewhere.

### Python + tkinter as the default

Zero install friction on the Windows image, and a window on screen inside 60 seconds.
The visual payoff matters enormously for holding a room of teenagers.

Students who already know another stack may use it (instructor's call, two conditions
recorded in `troubleshooting.md`). Examples stay Python + tkinter.

### Teaching Claude Code features only when they're needed

`/clear` appears in MS Session 3 as an escape hatch when the AI is making things worse,
and in HS Session 3 alongside `CLAUDE.md` and file-targeting. A feature tour on Session 1
would be forgotten by Session 3.

### Blunt honesty about what students did and didn't do

Sessions 1 and 4 both end with a version of *"the AI wrote the code; here's what that
does and doesn't mean."* Deliberate — it heads off both overclaiming and the quiet
suspicion that they cheated. **Flagged for your review:** it's the most opinionated call
in here and the tone is yours to set. The MS version is trimmed to two sentences; the HS
version is the full paragraph.

---

## Unverified — treat as assumptions, not facts

Nothing below was tested. The workspace VM wouldn't boot during drafting, so all
verification was done by hand.

| Assumption | Risk if wrong |
|---|---|
| `cc-ds` launches and works on the lab image | Session 1 doesn't happen |
| `cc` works for Claude Pro students | Minor; they fall back to `cc-ds` |
| `python -c "import tkinter"` succeeds | Every example breaks |
| Lab machines run PowerShell 5.1 or 7 | Command syntax notes need revisiting |
| `Copy-Item -Recurse` / `Remove-Item -Recurse` behave as documented under lab permissions | The entire save-point system breaks |
| Session lengths are exact and don't shrink in practice | Timing tables need rework |
| ~20 students per session | HS Session 4's 30-minute showcase assumes ~20 × 90 sec |

**Highest-value next action: run the Session 1 prep checklist on a real lab laptop, and
walk the full save-point cycle yourself.** Ten minutes, de-risks most of the above.

That last row matters more than it looks. HS Session 4 has 30 minutes of demo time. At
90 seconds each that's 20 students with zero slack. If sessions are larger, either cut to
60 seconds or run part of it as a gallery walk — decide before the day, not during it.

---

## Known gaps

Things deliberately not done, so nobody "fixes" them by accident.

- **No slides.** Everything is instructor-read. If CompuCon wants slides, Session 1 is
  the only one that really warrants them.
- **No assessment or rubric.** The showcase is the assessment.
- **No parent-facing summary.** Likely useful; not written.
- **No pre-written demo code.** Instructors generate `dice.py` live in Session 1. That's
  the point of the opening, but it means being comfortable improvising.
- **Timing tables are theoretical.** Every block sums correctly; no block has been run
  with real students. Expect the first delivery to run long.
- **MS has no scheduled breaks.** All four MS sessions are 85 minutes straight. Each file
  has a note on where to take 5 minutes and what to cut for it, but the decision is the
  instructor's and should be made before the session, not during.
- **The Session 2 bad-prompts handout and spec sheet are inline in `day-2.md`,** not
  separate printable files.
- **`project-ideas.md` hasn't been re-tiered since the MS cuts.** The Starter tier is now
  effectively a hard ceiling for MS rather than a recommendation. Worth a pass.

---

## Suggested next steps, in order

1. **Verify the environment** on a real lab laptop — `cc-ds`, tkinter, PowerShell
   version, and the full `Copy-Item` / `Remove-Item` save-point cycle
2. **Read MS Session 1 aloud with a timer.** 85 minutes is the tightest budget in the
   track and the one that must land perfectly, since it's standalone
3. **Confirm the expected class size** and adjust HS Session 4's showcase format if it's
   above ~20
4. **Decide the MS break policy** for all four sessions
5. **Re-check `project-ideas.md` tiers** against MS's reduced scope
6. **Decide the tone** of the "the AI wrote the code" talks — soften, sharpen, or keep
7. **Print `prompt-cheat-sheet.md`** double-sided and confirm it fits on one sheet
8. **Pull the Session 2 handouts into printable files** if you want them separate

---

## Notes for whoever edits next

Read `CLAUDE.md` — hard constraints and writing conventions.

Failure modes to watch for:

**Breaking a timing table.** There are now eight of them (two per file). If a block
grows, another shrinks, and the table gets updated — for the correct age group. This is
still the easiest thing to silently invalidate.

**Re-adding multi-file content to MS.** It was cut deliberately, not overlooked. MS
Session 3 is *Make It Solid*, and the 85-minute budget doesn't survive putting
architecture back in.

**Adding build time to HS Session 4.** It's 60 minutes of demos. The capstone is finished
in Session 3. If HS students routinely arrive at Session 4 with unfinished projects,
that's a signal to cut scope harder at the Session 2 pitch, not to add build time.

**Adding lecture.** The target is ~20% talking, 80% building. This gets harder to hold
under tight budgets, not easier — the instinct under time pressure is to explain faster
rather than cut content, which is backwards. Cut content.

**Leaving git in.** Grep for `git` before calling any file done. It should only appear
inside an explanation of why it was removed.

One more: the curriculum repeatedly tells students to cut scope, ship something small
that works, and test before adding more. Material that violates its own advice reads
badly to instructors. Keep additions small and verified.
