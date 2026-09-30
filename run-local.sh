#!/usr/bin/env bash
# Run the whole MobilCube Google Ads toolkit on your own computer.
# Needs: git, Python 3.9+, Node 20+ (only for the image generator).
#   curl -O https://raw.githubusercontent.com/jpdemuszka-art/MobilCube/claude/optimistic-hamilton-isolc8/run-local.sh
#   bash run-local.sh
set -euo pipefail
REPO="https://github.com/jpdemuszka-art/MobilCube.git"
BRANCH="claude/optimistic-hamilton-isolc8"

if [ ! -f ads/build_import.py ]; then
  if [ -d MobilCube/.git ]; then cd MobilCube && git fetch origin "$BRANCH" && git checkout "$BRANCH" && git pull --ff-only origin "$BRANCH"
  else git clone --branch "$BRANCH" "$REPO" MobilCube && cd MobilCube; fi
fi

echo "== 1/4 Build the Google Ads Editor import files"
python3 ads/build_import.py

echo "== 2/4 Scan competitors (free) and collect Google search suggestions"
python3 tools/competitor-watch/watch.py --suggest

echo "== 3/4 Ad images with Gemini (skipped if no key)"
if [ -f tools/gemini-creatives/.env ] && grep -q '^GEMINI_API_KEY=.\+' tools/gemini-creatives/.env && ! grep -q 'your_key_here' tools/gemini-creatives/.env; then
  (cd tools/gemini-creatives && npm install --no-audit --no-fund && npm run gen:all && npm run check)
else
  echo "   Put GEMINI_API_KEY in tools/gemini-creatives/.env (copy .env.example) to generate images."
fi

echo "== 4/4 Preview the landing pages at http://localhost:8765 (Ctrl+C to stop)"
echo "   Import files: ads/google-ads-editor/   Competitor report: tools/competitor-watch/reports/latest.md"
cd landing && python3 -m http.server 8765
