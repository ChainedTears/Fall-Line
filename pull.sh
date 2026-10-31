#!/usr/bin/env bash
# Move everything in this folder into backup/<timestamp>/, then pull a fresh copy of main.
set -euo pipefail
cd "$(dirname "$(readlink -f "$0")")"

dest="backup/$(date +%Y-%m-%d_%H-%M-%S)"
mkdir -p "$dest"

shopt -s dotglob nullglob
for item in *; do
    case "$item" in
        backup|.git) continue ;;
    esac
    mv -- "$item" "$dest/"
done

git fetch origin main
git reset --hard origin/main
echo "Backed up old files to $dest and pulled latest main."
