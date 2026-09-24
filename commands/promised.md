---
description: Show what you've promised — who you owe, what you said, and where you said it
argument-hint: [person name]
allowed-tools: Read, Glob, Grep
---

Show the person you work for what they've committed to and haven't closed yet.

`/projects` answers *what am I working on*. This answers a harder question: **what did I say I
would do, to whom, and when.** Those promises are the things that quietly cost people trust,
because they're made out loud in a meeting and then live nowhere.

If `$ARGUMENTS` names a person, show only what's owed to them and skip the rest — that's the view
they want walking into a one-on-one.

## Where to look

Your memory directory. **A promise is any note whose `type:` is `promise`.** Read frontmatter
only; you'll open the full note when they pick one.

| Field | Holds |
|---|---|
| `title:` | what was promised, in their words where possible |
| `to:` | who it was promised to |
| `made:` | the date they said it |
| `due:` | a real date, or `unstated` |
| `status:` | `open`, `done`, `dropped` |
| `source:` | the meeting it came from |

## The table

| Owed to | What | Said | Due | Age |

- **Owed to** — `to:`. Strip the wikilink brackets; show the name.
- **What** — `title:`.
- **Said** — `made:`, as a date.
- **Due** — `due:`, or **"none given"** when it's `unstated`. Never infer one.
- **Age** — days since `made:`, in plain words.

Show only `status: open` unless they ask for everything.

### Order

1. **Overdue first** — a real `due:` that has passed. These are the ones costing them something
   right now.
2. **Then oldest-said first.** A promise with no deadline doesn't expire, it just rots, and age is
   the only signal it has.

### What to flag underneath

- **Anything past its `due:`** — say so plainly, and say how long. "Two days late" is actionable;
  a red row is decoration.
- **More than one promise to the same person** — group them and say it. Walking into a one-on-one
  owing somebody four things is a different conversation than owing them one.
- **Anything older than three weeks with no `due:`** — surface it and ask whether it's still real.
  A promise nobody has mentioned in a month is often already dead, and saying so is kinder than
  letting it sit on a list forever.

## After the table

One line: they can name a promise to open it, or name a person to see just that person's. Don't
re-summarize the rows in prose.

## Closing one out

When they say something is done, set `status: done` and leave the note in place. **Don't delete
it.** The record of having closed something matters as much as the open list, and a promise that
vanishes can't be pointed at later.

If they say a promise is no longer real, `status: dropped` — and if it was made to another person,
say out loud that the other person may not know that yet. Quietly dropping something someone else
is still waiting on is the exact failure this command exists to prevent.

## When there's nothing to show

Say so plainly, in one line. Don't render an empty table, and don't treat it as suspicious — an
empty list is a good outcome, not a sign the sweep is broken.

## Do not

- **Don't invent a due date.** "None given" is the truth and it is useful. A guessed deadline makes
  them late for something nobody asked for.
- **Don't show promises made *to* them** in this view. This list is what they owe. Things other
  people owe them belong in those people's notes.
- **Don't quote a promise without its source.** Every note carries where it was said; if they
  doubt one, the link is the answer.
- **Don't hand this to a specialist.** It's their own word and their own history — your domain.
