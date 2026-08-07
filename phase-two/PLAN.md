# Phase two — `set-up-my-deck` (do not build before the workshop)

The coach-scale Command Deck: a daily self-assembling checklist at a stable bookmarked URL,
for coaches who have **outgrown the morning brief**. Adapted from Mike's production Command
Deck (running scheduled since July against six sources); the full architecture handoff lives
with Mike privately — this file is the coach-scale decision record.

**Positioning rule, non-negotiable:** the deck's value scales with how many systems a coach is
drowning in. A coach with a calendar and an inbox is *better served by the 200-word brief*.
Offer the deck when a coach says the brief feels thin, asks for links/checkboxes, or has
accumulated real volume — never as the default upgrade. A mostly-empty checklist is a worse
demo than a good paragraph.

## What it is, in one sentence

The morning brief is step 4 of a Command Deck without steps 1–3; the deck adds breadth of
sources and structure of output — same scheduled task, same stable page, same bookmark.

## What survives the shrink from Mike's deck

- One scheduled local task → stable artifact URL → bookmark (already proven in the kit)
- Checkbox state in `localStorage`, **keyed by date only** — never a build label. A wrong key
  orphans every checkmark the coach made that day.
- **Item ids derived from source identifiers**, never hand-authored — that's what lets the
  page be republished under the reader without losing their progress.
- Every item links to its own source in one click — the anti-skepticism feature. A link to
  something the item *mentions* is not a substitute for where it *came from*.
- Single column, scanned top to bottom. No grids, ever.
- Honest sourcing in the caveats: what was read live, what was carried forward.

## What's dropped (Mike-scale, not coach-scale)

FULL/REFRESH split and hourly rebuilds (one morning run), "new since" badges, Logseq, browser
automation, GitHub boards, build letters. If a coach someday needs hourly, that's a bespoke
conversation, not the kit.

## The coach deck: three sources, four sections

| Section | Content | Source |
|---|---|---|
| Today | Schedule with prep flags and **open gaps** | calendar connector |
| Act on first | The 1–3 things that actually matter today | synthesis |
| What you're owed | Follow-ups / client To-Dos gone quiet | email connector + notes |
| Overlaps | Same commitment visible in two places (inbox + session notes) | synthesis |

Id derivation for coach sources: calendar → event `eid`; Gmail → thread id; assistant-notes
items → note-file date + title slug. Pills: `cal` · `mail` · `notes` (rename in scaffold CSS
custom properties *and* markup).

## Build checklist (the week after the workshop)

1. New skill `skills/set-up-my-deck/` that **reuses `set-up-my-morning`'s machinery
   verbatim**: persona load with floor-not-ceiling, memory read, stored-URL file
   (`deck-url.txt`, separate from the brief's), mandatory supervised first run. The three
   connector gates documented there apply identically — do not re-litigate them.
2. Adapt `deck-scaffold.html` (in this folder — content-free, CSS/JS proven in production,
   both themes handled): rename pills, template the two `{{DECK_SLUG}}`/`{{YYYY-MM-DD}}` JS
   literals. **Do not rename** the ids the JS binds: `progress`, `btn-hide`, `btn-export`,
   `btn-import`, `import-file`, `save-state`, `allclear`.
3. Rewrite the two build scripts for coach sources (Mike has originals; they carry his
   workspace hostnames, so they're not committed here): `derive-ids.js` with cal/gmail/notes
   branches, `verify.js` with coach RULES. Keep the exit-nonzero-means-don't-publish contract
   and the title-slug-fallback report.
4. Decide brief-vs-deck at setup: the deck **replaces** the brief's task (one page, one
   morning voice), it doesn't run alongside it. Offer to keep the prose brief as the deck's
   masthead note instead.
5. Eval cases: republish preserves checkmarks (check three boxes, Run now again, boxes
   survive); every item's link lands on its source; day rollover resets naturally at
   midnight.

## Known traps, inherited from production so we don't rediscover them

- **A Slack/Gmail permalink anywhere in an item wins id derivation** — citing a source as
  evidence inside a different source's item silently re-keys it and orphans the checkbox.
  Citations go in callouts (they carry no ids) or prose.
- **Build at fixed paths, never session scratchpads** — tool approvals are stored per exact
  command string; a per-session path re-prompts forever and kills the unattended run.
- **Always pass the stored URL and a favicon on every publish** — "this session already
  published" reasoning has minted stray duplicates; missing favicon hard-fails.
- **Expect a publish conflict on every scheduled run** (fresh session each time) — confirm
  successorship from the build stamp before forcing, precisely *because* the expected
  conflict looks identical to a real one.

## Tuesday's only involvement

A ~60-second showing of Mike's live deck during open floor (run-of-show, 1:45 slot), framed
as: *"Your brief is this, minus the parts you don't need yet. When you're drowning in enough
systems, this is where it goes — that's webinar two."* No coach builds one on Tuesday.
