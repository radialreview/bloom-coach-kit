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
   `<!-- bloom-coach-kit -->`, disambiguated by the persona path in the folder's `CLAUDE.md`
   block. **If the folder's `.claude/settings.json` has an `agent` key pointing at a bloom
   persona, remove that key** (preserve the rest of the file) — earlier kit versions wrote it,
   and headless runs honor it: the persona loads as a real agent, its tools whitelist is
   enforced mechanically, and the run loses every connector. This was the single largest cause
   of connector-less briefs. No persona → offer `meet-your-assistant` first; the brief has to
   come *from* someone.

2. **Read the coach's memory file** (`~/.claude/agent-memory/{{SLUG}}/about-my-coach.md`). The
   one-job answer and any client names shape what the brief should contain.

3. **Know how scheduled runs reach connectors — it's gated, not absent.** Local scheduled runs
   can and do call the coach's connectors unattended (verified 2026-08-05 on a working machine:
   calendar, Gmail, Slack, 13 runs a day). Three gates, each observed silently breaking briefs:
   - **The machine's headless auth must be the claude.ai login.** Connectors are fetched only
     under a claude.ai subscription login; when API-key or console-billing auth is active for
     CLI/headless runs, they're suppressed entirely — runs complete but the tools are simply
     absent, with no error. Coaches signing in through the app normally never hit this; a
     machine with developer history can (a stale CLI credential). If a run reports no connector
     tools exist, this is the first thing to check: `claude` in a terminal, `/status`, and
     `/login` with the claude.ai account if it shows anything else.
   - **Approvals are per-task.** Connector tool calls need permission grants, and grants made
     during a run are **stored on the task and auto-applied to future runs**. A task that never
     had a supervised first run has no grants. This is why Phase 3 ends with a mandatory Run now.
   - **No `agent` key in the folder's settings** (checked in step 1 above). This is the
     mechanical version of the whitelist problem and the one that actually bit: headless runs
     honor the key, load the persona as a real agent, and its `tools:` whitelist strips every
     connector at the loader — no prompt can reach a tool that was never attached. Verified
     both ways 2026-08-06: key present, no calendar; key removed, live events. The task
     prompt's floor-not-ceiling line handles the softer variant (the run *reading* the persona
     file and believing the whitelist), so keep both defenses.
   Offer connector-backed ingredients only for connectors actually authorized in this session,
   and build every one with an honest notes fallback.

---

## Phase 2 — Two questions

Use `AskUserQuestion`. This phase is two questions, not an interview.

**1. What time?** Options: 6:30 / 7:00 / 7:30 / 8:00, or let them name one. Weekdays is the
default — only ask about days if they bring it up.

**2. What's in it?** Multi-select, shaped by which connectors Phase 1 found live:

- **Today's sessions** — from the live calendar when it's connected, from {{NAME}}'s notes when
  it isn't; flagged for prep either way
- **What you're owed** — follow-ups and client To-Dos that have gone quiet; from notes, plus
  the inbox when email is connected
- **Growth calls** — a daily nudge to protect outreach time: a concrete window picked from the
  day's open calendar gaps, their call target, and — only when {{NAME}}'s notes actually hold
  them — a name or two worth reaching
- **One suggested priority** — the single thing {{NAME}} would put first today
- *(anything else they name — take it if the connectors and notes can support it; say so
  plainly if not)*

If they pick **Growth calls**, ask one extra question: *"How many calls a day are you aiming
for?"* Many Bloom coaches run a five-a-day discipline — offer 5 as the default, take whatever
they say. Two rules for the ingredient's wording in the task prompt: the nudge must name a
**specific window** ("your 10–11 gap"), because "make your calls today" is noise a coach reads
past by Thursday — and it must **never invent a name to call**. Names come from the notes or
the nudge stays about the time block; a made-up prospect kills trust in the whole brief.

---

## Phase 3 — Create the task

Create **one local scheduled task** using the scheduled-tasks tool available in the session
(`create_scheduled_task`, from the built-in `scheduled-tasks` MCP server). It must be a **local
task on the coach's machine — never a cloud or remote routine**, even if one is offered. A cloud
routine runs from a fresh clone with no access to the coach's files, so it would produce a brief
from nothing; this constraint is load-bearing.

If the tool genuinely isn't in this session (check before claiming so — persona whitelists
written before v0.1.6 blocked it), don't fake success and don't substitute a cloud routine. Save
the coach's choices to memory, say plainly that this needs a fresh session, and pick it up there.

- **taskId:** `{{SLUG}}-morning-brief`
- **description:** `{{NAME}}'s weekday morning brief for {{COACH_FIRST_NAME}}`
- **cronExpression:** minute and hour from Phase 2, weekdays — e.g. 7:30 → `30 7 * * 1-5`.
  Local time, exactly as the coach said it.
