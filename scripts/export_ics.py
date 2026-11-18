#!/usr/bin/env python3
"""Export planned items of the local content log to an .ics calendar file.
Usage: export_ics.py studio/content-log.csv calendar.ics
Reads rows with a planned_date (ISO 8601, e.g. 2027-01-01T18:00) and status not in published/rejected."""
import csv, sys, datetime as dt

if len(sys.argv) != 3:
    sys.exit(__doc__)
out = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//content-studio//EN"]
n = 0
with open(sys.argv[1], newline="", encoding="utf-8") as fh:
    for r in csv.DictReader(fh):
        if not r.get("planned_date") or r.get("status") in ("published", "rejected"):
            continue
        try:
            d = dt.datetime.fromisoformat(r["planned_date"])
        except ValueError:
            print("skip (bad date): %s" % r.get("id")); continue
        s = d.strftime("%Y%m%dT%H%M%S")
        e = (d + dt.timedelta(minutes=30)).strftime("%Y%m%dT%H%M%S")
        title = (r.get("title") or "").replace("\n", " ")
        out += ["BEGIN:VEVENT", "UID:%s@content-studio" % r.get("id", n),
                "DTSTART:%s" % s, "DTEND:%s" % e,
                "SUMMARY:[%s] %s" % (r.get("channel", ""), title), "END:VEVENT"]
        n += 1
out.append("END:VCALENDAR")
open(sys.argv[2], "w", encoding="utf-8", newline="").write("\r\n".join(out) + "\r\n")
print("ok: %d event(s) -> %s" % (n, sys.argv[2]))
