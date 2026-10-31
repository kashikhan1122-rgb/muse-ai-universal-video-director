#!/usr/bin/env python3
"""Plan clip batches for a Muse AI Universal Video Director project.

Muse AI generates video in ~10-second clips, max 6 successful generations
per user message. This helper turns a requested duration into an honest
production plan: clip count, batch map, and message count.

Usage:
    python3 plan_clips.py --duration 600 [--clip-seconds 10] [--per-message 6]
    python3 plan_clips.py --duration 60 --ratio 9:16 --title "Red Boy"

Output is a Markdown plan on stdout. Exit code 0 on success, 2 on bad input.
Only the Python standard library is used.
"""

import argparse
import math
import sys

CLIP_SECONDS_DEFAULT = 10
PER_MESSAGE_DEFAULT = 6


def plan(duration_seconds, clip_seconds=CLIP_SECONDS_DEFAULT,
         per_message=PER_MESSAGE_DEFAULT):
    """Return a dict describing the clip plan."""
    if duration_seconds <= 0:
        raise ValueError("duration must be positive")
    if clip_seconds <= 0:
        raise ValueError("clip length must be positive")
    if per_message <= 0:
        raise ValueError("clips per message must be positive")
    clip_count = math.ceil(duration_seconds / clip_seconds)
    batches = []
    for start in range(1, clip_count + 1, per_message):
        end = min(start + per_message - 1, clip_count)
        batches.append((start, end))
    return {
        "duration_seconds": duration_seconds,
        "clip_seconds": clip_seconds,
        "clip_count": clip_count,
        "per_message": per_message,
        "batches": batches,
        "message_count": len(batches),
    }


def render_markdown(result, title=None, ratio=None):
    lines = []
    if title:
        lines.append(f"# Clip plan — {title}")
        lines.append("")
    lines.append(f"- Requested duration: {result['duration_seconds']}s")
    lines.append(f"- Clip length: ~{result['clip_seconds']}s")
    if ratio:
        lines.append(f"- Aspect ratio: {ratio}")
    lines.append(f"- Total clips: {result['clip_count']}")
    lines.append(f"- Clips per user message: {result['per_message']}")
    lines.append(f"- Messages required: {result['message_count']}")
    lines.append("")
    lines.append("| Batch | Clips |")
    lines.append("|---|---|")
    for i, (start, end) in enumerate(result["batches"], 1):
        span = f"{start}–{end}" if start != end else f"{start}"
        lines.append(f"| {i} | {span} |")
    lines.append("")
    if result["message_count"] > 1:
        lines.append(
            "Note: this project spans multiple messages. Each batch is "
            "generated and verified before the next starts. Partial joins "
            "are labelled INCOMPLETE with missing clip numbers; a partial "
            "join is never presented as the complete video."
        )
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--duration", type=float, required=True,
                        help="requested total duration in seconds")
    parser.add_argument("--clip-seconds", type=float,
                        default=CLIP_SECONDS_DEFAULT,
                        help="seconds per clip (default 10)")
    parser.add_argument("--per-message", type=int,
                        default=PER_MESSAGE_DEFAULT,
                        help="max successful generations per user message "
                             "(default 6)")
    parser.add_argument("--title", default=None)
    parser.add_argument("--ratio", default=None)
    args = parser.parse_args(argv)
    try:
        result = plan(args.duration, args.clip_seconds, args.per_message)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(render_markdown(result, title=args.title, ratio=args.ratio))
    return 0


if __name__ == "__main__":
    sys.exit(main())
