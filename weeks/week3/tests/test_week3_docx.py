from pathlib import Path
from docx import Document
WEEK=Path(__file__).resolve().parents[1]
DOCX=WEEK/"reports"/"Interactive_Module_Week3.docx"
def test_exists(): assert DOCX.exists()
def test_word_count():
    d=Document(str(DOCX)); full="\n".join(p.text for p in d.paragraphs); tables="\n".join(c.text for t in d.tables for r in t.rows for c in r.cells)
    assert len((full+"\n"+tables).split())>1000
def test_images():
    import zipfile; z=zipfile.ZipFile(DOCX); assert len([n for n in z.namelist() if n.startswith("word/media/")])>=8
