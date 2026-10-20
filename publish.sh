#!/usr/bin/env bash
# Build du dashboard + commit + push.
# Usage : ./publish.sh "Debrief 2026-10-20"
set -e
cd "$(dirname "$0")"

MESSAGE="${1:-Mise à jour suivi $(date +%F)}"

python3 build.py

git add data/suivi.json dashboard.html
if git diff --cached --quiet; then
  echo "Rien à publier."
  exit 0
fi

git commit -m "$MESSAGE"
git push
echo "Publié : $MESSAGE"
