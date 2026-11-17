# Coach workshop, 17 November 2026

Presenter files for the day: August's morning, then the Bloom MCP hour (2:00–3:00, beta).

| File | What it is |
|---|---|
| `slides.pdf` | The whole day, 34 slides, 16:9. Works offline. Slides 1–15 are August's morning with the afternoon times updated; 16–34 are the Bloom MCP hour. |
| `slides-src.html` | The source, in the same style as `../slides-src.html`. Edit this, then re-render. |
| `shots/` | Real answers for demo steps 1, 2, 3 and 5, from a Claude chat with only the Bloom Staging connector on. Made-up clients on Bloom's test site. |
| `prompt-sheet.html` | For the presenter's second monitor: every prompt with a Copy button (keys 1–6 copy the demo steps), what to watch for, what to say, and the slide number. Works offline. |
| `demo-coach/` | The demo coaching folder: an assistant, Juniper, set up the way the kit sets one up, for a made-up firm whose three clients live on Bloom's test site. |
| `render.sh` | Re-renders `slides.pdf` from the source. |

## On the presenting laptop

1. Pull this repo.
2. In Claude, update the Bloom coach kit to **0.9.1 or later** and restart Claude. Prep through the
   assistant (demo step 4) needs the kit that reads Bloom.
3. Copy `demo-coach` out of the repo into a regular folder. The kit doesn't behave inside a git
   repository, so don't open it where it is.
   - Windows (PowerShell, from the repo root):
     `Copy-Item -Recurse .\workshop\2026-11\demo-coach (Join-Path ([Environment]::GetFolderPath('MyDocuments')) 'Bloom demo coach')`
   - Mac (from the repo root): `cp -R workshop/2026-11/demo-coach ~/Documents/"Bloom demo coach"`
4. In Claude, start a new session in that folder. Connectors: **Bloom Staging on**; Bloom (prod),
   mail, Slack and Drive off. Say "good afternoon" and Juniper should answer.
5. Open `slides.pdf` full screen, and `prompt-sheet.html` in a browser on the second monitor.

`demo-coach/.claude/settings.json` blocks two Code-side Bloom servers by name (`bloom-staging`,
`bloom-prod`) that some machines have, so the assistant only sees the account's Bloom Staging
connector. It does nothing where those servers don't exist.

## Demo steps 4 and 6

Both go through the assistant, so they only run in the desktop app, in the demo folder. Until they
are captured, slides 24 and 26 show what you should see. To swap in the real thing:

1. Run each prompt in the demo folder (they're on the prompt sheet) and snip the answer.
2. Save the snips here as `shots/4-prep.png` and `shots/6-todo.png`. The slides pick them up on
   their own.
3. Re-render: `bash render.sh` in Git Bash (uses Playwright's headless Chromium), or open
   `slides-src.html` in Chrome, Print, Save as PDF, margins None, background graphics on.

Step 6 is the trust moment: the assistant writes the To-Do out and tells you to add it yourself.
Never run it in a plain chat. Plain Claude may create the To-Do in your own firm instead.
