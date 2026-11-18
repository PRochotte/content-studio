---
name: studio-planner
description: Builds and maintains the editorial calendar from the profile cadence, key dates and the content log, balancing formats, domains and promotional share, and proposes publishing slots. Use when the user asks for a plan, a week or month of content, a posting schedule, or how to prepare a launch or a seasonal period.
---

# Studio planner: calendar and cadence

## Inputs
Profile channels (cadence, days, times, timezone), `scope.domains`, `cta`, the log (what is published, approved, drafted), key dates from the user, and `studio/learnings.md` if present. If the user gives a goal date (launch, event), plan backwards from it.

## Process
1. **Time frame**: ask week, month or custom; default 2 weeks.
2. **Key dates**: ask for launches, events, holidays, seasons relevant to the domains. Verify public dates/anniversaries by search. Never invent.
3. **Slots**: place posts on `preferred_days` and `preferred_times` per channel in the profile timezone. If analytics are connected, check best-time data, but treat it as a suggestion.
4. **Balance** across the period: formats (video vs carousel vs text), domains (no domain over ~50%), promotional share (default max 1 in 4), difficulty/effort (not three heavy videos on consecutive days).
5. **Assign**: for each slot a status: existing approved content, an idea from the log, or `needs idea` (hand over to `studio-ideas`).
6. **Launch mode** (countdown): a short arc (tease → proof → how it works → last call → launch day). Do not invent proof; use only what the user has.
7. **Output** a calendar table (date, time, channel, format, topic or idea id, status, owner) and a short list of what is missing. Write it to the tracker (`planned_date` field) and optionally an `.ics` file via `python scripts/export_ics.py` if available.

## Rules
- Dates are written with timezone; handle daylight-saving changes explicitly.
- A plan is a proposal: the user can drop or move any item. Reschedule rather than delete when a slot is missed.
- Keep it sustainable: if the cadence is more than the user can produce (ask about weekly hours available), recommend a lower one and say why.
