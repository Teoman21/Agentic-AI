#!/usr/bin/env bash
# Pull the latest lecture files and make your own working copy of a session.
# Usage: ./scripts/new-week.sh W03a
set -euo pipefail

WEEK="${1:-}"
if [[ -z "$WEEK" ]]; then
  echo "usage: $0 <WEEK>   e.g. $0 W03a" >&2
  exit 1
fi

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT/lecture-files"

# Running a notebook writes outputs into lecture-files, which blocks a pull.
if ! git diff --quiet; then
  echo "lecture-files has local changes (notebook outputs). Restoring..."
  git restore .
fi
git pull

cd "$ROOT"
if [[ ! -d "lecture-files/$WEEK" ]]; then
  echo "error: lecture-files/$WEEK does not exist yet. Available:" >&2
  ls -d lecture-files/W* 2>/dev/null | sed 's|lecture-files/|  |' >&2
  exit 1
fi

if [[ -d "$WEEK" ]]; then
  echo "note: $WEEK/ already exists — leaving your work untouched."
else
  cp -r "lecture-files/$WEEK" "$WEEK"
  echo "created $WEEK/ — open the copy, not the original."
fi
