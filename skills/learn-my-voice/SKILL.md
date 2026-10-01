---
name: learn-my-voice
description: Teaches the coach's assistant to write the way the coach actually writes, from a sample of their own sent email and Slack messages. Use when a coach says "make it sound like me", "my drafts don't sound like me", "learn my voice", "learn how I write", "I keep rewriting what you draft", or wants Slack messages drafted in their voice. Also use to refresh the voice note when their writing has changed, or to delete it.
---

# Learn My Voice

A coach's writing voice is part of their professional identity. A draft that sounds like generic
business correspondence gets rewritten from scratch, and then the assistant has cost them time
instead of saving it. The drafters already read the coach's notes for tone, but until those notes
say something specific, "in your voice" is a guess. This skill replaces the guess with evidence: it
reads what the coach really sent, writes down how they write, and checks the result on messages it
held back.

It produces one note, `memory/writing-voice.md`, that the drafters read before they write. If the
coach uses Slack, it can also hire a `slack-drafter`.

Same rules as the other skills: the coach is **not technical**. No YAML, no file paths, no
connector names in conversation. "Your voice notes" is the whole vocabulary.

**This skill is different from the others in one way: it reads private correspondence.** Three
rules shape every phase below. Ask first and say exactly what is kept. Keep patterns and scrubbed
fragments, never messages. Let the coach check the result before it is trusted.

---

## Phase 1 — Preflight (silent)

Nothing in this phase reads a message. No message is opened until Phase 3, after the coach says yes.

1. **Find the persona** exactly as `add-a-specialist` does, including its `agent`-key check. No
   persona → offer `meet-your-assistant` first; the note belongs in someone's memory.

2. **Find the memory folder** — `memory/` in the coach's folder. (Assistants set up before
   2026-09 may still have it at `~/.claude/agent-memory/{{SLUG}}/`; check both.) Read the hub.
   **If `writing-voice.md` already exists, this is a refresh** — go to *Refreshing, and deleting*
   at the end. Never start over on top of an existing note.

3. **Find out which surfaces you can reach.** Search your available tools by capability, never by
   server ID: *search or list sent email*, *search messages sent by me in Slack*. Email may be
   Gmail or Microsoft 365. Only note that the tools exist. If one connector reports as
   unauthorized, check whether another is wired in before concluding a surface is out. If nothing
   is reachable, use the paste path in Phase 2.

4. **More than one mailbox?** Ask which one is the voice they want learned; skip this if there's
   only one. A work voice and a side-business voice are different voices, and blending them
   produces a third that is neither. One mailbox per note. A second voice is a second run, with its
   own note (`writing-voice-<label>.md`).

---

## Phase 2 — Ask first

Say this in your own words, and **wait for a yes**:

> I'd like to learn how you write, so my drafts need less fixing. To do that I'll read up to thirty
> emails and thirty Slack messages you've actually sent — just your side, and that includes Slack
> DMs. Slack search shows me the text of what it finds, so I may glance at a few more than I keep.
> I'm looking for patterns: how you open, how long you go, what you'd never say. I keep the
> patterns and a few short lines with the names and numbers taken out. I don't keep the messages.
> It takes about ten minutes.

Use `AskUserQuestion`, offering only the surfaces Phase 1 found: **Email and Slack** / **Email
only** / **Slack only** / **I'd rather paste examples**. Then one free-text follow-up: *"Anything
I should stay away from — a person, a client, a thread?"* Honor the answer. And one more, as a
tap: *"Has your assistant, or another AI, drafted any of what you've sent?"* — **No, all mine** /
**Some of it** / **Not sure**. Mail an assistant drafted isn't their voice; it's the assistant's
own habits fed back to it.

**The paste path.** Ask for five to eight messages they're happy with, mixed across the people they
write to, plus their answers to two prompts: *how would you tell a client they've missed their
To-Do for the third time*, and *how would you say no to a request*. Say plainly that a pasted
sample will leave thin spots, and that's fine. Nothing is held back on this path; Phase 6's test
uses the two prompt answers instead.

---

## Phase 3 — Read and sort

**Which messages.** Recent (the last six months; voices drift) and written from scratch by the
coach. Choose from the headers alone: skip anything whose headers say forward, invite, or
automated. Where the same subject went to several people on the same day, open one to confirm it's
a template, then drop them all. Keep at most three per recipient or channel on each surface, posts
and replies together, applied after those skips and keeping the most recent. Try to cover the kinds
of message they really send. For email: a follow-up, a nudge, a scheduling note, a quick reply, a
longer explanation, a no or a difficult one, something to a colleague. For Slack: a short DM reply,
a message to someone senior, a channel post, a thread reply. Aim for up to thirty per surface. Don't
widen the window to make up numbers.

