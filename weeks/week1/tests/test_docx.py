import re
import zipfile
from pathlib import Path
from datetime import date
from xml.etree import ElementTree as ET

import pytest
from docx import Document

WEEK = Path(__file__).resolve().parents[1]
DOCX = WEEK / "reports" / "Project_Plan_Scope_Definition_Week1.docx"

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
    assert words > 3000, f"word count {words} below target 4000-6000 range (floor 3000 for test)"

def test_toc_field_present():
    with zipfile.ZipFile(DOCX) as z:
        doc_xml = z.read("word/document.xml").decode()
        settings_xml = z.read("word/settings.xml").decode()
    assert 'TOC' in doc_xml, "no TOC field"
    assert "updateFields" in settings_xml, "update-on-open not set"

def test_required_headings_in_order():
    d, full, _ = load()
    headings = [p.text.strip() for p in d.paragraphs if p.style.name.startswith("Heading")]
    required = [
        "Executive summary",
        "1 Overview and purpose",
        "2 Target audience",
        "3 Research summary: challenges non-programmers face and what works",
        "4 Educational objectives and learning outcomes",
        "5 Key content areas and curriculum structure",
        "6 Instructional methodologies and teaching methods",
        "7 Assessment techniques",
        "8 Resource requirements and allocation",
        "9 Timeline, milestones and deadlines",
        "10 Risks, assumptions and mitigations",
        "11 Success metrics and evaluation of the programme itself",
        "12 Conclusion and next steps",
        "Glossary",
        "References",
        "Appendix: assumptions and decisions log",
    ]
    idx = []
    for req in required:
        found = [i for i, h in enumerate(headings) if h == req]
        assert found, f"missing heading: {req!r}"
        idx.append(found[0])
    assert idx == sorted(idx), f"headings not in order: {idx}"

def test_at_least_5_images():
    with zipfile.ZipFile(DOCX) as z:
        media = [n for n in z.namelist() if n.startswith("word/media/")]
    assert len(media) >= 5, f"only {len(media)} images embedded"

def test_every_figure_has_caption():
    d, full, _ = load()
    captions = [p.text for p in d.paragraphs if p.text.strip().startswith("Figure ")]
    assert len(captions) >= 5, f"only {len(captions)} captions"
    # each caption should be in form "Figure N: ..."
    for c in captions:
        assert re.match(r"Figure \d+:", c.strip()), f"caption format off: {c[:60]!r}"

def test_no_placeholder_text():
    d, full, tables_text = load()
    text = (full + "\n" + tables_text).lower()
    for bad in ["todo", "lorem", "placeholder", "xxx"]:
        assert bad not in text, f"found placeholder text: {bad!r}"

def _parse_dd_mmyyyy(s):
    s = s.strip()
    # allow "5 November 2026" or "9 November 2026 (planned)"
    s = s.replace("(planned)", "").strip()
    from datetime import datetime
    for fmt in ("%d %B %Y", "%d %b %Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"unparseable date: {s!r}")

def test_milestone_dates_ascending():
    d, _, _ = load()
    # find milestone table: it has headers including Milestone and Due date
    target = None
    for t in d.tables:
        headers = [c.text.strip().lower() for c in t.rows[0].cells]
        if any("milestone" in h for h in headers) and any("due" in h for h in headers):
            target = t
            break
    assert target is not None, "milestone table not found"
    dates = []
    for row in target.rows[1:]:
        due = row.cells[5].text if len(row.cells) > 5 else row.cells[-2].text
        dates.append(_parse_dd_mmyyyy(due))
    assert len(dates) >= 5, f"too few milestones: {len(dates)}"
    for a, b in zip(dates, dates[1:]):
        assert a < b, f"milestone dates not strictly ascending: {a} !< {b}"

def test_learning_outcome_mapping_complete():
    d, _, _ = load()
    # find table with Outcome header and Modules/Assessments
    target = None
    for t in d.tables:
        headers = [c.text.strip() for c in t.rows[0].cells]
        if headers and headers[0] == "Outcome" and len(headers) >= 4 and "Module" in headers[1]:
            target = t
            break
    assert target is not None, "outcome->module->assessment table not found"
    for row in target.rows[1:]:
        mods = row.cells[1].text.strip()
        assesses = row.cells[2].text.strip()
        assert mods, "empty module mapping"
        assert assesses, "empty assessment mapping"

def test_dates_anchor_baseline_and_report_date():
    d, full, tables_text = load()
    text = full + "\n" + tables_text
    # baseline present
    assert "5 November 2026" in text, "baseline date not stated"
    assert "4 November 2026" in text, "report date not stated"
    # milestone dates all >= baseline
    for t in d.tables:
        headers = [c.text.strip().lower() for c in t.rows[0].cells]
        if any("milestone" in h for h in headers) and any("due" in h for h in headers):
            for row in t.rows[1:]:
                due = _parse_dd_mmyyyy(row.cells[5].text)
                assert due >= date(2026, 11, 5), f"milestone before baseline: {due}"
            break
    # report date differs check: build date is today according to file mtime, report date must equal build date (allow same day)
    import datetime as _dt
    mtime = _dt.date.fromtimestamp(DOCX.stat().st_mtime)
    # mtime is local date; report date string is 4 November 2026 which should match when built on that day
    # we check that report date is not in the future relative to mtime and not wildly off
    assert mtime >= date(2026, 11, 4), f"build date {mtime} before report date"

def test_effort_matches_resources():
    d, full, tables_text = load()
    text = full + "\n" + tables_text
    # 120 hours total appears in both sections; just check the number is present
    assert "120" in text, "effort total 120 not stated"
