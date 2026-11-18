---
name: studio-create
description: Turns an approved idea into a ready-to-publish content package (hook, script or slides, caption, hashtags, alt text, visual brief, call to action) in the brand's voice, runs a quality checklist, and logs it in the tracker (local file, Notion, Google Sheets or Airtable). Use when the user wants to write or produce a post, reel, carousel, thread or newsletter.
---

# Studio create: from idea to package

## Inputs
Profile (voice, brand, channels, cta, rules), the chosen idea from the log (with sources), the target channel and format. If no idea is given, run `studio-ideas` first.

## Package (one folder or one tracker row per piece)
1. **Hook.** One sentence that creates a gap the rest answers. Short, concrete, no spoiler, no filler opening. Offer 3 variants; recommend one.
2. **Body.** Format-specific:
   - *Short video*: scenes with on-screen text and timing. Reading-time rule: at least 0.3 s per word + 1 s per text block. Total length within `formats.video.target_seconds`. One idea per scene.
   - *Carousel*: slide 1 = hook, then one point per slide, last slide = call to action. Max ~25 words per slide.
   - *Single post / thread / newsletter*: respect `formats.text.max_caption_chars` and platform limits.
3. **Voice.** Apply `voice` strictly (address form, vocabulary do/avoid, emoji level, sign-off). Never invent a persona that the profile does not describe.
4. **Caption + hashtags** per channel (`hashtag_policy`), plus **alt text** for every image.
5. **One call to action** (`cta.primary`). No stacking.
6. **Visual brief.** For each visual: what it shows, source and licence (`brand.image_sources`), credit line, colors and fonts from `brand`. Never use an image whose rights are unclear.
7. **Sources block.** Keep the sources from the idea; add a short line in the caption only if credit is required.
8. **Publication note.** Channel, suggested slot (from the planner), location/tag if relevant.

## Quality checklist (fail = not deliverable; fix or say why)
- [ ] Inside `scope.domains`, nothing in `scope.excluded`.
- [ ] Every fact traces to a source in the package. No invented number, quote, partnership, testimonial, price.
- [ ] Hook readable in under 4 seconds and creates a gap.
- [ ] Voice matches the profile; address form consistent.
- [ ] Exactly one call to action.
- [ ] Alt text present; captions/subtitles for video if `subtitles: true`.
- [ ] Image rights documented.
- [ ] Not a duplicate of something in the log.
- [ ] Platform limits respected (length, hashtags, aspect ratio).
- [ ] AI-use disclosure handled per `rules.disclose_ai_use`.

## Logging
Write the record to the tracker per `adapters/<tracking.backend>.md` with status `draft`, then `to_review`. Fields are defined in `docs/data-contract.md`. When the user approves: `approved` and scheduled date. When they publish: ask for the URL and set `published` (the user publishes; this pack never posts on their behalf unless they explicitly connect a scheduling tool and approve each post).

## Video
If the format is video and `formats.video.enabled` is true, hand the scene list to `studio-video`. If not enabled, deliver the script and shot list only.

## Output to the user
Short: the recommended hook, the package (or the file path), failed checklist items, and what you need from them (approval, an image, a missing fact).
