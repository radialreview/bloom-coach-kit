---
name: nightly-promise-sweep
description: Sets up a nightly routine where the assistant reads the day's meeting transcripts, files what the coach promised and what it learned about the people they met, and leaves a short list waiting for the morning. Use when someone says "go through my transcripts", "track what I promised", "set up the nightly sweep", "read my Zoom notes each night", or wants their meetings to stop evaporating.
---

# Nightly Promise Sweep

Every evening, the assistant reads the transcripts of the day's meetings, files two kinds of thing
it finds, and leaves a short list for the morning.

The two things are:

1. **Promises the coach made** — "I'll get you that", "let me check", "I'll set that up". Said out
   loud, believed by someone else, and written down nowhere.
2. **What it learned about the people they met** — so the next one-on-one starts from somewhere
   instead of from scratch.

This pairs with `set-up-my-morning`. That one tells them the shape of the day ahead; this one
makes sure the day just gone didn't evaporate. Run together, the morning brief can open with
*"here's what you owe people"* instead of *"here's your calendar."*

Same rule as every other skill in this kit: **the coach is not technical.** No cron, no YAML, no
file paths in conversation.

---

## Phase 1 — Preflight (silent)

1. **Find the persona and the memory directory** exactly as `set-up-my-morning` does, including
   the `agent`-key check in the folder's `.claude/settings.json`. Everything that skill documents
   about headless runs and connectors applies here unchanged — read it rather than re-deriving it.

2. **Find where the transcripts actually are.** Do not assume, and do not conclude they're missing
   on the first failed call. Meeting platforms file the same recording in several places and only
   one of them usually has the text:
   - The **host-side record** (recordings, meeting assets) is often empty for meetings the coach
     attended but did not host.
   - The **attendee-side notes collection** — Zoom's My Notes and its equivalents — is usually
     where a participant's own transcript lives, including for meetings hosted elsewhere.
   - Transcript text is frequently **behind an explicit flag** on the fetch call. A note that comes
     back with empty content may simply need asking for the transcript by name.

   Try the attendee-side collection before reporting that nothing is there. **If one connector for
   a platform reports as unauthorized, check whether another one is wired up before telling the
   coach the platform is unavailable** — more than one can be installed at once.

3. **Confirm a day's worth actually reads** before promising a nightly anything. One transcript,
   start to finish. If that fails, fix it now; a routine that silently finds nothing every night is
   worse than no routine, because they'll stop checking.

---

## Phase 2 — Two questions

Use `AskUserQuestion`. Two questions, not an interview.

**1. What time?** The sweep wants to run after the last meeting and before they stop for the day.
Offer 6:00pm / 7:00pm / 8:00pm / 9:00pm. Weekdays by default.

**2. What should it watch for?** Multi-select:

- **What I promised** — the core of it; on by default
- **What I learned about people** — dossier notes on whoever they met
- **What others promised me** — filed on that person's note, not in the promise ledger
- **Decisions made** — things settled in a room that nobody wrote down
- **Anything they name**

---

## Phase 3 — What the sweep actually does

Write this into the task prompt. The order matters: read, file, then summarize. A run that
summarizes without filing produces a nice message and no memory.

### Read

List the day's transcripts. Read each one **in full**. Skip nothing for being a standup — the
throwaway line at the end of a fifteen-minute call is exactly where "I'll sort that out" lives.

### File what it finds

**A promise is something the coach said they would do.** Not something they thought about, not
something someone asked for and they didn't answer. The test is whether another person in that
room would now be waiting.

Each promise becomes its own note with this frontmatter:

```
type: promise
title: <what, in their words where possible>
to: <who it was promised to>
made: <the date it was said>
due: <a real date, or: unstated>
status: open
source: <meeting name and date>
```

Then the body: what was actually said, enough context to act without re-reading the transcript,
and **a link back to the transcript**. Every promise carries its source. If they doubt one, the
link settles it.

Three rules that keep this honest:

- **Never invent a due date.** `unstated` is the truth and it is useful. A guessed deadline makes
  them late for something nobody asked for.
- **Quote where you can.** "I'll get you added today" is worth ten words of paraphrase, because
  it's how they'll remember saying it.
- **Don't double-file.** Check the existing promise notes first. The same commitment restated in
  three meetings is one promise with a history, not three promises.

**Dossier material** goes in the person's note under a dated one-on-one log, newest first — what
they're working on, what's worrying them, what they asked for, what to follow up on next time.

### The judgement call that matters

Meetings contain things about people that should not be written down: speculation nobody can
evidence, someone's bad week, a half-formed worry about a colleague's performance.

**File the commitment, not the characterization.** If a manager raises a concern about someone and
the coach commits to act, record *that a concern was raised, by whom, and what was promised* —
and leave the adjectives in the transcript where they belong. Link the transcript so the detail is
one click away without living in a file.

Where a note is unavoidably sensitive, say so at the top of it and keep it factual.

### Leave a morning list

Short. Ordered by what actually needs doing:

1. **Overdue promises** — with who's waiting and how long.
2. **Promised yesterday** — still warm, cheap to close.
3. **Anything with a date attached this week.**
4. **One line per person they meet today** — what's open with that person, so they walk in loaded.

No table unless there's enough to need one. Four lines they read beats twelve they skim.

---

## Phase 4 — Run it once, supervised

**Mandatory.** Same reason as `set-up-my-morning`: connector approvals are stored on the task and
auto-applied to later runs, so a task that has never had a supervised run has no grants and will
come back empty forever.

Run it in front of them. Then check the two things that are actually load-bearing:

- **Did it file anything?** Open one promise note. If the ledger is empty after a day with
  meetings in it, the sweep read nothing — go back to Phase 1 step 2.
- **Is what it filed true?** Read one promise back to them and ask whether that's what they meant.
  A ledger full of near-misses is worse than an empty one, because they'll stop trusting the
  accurate entries too.

Then tell them the one thing they need to know: **`/promised` shows the list any time**, and
naming a person shows just what's owed to them. That's the habit worth forming — running it before
a one-on-one rather than reading the morning list and forgetting by ten.

---

## Do not

- **Don't let it close promises on its own.** It files and it reminds. Only the coach says
  something is done — they're the only one who knows.
- **Don't have it message anyone.** Everything it produces lands in their notes and their morning
  list. A routine that chases people on their behalf is a different thing they did not ask for.
- **Don't promise the coach it caught everything.** Transcripts drop words, people mumble, and some
  meetings never record. The sweep is a net, not a guarantee, and it should say so the first time
  it runs.
