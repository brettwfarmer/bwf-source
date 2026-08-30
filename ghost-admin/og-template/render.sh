#!/usr/bin/env bash
# Render a BWF OG card to a 1200x627 PNG.
#
#   ./render.sh "Post title" "Series name" [outfile.png]
#
# Series must match one of the four keys in card.html's ACCENTS map; anything
# else falls back to steel. Fonts are vendored in fonts/, so this works offline
# and never renders in a fallback face. Requires Google Chrome. No npm deps.
set -euo pipefail

TITLE="${1:?usage: render.sh \"Title\" \"Series\" [out.png]}"
SERIES="${2:?usage: render.sh \"Title\" \"Series\" [out.png]}"
OUT="${3:-og-card.png}"

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[ -x "$CHROME" ] || { echo "Chrome not found at $CHROME" >&2; exit 1; }

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
enc() { python3 -c 'import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1]))' "$1"; }
URL="file://$DIR/card.html?title=$(enc "$TITLE")&series=$(enc "$SERIES")"

TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT

# NOTE: do not add --virtual-time-budget. It hangs indefinitely here with
# --screenshot; the load event alone is sufficient now that fonts are local.
"$CHROME" --headless --disable-gpu --no-sandbox --hide-scrollbars \
  --force-device-scale-factor=1 --window-size=1200,627 \
  --user-data-dir="$TMP" --screenshot="$OUT" "$URL" >/dev/null 2>&1 &
CPID=$!
( sleep 45; kill -9 $CPID 2>/dev/null ) & WPID=$!
wait $CPID 2>/dev/null || true
kill $WPID 2>/dev/null || true

[ -s "$OUT" ] || { echo "render failed: no output" >&2; exit 1; }
echo "wrote $OUT ($(wc -c < "$OUT" | tr -d ' ') bytes)"
