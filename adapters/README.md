# Adapters

An adapter tells a skill how to **create the tracker**, **read the log**, **write a record** and **update a status** in one tool. Pick yours in `tracking.backend`. All adapters implement the fields of `docs/data-contract.md`.

| Backend | Needs | Good for |
|---|---|---|
| `local` | nothing | getting started, privacy, git history |
| `notion` | Notion connector | team review, calendar and board views |
| `google-sheets` | Google Drive/Sheets connector | simple sharing, formulas |
| `airtable` | Airtable connector | relational views, forms |

Write your own: copy `local.md`, keep the five sections (Create, Read, Write, Update, Limits).
