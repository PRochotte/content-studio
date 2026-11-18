#!/usr/bin/env python3
"""Render a short vertical video from a JSON scene spec using ffmpeg only.

Usage: render_video.py spec.json out.mp4 [--preview] [--allow-fast]
No third-party Python package needed.
"""
import argparse, json, math, os, shutil, subprocess, sys, tempfile, textwrap

FALLBACK_FONTS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
]


def die(msg):
    print("error: " + msg, file=sys.stderr)
    sys.exit(1)


def ff_color(c, default="white"):
    """'#rrggbb' or '#rrggbbaa' -> ffmpeg 0xRRGGBB[@alpha]"""
    if not c:
        return default
    c = c.lstrip("#")
    if len(c) == 8:
        return "0x%s@%.2f" % (c[:6], int(c[6:], 16) / 255)
    return "0x" + c[:6]


def esc_path(p):
    # escape for use inside an ffmpeg filter option value
    return p.replace("\\", "/").replace(":", "\\:").replace("'", "\\'")


def reading_min(text):
    return 0.3 * len(text.split()) + 1.0


def pick_font(spec):
    f = spec.get("font", "")
    if f and os.path.isfile(f):
        return f
    for cand in FALLBACK_FONTS:
        if os.path.isfile(cand):
            if f:
                print("warning: font not found (%s), using %s" % (f, cand))
            return cand
    die("no usable font; set 'font' to a .ttf/.otf file")


def run(cmd):
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if r.returncode != 0:
        die("ffmpeg failed:\n" + r.stderr[-1500:])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("out")
    ap.add_argument("--preview", action="store_true", help="half-size draft")
    ap.add_argument("--allow-fast", action="store_true", help="allow scenes shorter than the reading-time rule")
    a = ap.parse_args()

    if not shutil.which("ffmpeg"):
        die("ffmpeg not found. Install it (https://ffmpeg.org) or use the script + shot list instead.")
    with open(a.spec, encoding="utf-8") as fh:
        spec = json.load(fh)

    w, h = (int(x) for x in spec.get("size", "1080x1920").split("x"))
    fps = int(spec.get("fps", 30))
    if a.preview:
        w, h = w // 2, h // 2
    font = pick_font(spec)
    text_color = ff_color(spec.get("text_color", "#ffffff"))
    box_color = ff_color(spec.get("box_color", "#00000088"))
    scenes = spec.get("scenes") or die("spec has no scenes")
    base = os.path.dirname(os.path.abspath(a.spec))

    def rel(p):
        return p if os.path.isabs(p) else os.path.join(base, p)

    tmp = tempfile.mkdtemp(prefix="studio-video-")
    clips = []
    total = 0.0
    try:
        for i, sc in enumerate(scenes, 1):
            text = sc.get("text", "")
            secs = float(sc.get("seconds", 4))
            need = reading_min(text) if text else 0
            if secs + 1e-6 < need:
                if a.allow_fast:
                    print("warning: scene %d is shorter than the reading-time rule (%.1fs < %.1fs)" % (i, secs, need))
                else:
                    print("note: scene %d lengthened %.1fs -> %.1fs (reading-time rule)" % (i, secs, need))
                    secs = math.ceil(need * 10) / 10
            total += secs
            frames = int(round(secs * fps))
            clip = os.path.join(tmp, "s%02d.mp4" % i)
            bg = sc.get("background")
            if bg:
                bg = rel(bg)
                if not os.path.isfile(bg):
                    die("scene %d: background not found: %s" % (i, bg))
                src = ["-loop", "1", "-framerate", str(fps), "-t", "%.2f" % secs, "-i", bg]
                if sc.get("zoom", False):
                    zp = ("scale=%d:%d:force_original_aspect_ratio=increase,crop=%d:%d,"
                          "zoompan=z='min(zoom+0.0006,1.12)':d=%d:s=%dx%d:fps=%d") % (
                        w * 4, h * 4, w * 4, h * 4, frames, w, h, fps)
                else:
                    zp = "scale=%d:%d:force_original_aspect_ratio=increase,crop=%d:%d" % (w, h, w, h)
                vf = [zp]
            else:
                col = ff_color(sc.get("background_color", spec.get("background_color", "#222222")))
                src = ["-f", "lavfi", "-i", "color=c=%s:s=%dx%d:r=%d:d=%.2f" % (col, w, h, fps, secs)]
                vf = []
            if sc.get("dim"):
                k = 1.0 - float(sc["dim"])
                vf.append("colorchannelmixer=rr=%.2f:gg=%.2f:bb=%.2f" % (k, k, k))
            if text:
                size = int(sc.get("font_size", 84 * h / 1920))
                width_chars = max(10, int(w * 0.8 / (size * 0.58)))
                wrapped = "\n".join(textwrap.wrap(text, width_chars, break_on_hyphens=False))
                tf = os.path.join(tmp, "t%02d.txt" % i)
                with open(tf, "w", encoding="utf-8") as fh:
                    fh.write(wrapped)
                style = sc.get("text_style", spec.get("text_style", "box"))
                ypos = {"center": "(h-text_h)/2", "upper": "h*0.27-text_h/2", "lower": "h*0.66-text_h/2"}[sc.get("position", "center")]
                common = ("drawtext=fontfile='%s':textfile='%s':fontsize=%d:fontcolor=%s:line_spacing=%d:text_align=center:x=(w-text_w)/2:y=%s"
                          % (esc_path(font), esc_path(tf), size, text_color, int(size * 0.25), ypos))
                if style == "shadow":
                    extra = ":shadowcolor=black@0.55:shadowx=4:shadowy=4:borderw=2:bordercolor=black@0.25"
                else:
                    extra = ":box=1:boxcolor=%s:boxborderw=%d" % (box_color, int(size * 0.4))
                vf.append(common + extra)
            fade = min(0.4, secs / 4)
            vf.append("fade=t=in:st=0:d=%.2f,fade=t=out:st=%.2f:d=%.2f" % (fade, secs - fade, fade))
            vf.append("format=yuv420p")
            run(["ffmpeg", "-y", "-loglevel", "error"] + src +
                ["-vf", ",".join(vf), "-r", str(fps), "-t", "%.2f" % secs,
                 "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-an", clip])
            clips.append(clip)

        lst = os.path.join(tmp, "list.txt")
        with open(lst, "w") as fh:
            for c in clips:
                fh.write("file '%s'\n" % c.replace("'", "'\\''"))
        silent = os.path.join(tmp, "all.mp4")
        run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", silent])

        music = spec.get("music")
        if music and os.path.isfile(rel(music)):
            vol = float(spec.get("music_volume", 0.25))
            fo = min(2.0, total / 3)
            run(["ffmpeg", "-y", "-loglevel", "error", "-i", silent, "-stream_loop", "-1", "-i", rel(music),
                 "-filter_complex", "[1:a]volume=%.2f,afade=t=out:st=%.2f:d=%.2f[a]" % (vol, total - fo, fo),
                 "-map", "0:v", "-map", "[a]", "-t", "%.2f" % total, "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", a.out])
        else:
            if music:
                print("warning: music file not found, rendering without sound")
            shutil.copy(silent, a.out)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("ok: %s (%.1fs, %dx%d)" % (a.out, total, w, h))


if __name__ == "__main__":
    main()
