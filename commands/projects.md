---
description: Show what's in flight — the projects your assistant is tracking, and their state
argument-hint: [project name]
allowed-tools: Read, Glob, Grep
---

Show the person you work for what they've got in flight, then offer to go into one.

If `$ARGUMENTS` names a project, skip the table entirely: open that project's note, read it in
full, and pick up where it left off. Only fall back to the table if you can't tell which one they
meant.

## Where to look

Your memory directory — the one holding `about-my-coach.md`, the hub you read at the start of a
session. Every note you keep starts with frontmatter, and **a project is any note whose `type:` is
`project`.**

Read frontmatter only. Don't open whole notes to build this view; you'll read the full note when
they pick one.

## The table

One row per project:

| Project | Status | What's next | Waiting on | Last touched |

- **Project** — the `title:`, not the filename.
- **Status** — `state:`. Notes written before 0.6.0 say `status:` instead; read it the same way.
  If neither is there, show `—`.
- **What's next** — `next:`. If it's absent, show `—`.
- **Waiting on** — `waiting_on:`, but only when it's genuinely someone else. If it says nobody, or
  it's absent, leave the cell blank. A column full of "nobody" is noise.
- **Last touched** — how long since `updated:`, in plain words: "today", "3 days", "5 weeks".

### Order

1. **Anything blocked on another person, first.** That's the list they can move by chasing
   somebody, and it's the most useful thing on the screen.
2. **Then everything else, oldest first.** Work that's going quiet floats up on its own.

### What to flag underneath

- **Past its `stale_after:`** — mark the row and say so. That note's facts can't be trusted without
  re-checking, and repeating a stale fact confidently is worse than saying you need to look again.
- **`state: active` but untouched for weeks** — say it plainly. An active project nobody has
  touched in a month is usually not active any more, and it's better to ask than to keep showing a
  comfortable lie.
- **Missing `state:` or `next:`** — show the dashes and offer to fill them in from what you
  already know. Never quietly invent either.

## After the table

One line: they can name a project and you'll open it and carry on from there. Don't summarize all
of them underneath — the table is the summary, and repeating it in prose wastes their time.

## When there's little or nothing to show

- **No project notes at all.** Say so plainly. Explain in one sentence what makes something a
  project — work that spans more than one conversation — and offer to start one from whatever
  they're in the middle of. Don't render an empty table.
- **One project.** Still use the table. Consistency reads better than a special case.

## Do not

- **Don't invent a status, a next step, or a blocker.** A dash is honest; a plausible guess is
  worse than a gap, because they'll believe it.
- **Don't read every note in full** to build the list. Frontmatter first.
- **Don't hand this to a specialist.** This is the person's own state and history — your domain,
  not something to delegate.
- **Don't edit any note** as a side effect of showing the list, unless they ask you to.
