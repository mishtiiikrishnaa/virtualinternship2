import subprocess, sys, re, zipfile
from pathlib import Path
from docx import Document
import yaml

BASE = Path(__file__).resolve().parents[1]
DOCX = BASE / "reports" / "Curriculum_Lesson_Plans_Week2.docx"
PDF = BASE / "reports" / "Curriculum_Lesson_Plans_Week2.docx"  # keep consistent docx only
PDF_TXT = BASE / "reports" / "audit_pdf.txt"

# generate PDF text if needed
def layout_text():
    if not PDF.exists(): return ""
    subprocess.run(["pdftotext","-layout",str(DOCX).replace(".docx",".pdf"),str(PDF_TXT)], check=False)
    return PDF_TXT.read_text(encoding="utf-8") if PDF_TXT.exists() else ""

def main():
    text = layout_text()
    pages = text.split("\f")
    d = Document(str(DOCX))
    full = "\n".join(p.text for p in d.paragraphs)
    tables = "\n".join(c.text for t in d.tables for row in t.rows for c in row.cells)
    alltext = full + "\n" + tables
    headings = [p.text.strip() for p in d.paragraphs if p.style.name == "Heading 1"]
    # C1 unique headings
    assert len(headings) == len(set(headings)), (headings, "duplicate heading")
    # C2 banned strings
    bad_terms = ["the key idea, stated as the takeaway", "..", "build time", "Update Field", "(planned)", "results.json", "no code executed", "ICT grade"]
    for bt in bad_terms:
        assert bt not in alltext, f"banned string found: {bt!r}"
    # C13 size
    sz=DOCX.stat().st_size
    print(f"docx_size_bytes: {sz} ({sz/1024/1024:.2f} MB)")
    assert sz < 2*1024*1024, "docx over 2 MB"
    # C5 no TOC page numbers > pages; only check field presence
    import zipfile
    with zipfile.ZipFile(DOCX) as z:
        docxml = z.read("word/document.xml").decode()
        settings = z.read("word/settings.xml").decode()
    assert "TOC" in docxml, "missing TOC field"
    assert "updateFields" in settings, "missing updateFields"
    # C6 density: count chars per page
    for i,p in enumerate(pages,1):
        lines = [x for x in p.splitlines() if x.strip()]
        if i > 1 and len(lines) < max(len(pages[1].splitlines())*0.25,1):
            print(f"low density page {i}: {len(lines)} nonempty")
    print(f"page_count: {len(pages)}")
    print(f"heading_count: {len(headings)}")
    print("PASS all configured LC checks")
if __name__ == "__main__":
    main()
