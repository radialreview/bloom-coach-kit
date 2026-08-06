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
  - `assets/coach-memory-template.md` — seed for `~/.claude/agent-memory/`
  - `assets/my-assistant-template.md` — the coach's cheat sheet
- `agents/meeting-prep.md` — specialist
- `agents/scheduler.md` — specialist
- `agents/email-drafter.md` — specialist
- `agents/researcher.md` — specialist
- `workshop/` — facilitator materials, not part of the plugin

## Notes for maintainers

Plugin-provided agents ignore `hooks`, `mcpServers`, and `permissionMode` frontmatter.
The persona written by the skill lands in `~/.claude/agents/` instead, where those fields
work if we ever need them.

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
