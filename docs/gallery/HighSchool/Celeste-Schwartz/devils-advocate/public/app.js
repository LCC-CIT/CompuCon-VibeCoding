// Devil's Advocate — frontend logic.
// Loads topics, opens a debate, and streams the debater's replies.

const $ = (sel) => document.querySelector(sel);

const topicView = $('#topic-view');
const debateView = $('#debate-view');
const topicGrid = $('#topic-grid');
const messagesEl = $('#messages');
const composer = $('#composer');
const userInput = $('#user-input');
const sendButton = $('#send-button');
const debateTopicTitle = $('#debate-topic-title');
const switchTopicBtn = $('#switch-topic');
const demoBanner = $('#demo-banner');

const topics = new Map(); // id -> topic
let currentTopic = null;
let history = []; // { role: 'user' | 'assistant', content: string }
let busy = false;

// ---------------------------------------------------------------------------
// Boot
// ---------------------------------------------------------------------------
async function init() {
  const [topicsRes, healthRes] = await Promise.all([
    fetch('/api/topics'),
    fetch('/api/health'),
  ]);
  const topicList = await topicsRes.json();
  for (const t of topicList) topics.set(t.id, t);

  let health = null;
  try {
    health = await healthRes.json();
  } catch {
    /* older server without /api/health — assume key is present */
  }
  if (health && health.hasApiKey === false) {
    demoBanner.classList.remove('hidden');
  }

  renderTopicGrid(topicList);

  // Enter key sends; Shift+Enter makes a newline.
  userInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      composer.requestSubmit();
    }
  });
  userInput.addEventListener('input', autoGrow);
}

function renderTopicGrid(topicList) {
  topicGrid.textContent = '';
  for (const t of topicList) {
    const card = document.createElement('button');
    card.type = 'button';
    card.className = 'topic-card';
    card.setAttribute('role', 'listitem');
    card.innerHTML = `
      <span class="topic-emoji">${t.emoji}</span>
      <span class="topic-name">${escapeHtml(t.name)}</span>
      <span class="topic-tagline">${escapeHtml(t.tagline)}</span>
      <span class="topic-go">Debate it →</span>
    `;
    card.addEventListener('click', () => openTopic(t));
    topicGrid.appendChild(card);
  }
}

// ---------------------------------------------------------------------------
// Opening a debate
// ---------------------------------------------------------------------------
function openTopic(topic) {
  currentTopic = topic;
  history = [{ role: 'assistant', content: topic.opening }];

  debateTopicTitle.textContent = `${topic.emoji} ${topic.name}`;
  messagesEl.textContent = '';
  addMessage('debater', topic.opening);

  topicView.classList.add('hidden');
  debateView.classList.remove('hidden');
  userInput.value = '';
  autoGrow();
  userInput.focus();
}

function switchTopic() {
  debateView.classList.add('hidden');
  topicView.classList.remove('hidden');
  currentTopic = null;
}

// ---------------------------------------------------------------------------
// Sending a turn
// ---------------------------------------------------------------------------
composer.addEventListener('submit', async (e) => {
  e.preventDefault();
  const text = userInput.value.trim();
  if (!text || busy || !currentTopic) return;

  history.push({ role: 'user', content: text });
  addMessage('user', text);
  userInput.value = '';
  autoGrow();
  setBusy(true);
  scrollToBottom();

  const bubble = addMessage('debater', '', { streaming: true });

  let replyText = '';
  let errorMsg = null;

  try {
    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ topicId: currentTopic.id, messages: history }),
    });

    if (!response.ok) {
      const body = await response.json().catch(() => ({}));
      throw new Error(body.error || `Server responded ${response.status}`);
    }
    if (!response.body) throw new Error('Streaming is not supported by this browser.');

    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let buffer = '';

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      buffer += decoder.decode(value, { stream: true });

      let idx;
      while ((idx = buffer.indexOf('\n\n')) !== -1) {
        const raw = buffer.slice(0, idx);
        buffer = buffer.slice(idx + 2);
        const line = raw.split('\n').find((l) => l.startsWith('data: '));
        if (!line) continue;
        let evt;
        try {
          evt = JSON.parse(line.slice(6));
        } catch {
          continue;
        }
        if (evt.type === 'delta') {
          replyText += evt.text;
          renderBubble(bubble, replyText);
          scrollToBottom();
        } else if (evt.type === 'error') {
          errorMsg = evt.message;
        } else if (evt.type === 'mode' && evt.mode === 'demo') {
          showDemoNote();
        } else if (evt.type === 'done') {
          // finish
        }
      }
    }
  } catch (err) {
    errorMsg = err.message || String(err);
  }

  bubble.classList.remove('streaming');

  if (errorMsg) {
    renderBubble(bubble, replyText);
    bubble.querySelector('.bubble').insertAdjacentHTML(
      'beforeend',
      `<div class="error-note">⚠️ ${escapeHtml(errorMsg)}</div>`
    );
  } else {
    renderBubble(bubble, replyText);
    history.push({ role: 'assistant', content: replyText });
  }

  setBusy(false);
  userInput.focus();
  scrollToBottom();
});

// ---------------------------------------------------------------------------
// Rendering
// ---------------------------------------------------------------------------
function showDemoNote() {
  if (messagesEl.querySelector('.demo-note')) return;
  const note = document.createElement('div');
  note.className = 'demo-note';
  note.textContent = 'demo mode — pre-written rebuttals. Add an API key for a live debate.';
  messagesEl.appendChild(note);
}

function addMessage(role, text, opts = {}) {
  const wrap = document.createElement('div');
  wrap.className = `msg ${role}`;
  wrap.innerHTML = `<div class="who">${role === 'user' ? 'You' : 'The Devil’s Advocate'}</div>
    <div class="bubble"></div>`;
  if (opts.streaming) wrap.querySelector('.bubble').classList.add('streaming');
  messagesEl.appendChild(wrap);
  if (text) renderBubble(wrap, text);
  return wrap;
}

function renderBubble(wrap, text) {
  wrap.querySelector('.bubble').innerHTML = markdown(text);
}

// A tiny, safe markdown-lite renderer: escape everything first, then format.
function markdown(text) {
  let html = escapeHtml(text);

  // Block-level: bullet lists, then paragraphs.
  const lines = html.split('\n');
  let out = '';
  let inList = false;
  for (const line of lines) {
    const listMatch = line.match(/^(\s*)[*-] (.+)$/);
    if (listMatch) {
      if (!inList) {
        out += '<ul>';
        inList = true;
      }
      out += `<li>${inline(listMatch[2])}</li>`;
    } else {
      if (inList) {
        out += '</ul>';
        inList = false;
      }
      const trimmed = line.trim();
      if (trimmed) out += `<p>${inline(trimmed)}</p>`;
    }
  }
  if (inList) out += '</ul>';
  return out;
}

function inline(text) {
  return text
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/__([^_]+)__/g, '<strong>$1</strong>')
    .replace(/(^|[^*])\*([^*]+)\*/g, '$1<em>$2</em>')
    .replace(/`([^`]+)`/g, '<code>$1</code>');
}

function escapeHtml(str) {
  return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function autoGrow() {
  userInput.style.height = 'auto';
  userInput.style.height = Math.min(userInput.scrollHeight, 160) + 'px';
}

function setBusy(b) {
  busy = b;
  sendButton.disabled = b;
  sendButton.textContent = b ? 'Arguing…' : 'Send';
  userInput.disabled = b;
}

function scrollToBottom() {
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

switchTopicBtn.addEventListener('click', switchTopic);

init();
