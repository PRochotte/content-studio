# Architecture

**Shared state, not shared context.** Skills do not call each other directly. They share files and records:

1. `studio/profile.yml`: the only place that knows the brand. Written by `studio-setup`, read by everyone.
2. The content log: one record per idea/piece (`docs/data-contract.md`), stored by an adapter.
3. `studio/metrics.csv` and `studio/learnings.md`: written by `studio-analytics`, read by `studio-ideas`, `studio-create` and `studio-planner`.

**Why skills and not one big prompt:** each skill has a narrow trigger description, so Claude loads only what is needed, and each can be improved or replaced on its own.

**Why a profile file:** the same pack serves any niche; the scope block turns "any content" into "only your domains", which is what makes ideas relevant.

**Safety by construction:** `rules.*` are checked by `scripts/validate_profile.py` (e.g. engagement automation is rejected) and repeated in each skill that could violate them.

**Optional pieces:** `studio-video` needs ffmpeg; trackers other than `local` need a connector; Metricool needs its connector. Every skill degrades gracefully (script instead of video, CSV instead of Notion, pasted numbers instead of Metricool).

**Feedback loop:** analytics → learnings → ideas/create/planner. Learnings carry a status (`finding`, `hypothesis`, `superseded`) so weak evidence is never treated as a rule.
