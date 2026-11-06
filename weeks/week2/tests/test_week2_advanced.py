import re
from pathlib import Path

from docx import Document

WEEK = Path(__file__).resolve().parents[1]
DOCX = WEEK / "reports" / "Curriculum_Lesson_Plans_Week2.docx"

def test_no_empty_code_boxes():
    d = Document(str(DOCX))
    for t in d.tables:
        if len(t.rows) == 1 and len(t.columns) == 1:
            txt = "".join(c.text for r in t.rows for c in r.cells).strip()
            assert txt, "empty code box table found"

def test_toc_titles_match_headings():
    d = Document(str(DOCX))
    headings = [p.text.strip() for p in d.paragraphs if p.style.name == "Heading 1"]
    for i in range(1, 11):
        expected_head = f"{4 + i} Module {i}: "
        assert any(h.startswith(expected_head) for h in headings), f"missing numbered heading for module {i}"

def test_every_rn_resolves_in_reference_list():
    d = Document(str(DOCX))
    para_text = "\n".join(p.text for p in d.paragraphs)
    table_text = "\n".join(" ".join(c.text for c in r.cells) for t in d.tables for r in t.rows)
    text = para_text + "\n" + table_text
    cites = set(re.findall(r"\bR\d+\b", text))
    refids = set()
    for t in d.tables:
        for row in t.rows:
            first = row.cells[0].text.strip()
            if re.match(r"R\d+$", first):
                refids.add(first)
    missing = sorted(cites - refids)
    extra = sorted(refids - cites)
    assert not missing, ("unresolved citations", missing)
    assert not extra, ("uncited references", extra)

def test_core_properties_author():
    d = Document(str(DOCX))
    p = d.core_properties
    assert p.author and p.author != "python-docx"
    assert p.title and p.subject and p.keywords

def test_figure_uniqueness_and_count():
    d = Document(str(DOCX))
    captions = [p.text.strip() for p in d.paragraphs if p.text.strip().startswith("Figure ")]
    nums = sorted(int(re.search(r"Figure (\d+):", c).group(1)) for c in captions if re.search(r"Figure (\d+):", c))
    assert len(nums) == len(set(nums)), "duplicate figure numbers"
    assert nums == list(range(1, len(nums) + 1)), "figure numbers not consecutive"
    assert len(captions) >= 10, captions
