#!/usr/bin/env python3
"""Active-time helper for the hours skill.

Reads Claude Code session transcripts (~/.claude/projects/**/*.jsonl) and
reports when you were working in one project, per local day, as spans with
idle gaps removed. Every transcript line carries a UTC timestamp and most
carry the session's working directory (cwd), which is how a session is tied
to a project.

usage:
  python3 active_time.py --project acme-site
  python3 active_time.py --project acme-site --from 2026-10-01 --to 2026-10-08
  python3 active_time.py --project acme-site --after "2026-10-08 20:30"
  options: --idle MINUTES (default 20)  --round MINUTES (default 15)
           --projects-dir DIR (default ~/.claude/projects)

It only sees time spent in Claude sessions. Calls, reading and thinking
away from the keyboard don't show up; add those by hand.
"""
import argparse
import json
import math
from datetime import date, datetime, timedelta
from pathlib import Path


def norm(path):
    return path.replace("\\", "/").lower()


def parse_ts(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone()


def session_stamps(path, fragment):
    """All timestamps in one transcript, or [] if it isn't this project's."""
    stamps, matched = [], False
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            if not isinstance(rec, dict):
                continue
            cwd = rec.get("cwd")
            # Match whole folder names, so "acme-site" doesn't also catch "acme-site-old".
            if isinstance(cwd, str) and f"/{fragment}/" in f"/{norm(cwd).strip('/')}/":
                matched = True
            ts = rec.get("timestamp")
            if isinstance(ts, str):
                try:
                    stamps.append(parse_ts(ts))
                except ValueError:
                    pass
    return stamps if matched else []


def spans(stamps, idle):
    """Merge sorted timestamps into (start, end) spans, splitting on idle gaps."""
    out = []
    for ts in sorted(stamps):
        if out and ts - out[-1][1] <= idle:
            out[-1][1] = ts
        else:
            out.append([ts, ts])
    return out


def fmt_minutes(minutes):
    return f"{int(minutes // 60)}h{int(minutes % 60):02d}m"


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--project", required=True, help="the project folder's name, e.g. acme-site")
    p.add_argument("--from", dest="start", help="first local date, YYYY-MM-DD (default today)")
    p.add_argument("--to", dest="end", help="last local date, YYYY-MM-DD (default today)")
    p.add_argument("--after", help='only activity after this local time, "YYYY-MM-DD HH:MM" '
                                   "(the end of the last logged row); implies --from that date")
    p.add_argument("--idle", type=int, default=20, help="minutes of silence that end a span")
    p.add_argument("--round", type=int, default=15, help="round each day's total to this many minutes")
    p.add_argument("--projects-dir", default=str(Path.home() / ".claude" / "projects"))
    args = p.parse_args()

    after = datetime.fromisoformat(args.after).astimezone() if args.after else None
    if args.start:
        first = date.fromisoformat(args.start)
    else:
        first = after.date() if after else date.today()
    last = date.fromisoformat(args.end) if args.end else date.today()
    fragment = norm(args.project).strip("/")
    window_start = datetime.combine(first, datetime.min.time()).astimezone()

    stamps = []
    for path in Path(args.projects_dir).rglob("*.jsonl"):
        try:
            # A transcript last written before the window can't hold anything in it.
            if datetime.fromtimestamp(path.stat().st_mtime).astimezone() < window_start:
                continue
            found = session_stamps(path, fragment)
        except OSError:
            continue  # unreadable, e.g. a Windows path over 260 characters
        stamps.extend(s for s in found if first <= s.date() <= last and (not after or s > after))

    if not stamps:
        since = f"after {after:%Y-%m-%d %H:%M}" if after else f"from {first}"
        print(f"No Claude session activity for '{args.project}' {since} through {last}.")
        return

    by_day = {}
    for start, end in spans(stamps, timedelta(minutes=args.idle)):
        by_day.setdefault(start.date(), []).append((start, end))

    for day in sorted(by_day):
        print(day.strftime("%a %Y-%m-%d"))
        total = 0.0
        for start, end in by_day[day]:
            minutes = (end - start).total_seconds() / 60
            total += minutes
            print(f"  {start:%H:%M}-{end:%H:%M}  {fmt_minutes(minutes)}")
        rounded = math.floor(total / args.round + 0.5) * args.round  # half rounds up
        print(f"  active {fmt_minutes(total)} -> proposed {rounded / 60:.2f} h "
              f"(nearest {args.round} min, gaps over {args.idle} min dropped)")


if __name__ == "__main__":
    main()
