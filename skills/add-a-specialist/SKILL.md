---
name: add-a-specialist
description: Grows the coach's assistant roster with a new specialist, conversationally. Use when a coach wants their assistant to handle something no current specialist covers — "add a specialist", "can April do proposals", "I keep doing X by hand, can we automate it", "my assistant says that's not something her team does" — or when the assistant itself told them a capability is missing. Writes the new agent file, wires it into the persona's roster, and updates the coach's cheat sheet.
---

# Add a Specialist

A coach's roster grows after the workshop, in month two, when they hit something real that the
original four don't cover. This skill is that growth path — same rules as `meet-your-assistant`:
the coach is **not technical**, sees no YAML, JSON, or file paths, and everything happens
conversationally.

---

## Phase 1 — Preflight (silent)

Do this before saying anything. Do not narrate it.

1. **Find the persona.** Look in `~/.claude/agents/` for `.md` files containing the marker
   `<!-- bloom-coach-kit -->`. If several exist (a coach who started fresh once), the live one is
   whichever the current folder points at — check the `agent` key in the folder's
   `.claude/settings.json` and the persona path in its `CLAUDE.md` block. If **none** exist, stop
   and offer `meet-your-assistant` instead: *"Let's set up your assistant first — the specialist
   needs someone to work for."*

2. **Read the persona's current roster** — the `Agent(...)` list and the "Your roster" section.
   You'll need both, and you must not damage either.

3. **Note which connectors are live** in this session. If the new specialist's job needs the
   coach's calendar, email, or CRM and that connector isn't authorized, say so in plain language
   before building it, exactly as `meet-your-assistant` does.

---

## Phase 2 — The conversation

Keep it to three beats. This should take two minutes, not ten.

**1. The job.** *"What should they handle?"* Free text. Ask at most one follow-up, and make it
about the *output*: what should come back when the work is done — a draft, a list, a plan, a
document? A specialist with a fuzzy deliverable produces fuzz.

If the job substantially overlaps an existing specialist, say so and offer the better path:
*"That's close to what your email drafter already does — want me to teach them this instead of
hiring someone new?"* Extending an existing specialist means editing that agent file's body, and
skipping Phases 3–4 entirely.

**2. The name.** Propose one — a plain working title like "proposal writer" or "invoice chaser",
not something cute. Let them rename it. Derive the slug the same way as `meet-your-assistant`:
lowercase, hyphens, letters and numbers only.

**3. Confirm the shape back** in one sentence — *"So: they take a client name and a scope
conversation, and hand back a draft proposal in your voice"* — and get a yes before writing
anything.

**Decide the tool posture yourself. Never ask the coach about tools.** From the job:

- Needs the coach's calendar, email, CRM, or files → **omit the `tools:` field entirely** so it
  inherits the coach's authorized connectors. An explicit list is a whitelist and would block MCP
  tools whose names can't be known in advance.
- Must not touch the coach's accounts (pure research, pure writing from handed material) →
  declare `tools:` explicitly, the way the plugin's `researcher` does: `WebSearch, WebFetch,
  Read, Write, Glob, Grep` or a subset.

---

## Phase 3 — Write the specialist

One file: `~/.claude/agents/{{SLUG}}.md`, from `assets/specialist-template.md`. Fill every
placeholder. Non-negotiables, all inherited from how the plugin's own specialists are built:

- **`model: sonnet`**, pinned.
- **The cannot-ask-questions block stays.** Specialists never get `AskUserQuestion`; they must
  state gaps at the top of their reply instead of guessing silently, and never invent a
  client-specific detail.
- **A concrete output format**, shaped by the coach's answer about the deliverable.
- **Boundaries**: client confidentiality always; *draft, never send* if it produces anything
  client-facing; never carry one client's information into another's work.

---

## Phase 4 — Wire it in (the step that's easy to miss)

A specialist that exists but isn't wired is invisible — the persona won't route to it, won't
mention it, and the coach concludes the whole thing didn't work. **Writing the agent file is not
enough.** Three edits, all merge-don't-clobber:

1. **The persona's `tools:` line.** Add `{{SLUG}}` — the **bare name** — to the inside of the
   `Agent(...)` list. New specialists live in `~/.claude/agents/`, so they are *not* namespaced.
   The plugin's original specialists keep their `bloom-coach-kit:` prefix — do not "tidy" them to
   match, and do not remove or reorder anything already in the list. A grown roster is
   legitimately mixed:

   `Agent(bloom-coach-kit:scheduler, bloom-coach-kit:meeting-prep, proposal-writer)`

2. **The persona's "Your roster" section.** Add one routing entry in the same shape as the
   existing ones: when to route there, what to send, what comes back.

3. **The cheat sheet.** If `MY-ASSISTANT.md` exists in the coach's folder, add a plain-English
   line to its specialist list. No jargon, no agent names.

Write Phase 3 and Phase 4 together, at the end, once the coach has confirmed — never leave the
agent file written but unwired.

---

## Phase 5 — Handoff

The new specialist isn't visible until the coach starts a new session. Stage it, briefly:

> Done — {{NAME}} has a {{SPECIALIST}} on the team now. Start a new session and try them out:
> *"{{EXAMPLE_REQUEST}}"*

Make `{{EXAMPLE_REQUEST}}` a real request from the coach's own use case, not a generic one. Then
stop.

---

## Guardrails

- **Never remove, rename, or rewrite an existing roster entry.** You are adding a chair to the
  room, not rearranging it.
- **Never show YAML, JSON, or a typeable file path.**
- **Retiring a specialist** (if asked): remove its entry from the `Agent(...)` list, its roster
  bullet, and its cheat-sheet line, and tell the coach it's off the team. Leave the agent file on
  disk unless they explicitly want it gone.
- **Don't build a duplicate.** Overlap goes to the existing specialist (Phase 2).
- **Nothing is written outside `~/.claude/` and the coach's folder.**
