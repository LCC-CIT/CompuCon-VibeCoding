# Project Idea Bank

Sorted by how much can go wrong. Project this in Session 1 and keep it up for the rest
of the track.

**Which tier, by age group and session:**

| | MS (85 min sessions) | HS (120/180/180/60) |
|---|---|---|
| **Session 1** build #2 | Starter — but most MS campers customize Mad Libs instead | Starter or Solid |
| **Session 2** spec-first build | Starter | Solid |
| **Session 3** | *No new project* — MS hardens an existing app | Capstone continues (Solid or Stretch) |
| **Session 4** | Capstone — **Starter**, two must-haves max | *No build time* — demos only |

**Starter is a hard ceiling for middle school.** MS has 340 minutes total against HS's
540, and the longest MS build block in the track is 38 minutes. A Solid-tier project
will not finish.

**All of these assume Python + tkinter.** That's deliberate — one language, one GUI
library, no install friction on the Windows lab image, instant visual payoff.

**Campers who already know another stack may use it.** Every idea below works in
HTML/CSS/JS in a browser too, and most work as a plain terminal program. The idea is the
idea; the stack is a detail. See the "different language" entry in
[`troubleshooting.md`](troubleshooting.html) for the two conditions.

---

## Starter — build in 10–20 minutes

**Everything middle school builds comes from this tier**, plus HS's Session 1 build.

