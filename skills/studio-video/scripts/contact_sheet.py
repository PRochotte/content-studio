#!/usr/bin/env python3
"""Make a contact sheet (JPEG) of evenly spaced frames to inspect a video.
Usage: contact_sheet.py video.mp4 sheet.jpg [--frames 8]
"""
import argparse, json, shutil, subprocess, sys

ap = argparse.ArgumentParser()
ap.add_argument("video"); ap.add_argument("out"); ap.add_argument("--frames", type=int, default=8)
a = ap.parse_args()
if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
    sys.exit("error: ffmpeg/ffprobe not found")
d = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                   "-of", "default=nw=1:nk=1", a.video], text=True))
fps = a.frames / d
cols = min(a.frames, 4); rows = -(-a.frames // cols)
subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-i", a.video,
                       "-vf", "fps=%f,scale=270:-1,tile=%dx%d" % (fps, cols, rows),
                       "-frames:v", "1", "-update", "1", a.out])
print("ok: %s (%.1fs video)" % (a.out, d))
