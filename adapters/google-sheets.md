# Adapter: Google Sheets

Requires the Google Drive connector.

## Create
Create a spreadsheet `Content Studio` with sheet `content` (header row = the CSV header in `docs/data-contract.md`) and sheet `metrics`. Freeze the header row; add data validation for `status`, `channel`, `format`. Save the URL in `tracking.google_sheets.spreadsheet_url`.

## Read / Write / Update
Read the whole `content` sheet before deduplicating. Append rows; update by matching `id`. Never delete rows (use `rejected`).

## Limits
Long scripts in one cell are hard to read: keep `body` short and link to a document for long form.
