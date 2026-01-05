#!/usr/bin/env bash
# Check repo + virtualenv sizes and warn if total exceeds 250M
set -e
THRESHOLD_MB=250
ROOT_DIR=$(pwd)
VENV_DIR=$(pip -V 2>/dev/null | awk '{print $6}' | sed 's:/bin/pip::' || echo "$HOME/.virtualenvs")
REPO_SIZE=$(du -sm "$ROOT_DIR" | awk '{print $1}')
VENV_SIZE=0
if [ -d "$VENV_DIR" ]; then
  VENV_SIZE=$(du -sm "$VENV_DIR" | awk '{print $1}')
fi
TOTAL=$((REPO_SIZE + VENV_SIZE))

echo "Repo size: ${REPO_SIZE} MB"
echo "Venv dir size: ${VENV_SIZE} MB"
echo "Total size: ${TOTAL} MB (threshold ${THRESHOLD_MB} MB)"

if [ "$TOTAL" -gt "$THRESHOLD_MB" ]; then
  echo "WARNING: total size exceeds ${THRESHOLD_MB} MB. Consider using 'requirements-light.txt' and removing optional packages." >&2
  exit 2
fi

echo "OK: total size under ${THRESHOLD_MB} MB"
