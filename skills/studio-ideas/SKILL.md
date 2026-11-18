---
name: studio-ideas
description: Finds and ranks content topics strictly inside the domains defined in the Content Studio profile, checks facts against sources, avoids repeating published content, and logs approved ideas. Use when the user asks what to post, wants topic ideas, a batch of ideas, or ideas around a date or news.
---

# Studio ideas: find topics that fit

## Inputs
- `studio/profile.yml`: `scope.domains`, `scope.excluded`, `scope.fact_policy`, `identity.audience`, `identity.goal`, channels.
- The content log: everything already published, scheduled or rejected.
- Optional: `studio/learnings.md` (written by `studio-analytics`) for what performs.
- The user's request: how many ideas, which channel, any date or theme.

## Process
1. **Stay in scope.** Generate only inside `scope.domains`. If the user asks for something outside, say so and offer to widen the profile. Drop anything in `scope.excluded`.
2. **Mix idea families** relevant to the domains. Examples: a surprising fact, a myth busted, a "did you know", a how-it-works, a behind-the-scenes, a story, a quiz or poll, a comparison, a before/after, a local angle, a tip, a news or anniversary hook, a product tie-in. Pick families that fit the goal, not all of them.
3. **Research and verify** (web search if available). For every factual idea:
   - find at least 2 independent sources (not copies of each other), prefer primary or institutional ones;
   - note source URL, date and any disagreement between sources;
   - if sources conflict or only one exists, mark the idea `unverified` and say what is missing. Never fill gaps from memory.
4. **Deduplicate.** Compare against the log by topic, not only by title. Same fact with a new angle = allowed if flagged "angle B of #id".
5. **Check visuals and rights.** Note if an image is likely available under an allowed source (`brand.image_sources`) and under what licence. No visual option = lower score.
6. **Score each idea 1 to 5** on: fit with audience, hook strength (can it be said in one sentence that creates a gap?), verifiability, visual availability, effort, and timing. Show the total and the one-line reason.
7. **Present** a table: title, domain, family, hook sentence, sources, risk flags, score. Recommend a top pick and say why. Be honest about weak ideas.
8. **Log.** After approval, write each chosen idea to the content log with status `idea` (or `approved`), including sources and the hook. Rejected ideas are logged `rejected` with the reason so they are not proposed again.

## Rules
- Batch size defaults to 5 to 10. Quality over quantity.
- Dates and anniversaries must be checked, never assumed.
- Sensitive topics (tragedies, religion, politics, health): flag them and propose a careful framing, or skip if excluded.
- No idea may rely on an invented number, quote, partnership or testimonial.
- Ideas about the user's own product or service are allowed only if the profile lists it as a domain, and are capped by the user's mix (default: no more than 1 in 4 is promotional).
