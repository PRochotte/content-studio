# Adapter: Notion

Requires the Notion connector.

## Create
Search first for an existing database named `Content Studio` or `<brand> content`. If none, create a database with the properties below. Names are the contract; types:

- `Title` (title) = `title`
- `Status` (select): idea, approved, draft, to_review, scheduled, published, rejected
- `Channel` (select), `Format` (select), `Domain` (select or text)
- `Hook`, `Body`, `Caption`, `Hashtags`, `Alt text`, `Visual brief`, `Sources`, `Image credits`, `CTA`, `Location tag`, `Notes` (text)
- `Verified` (checkbox)
- `Planned date`, `Published date` (date with time)
- `Post URL` (url)
Save the database URL in `tracking.notion.database_url` of the profile. Suggest two views: a board grouped by `Status`, and a calendar on `Planned date`.

## Read
Query the database; filter on `Status` and search `Title`/`Hook`. Always check the database before claiming something is new: conversation memory is incomplete.

## Write
Create a page per record. Put long content (script, slides) in the page body if properties would exceed limits, with the same section headings each time.

## Update
Update properties by page. If you add a select option, list **all** options to keep, or omitted ones may be removed.

## Limits
Files hosted by Notion expire: keep final visuals in your own storage (Drive, repo, local folder) and store only the link.
Do not write personal data of followers.
