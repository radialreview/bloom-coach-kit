---
name: set-up-my-morning
description: Sets up the coach's weekday morning brief — a scheduled task on their own computer where their assistant reaches out first thing with the day's shape. Use when a coach says anything like "set up my morning", "I want a daily brief", "have April check in with me each morning", "morning routine", or when they're wrapping up the workshop and want their assistant to come to them instead of waiting to be opened.
---

# Set Up My Morning

This is the moment the assistant stops being something the coach opens and starts being someone
who shows up. Every weekday morning, {{NAME}} puts together a short brief and has it waiting.

Same rules as the other skills: the coach is **not technical**. No YAML, no cron talk, no file
paths. "Every weekday at 7:30" is the entire vocabulary.

---

## Phase 1 — Preflight (silent)

1. **Find the persona** the same way `add-a-specialist` does: `~/.claude/agents/*.md` containing
   `<!-- bloom-coach-kit -->`, disambiguated by the folder's `.claude/settings.json` `agent` key
   or its `CLAUDE.md` block. No persona → offer `meet-your-assistant` first; the brief has to
   come *from* someone.

2. **Read the coach's memory file** (`~/.claude/agent-memory/{{SLUG}}/about-my-coach.md`). The
   one-job answer and any client names shape what the brief should contain.

3. **Note which connectors are live.** A calendar-heavy brief with no calendar connected is a
   daily embarrassment. Offer only ingredients that will actually work, and say why in plain
   language if one's missing.

---

## Phase 2 — Two questions

Use `AskUserQuestion`. This phase is two questions, not an interview.

**1. What time?** Options: 6:30 / 7:00 / 7:30 / 8:00, or let them name one. Weekdays is the
default — only ask about days if they bring it up.

**2. What's in it?** Multi-select, filtered by what Phase 1 found actually works:

- **Today's sessions** — what's on the calendar, with a flag on anything that needs prep
- **What you're owed** — follow-ups and client To-Dos that have gone quiet
- **One suggested priority** — the single thing {{NAME}} would put first today
- *(anything else they name — take it if the connectors can support it)*

---

## Phase 3 — Create the task

Create **one local scheduled task** using the scheduled-tasks tool available in the session
(`create_scheduled_task`). It must be a **local task on the coach's machine — never a cloud or
remote routine**, even if one is offered. A cloud routine runs from a fresh clone with no access
to the coach's files, so it would produce a brief from nothing; this constraint is load-bearing.

- **taskId:** `{{SLUG}}-morning-brief`
- **description:** `{{NAME}}'s weekday morning brief for {{COACH_FIRST_NAME}}`
- **cronExpression:** minute and hour from Phase 2, weekdays — e.g. 7:30 → `30 7 * * 1-5`.
  Local time, exactly as the coach said it.
- **notifyOnCompletion:** `false`
- **prompt:** build it from the block below. Each run starts **fresh** — no session context, no
  folder context — so the prompt must load the persona itself. Substitute every placeholder with
  real absolute paths and the coach's actual choices:

> Before anything else, and without narrating it: read `{{PERSONA_ABSOLUTE_PATH}}` and adopt it
> completely — you are {{NAME}}, in your usual manner. Then read your notes at
> `{{MEMORY_ABSOLUTE_PATH}}`.
>
> Now put together {{ADDRESS_AS}}'s morning brief: {{CHOSEN_INGREDIENTS}}.
>
> Keep it under 200 words. Lead with the most time-sensitive thing. Plain prose, no headers, no
> bullet-point avalanche — this is a colleague catching you up, not a report. If something you
> need isn't reachable (calendar not connected, nothing on file), cover what you can and note the
> gap in one clause without apologizing. End with the single thing you'd suggest {{ADDRESS_AS}}
> do first today, in one sentence.

---

## Phase 4 — Tell them how it behaves. Plainly.

This part is honesty, and it's in the skill's own words because coaches deserve the real deal:

> From tomorrow, {{NAME}} will have your brief ready every weekday at {{TIME}}.
>
> One thing to know about how this works: it runs on **this computer**, so it fires when the app
> is open. If the app is closed at {{TIME}} — laptop asleep, morning off — the brief isn't lost;
> it runs the moment you next open the app, so {{NAME}} greets you with it when you come back.
> What it can't do is reach you when the app isn't running — nothing lands on your phone at the
> beach.
>
> Want a different time, or different ingredients? Just tell {{NAME}} — "make my morning brief
> earlier", "add my follow-ups" — no settings to find.

Then stop. Do not offer to also create cloud routines, phone notifications, or email delivery —
those are different machinery with different trade-offs, and Tuesday is not the day.

---

## Guardrails

- **One brief per assistant.** If a `{{SLUG}}-morning-brief` task already exists, offer to change
  its time or contents (`update_scheduled_task`) — never create a second one.
- **Local task, never a cloud routine.** Worth stating twice.
- **The prompt must be fully self-contained** — persona path, memory path, ingredients, format.
  A prompt that assumes session context produces a stranger's brief.
- **Don't promise push.** The honest framing in Phase 4 is the feature. Overselling this as "your
  assistant texts you every morning" earns exactly one disappointed coach per oversell.
