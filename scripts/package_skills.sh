#!/usr/bin/env bash
# Build one .zip per skill (for Claude.ai "upload a skill") into dist/.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$root/dist"
cd "$root/skills"
for d in */; do
  name="${d%/}"
  rm -f "$root/dist/$name.zip"
  zip -qr "$root/dist/$name.zip" "$name" -x '*/__pycache__/*'
  echo "dist/$name.zip"
done
