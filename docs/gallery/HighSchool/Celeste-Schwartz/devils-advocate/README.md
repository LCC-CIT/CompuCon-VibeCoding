# ⚖️ Devil's Advocate

A website that **debates you** on controversial topics. You state a position — it argues the opposite side, with real evidence, concedes when you're right, and keeps pressing. Powered by Claude.

Built-in topics:
- ⚡ **Clean energy** — solar, wind, nuclear, hydro, or geothermal. Pick your champion.
- 💸 **Universal basic income**
- 🚀 **Space exploration**
- 🏠 **Remote work**

## How it works

A tiny local server (`server.js`) serves the site and proxies every debate turn to the Claude API. The **API key lives only on the server** (in an environment variable) — it is never sent to your browser. Replies stream in as the model thinks.

**No key? It still works.** Without an API key the site runs in **demo mode**: the debater answers from a set of pre-written rebuttals, so you can click around and try it immediately. Add a key and it upgrades to the live Claude debate automatically.

## Setup

You need **Node.js 18+**. An **Anthropic API key** is optional (free credits at [console.anthropic.com](https://console.anthropic.com/)) — it upgrades the debate from demo mode to live.

```bash
cd devils-advocate

# 1. Install dependencies
npm install

# 2. Run it
npm start
```

Open **http://localhost:3000** and pick a side.

To enable the live debate, create `.env` from `.env.example` and paste your key next to `ANTHROPIC_API_KEY=`.

### No `.env` handy?

No problem — without a key the server just runs in **demo mode**, no setup
needed. To go live, you can set the `ANTHROPIC_API_KEY` environment variable
in your shell instead of a `.env` file; the server reads it either way.

## Configuration

Everything lives in `.env`:

| Variable | Default | What it does |
|---|---|---|
| `ANTHROPIC_API_KEY` | — | Your Anthropic key. Needed only for the live debate; without it the site runs in demo mode. |
| `MODEL` | `claude-opus-5` | Which model debates you. `claude-opus-5` for the sharpest sparring, `claude-sonnet-5` for a cheaper round. |
| `PORT` | `3000` | Local port the server listens on. |
| `ANTHROPIC_BASE_URL` | `https://api.anthropic.com` | Only honored from your `.env`. Lets you point at a compatible endpoint — everything else defaults to the official Anthropic API. |

## How the debate works

The debater is told to argue *against* whatever position you state — specifically
against your claim, not a strawman. It is instructed to concede genuine wins
and then pivot, and to end each round with one pointed question, so the
conversation stays a real back-and-forth rather than a lecture.

## Project layout

```
devils-advocate/
├── server.js        # Express server: static files + /api/chat streaming proxy
├── topics.js        # Topic metadata + the debater's system prompts
├── public/
│   ├── index.html   # Topic picker + debate UI
│   ├── styles.css
│   └── app.js       # Chat logic, SSE streaming, markdown-lite rendering
├── package.json
└── .env.example
```

## API

- `GET /api/topics` — topic list (id, name, emoji, tagline, opening line).
- `POST /api/chat` — `{ "topicId": "...", "messages": [{role, content}, …] }` → streams an SSE reply (`delta` / `done` / `error` events).
- `GET /api/health` — server status, model, and whether an API key is configured.

## Security notes

- The API key is read **server-side only**. The browser never sees it.
- Requests are pinned to `https://api.anthropic.com` unless you set `ANTHROPIC_BASE_URL` in your `.env` — so a stray `ANTHROPIC_BASE_URL`/`ANTHROPIC_AUTH_TOKEN` floating in your shell (e.g. from another tool's session) can't reroute your key to a third party.
- `messages` are validated to only user/assistant text roles before being forwarded.
- The server is a local dev tool — don't expose it to the public internet.
