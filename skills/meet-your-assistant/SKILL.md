---
name: meet-your-assistant
description: Creates the coach's named personal assistant — an orchestrator agent with a personality and a roster of specialists it delegates to. Interviews the coach conversationally, then writes their persona agent, wires it as the default agent for their folder, and seeds its memory. Use this whenever a coach wants to set up, create, name, or personalize their assistant, says anything like "set up my assistant", "I want to build my AI assistant", "meet my assistant", "create my personal assistant", or is going through the Bloom coach AI workshop for the first time. Also use it when a coach wants to rename their assistant, change its personality, or add specialists to an existing one.
---

# Meet Your Assistant

This skill gives a Bloom coach a working personal assistant in about ten minutes.

The coach is **not technical**. They are a business coach who facilitates Bloom Growth OS
meetings for their clients. They will not read YAML, will not edit JSON, and will not open a
terminal. Everything below happens conversationally. Never show the coach a config file,
a file path they have to type, or a code block. Talk to them like a colleague setting up a
new hire's desk.

The emotional goal matters as much as the technical one. By the end, the coach should feel
like they hired someone, not configured something.

---

## Phase 1 — Preflight (silent)

Do this before saying anything to the coach. Do not narrate it.

1. **Check the working folder.** If the current folder is a git repository, that's a problem —
   sessions get isolated worktree copies and the coach will be confused about where their
   files went. Tell them plainly: *"The folder you've got open is set up for software
   projects, which will make this behave oddly. Let's use a regular folder instead — do you
   have one where you keep your coaching notes and client files?"* Then use the folder they
   name.

2. **Check whether an assistant already exists.** Look for `~/.claude/agents/*.md` files that
   contain the marker comment `<!-- bloom-coach-kit -->`. If one exists, do NOT start over.
   Say: *"Looks like you've already got [Name]. Want to update them, or start fresh with
   someone new?"* If updating, skip to Phase 3 and only change what they ask for. Never
   silently overwrite an existing assistant — coaches will have invested in this one.

3. **Note which connectors are live.** Check what tools are actually available in this session
   (calendar, email, CRM, etc.). You will offer specialists in Phase 2 based on what will
   actually work. Offering an email specialist when Gmail isn't connected sets the coach up
   to watch it fail.

4. **Confirm `~/.claude/agents/` exists** and create it if not.

---

## Phase 2 — The interview

Open warmly and set expectations for length:

> Let's hire you an assistant. I'll ask you six quick things, then they'll be ready to meet
> you. Takes about five minutes.

Ask these using `AskUserQuestion` with tappable options wherever possible — coaches on
laptops in a workshop room type slowly, and options move faster than free text. Ask them
one or two at a time, not all six at once. Keep your own commentary between questions to a
single sentence.

**1. Name.** Free text. *"What do you want to call them?"*
If they hesitate or say "I don't know", offer four suggestions immediately rather than
waiting — something like Ada, Sol, Marlowe, June. Never let this stall; a stuck coach here
loses momentum for the whole session.

**2. Personality.** Options:
- Warm and encouraging — checks in on you, celebrates wins
- Dry and efficient — no small talk, just the work
- Calm and steady — measured, unhurried, good under pressure
- Playful — light, a bit of humor, keeps things human
- *(let them describe their own)*

Their answer selects a preset from `assets/personalities.md`, which carries both the behavioral
block and the color. Don't improvise a personality description — use the file.

**3. How should they address you?** Options: first name / formal (Mr./Ms. + last) / a nickname
they specify / "Coach".

**4. Tell me about your practice.** Free text, and **ask for detail** — this is the single
richest input in the whole interview and everything downstream gets better with more of it.
Prompt them: *"How many clients, what does a typical week look like, what's the part of the
job you'd most like off your plate?"* If they give one line, ask one follow-up. Don't ask
twice.

**5. Which specialists should they have?** Multi-select, from the roster that's actually
available given Phase 1:
- **Scheduler** — calendar, availability, booking client sessions
- **Email drafter** — writes and revises your client emails
- **Researcher** — background on companies and people before a meeting
- **Meeting prep** — pulls together what you need before a client's Bloom Weekly or Quarterly

Default all four to selected. If a connector is missing for one, say so in plain language:
*"I'd leave the scheduler off for now — your calendar isn't connected yet, so they'd have
nothing to look at. Easy to add later."*