| App | What it does | Why it works |
|---|---|---|
| [**Mad Libs**](#mad-libs) | Fill in 5 words, get a funny story | Instant payoff, endlessly customizable |
| [**Dice Roller**](#dice-roller) | Click to roll a d20 | Simplest possible thing that's still fun |
| [**Magic 8-Ball**](#magic-8-ball) | Ask a question, get an answer | Adding your own answers is the hook |
| [**Coin Flip Streak**](#coin-flip-streak) | Flip and track heads/tails counts | Sneaks in real state management |
| [**Compliment Generator**](#compliment-generator) | Random nice thing, on a button | Easy to personalize |
| [**Random Team Picker**](#random-team-picker) | Names in, shuffled groups out | Actually useful — they'll use it |
| [**Color Picker**](#color-picker) | Sliders that change the background live | Very visual, very immediate |
| [**Countdown Timer**](#countdown-timer) | Set minutes, count down, beep | Timing bugs teach a lot |
| [**Rock Paper Scissors**](#rock-paper-scissors) | Play the computer, keep score | Score tracking is the real lesson |
| [**Unit Converter**](#unit-converter) | Miles↔km, F↔C, etc. | Great for wrong-input testing |

---

## Solid — build in 30–60 minutes

**High school only.** HS Session 2's spec-first build, and the smaller end of HS
capstones. Too big for any MS block.

| App | What it does | The interesting part |
|---|---|---|
| [**Quiz Game**](#quiz-game) | Multiple choice, score at the end | Scoring edge cases everywhere |
| [**Todo List**](#todo-list) | Add, check off, delete | Persistence — save to a file |
| [**Pomodoro Timer**](#pomodoro-timer) | 25 work / 5 break, cycles | State machine, real logic |
| [**Flashcards**](#flashcards) | Front/back cards, mark right or wrong | Data structure choice matters |
| [**Password Strength Checker**](#password-strength-checker) | Live feedback as you type | Rules-based scoring, easy to break |
| [**Hangman**](#hangman) | Classic word guessing | Real game logic, win/lose states |
| [**Number Guessing Game**](#number-guessing-game) | Higher/lower with hints | Perfect for teaching input validation |
| [**Habit Tracker**](#habit-tracker) | Check off daily habits, keep streaks | Dates are gloriously bug-prone |
| [**Grade Calculator**](#grade-calculator) | Enter scores, get weighted average | Empty-list bug lives here |
| [**Tip Splitter**](#tip-splitter) | Bill + people + tip % → per person | Division by zero, rounding |
| [**Memory Match**](#memory-match) | Flip cards, find pairs | Grid layout, timing |
| [**Budget Tracker**](#budget-tracker) | Log spending by category | Text file storage, totals |
| [**Study Playlist Timer**](#study-playlist-timer) | Timer that suggests break activities | Combines two ideas |
| [**Text Adventure**](#text-adventure) | Rooms, choices, an ending | Great for data-file separation |

---

## Stretch — 60–90 minutes, some ambition

**High school capstones only** — pitched end of Session 2, built in Session 3. Assume
they'll cut something.

| App | What it does | Why it stretches |
|---|---|---|
| [**Two-Player Battle Game**](#two-player-battle-game) | Turn-based, same keyboard, HP and attacks | Turn logic, state, balance |
| [**Typing Speed Test**](#typing-speed-test) | Type a passage, get WPM and accuracy | Timing + string comparison |
| [**Recipe Scaler**](#recipe-scaler) | Recipe in, scale to N servings | Fractions and units are hard |
| [**Class Schedule Builder**](#class-schedule-builder) | Add classes, detect time conflicts | Real algorithmic thinking |
| [**Simple Drawing App**](#simple-drawing-app) | Draw on a canvas, pick colors, save | Canvas events, file output |
| [**Music Practice Log**](#music-practice-log) | Log sessions, chart weekly minutes | Data over time, simple charting |
| [**Wordle Clone**](#wordle-clone) | 5 letters, 6 guesses, color feedback | The yellow-letter rule is genuinely tricky |
| [**Inventory Manager**](#inventory-manager) | Items, quantities, low-stock alerts | Multi-file, JSON data |
| [**Sports Stat Tracker**](#sports-stat-tracker) | Log games, compute season averages | Real data modeling |
| [**Choose-Your-Own-Story Engine**](#choose-your-own-story-engine) | Story loaded from a data file | Best multi-file project on this list |
| [**Pixel Art Editor**](#pixel-art-editor) | Grid of cells, click to color, export | Grid math, save/load |
| [**Sorting Visualizer**](#sorting-visualizer) | Watch bubble sort run step by step | Animation + a real CS concept |

---

## Project Descriptions

One paragraph each — enough to picture the screen and start building. The names in the
tables above link here.

### Starter

#### Mad Libs

Fill in a few words, get a silly story back. The classic first build — quick to finish,
easy to make funnier.

#### Dice Roller

A big button. Click it, get a number. Add sounds, colors, or a list of your last rolls.

#### Magic 8-Ball

Type a question, get a mysterious answer. Writing your own answers is the fun part.

#### Coin Flip Streak

Flip a coin and count heads versus tails. Simple, but the counting gets interesting.

#### Compliment Generator

A button that says something nice. Personalizing the compliments is where it gets good.

#### Random Team Picker

Type in names, get shuffled groups back. Actually useful — campers will use it to split
into teams.

#### Color Picker

Sliders that change the window's color as you move them. Instant visual payoff.

#### Countdown Timer

Set minutes, watch it count down, get beeped at zero. Timing is harder than it looks.

#### Rock Paper Scissors

Play the computer and keep score. The scorekeeping is the real lesson.

#### Unit Converter

Miles to kilometers, Fahrenheit to Celsius, anything. Great for finding wrong-input bugs.

### Solid

#### Quiz Game

Multiple-choice questions with a score at the end. Everything that can go wrong with
scoring lives here.

#### Todo List

Add tasks, check them off, delete them. Save to a file so the list survives a restart.

#### Pomodoro Timer

Twenty-five minutes of work, five-minute break, on a loop. Real logic, real state.

#### Flashcards

Front of a card, back of a card, mark it right or wrong. The card data structure matters.

#### Password Strength Checker

Type a password, get a rating as you type. Rules you can break.

#### Hangman

Guess the word before you run out of tries. Real game logic with win and lose states.

#### Number Guessing Game

It picks a number, you guess higher or lower. Perfect for learning input checking.

#### Habit Tracker

Check off daily habits and keep a streak going. Dates are gloriously buggy.

#### Grade Calculator

Enter scores, get a weighted average. An empty list breaks it — good.

#### Tip Splitter

Bill, people, tip percent, cost per person. Division by zero and rounding live here.

#### Memory Match

Flip cards and find the pairs. Grids and timing.

#### Budget Tracker

Log spending by category and see totals. Store everything in a text file.

#### Study Playlist Timer

A timer that suggests break activities. Two ideas in one app.

#### Text Adventure

Rooms, choices, an ending. Great for separating the story from the code.

### Stretch

#### Two-Player Battle Game

Turn-based combat, two players, one keyboard. HP, attacks, balance.

#### Typing Speed Test

Type a passage and get words-per-minute and accuracy. Timing plus string comparison.

#### Recipe Scaler

Put in a recipe and scale it to any number of servings. Fractions are genuinely hard.

#### Class Schedule Builder

Add classes and find time conflicts. Real algorithmic thinking.

#### Simple Drawing App

Draw on a canvas, pick colors, save your art. Canvas events and file output.

#### Music Practice Log

Log practice sessions and chart your weekly minutes. Data over time.

#### Wordle Clone

Five letters, six guesses, color feedback. The yellow-letter rule is sneaky.

#### Inventory Manager

Items, quantities, low-stock alerts. Multi-file, JSON data.

#### Sports Stat Tracker

Log games and compute season averages. Real data modeling.

#### Choose-Your-Own-Story Engine

A story loaded from a data file. The best multi-file project here.

#### Pixel Art Editor

A grid of cells, click to color, export. Grid math, save and load.

#### Sorting Visualizer

Watch bubble sort run step by step. Animation plus a real CS concept.

---

## Good For Specific Lessons

Reach for these when you want to teach a particular thing.

| Lesson | Use this |
|---|---|
| **Wrong-input testing** | Unit Converter, Grade Calculator, Tip Splitter |
| **Splitting into files** (HS only) | Choose-Your-Own-Story Engine, Quiz Game |
| **Saving data** | Todo List, Habit Tracker, Budget Tracker |
| **The AI's code runs but is wrong** | Grade Calculator (empty list), Wordle (duplicate letters) |
| **Scope cutting** | Anything a camper describes as "like [big famous app]" |
| **They'll actually use it** | Random Team Picker, Todo List, Class Schedule Builder |

---

## Ideas To Steer Away From

Not because they're bad — because they burn the session on setup instead of the skills.

| They'll ask for | Why it stalls | Redirect to |
|---|---|---|
| A Discord/Instagram bot | API keys, accounts, rate limits, permissions | Same logic as a local app |
| A multiplayer online game | Networking eats the entire session | Two players, one keyboard |
| An iPhone app | Toolchain, signing, a Mac | Desktop app with the same idea |
| Anything with a login system | Auth is a rabbit hole with no payoff here | One user, data in a file |
| "An AI that ___" | They mean training a model. Won't finish. | Rules-based version of the same idea |
| A 3D game | Engine setup, assets, physics | 2D version, or top-down |
| Something scraping a website | Network access, blocked sites, brittle | Local data file with the same shape |

**The redirect script:**

> "That's a great idea and it's a real project — it's just a *ten hour* project, and most
> of those hours are setup that teaches you nothing. What's the version of that which
> runs on this machine, right now, with no accounts? Build that. If it's good, the big
> version is a summer project."

---

## Instructor Note: Letting Campers Bring Their Own

Always allow it. Sign it off against three questions:

1. **Can I picture the screen?** If they can't describe what it looks like, it's not
   ready.
2. **Does it need anything but Python?** Accounts, keys, internet, other people — cut it
   or redirect.
3. **What's the smallest version that's still the same idea?** Build that one.

A camper building their own idea badly is learning more than a camper building your
idea well. Protect that — just protect them from reaching the showcase with nothing to
demo.

**Be strictest in MS Session 4.** It's the only MS session with a self-chosen project,
and there are 38 minutes to build it. "Rebuild my Session 1 app, better" is a completely
legitimate answer for anyone who can't settle on something.
