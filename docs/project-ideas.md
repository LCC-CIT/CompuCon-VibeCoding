# Project Idea Bank

Sorted by how much can go wrong. Project this in Session 1 and keep it up for the rest
of the track.

**Which tier, by age group and session:**

| | MS (one 85 min session) | HS (120/180/180/60) |
|---|---|---|
| **Session 1** build #2 | Starter — but most MS campers customize Mad Libs instead | Starter or Solid |
| **Session 2** spec-first build | — MS track has ended | Solid |
| **Session 3** | — | Capstone continues (Solid or Stretch) |
| **Session 4** | — | *No build time* — demos only |

**Starter is a hard ceiling for middle school.** MS is a single 85-minute session with
one ~22-minute build block in it. Anything above Starter will not finish.

**All of these assume Python + tkinter.** That's deliberate — one language, one GUI
library, no install friction on the Windows lab image, instant visual payoff.

**Campers who already know another stack may use it.** Every idea below works in
HTML/CSS/JS in a browser too, and most work as a plain terminal program. The idea is the
idea; the stack is a detail. See the "different language" entry in
[`troubleshooting.md`](troubleshooting.html) for the two conditions.

---

## Contents

- [Starter — build in 10–20 minutes](#starter-build-in-1020-minutes)
- [Solid — build in 30–60 minutes](#solid-build-in-3060-minutes)
- [Stretch — 60–90 minutes, some ambition](#stretch-6090-minutes-some-ambition)
- [Project Descriptions](#project-descriptions)
  - [Starter](#starter)
    - [Mad Libs](#mad-libs)
    - [Dice Roller](#dice-roller)
    - [Magic 8-Ball](#magic-8-ball)
    - [Coin Flip Streak](#coin-flip-streak)
    - [Compliment Generator](#compliment-generator)
    - [Random Team Picker](#random-team-picker)
    - [Color Picker](#color-picker)
    - [Countdown Timer](#countdown-timer)
    - [Rock Paper Scissors](#rock-paper-scissors)
    - [Unit Converter](#unit-converter)
  - [Solid](#solid)
    - [Quiz Game](#quiz-game)
    - [Todo List](#todo-list)
    - [Pomodoro Timer](#pomodoro-timer)
    - [Flashcards](#flashcards)
    - [Password Strength Checker](#password-strength-checker)
    - [Hangman](#hangman)
    - [Number Guessing Game](#number-guessing-game)
    - [Habit Tracker](#habit-tracker)
    - [Grade Calculator](#grade-calculator)
    - [Tip Splitter](#tip-splitter)
    - [Memory Match](#memory-match)
    - [Budget Tracker](#budget-tracker)
    - [Study Playlist Timer](#study-playlist-timer)
    - [Text Adventure](#text-adventure)
  - [Stretch](#stretch)
    - [Two-Player Battle Game](#two-player-battle-game)
    - [Typing Speed Test](#typing-speed-test)
    - [Recipe Scaler](#recipe-scaler)
    - [Class Schedule Builder](#class-schedule-builder)
    - [Simple Drawing App](#simple-drawing-app)
    - [Music Practice Log](#music-practice-log)
    - [Wordle Clone](#wordle-clone)
    - [Inventory Manager](#inventory-manager)
    - [Sports Stat Tracker](#sports-stat-tracker)
    - [Choose-Your-Own-Story Engine](#choose-your-own-story-engine)
    - [Pixel Art Editor](#pixel-art-editor)
    - [Sorting Visualizer](#sorting-visualizer)
- [Good For Specific Lessons](#good-for-specific-lessons)
- [Ideas To Steer Away From](#ideas-to-steer-away-from)
- [Instructor Note: Letting Campers Bring Their Own](#instructor-note-letting-campers-bring-their-own)

## Starter — build in 10–20 minutes

**Everything middle school builds comes from this tier** — it's their only session — plus
HS's Session 1 build.

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
capstones. Too big for middle school's single session.

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

The app shows a fill-in-the-blank story. Each blank is labeled with a word type — noun,
verb, adjective — and the user types a word into each one. A button fills every word into
the story and shows the finished result. The story and its blanks are stored in the code,
so changing them changes the game.

#### Dice Roller

The window shows one big button and a number. Each click rolls a 20-sided die and
displays a random result from 1 to 20. A list of recent rolls can appear beneath the
button.

#### Magic 8-Ball

The user types a question into a box and clicks the button. The app answers with a random
message from a list — "Yes", "No", "Ask again later". The list of answers is stored in
the code, so the user can add their own.

#### Coin Flip Streak

Each click flips a coin and shows heads or tails. The window keeps a running count of
heads and tails, and shows how many of the same side have landed in a row.

#### Compliment Generator

The window shows a button. Each click displays a random compliment from a list of
messages stored in the code. The user can add new messages to the list.

#### Random Team Picker

The user types a list of names, one per line. A button splits the names into randomly
chosen groups of a set size and displays the teams. Clicking again shuffles the names
into new groups.

#### Color Picker

The window shows three sliders — one each for red, green, and blue. Moving a slider
changes the background to the color the three values describe. The current numbers are
shown on the window.

#### Countdown Timer

The user sets a number of minutes and presses Start. The window counts down, showing the
time remaining, and makes a sound when it reaches zero. Pause and Reset buttons stop or
restart the countdown.

#### Rock Paper Scissors

The user picks rock, paper, or scissors. The app picks one at random, compares the two,
and says who won. A scoreboard on the window tracks wins, losses, and ties.

#### Unit Converter

The user picks a conversion — miles to kilometers, Fahrenheit to Celsius, and a few more
— types a number, and the app shows the converted result. Choosing a different unit
clears the old number and starts fresh.

### Solid

#### Quiz Game

The app shows multiple-choice questions one at a time. The user picks an answer, the app
says whether it was right or wrong, and the next question appears. A final score is shown
when all the questions are done.

#### Todo List

The app shows a list of tasks. The user types a new task to add it, checks tasks off when
done, and removes tasks. The list is saved to a file, so it is still there when the app
reopens.

#### Pomodoro Timer

The timer runs a repeating cycle — 25 minutes of work, then 5 minutes of break. The
window shows which phase it is in and the time left in that phase. It switches phases on
its own and keeps a count of completed cycles.

#### Flashcards

The app shows a card with a question or term on the front. A click flips the card to show
the answer on the back. Buttons mark the card as known or unknown, and the app moves to
the next card and keeps a tally of both.

#### Password Strength Checker

The user types a password and the app scores it as it is typed — weak, okay, or strong —
based on rules like length and whether it mixes letters, numbers, and symbols. The rating
updates with every keystroke.

#### Hangman

The app picks a secret word. The user guesses one letter at a time; the app fills in every
place that letter appears and adds a new part of the hangman for each wrong guess. The
game ends when the word is complete or the drawings run out.

#### Number Guessing Game

The app picks a secret number. The user guesses a number and the app says whether the
secret is higher or lower. When the user gets it right, the app shows how many guesses it
took.

#### Habit Tracker

The app shows a list of daily habits. The user checks each habit off for the day, and the
app stores the checkmarks by date. For every habit it shows the current streak — how many
days in a row it has been done.

#### Grade Calculator

The user enters assignment scores and the weight of each one. The app combines them into a
weighted average and shows the final grade. If no scores are entered, it shows a message
instead of failing.

#### Tip Splitter

The user enters the bill total, the number of people, and a tip percentage. The app
calculates the tip and the cost per person, and shows both numbers.

#### Memory Match

The app shows a grid of face-down cards. The user flips two cards at a time to find
matching pairs — matching cards stay face up, and mismatches flip back over. A move
counter runs until every pair is found.

#### Budget Tracker

The user logs spending as a category and an amount — food, games, transport. The app
stores the entries in a file and shows the total spent, plus the total for each category.

#### Study Playlist Timer

The app runs a study timer for a set number of minutes. When it ends, it shows a suggested
break activity from a list — stretch, walk, get water — and then starts the next study
period.

#### Text Adventure

The app plays a text-based story. The user reads a description of a room, then chooses
from the options the app offers, and the story moves forward from that choice. The rooms,
options, and endings live in a separate data file, so a new story is just a new file.

### Stretch

#### Two-Player Battle Game

Two players take turns on the same keyboard. Each turn, the player whose turn it is picks
an attack, and the app applies the damage to the other character's hit points. Both
characters' hit points stay on screen, and a winner is declared when one runs out.

#### Typing Speed Test

The app shows a passage to type. As the user types, it times them and compares each
keystroke to the passage. When the passage is finished, it shows words per minute and an
accuracy percentage.

#### Recipe Scaler

The app shows a recipe with ingredient amounts. The user enters how many servings they
want, and the app multiplies every ingredient to match. Fractional amounts scale too — a
third becomes two-thirds — and the scaled amounts are shown next to the originals.

#### Class Schedule Builder

The user adds classes one at a time, each with a day and a time slot. The app checks each
new class against the ones already added and flags any that overlap. The schedule is laid
out in a grid with conflicts highlighted.

#### Simple Drawing App

The app shows a blank canvas. The user draws by clicking and dragging, picks a color from
a palette, and can erase. A save button writes the drawing to a file so it can be opened
again later.

#### Music Practice Log

The user logs each practice session by entering the date and the number of minutes
practiced. The app stores the entries and shows the practice time per week as a list or
chart.

#### Wordle Clone

The user gets six tries to guess a five-letter word. After each guess, the app colors each
letter — green for a letter in the right place, yellow for a letter in the word but in
the wrong place, gray for a letter not in the word. The game ends when the word is
guessed or the six tries run out.

#### Inventory Manager

The app tracks a list of items, each with a quantity. The user adds, removes, and edits
items, and the app saves the inventory to a data file. Items below a set quantity appear
on a low-stock list.

#### Sports Stat Tracker

The user logs each game for a team — the score, the opponent, and the date. The app
stores the games and computes season statistics like average score and win-loss record,
showing them on a summary screen.

#### Choose-Your-Own-Story Engine

The app plays a branching story in which the user chooses what happens next at each
point. Every scene and every choice is loaded from a separate data file, so the engine
itself never changes when a new story is added.

#### Pixel Art Editor

The app shows a grid of empty cells. The user clicks cells to fill them with the current
color, switches colors from a palette, and clears cells. Save and load buttons write a
picture to a file and bring it back.

#### Sorting Visualizer

The app shows a list of bars of different heights. The user picks a sorting algorithm and
presses a button, and the app animates the sort step by step, moving the bars as it goes,
until the list is sorted.

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

**Be strictest with middle school.** Their whole track is one session, and Build #2 is
~22 minutes of it. "Change Mad Libs into something else" is a completely legitimate
answer for anyone who can't settle on something.

------

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/) This Vibe Coding Curriculum by [Brian Bird](https://profbird.dev), created in <time>2026</time> with AI assistance, is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
