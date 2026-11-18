#!/usr/bin/env bash
# Install the Content Studio skills for Claude Code.
# Usage: scripts/install.sh [--project]   (default: user-wide ~/.claude/skills; --project: ./.claude/skills)
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
dest="$HOME/.claude/skills"
[ "${1:-}" = "--project" ] && dest="$PWD/.claude/skills"
mkdir -p "$dest"
for d in "$root"/skills/*/; do
  name="$(basename "$d")"
  rm -rf "$dest/$name"
  cp -R "$d" "$dest/$name"
  echo "installed $name -> $dest/$name"
done
# the skills refer to pack files (templates, adapters, docs, scripts): keep them next to the skills
rm -rf "$dest/_content-studio"
mkdir -p "$dest/_content-studio"
cp -R "$root"/{templates,adapters,docs,scripts} "$dest/_content-studio/"
echo "pack resources -> $dest/_content-studio"
echo "Done. Start Claude Code and say: set up Content Studio"
