---
name: track-my-hours
description: Keeps the coach's billable hours and turns them into invoices. That means a plain timesheet per client, a PDF invoice built from it, and nudges when an invoice is due or unpaid. Use when a coach says anything like "log my hours", "I put three hours into Acme today", "how many hours have I got this month", "time to invoice", "build the Acme invoice", "they paid", or asks to be reminded to send invoices.
---

# Track My Hours

The coach's billable time, kept somewhere they can trust: one row per piece of work, invoices
built from those rows, and a nudge before anything goes unbilled or unpaid.

The coach is **not technical**. Talk about hours, clients and invoices, never about
spreadsheets, scripts or file paths. When they need a file, open it or open the folder it's in.
Don't describe where it lives.

## Where it lives

If the folder has `memory/about-my-coach.md`, billing lives in `memory/billing/<client-slug>/`.
Otherwise it lives in `~/billing/<client-slug>/`. Each client gets its own folder:

| File | What it holds |
|---|---|
| `client.md` | Billing details, copied from `client-template.md` next to this file |
| `timesheet.csv` | `date,start,end,hours,description,invoice` |
| `invoices.csv` | `number,issued,period_from,period_to,hours,amount,due,paid` |
| `invoices/` | Each invoice's PDF, plus the HTML it was printed from |

The client slug is the client's name in lowercase with hyphens (`acme-co`). Create each CSV with
its header row the first time it's needed. In the CSVs, dates are `YYYY-MM-DD`, times are 24-hour
`HH:MM`, and hours and amounts are plain numbers with 2 decimals and no currency sign. Quote any
field that contains a comma or a double quote. These are plain files, so they open in any
spreadsheet and outlive any tool.

**Rows are permanent.** Write to an existing row in only two cases: filling in a timesheet row's
`invoice` column or an invoice's `paid` column, and making a change the coach asked for.

In `client.md`, a value that starts with `?` isn't known yet. Replace the whole cell when you fill
it in. Store the rate as a plain number.

## Every run: check first

Before anything else, say each of these that's true, one line apiece. Say nothing if none are.
- An invoice is past due and `paid` is empty: "Invoice ACME-0003, $1,240, was due Oct 30 and isn't marked paid."
- A billing period has closed and still has unbilled rows: "October's closed with 31.5 unbilled hours for Acme. Want the invoice?"

A period is a calendar month when `Billing cadence` is monthly or `?`. For every N weeks,
periods count forward from `Period starts`.

## Log hours

1. **Pick the client.** If there's exactly one billing folder, use it. If there are none, ask,
   and offer a client named in the coach's notes as the likely answer.
   **For a new client**, ask three things in plain words: the client's name, a word in calendar
   invites (or their email domain) that means this client, and, if they do the work in Claude
   Code, the name of the folder they work in. Then create its folder from the template with
   those three filled in. Leave everything else as `?` until an invoice needs it.
2. **Gather what you can see** since the client's last logged row. With no rows yet, look back
   7 days. Check whichever of these sources exist:
   - **Calendar**, if it's connected: events whose title or attendees match `Calendar match`.
     Skip any event whose date and start time are already in the timesheet.
   - **Claude Code sessions**, if Python is available and `Project folder` is filled in. Run
     `python3 active_time.py --project "<Project folder>" --after "<YYYY-MM-DD HH:MM>" --idle <minutes> --round <minutes>`.
     For `--after`, use the latest date and `end` among this client's session rows. If there
     isn't one, use `--from <date 7 days ago>` instead. The numbers come from `Idle gap` and
     `Rounding`. Use `python` or `py` on Windows, and the script sits next to this file. It
     prints only what came after that moment: the active spans for each day, with idle gaps
     dropped, and a rounded total. So nothing it prints has been logged yet.
   - If neither is available, go straight to asking.
3. **Propose, then ask.** Show what you found with 12-hour times ("7:00 to 7:40 pm") and the
   hours it adds up to. Then ask about anything the sources can't see: prep, reading, thinking,
   calls that weren't on the calendar. Added work is dated today unless the coach says
   otherwise. **The coach's number wins** over anything you propose. If nothing new turned up and
   they add nothing, say so and write nothing.
