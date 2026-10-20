#!/usr/bin/env bash
# Build du dashboard + commit + push.
# Usage : ./publish.sh "Debrief 2026-10-20"
set -e
cd "$(dirname "$0")"

MESSAGE="${1:-Mise à jour suivi $(date +%F)}"

# Premier Python qui fonctionne vraiment : py (Windows), python3 (Mac), python
PY=""
for candidat in py python3 python; do
  if "$candidat" --version >/dev/null 2>&1; then PY="$candidat"; break; fi
done
if [ -z "$PY" ]; then echo "Python introuvable (py, python3, python)."; exit 1; fi

"$PY" build.py

git add data/suivi.json dashboard.html
if git diff --cached --quiet; then
  echo "Rien à publier."
  exit 0
fi

git commit -m "$MESSAGE"
git push
echo "Publié : $MESSAGE"
