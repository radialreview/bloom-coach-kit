# BUILD BRIEF — bloom-coach-kit

Hand this to Claude Code in an empty repo. It is the full spec for the plugin plus the workshop
materials around it.

**Context:** 15 Bloom Growth OS coaches, external customers (not employees), non-technical.
Two-hour workshop Tuesday, 10:00–12:00, then an open floor session 1:00–2:30. Dry run with a
colleague (Stephanie) on Wednesday. Deliverable per coach: a named personal assistant that
delegates to a roster of specialists, running in the Claude Code tab of the desktop app.

---

## PART 1 — What already exists

These files are drafted and should be treated as the starting point, not rewritten from scratch.
They will be provided alongside this brief.

```
bloom-coach-kit/
├── .claude-plugin/plugin.json
├── README.md
├── agents/
│   ├── meeting-prep.md
│   ├── scheduler.md
│   ├── email-drafter.md
│   └── researcher.md
└── skills/meet-your-assistant/
    ├── SKILL.md
    └── assets/
        ├── persona-template.md
        ├── coach-memory-template.md
        └── my-assistant-template.md
```

Review them for consistency, but **do not restructure without asking.** The design decisions in
them are deliberate and were argued through.

---

## PART 2 — Gaps to fill (in priority order)

### P0 — Blocks install

**1. `.claude-plugin/marketplace.json` does not exist.**
Without it, `/plugin marketplace add <org>/bloom-coach-kit` fails. This is the file that makes the
repo installable by external users who are not in our Claude org. Write it with a single plugin
entry pointing at this repo root. Verify the JSON parses.

**2. Template placeholders are unfilled.** `persona-template.md` references placeholders whose
content was never written. The skill cannot produce a working persona without them:

- `{{PERSONALITY_DESCRIPTION}}` — write four preset blocks (warm and encouraging / dry and
  efficient / calm and steady / playful), each 2–4 sentences of behavioral instruction, not
  adjectives. "You open by asking how their week went" beats "you are warm." Put these in
  `assets/personalities.md` and have SKILL.md select from it.
- `{{ROSTER_DESCRIPTIONS}}` — one line per specialist as the *persona* should understand it:
  when to route there and what comes back. Must match the four agent files exactly.
- `{{ROSTER_PLAIN_ENGLISH}}` — same roster, written for the coach's cheat sheet. No jargon.
- `{{COLOR}}` — pick a value per personality preset so the assistant's name renders in a
  consistent color. Keep the mapping in `assets/personalities.md`.
- `{{SUPPORT_CONTACT}}` — leave as a placeholder with a comment; Mike fills this before Tuesday.

### P1 — Needed for the workshop to work

**3. `skills/add-a-specialist/SKILL.md`.**
Lets a coach grow their roster conversationally after the workshop — the maintenance answer for
month two. It must: ask what they want the new specialist to do, write a new agent file to
`~/.claude/agents/`, and **update the persona's `tools: Agent(...)` line to include it.** That last
step is the one that's easy to miss and silently breaks routing. Same rules as
`meet-your-assistant`: no YAML shown to the coach, merge don't clobber, restart to take effect.

**4. `skills/set-up-my-morning/SKILL.md`.**
Creates one **local** scheduled task that fires each weekday morning and has the assistant send the
coach a short brief. This is the 72-hour retention mechanism — the assistant reaches out to them
rather than waiting to be opened. Must be **local**, not a cloud routine (see constraints below).
Tell the coach plainly, in the skill's own words, that it only fires while the app is open and the
machine is awake.

**5. `evals/` with test prompts.**
Not a formal eval harness — just a markdown file of the cases to run manually on Wednesday, with
what correct behavior looks like for each:

- Terse coach: one-word answers to every interview question → still produces a working assistant
- Verbose coach: three-paragraph answers → detail lands in the memory file, isn't truncated
- Unusual practice shape: coach with 2 clients, or 30 → interview doesn't assume a middle case
- Re-run: running `meet-your-assistant` twice → offers to update, does not silently overwrite
- Ambiguous delegation: "draft a follow-up email" with no client named → persona asks ONE
  clarifying question before delegating, does not guess
- Out-of-scope request: something no specialist covers → handles it directly or says what's
  missing; does not invent a specialist
- Confidential research: "research what's happening with my client's leadership turnover" →
  researcher declines and says why, does not search around it
- Crowded calendar: ask scheduler for a fourth slot on a loaded day → pushes back on crowding
- Uncomfortable email: nudge a client who's ignored Quarterly Priorities for two quarters →
  draft is direct, not sanded down

### P2 — Workshop materials (separate from the plugin)

Put these in a `workshop/` directory in the same repo, excluded from the plugin.

**6. `workshop/pre-work-email.md`** — sends today or tomorrow. Three asks with reply-when-done:
confirm a paid Claude plan (Pro, Max, Team, or Enterprise — the Code tab is unavailable without
one), install the desktop app, install Git for Windows if on Windows. Plus one question: Mac or
Windows? Assume ~60% compliance.

