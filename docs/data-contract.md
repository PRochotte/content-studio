# Data contract

All skills talk to the same two data shapes. Adapters (`adapters/`) map them to Notion, Google Sheets, Airtable or a local CSV. If you add a backend, keep these field names.

## Content record

| Field | Type | Notes |
|---|---|---|
| `id` | text | stable id, e.g. `2027-01-0001` or the tracker's row id |
| `title` | text | the subject, in plain words |
| `status` | select | `idea`, `approved`, `draft`, `to_review`, `scheduled`, `published`, `rejected` |
| `channel` | select | instagram, tiktok, youtube, linkedin, x, threads, blog, newsletter |
| `format` | select | reel, short, carousel, post, thread, article, newsletter |
| `domain` | text | one of `scope.domains` |
| `hook` | text | the opening sentence |
| `body` | text | script, slide texts or article text |
| `caption` | text | final caption |
| `hashtags` | text | |
| `alt_text` | text | |
| `visual_brief` | text | what the visuals are, with source and licence |
| `sources` | text | URLs, one per line, with date accessed |
| `image_credits` | text | author, licence, link |
| `verified` | checkbox | true only when the fact policy is met |
| `cta` | text | the single call to action |
| `planned_date` | datetime | ISO 8601 with timezone |
| `published_date` | datetime | |
| `post_url` | url | filled by the human at publication |
| `location_tag` | text | optional |
| `notes` | text | rejection reason, angle B of #id, etc. |

CSV header (local backend), in this order:

```
id,title,status,channel,format,domain,hook,body,caption,hashtags,alt_text,visual_brief,sources,image_credits,verified,cta,planned_date,published_date,post_url,location_tag,notes
```

## Metrics snapshot (written by `studio-analytics`)

One row per published piece and measurement date.

| Field | Notes |
|---|---|
| `content_id` | joins to the content record |
| `measured_on` | date; also write the age of the post in days |
| `views`, `reach` | whatever the platform provides |
| `avg_watch_seconds`, `watch_through_rate` | video only |
| `likes`, `comments`, `shares`, `saves`, `follows` | |
| `link_clicks` | |

Keep these in `studio/metrics.csv` (any backend can mirror them). Findings go in `studio/learnings.md`: dated, with the evidence and the status `finding`, `hypothesis` or `superseded`.

## Files in the user's project

```
studio/
  profile.yml        # created by studio-setup
  content-log.csv    # local backend only
  metrics.csv        # snapshots
  learnings.md       # findings and tests
  faq.md             # recurring questions (studio-engage)
```
