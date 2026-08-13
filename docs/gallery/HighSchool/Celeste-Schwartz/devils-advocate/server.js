// Devil's Advocate — local server.
//
// Serves the static frontend and proxies debate turns to the Claude API.
// The Anthropic API key lives ONLY here (in the environment), never in the
// browser. Debate responses stream to the client as Server-Sent Events.
//
// Run:  npm install  &&  cp .env.example .env  (add your key)  &&  npm start
// Then open http://localhost:3000

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import express from 'express';
import Anthropic from '@anthropic-ai/sdk';

import { getTopics, getTopic } from './topics.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// ---- Minimal .env loader (no dotenv dependency). ---------------------------
// Returns the values parsed from the .env file, so the API config below can
// distinguish "set by the user in .env" from "inherited from the shell" — we
// don't want an ambient ANTHROPIC_BASE_URL in the shell hijacking where the
// user's API key gets sent.
function loadEnv() {
  const fileEnv = {};
  const envPath = path.join(__dirname, '.env');
  try {
    const text = fs.readFileSync(envPath, 'utf8');
    for (const line of text.split(/\r?\n/)) {
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith('#')) continue;
      const eq = trimmed.indexOf('=');
      if (eq === -1) continue;
      const key = trimmed.slice(0, eq).trim();
      let value = trimmed.slice(eq + 1).trim();
      if (
        (value.startsWith('"') && value.endsWith('"')) ||
        (value.startsWith("'") && value.endsWith("'"))
      ) {
        value = value.slice(1, -1);
      }
      fileEnv[key] = value;
      if (!(key in process.env)) process.env[key] = value;
    }
  } catch {
    // No .env file — rely on real environment variables instead.
  }
  return fileEnv;
}
const fileEnv = loadEnv();

// API key resolution: .env file value first, then a real environment variable.
const API_KEY = fileEnv.ANTHROPIC_API_KEY || process.env.ANTHROPIC_API_KEY;
// Only a base URL the user puts in .env is honored; otherwise we pin to the
// official Anthropic endpoint so stray shell env vars can't reroute requests.
const BASE_URL = fileEnv.ANTHROPIC_BASE_URL || 'https://api.anthropic.com';

function buildClient() {
  return new Anthropic({ baseURL: BASE_URL, ...(API_KEY ? { apiKey: API_KEY } : {}) });
}

const PORT = Number(process.env.PORT || 3000);
const MODEL = process.env.MODEL || 'claude-opus-5';

const app = express();
app.use(express.json({ limit: '1mb' }));

// ---- Static frontend -------------------------------------------------------
app.use(express.static(path.join(__dirname, 'public')));

// ---- API: topic metadata ---------------------------------------------------
app.get('/api/topics', (req, res) => {
  res.json(getTopics());
});

// ---- API: setup health check ----------------------------------------------
app.get('/api/health', (req, res) => {
  res.json({
    ok: true,
    model: MODEL,
    hasApiKey: Boolean(API_KEY),
    mode: API_KEY ? 'live' : 'demo',
  });
});

