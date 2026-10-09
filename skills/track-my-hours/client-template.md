# Billing details

The track-my-hours skill reads this file. A `?` means the value isn't known yet, and the skill
asks for it when it needs it.

| Field | Value |
|---|---|
| Client | ? |
| Billing contact | ? |
| Billing email | ? |
| Rate per hour | ? |
| Currency | USD |
| Billing cadence | ? (monthly, or every N weeks) |
| Period starts | ? (only for every-N-weeks billing: the first day of the first period) |
| Payment terms | ? (for example, Net 15) |
| Rounding | 15 minutes |
| Idle gap | 20 minutes |
| Calendar match | ? (a word in calendar titles, or an attendee's email domain, that means this client) |
| Project folder | ? (only if the work happens in Claude Code: that folder's name, like acme-site) |
| From | ? (your name or business name, as it should appear on the invoice) |
| Address | ? |
| Email | ? |
| How to pay | ? (the payment instructions printed on the invoice) |
| Send from | ? (the email account invoices go out from) |
| Invoice prefix | ? (for example, ACME-) |
| Next invoice number | 1 |
| Reminder offered | no |
