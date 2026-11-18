# Adapter: local CSV

## Create
Create `studio/content-log.csv` with the header from `docs/data-contract.md`. Create `studio/metrics.csv`, `studio/learnings.md` (empty with a title).

## Read
Open the CSV. Search by `title`, `domain` and `hook` to deduplicate; compare topics, not only titles.

## Write
Append a row. Quote fields that contain commas or newlines (RFC 4180). Generate `id` as `YYYY-MM-NNNN` (next free number for the month).

## Update
Rewrite the row with the same `id`. Never delete rows: set `status: rejected` and explain in `notes`.

## Limits
Single user, no views or reminders. Commit the file to git if you want history (the profile may contain private info: keep `studio/` in a private repo).
