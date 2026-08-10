# Project Idea Bank

Sorted by how much can go wrong. Project this in Session 1 and keep it up for the rest
of the track.

**Which tier, by age group and session:**

| | MS (85 min sessions) | HS (120/180/180/60) |
|---|---|---|
| **Session 1** build #2 | Starter — but most MS students customize Mad Libs instead | Starter or Solid |
| **Session 2** spec-first build | Starter | Solid |
| **Session 3** | *No new project* — MS hardens an existing app | Capstone continues (Solid or Stretch) |
| **Session 4** | Capstone — **Starter**, two must-haves max | *No build time* — demos only |

**Starter is a hard ceiling for middle school.** MS has 340 minutes total against HS's
540, and the longest MS build block in the track is 38 minutes. A Solid-tier project
will not finish.

**All of these assume Python + tkinter.** That's deliberate — one language, one GUI
library, no install friction on the Windows lab image, instant visual payoff.

**Students who already know another stack may use it.** Every idea below works in
HTML/CSS/JS in a browser too, and most work as a plain terminal program. The idea is the
idea; the stack is a detail. See the "different language" entry in
[`troubleshooting.md`](troubleshooting.md) for the two conditions.

---

## Starter — build in 10–20 minutes

**Everything middle school builds comes from this tier**, plus HS's Session 1 build.

| App | What it does | Why it works |
|---|---|---|
| **Mad Libs** | Fill in 5 words, get a funny story | Instant payoff, endlessly customizable |
| **Dice Roller** | Click to roll a d20 | Simplest possible thing that's still fun |
| **Magic 8-Ball** | Ask a question, get an answer | Adding your own answers is the hook |
| **Coin Flip Streak** | Flip and track heads/tails counts | Sneaks in real state management |
| **Compliment Generator** | Random nice thing, on a button | Easy to personalize |
| **Random Team Picker** | Names in, shuffled groups out | Actually useful — they'll use it |
| **Color Picker** | Sliders that change the background live | Very visual, very immediate |
| **Countdown Timer** | Set minutes, count down, beep | Timing bugs teach a lot |
| **Rock Paper Scissors** | Play the computer, keep score | Score tracking is the real lesson |
| **Unit Converter** | Miles↔km, F↔C, etc. | Great for wrong-input testing |

---

## Solid — build in 30–60 minutes

**High school only.** HS Session 2's spec-first build, and the smaller end of HS
capstones. Too big for any MS block.

| App | What it does | The interesting part |
|---|---|---|
| **Quiz Game** | Multiple choice, score at the end | Scoring edge cases everywhere |
| **Todo List** | Add, check off, delete | Persistence — save to a file |
| **Pomodoro Timer** | 25 work / 5 break, cycles | State machine, real logic |
| **Flashcards** | Front/back cards, mark right or wrong | Data structure choice matters |
| **Password Strength Checker** | Live feedback as you type | Rules-based scoring, easy to break |
| **Hangman** | Classic word guessing | Real game logic, win/lose states |
| **Number Guessing Game** | Higher/lower with hints | Perfect for teaching input validation |
| **Habit Tracker** | Check off daily habits, keep streaks | Dates are gloriously bug-prone |
| **Grade Calculator** | Enter scores, get weighted average | Empty-list bug lives here |
| **Tip Splitter** | Bill + people + tip % → per person | Division by zero, rounding |
| **Memory Match** | Flip cards, find pairs | Grid layout, timing |
| **Budget Tracker** | Log spending by category | Text file storage, totals |
| **Study Playlist Timer** | Timer that suggests break activities | Combines two ideas |
| **Text Adventure** | Rooms, choices, an ending | Great for data-file separation |

---

## Stretch — 60–90 minutes, some ambition

**High school capstones only** — pitched end of Session 2, built in Session 3. Assume
they'll cut something.

| App | What it does | Why it stretches |
|---|---|---|
| **Two-Player Battle Game** | Turn-based, same keyboard, HP and attacks | Turn logic, state, balance |
| **Typing Speed Test** | Type a passage, get WPM and accuracy | Timing + string comparison |
| **Recipe Scaler** | Recipe in, scale to N servings | Fractions and units are hard |
| **Class Schedule Builder** | Add classes, detect time conflicts | Real algorithmic thinking |
| **Simple Drawing App** | Draw on a canvas, pick colors, save | Canvas events, file output |
| **Music Practice Log** | Log sessions, chart weekly minutes | Data over time, simple charting |
| **Wordle Clone** | 5 letters, 6 guesses, color feedback | The yellow-letter rule is genuinely tricky |
| **Inventory Manager** | Items, quantities, low-stock alerts | Multi-file, JSON data |
| **Sports Stat Tracker** | Log games, compute season averages | Real data modeling |
| **Choose-Your-Own-Story Engine** | Story loaded from a data file | Best multi-file project on this list |
| **Pixel Art Editor** | Grid of cells, click to color, export | Grid math, save/load |
| **Sorting Visualizer** | Watch bubble sort run step by step | Animation + a real CS concept |

---

## Good For Specific Lessons

Reach for these when you want to teach a particular thing.

| Lesson | Use this |
|---|---|
| **Wrong-input testing** | Unit Converter, Grade Calculator, Tip Splitter |
| **Splitting into files** (HS only) | Choose-Your-Own-Story Engine, Quiz Game |
| **Saving data** | Todo List, Habit Tracker, Budget Tracker |
| **The AI's code runs but is wrong** | Grade Calculator (empty list), Wordle (duplicate letters) |
| **Scope cutting** | Anything a student describes as "like [big famous app]" |
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

## Instructor Note: Letting Students Bring Their Own

Always allow it. Sign it off against three questions:

1. **Can I picture the screen?** If they can't describe what it looks like, it's not
   ready.
2. **Does it need anything but Python?** Accounts, keys, internet, other people — cut it
   or redirect.
3. **What's the smallest version that's still the same idea?** Build that one.

A student building their own idea badly is learning more than a student building your
idea well. Protect that — just protect them from reaching the showcase with nothing to
demo.

**Be strictest in MS Session 4.** It's the only MS session with a self-chosen project,
and there are 38 minutes to build it. "Rebuild my Session 1 app, better" is a completely
legitimate answer for anyone who can't settle on something.