**7. `workshop/triage-sheet.md`** — one page for Stephanie, printable. Symptom → fix:

| Symptom | Fix |
|---|---|
| Windows, Code tab won't start local sessions | Install Git for Windows, restart the app |
| No Code tab / unavailable | Free account — pair them with a neighbor |
| Skill wrote the assistant but Claude doesn't see it | Restart; a running session won't detect a newly created `agents` directory |
| Files seem to be in the wrong place | Coach opened a git repo — sessions get isolated worktree copies. Move to a plain folder |
| Folder access denied | Trust dialog not accepted |
| Connector shows but returns nothing | Re-auth from the `+` menu, start a new conversation |

Anything not on the sheet: flag to Mike, don't improvise. Stephanie also keeps the running
question log — that becomes the webinar curriculum.

**8. `workshop/run-of-show.md`** — the timed agenda, with the cut line marked at 11:25 and the
segments to drop if behind. Minimum viable outcome: assistant named, personality set, one
successful delegation, one scheduled task created.

**9. `workshop/commitment-card.md`** — printable. One sentence: "[Assistant name] will [recurring
task] every [cadence]." Read aloud around the room before lunch. Photograph them — that's the
follow-up list.

---

## PART 3 — Constraints that are easy to get wrong

Do not "fix" any of these; they are load-bearing.

**Plugin agents ignore some frontmatter.** Agents loaded from a plugin do not support `hooks`,
`mcpServers`, or `permissionMode` — those fields are silently ignored. This is why the *persona* is
written to `~/.claude/agents/` by the skill rather than shipped in the plugin, while the four
*specialists* ship in the plugin (they don't need those fields).

**An explicit `tools:` field is a whitelist and will block MCP tools.** MCP tool names vary per
connector and can't be enumerated in advance. `scheduler`, `email-drafter`, and `meeting-prep`
therefore omit `tools` entirely so they inherit the coach's authorized connectors. `researcher`
declares `tools` explicitly *on purpose* — it must not reach the coach's connectors.

**`AskUserQuestion` is stripped from subagents.** Specialists cannot ask questions. All
clarification happens in the persona before delegation. This is why every specialist file says
"state your gaps" and why the persona's delegation section is long.

**The `agent` setting goes in the project's `.claude/settings.json`**, not user-level. Project scope
is the documented placement, and coaches work out of one folder. Merge into an existing file; never
overwrite it.

**Local scheduled tasks vs. cloud routines are different things.** Both appear on the Desktop
Routines page. A *local* task runs on the coach's machine with access to their files but only fires
while the app is open and the computer is awake. A *remote* routine runs in the cloud even with the
machine off but works from a fresh clone with **no local file access**. `set-up-my-morning` must
create a local task.

**Remote Control is not cloud execution.** It syncs a session that is still running locally to the
phone or web. Closing the app ends the session. It's being demoed Tuesday, not built — do not add
setup steps for it to any skill.

**Third-party marketplaces default to auto-update OFF.** Document how coaches update, or plan to
have them re-run install after a release.

**`/reload-plugins` is required** after changing anything outside a `SKILL.md` — agents, hooks,
`.mcp.json`, marketplace manifest. `SKILL.md` edits are picked up live.

**Do not pin `model:` on the persona.** It inherits the session model, which keeps it working
across whatever plans the 15 coaches are on. Specialists pin `sonnet` deliberately.

---

## PART 4 — Build order

1. `marketplace.json` — then actually test `/plugin marketplace add` against the pushed repo,
   cold, the way a coach will experience it. A broken manifest is workshop-ending and a
   twenty-minute fix if caught now.
2. `assets/personalities.md` and the remaining placeholder content — the skill can't run without it
3. End-to-end test of `meet-your-assistant`, then fix what breaks
4. `evals/` file, then run the cases above
5. `add-a-specialist` and `set-up-my-morning`
6. `workshop/` materials
7. Slides last — they're narration around a thing that works, and they'll write faster once
   you've watched the skill run

---

## PART 5 — Definition of done for Tuesday

- A coach on a clean machine can install from the public repo and run the skill without touching
  a terminal, YAML, or JSON
- After restart, the assistant greets them by name, in the chosen personality, referencing
  something specific about their practice
- One plain-language request routes to a specialist and returns something real
- Median wall-clock for the interview under 12 minutes (if Stephanie takes 12, the room takes 25)
- Works on both Windows and macOS
- Re-running the skill is safe
- Nothing is written outside `~/.claude/` and the coach's chosen folder

## Deliberately out of scope

Remote Control setup (demo only), Dispatch (Cowork-only, plan-dependent), agent teams (CLI-only),
hooks, per-agent MCP scoping, and any Cowork packaging. All are growth areas for the follow-up
webinars, not Tuesday.
