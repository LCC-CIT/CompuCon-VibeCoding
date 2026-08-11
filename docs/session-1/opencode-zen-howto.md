# How To — OpenCode Zen, a Free Model Provider (Draft)

**Draft. Signup and free-model use are confirmed on a personal machine; nothing has been
tested on an LCC lab (CompuCon) machine yet.** See
[Verify this before you teach it](#verify-this-before-you-teach-it) for exactly what's
settled and what isn't — and note the flag on the **interface tested**, in the same
section, before you trust the written steps below.

This walks through creating a free OpenCode Zen account, getting an API key, adding it to
OpenCode as a provider, and running a free model such as **Big Pickle** or **MiMo-V2.5**.
It assumes OpenCode is already installed on the machine.

**Why this exists: so campers can keep coding at home without paying for anything.** The
tool used in class costs money, which makes "go build a fourth thing" a hollow send-off
for a camper whose family isn't going to buy a subscription. A free provider closes that
gap. That is the whole point of this page — it is an *after camp* path first and
everything else second.

> **It is a departure from the rest of the track, on purpose.** The curriculum's standing
> rules are one command (`claude`), no accounts, and campers never touch an API key.
> Everything below breaks all three. That's acceptable for a take-home page and not
> acceptable inside the Session 1 spine — don't fold it in.

---

## Contents

- [Verify this before you teach it](#verify-this-before-you-teach-it)
- [What this costs](#what-this-costs)
- [Part 1 — Create the account](#part-1-create-the-account)
- [Part 2 — Get your API key](#part-2-get-your-api-key)
- [Part 3 — Add the key to OpenCode](#part-3-add-the-key-to-opencode)
- [Part 4 — Pick a free model](#part-4-pick-a-free-model)
- [Part 5 — Prove it works](#part-5-prove-it-works)
- [When it breaks](#when-it-breaks)
- [If you hand this to campers](#if-you-hand-this-to-campers)

## Verify this before you teach it

**Settled: signup needs no credit card.** Confirmed 2026-08-10 by creating a real
account. The one vendor page that read otherwise was describing the paid-model flow.
Campers can sign up without payment details.

**Settled: the free models actually work.** Also confirmed 2026-08-10 — two OpenCode
Zen free models run successfully on a personal Windows 11 machine.

**Flag: that test used the OpenCode desktop app, not the terminal.** Everything from
[Part 3](#part-3-add-the-key-to-opencode) on documents the command-line flow — `opencode`
in a terminal, `/connect`, `opencode auth login` — because that matches how the rest of
the track teaches Claude Code. **Those specific commands have not themselves been
confirmed** by the desktop-app test. The desktop app has its own settings screen and
model picker, described differently. Until someone runs the CLI steps end to end, treat
Part 3 and Part 4 as vendor-documented, not instructor-verified, even though the
underlying account and models are now known to work.

What's left, and each takes one person twenty minutes to settle:

1. **Do the LCC lab (CompuCon) machines allow it?** OpenCode writes credentials to your
   user profile and needs outbound HTTPS to `opencode.ai`. College lab images restrict
   both. This is the same class of problem that killed the old two-command setup. **This
   is the gating item for teaching it in class** — a personal machine proves nothing
   about the lab image. It does *not* gate the take-home use case, since campers using
   this at home are on their own machines, not CompuCon's.
2. **Are the free models still free?** The vendor lists these as free *during trial
   periods*. That is not a stable guarantee — a model that's free in August may not be in
   October. Re-check the list the week you teach, not the term before.

## What this costs

Free models are rate-limited. The vendor does not publish per-model limits clearly, and
one third-party source reports a daily request cap. **Assume a cap exists and that a room
of twenty campers will find it.** If you're running this with a class rather than one
person, test with several machines hitting it at once before you commit.

Paid models on the same account are charged per request. Since account setup and model
selection sit next to each other in the interface, a camper can wander onto a paid model
by accident if billing is ever added. **Don't add billing to an account campers will
touch.**

## Part 1 — Create the account

1. Go to **<https://opencode.ai/auth>**
2. Sign in with the method offered there.

No credit card, no payment details. This has been done for real, so if a card is ever
demanded, something changed on the vendor's end — don't enter one, and re-check the free
model list, because that's the likeliest thing to have moved.

Campers each need an email address they can receive mail at, and each is agreeing to a
third party's terms of service. For a camp with minors that's a question for whoever
handles permissions, not a technical detail — settle it before the day.

## Part 2 — Get your API key

Still at <https://opencode.ai/auth>, find your API key and copy it.

**Treat the key like a password.** It's tied to your account and anyone holding it can
spend against it.

- Don't paste it into a shared doc, a chat, or a slide.
- Don't put it in a file that goes to Google Drive with the rest of the project.
- If it leaks, revoke it and make a new one.

This is worth ninety seconds of instructor talk if campers are doing it themselves — it's
the first time in the track they hold a credential, and the habit matters more than the
key does.

## Part 3 — Add the key to OpenCode

**These are the terminal steps, unconfirmed as written — see the flag above.** The
account and the free models themselves are known to work; whether they work *this way*
on a lab machine is still open.

Start OpenCode in a project folder, the same way campers start `claude`:

```powershell
cd $HOME\Documents\Projects
cd <Name>
mkdir opencode-test
cd opencode-test
opencode
```

Inside the OpenCode interface, run:

```
/connect
```

Select **OpenCode Zen** from the provider list, then paste your API key when prompted.

**Alternative, from the terminal instead of the interface:**

```powershell
opencode auth login
```

Same result — pick the provider, paste the key.

**Confirm it was stored:**

```powershell
opencode auth list
```

OpenCode Zen should appear in the output. Credentials live under your user profile in
`.local\share\opencode\auth.json` — the exact Windows path is one of the things to
confirm on a lab machine, since it decides whether a roaming profile keeps the key
between sessions or campers re-enter it every time.

## Part 4 — Pick a free model

Inside OpenCode:

```
/models
```

Pick one of the free models. As of writing, the free list is:

| Model | ID |
|---|---|
| Big Pickle | `big-pickle` |
| DeepSeek V4 Flash | `deepseek-v4-flash-free` |
| MiMo-V2.5 | `mimo-v2.5-free` |
| Nemotron 3 Ultra | `nemotron-3-ultra-free` |
| North Mini Code | `north-mini-code-free` |
| Laguna S 2.1 | `laguna-s-2.1-free` |
| Ling 3.0 Tiny | `ling-3.0-tiny-free` |
| LongCat 2.0 | `longcat-2.0-free` |

Where a model has to be written out in full, the form is `opencode/` plus the ID — so
`opencode/big-pickle` or `opencode/mimo-v2.5-free`.

**Note the pattern:** every free model except Big Pickle carries `-free` in its ID. If
you're reading a model name off a screen and typing it somewhere, that suffix is the
difference between free and billed. Check it twice.

The API base URL, if you ever need it directly, is `https://opencode.ai/zen/v1`. You
should not need it for this workflow — `/connect` handles it.

## Part 5 — Prove it works

Don't assume the connection is good because nothing errored. Run the track's own standard
and make it build something you can check:

```
Build a dice roller in Python with a tkinter window. Big button that says ROLL, and
when I click it, it shows a random number from 1 to 20 in huge text. Save it as
dice.py
```

Then:

```powershell
python dice.py
```

A window with a working button means the whole chain is good — account, key, provider,
model, and the model's ability to write code that runs.

**This is the same dice roller from the Session 1 hook**, which makes it a fair
comparison: run the identical prompt through `claude` and through a free Zen model and
look at the two results side by side. That comparison is genuinely worth class time — it
makes "the interface and the model are separable" concrete instead of abstract, and it
shows that model choice is a real engineering decision with visible consequences.

## When it breaks

| What you see | Likely cause |
|---|---|
| Provider missing from `/connect` list | OpenCode is out of date — update it |
| Key rejected immediately | Copied with trailing whitespace, or pasted into the wrong provider |
| Works, then stops mid-class | Rate limit. Switch models or wait it out |
| Model missing from `/models` | Free trial for that model ended — pick another from the list |
| Nothing connects, on every machine | Lab firewall blocking `opencode.ai`. Nothing you can fix in the room |
| Key gone next session | Profile isn't persisting `auth.json`. Campers re-run `/connect` each time |

The general troubleshooting reference is
[`troubleshooting.html`](../troubleshooting.html) — it's written for `claude`, but the
sections on hung sessions and on reading errors apply to any agent in a terminal.

## If you hand this to campers

Should you decide to run it camper-side rather than instructor-side, three things change:

- **Budget 15–20 minutes**, not five. Account creation with a room of twenty is slow, and
  email verification is where it stalls.
- **Have a fallback ready for anyone who can't sign up.** Someone will have no email
  access, a typo'd address, or a blocked verification mail. They should pair with a
  neighbor rather than sit out.
- **Say the API key rule out loud before you hand out the URL**, not after. See
  [Part 2](#part-2-get-your-api-key).

Given all of that, the honest recommendation is to run this as an instructor demo and a
take-home handout, and keep class time on building.

**Nothing on the site links to this page while it's a draft.** That is not the same as
hidden: GitHub Pages renders every `.md` under `docs/`, so
`/session-1/opencode-zen-howto.html` is live and publicly reachable right now by anyone
with the URL — which is exactly what makes it usable as a take-home link you paste into
Drive or read out at the end of a session. When it's been tested and you're ready for
campers to find it on their own, it belongs on `teacher.html`, or in the Session 1 camper
notes' take-home section if it's going camper-side.

------

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/) This Vibe Coding Curriculum by [Brian Bird](https://profbird.dev), created in <time>2026</time> with AI assistance, is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
