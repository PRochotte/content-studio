---
name: studio-setup
description: Onboarding interview that builds the Content Studio profile (who you are, audience, allowed topics, voice, visual identity, channels, tracking tool, rules). Use first, or when the user wants to change their brand, scope, channels or tracking tool. Writes studio/profile.yml which every other studio skill reads.
---

# Studio setup: build the profile

Goal: turn a short conversation into `studio/profile.yml` (schema: `templates/profile.template.yml` in the pack). Keep it light: **ask in small groups, never the whole form at once**, and propose defaults the user can accept with one word.

## Before asking
- If a profile already exists, read it and run in **update mode**: show a 5-line summary, ask what changes, edit only that.
- If the user already gave info (a website, a brief, a previous doc), extract from it first and only ask for what is missing. If they share a URL, read it for tone, colors and wording.
- Ask the user their language and answer in it.

## Interview (4 rounds)
**Round 1, identity and goal.** Name, one-line description, type of project, audience (who, level, where), main goal, how success is measured, content language.

**Round 2, scope (most important).** "What may I talk about, and what never?"
- 1 to 5 `domains`. Push for specific ones: "history facts about my region" beats "culture".
- `excluded` topics. Evergreen vs timely mix.
- Fact policy: default `verified` (2 independent sources). Confirm the `never_invent` list.
- Show the user how the scope will be used: "I will only suggest ideas inside these domains."

**Round 3, voice and visuals.** Tone words, formal/informal address, words to use or avoid, sign-off, emoji level. Colors (hex), fonts, logo, mascot, image style, allowed image sources. If they have no charter, offer to derive a minimal one from their site or three adjectives; mark it `draft`.

**Round 4, channels and tools.** Platforms and handles, formats per platform, cadence and best days, timezone, call to action (one only), video yes/no (explain the optional module needs Python and ffmpeg), where to track content (`local`, Notion, Google Sheets, Airtable) and where stats come from (Metricool, platform exports, manual).

## Writing the profile
1. Fill the template; leave unknown fields empty rather than guessing. List the empty ones at the end.
2. Save to `./studio/profile.yml` (create the folder). Add `studio/` to the user's `.gitignore` if the folder is a git repo and the profile has private info.
3. Run `python scripts/validate_profile.py studio/profile.yml` if the pack scripts are available; fix errors.
4. Create the tracker for the chosen backend by following `adapters/<backend>.md`. For `local`, create `studio/content-log.csv` with the header from `docs/data-contract.md`.
5. Show a summary the user can approve in 10 lines: who, audience, scope, voice, channels, tracker.

## Rules
- Do not collect secrets (passwords, API tokens) in the profile. Tools are connected through the user's own connectors.
- Do not send personal data to outside services while setting up (`rules.private_info_in_prompts: false`).
- If the user wants several brands, create one profile per brand folder (`studio/<brand>/profile.yml`) and ask which is active.
- End by suggesting the next step: usually `studio-ideas`.
