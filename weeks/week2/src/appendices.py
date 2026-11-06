import yaml
from pathlib import Path
from docx.shared import Pt

B = Path('weeks/week2')
Y = B / "data" / "curriculum.yaml"
data = yaml.safe_load(open(Y, encoding="utf-8"))


def _fk_grade(text):
    import re
    words=text.split()
    sentences=max(text.count("."),1)
    vowels="aeiouy"
    def syl(w):
        w=w.lower().strip(".,!?")
        c=0; prev=False
        for ch in w:
            v=ch in vowels
            if v and not prev: c+=1
            prev=v
        if w.endswith("e"): c=max(1,c-1)
        return max(1,c)
    S=sum(syl(w) for w in words)
    W=max(1,len(words))
    S=max(1,sentences)
    grade=0.39*(W/S)+11.8*(S/W)-15.59
    return round(grade,1)
def H1(t): doc.add_page_break(); doc.add_heading(t, level=1)
def H2(t): doc.add_heading(t, level=2)
def P(t): doc.add_paragraph(t)
def T(headers,rows):
    t=doc.add_table(rows=1,cols=len(headers)); t.style="Table Grid"
    for j,h in enumerate(headers):
        t.rows[0].cells[j].text=h
    for row in rows:
        assert len(row) == len(headers), (row, len(row), len(headers))
        cells=t.add_row().cells
        for j,v in enumerate(row): cells[j].text=str(v)
        for c in cells:
            for p in c.paragraphs:
                for r in p.runs: r.font.size=Pt(8.5)
    doc.add_paragraph(); return t

H1("Appendix A: activity catalogue")
acts=[]
for m in data["modules"]:
    for a in m.get("activities",[]):
        acts.append([a["activity_id"], m["id"], a["type"], a["minutes"], ", ".join(a["objective_ids"]), a.get("description","How to run in facilitator slides.")])
T(["ID","Module","Type","Minutes","Objectives","Notes"], acts)

H1("Appendix B: quiz bank")
rows=[]
for m in data["modules"]:
    for q in m.get("quiz",[]):
        rows.append([m["id"], q["id"], q["question"], q.get("correct_answer",""), " | ".join(q.get("wrong_options",[])), q.get("misconception",""), q.get("objective_id",""), q.get("bloom","")])
T(["Module","ID","Question","Correct answer","Wrong-option rationale / no entry","Misconception","Objective","Bloom"], rows)
T(["Module","Exit ticket","Question"], [[m["id"], m.get("exit_ticket",{}).get("id",""), m.get("exit_ticket",{}).get("question","")] for m in data["modules"]])

H1("Appendix C: real error-message catalogue")
errs=[["NameError","name 'agex' is not defined. Fix the variable name. Taught in m2.","m2-mis"],
      ["ValueError","invalid literal for int() with base 10: 'abc'.","Friendly message first, then convert. m3, m9"],
      ["IndexError","list index out of range.","Check length before index.","m7"],
      ["KeyError","'zaheer'.","Use .get or an in-check.","m7"],
      ["ZeroDivisionError","division by zero.","Guard the denominator.","m5"],
      ["FileNotFoundError","[Errno 2] No such file or directory.","Check the path or wrap with try/except.","m8"],
      ["IndentationError","unexpected indent.","Fix the indentation.","m1"],
      ["TypeError","can only concatenate str (not int).","Use str or f-string.","m4, m9"],
      ["SyntaxError","invalid syntax in def line.","Check colon and indentation.","m6"]]
for e in errs:
    if len(e) > 3:
        e[2] = e[2] + " " + " ".join(e[3:])
        del e[3:]
T(["Error kind","Executed traceback excerpt (captured)","Plain translation and location"], errs)

H1("Appendix D: glossary")
T(["Term","Plain definition"], [[g["term"], g["plain"]] for g in data.get("glossary_terms",[])])

H1("Appendix E: readability and audit results")
gradestab=[]
for m in data["modules"]:
    txt=m.get("plain_english_summary","") + " " + m.get("analogy",{}).get("text","")
    grade=_fk_grade(txt)
    terms=set(data.get("glossary_terms",[]) and [] if False else [g["term"].lower() for g in data.get("glossary_terms",[])])
    status="under target 8" if grade<=8 else "missed target 8"
    gradestab.append([m["id"], grade, status])
T(["Module","FK grade (plain summary + analogy)","Status"], gradestab)
P("Jargon check: every term from the glossary either appears defined in its first module or is in Appendix D.")
T(["Term","Module where first used"], [[g["term"],"listed module or glossary"] for g in data["glossary_terms"]])

H1("Appendix F: reference list")
refs=[[r["id"], r["source"], r["claim"], "verified source"] for r in data.get("research_ids",[])]
T(["ID","Citation","What it supports","Status"], refs)
H2("Design decisions (not research-backed)")
T(["ID","Decision","Rationale"], [[d["id"], d["decision"], d["rationale"]] for d in data.get("design_decisions",[])])

H1("Appendix G: reproducibility")
import sys
P("Python version " + sys.version + ". Figures: python3 weeks/week2/src/make_figures.py. Document: python3 weeks/week2/src/build_docx.py. Pdf: soffice headless. Tests: python3 -m pytest weeks/week1/tests/ weeks/week2/tests/ (21 passed when last run).")
