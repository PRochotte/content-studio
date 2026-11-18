# Contributing

Thanks for helping. Keep the pack **generic**: no brand-specific names, handles, colours or facts outside `examples/`.

## Add a skill
1. `skills/<name>/SKILL.md` with frontmatter `name` (= folder) and a `description` that says **when** to use it (40 to 1024 chars, no angle brackets).
2. Read the profile; never hard-code a brand. Respect the rules: scope, `never_invent`, human approval, no engagement automation.
3. Keep SKILL.md focused (under ~300 lines). Put scripts in `skills/<name>/scripts/`, stdlib only if possible.
4. `pytest -q` must pass.

## Add an adapter
Copy `adapters/local.md`; implement Create, Read, Write, Update, Limits on the fields of `docs/data-contract.md`.

## Add an example profile
`examples/<name>/profile.yml` + a short README. It must pass `scripts/validate_profile.py`. Use only facts you are allowed to publish and no personal data (no emails, private links, tokens).

## Style
Plain language, short sentences. Say what to do, not how clever it is. When a rule exists for a reason, give the reason in one line.

## Ground rules
- Never add features that automate likes, follows, comments or DMs.
- No scraping that breaks a platform's terms; use official exports or connected tools.
- Do not commit anything from a real `studio/` folder.