**6. The one job.** *"What's the one recurring thing you'd hand them tomorrow if you could?"*
Free text. This feeds their memory file and their commitment card.

---

## Phase 3 — Write the four files

Derive a slug from the name: lowercase, spaces to hyphens, strip anything that isn't a letter,
number, or hyphen. `Sol` → `sol`. `Ms. Marple` → `ms-marple`.

Write all four. Use the templates in `assets/`. Substitute every `{{PLACEHOLDER}}` — a template
that still contains `{{` when you write it out is a bug the coach will see.

**Do NOT write an `agent` key into the folder's `.claude/settings.json`.** Earlier versions of
this kit did, and it broke the morning brief invisibly: desktop GUI sessions ignore the key, but
**headless scheduled-task runs honor it** — they load the persona as a real agent, its `tools:`
whitelist is mechanically enforced, and every connector (calendar, email) is stripped from the
run. Verified live 2026-08-06: same task, same prompt — key present, no calendar; key removed,
live events. If the folder's settings already contain an `agent` key pointing at a persona with
the `<!-- bloom-coach-kit -->` marker, **remove that key** (preserve everything else in the
file) — it's a leftover from an earlier install.

Where the content comes from:

| Placeholder | Source |
|---|---|
| `{{NAME}}`, `{{SLUG}}` | Q1 |
| `{{PERSONALITY_DESCRIPTION}}`, `{{COLOR}}` | the matching preset in `assets/personalities.md` |
| `{{ADDRESS_AS}}` | Q3 |
| `{{COACH_NAME}}`, `{{PRACTICE_SUMMARY}}`, `{{CLIENT_COUNT}}`, `{{WEEK_SHAPE}}` | Q4 |
| `{{CHOSEN_SPECIALISTS}}`, `{{ROSTER_DESCRIPTIONS}}`, `{{ROSTER_PLAIN_ENGLISH}}` | Q5 + `assets/roster.md` |
| `{{THE_ONE_JOB}}` | Q6 |
| `initialPrompt` | **not a placeholder** — leave the template's text alone. See below |
| `{{EXAMPLE_CLIENT}}` | a real client name from Q4 if they gave one; otherwise write the example lines with a generic "your client" phrasing rather than leaving a bracket in the file |
| `{{DATE}}` | today's date, plainly formatted — "5 August 2026", not an ISO stamp |

If the coach gave a one-word answer to Q4, don't leave `{{CLIENT_COUNT}}` or `{{WEEK_SHAPE}}`
empty — write "not yet known" and let the assistant learn it later. An empty heading reads as
broken; an honest gap doesn't.

### 1. The persona — `~/.claude/agents/{{SLUG}}.md`

From `assets/persona-template.md`.

Two fields need care:

- **`tools:`** — the `Agent(...)` list must contain **only** the specialists the coach chose in
  question 5. This is what makes the assistant aware of its actual roster instead of guessing
  at agents that aren't there. The `{{ROSTER_DESCRIPTIONS}}` block must list exactly the same
  set — pull both from `assets/roster.md`.

  **Copy the agent names verbatim from `assets/roster.md`. Do not retype them from the question 5
  labels.** The specialists ship in the plugin, so each name carries the `bloom-coach-kit:` prefix
  — `bloom-coach-kit:scheduler`, not `scheduler`. Without the prefix the name doesn't resolve, and
  because nothing errors at load time the coach finds out only when their first request fails.
  This is the single easiest thing to get wrong in the whole skill.

  **Keep the four `mcp__scheduled-tasks__*` entries** in the template's list. They're what
  `set-up-my-morning` rides on — an explicit `tools:` field is a whitelist, and dropping them
  means the assistant can't create or change the coach's morning brief. They're safe to
  enumerate because they're a built-in desktop server with stable names, unlike connector MCP
  tools.
- **`initialPrompt:`** — **leave the template's text as it is.** Do not replace it with a written
  greeting.

  This field is counterintuitive and getting it wrong costs the coach the best moment in the
  workshop. `initialPrompt` is auto-submitted as **the coach's first turn**, not as the assistant's
  first message. Text like *"Good morning Sarah, I see you've got three clients mid-Quarterly"*
  placed here is delivered to the assistant **as though the coach typed it** — so the coach sees
  either nothing useful or their assistant replying to a message they never sent.

  The template instead holds an *instruction* that makes the assistant greet them. The
  personalization comes from the assistant reading its memory file at that moment, which is better
  than a greeting frozen at setup time — it stays accurate as the coach's practice changes.

  It also has to survive the coach typing something immediately, because this text is prepended to
  whatever they send. The template's wording handles both cases; rewriting it usually breaks the
  second one.

  The one thing worth tailoring is voice: if the chosen personality is `dry`, trim the warmth out
  of the instruction so the greeting doesn't fight the manner. Keep the structure.

