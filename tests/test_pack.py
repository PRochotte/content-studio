import json, os, subprocess, sys, shutil, tempfile, pathlib
import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent


def run(*args, cwd=ROOT):
    return subprocess.run([sys.executable, *map(str, args)], cwd=cwd, capture_output=True, text=True)


def test_skills_valid():
    r = run("scripts/validate_skills.py")
    assert r.returncode == 0, r.stdout + r.stderr


def test_no_leaks():
    r = run("scripts/privacy_check.py")
    assert r.returncode == 0, r.stdout


def test_template_profile_reports_missing_fields():
    r = run("scripts/validate_profile.py", "templates/profile.template.yml")
    assert r.returncode == 1 and "scope.domains" in r.stdout


def test_example_profile_valid():
    r = run("scripts/validate_profile.py", "examples/temporia/profile.yml")
    assert r.returncode == 0, r.stdout


def test_automation_flag_rejected(tmp_path):
    import yaml
    p = yaml.safe_load((ROOT / "examples/temporia/profile.yml").read_text(encoding="utf-8"))
    p["rules"]["automate_engagement"] = True
    f = tmp_path / "p.yml"; f.write_text(yaml.safe_dump(p), encoding="utf-8")
    r = run("scripts/validate_profile.py", f)
    assert r.returncode == 1 and "automate_engagement" in r.stdout


def test_csv_header_matches_contract():
    header = (ROOT / "templates/content-log.header.csv").read_text().strip()
    assert header in (ROOT / "docs/data-contract.md").read_text()


@pytest.mark.skipif(not shutil.which("ffmpeg"), reason="ffmpeg not installed")
def test_render_video(tmp_path):
    out = tmp_path / "o.mp4"
    r = run("skills/studio-video/scripts/render_video.py", "skills/studio-video/spec.example.json", out, "--preview")
    assert r.returncode == 0, r.stderr
    assert out.stat().st_size > 1000


@pytest.mark.skipif(not shutil.which("ffmpeg"), reason="ffmpeg not installed")
def test_reading_time_rule(tmp_path):
    spec = {"scenes": [{"background_color": "#000000", "text": "one two three four five six seven", "seconds": 1}]}
    f = tmp_path / "s.json"; f.write_text(json.dumps(spec))
    r = run("skills/studio-video/scripts/render_video.py", f, tmp_path / "o.mp4", "--preview")
    assert "lengthened" in r.stdout
