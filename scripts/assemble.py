#!/usr/bin/env python3
"""Assemble verified clips into one video and verify the result.

Joins clips in story order with ffmpeg (concat demuxer, re-encode for a
consistent output), then verifies the joined file with ffprobe: duration,
resolution, frame rate, and audio presence. Writes a short QC note as JSON.

Usage:
    python3 assemble.py --out final.mp4 --qc-note qc.json clip-01.mp4 clip-02.mp4 ...
    python3 assemble.py --out final.mp4 --expected-duration 60 --expected-ratio 9:16 clip-*.mp4

Exit code 0 when the join verifies (duration within 1.0s of expected when
given, ratio matches when given, audio present). Exit code 1 otherwise.
Requires ffmpeg and ffprobe on PATH. Standard library only.
"""

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

RATIO_MAP = {
    "9:16": (9, 16),
    "16:9": (16, 9),
    "1:1": (1, 1),
}


def probe(path):
    """Return (width, height, duration, fps, has_audio) for a video file."""
    cmd = [
        "ffprobe", "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=width,height,duration,r_frame_rate",
        "-show_entries", "format=duration",
        "-of", "json", str(path),
    ]
    out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    data = json.loads(out)
    stream = data["streams"][0]
    num, den = stream["r_frame_rate"].split("/")
    fps = float(num) / float(den) if float(den) else 0.0
    duration = float(data["format"]["duration"])
    audio = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a:0",
         "-show_entries", "stream=index", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    return {
        "width": int(stream["width"]),
        "height": int(stream["height"]),
        "duration": duration,
        "fps": round(fps, 2),
        "has_audio": bool(audio),
    }


def ratio_of(width, height):
    """Return the closest named ratio (9:16, 16:9, 1:1) or 'other'."""
    actual = width / height
    for name, (w, h) in RATIO_MAP.items():
        if abs(actual - w / h) < 0.02:
            return name
    return "other"


def assemble(clips, out_path):
    """Join clips with ffmpeg; return the ffmpeg CompletedProcess."""
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
        for clip in clips:
            # Absolute paths: ffmpeg resolves concat-list entries relative
            # to the list file's directory, not the working directory.
            abs_path = str(Path(clip).resolve())
            safe = abs_path.replace("'", "'\\''")
            f.write(f"file '{safe}'\n")
        list_path = f.name
    cmd = [
        "ffmpeg", "-y", "-v", "error",
        "-f", "concat", "-safe", "0", "-i", list_path,
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
        "-c:a", "aac", str(out_path),
    ]
    return subprocess.run(cmd, capture_output=True, text=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, help="output video path")
    parser.add_argument("--qc-note", default=None,
                        help="write QC note JSON to this path")
    parser.add_argument("--expected-duration", type=float, default=None)
    parser.add_argument("--expected-ratio", default=None,
                        choices=list(RATIO_MAP))
    parser.add_argument("clips", nargs="+", help="clip files in story order")
    args = parser.parse_args(argv)

    clip_paths = [Path(c) for c in args.clips]
    missing = [str(c) for c in clip_paths if not c.exists()]
    if missing:
        print(f"error: missing clips: {', '.join(missing)}", file=sys.stderr)
        return 1

    print(f"joining {len(clip_paths)} clips -> {args.out}")
    proc = assemble(clip_paths, args.out)
    if proc.returncode != 0:
        print(f"error: ffmpeg failed:\n{proc.stderr}", file=sys.stderr)
        return 1

    info = probe(args.out)
    info["ratio"] = ratio_of(info["width"], info["height"])
    info["clip_count"] = len(clip_paths)
    problems = []
    if args.expected_duration is not None:
        if abs(info["duration"] - args.expected_duration) > 1.0:
            problems.append(
                f"duration {info['duration']:.2f}s != expected "
                f"{args.expected_duration}s")
    if args.expected_ratio is not None and info["ratio"] != args.expected_ratio:
        problems.append(
            f"ratio {info['ratio']} != expected {args.expected_ratio}")
    if not info["has_audio"]:
        problems.append("no audio stream in output")
    info["problems"] = problems
    info["verdict"] = "PASS" if not problems else "FAIL"

    print(f"output: {info['width']}x{info['height']} ({info['ratio']}), "
          f"{info['duration']:.2f}s, {info['fps']}fps, "
          f"audio={'yes' if info['has_audio'] else 'no'}")
    if args.qc_note:
        Path(args.qc_note).write_text(json.dumps(info, indent=2))
        print(f"QC note written to {args.qc_note}")
    if problems:
        print("FAIL: " + "; ".join(problems), file=sys.stderr)
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
