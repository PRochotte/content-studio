# Adapter: Airtable

Requires an Airtable connector (or exports as CSV if none is available: then treat it as `local` and import by hand).

## Create
Table `content` with the fields of `docs/data-contract.md`: single selects for `status`, `channel`, `format`; checkbox for `verified`; date fields for `planned_date` and `published_date`. Table `metrics` linked by `content_id`. Save `base_id` and `table` in the profile.

## Read / Write / Update
Filter by formula on `status` and search on `title`. Update by record id. Never delete records.

## Limits
Respect API rate limits; batch writes.
