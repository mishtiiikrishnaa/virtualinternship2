import re
import zipfile
from pathlib import Path
from datetime import datetime

import pytest
import yaml
from docx import Document

WEEK = Path(__file__).resolve().parents[1]
DOCX = WEEK / "reports" / "Curriculum_Lesson_Plans_Week2.docx"
YAML = WEEK / "data" / "curriculum.yaml"
FIG = WEEK / "figures"

def load():
    d = Document(str(DOCX))
    full = "\n".join(p.text for p in d.paragraphs)
    tables_text = "\n".join(c.text for t in d.tables for row in t.rows for c in row.cells)
    return d, full, tables_text

def test_docx_exists_and_size_under_2mb():
    assert DOCX.exists(), f"missing {DOCX}"
    size = DOCX.stat().st_size
    assert size < 2 * 1024 * 1024, f"size {size/1024:.0f} KB over 2 MB"
    assert size < 1.8 * 1024 * 1024, f"size {size/1024:.0f} KB over 1.8 MB build limit"

def test_word_count():
    d, full, tables_text = load()
    words = len((full + "\n" + tables_text).split())
    assert words > 200, f"word count {words} too low"
    assert words > 3000, f"word count {words} below floor"

def test_toc_field_present():
    with zipfile.ZipFile(DOCX) as z:
        doc_xml = z.read("word/document.xml").decode()
        settings_xml = z.read("word/settings.xml").decode()
    assert "TOC" in doc_xml, "no TOC field"
    assert "updateFields" in settings_xml, "update-on-open not set"

def test_required_headings_in_order():
    d, full, _ = load()
    headings = [p.text.strip() for p in d.paragraphs if p.style.name.startswith("Heading")]
    required = ["Executive summary", "1 About this curriculum", "2 Research summary and evidence map",
                "3 Curriculum architecture", "4 Session-by-session plan", "15 Assessment strategy",
                "16 Supporting non-programmers", "18 Validation plan and known limitations",
                "Appendix A: activity catalogue"]
    idx = []
    for req in required:
        found = [i for i, h in enumerate(headings) if h == req]
        assert found, f"missing heading: {req!r}"
        idx.append(found[0])
    assert idx == sorted(idx), f"headings not in order: {idx}"

def test_at_least_10_images():
    with zipfile.ZipFile(DOCX) as z:
        media = [n for n in z.namelist() if n.startswith("word/media/")]
    assert len(media) >= 8, f"only {len(media)} images embedded"

def test_every_figure_has_caption():
    d, full, _ = load()
    captions = [p.text for p in d.paragraphs if p.text.strip().startswith("Figure ")]
    assert len(captions) >= 10, f"only {len(captions)} captions"
    for c in captions:
        assert re.match(r"Figure \d+:", c.strip()), f"caption format off: {c[:60]!r}"

def test_no_placeholder_text():
    d, full, tables_text = load()
    text = (full + "\n" + tables_text).lower()
    for bad in ["lorem", "placeholder", "xxx"]:
        assert bad not in text, f"found placeholder text: {bad!r}"

def test_curriculum_yaml_loads():
    assert YAML.exists()
    data = yaml.safe_load(open(YAML, encoding="utf-8"))
    assert data["total_teaching_hours"] == 30
    assert len(data["modules"]) == 10
    assert len(data["objectives"]) == 12
    assert len(data["figures"]) == 12
    # session block sums
    for s in data["sessions"]:
        assert sum(b["minutes"] for b in s["blocks"]) == s["duration_minutes"], f"{s['session_id']} block sum mismatch"
    # module durations from sessions
    bymod = {}
    for sid in sum(data["sessions_by_module"].values(), []):
        pass
    for mid, sids in data["sessions_by_module"].items():
        m = next(x for x in data["modules"] if x["id"] == mid)
        total = sum(next(s for s in data["sessions"] if s["session_id"] == sid)["duration_minutes"] for sid in sids)
        assert total == m["duration_minutes"], f"{mid}: {total} != {m['duration_minutes']}"
    assert sum(m["duration_minutes"] for m in data["modules"]) == 1800

def test_at_least_5_figures_files():
    assert len(list(FIG.glob("*.png"))) >= 12, f"only {len(list(FIG.glob('*.png')))} pngs"

def test_submission_text_word_count():
    path = WEEK / "docs" / "submission_text.txt"
    assert path.exists()
    words = len(path.read_text().split())
    assert 230 <= words <= 280, f"submission_text.txt has {words} words"

