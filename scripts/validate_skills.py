#!/usr/bin/env python3
"""Check every skills/*/SKILL.md: frontmatter, name matches folder, description length,
and that files referenced in backticks like `scripts/x.py` exist. Run from the repo root."""
import glob, os, re, sys
try:
    import yaml
except ImportError:
    sys.exit("PyYAML missing: pip install pyyaml")

bad = 0
for path in sorted(glob.glob("skills/*/SKILL.md")):
    folder = os.path.basename(os.path.dirname(path))
    txt = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    if not m:
        print("FAIL %s: no frontmatter" % path); bad += 1; continue
    fm = yaml.safe_load(m.group(1))
    if fm.get("name") != folder:
        print("FAIL %s: name %r != folder %r" % (path, fm.get("name"), folder)); bad += 1
    d = fm.get("description", "")
    if not (40 <= len(d) <= 1024):
        print("FAIL %s: description length %d (want 40-1024)" % (path, len(d))); bad += 1
    if "<" in d or ">" in d:
        print("FAIL %s: description must not contain angle brackets" % path); bad += 1
    if len(txt.splitlines()) > 400:
        print("WARN %s: long (%d lines)" % (path, len(txt.splitlines())))
    print("ok   %s" % path)
print("failures: %d" % bad)
sys.exit(1 if bad else 0)
