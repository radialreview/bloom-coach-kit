# The roster

Source of truth for the two roster placeholders in the templates. Include **only** the specialists
the coach selected in interview question 5 — the persona's `tools: Agent(...)` line, the
`{{ROSTER_DESCRIPTIONS}}` block, and the `{{ROSTER_PLAIN_ENGLISH}}` block must all list the same
set. A persona that describes a specialist it can't reach will try to route there and fail.

## Agent names — use these exact strings

The four specialists ship in the plugin, so their agent names are **namespaced with the plugin
name**. `{{CHOSEN_SPECIALISTS}}` must be built from these literal strings, comma-separated:

```
bloom-coach-kit:scheduler
bloom-coach-kit:email-drafter
bloom-coach-kit:researcher
bloom-coach-kit:meeting-prep
```

All four selected produces exactly:

```
tools: Agent(bloom-coach-kit:scheduler, bloom-coach-kit:email-drafter, bloom-coach-kit:researcher, bloom-coach-kit:meeting-prep), Read, Write, Edit, Glob, Grep, TodoWrite, AskUserQuestion, WebSearch
```

**Dropping the `bloom-coach-kit:` prefix breaks routing silently.** The bare name doesn't resolve,
but nothing errors at load time — the persona believes it has a roster and every delegation fails
in front of the coach. Never write `Agent(scheduler, ...)`.

Specialists added later by `add-a-specialist` are written to `~/.claude/agents/` rather than
shipped in the plugin, so those are **not** namespaced — they go in the same list under their bare
name. A grown roster is legitimately mixed:

```
tools: Agent(bloom-coach-kit:scheduler, bloom-coach-kit:meeting-prep, proposal-writer), ...
```

The rule is where the agent file lives, not when it was added: plugin agents take the prefix, and
anything in `~/.claude/agents/` does not.

- **`{{ROSTER_DESCRIPTIONS}}`** → the *Routing* entries below, copied into `persona-template.md`.
  Written for the persona: when to route there, and what comes back.
- **`{{ROSTER_PLAIN_ENGLISH}}`** → the *Cheat sheet* entries below, copied into
  `my-assistant-template.md`. Written for the coach. No jargon, no agent names, no file paths.

If you edit an agent file in `agents/`, update the matching entry here in the same change.

---

## scheduler

**Routing** (for the persona):

> - **scheduler** — anything about the calendar: finding availability, proposing times for a client
>   session, rescheduling, or "what does my week look like." Send it the client, the meeting type,
>   the rough window, and any timezone you know. Comes back with two to four proposed times with
>   timezones stated, a ready-to-send message proposing them, and flags on crowding or missing
>   buffer. It proposes and never books — the booking is always your coach's to confirm.

**Cheat sheet** (for the coach):

> - **Scheduling** — finds times that actually work, writes the message proposing them, and tells
>   you when a day is too full. It never puts anything on your calendar itself.

---

## email-drafter

**Routing** (for the persona):

> - **email-drafter** — anything written to a client or prospect: session follow-ups, nudges on
>   outstanding To-Dos, scheduling notes, the difficult conversations. Send it the recipient, the
>   purpose, and the tone if it matters. Comes back with a subject line, a body, and a short note on
>   anything it guessed at or left blank. If the tone could reasonably go gentle or firm, it returns
>   both, labeled. It drafts and never sends.

**Cheat sheet** (for the coach):

> - **Writing** — drafts your client emails in your voice, including the awkward ones. You always
>   read and send them yourself; nothing goes out without you.

---

## researcher

**Routing** (for the persona):

> - **researcher** — public background on a company, a person's professional history, or an
>   industry: before a first meeting with a prospect, ahead of an Annual, or when a client's market
>   context matters. Send it the subject and *why* you want it. Comes back with a one-page brief
>   that labels every claim verified, reported, or inferred, with dates and sources. It has no
>   access to your coach's connectors by design, so never route it anything that needs the
>   calendar, the inbox, or a client's private situation — and never hand it confidential detail
>   to search on. If a question can only be answered by revealing something confidential, it will
>   decline and tell you why. That's correct behavior, not a failure; bring it back to your coach
>   rather than working around it.

**Cheat sheet** (for the coach):

> - **Research** — public background on a company or a person before you meet them, with sources
>   and a clear line between what's confirmed and what's a guess. It only looks at public
>   information and won't search on anything your client told you in confidence.

---

## meeting-prep

**Routing** (for the persona):

> - **meeting-prep** — a specific named client session that's coming up: a Bloom Weekly,
>   Quarterly, Annual, or a one-off. Send it the client, the meeting type, and the date. Comes back
>   with an under-a-page brief: where they left off, open To-Dos and Quarterly Priorities with
>   owners, two to four things to watch for, questions worth opening with, and an explicit list of
>   what it couldn't find. Never route this one without a named client — a prep brief for the wrong
>   company is worse than none, and it cannot ask you which one you meant.

**Cheat sheet** (for the coach):

> - **Meeting prep** — pulls together what you need before a client session: where you left off,
>   what's still open, and what to watch for. Short enough to read in the parking lot.
