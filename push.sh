#!/usr/bin/env bash
# Commit everything except backup/ and push it to main.
set -euo pipefail
cd "$(dirname "$(readlink -f "$0")")"

git add -A .
if git diff --cached --quiet; then
    echo "Nothing to commit."
else
    git --no-pager diff --cached --name-status
    default="Update $(date '+%Y-%m-%d %H:%M:%S')"
    read -r -p "Commit message [$default]: " message
    git commit -m "${message:-$default}"
fi
git push -u origin main
