---
name: studio-video
description: Optional module that renders a short vertical video (text over images or color, fades, music, subtitles) from a scene list using Python and ffmpeg, with brand colors and fonts from the profile. Use only when formats.video.enabled is true and the user wants the video file built from a script made by studio-create.
---

# Studio video (optional)

This module is **optional**: it needs `ffmpeg` and Python 3 on the machine. If either is missing, tell the user how to install them or fall back to a script + shot list for their usual editor (CapCut, Canva, Premiere, DaVinci...).

## Input: a scene spec (JSON)
```json
{
  "size": "1080x1920", "fps": 30,
  "font": "path/to/font.ttf", "text_color": "#ffffff", "box_color": "#00000066",
  "music": "path/to/track.mp3", "music_volume": 0.25,
  "scenes": [
    {"background": "path/to/image.jpg", "text": "Hook sentence here", "seconds": 4, "zoom": true},
    {"background_color": "#4b4237", "text": "Answer sentence", "seconds": 5}
  ]
}
```
Optional per spec or per scene: `text_style` (`box` or `shadow`), `position` (`upper`, `center`, `lower`), `font_size`, `zoom` (slow zoom on a background image), `dim` (0 to 1, darkens a photo so text stays readable). Fill `font`, colors and music from the profile (`brand`, `formats.video`). Schema and example: `skills/studio-video/spec.example.json`.

## Steps
1. Build the spec from the approved script. Apply the reading-time rule: `seconds >= 0.3 * words + 1` for each text; the script refuses shorter scenes unless `--allow-fast`.
2. Run: `python skills/studio-video/scripts/render_video.py spec.json out.mp4` (add `--preview` for a 540x960 draft).
3. Make a contact sheet to inspect: `python skills/studio-video/scripts/contact_sheet.py out.mp4 sheet.jpg`. Look at it: text readable, nothing cut off, safe zone respected (keep important text away from the top 10% and bottom 15%, where apps overlay buttons).
4. Check loudness if music is used: `ffmpeg -i out.mp4 -af ebur128 -f null -` (target about -14 LUFS for social).
5. Report to the user: duration, any scene the script lengthened, and what you could not verify visually.

## Rules
- Use only fonts, music and images the user has the right to use. Ask for the licence when unclear. Never download copyrighted tracks.
- Keep it simple: this module does not do effects beyond fade, slow zoom, text box and music. Complex edits go to the user's editor.
- Captions/subtitles come from the scene text; do not add extra text not in the approved script.
