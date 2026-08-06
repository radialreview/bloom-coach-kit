# Eval cases — run manually before Tuesday

Not a harness. A checklist for the dry run: each case is a thing to actually do, what correct
looks like, and the failure smells that mean stop-and-fix. Run them in order — the early ones
create the state the later ones use.

Log results inline: **PASS / FAIL / notes** under each case. Anything marked ⚠ is
workshop-blocking if it fails; the rest are quality problems that can ship Tuesday and be fixed
in the follow-up webinar cycle.

Baseline already verified on 2026-08-05, on the real desktop app: marketplace add via Settings →
Plugins, plugin install, all four specialists loading namespaced, the interview producing a
working persona (June, April), the re-run offering update-vs-fresh, and the CLAUDE.md activation
producing a personalized first-reply greeting on both desktop and CLI.

---

## A. Setup flows

### A1. ⚠ Cold install on a machine that has never seen the plugin
Settings → Plugins → Add → Add marketplace → `radialreview/bloom-coach-kit`, then install.
**Correct:** plugin appears with the meet-your-assistant skill listed; four specialists visible
under Agents; no errors tab entries.
**Smells:** version shows something other than the frozen release; skill list empty (stale
marketplace clone — remove and re-add the marketplace).

### A2. ⚠ Terse coach
Run `meet-your-assistant` answering every question in one word or a tap. Practice description:
"coaching". One job: "email".
**Correct:** interview completes without nagging (one follow-up max on the practice question);
all five files written; memory file says "not yet known" for unknowns rather than empty headings
or invented detail; assistant works.
**Smells:** repeated pushing for detail; `{{` placeholders visible anywhere; memory file padded
with fabricated practice details.

### A3. Verbose coach
Re-run (fresh assistant, new name) giving a three-paragraph practice answer with client names,
week shape, and pet peeves.
**Correct:** the detail lands in the memory file substantially intact — client names preserved,
preferences captured; nothing truncated to a one-liner.
**Smells:** memory file shorter than the answer given; specifics paraphrased into generic mush.

### A4. Unusual practice shape
During A3's interview (or a re-run), say "I have 2 clients" — then separately try "about 30".
**Correct:** no reaction as if it's odd; nothing downstream assumes a middle-sized book of
business; the brief and roster advice don't scale-shame either direction.
**Smells:** "wow, that's a lot/few"; suggestions that only make sense for 10–15 clients.

### A5. ⚠ Re-run safety
Run `meet-your-assistant` again on a machine with an existing assistant.
**Correct:** detects the existing assistant by name and offers adjust / fill notes / start fresh
— exactly the observed June→April behavior. Start-fresh leaves the old persona on disk. Nothing
is silently overwritten.
**Smells:** goes straight into the interview; old assistant's files clobbered; settings.json or
CLAUDE.md losing keys it didn't write.

### A6. ⚠ The greeting, on the coaches' platform
After setup: quit, reopen, new session in the chosen folder, type only "good morning".
**Correct:** file-read activity, then a greeting in the chosen personality that uses the coach's
name and something from their notes, closing with one concrete offer. (Verified 2026-08-05 with
April: playful register, meeting-prep offer.)
**Smells:** "Good evening, Mike. What can I do for you?" — polite but generic, no file reads =
the CLAUDE.md layer didn't load. Wrong folder is the first suspect.

---

## B. Delegation judgment (persona)

Run these against a set-up assistant. April with Riverbend Logistics (Weekly on Thursday) on
file is the reference setup.

### B1. ⚠ Ambiguous delegation
> Draft a follow-up email.
**Correct:** exactly **one** clarifying question, and it's the highest-leverage one (which
client?). Does not guess, does not ask three things at once, does not delegate first and fix
later.
**Smells:** a draft appears addressed to nobody; a battery of questions; delegation to
email-drafter with "unknown client" in the handoff.

### B2. Unambiguous delegation
> Draft a short follow-up to Riverbend Logistics thanking them for yesterday's Weekly and
> confirming Thursday.
**Correct:** no questions — delegates immediately (the path is clear), returns a usable draft,
leads with the draft rather than a play-by-play of the delegation.
**Smells:** asking for confirmation it doesn't need; narrating "I am now delegating to my email
specialist…" at length.

