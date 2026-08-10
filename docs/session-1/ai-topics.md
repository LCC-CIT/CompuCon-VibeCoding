# Session 1 Extension — AI Topics (Draft)

**Draft. Not taught yet, not timed with real campers.** Six short teaching segments,
each followed by a build. Written after the first HS Session 1 ran in about 60 minutes
against a 120-minute plan.

**High school only.** MS Session 1 is 85 minutes and is the entire middle school track.
It has now been delivered: it used all 85 minutes, took a break, and the workload was
judged about right — so there is measurably no slack in it. Nothing here goes to middle
school.

Each segment is one idea about AI, said out loud in under seven minutes, followed by
campers building something with Claude Code that makes the idea concrete. The build is
not decoration. In every case the app is the argument.

---

## Contents

- [How To Use This](#how-to-use-this)
  - [The time you actually have](#the-time-you-actually-have)
  - [Pick three](#pick-three)
  - [Where each segment fits](#where-each-segment-fits)
  - [The setup, once](#the-setup-once)
- [Segment 1 — What It's Actually Doing (6 min talk / 14 min build)](#segment-1-what-its-actually-doing-6-min-talk-14-min-build)
  - [The talk](#the-talk)
  - [The build](#the-build)
  - [The check](#the-check)
  - [If you're running long](#if-youre-running-long)
- [Segment 2 — Confident Wrongness (6 min talk / 14 min build)](#segment-2-confident-wrongness-6-min-talk-14-min-build)
  - [The talk](#the-talk-1)
  - [The build](#the-build-1)
  - [The check](#the-check-1)
- [Segment 3 — Bias Is Inherited, Not Invented (7 min talk / 13 min build)](#segment-3-bias-is-inherited-not-invented-7-min-talk-13-min-build)
  - [The talk](#the-talk-2)
  - [The build](#the-build-2)
  - [The check](#the-check-2)
- [Segment 4 — What You Paste Is Not Private (5 min talk / 15 min build)](#segment-4-what-you-paste-is-not-private-5-min-talk-15-min-build)
  - [The talk](#the-talk-3)
  - [The build](#the-build-3)
  - [The check](#the-check-3)
- [Segment 5 — The True Cost (7 min talk / 13 min build)](#segment-5-the-true-cost-7-min-talk-13-min-build)
  - [The talk](#the-talk-4)
  - [The build](#the-build-4)
  - [The check](#the-check-4)
- [Segment 6 — What It's Genuinely Good At (6 min talk / 14 min build)](#segment-6-what-its-genuinely-good-at-6-min-talk-14-min-build)
  - [The talk](#the-talk-5)
  - [The build](#the-build-5)
  - [The check](#the-check-5)
- [Instructor Prep Checklist](#instructor-prep-checklist)

## How To Use This

### The time you actually have

HS Session 1 is budgeted at 120 minutes. The first delivery finished in about 60 — while
the MS group used all 85 of theirs. The HS estimate, not the content, was wrong. That
leaves roughly an hour, which is **three segments, not six.**

| | Talk | Build | Total |
|---|---|---|---|
| One segment | 5–7 min | 13–15 min | 20 min |
| Three segments | | | 60 min |

Treat this file as a bank. Teach three, keep the rest for the next group that runs fast.
Two segments plus a longer Build #2 is also a fine answer.

**Watch the ratio.** The track runs at roughly 20% talking, 80% building. A segment at
6 and 14 holds that line. A segment at 10 and 10 does not — and the failure mode when
you're standing in front of a room with time left over is always to talk more. If a talk
is running long, cut it and let the build carry the idea.

### Pick three

If you want a default: **Segment 1, Segment 2, and one values topic.** Segment 1 explains
the mechanism, Segment 2 turns it into a habit, and the third makes it matter. Segment 4
lands hardest with high schoolers because it is about them and it is immediately
actionable.

The six are deliberately not all warnings. Segment 6 exists so the session doesn't teach
cynicism instead of judgment — a room that leaves thinking "AI bad" learned as little as
a room that leaves thinking "AI magic."

### Where each segment fits

Slot these into the existing HS block sequence in
[`lesson-plan.html`](lesson-plan.html). They are modular — no fixed clock position — but
some sit better in some places than others.

| Segment | Best slot | Why |
|---|---|---|
| 1 — What It's Actually Doing | After *What Just Happened* | Answers the question they just formed |
| 2 — Confident Wrongness | After *The AI Was Wrong* | Turns the demo into a method |
| 3 — Bias Is Inherited | After Build #2 | Needs them fluent with the tool first |
| 4 — What You Paste | Anywhere after Build #1 | Self-contained |
| 5 — The True Cost | After Build #2 | Self-contained, good pre-showcase cooldown |
| 6 — What It's Good At | Last, before the showcase | Ends on capability, not dread |

### The setup, once

Campers make one folder for the segment builds and stay in it:

```powershell
cd $HOME\Documents\Projects
cd <Name>
mkdir ai-topics
cd ai-topics
claude
```

`<Name>` is their name folder from setup. Each segment build is a new file in this one
folder — no new folder per segment, there isn't time.

Everything here is Python + tkinter. No installs, no accounts, no API keys, no network
calls from any app they build. Where a segment says "ask Claude for X," they ask it in
the terminal and read the answer themselves — nothing in their app talks to a model.

---

## Segment 1 — What It's Actually Doing (6 min talk / 14 min build)

The most valuable six minutes in this file. It converts the whole track's thesis from a
moral warning into a mechanical fact they can hold in their hands.

### The talk

Start with the thing in their pocket.

> "Your phone suggests the next word when you type. This is that. Trained on a library
> instead of your group chat, but that is the mechanism, not a simplification of it."

Then the part that does the work:

> "It doesn't look anything up. There's no drawer of facts in there to open. It produces
> the word that most plausibly comes next, then does it again, and again. Everything it
> says is a very good guess about what a sentence like this usually sounds like."

Land it:

> "So when it's right, it's right because true things are common in what it read. That
> works most of the time. Notice that 'most of the time' is doing a lot of work in that
> sentence."

Mention randomness briefly — same prompt, different answers, because it samples rather
than always picking the single likeliest word. Don't use the word "temperature" unless
someone asks; it costs a minute and buys nothing.

### The build

They build a toy version of the thing they've been using all session.

> Build a Python tkinter app. It reads a text file called `source.txt`, learns which
> words tend to follow which other words, and shows 3 made-up sentences when I click a
> Generate button. Save it as `predictor.py`

They need a `source.txt` with real text in it — song lyrics, a chapter they paste in,
the text of anything long enough. **Under about 500 words the output is gibberish and
the point doesn't land.** Have a long text file ready on a share for anyone stuck.

### The check

Two questions, in this order:

1. **Click Generate twice. Why is it different both times?** They just built the
   randomness they saw all session.
2. **Is anything it said true?** Then: where in this program would truth even come from?
   Walk them through their own code — there is no step where truth could enter. There
   isn't one in the real thing either. It's the same shape, with a much bigger pile of
   text.

> "You just built the world's dumbest language model, and it has the same hole in it as
> the smart one. The smart one is better at hiding it."

### If you're running long

Cut the second Generate-twice discussion. Keep question 2 — it's the entire segment.

---

## Segment 2 — Confident Wrongness (6 min talk / 14 min build)

Pairs directly with the *AI Was Wrong* block. That block shows them one error. This one
makes them measure the error rate themselves.

### The talk

> "It has no idea when it doesn't know. There's no light that comes on. Confidence and
> accuracy are two separate dials, and only one of them is turned up."

The useful distinction:

> "It's not lying. Lying takes knowing the truth and choosing something else. It's
> producing the most plausible-sounding answer, and a plausible-sounding wrong answer
> looks exactly like a plausible-sounding right one. That's the problem. Not that it's
> wrong sometimes — that being wrong doesn't *look* like anything."

Give them the only reliable defense:

> "Ask it about things you can check. Then check them."

### The build

A scoreboard for the AI's accuracy, using questions only they can grade.

> Build a Python tkinter app that keeps score. I type a question and click Right or
> Wrong. It shows a running list and a percentage at the top. Save it as
> `factcheck.py`

Then they do the actual work: ask Claude ten checkable questions about something they
know cold — their town, a game they play, the rules of a sport, their school — verify
each answer themselves, and log it.

**Questions have to be checkable by them, not googleable in theory.** "What's the
capital of France" teaches nothing. "How many stops are on the number 11 bus" teaches
plenty.

### The check

Pool the class numbers on the board. Then:

- **If accuracy is low**, ask which questions it missed. It will be the specific, local,
  recent ones. That's a pattern worth naming: it's weakest exactly where you're strongest.
- **If accuracy is high** — and it often will be — that's a real finding, don't spin it.
  Say so, then push: get more obscure, more recent, more local. Find the edge. Finding
  where the edge *is* is more useful than assuming it's everywhere.

Also break the app: what does it show when nothing has been logged yet? A percentage of
zero out of zero is a divide-by-zero waiting to happen, and most of them will have one.

---

## Segment 3 — Bias Is Inherited, Not Invented (7 min talk / 13 min build)

The longest talk of the six, because the easy version of this topic is wrong and the
wrong version is worse than not teaching it.

### The talk

> "It learned patterns from an enormous amount of text that people wrote. If we wrote
> something lopsided, it learned something lopsided. Nobody typed the bias in. It got
> inherited."

Make sure the "nobody's fault" framing doesn't become "nobody's problem":

> "That sounds like it lets everyone off the hook. It doesn't. If a hiring tool learned
> from twenty years of who got hired, and twenty years of hiring was skewed, then the
> tool is skewed — and it's now skewed at enormous speed, with a computer's reputation
> for being objective attached to it. Nobody has to be a villain for that to hurt
> somebody real."

Then the honest caveat, which is also a lesson:

> "Companies know about this and tune against it. So you might test for it and find
> less than you expected. That's worth knowing too — 'I looked and it wasn't there' is
> a real result, as long as you actually looked."

### The build

> Build a Python tkinter app that counts things. I type a label, click Add, and it keeps
> a tally of how many times each label came up. Show the counts as a list. Save it as
> `tally.py`

Then the data collection: ask Claude for twenty short character descriptions for a job —
surgeon, kindergarten teacher, CEO, nurse, coach — and tally an attribute across them.
Pairs work well here; different pairs take different jobs.

### The check

The verification lesson here is about **the evidence, not the app**:

1. **Is twenty enough to conclude anything?** Push on this. It isn't, really.
2. **What result would have changed your mind?** If they can't answer that, they weren't
   testing, they were confirming.
3. **Did the wording of your request steer the answer?** Have a pair re-run it with a
   deliberately neutral phrasing and compare.

> "You just ran an experiment on a system nobody fully understands, with a sample size
> of twenty, and got a result. That's roughly how most claims about AI you'll read
> online were produced. Hold yours to a higher standard than they do."

---

## Segment 4 — What You Paste Is Not Private (5 min talk / 15 min build)

Shortest talk, longest build, most immediately useful thing in this file. Lands hardest
because it's about them and they can act on it today.

### The talk

Keep it concrete and non-preachy. They tune out lectures about internet safety and they
should — most are useless.

> "Assume anything you type into a chatbot could be read by a person someday. Not
> definitely. Assume it. Now decide what you're willing to type."

The specifics that matter:

- Passwords, ever, for any reason
- Medical details — yours or anybody's
- **Other people's information.** Their friend didn't agree to this.
- School work you've been told to keep off third-party services

> "The one that gets people isn't passwords. It's pasting a whole group chat in to ask
> what someone meant. Four other people are in that message and none of them were asked."

### The build

A tool that finds personal information hiding in a block of text.

> Build a Python tkinter app with a big text box. When I click Scan, it finds phone
> numbers, email addresses, and any 9-digit numbers, and shows them in a list below.
> Save it as `scrubber.py`

Fast finishers add a Redact button that replaces each find with `[REMOVED]`.

### The check

This is the best edge-case playground in the file. Give them the list:

- A phone number written `541-555-0182`, `(541) 555-0182`, and `5415550182`
- An email in the middle of a sentence, with a period right after it
- A year like `1999` — does it flag it? Should it?
- A nine-digit order number that isn't an ID at all

Then swap machines and try to slip something past a partner's scrubber. **A tool that
catches most personal information is a tool that quietly reassures you about the parts
it missed** — that's worth saying out loud, because it's true of a lot of safety
software they'll meet later.

---

## Segment 5 — The True Cost (7 min talk / 13 min build)

Covers the environmental footprint and the human labor together, because separately each
is a five-minute talk with a two-minute build and together they're one good segment.

### The talk

> "It feels like magic partly because everything expensive about it is out of frame."

Two things out of frame:

**The physical side.** Data centers are buildings — real ones, drawing real power, often
cooled with real water, sited in real places where those things were already contested.

**The human side.**

> "Somebody labeled the training data. Somebody sat and rated thousands of answers so it
> would learn which ones people prefer. Somebody moderated the worst material on the
> internet so that it wouldn't come back to you. That work is real, it's often
> outsourced and low-paid, and the whole point of it is that you never notice it."

**Do not assert specific figures from the front of the room.** Energy and water numbers
per prompt vary enormously by model, hardware, and data center, and a lot of the ones in
circulation are shaky or badly out of date. Say that. It's the honest position and it
sets up the build.

### The build

> Build a Python tkinter app. I type how many AI prompts I send per day, and it shows me
> estimated energy use, water use, and human labor behind that, per year. Put the numbers
> I give it in clearly-labeled variables at the top. Save it as `truecost.py`

The variables at the top matter — they need to be able to see and change the assumptions
their app is built on.

### The check

The whole segment lives here:

1. **Ask Claude for the figures.** It will produce confident, specific, plausible numbers.
2. **Now verify one of them.** Ask it where that number came from. Ask for the source.
   Ask what year it's from. Ask whether it's per prompt or per training run — those
   differ by orders of magnitude and get conflated constantly.
3. **Change one assumption and watch the output move.** If a 3x change in one input
   swings the answer 3x, how much does the answer actually tell you?

> "Your app is now producing confident numbers on a screen, which is the most convincing
> format there is. It's exactly as trustworthy as the number you typed at the top and
> nothing more. Remember that the next time you see a statistic in a nice font."

---

## Segment 6 — What It's Genuinely Good At (6 min talk / 14 min build)

Put this last. A session that only lists harms produces cynicism, and cynicism is just
credulity pointed the other way — neither one is judgment.

### The talk

> "Everything worth worrying about is worth worrying about because it's powerful. Point
> the same power somewhere else and you get the biggest jump in accessibility technology
> in a decade."

Concrete examples, not abstractions:

- Live captioning that actually keeps up with a fast talker
- Translation good enough to follow a class in a language you're still learning
- Screen reading and text description for people who can't see the screen
- Simplifying dense text for someone with dyslexia or a reading difficulty
- Describing a photo to someone over the phone

> "A kid who couldn't read the textbook can now read the textbook. That's not a
> consolation prize for the other stuff. It's just also true."

### The build

> Build a Python tkinter app that helps someone read a hard piece of text. It has a big
> text box I can paste into, a button to make the text much bigger, a button for high
> contrast, and a button that shows one sentence at a time. Save it as `readingtool.py`

### The check

Different from the others, and better: **hand it to a partner and make them actually use
it for two minutes** on a genuinely dense piece of text. Have a paragraph of something
hard ready — a terms of service, a dense paragraph from a science article.

Then ask the partner, not the builder:

- Did that help, or did it just look like it helped?
- What did you want it to do that it didn't?

> "You just did user testing. The person who built it is the worst possible judge of
> whether it works, because they know what it's supposed to do. Everyone in this room
> just found that out in two minutes."

---

## Instructor Prep Checklist

- [ ] **Decide which three** before the day, not during it — see [Pick three](#pick-three)
- [ ] Have a long text file (500+ words) on a share for Segment 1 stragglers
- [ ] Test each build yourself once — 14 minutes is tight and you need to know where
      campers will get stuck
- [ ] Segment 2: have three or four example "checkable questions" ready for campers who
      can't think of one
- [ ] Segment 3: decide which jobs each pair tallies, so you get a spread
- [ ] Segment 4: print the edge-case list, or put it on the board
- [ ] Segment 5: **do not prepare figures to assert.** Prepare to say the numbers are
      contested and have campers source them
- [ ] Segment 6: have a genuinely dense paragraph ready for the partner test
- [ ] Confirm `Documents\Projects` and each camper's `<Name>` folder still exist from
      setup — these builds assume both

------

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/) This Vibe Coding Curriculum by [Brian Bird](https://profbird.dev), created in <time>2026</time> with AI assistance, is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
