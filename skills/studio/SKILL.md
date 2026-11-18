---
name: studio
description: Entry point of the Content Studio pack. Use when the user wants to plan, create, track or improve social media content (reels, carousels, posts, newsletters) and it is unclear which step they need, or when they say "content studio". Checks the profile exists, then routes to setup, ideas, create, video, analytics, planner or engage.
---

# Content Studio: router

Content Studio is a pack of skills that share **one profile file** (`studio/profile.yml`) and **one content log**. This skill only decides where to go next.

## Steps
1. Look for the profile: `./studio/profile.yml`, then `~/.content-studio/profile.yml`.
   - Not found → run **studio-setup** first. Nothing else works without it.
   - Found → read it fully. Treat it as the user's standing rules. Answer in `identity.assistant_language` (or `identity.language`).
2. Read the content log (see `tracking.backend`) to know what exists: ideas, drafts, scheduled, published.
3. Route by intent:

| The user says... | Skill |
|---|---|
| "set up", "who am I", "change my brand/scope/channels" | `studio-setup` |
| "what should I post", "find topics", "ideas" | `studio-ideas` |
| "write", "script", "caption", "make the post/reel/carousel" | `studio-create` |
| "render the video", "assemble the reel" | `studio-video` (only if `formats.video.enabled`) |
| "how did it perform", "stats", "what to improve" | `studio-analytics` |
| "calendar", "schedule", "cadence", "key dates" | `studio-planner` |
| "replies", "comments", "community" | `studio-engage` |

4. If the request spans several steps (e.g. "give me a week of content"), chain them in this order: planner → ideas → create → (video) → log. Stop and ask for approval between ideas and create.

## Where the pack files are
When installed with `scripts/install.sh`, templates, adapters, docs and scripts live in `_content-studio/` next to the skills folders (for example `~/.claude/skills/_content-studio/adapters/notion.md`). In the repo they are at the top level. Paths in the skills (`templates/...`, `adapters/...`, `docs/...`, `scripts/...`) refer to that folder.

## Always true
- The profile wins over your own taste. If a request contradicts it (off-scope topic, banned claim), say so and ask whether to update the profile instead of silently breaking it.
- Never invent statistics, partnerships, testimonials, prices or dates listed in `scope.never_invent`. Ask.
- Nothing is published, scheduled or sent without an explicit human yes (`rules.require_human_approval`).
- Likes, follows and comments are never automated (see `studio-engage`).
- Flag weak points honestly (small sample, thin sources, off-brand idea) instead of reassuring.
