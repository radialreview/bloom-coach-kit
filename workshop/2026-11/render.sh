#!/usr/bin/env bash
# Re-render the day deck: slides-src.html -> slides.pdf (16:9, one slide per page).
# Needs Playwright's headless Chromium (already on this laptop) and the internet once,
# for the Google Fonts. The PDF embeds the fonts, so it then works offline.
# Usage (Git Bash): bash render.sh
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd -W 2>/dev/null || pwd)"
shell_exe="$(ls "$LOCALAPPDATA"/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-win64/chrome-headless-shell.exe | tail -1)"
"$shell_exe" --headless --disable-gpu --allow-file-access-from-files \
  --virtual-time-budget=20000 --no-pdf-header-footer \
  --print-to-pdf="$here/slides.pdf" "file:///$here/slides-src.html" 2>/dev/null
echo "wrote $here/slides.pdf"
