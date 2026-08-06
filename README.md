# Bloom Coach Kit

Gives a Bloom Growth OS coach a named personal assistant that delegates to specialists.

## Install

```
/plugin marketplace add radialreview/bloom-coach-kit
/plugin install bloom-coach-kit@bloom-coach-kit
```

Then run `/bloom-coach-kit:meet-your-assistant` and answer six questions.

Requires a paid Claude plan — the Code tab isn't available on the free tier.

## What's here

- `skills/meet-your-assistant/` — the interview + setup skill
  - `assets/persona-template.md` — the orchestrator written to `~/.claude/agents/`
  - `assets/personalities.md` — the four personality presets and their colors
  - `assets/roster.md` — specialist descriptions, in both persona and coach-facing wording
  - `assets/claude-md-template.md` — the folder activation block (see maintainer notes)
  - `assets/coach-memory-template.md` — seed for `~/.claude/agent-memory/`
  - `assets/my-assistant-template.md` — the coach's cheat sheet
- `skills/add-a-specialist/` — grows the roster after the workshop; wires the persona's
  `Agent(...)` line, which is the step that silently breaks routing if skipped
- `skills/set-up-my-morning/` — creates the local weekday morning-brief task
- `agents/meeting-prep.md` — specialist
- `agents/scheduler.md` — specialist
- `agents/email-drafter.md` — specialist
- `agents/researcher.md` — specialist
- `evals/workshop-eval-cases.md` — manual test cases with pass criteria
- `workshop/` — facilitator materials, not part of the plugin

## Notes for maintainers

Plugin-provided agents ignore `hooks`, `mcpServers`, and `permissionMode` frontmatter.
The persona written by the skill lands in `~/.claude/agents/` instead, where those fields
work if we ever need them.

The persona is activated by two mechanisms on purpose (verified 2026-08-05): the desktop app
ignores the `agent` key in project `.claude/settings.json`, while the terminal CLI honors it.
The `CLAUDE.md` block written to the coach's folder carries activation on desktop; the settings
key covers the CLI and takes over if a future desktop build honors it. Both point at the same
persona file. Don't remove either.

Model policy: the persona deliberately has no `model:` field (inherits the coach's session
model, works on every plan tier); the four specialists pin `sonnet`; scheduled-task runs are
created without a model and inherit the coach's app default. The coach-facing guidance for all
of this is one cheat-sheet entry: switch the picker to Sonnet if you hit usage limits.

Routine fine-tuning (support, not training): the desktop **Edit routine** dialog can set a
per-routine model, permissions, and working folder after creation — the `create_scheduled_task`
tool can't. If a coach's daily brief is eating their plan, Edit routine → Model → Sonnet 5.
Routines also fire with a randomized delay of several minutes, so never demo one by waiting for
its scheduled time — run it manually.

Scheduled runs and connectors (final model, confirmed 2026-08-06 against a machine where they
work and one where they didn't): account connectors (calendar, email, Slack) **are** available
to local scheduled runs, behind three gates. First, **headless auth must be the claude.ai
subscription login** — under API-key/console-billing auth (typical on developer machines with a
stale CLI credential) connectors are suppressed entirely: runs complete, tools are silently
absent. Fix: `claude` → `/status` → `/login` with the claude.ai account. Coaches on clean
machines don't hit this. Second, **approvals are per-task**: grants made during a run are
stored on the task and auto-applied to future runs — the supervised first run where the coach
approves the calls is mandatory. Third, the run adopts the persona file, whose `tools:`
whitelist must be framed as a floor, not a ceiling, or the run self-limits. Task prompts search
for connector tools by capability, never by server ID — connector names are UUID-namespaced
per account.

Third-party marketplaces default to auto-update OFF. Tell coaches how to toggle it, or
re-run install after a release.

Run `/reload-plugins` after changing anything outside `SKILL.md`. `SKILL.md` edits are picked
up live; agents, the manifests, and `.mcp.json` are not.

The `<!-- bloom-coach-kit -->` marker in `persona-template.md` must stay below the closing `---`
of the frontmatter. Above it, the frontmatter stops parsing and every persona the skill writes
loses its name, roster, memory, and greeting.

`assets/roster.md` and the files in `agents/` have to be changed together — the roster file is
what the persona is told about its specialists.

## Tool declarations in specialists

`scheduler`, `email-drafter`, and `meeting-prep` deliberately omit the `tools` frontmatter
field so they inherit the coach's authorized connectors — MCP tool names vary per connector
and can't be safely enumerated in advance. `researcher` declares its tools explicitly
because it must NOT reach the coach's connectors; web and local files only.
