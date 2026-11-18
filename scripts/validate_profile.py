#!/usr/bin/env python3
"""Validate a Content Studio profile. Usage: validate_profile.py studio/profile.yml
Exit code 0 = valid (warnings allowed), 1 = errors. Needs PyYAML."""
import re, sys
try:
    import yaml
except ImportError:
    sys.exit("PyYAML missing: pip install pyyaml")

HEX = re.compile(r"^#[0-9a-fA-F]{6}$")
BACKENDS = {"local", "notion", "google-sheets", "airtable"}
SOURCES = {"metricool", "platform-export", "manual"}


def get(d, path):
    for k in path.split("."):
        if not isinstance(d, dict) or k not in d:
            return None
        d = d[k]
    return d


def main(path):
    with open(path, encoding="utf-8") as fh:
        p = yaml.safe_load(fh)
    errors, warns = [], []
    if not isinstance(p, dict):
        sys.exit("error: profile is empty or not a mapping")
    for req in ["identity.name", "identity.language", "identity.audience.description", "identity.goal"]:
        if not get(p, req):
            errors.append("missing required field: " + req)
    domains = [x for x in (get(p, "scope.domains") or []) if x]
    if not domains:
        errors.append("scope.domains must list at least one topic domain")
    elif len(domains) > 8:
        warns.append("scope.domains has more than 8 entries: a narrow scope gives better ideas")
    if not [c for c in (p.get("channels") or []) if c.get("name")]:
        errors.append("channels: define at least one channel")
    for k, v in (get(p, "brand.colors") or {}).items():
        if v and not HEX.match(str(v)):
            errors.append("brand.colors.%s is not a #RRGGBB hex code: %r" % (k, v))
    if get(p, "tracking.backend") not in BACKENDS:
        errors.append("tracking.backend must be one of %s" % sorted(BACKENDS))
    if get(p, "analytics.source") not in SOURCES:
        errors.append("analytics.source must be one of %s" % sorted(SOURCES))
    if get(p, "rules.automate_engagement") is True:
        errors.append("rules.automate_engagement must stay false: this pack never automates likes, follows or comments")
    if get(p, "rules.require_human_approval") is False:
        warns.append("rules.require_human_approval is false: nothing should be published without a human yes")
    if not get(p, "voice.tone"):
        warns.append("voice.tone is empty: content will sound generic")
    if not get(p, "brand.colors.primary"):
        warns.append("brand colors not set (needed for visuals and video)")
    for e in errors:
        print("ERROR  " + e)
    for w in warns:
        print("WARN   " + w)
    print("%d error(s), %d warning(s)" % (len(errors), len(warns)))
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
