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
one third-party source reports a daily request cap. **Assume a cap exists.** 

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



## Free Coding Models on OpenCode Zen 

## Ranked by Coding Ability

These models were free as of August 10, 2026

| Rank  | Model                                  | Parameters (Total / Active) | Context Length   | Key Coding Benchmarks                                        |
| ----- | -------------------------------------- | --------------------------- | ---------------- | ------------------------------------------------------------ |
| **1** | **DeepSeek V4 Flash**                  | 284B / 13B                  | 1M tokens        | Terminal Bench 2.1 **82.7%**, DeepSWE **54.4%**, Toolathlon Verified **70.3%**, NL2Repo **54.2%** [[github.com\]](https://github.com/anomalyco/opencode/issues/10404), [[docs.zenmux.ai\]](https://docs.zenmux.ai/zh/best-practices/opencode.html) |
| **2** | **Nemotron 3 Ultra**                   | 550B / 55B                  | 1M tokens        | Code benchmark **85.3%**; designed for long-horizon agentic coding, reasoning, and software engineering tasks. [[open.bigmodel.cn\]](https://open.bigmodel.cn/), [[github.com\]](https://github.com/AftabIbrahimKazi/ai-dev-kit/blob/main/skills/models/opencode/big-pickle.md), [[freeaiapi.org\]](https://freeaiapi.org/endpoint/opencode/opencode-big-pickle) |
| **3** | **LongCat-2.0**                        | 1.6T / ~48B active          | 1M tokens        | SWE-Bench Pro **59.5%**, Terminal-Bench **70.8%**. Purpose-built for agentic coding. [[en.oninvest.com\]](https://en.oninvest.com/article/chinese-ai-company-zhipu-has-won-the-war-of-hundreds-of-models-but-what-s-next-for-it), [[en.webhakim.com\]](https://en.webhakim.com/zhipu-ai-raises-137m-to-boost-generative-ai/) |
| **4** | **Laguna S 2.1**                       | 118B / 8B                   | 1,048,576 tokens | SWE-Bench Multilingual **78.5%**, SWE-Bench Pro **59.4%**, Terminal-Bench 2.1 **70.2%**. [[mastra.ai\]](https://mastra.ai/models/providers/opencode), [[huntscreens.com\]](https://huntscreens.com/zh/products/opencode-zen) |
| **5** | **Big Pickle (identified as GLM-4.6)** | ~355B / ~32B active         | 200K tokens      | OpenCode maintainers confirmed Big Pickle is GLM-4.6; widely regarded as a strong coding-agent model. 200K context and 128K output. [[huggingface.co\]](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash), [[atlas.kevinhu.io\]](https://atlas.kevinhu.io/models/north-mini-code-1-0), [[artificial...nalysis.ai\]](https://artificialanalysis.ai/articles/north-mini-code-cohere-s-small-coding-focused-moe-model) |
| **6** | **MiMo-V2.5**                          | 310B / 15B                  | 1M tokens        | Coding Agent score **71.8**, MiMo Coding Bench **62.3**, Terminal-Bench 2.0 **56.1**. [[anyrouter.dev\]](https://anyrouter.dev/model/opencode/big-pickle), [[beatriz.page\]](https://www.beatriz.page/2026-02-06-opencode-get-started-yc-case-study), [[github.com\]](https://github.com/anomalyco/opencode/issues/4276) |
| **7** | **North Mini Code**                    | 30B / 3B                    | 256K tokens      | Artificial Analysis Coding Index **33.4-41.7**; built specifically for software engineering workflows. [[cryptopolitan.com\]](https://www.cryptopolitan.com/zhipu-ai-free-agent-launch-deepseek/), [[edgen.tech\]](https://www.edgen.tech/news/post/zhipu-ai-hikes-model-price-10-after-new-version-tops-opus-46-benchmark), [[opencode.ai\]](https://opencode.ai/docs/zen/) |
| **8** | **Ling-3.0-tiny**                      | 7.9B / 1.3B                 | 256K-262K tokens | Artificial Analysis Coding Index **26.5**, SciCode **24.2%**. [[brunch.co.kr\]](https://brunch.co.kr/@drytree21/476), [[hunted.space\]](https://hunted.space/dashboard/opencode/launches/opencode-zen) |

### 

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/) This Vibe Coding Curriculum by [Brian Bird](https://profbird.dev), created in <time>2026</time> with AI assistance, is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
