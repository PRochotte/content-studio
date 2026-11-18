---
name: studio-analytics
description: Reads performance data of published videos and posts (Instagram, TikTok, YouTube, LinkedIn... via Metricool, platform exports or pasted numbers), compares formats and hooks fairly, and proposes at most three concrete improvements with a test plan. Use when the user asks how content performed, what works, or what to change.
---

# Studio analytics: read the numbers, propose changes

## Data sources (use `analytics.source`)
1. **Metricool** (if its tools are connected): list the metrics available first, then pull per-post data for the period. Never guess metric ids.
2. **Platform export** (CSV/XLSX from Instagram, TikTok Studio, YouTube Studio, LinkedIn): ask the user to drop the file, read it, map columns.
3. **Manual**: ask the user to paste views, reach, watch time, likes, comments, shares, saves, follows for each post.
Join the numbers with the content log (format, hook type, topic, duration, post time) by URL or date. A post without a log entry is analysed but flagged "untracked".

## Method (be strict; small accounts are noisy)
1. **Define the goal metric** from the profile (`identity.goal`): awareness → reach/views and follows; community → shares, saves, comments; traffic → link clicks; education → completion and saves. Do not optimise raw views if the goal is something else.
2. **Normalise.** Compare rates (watch-through, share per reach, follows per reach), not only counts. Note the account size and reach-to-follower ratio.
3. **Group, never anecdote.** Compare groups of at least `analytics.min_posts_per_comparison` posts (default 5). With fewer, say "not enough data" and describe it as a hypothesis, not a finding.
4. **One variable at a time.** Compare formats, hook types, topics, length, slot, thumbnail separately; warn when two changed together.
5. **Check retention** if the platform gives it: where do viewers drop (first 3 seconds? mid?) and what the first frame/sentence was.
6. **Spot outliers** and say whether they are explained (a share by a large account, a trend) or not. Exclude explained outliers from averages and show both.
7. **Wait for maturity.** Do not judge posts younger than 48 hours; re-measure at 7 days.

## Output
1. A table: group, number of posts, goal metric (median, not only mean), best and worst post.
2. **Findings** (supported by enough data) vs **hypotheses** (not enough). Label each.
3. **At most 3 changes**, each as: *change / why (evidence) / how to test (what to publish, how many posts, over how long) / success threshold / risk*. Prefer cheap tests.
4. What the data cannot tell (e.g. the platform hides a metric).
5. Update `studio/learnings.md` with dated findings and the tests started, so `studio-ideas` and `studio-create` can use them. Mark old learnings superseded instead of deleting.

## Rules
- Never invent a number, a benchmark or an algorithm claim. If you quote a platform rule or benchmark, cite where it comes from or say it is an assumption.
- Do not blame or flatter; report plainly, including "nothing moved".
- Do not store follower or viewer personal data. Work on aggregates.
- Do not log in to a user's accounts with their password; use connected tools or exports.