// ---- API: a debate turn (streamed) ----------------------------------------
app.post('/api/chat', (req, res) => {
  const { topicId, messages } = req.body || {};
  const topic = getTopic(topicId);

  if (!topic) {
    res.status(404).json({ error: `Unknown topic: ${topicId}` });
    return;
  }
  if (!Array.isArray(messages) || messages.length === 0) {
    res.status(400).json({ error: 'messages must be a non-empty array' });
    return;
  }

  // Validate the payload shape before touching the API.
  const sanitized = [];
  for (const m of messages) {
    if (m && (m.role === 'user' || m.role === 'assistant') && typeof m.content === 'string') {
      sanitized.push({ role: m.role, content: m.content });
    }
  }
  if (sanitized.length === 0) {
    res.status(400).json({ error: 'messages must contain {role, content}' });
    return;
  }

  // SSE response headers — one streamed reply, then the connection closes.
  res.setHeader('Content-Type', 'text/event-stream; charset=utf-8');
  res.setHeader('Cache-Control', 'no-cache, no-transform');
  res.setHeader('Connection', 'keep-alive');
  res.flushHeaders();

  const send = (obj) => {
    res.write(`data: ${JSON.stringify(obj)}\n\n`);
  };

  // Demo mode: no API key configured → stream pre-written rebuttals instead
  // of failing, so the site works out of the box. We gate on an explicit key
  // rather than on whether a client constructs: the SDK can resolve an ambient
  // ANTHROPIC_AUTH_TOKEN from the shell, which would wrongly look "live" and
  // then fail against the real endpoint. With a key set, the explicit apiKey
  // option wins over any ambient credential.
  if (!API_KEY) {
    streamDemoReply(res, send, topic, sanitized);
    return;
  }

  let client;
  try {
    client = buildClient();
  } catch (err) {
    send({ type: 'error', message: friendlyError(err) });
    res.end();
    return;
  }

  const stream = client.messages.stream({
    model: MODEL,
    max_tokens: 4096,
    thinking: { type: 'adaptive' },
    system: topic.prompt,
    messages: sanitized,
  });

  stream.on('text', (delta) => send({ type: 'delta', text: delta }));

  stream.finalMessage().then(
    () => {
      send({ type: 'done' });
      res.end();
    },
    (err) => {
      // Typed exceptions, most-specific first.
      let message;
      if (err instanceof Anthropic.AuthenticationError) {
        message =
          'Your Anthropic API key was rejected. Check ANTHROPIC_API_KEY in the .env file, then restart the server.';
      } else if (err instanceof Anthropic.RateLimitError) {
        message = 'Rate limit hit — give it a few seconds and try again.';
      } else if (err instanceof Anthropic.BadRequestError) {
        message = `The request was rejected by the API: ${err.message}`;
      } else if (err instanceof Anthropic.APIError) {
        message = `API error: ${err.message}`;
      } else {
        message = friendlyError(err);
      }
      send({ type: 'error', message });
      res.end();
    }
  );

  // If the browser goes away, stop billing tokens.
  res.on('close', () => {
    try {
      stream.abort();
    } catch {
      // already finished
    }
  });
});

// ---- Startup ---------------------------------------------------------------
app.listen(PORT, () => {
  console.log('⚖️  Devil\'s Advocate is running at http://localhost:' + PORT);
  console.log('   Model: ' + MODEL);
  console.log('   API endpoint: ' + BASE_URL);
  if (!API_KEY) {
    console.log(
      '   Running in demo mode (pre-written rebuttals). Add ANTHROPIC_API_KEY to .env ' +
        'for a live Claude debate.'
    );
  }
});

// ---- Demo mode -------------------------------------------------------------
// Pre-written debate replies when no API key is configured. Works its way
// through the topic's rebuttals in order, then appends a closing note.
const DEMO_CLOSING =
  "I can keep swinging — but right now I'm reading from a script. Add an ANTHROPIC_API_KEY to your .env file and restart the server, and I'll debate you for real, adapting to everything you say.";

function streamDemoReply(res, send, topic, messages) {
  send({ type: 'mode', mode: 'demo' });

  const assistantCount = messages.filter((m) => m.role === 'assistant').length;
  const round = Math.max(0, assistantCount - 1); // the opening is the first assistant message
  const replies = topic.demoReplies || [];
  const text =
    (replies[Math.min(round, replies.length - 1)] || replies[0]) +
    (round >= replies.length - 1 ? '\n\n' + DEMO_CLOSING : '');

  // Stream it word-by-word so it feels like a live reply.
  const words = text.split(/(?<=\s)/);
  let i = 0;
  let closed = false;
  res.on('close', () => {
    closed = true;
  });
  function tick() {
    if (closed) return;
    if (i >= words.length) {
      send({ type: 'done' });
      res.end();
      return;
    }
    send({ type: 'delta', text: words[i] });
    i += 1;
    setTimeout(tick, 25);
  }
  tick();
}

function friendlyError(err) {
  const msg = err && err.message ? err.message : String(err);
  if (/auth/i.test(msg) && /resolve/i.test(msg)) {
    return 'No API key found. Add ANTHROPIC_API_KEY to your .env file and restart the server.';
  }
  return `Something went wrong: ${msg}`;
}
