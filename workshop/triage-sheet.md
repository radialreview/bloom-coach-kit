# Triage sheet — print one page for Stephanie

Rules of engagement, before the table:

- **Anything not on this sheet: flag Mike. Don't improvise.** A wrong fix in front of a coach
  costs more than a two-minute wait.
- **Keep the running question log** — every question a coach asks, verbatim, even the ones you
  answer on the spot. That log is the webinar curriculum.
- Fixes are ordered by when coaches hit them: install → setup → first use → morning brief.

| # | Symptom | Fix |
|---|---------|-----|
| 1 | Windows: Code tab won't start a session | Git for Windows isn't installed (pre-work step 3). Install it, then **fully quit and reopen** the app. |
| 2 | No Code tab at all | Free account — can't be fixed in the room. Pair them with a neighbor (Mike has the list of unconfirmed plans from the pre-work replies). |
| 3 | "Add marketplace" can't find the plugin | They typed a URL, or downloaded a ZIP from the web. The box wants exactly: `radialreview/bloom-coach-kit` — nothing else. Settings → Plugins → Add → Add marketplace. |
| 4 | Plugin installed but `/meet-your-assistant` isn't offered | Open a **new session** first. Still missing: Settings → Plugins → remove the marketplace, re-add it, reinstall, new session. |
| 5 | Skill finished but the assistant isn't there in a new session | **Wrong folder** — the assistant lives in the folder they picked during setup. Check the folder chip on the session screen. If the folder is right: quit the app completely, reopen, new session. |
| 6 | "It answers like a stranger / forgot who I am" | Same as #5 — folder first. If the folder is right, have them say: *"read your notes about me."* |
| 7 | "It never greeted me" | It won't speak first — that's by design. Have them type "good morning." The greeting comes back knowing who they are. |
| 8 | Files seem to be in the wrong place / "where did my stuff go" | They picked a folder that's set up for software projects (a git repo) — sessions get isolated copies. Move to a plain folder (Documents works) and re-run the setup skill. |
| 9 | Folder access denied | The trust dialog wasn't accepted. Reopen the folder and accept it. |
| 10 | Connector shows in the + menu but returns nothing | Re-authenticate it from the **+** menu, then start a **new conversation**. |
| 11 | Assistant/specialist says it can't see calendar or email | The connector was never authorized. + menu → connect it → approve in the browser → new conversation. Google coaches: Gmail + Google Calendar connectors. Microsoft coaches: the **Microsoft 365** connector (mail + calendar in one). |
| 11a | Microsoft coach: M365 connector won't sign in, or shows "Need admin approval" | Two causes. Personal `@outlook.com`/`@hotmail.com` account → can't connect at all (business accounts only) — assistant runs notes-based, still works. Business account with the approval screen → their IT admin must consent once; **cannot be fixed in the room** — log it, tell the coach their assistant works from notes until IT clicks yes, Mike sends the IT instructions after. |
| 12 | Morning brief came back without calendar (notes only) | The supervised **Run now** never happened or a permission prompt wasn't approved. Routines page → Run now → approve every prompt that appears. |
| 13 | Morning brief page (the bookmark) shows yesterday | The app wasn't open at brief time — it catches up when the app next opens. Not a bug. Check the date at the top after the app has been open a minute. |
| 14 | Morning brief page never updates, even with the app open | Flag Mike — likely the page URL wasn't stored and runs are minting new pages. (Mike: check `agent-memory/<slug>/morning-brief-url.txt` exists and matches the bookmark.) |
| 15 | Coach on a Pro plan says Claude warned about usage limits | Model picker (name near the message box) → **Sonnet**. Assistant is unchanged. If it's the daily brief eating the plan: Routines → Edit routine → Model → Sonnet 5. |

**Weird ones that only happen on developer machines** (unlikely Tuesday, listed so they don't
burn time): scheduled runs missing connectors because the folder's settings contain an `agent`
key from an old kit version (re-run the setup skill — it removes it), a stale second `claude`
binary on PATH, or CLI auth on API billing instead of the claude.ai login. All three: flag Mike,
move on.