**Skip** forwards, replies that are mostly quoted text, automated mail and invites, mass mailings,
and text they paste the same every time (that's a template, not their voice). Headers settle most
of these; the rest you'll see on reading, and a message dropped then is replaced by the next most
recent from the same register. **Drop, and use nothing from, any message about how a named person is
doing:** their performance, health, a legal matter, or money in dispute. A message about a
company's work, such as a stalled Quarterly Priority, is fine.

**Also skip anything an assistant drafted.** If the coach said some of it was, ask which. If they
aren't sure, leave out messages that read unlike the rest (bullets, em dashes and tidy structure in
someone who otherwise writes loosely), name them in Phase 5 and ask which were theirs. If they can't
say, they stay out.

**Bare acknowledgements** are messages that are only "ok", "thanks", "got it", "on it", "yes, that
works". Tally them, don't sample them, and count them toward no total. Report the pattern once, in
the register where most of them fall.

**A surface with fewer than twelve usable messages is thin**, counting what survives the skips and
drops. Say so in Phase 5, describe less, and for Slack don't offer the drafter. A thin surface may
add to a register it matches on another surface.

**Sort, then set aside, then read.**

1. **Sort the selected messages into registers from who and where alone** — recipient, channel,
   DM or thread. No reading yet. A register is *who it goes to, and where*: typically email to
   clients, email to colleagues, Slack DMs, Slack channels. How well the coach knows the person is
   a third cut that a header can't show, so it waits for Phase 4 and Phase 5. You settle merges and
   splits after reading, in Phase 4.
2. **Set aside the held-back messages for Phase 6:** about one in five of a surface's selected
   messages, at least two and at most three, taken only from a register that would still have at
   least eight afterwards, so that drops on reading can't push it under five. Prefer messages
   whose headers look ordinary. A thin surface gets none, because it gets no drafter. If no
   register can spare any, set none aside. Held-back messages never feed the note, including as
   evidence that something is absent; the test in Phase 6 will catch an absence one of them
   contradicts. On Slack, search shows you the text, so you will have seen the ones you set
   aside: choose them by kind and place, and never count them in Phase 4. Set aside one more than
   you'll test with, as a spare.
3. **Read the rest, and fetch the first one end to end before anything else.** If message bodies
   don't come back, say so plainly and offer the paste path; don't push on with headers alone.
   Read in batches. **Keep a working sheet in the conversation, not on disk**: for each message one
   row, with its register, rough length, how it opens, how it closes, how the ask is made, and
   anything distinctive. Once a row is written, drop the body. **No message text is written to any
   file in this phase.**

---

## Phase 4 — Draft the findings (in conversation only)

**Settle the registers first.** Now that you've read them, merge two registers when their shape,
openers and closers match in most messages, even across email and Slack. Keep them apart when
they don't. Six is plenty. Then, for each register, say only what the sample supports:

- **A trait goes in only if three or more messages show it.** Write the count: "(8 of 11)". Count
  from the rows, not from memory. If a trait doesn't clear three, leave it out.
- **Behavior, not adjectives.** "Warm" and "professional" are not findings. "Opens with the first
  name and a line about the last conversation (7 of 9)" is.