4. **Get a description for every row**, in the coach's words. A row is one piece of work the
   coach describes: a day's session work is one row, and a call they add is another. Write each
   description the way the client will read it on the invoice, saying what was delivered in
   plain words ("Leadership quarterly: agenda, facilitation, follow-up notes"). Never make up a
   description the coach didn't give you. Ask for it.
5. **Write the rows** only after the coach confirms the hours. `hours` is what they confirmed.
   For session work, `start` and `end` are the first and last times the script printed. For a
   calendar event, they're the event's times. For anything the coach added, leave them blank.
   Read back what you logged, then the period's unbilled hours, with the amount once there's a
   rate.

## Status

Show the unbilled hours and the amount for each client in the current period, plus the two
checks above.

## Build an invoice

1. **Fill in the blanks first.** Ask in one go for every `?` in `client.md` except `Period starts`,
   `Calendar match` and `Project folder`. If they bill every N weeks, also ask when the first
   period started.
2. **Show it before you build it.** The invoice covers every unbilled row up to its end date.
   That's the end of the period, or an earlier date the coach names ("October so far" means
   today). Its start date is the start of the period. List the rows with their total hours and
   amount, and get a yes.
3. **Fill in `invoice-template.html`**, which sits next to this file, and replace every
   double-brace placeholder:
   - `invoice_number`: `<Invoice prefix>` followed by the next number, padded to 4 digits (ACME-0001).
   - `issue_date` and `due_date`: dates like "Oct 8, 2026". The due date is the issue date plus
     the payment terms.
   - `period`: the start and end dates, like "Oct 1 – Oct 8, 2026". The same two dates go in
     `period_from` and `period_to`.
   - `from_name`, `from_address`, `from_email`: `From`, `Address`, `Email`.
   - `client_name`: `Client`. `billing_contact`: the contact's name only.
   - `payment_instructions`: `How to pay`.
   - `total_hours`, `rate`, `total`: hours with 2 decimals, and money with the currency's symbol
     and 2 decimals ("$1,240.00").
   - `line_items`: one row per timesheet row, in date order:
     `<tr><td>2026-10-08</td><td>Description</td><td class="num">2.25</td><td class="num">$270.00</td></tr>`.

   Escape `&`, `<` and `>` in every value you put into the HTML.

   Save it as `invoices/<number>.html`.
4. **Print it to PDF** with headless Chrome or Edge. Give it a fresh profile folder in the
   system temp folder, or a browser window that's already open will swallow the job:
   `<browser> --headless=new --user-data-dir=<temp folder> --no-pdf-header-footer --print-to-pdf=<out.pdf> <file:/// URL of the html, spaces as %20>`
   On macOS, Chrome is at `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`. On
   Windows, Edge is at `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`. The
   command can return before the PDF exists, so **wait for the file**, then delete the temp
   profile. **Open the PDF and check it** before you call it done. If neither browser is
   installed, open the HTML in the coach's browser and walk them through Print → Save as PDF.
5. **Record it.** Put the invoice number in the `invoice` column of those rows, add a row to
   `invoices.csv`, and bump `Next invoice number` in `client.md`.
6. **Hand it over.** Open the PDF, or the folder it's in, so the coach can attach it. Then draft
   the cover email in their voice (read `memory/writing-voice.md` if it exists): to, subject,
   and a body of two or three lines, signed with their first name. **Never send it.** If a mail connector is available, ask
   whether it's signed into the `Send from` account. Only if they say yes, offer to save the
   draft there. Never use any other account.
7. **Offer the reminder** on the first invoice built while a scheduled-task tool is available,
   if `Reminder offered` is `no`. The offer is a weekly task, Monday morning, run in this
   folder, with this prompt: "Run track-my-hours status and tell me if an invoice is due or
   unpaid." Set `Reminder offered` to `yes` whatever they answer.

## Mark paid

"Acme paid number 3" means ACME-0003. Set `paid` to today, or to the date they give. If they
don't give a number and only one invoice is unpaid, it's that one. Otherwise, ask which one.
