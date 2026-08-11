# How To — Running AI Models on Your Own Computer (Draft)

**Draft. Not tested on a CompuCon lab machine, not tested at home either.** Everything
below is built from current vendor docs and community write-ups, not from running it
ourselves. Treat commands and numbers as a starting point, not a promise. See
[Verify This Before You Teach It](#verify-this-before-you-teach-it).

This is the deepest of the three "keep coding at home" options:

- Claude Pro, ChatGPT Pro, Gemini Pro, Mistral — pay a company, use their computer.
- OpenCode Zen (see the [OpenCode Zen how-to](opencode-zen-howto.html)) — free, no
  setup, someone else's computer, some cap you don't control.
- **This page — no company, no monthly bill, no cap. Your computer does the work.**

It's also the most advanced option. It needs real hardware, a bigger download, and more
patience than either of the other two. Read [What You Get](#what-you-get) and
[What You Give Up](#what-you-give-up) before you spend an evening on this.

> **It's a bigger departure from the rest of the track than the OpenCode Zen page.**
> That page breaks one rule (a second command). This one breaks several: it needs an
> install with real disk space, it needs hardware most lab machines don't have, and the
> whole point is running software the track never touches in class. That's fine for a
> take-home page for a camper with a gaming PC or a family computer with a good graphics
> card. It has no place in the Session 1 spine, and it isn't for every camper — most
> should use OpenCode Zen instead.

---

## Contents

- [Verify This Before You Teach It](#verify-this-before-you-teach-it)
- [What You Get](#what-you-get)
- [What You Give Up](#what-you-give-up)
- [Hardware You Need](#hardware-you-need)
- [Part 1 — Pick a Local Model Server](#part-1-pick-a-local-model-server)
- [Part 2 — Install and Pull a Model](#part-2-install-and-pull-a-model)
- [Part 3 — Pick a Coding Model](#part-3-pick-a-coding-model)
- [Part 4 — Use It With OpenCode](#part-4-use-it-with-opencode)
- [Part 5 — Use It With Claude Code](#part-5-use-it-with-claude-code)
- [When It Breaks](#when-it-breaks)

## Verify This Before You Teach It

- **Nobody on this project has run these steps.** They come from Ollama's own docs,
  OpenCode's provider docs, and a handful of 2026 write-ups on connecting Claude Code to
  a local model. Before this page gets a footnote link anywhere, someone needs to walk
  it end to end on a real Windows 11 machine.
- **The Claude Code half is the least certain part.** Claude Code only speaks
  Anthropic's own API format. Ollama added a compatible endpoint in version 0.14, which
  is what [Part 5](#part-5-use-it-with-claude-code) uses — confirm that version number
  and the exact commands still match Ollama's current docs before you teach this.
- **Model names and sizes move fast.** The models named in
  [Part 3](#part-3-pick-a-coding-model) are what's strong as of August 2026. Check
  `ollama.com/library` or LM Studio's model browser for anything newer before you point
  a camper at a specific download.

## What You Get

- **No account, no subscription, no monthly bill.** Once the download is done, it runs
  with no internet connection at all.
- **No usage cap.** Nobody is counting your requests. The only limit is how fast your
  own hardware runs.
- **Nothing you type leaves your computer.** For a school-owned or family-shared
  machine, that's worth something on its own.
- **It keeps working after the free trial ends.** Free tiers and free models come and
  go. A model sitting on your hard drive doesn't expire.

## What You Give Up

- **Speed.** A cloud model runs on a data-center GPU. Your laptop is not a data-center
  GPU. Expect slower replies, especially on a longer prompt.
- **Model quality.** The best local models are good at coding, but the very best models
  in the world — the ones Claude Pro, ChatGPT Pro, and Gemini Pro give you — are bigger
  than anything that fits on a home computer. Local models are "very good for their
  size," not "the best there is."
- **The easy setup.** OpenCode Zen needs zero configuration. This needs an install, a
  multi-gigabyte download, and some command-line setup. Budget a real chunk of time the
  first time through.
- **Free disk space.** Coding models start around 4–5 GB and climb from there. Check
  what's actually free on the drive before picking a model.

## Hardware You Need

The two things that matter: **how much RAM your computer has**, and **whether it has a
dedicated graphics card (GPU) with its own memory (VRAM)**. A model with no GPU still
runs — it just runs on the CPU and RAM, and it runs much slower.

| Model size | Minimum to run it at all | Comfortable | What that gets you |
|---|---|---|---|
| 7–8B (billion parameters) | 8 GB RAM, no GPU needed | 8 GB VRAM GPU | Fast enough for real use, weakest coding quality of the three |
| 14B | 16 GB RAM | 12 GB VRAM GPU | The sweet spot for most home computers in 2026 |
| 30–32B | 32 GB RAM | 24 GB VRAM GPU | Noticeably stronger, needs a serious gaming or workstation card |

- **Apple Silicon Macs (M-series) are a special case.** RAM and VRAM are the same pool
  of "unified memory," so a Mac with 16 GB or more of RAM can run models that would need
  a dedicated GPU on Windows.
- **No GPU at all still works, just slowly.** A 7B model on RAM alone is usable for
  short prompts; a 30B model on RAM alone will feel painfully slow.
- **This is why it's not a lab-machine thing.** CompuCon's lab computers are built for
  general classwork, not for running an AI model — this path is for a home computer a
  camper's family already has, ideally with a gaming or newer graphics card.

## Part 1 — Pick a Local Model Server

A **local model server** is the program that actually loads the model into memory and
answers requests — OpenCode and Claude Code both talk to it instead of talking to
Anthropic or OpenAI over the internet. Two good options:

| | Ollama | LM Studio |
|---|---|---|
| **Interface** | Command line | Graphical app with a chat window and a model browser |
| **Best for** | Someone comfortable in a terminal, or scripting it | Someone who wants to click around, browse, and compare models visually |
| **Runs headless (no window)** | Yes | Not really — it's built as a desktop app |
| **Install** | One installer, small download | One installer, small download |

Either one works with OpenCode and Claude Code. This page uses **Ollama**, because its
command-line habits match the rest of the track. If a camper would rather click through
a graphical model browser, LM Studio does the same job — see
[lmstudio.ai](https://lmstudio.ai).

## Part 2 — Install and Pull a Model

Install Ollama from **<https://ollama.com/download/windows>**, or with `winget`:

```powershell
winget install --id Ollama.Ollama
```

Ollama installs as a background service — once it's installed, it's just running,
listening on your own computer. No `opencode`-style command to start it every time.

**Download a model** — this is the multi-gigabyte part, and only needs to happen once
per model:

```powershell
ollama pull qwen2.5-coder:7b
```

Swap `7b` for `14b` or `32b` depending on the hardware table above. Bigger number,
bigger download, slower to load, better answers.

**Try it right from the terminal**, no OpenCode or Claude Code involved yet:

```powershell
ollama run qwen2.5-coder:7b
```

Type a question, see it answer. Type `/bye` to exit.

## Part 3 — Pick a Coding Model

Not every model is good at writing code — plenty are built for chat and creative
writing instead. As of August 2026, the strongest local coding models are all in the
**Qwen Coder** family, with a couple of other names worth knowing:

| Model | Ollama name | Size | Good for |
|---|---|---|---|
| Qwen2.5-Coder | `qwen2.5-coder:7b` | 7B | The safe default — runs on almost anything, strong for its size |
| Qwen3-Coder | `qwen3-coder:30b` | 30B (only ~3B active at once) | The best quality-per-GB pick if you have 24 GB+ of RAM or VRAM |
| DeepSeek-Coder V3 | `deepseek-coder-v3` | Large | The strongest open coding model overall, but needs serious hardware |
| Devstral | `devstral:24b` | 24B | Built specifically for multi-step, agent-style coding tasks like Claude Code and OpenCode use |

**Rule of thumb:** start with `qwen2.5-coder:7b`. If it feels slow to reply but the
answers are good, the model is right and the hardware is the bottleneck. If the answers
themselves are weak, and the hardware table says you can afford it, step up to a bigger
model.

## Part 4 — Use It With OpenCode

OpenCode needs to know your local server exists. Create (or edit)
`opencode.json` in `$HOME\.config\opencode\`:

```json
{
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "options": { "baseURL": "http://localhost:11434/v1" },
      "models": {
        "qwen2.5-coder:7b": {}
      }
    }
  }
}
```

Then, inside OpenCode:

```
/models
```

Your local model shows up alongside the OpenCode Zen models from the
[OpenCode Zen how-to](opencode-zen-howto.html). Pick it, and prompts run against your
own computer instead of the internet — no request leaves the machine.

## Part 5 — Use It With Claude Code

**This is the least certain part of this page — see the warning at the top.** Claude
Code normally only understands Anthropic's own API. Recent versions of Ollama (0.14 and
up) added a compatible endpoint, which lets `claude` talk to it directly with no
translator program in between:

```powershell
$env:ANTHROPIC_BASE_URL = "http://localhost:11434"
$env:ANTHROPIC_AUTH_TOKEN = "ollama"
$env:OLLAMA_CONTEXT_LENGTH = "32768"
claude --model qwen2.5-coder:7b
```

- **The context-length line matters.** Ollama's default context window is small enough
  to break Claude Code mid-task. Set it higher, as above, before starting `claude`.
- **These environment variables only last for the current terminal window.** Close the
  window, and `claude` goes back to normal — no local setup left behind, and no risk of
  accidentally leaving a lab machine pointed at the wrong thing.
- **If this doesn't work as written,** the fallback is a small translator program
  (search "LiteLLM" or "claude-code-proxy") that sits between `claude` and Ollama and
  converts between the two API formats. That's a second install and outside the scope
  of this page — treat it as the thing to reach for only if the direct route above is
  confirmed broken.

## When It Breaks

| What you see | Likely cause |
|---|---|
| Ollama install finishes, nothing seems to be running | It's a background service, not a window — check with `ollama list` in a terminal |
| Model download is extremely slow | Normal for the first pull of a large model — it's several GB over your home internet |
| Replies are very slow | Model is too big for the hardware — see the [hardware table](#hardware-you-need), try a smaller size |
| OpenCode doesn't list the local model | `opencode.json` has a typo, or Ollama isn't running — confirm with `ollama list` first |
| `claude` errors immediately after setting the environment variables | Ollama version is older than 0.14 — update it, or use the LiteLLM fallback in [Part 5](#part-5-use-it-with-claude-code) |
| Computer becomes unusably slow while a model answers | Normal on a machine near its hardware limit — close other programs, or step down to a smaller model |

The general troubleshooting reference is
[`troubleshooting.html`](../troubleshooting.html) — it's written for `claude` against
Anthropic's cloud, but the sections on hung sessions and on reading errors still apply.

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/) This Vibe Coding Curriculum by [Brian Bird](https://profbird.dev), created in <time>2026</time> with AI assistance, is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
