#!/usr/bin/env bash
# Commit everything except backup/ and push it to main.
set -euo pipefail
cd "$(dirname "$(readlink -f "$0")")"

git add -A -- . ':!backup'
if git diff --cached --quiet; then
    echo "Nothing to commit."
else
    git commit -m "Update $(date '+%Y-%m-%d %H:%M:%S')"
fi
git push -u origin main
