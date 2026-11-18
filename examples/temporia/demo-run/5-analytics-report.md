# Analytics report, 18 Nov 2026 (`studio-analytics`)

**Source:** Metricool, Instagram reels, 21 Oct to 18 Nov 2026. 34 posts pulled; the 2 published in the last 48 h (17 and 18 Nov) are excluded as too young, leaving **32**. Goal metric from the profile (`awareness`): views and share rate, with watch time as support. Medians, not means.

## Table
| Group | Posts | Median views | Median reach | Median avg watch (s) | Median viewed past 3 s (%) | Posts with ≥1 share |
|---|---|---|---|---|---|---|
| Halloween series (21–31 Oct) | 15 | 166 | 129 | 3.84 | 27.7 | 9 of 15 |
| November (1–16 Nov) | 17 | 159 | 122 | 3.87 | 24.7 | 5 of 17 |
| November, « send it to… » call to action | 10 | 158.5 | 121.5 | 3.94 | 24.9 | 3 of 10 |
| November, « subscribe » call to action | 2 | not computed | | | | |

## Findings (enough data)
1. **Views are flat.** Median 159 to 166 in both periods, range 39 to 319. Topic changes have not moved reach.
2. **Shares are rare and fell.** 20 shares in 32 posts; 9 of 15 Halloween posts got one, 5 of 17 in November. The numbers are small, so a drop of this size is suggestive, not proof.

## Hypotheses (not enough data, do not act on them yet)
- The « send it to… » call to action does not beat the others: 3 of 10 posts with it got a share. Confounded by topic and date.
- Two outliers (25 Oct, 313 views; 7 Nov, 319 views) are about 2x the median on different topics. One is a team story. One post is not a pattern.
- « Subscribe » vs « send »: only 2 posts used « subscribe » in November. **Not enough data**, and the pack refuses to compare below 5.

## What the data cannot tell
Where viewers leave. The skip rate and retention fields (IGRE30, IGRE27) were not pulled, so the first 3 seconds cannot be diagnosed yet. TikTok was not analysed in this run.

## Three changes to test (maximum)
| # | Change | Why | Test | Success threshold | Risk |
|---|---|---|---|---|---|
| 1 | Pull skip rate and retention for all 32 posts | Cannot locate the drop-off | One extra Metricool pull, today | Identify whether most viewers leave before 3 s | None |
| 2 | Alternate « send it to… » and « subscribe » endings, 5 posts each, same time slot | Settle the hypothesis on enough data | 10 posts over 2.5 weeks | Share rate and follows differ by more than the noise seen here (~±1 share per 10 posts) | Mixed topics add noise: keep topics comparable |
| 3 | Publish 5 « people and behind-the-scenes » posts against the next 5 standard ones | One strong outlier is a team story | 10 posts | Median views of the group ≥ 1.3x the other | Novelty effect |

Written to `studio/learnings.md` with status `finding` / `hypothesis`. Re-measure at 7 days.
