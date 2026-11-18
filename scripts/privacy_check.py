#!/usr/bin/env python3
"""Fail if personal data or project-specific names leak outside examples/.
Run from the repo root. Edit DENY to add your own terms for your fork."""
import os, re, sys

DENY = [r"temporia", r"@gmail\.com", r"@outlook\.", r"api[_-]?key\s*[:=]", r"secret\s*[:=]\s*\S+", r"sk-[A-Za-z0-9]{20,}"]
ALLOW_DIRS = ("examples", ".git")
ALLOW_FILES = {"tests/test_pack.py", "README.md", "README.fr.md", "scripts/privacy_check.py", "CHANGELOG.md"}
bad = 0
for dp, dn, fn in os.walk("."):
    rel_dir = os.path.relpath(dp, ".")
    if rel_dir.split(os.sep)[0] in ALLOW_DIRS:
        continue
    for f in fn:
        rel = os.path.normpath(os.path.join(rel_dir, f))
        if rel in ALLOW_FILES or f.endswith((".png", ".jpg", ".mp4", ".zip")):
            continue
        try:
            txt = open(os.path.join(dp, f), encoding="utf-8").read()
        except (UnicodeDecodeError, OSError):
            continue
        for pat in DENY:
            for m in re.finditer(pat, txt, re.I):
                line = txt.count("\n", 0, m.start()) + 1
                print("LEAK %s:%d matches /%s/" % (rel, line, pat)); bad += 1
print("privacy check: %d problem(s)" % bad)
sys.exit(1 if bad else 0)
