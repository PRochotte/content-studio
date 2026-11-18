# Content Studio

**A pack of Claude skills that runs a small brand's content workflow: set up once, find topics, create, track, learn from the numbers.**

[Français](README.fr.md) · MIT licence · works with Claude Code and Claude.ai skills

Small brands, creators, museums, schools and side projects publish alone, and the hard part is not one post: it is staying on-topic, accurate, consistent, and learning from what works. Content Studio gives Claude a **profile of who you are** and a set of focused skills that all read it, so the same pack works for a history channel, a bakery, a SaaS or a nonprofit.

## The skills

| Skill | What it does |
|---|---|
| `studio` | Entry point. Checks the profile exists, then routes to the right skill. |
| `studio-setup` | Short interview → `studio/profile.yml`: identity, audience, **allowed topics**, voice, brand, channels, tracker, rules. |
| `studio-ideas` | Finds and ranks topics **only inside your domains**, verifies facts with 2 sources, avoids repeats, logs the ideas. |
| `studio-create` | Turns an idea into hook, script or slides, caption, hashtags, alt text, visual brief; runs a quality checklist; logs it. |
| `studio-video` *(optional)* | Renders a vertical video from the script with Python + ffmpeg (text, fades, music), using your colours and font. |
| `studio-analytics` | Reads stats (Metricool, platform exports, pasted numbers), compares formats fairly, proposes **at most 3 changes** with a test plan. |
| `studio-planner` | Editorial calendar from your cadence and key dates; launch countdowns; `.ics` export. |
| `studio-engage` | Drafts replies and community suggestions **for you to post by hand**. Never automates likes, follows or comments. |

```
            ┌──────────────┐
            │ studio-setup │──► studio/profile.yml ◄───────────────┐
            └──────────────┘          │ read by all                 │
 studio-planner ─► studio-ideas ─► studio-create ─► (studio-video)  │
        ▲                │                 │                        │
        │                ▼                 ▼                        │
        │           content log  (local · Notion · Sheets · Airtable)
        │                                  │ published
        └──── learnings.md ◄── studio-analytics ◄── stats ──────────┘
```

## Design principles

- **One profile, many skills.** Nothing is hard-coded to one brand. Change the profile, change the pack.
- **Scope is a hard rule.** Ideas and content stay inside the domains you list.
- **No invented facts.** Statistics, partnerships, testimonials, prices and dates are on a `never_invent` list: Claude asks instead of guessing. Facts need two independent sources.
- **Human in the loop.** Nothing is published or sent without your yes. No automation of likes, follows or comments (the profile validator rejects it).
- **Honest analytics.** Compare groups of posts, not anecdotes. Say "not enough data" when it is true. Maximum three changes per review.
- **Bring your own tools.** Trackers are adapters (`adapters/`). The video module is optional.

## Install

**Claude Code**
```bash
git clone https://github.com/PRochotte/content-studio.git
cd content-studio
scripts/install.sh            # user-wide (~/.claude/skills)
scripts/install.sh --project  # or only for the current project
```
Then, in your own project folder, say: *"Set up Content Studio."*

**Claude.ai** (skills upload): run `scripts/package_skills.sh` and upload the zips in `dist/` (start with `studio` and `studio-setup`).

**Optional video module:** Python 3.9+ and [ffmpeg](https://ffmpeg.org). Check with `ffmpeg -version`.

## Quick start

1. `Set up Content Studio` → answer four short rounds → profile saved (and validated with `python scripts/validate_profile.py studio/profile.yml`).
2. `Give me 8 ideas for next week` → ranked table with sources and risk flags; approve the ones you like.
3. `Make idea 3 as a reel` → package with hook variants, script, caption, checklist; logged in your tracker.
4. Two weeks later: `How did my last 10 posts do?` → findings, hypotheses, three tests to run.

## Demo

A walkthrough video (setup → ideas → create → video → analytics): **[demo video (English)](https://youtu.be/U0UuWZV3FqM)** · [version française](https://youtu.be/OJ_CTXQ1vuw). It shows a real run, whose files are in [`examples/temporia/demo-run/`](examples/temporia/demo-run/).

## Worked example

`examples/temporia/` is the profile of a real project (a history and heritage quiz app) with video enabled, Notion tracking and Metricool stats. It shows a narrow scope, strict `never_invent` rules and brand-specific voice constraints. It is an example only, not part of the pack.

## Repository layout

```
skills/         the 8 skills (each: SKILL.md, optional scripts)
templates/      profile template, log header, learnings template
adapters/       tracker backends: local, notion, google-sheets, airtable
docs/           data contract, architecture notes
scripts/        install, package, validators, ics export
examples/       worked example(s)
tests/          pytest suite (CI runs it)
```

## Development

```bash
pip install -r requirements-dev.txt
pytest -q
```
The suite validates skill frontmatter, the profile validator, the CSV contract, the video renderer and a privacy check that fails if project-specific names leak outside `examples/`.

## Limits (read before relying on it)

- Skills guide Claude; they do not guarantee output. Always review facts and rights (images, music) yourself.
- Stats analysis is only as good as the data: tiny accounts are noisy, which is why the pack insists on groups and says when it cannot conclude.
- Platform rules and APIs change. Metricool and connector tool names may differ in your setup.
- Video rendering is deliberately basic (text, fade, slow zoom, music). Complex edits belong in your editor.

## Roadmap

Newsletter and blog formats, an `studio-repurpose` skill (one idea → several channels), brand-kit import from a website, more tracker adapters, more example profiles (bakery, museum, SaaS).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New example profiles and adapters are very welcome.

## Licence

[MIT](LICENSE)
