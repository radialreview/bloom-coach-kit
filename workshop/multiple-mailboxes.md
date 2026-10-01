# Multiple mailboxes — one inbox your assistant can actually work

**For:** any coach with more than one email address. A coaching practice plus a shop, a practice
plus a newsletter, an old address clients still use.
**Where it goes:** open floor, or a webinar. **Not** the pre-work email — see the notes at the
bottom for why.
**Coach's time:** about 15 minutes, once.

Three notes on why this is shaped the way it is:

- **Claude's email connector holds one Google account at a time.** That's the whole problem. There
  is no multi-account setting to find, so a coach hunting for one is a coach who'll email Mike.
  The fix isn't in Claude — it's in Gmail, before the connector is ever authorized.
- **Forwarding, not software.** A multi-account email server exists as an option and is the wrong
  answer here: a coach can't judge whether it's trustworthy, can't tell why it stopped working, and
  when it does stop working they call Mike. Fifteen coaches times one fragile dependency is a
  support queue. Gmail's own forwarding never breaks, costs nothing, and needs no maintenance.
- **Forwarding first, then send-as.** Both steps make Gmail mail a confirmation code, and doing
  them in this order means every code lands somewhere the coach is already looking. Reverse the
  order and they're hunting through an inbox they just stopped reading. This is the step that
  generates support calls; the order is the fix.

---

## For the coach

You've got mail arriving in more than one place. Your assistant can only watch one of them.

Rather than pick a favourite and lose the rest, you're going to point everything at a single
inbox — and set it up so replies still go out from the right address. Your clients see no
difference. Your assistant sees everything.

### 1. Pick your hub

**Use the account for your main business** — the one that pays you. Everything else forwards into
it.

Not an arbitrary choice. Once this is set up, a reply can occasionally leave from the hub address
instead of the one you intended. If that happens, a shop email going out under your coaching name
is a little odd. A client email going out under "Wildflower Candle Co." is worse. Point the risk at
the direction that matters least.

### 2. In each *other* account, turn on forwarding

Sign in to the other account and go:

**Gear icon → See all settings → Forwarding and POP/IMAP → Add a forwarding address**

Enter your hub address. Gmail sends a **confirmation code to your hub inbox** — go and read it,
click the link, come back, and choose **Forward a copy of incoming mail**.

Leave it on **keep Gmail's copy in the Inbox** for now. Nothing disappears from where it's always
been, which makes this easy to undo if you change your mind.

Repeat for each account. Two accounts, two passes. Four, four.

> **If forwarding is greyed out or refuses:** it's a work account whose administrator has switched
> it off. Stop there and flag it — that one needs a different answer.

### 3. In your hub, add each address as a "send mail as"

Now back in your hub account:

**Gear icon → See all settings → Accounts and Import → Send mail as → Add another email address**

Add each of the other addresses, one at a time. Gmail sends a verification code to each — and
because you did step 2 first, **those codes now arrive in this inbox.** That's the whole reason for
the order.

This is the step that makes the setup genuinely good rather than merely tolerable. Reply to a shop
email and it goes out from the shop address. Reply to a client and it goes out as you. Your
assistant drafts it, you send it, and the right name is on it without either of you thinking about
it.

### 4. Label what's coming in

**Gear icon → See all settings → Filters and Blocked Addresses → Create a new filter**

In the **To** box put one of your forwarded addresses. Next → **Apply the label** → make a new one
named after that business. Do it once per forwarded address.

Skip this and everything lands in one undifferentiated pile, and your assistant treats a wholesale
enquiry and a client in crisis as equally urgent. Two minutes here is what lets it tell them apart.

### 5. Tell your assistant

Last step, and the only one that isn't Gmail. Open a session and say it in your own words —
something like:

> *I run two businesses. My coaching practice is the main one, and that mail comes straight to
> this address. My shop mail is forwarded in and lands under the Shop label. When you draft a
> reply, send it from whichever address it came to.*

It'll write that into its notes. From then on it knows which hat it's wearing.

### One thing this doesn't do

Forwarding moves **new** mail only. Everything already sitting in the other accounts stays there.
Don't close those accounts or stop paying for them — they're still the home of your history, and
they're still where the forwarding comes from.

---

## For Mike, not for the coaches

**Why this isn't a fourth pre-work ask.** The pre-work email works because it asks for three
things and gets one reply. A fourth ask costs compliance on the three that block the session —
and the paid-plan check is the one that genuinely can't be fixed in the room. Mailbox
consolidation blocks nothing: calendar carries the Tuesday demo and email sits behind the cut
line. It doesn't belong in front of the session.

**Where it does belong.** Two places:

- **Open floor.** It sits alongside `add-a-specialist` as a thing for coaches who are moving
  fast — hand them this sheet and let them work down it. Most coaches with a side business will
  self-identify the moment email gets connected and only one inbox shows up.
- **A webinar.** It's a better fit here than in the room: it's fifteen minutes of settings
  screens, it's the same five steps for everyone, and it records once and serves every future
  cohort. If the question log from Tuesday has multiple mailboxes in it, that's the signal to
  give it a slot rather than a mention.

**The case where this advice is wrong.** A mailbox the coach's employer owns. Consolidating that
into a personal account moves company material off the company's tenant, and forwarding personal
mail *into* it hands their own business correspondence to someone else's retention and
administrator access. Independent coaches never hit this. A coach with a day job plus a practice
hits it squarely — and for them the answer is two separate setups, not one hub. Ask before
recommending; don't let the sheet make the call.

**Expected support calls, in order:**

1. The confirmation code in step 2 — they don't realise it's gone to the *other* inbox, or they
   click the link while signed into the wrong account. Most common by a distance.
2. Send-as verification appearing to fail when they've done steps 2 and 3 out of order.
3. Workspace admin has forwarding disabled — not fixable by the coach.

**Why not the multi-account route.** Worth having the answer ready, because a technical coach will
ask. Claude Code can hold several accounts through a locally-configured server, scoped per folder,
and it works — Mike runs a variant of it. It also means third-party code holding live credentials
for their mail, a setup step involving a command line, and a failure mode only Mike can diagnose.
For a coach whose business runs on that inbox, the trade is bad. Forwarding gets them the same
outcome with nothing to maintain.