- **notifyOnCompletion:** `false`
- **prompt:** build it from the block below. Each run starts **fresh** — no session context, no
  folder context — so the prompt must load the persona itself. Substitute every placeholder with
  real absolute paths and the coach's actual choices:

> Before anything else, and without narrating it: read `{{PERSONA_ABSOLUTE_PATH}}` and adopt its
> persona completely — you are {{NAME}}, in your usual manner. One important exception: the
> `tools:` line in that file is loader configuration, a floor rather than a ceiling — it is NOT
> a limit on you in this run. Use any tool actually available to you here. Then read your notes
> at `{{MEMORY_ABSOLUTE_PATH}}` and anything else in that directory that looks relevant.
>
> You are running as {{ADDRESS_AS}}'s scheduled morning brief (timezone {{TIMEZONE}}).
>
> **Step 1 — try the live sources.** Search your actually-available tools for
> {{NEEDED_CAPABILITIES}} — connector tools are UUID-namespaced, so search by capability
> (e.g. "calendar list events"), never by a remembered server ID. Pull what the ingredients
> need. If a permission prompt blocks a call or the tool genuinely isn't in this run, fall back
> to your notes — say which source you used in one plain clause, no apology, and never imply
> you checked live data you didn't.
>
> **Step 2 — the brief:** {{CHOSEN_INGREDIENTS}}.
>
> Keep it under 200 words. Lead with the most time-sensitive thing. Plain prose, no headers, no
> bullet-point avalanche — this is a colleague catching you up, not a report. If a part is thin,
> cover what you can in a clause and move on. End with the single thing you'd suggest
> {{ADDRESS_AS}} do first today, in one sentence.
>
> **Step 3 — update the page.** Write the brief to
> `{{MEMORY_DIR}}\morning-brief.md` as Markdown: first line `# {{NAME}} — {{DAY_AND_DATE}}`,
> then the brief exactly as composed, then a final italic line noting when it was built and the
> source (live calendar or your notes). Then check `{{MEMORY_DIR}}\morning-brief-url.txt`:
> if it exists, publish with the Artifact tool passing that stored URL so the **same page
> updates in place**; if it doesn't exist yet, publish fresh, then write the returned URL into
> that file. Favicon `☀️`, keep it identical every day. Never mint a new page when a stored URL
> exists — {{ADDRESS_AS}} has it bookmarked.
>
> Deliver the same brief text as your run summary too, so it reads well from the notification.

**Then run it once, supervised — this step is mandatory, not a nicety.** Have the coach click
Run now on the Routines page (or run it from here) and **approve the permission prompts when
they appear** — connector calls and the Artifact publish alike. Approvals granted during a run
are stored on the task and auto-applied to every future run — this supervised first run is the
only thing standing between the coach and a 7:30 brief silently blocked on a permission prompt
nobody's there to answer. It also does two more jobs: it shows them their first brief on the
spot, and it **mints their page** — the artifact URL the run stores and reuses every morning.
Have the coach open that page and bookmark it before you call this done; the bookmark is the
whole point of Step 3.

---

## Phase 4 — Tell them how it behaves. Plainly.

This part is honesty, and it's in the skill's own words because coaches deserve the real deal:

> From tomorrow, {{NAME}} will have your brief ready every weekday at {{TIME}} — and it always
> lands on the same page, the one you just bookmarked. That's your spot: open it with your
> coffee and the morning's brief is sitting there. No menus, no clicking around.
>
> One thing to know about how this works: it runs on **this computer**, so it fires when the app
> is open. If the app is closed at {{TIME}} — laptop asleep, morning off — the brief isn't lost;
> it runs the moment you next open the app, and the page catches up then. What it can't do is
> reach you when the app isn't running — the page keeps yesterday's brief until the app wakes
> up, so check the date at the top.
>
> Also: the brief pulls your live calendar where it can — we just approved that together — and
> works from {{NAME}}'s notes for the rest. So the more {{NAME}} knows about your clients and
> your week, the better every morning gets.
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
- **Never skip the supervised first run.** Unapproved connector calls are the most likely way
  this feature dies silently in week two.
- **Live-or-fallback, stated honestly.** The brief names its source in a clause and never
  implies it checked live data it didn't. A confident brief built on nothing is the worst
  output this skill can produce.
- **Never hardcode a connector server ID into the prompt.** They're UUID-namespaced and change;
  the prompt searches by capability at run time.
- **One page per assistant, forever.** The stored-URL file is what prevents a new artifact
  being minted every morning. If the coach reports "my page stopped updating," the likely
  causes in order: the run is publishing to a fresh URL (check the url file exists and the
  prompt passes it), the app hasn't been open yet today (check the date on the page), or the
  publish call lost its approval (re-run supervised).
- **Don't promise push.** The honest framing in Phase 4 is the feature. Overselling this as "your
  assistant texts you every morning" earns exactly one disappointed coach per oversell.
