# How To — OpenCode Zen, a Free Model Provider

**Confirmed working, no account needed.** OpenCode's free models are available the moment
you install it — no signup, no API key, no provider setup. Confirmed on a personal
Windows 11 machine (2026-08-10) and on a CompuCon lab machine (2026-08-11). The only open
question is the usage cap — see [What this costs](#what-this-costs).

This walks through installing OpenCode, running it, and picking a free model such as
**Big Pickle** or **MiMo-V2.5**. It assumes OpenCode is already installed on the machine.

**Why this exists: so campers can keep coding at home without paying for anything.** The
tool used in class costs money, which makes "go build a fourth thing" a hollow send-off
for a camper whose family isn't going to buy a subscription. A free provider closes that
gap. That is the whole point of this page — it is an *after camp* path first and
everything else second.

> **It is a departure from the rest of the track, on purpose.** The curriculum's standing
> rule is one command (`claude`). This uses a different command (`opencode`) instead —
> though it needs no account and no API key, so it's a smaller departure than it first
> looks. That's acceptable for a take-home page and not acceptable inside the Session 1
> spine — don't fold it in.

---

## Contents

- [What this costs](#what-this-costs)
- [Part 1 — Run OpenCode](#part-1-run-opencode)
- [Part 2 — Pick a free model](#part-2-pick-a-free-model)
- [Part 3 — Prove it works](#part-3-prove-it-works)
- [When it breaks](#when-it-breaks)
- [Free Coding Models on OpenCode Zen](#free-coding-models-on-opencode-zen)
  - [Ranked by Coding Ability](#ranked-by-coding-ability)

## What this costs

Free models are rate-limited, and the exact caps aren't published. One user reports
hitting a limit of **200 requests in a 5-hour window** — it isn't confirmed whether that's
per model or a total across all free models, so budget as if it's a total. If you hit it,
switch models or wait it out.

## Part 1 — Run OpenCode

Start OpenCode in a project folder, the same way campers start `claude`:

```powershell
cd $HOME\Documents\Projects
cd <Name>
mkdir opencode-test
cd opencode-test
opencode
```

That's it — no `/connect`, no login, no key. The free models are ready to use as soon as
OpenCode opens.

## Part 2 — Pick a free model

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

## Part 3 — Prove it works

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

A window with a working button means the whole chain is good — OpenCode, the free
provider, model, and the model's ability to write code that runs.

**This is the same dice roller from the Session 1 hook**, which makes it a fair
comparison: run the identical prompt through `claude` and through a free Zen model and
look at the two results side by side. That comparison is genuinely worth class time — it
makes "the interface and the model are separable" concrete instead of abstract, and it
shows that model choice is a real engineering decision with visible consequences.

## When it breaks

| What you see | Likely cause |
|---|---|
| Works, then stops mid-class | Rate limit. Switch models or wait it out |
| Model missing from `/models` | Free trial for that model ended — pick another from the list |
| Nothing connects, on every machine | Lab firewall blocking outbound access — nothing you can fix in the room |

The general troubleshooting reference is
[`troubleshooting.html`](../troubleshooting.html) — it's written for `claude`, but the
sections on hung sessions and on reading errors apply to any agent in a terminal.

## Free Coding Models on OpenCode Zen

### Ranked by Coding Ability

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

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/) This Vibe Coding Curriculum by [Brian Bird](https://profbird.dev), created in <time>2026</time> with AI assistance, is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