Do not set a `model:` field. The assistant inherits the coach's session model, which keeps it
working regardless of which plan they're on.

Keep the `<!-- bloom-coach-kit -->` marker line in the body. That's what Phase 1 looks for on a
re-run. It must stay *below* the closing `---` — anything above the opening `---` stops the
frontmatter from being read at all, and the persona silently loses its name, roster, and memory.

### 2. The activation — `CLAUDE.md` in their folder

From `assets/claude-md-template.md`. Fill `{{PERSONA_PATH}}` and `{{MEMORY_PATH}}` with the real
absolute paths of the files from steps 1 and 3.

This is the **only** activation mechanism, on purpose. `CLAUDE.md` is project memory — every
session in the folder loads it, on every surface: desktop GUI, terminal CLI, and scheduled-task
runs. It tells the session to read the persona file and become {{NAME}} before its first reply,
while leaving the session's own toolset intact — which is what keeps connectors reachable in
scheduled runs. (The `agent` settings key was tried and removed; see the Phase 3 warning above.)

**Merge, don't overwrite.** If a `CLAUDE.md` already exists in the folder, replace only the block
between `<!-- bloom-coach-kit:persona -->` and `<!-- /bloom-coach-kit:persona -->` if present, or
append the block at the end if not. Never touch anything else in the file.

### 3. Seeded memory — `~/.claude/agent-memory/{{SLUG}}/about-my-coach.md`

From `assets/coach-memory-template.md`. Built from answers 3, 4, and 6.

This is the highest-leverage file in the set. Because the persona declares `memory: user`, this
directory persists across every future conversation — so the assistant knows the coach on first
contact instead of starting cold. Write it as notes an assistant would keep about their boss:
specific, useful, no filler.

### 4. The cheat sheet — `MY-ASSISTANT.md` in their folder

From `assets/my-assistant-template.md`. Plain English, no jargon. Written for a coach who finds
it three weeks from now, confused, without you in the room. Include the name, what each
specialist does, how to restart, what to do if the greeting stops appearing, and who to contact.

Use the *Cheat sheet* entries from `assets/roster.md` here, not the routing ones — the routing
descriptions are written for the assistant and name things the coach doesn't need to know about.

---

## Phase 4 — The handoff ceremony

The persona doesn't take effect until the coach starts a new session. Don't apologize for this —
stage it.

Tell the coach, in your own words:

> {{NAME}} is ready. Start a new session in this same folder, and say anything — "good morning"
> works. {{NAME}} won't speak until you do, but the moment you say hello, you'll see they already
> know who you are.
>
> One thing to know: {{NAME}} doesn't do the work themselves. They've got {{N}} specialists
> they hand things off to. So just tell them what you need in plain language and let them
> figure out who does it.

Two details that matter in that instruction: **same folder** — the wiring lives in the folder
from Phase 3, and a session opened anywhere else won't have {{NAME}} in it — and **the coach
speaks first**. Do not promise that {{NAME}} greets them before they've typed anything; the
assistant's first words arrive in reply to theirs.

Then stop. Do not keep talking, do not offer more configuration, do not summarize what you
wrote. The restart is the moment; let them go have it.

---

## Guardrails

- **Never write outside `~/.claude/` and the coach's chosen folder.**
- **Never show the coach YAML, JSON, or a file path they'd have to type.** If something goes
  wrong, describe it in plain language and fix it yourself.
- **Handle interruption.** If the coach quits partway through the interview, do not leave a
  half-written persona in `~/.claude/agents/`. Write files only in Phase 3, all at once, after
  the interview is complete.
- **One-word answers are fine.** A coach who answers everything in one word still gets a working
  assistant. Fill gaps with sensible defaults rather than pushing for more.
- **Three-paragraph answers are also fine.** Use the detail; don't truncate it out of the memory
  file.
- **Don't offer a specialist whose connector isn't authorized.** Say why, and say it's easy to
  add later.