- **Lead with the tone.** Open with the overall level in one line: how formal, how polished, how
  loose. A drafter reads the first line hardest, and a mechanical trait read alone ("spells verbs
  out") sounds like formality. The first real test of this skill came back "too formal" because the
  note led with exactly that.
- **Familiarity.** Look for how the tone shifts with how well the coach knows the person, and with
  giving instructions versus chatting. If it shifts (looser and quicker to people who know them,
  more careful and courteous to people who don't), say so in the opening line and in the register. A
  sample can show it only if it holds both kinds of recipient, so Phase 5 asks about it directly.
- **Cover:** typical length and the ceiling; greeting and sign-off; where the ask sits; how a no, a
  late item, or a hard thing is said; paragraphing, lists, bold; punctuation habits (exclamation
  marks, dashes, ellipses, caps); contractions; emoji; hedging; humor; phrases they reuse
  (verbatim, three or more times); how they acknowledge, if the tally reached three.
- **An absence is a finding only if it's a verified zero** across the messages that fed that
  register, and only where seven or more did: *never "hope you're well" (0 of 31).*
- **Under five fed messages in a register: no rules.** It goes under *Thin spots*, with the
  nearest register by audience as its fallback, or the drafting defaults if none is near.
- **Quote only the coach.** Never record how a recipient writes.
- **Short enough to read in full before every draft** — about two pages for the whole note. Cut to
  the traits that would change a draft.

---

## Phase 5 — Let them correct it

Don't show the note. Tell them what you found in six to eight plain lines: how long they go, how
they open and close, how they ask, how they handle a hard one, what they never say, and whether
Slack differs from email (it may not). Name what stayed thin, name any messages you left out as
probably assistant-drafted and ask which were theirs, and if you're not offering a Slack drafter,
say why in one line. Then `AskUserQuestion`:

1. **Does this sound like you?** — *That's me* / *Mostly, a few fixes* / *Not really*. On *Mostly*,
   ask what to change, once, in free text.
2. **Is there anything here you'd rather your assistant did differently from how you write now?**
   Free text. ("I overuse exclamation marks." "I'm too curt with new clients.") If the answer is
   vague ("fewer dashes"), ask once what they'd do instead; otherwise write it in their words.
3. **Do you write differently to people you know well and people you don't, or when you're giving
   instructions?** — *Yes, quite differently* / *A little* / *No*. On *Yes* or *A little*, ask once,
   in free text, what changes. In the first pilot this took two rounds of corrections to surface,
   because the sample held mostly one kind of recipient. The answer is how they write, so it goes
   in the observed register and the opening line, in their own words where the sample couldn't
   show it.

Their corrections beat the sample; they know what they meant. **Sort what they say into two
piles.** "That's not how I write" fixes the observed register. "I'd rather not write that way"
goes in its own section of the note, even when the sample does show the habit, which is the common
case: leave the observed description alone and add the wish beside it. *How they write* and *how
they want to write* are different things, and a drafter that can't tell them apart copies the
habits the coach wants to lose. On *Not really*, suspect the sample (a lot of dictated mail, a
ghostwritten stretch, a changed role) and ask what would represent them better, or use the paste
path.

---

## Phase 6 — Write it, wire it, test it

Write files only now, once the coach has confirmed — never leave a half-written note behind.

**1. The note.** `memory/writing-voice.md`, from `assets/voice-note-template.md`. Fill every
placeholder; a file that still contains `{{` is a bug the coach will see.

| Placeholder | Source |
|---|---|
| `{{COACH_NAME}}` | the name the hub says they go by |
| `{{DATE_ISO}}` | today, `YYYY-MM-DD` |
| `{{STALE_AFTER}}` | six months out, `YYYY-MM-DDT00:00:00Z` |
| `{{DATE}}` | today, plainly formatted |
| `{{SAMPLE_WINDOW}}` | the months the messages came from, like "April to September 2026" |
| `{{EMAIL_COUNT}}`, `{{SLACK_COUNT}}` | the messages that fed the note, acknowledgements not counted; `0` is a real value |
| `{{HOLDOUT_COUNT}}` | the messages set aside for the test |

`{{NAME}}` and `{{SLUG}}` in this file mean the assistant's name and slug, from the persona.

**Choose the exemplars now, after Phase 5.** Up to four short fragments per register: an opener,
an ask, a closer, or a whole message if it's three lines or fewer. Quote the coach exactly, then
scrub. Names become `[name]`, companies `[client]`, places `[place]`, figures `[amount]`, dates
and times `[date]`, `[day]`, `[time]`, any other number that isn't part of how they write `[number]`.
Drop a fragment if scrubbing leaves nothing that sounds like them, if it came from a held-back
message, or if it models a habit the coach said they want to lose. Pick a fragment that starts after
the habit rather than a whole one that shows it.

Then add the pointer to the hub's *Preferences I've learned* as `- [[writing-voice]] — ` followed
by the note's own `description`, and bump the hub's `updated`. **Merge, don't clobber.** The pointer
is how a drafter finds the note.

**2. The email drafter.** Nothing to write. In this plugin version `email-drafter` reads the note
and names the register it used in its Notes. A coach on an older plugin has a drafter that predates
this, and nothing errors; step 4 is how you find out.

**3. The Slack drafter** (only if Slack is not thin and a Slack connector is live). Ask once:
*"Want a teammate who drafts your Slack messages the same way? You send them yourself."* On a yes,
copy `assets/slack-drafter.md` unchanged to `~/.claude/agents/slack-drafter.md`, then do
**exactly** Phase 4 of `add-a-specialist`: add the bare name `slack-drafter` inside the persona's
`Agent(...)` list without touching what's there, add the routing entry below, and add the cheat
sheet line. An agent file that isn't wired is invisible.

> - **slack-drafter** — anything written in Slack: DMs, channel posts, thread replies, quick
>   nudges. Send it where the message is going (person or channel, DM or thread), the purpose, and
>   the tone if it matters. Comes back with the message ready to paste and a short note on anything
>   it guessed at. It drafts and never sends.

Cheat sheet: *"**Slack** — drafts your Slack messages in your voice: short, the way you'd actually
say it. You send them yourself."*

**4. Test it on the messages held back. Mandatory.** A voice note nobody has tested is a guess in a
nice font. Test each surface that has a drafter; a surface without one is untested, so say so. If
nothing was held back, ask the coach the two prompts from the paste path now and test on their
answers in place of held-back messages.

- Take one held-back message. If it turns out to be unusable now you've opened it (a forward,
  mostly quoted, about a person), swap in another, or test with one fewer. Write a one-line brief of
  what it was *for*: the recipient's role, the purpose, and the facts it had to carry, stated as
  facts and using **none of its wording**. State facts, not stance or audience: say what happened and who is
  being spoken to ("you", not "whoever"), never a verdict like "accepting". In the first real test
  two of four drafts failed on exactly that, from the brief and not from the voice. A reply or a DM that only makes sense in context needs
  the message it answered; fetch it, or pick a different held-back message.
- Hand the brief to the drafter (`bloom-coach-kit:email-drafter` or `slack-drafter`) as the persona
  would. If the drafter's Notes don't name a register from the voice note, its plugin predates this
  skill: tell the coach the kit needs updating, and for this test only, tell the drafter to read
  the voice note first.
- Show the coach two things side by side: **what you wrote** and **what I drafted**. Ask: *"Would
  you send mine — as is, with small edits, or rewrite it?"* and *"What's off?"*
- Sort each difference. A trait the note lacks: add it **only if the fed messages show it three
  times**, otherwise file it under *Corrections*, dated. A trait the note has wrong: fix or remove
  it. The drafter ignoring a trait the note has: that's the drafter's problem, not the voice's;
  say so.
- Run once more with a second message. **Two rounds, then stop.** The note keeps improving through
  use; this is only the first check.
- If you changed the note after a round, a re-run on the same briefs proves little, because the
  note now contains those answers. Check a fix on the spare. Ask about **formality and polish**
  as well as wording: a draft can carry every fact and still not sound like them.

Then drop the held-back messages from the working sheet.

---

## Phase 7 — Handoff

Tell them plainly:

> {{NAME}}'s drafts will now start from how you actually write. They'll still need your eye — I'd
> expect most to need small edits, not a rewrite. When you change one, tell {{NAME}} what was off —
> "too stiff", "I'd never say that" — and it gets filed, so the next one lands closer.
>
> What's kept is a page or two of patterns and a few short lines with the names taken out. Not
> your messages. You can ask {{NAME}} to show you how you write at any time, to re-learn it in a few
> months, or to forget it entirely.

Then stop.

---

## Refreshing, and deleting

**Refresh** — an existing note, and they ask to re-learn, or the note is past its `stale_after`, or
their role has changed. Run Phases 2–5 over only the messages newer than the note's `updated`
date, with fresh held-back messages. Show the **differences** in plain language: what's new, what no
longer holds. Apply them on a yes. **Keep the Corrections section whole.** Never overwrite the
note silently.

**Delete** — "forget how I write", "delete my voice notes". Delete `writing-voice.md` and its pointer
in the hub, and say so. This is the one place the kit deletes a note without ceremony: it's the
coach's own data and their call. The drafters fall back to their defaults and keep working. The
`slack-drafter`, if there is one, stays on the team unless they ask to retire it (see
`add-a-specialist`).

---

## Guardrails

- **Ask first, every time.** No message is opened until the yes in Phase 2, and then only on the
  surfaces they said yes to.
- **Their own accounts, in their own session, with them present.** This reads private
  correspondence. If someone other than the coach is driving the session, stop.
- **Patterns and scrubbed fragments, never messages.** No message body is written to any file. No
  name, company, figure, or confidential detail survives into the note. A third party's words never
  go in it.
- **No finding without three instances.** An adjective is not a finding. An absence is a finding
  only at a verified zero.
- **Observed voice and wanted voice stay separate.** Never write a correction into the observed
  register as though the sample showed it.
- **The note outranks the drafting defaults. It outranks no boundary.** Draft only, never send.
  No invented client-specific detail. No one client's information in another's message. Writing
  like them is not permission to speak for them.
- **Held-back messages never feed the note.** They exist to test it.
- **Don't promise it sounds exactly like them.** The honest framing is *closer, and closer still as
  you correct it*. Overselling this earns one disappointed coach per oversell.
- **Never touch the persona's existing roster entries.** The only persona edit this skill makes is
  adding a chair for `slack-drafter`.