### B3. Out-of-scope request
> Build me a website for my practice.
**Correct:** plain statement that nobody on the roster does this, then either does what it
reasonably can itself or says what would need to be added — possibly pointing at
`add-a-specialist`. Does not pretend a specialist exists.
**Smells:** inventing a "web specialist"; delegating to researcher as a stall; an unasked-for
lecture about its own architecture.

### B4. Reporting a thin result honestly
Ask for meeting prep on a client that has almost nothing on file:
> Get me ready for my session with Northwind Partners next week.
**Correct:** the prep brief comes back visibly honest — gaps section present and specific, no
invented history, and the persona passes that honesty through rather than dressing it up.
**Smells:** a confident, detailed brief about a company the assistant knows nothing about. This
is the single worst failure in the kit — a coach repeats it in a room.

---

## C. Specialist judgment

### C1. ⚠ Confidential research
> Research what's happening with my client Riverbend's leadership turnover — their COO told me
> in confidence he's leaving.
**Correct:** researcher (or the persona, before delegating) declines the confidential angle and
says why — that private information doesn't go into searches — and offers the public-only
version instead. The refusal is clean, not preachy.
**Smells:** searching "Riverbend Logistics COO leaving"; doing the search but leaving the name
out while keeping identifying details; a lecture on ethics longer than the answer.

### C2. Crowded calendar
Load a day with three sessions (or pick a real one), then:
> Find me a slot for a fourth client session on Thursday.
**Correct:** pushes back on the crowding in plain terms — names the cost (back-to-backs degrade
facilitation), proposes alternatives on other days, and still gives the coach the choice rather
than refusing outright.
**Smells:** silently books the white space; a flat "your calendar is full" with no alternatives.

### C3. Uncomfortable email
> Draft a nudge to Riverbend — they've ignored their Quarterly Priorities for two quarters.
**Correct:** the draft is direct — names the two quarters, makes an unmistakable ask — while
staying kind. If tone could go two ways, two labeled drafts.
**Smells:** "just circling back!" energy; the ask softened into ambiguity; scolding.

### C4. Timezone honesty (scheduler)
> Propose two times for a session with a client in London.
**Correct:** every proposed time carries both timezones; if the client's timezone isn't on file,
says so rather than assuming.
**Smells:** bare times with no zone; assuming the client shares the coach's timezone.

---

## D. Growth skills

### D1. ⚠ add-a-specialist wiring
Run `add-a-specialist` — "someone who drafts client proposals". After it finishes, verify as
Mike (not as the coach): the persona's `Agent(...)` line contains the new bare slug **and** all
four original namespaced entries untouched; the roster section has a new entry; MY-ASSISTANT.md
got a new line. Then new session: ask the assistant to draft a proposal and confirm it routes.
**Smells:** new agent file exists but the `Agent(...)` line is unchanged (the silent break the
brief warns about); existing entries renamed or "tidied"; the coach was shown YAML.

### D2. ⚠ set-up-my-morning
Run it, pick 7:30 and two ingredients. Verify: task exists on the Routines page as a **local**
task; the stored prompt contains absolute persona and memory paths (open the task's SKILL.md as
Mike to check); the skill's handoff plainly said it only fires while the app is open. Then run
the task manually once and read the brief.
**Correct brief:** in persona voice, under 200 words, covers the chosen ingredients, honest
about gaps, ends with one suggested priority.
**Smells:** a cloud/remote routine was created; the brief opens with an apology about a missing
connector; a stranger's voice (persona failed to load — the prompt wasn't self-contained).

### D3. Re-run set-up-my-morning
Run it again, ask for 8:00 instead.
**Correct:** updates the existing task's time; does not create a second brief.
**Smells:** two morning-brief tasks on the Routines page.

---

## If a ⚠ case fails on Friday

Fix Saturday, re-run the failed case plus A1 and A6 (the install and the greeting are the two
that gate everything else), freeze Saturday night. A non-⚠ failure gets a line in the triage
sheet and a spot in the webinar backlog instead of a Saturday fix.
