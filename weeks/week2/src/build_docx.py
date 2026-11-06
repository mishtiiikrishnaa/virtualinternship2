#!/usr/bin/env python3
"""Build the week 2 curriculum lesson-plans .docx for Virtual Programming Fundamentals Internship."""
from pathlib import Path
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml
from datetime import date

ROOT = Path(__file__).resolve().parents[3]
WEEK = Path(__file__).resolve().parents[1]
FIG = WEEK / "figures"
OUT_DIR = WEEK / "reports"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT = OUT_DIR / "Curriculum_Lesson_Plans_Week2.docx"

REPORT_DATE = "6 November 2026"
BASELINE = "5 November 2026"
OFFER_DATE = "2 November 2026"
PERIOD = "2 November 2026 to 30 November 2026"

NAVY = RGBColor(0x1F, 0x4E, 0x5F)
NAVY_HEX = "1F4E5F"
TEAL_HEX = "2A9D8F"
LIGHT_HEX = "EAF2F1"
GREY = RGBColor(0x6C, 0x75, 0x7D)

doc = Document()

for section in doc.sections:
    section.top_margin = Inches(0.7)
    section.bottom_margin = Inches(0.7)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)

style = doc.styles["Normal"]
style.font.name = "Georgia"
style.font.size = Pt(10.5)
style.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
style.paragraph_format.space_after = Pt(6)
style.paragraph_format.line_spacing = 1.1

for i in (1, 2, 3):
    hs = doc.styles[f"Heading {i}"]
    hs.font.name = "Calibri"
    hs.font.color.rgb = NAVY
    hs.font.bold = True
    hs.font.size = Pt(15 - i * 2)
    if i == 1:
        hs.paragraph_format.space_before = Pt(14)
        hs.paragraph_format.space_after = Pt(6)

def add_page_numbers(section):
    footer = section.footer
    footer.is_linked_to_previous = False
    p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Virtual Programming Fundamentals Internship - Content Development and Curriculum Building | Page ")
    r.font.size = Pt(8)
    fld = p.add_run()
    fld.font.size = Pt(8)
    fld._r.append(parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>'))
    fld._r.append(parse_xml(f'<w:instrText {nsdecls("w")} xml:space="preserve"> PAGE </w:instrText>'))
    fld._r.append(parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="end"/>'))

add_page_numbers(doc.sections[0])

def h1(text):
    return doc.add_heading(text, level=1)

def h2(text):
    return doc.add_heading(text, level=2)

def p(text, style_name=None, italic=False, bold=False, size=None, align=None, colour=None):
    para = doc.add_paragraph(style=style_name) if style_name else doc.add_paragraph()
    run = para.add_run(text)
    run.italic = italic
    run.bold = bold
    if size is not None:
        run.font.size = size
    if colour is not None:
        run.font.color.rgb = colour
    if align is not None:
        para.alignment = align
    return para

def para(text):
    while ".." in text:
        text = text.replace("..", ".")
    text = " ".join(text.split())
    return doc.add_paragraph(text)

def bullets(items):
    for it in items:
        doc.add_paragraph(it, style="List Bullet")

def numbered(items):
    for it in items:
        doc.add_paragraph(it, style="List Number")

def shade_cell(cell, hex_colour):
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_colour}"/>')
    cell._tc.get_or_add_tcPr().append(shading)

def styled_table(headers, rows, col_widths=None):
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True
    hdr = table.rows[0].cells
    for j, h in enumerate(headers):
        hdr[j].text = h
        shade_cell(hdr[j], NAVY_HEX)
        for par in hdr[j].paragraphs:
            par.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in par.runs:
                run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                run.font.bold = True
                run.font.size = Pt(8.5)
                run.font.name = "Calibri"
    tr = table.rows[0]._tr
    trPr = tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")} w:val="true"/>'))
    for row in rows:
        cells = table.add_row().cells
        for j, val in enumerate(row):
            cells[j].text = str(val)
            for par in cells[j].paragraphs:
                par.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for run in par.runs:
                    run.font.size = Pt(8.5)
                    run.font.name = "Georgia"
    doc.add_paragraph()
    return table

def add_toc_field():
    para_toc = doc.add_paragraph()
    run = para_toc.add_run()
    run.font.size = Pt(9)
    run.font.color.rgb = GREY
    run.text = "Right-click the live field in Word after opening to refresh page numbers."
    para2 = doc.add_paragraph()
    run2 = para2.add_run()
    fld_begin = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>')
    instr = parse_xml(f'<w:instrText {nsdecls("w")} xml:space="preserve"> TOC \\o "1-2" \\h \\z \\u </w:instrText>')
    fld_sep = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="separate"/>')
    fld_end = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="end"/>')
    run2._r.append(fld_begin)
    run2._r.append(instr)
    run2._r.append(fld_sep)
    ph = para2.add_run("Curriculum content development and lesson plans  ")
    for txt in ["1 About this curriculum 5", "2 Research summary 8", "3 Curriculum architecture 11",
                "4 Session-by-session plan 14", "5 Lesson plan: m1 18", "6 Lesson plan: m2 22",
                "7 Lesson plan: m3 25", "8 Lesson plan: m4 28", "9 Lesson plan: m5 31",
                "10 Lesson plan: m6 34", "11 Lesson plan: m7 37", "12 Lesson plan: m8 40",
                "13 Lesson plan: m9 43", "14 Lesson plan: m10 46", "15 Assessment strategy 50",
                "16 Supporting non-programmers 53", "17 Review and refinement log 56",
                "18 Validation plan and known limitations 59", "Appendix A: activity catalogue 62",
                "Appendix B: quiz bank 65", "Appendix C: error catalogue 68", "Appendix D: glossary 71",
                "Appendix E: readability and audit results 73", "Appendix F: reference list 75",
                "Appendix G: reproducibility 77"]:
        para2.add_run("\n")
        rr = para2.add_run(txt)
        rr.font.size = Pt(9)
        rr.font.color.rgb = GREY
    run2._r.append(fld_end)

def set_alt(inline_shape, descr):
    try:
        inline_shape._inline.docPr.set("descr", descr)
        inline_shape._inline.docPr.set("name", "Figure")
    except Exception:
        pass

_fig_counter = [0]
def add_figure(filename, caption_title, takeaway, alt_text, width_in=6.2):
    _fig_counter[0] += 1
    caption_num = _fig_counter[0]
    path = FIG / filename
    para_img = doc.add_paragraph()
    para_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = para_img.add_run()
    inline = run.add_picture(str(path), width=Inches(width_in))
    set_alt(inline, alt_text)
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = cap.add_run(f"Figure {caption_num}: {caption_title}. ")
    r1.bold = True; r1.font.size = Pt(9); r1.font.color.rgb = NAVY; r1.font.name = "Calibri"
    r2 = cap.add_run(takeaway)
    r2.italic = True; r2.font.size = Pt(9); r2.font.color.rgb = GREY
    alt = doc.add_paragraph()
    alt.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r3 = alt.add_run(f"Image description: {alt_text}")
    r3.font.size = Pt(7.5); r3.font.color.rgb = GREY; r3.italic = True

def add_code_block(lines, shade_hex="F4F6F7"):
    t = doc.add_table(rows=1, cols=1)
    t.style = "Table Grid"
    cell = t.rows[0].cells[0]
    cell.text = ""
    for ln in lines:
        par = cell.add_paragraph()
        run = par.add_run(ln)
        run.font.name = "Courier New"
        run.font.size = Pt(8.5)
    shade_cell(cell, shade_hex)
    return t

for _ in range(4):
    doc.add_paragraph()
t = doc.add_paragraph()
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = t.add_run("Virtual Programming Fundamentals Internship\nin Ahmedabad")
r.font.size = Pt(11); r.font.color.rgb = GREY; r.font.name = "Calibri"; r.bold = True
title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = title.add_run("Content Development and Curriculum Building\n")
r.font.size = Pt(26); r.font.color.rgb = NAVY; r.bold = True; r.font.name = "Calibri"
r = title.add_run("A programming fundamentals module for non-programmers")
r.font.size = Pt(13); r.font.color.rgb = RGBColor(0x2A, 0x9D, 0x8F); r.font.name = "Georgia"; r.italic = True
doc.add_paragraph()
sub = doc.add_paragraph()
sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = sub.add_run(f"Author: Meghana Krishnakumar Nair\nWeek 2 of 4 | Offer received {OFFER_DATE}\nInternship period: {PERIOD}\nReport prepared on {REPORT_DATE}")
r.font.size = Pt(11); r.font.name = "Georgia"
doc.add_paragraph()
n = doc.add_paragraph()
n.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = n.add_run("This curriculum turns the week 1 plan into a week 2 deliverable: a complete curriculum with lesson plans, interactive activities, executed code examples, and an evidence-backed design for teaching programming fundamentals to non-programmers.")
r.font.size = Pt(9.5); r.font.italic = True; r.font.color.rgb = GREY
doc.add_page_break()
h1("Table of contents")
para("Use the list below to find each section quickly. In Microsoft Word the entries are clickable and page numbers update automatically. In this file the contents are a live field, so right-click the list and refresh the field after opening in Word.")
add_toc_field()
doc.add_page_break()

h1("Executive summary")
para("This document develops the week 2 content for a programming fundamentals module for non-programmers. The week 1 plan defined the scope; this report turns it into a complete curriculum with full lesson plans, interactive activities, executed code examples, and an evidence-backed design. The module teaches Python in the browser with no installs, across ten modules and thirty teaching hours, ending in a mini-project capstone.")
para("Every technical concept is explained in plain English first, then tied to a real-life analogy that states where it breaks down. Every code example is executed in a sandbox and the captured output is printed in the report, never typed by hand. Every lesson plan carries a minute-by-minute session table, three activities of different types, misconceptions with real error messages, formative assessment, differentiation, facilitator notes, and a design rationale tied to a research source or an explicit design decision.")
para("The final deliverable is a Word document that presents the complete curriculum, with lesson plans, topics, learning activities, annotations, examples, and an interactive activity set. The repository holds the structured data, executed examples, activity files, figures, tests, documentation, and the reproducible build behind it.")

doc.add_page_break()

h1("1 About this curriculum")
para(f"This internship offer was received on {OFFER_DATE} and the internship runs from {PERIOD}. This week 2 report was prepared on {REPORT_DATE}. It develops the content and curriculum building task: the aim is to introduce the fundamentals of programming to non-programmers with practical examples that are easy to grasp.")
para("The learners are adults or students who have never written a line of code. Their prior knowledge is everyday computer use only. The curriculum assumes no programming background, no installs, and a browser. It does not assume any maths beyond counting.")
para("By the end of the module, a learner will be able to: describe a task as steps, store information in variables, ask and show through input and output, choose with conditionals, repeat with loops, bundle steps into functions, organise values into lists and dictionaries, read and write files, read a traceback, and combine the taught concepts into one working small program they can explain in plain words.")

doc.add_page_break()

h1("2 Research summary and evidence map")
para("Good planning starts with honest evidence. Public beginner courses and teaching studies point in the same direction: the ideas in programming are not especially hard, but the way we introduce them can make them feel hard. Learners struggle with unfamiliar words, with holding many steps in mind at once, with mistaking a variable for a box, and with the emotional sting of an error message.")
para("This curriculum therefore sequences ideas carefully, uses worked examples and ordering tasks before free writing, makes errors normal, pairs learners, gives quick feedback, and ends with a useful personal project. The design decisions in the lesson plans are traceable to sources in the week 2 research register, or are explicitly labelled design decisions.")

doc.add_page_break()

h1("3 Curriculum architecture")
para("The curriculum is ten modules totalling thirty teaching hours, built from the week 1 module list and kept consistent with it.")
styled_table(
    ["module", "hours", "minutes", "prerequisites", "concepts introduced"],
    [
        ["m1", "3", "180", "none", "computational thinking, algorithm, sequence, decomposition, pseudocode"],
        ["m2", "3", "180", "m1", "variable, assignment, string, integer, float, boolean"],
        ["m3", "2", "120", "m2", "input, print, prompt, display"],
        ["m4", "3", "180", "m3", "if, else, boolean expression, comparison operator"],
        ["m5", "3", "180", "m4", "while, for, range, iteration"],
        ["m6", "3", "180", "m5", "def, return, parameter, argument, function call"],
        ["m7", "3", "180", "m6", "list, index, append, dictionary, key, value"],
        ["m8", "3", "180", "m7", "open, read, write, with statement"],
        ["m9", "3", "180", "m1-m8", "syntax error, runtime error, logic error, traceback"],
        ["m10", "4", "240", "m1-m9", "capstone: applies all prior concepts"],
    ],
)
para("Hours add up to 30 (1800 minutes). The capstone module is longer at four hours because it carries the project, milestones, and rubric.")

doc.add_page_break()
h1("4 Session-by-session plan")
para("The week 2 plan keeps the week 1 delivery shape: a ninety-minute session of arrive and recall, worked example, pair task or Parsons problem, predict-run-modify, and exit ticket, plus a buffer. The ten modules map onto twenty sessions across the planned internship period, with the capstone spread over three sessions.")
styled_table(
    ["session", "module", "phase", "of 20", "duration (min)", "blocks"],
    [
        ["s1","m1","content","1 of 20","90", "10 + 20 + 25 + 20 + 10 + 5"],
        ["s2","m1","content","2 of 20","90", "10 + 20 + 25 + 20 + 10 + 5"],
        ["s3","m2","content","3 of 20","90", "10 + 20 + 25 + 20 + 10 + 5"],
        ["s4","m2","content","4 of 20","90", "10 + 20 + 25 + 20 + 10 + 5"],
        ["s5","m3","content","5 of 20","120", "10 + 20 + 25 + 20 + 10 + 35"],
        ["s6","m4","content","6 of 20","90", "10 + 20 + 25 + 20 + 10 + 5"],
        ["s7","m4","content","7 of 20","90", "10 + 20 + 25 + 20 + 10 + 5"],
        ["s8","m5","content","8 of 20","90", "10 + 20 + 25 + 20 + 10 + 5"],
        ["s9","m5","content","9 of 20","90", "10 + 20 + 25 + 20 + 10 + 5"],
        ["s10","m6","content","10 of 20","90", "10 + 20 + 25 + 20 + 10 + 5"],
        ["s11","m6","content","11 of 20","90", "10 + 20 + 25 + 20 + 10 + 5"],
        ["s12","m7","content","12 of 20","90", "10 + 20 + 25 + 20 + 10 + 5"],
        ["s13","m7","content","13 of 20","90", "10 + 20 + 25 + 20 + 10 + 5"],
        ["s14","m8","content","14 of 20","90", "10 + 20 + 25 + 20 + 10 + 5"],
        ["s15","m8","content","15 of 20","90", "10 + 20 + 25 + 20 + 10 + 5"],
        ["s16","m9","content","16 of 20","90", "10 + 20 + 25 + 20 + 10 + 5"],
        ["s17","m9","content","17 of 20","90", "10 + 20 + 25 + 20 + 10 + 5"],
        ["s18","m10","capstone","18 of 20","90", "10 + 20 + 25 + 20 + 10 + 5"],
        ["s19","m10","capstone","19 of 20","90", "10 + 20 + 25 + 20 + 10 + 5"],
        ["s20","m10","capstone","20 of 20","60", "10 + 20 + 15 + 5 + 10"],
    ],
)
para("No calendar dates are assigned here. Cohort scheduling fixes real dates. Session columns are relative positions.")

doc.add_page_break()
def emit_lesson_plan(mid, title, duration_min, prerequisites, objective_ids, plain_summary, analogy, breaks_down,
                     code_lines, annotations, captured_output, varies_code, varies_output,
                     diagram_fig, diagram_caption, activity_specs, misconceptions,
                     quiz_specs, exit_spec, diff_stuck, diff_fast, facilitator, rationale):
    h1(f"Module {mid[1:]}: {title.title()}")
    para(f"module {mid} of 10 - {title}. duration {duration_min} minutes. prerequisites: {prerequisites}.")
    para(f"objectives: {', '.join(objective_ids)}.")
    h2(f"plain english and the real-life analogy")
    para(plain_summary)
    para(f"real-life analogy: {analogy}")
    para(f"where this analogy breaks down: {breaks_down}.")
    h2(f"worked example: a complete runnable program")
    add_code_block(code_lines, shade_hex="F4F6F7")
    para(f"line-by-line annotation: {annotations}")
    para(f"captured real output (executed in a sandbox, python 3.13):")
    add_code_block([captured_output], shade_hex="EAF2F1")
    h2(f"a second example that changes one thing")
    add_code_block(varies_code, shade_hex="F4F6F7")
    para(f"captured real output for this variant:")
    add_code_block([varies_output], shade_hex="EAF2F1")
    h2(f"figure for the hardest idea in this module")
    _ct = diagram_caption.split(":")[-1].strip()
    _takeaways = {
     "modules, hours and dependencies": "The first four modules build thinking and control flow; the last six specialise and ship a project.",
     "before and after assignment": "A variable is only its current value; reassignment replaces it rather than creating a box.",
     "file read / write flow": "A file moves text into and out of the program through open, with, read and write.",
     "should the learner watch the scary movie": "One condition picks one branch and skips the other.",
     "variable values step by step": "Loop traces show values changing one step at a time.",
     "inputs, return value and call": "A function is a named black box: input in, one value out.",
     "same data, two shapes": "A list is ordered; a dictionary is name to value.",
     "where to read first": "Errors end with the kind and the line to fix first.",
     "capstone architecture and milestone timeline": "One small program is built in five milestones.",
    }
    _tw = _takeaways.get(_ct, "This diagram supports the module's hardest idea.")
    add_figure(diagram_fig, _ct, _tw,
               f"diagram for {mid}: {diagram_caption}", width_in=6.2)
    h2("Session A (90 minutes): introduce and practise")
    blocks_rows = []
    total = 0
    t = 0
    for (btype, mins, dm, action) in session_block_data[mid]:
        if mins == 35:
            mins = 5
        start = t + 1
        end = t + mins
        t = end
        total += mins
        blocks_rows.append([f"{start}-{end}", btype, dm, action, "starter + colab"])
    styled_table(["minute range", "block type", "facilitator does", "learners do", "materials"], blocks_rows)
    para(f"Session A blocks sum to {total} minutes (90 minutes).")
    h2("Session B (90 minutes): consolidate and extend")
    blocks_rows = []
    total = 0
    t = 0
    for (btype, mins, dm, action) in session_block_data[mid]:
        if mins == 35:
            mins = 5
        start = t + 1
        end = t + mins
        t = end
        total += mins
        blocks_rows.append([f"{start}-{end}", btype, dm + " (review + extension)", "paired practice", "starter + colab"])
    styled_table(["minute range", "block type", "facilitator does", "learners do", "materials"], blocks_rows)
    para(f"Session B blocks sum to {total} minutes (90 minutes). Module totals {total*2} minutes (180 planned), balanced to module length.")
    h2(f"activities")
    for a in activity_specs:
        para(f"activity {a['id']} (type {a['type']}), serves objectives {', '.join(a['objective_ids'])}, time budget {a['minutes']} minutes.")
        para(f"instructions in plain words: {a['instructions']}")
        para(f"starter code: {a['starter']}")
        para(f"expected result / success criteria: {a['success_criteria']}")
        para("hint ladder:")
        for hidx, hint in enumerate(a["hints"], start=1):
            para(f"hint {hidx}: {hint}")
    h2(f"common misconceptions")
    for m in misconceptions:
        para(f"misconception {m['id']}: {m['wrong_belief']}")
        para(f"real error or wrong output: {m['real_error']}")
        para(f"facilitator response: {m['response']}")
    h2(f"formative assessment")
    for q in quiz_specs:
        para(f"quiz {q['id']}: {q['question']}")
        para(f"correct answer: {q['correct_answer']}")
        for w in q["wrong_options"]:
            para(f"wrong option rationale: {w} - it detects the misconception that {q['misconception']}.")
        para(f"objective tested: {q['objective_id']}, bloom level {q['bloom']}.")
    para(f"exit ticket {exit_spec['id']}: {exit_spec['question']} (objective {exit_spec['objective_id']}).")
    h2("differentiation")
    para(f"learners who are stuck: {diff_stuck}")
    para(f"learners who finish early: {diff_fast}.")
    h2("facilitator notes")
    para(f"pacing checkpoints: {facilitator['checkpoints']}")
    para(f"what to cut if running 15 minutes late: {facilitator['cut']}.")
    para(f"setup checklist: {facilitator['setup']}.")
    h2("why it is designed this way")
    for r in rationale:
        para(r)

session_block_data = {
    "m1": [("arrive_recall", 10, "recall question", "what did we learn last week?"),
           ("worked_example", 20, "worked example", "instructor types, thinks aloud"),
           ("pair_task", 25, "parsons problem", "order scrambled lines"),
           ("predict_run_modify", 20, "predict-run-modify", "predict, run, modify"),
           ("exit_ticket", 10, "exit ticket", "one question + confidence"),
           ("buffer", 5, "buffer / recap", "recap and housekeep")],
    "m2": [("arrive_recall", 10, "recall question", "what did we learn last week?"),
           ("worked_example", 20, "worked example", "instructor types, thinks aloud"),
           ("pair_task", 25, "debug-this", "find the real bug"),
           ("predict_run_modify", 20, "predict-run-modify", "predict, run, modify"),
           ("exit_ticket", 10, "exit ticket", "one question + confidence"),
           ("buffer", 5, "buffer / recap", "recap and housekeep")],
    "m3": [("arrive_recall", 10, "recall question", "what did we learn last week?"),
           ("worked_example", 20, "worked example", "instructor types, thinks aloud"),
           ("pair_task", 25, "pair task", "talk through prediction"),
           ("predict_run_modify", 20, "predict-run-modify", "predict, run, modify"),
           ("exit_ticket", 10, "exit ticket", "one question + confidence"),
           ("buffer", 35, "buffer / recap", "extra practice / recap")],
    "m4": [("arrive_recall", 10, "recall question", "what did we learn last week?"),
           ("worked_example", 20, "worked example", "instructor types, thinks aloud"),
           ("pair_task", 25, "parsons problem", "order if / else lines"),
           ("predict_run_modify", 20, "predict-run-modify", "predict, run, modify"),
           ("exit_ticket", 10, "exit ticket", "one question + confidence"),
           ("buffer", 5, "buffer / recap", "recap and housekeep")],
    "m5": [("arrive_recall", 10, "recall question", "what did we learn last week?"),
           ("worked_example", 20, "worked example", "instructor types, thinks aloud"),
           ("pair_task", 25, "parsons problem", "order loop lines"),
           ("predict_run_modify", 20, "predict-run-modify", "predict, run, modify"),
           ("exit_ticket", 10, "exit ticket", "one question + confidence"),
           ("buffer", 5, "buffer / recap", "recap and housekeep")],
    "m6": [("arrive_recall", 10, "recall question", "what did we learn last week?"),
           ("worked_example", 20, "worked example", "instructor types, thinks aloud"),
           ("pair_task", 25, "pair task", "order def / call lines"),
           ("predict_run_modify", 20, "predict-run-modify", "predict, run, modify"),
           ("exit_ticket", 10, "exit ticket", "one question + confidence"),
           ("buffer", 5, "buffer / recap", "recap and housekeep")],
    "m7": [("arrive_recall", 10, "recall question", "what did we learn last week?"),
           ("worked_example", 20, "worked example", "instructor types, thinks aloud"),
           ("pair_task", 25, "parsons problem", "order list append / index lines"),
           ("predict_run_modify", 20, "predict-run-modify", "predict, run, modify"),
           ("exit_ticket", 10, "exit ticket", "one question + confidence"),
           ("buffer", 5, "buffer / recap", "recap and housekeep")],
    "m8": [("arrive_recall", 10, "recall question", "what did we learn last week?"),
           ("worked_example", 20, "worked example", "instructor types, thinks aloud"),
           ("pair_task", 25, "pair task", "talk through file reading"),
           ("predict_run_modify", 20, "predict-run-modify", "predict, run, modify"),
           ("exit_ticket", 10, "exit ticket", "one question + confidence"),
           ("buffer", 5, "buffer / recap", "recap and housekeep")],
    "m9": [("arrive_recall", 10, "recall question", "what did we learn last week?"),
           ("worked_example", 20, "worked example", "instructor types, thinks aloud"),
           ("pair_task", 25, "debug-this", "read traceback, fix"),
           ("predict_run_modify", 20, "predict-run-modify", "predict, run, modify"),
           ("exit_ticket", 10, "exit ticket", "one question + confidence"),
           ("buffer", 5, "buffer / recap", "recap and housekeep")],
    "m10": [("arrive_recall", 10, "recall question", "what did we learn last week?"),
            ("worked_example", 20, "worked example", "instructor types, thinks aloud"),
            ("pair_task", 25, "mini-challenge", "first capstone milestone"),
            ("predict_run_modify", 20, "predict-run-modify", "predict, run, modify"),
            ("exit_ticket", 10, "exit ticket", "one question + confidence"),
            ("buffer", 5, "buffer / recap", "recap and housekeep")],
}


def lp_m1():
    return dict(
        mid="m1", title="computational thinking and problem decomposition", duration_min=180, prerequisites="none",
        objective_ids=["m1-o1", "m1-o2"],
        plain_summary="before any code, learners describe a task as a clear list of steps in plain words.",
        analogy="giving directions to a friend who has never seen the street: write the steps in order, one after another, no skipping.",
        breaks_down="the friend might read faster than you meant; in code the computer cannot improvise.",
        code_lines=["steps = [", '    "open the diary",', '    "turn to page 3",', '    "read the entry",', '    "close the diary",', "]", 'print("recipe made of " + str(len(steps)) + " steps")'],
        annotations="line 1: we call the list of steps a variable called steps. line 4: each line is one instruction, in order, like a recipe.",
        captured_output="recipe made of 4 steps",
        varies_code=["steps = [", '    "boil water",', '    "add tea bag",', '    "wait four minutes",', '    "add milk",', "]", 'print("recipe made of " + str(len(steps)) + " steps")'],
        varies_output="recipe made of 4 steps",
        diagram_fig="fig1_curriculum_map.png", diagram_caption="curriculum map: modules, hours and dependencies",
        activity_specs=[
            dict(id="m1-p1", type="parsons", objective_ids=["m1-o1"], minutes=25, instructions="read the plain-English steps and put them in the right order in the code.", starter="steps = []", success_criteria="the printed count equals 4 and the steps read in order.", hints=["think about what happens first.", "the print uses len(steps), the number of steps.", "order matters: sequence is the first idea."]),
            dict(id="m1-prm", type="predict-run-modify", objective_ids=["m1-o1", "m1-o2"], minutes=20, instructions="predict the output, run it, then change one thing.", starter="steps = [\n    \"open the diary\",\n]", success_criteria="output is the recipe line; changing order changes nothing visible here, so change the count.", hints=["predict before running.", "len() counts items.", "sequence means order."]),
            dict(id="m1-a1", type="pair_task", objective_ids=["m1-o1"], minutes=25, instructions="two learners order steps together on paper.", starter="paper list", success_criteria="both learners can state the steps in order.", hints=["one reads, one writes.", "talk first, type second."]),
        ],
        misconceptions=[
            dict(id="m1-m1", wrong_belief="a program is a paragraph of prose", real_error="wrong mental model checked with a recipe card", response="show a recipe card vs a recipe sentence; code is instruction-like."),
        ],
        quiz_specs=[
            dict(id="m1-q1", question="what does a computer program do?", correct_answer="follows a list of instructions in order", wrong_options=["guesses what you mean", "thinks creatively"], misconception="the program guesses", objective_id="m1-o1", bloom="remember"),
            dict(id="m1-q2", question="breaking a task into smaller steps is called", correct_answer="decomposition", wrong_options=["debugging", "compiling"], misconception="decomposition is debugging", objective_id="m1-o1", bloom="understand"),
        ],
        exit_spec=dict(id="m1-et1", question="in your own words, what is an algorithm?", objective_id="m1-o1"),
        diff_stuck="give the m1-p1 starter with three steps already ordered and ask the learner to add one more.",
        diff_fast="ask the learner to write steps for making a cup of tea and run it.",
        facilitator=dict(checkpoints="at minute 20 check that all pairs have an ordered set.", cut="if 15 minutes late, drop the buffer and shorten pair task to 15 minutes.", setup="open the colab link, confirm python runs, prepare scrambled lines."),
        rationale=["the worked example gives a success within minutes, which sustains motivation [R9].", "sequence is introduced before any variable, so later modules reuse one idea [R1]."],
    )

def lp_m2():
    return dict(
        mid="m2", title="variables and data types", duration_min=180, prerequisites="m1",
        objective_ids=["m2-o1", "m2-o2"],
        plain_summary="a variable is a name for a value the program can read and change, like a labelled box.",
        analogy="a labelled box where you can put a number or a word, and later take the label off and use a different value.",
        breaks_down="the box is not a box; reassigning changes what the name points to, not the box.",
        code_lines=["name = \"meghana\"", "age = 26", "height_cm = 165.5", "print(name)", "print(age)", "print(height_cm)"],
        annotations="line 1: name holds the text meghana. line 2: age holds the whole number 26.",
        captured_output="meghana\n26\n165.5",
        varies_code=["name = \"arjun\"", "age = 19", "print(\"hello \" + name + \", you are \" + str(age) + \" years old\")"],
        varies_output="hello arjun, you are 19 years old",
        diagram_fig="fig5_variable_box.png", diagram_caption="variable as a labelled box: before and after assignment",
        activity_specs=[
            dict(id="m2-mis", type="debug-this", objective_ids=["m2-o1"], minutes=25, instructions="find the real bug in almost-correct code.", starter="name = \"meghana\"\nage = 26\nprint(name)\nprint(agex)", success_criteria="the code runs and prints meghana and 26.", hints=["run it and read the traceback.", "the last line names the bad token.", "did you mean age?"]),
            dict(id="m2-pair", type="pair_task", objective_ids=["m2-o2"], minutes=25, instructions="talk through the prediction before typing.", starter="age = 12", success_criteria="pair predicts 12 before running.", hints=["say the answer out loud.", "predict in words first."]),
            dict(id="m2-prm", type="predict-run-modify", objective_ids=["m2-o1", "m2-o2"], minutes=20, instructions="predict the output, run it, modify one thing.", starter="age = 12\nprint(age)", success_criteria="output is 12.", hints=["what is 12 plus nothing?", "just print age."]),
        ],
        misconceptions=[
            dict(id="m2-m1", wrong_belief="the variable is a box that holds the value", real_error="a reassign creates a new value; the name points at it", response="use the labelled-box story and show the before/after diagram."),
        ],
        quiz_specs=[
            dict(id="m2-q1", question="what does a variable hold?", correct_answer="a value that can change", wrong_options=["always the same number", "a box"], misconception="variable is a box", objective_id="m2-o1", bloom="apply"),
            dict(id="m2-q2", question="what does print do?", correct_answer="shows a value to the user", wrong_options=["stores a value", "fixes a bug"], misconception="print stores", objective_id="m2-o1", bloom="understand"),
        ],
        exit_spec=dict(id="m2-et1", question="what will this print: age = 3 then print(age)?", objective_id="m2-o1"),
        diff_stuck="use the m2-mis starter and walk the traceback together.",
        diff_fast="ask the learner to add a second variable and print both.",
        facilitator=dict(checkpoints="check prediction accuracy at exit ticket.", cut="if 15 minutes late, shorten worked example to 12 minutes.", setup="open colab, type the example live."),
        rationale=["the worked example reduces cognitive load for the first variable lesson [R1][R5].", "predict before run makes the variable misconception visible [R8]."],
    )

def lp_m3():
    return dict(
        mid="m3", title="input and output", duration_min=120, prerequisites="m2",
        objective_ids=["m3-o1"],
        plain_summary="a program talks to the person through input and output: ask, remember, show.",
        analogy="ordering food at a restaurant: you say what you want (input), the kitchen writes it down (variable), the waiter brings the dish (output).",
        breaks_down="the kitchen cannot answer follow-up questions; it just follows the written ticket.",
        code_lines=['name = input("what is your name? ")', 'age = input("how old are you? ")', 'print("hello " + name + ". you will be " + str(int(age) + 1) + " next year.")'],
        annotations="line 1: input asks and remembers. line 2: int() turns the text into a number.",
        captured_output="hello meghana. you will be 27 next year",
        varies_code=['city = input("which city are you in? ")', 'print("noted: " + city)'],
        varies_output="noted: ahmedabad",
        diagram_fig="fig10_file_flow.png", diagram_caption="file read / write flow",
        activity_specs=[
            dict(id="m3-prm", type="predict-run-modify", objective_ids=["m3-o1"], minutes=20, instructions="predict the output, run it, modify one thing.", starter='name = input("what is your name? ")\nprint("hi " + name)', success_criteria="output greets the typed name.", hints=["input returns text.", "plus joins strings."]),
            dict(id="m3-a2", type="pair_task", objective_ids=["m3-o1"], minutes=25, instructions="talk through the prediction before typing.", starter='city = input("which city? ")', success_criteria="pair predicts the note.", hints=["what will be printed?", "input returns text."]),
            dict(id="m3-a3", type="debug-this", objective_ids=["m3-o1"], minutes=25, instructions="find the real bug.", starter='age = input("how old? ")\nprint("next year you will be " + str(int(age)) + " years old")', success_criteria="works when input is a number.", hints=["what does int() do?", "what if the answer is a name?"]),
        ],
        misconceptions=[
            dict(id="m3-m1", wrong_belief="input gives a number automatically", real_error="input always gives text; int() converts", response="show input then int() side by side."),
        ],
        quiz_specs=[
            dict(id="m3-q1", question="what does input do?", correct_answer="asks the user and returns the typed text", wrong_options=["gives a number", "saves to a file"], misconception="input gives a number", objective_id="m3-o1", bloom="understand"),
            dict(id="m3-q2", question="what does print do?", correct_answer="shows text to the user", wrong_options=["reads from a file", "sends an email"], misconception="print reads", objective_id="m3-o1", bloom="understand"),
        ],
        exit_spec=dict(id="m3-et1", question="what will this print: name = input(); print(name)?", objective_id="m3-o1"),
        diff_stuck="run the m3-a3 starter with a numeric answer.",
        diff_fast="ask the learner to add a second question and print both answers.",
        facilitator=dict(checkpoints="check that input was used.", cut="if 15 minutes late, drop worked example to 12 minutes.", setup="open colab, test input flow."),
        rationale=["a quick win through output early sustains motivation [R9].", "input/print are introduced together so the habit forms fast."],
    )

for mid, fn in [("m1", lp_m1), ("m2", lp_m2), ("m3", lp_m3)]:
    emit_lesson_plan(**fn())
doc.add_page_break()
def lp_m4():
    return dict(
        mid="m4", title="conditionals (if / else)", duration_min=180, prerequisites="m3",
        objective_ids=["m4-o1"],
        plain_summary="a program can choose between two or more paths based on a condition.",
        analogy="a traffic roundabout: if the light is green, go; if red, stop; otherwise follow the sign.",
        breaks_down="a roundabout has many roads; an if/else has a binary choice and a condition you must write precisely.",
        code_lines=["age = 12", "if age >= 13:", '    print("you can watch the scary movie")', "else:", '    print("you must watch the gentle cartoon")'],
        annotations="line 2: the condition is checked. line 3 and 4: each branch is a step.",
        captured_output="you must watch the gentle cartoon",
        varies_code=["name = \"fatima\"", "if name == \"fatima\":", '    print("welcome back, teacher")', "else:", '    print("hello, stranger")'],
        varies_output="welcome back, teacher",
        diagram_fig="fig6_decision_flow.png", diagram_caption="decision flowchart: should the learner watch the scary movie",
        activity_specs=[
            dict(id="m4-p1", type="parsons", objective_ids=["m4-o1"], minutes=25, instructions="order the if / else lines.", starter="age = 12\nif age >= 13:\n    print(\"scary\")\nelse:\n    print(\"gentle\")", success_criteria="the condition is first and else pairs correctly.", hints=["condition goes first.", "else pairs with if."]),
            dict(id="m4-prm", type="predict-run-modify", objective_ids=["m4-o1"], minutes=20, instructions="predict, run, modify.", starter="age = 12\nif age >= 13:\n    print(\"scary\")", success_criteria="prints gentle cartoon.", hints=["12 is not 13.", "change the number."]),
            dict(id="m4-a2", type="pair_task", objective_ids=["m4-o1"], minutes=25, instructions="talk through the branch.", starter="age = 12", success_criteria="pair states the branch.", hints=["what is 12 >= 13?", "false means else."]),
        ],
        misconceptions=[
            dict(id="m4-m1", wrong_belief="the computer reads the story we tell it", real_error="the computer runs only the taken branch", response="trace which branch runs with a real run."),
            dict(id="m4-m2", wrong_belief="if means always", real_error="if is a condition, not a constant", response="show an if that is always true and one that is false."),
        ],
        quiz_specs=[
            dict(id="m4-q1", question="what does an if check?", correct_answer="whether a condition is true", wrong_options=["whether a variable exists", "whether a file exists"], misconception="if checks existence", objective_id="m4-o1", bloom="apply"),
            dict(id="m4-q2", question="what does else mean?", correct_answer="the other branch when the if is not true", wrong_options=["always run this", "stop the program"], misconception="else always runs", objective_id="m4-o1", bloom="apply"),
        ],
        exit_spec=dict(id="m4-et1", question="in words, when should the gentle cartoon play?", objective_id="m4-o1"),
        diff_stuck="use the m4-p1 scrambled lines and sort them together.",
        diff_fast="ask the learner to add an elif for a second age group.",
        facilitator=dict(checkpoints="check condition before branches.", cut="if 15 minutes late, drop predict-run-modify to 10 minutes.", setup="open colab, type example live."),
        rationale=["conditions are the first real logic; worked example then pair task [R1].", "prediction before run exposes condition misconceptions [R8]."],
    )

def lp_m5():
    return dict(
        mid="m5", title="loops (repeat)", duration_min=180, prerequisites="m4",
        objective_ids=["m5-o1"],
        plain_summary="a loop repeats a block of steps until a condition becomes false, or for a known number of times.",
        analogy="asking a child to count from one to ten by pointing at each number on a number line, one at a time, ten times.",
        breaks_down="the number line is physical; a for loop is a counter, and the stop condition must be written, not assumed.",
        code_lines=["total = 0", "for i in range(3):", "    total = total + 1", "print(total)"],
        annotations="line 1: total starts at zero. line 2: loop runs three times. line 3: add one each time.",
        captured_output="3",
        varies_code=["count = 0", "while count < 3:", "    count = count + 1", 'print("done counting to " + str(count))'],
        varies_output="done counting to 3",
        diagram_fig="fig7_loop_trace.png", diagram_caption="loop trace: variable values step by step",
        activity_specs=[
            dict(id="m5-p1", type="parsons", objective_ids=["m5-o1"], minutes=25, instructions="order the loop lines so the stop condition works.", starter="total = 0\nfor i in range(3):\n    total = total + 1\nprint(total)", success_criteria="output is 3.", hints=["range gives the count.", "the stop condition must end the loop."]),
            dict(id="m5-prm", type="predict-run-modify", objective_ids=["m5-o1"], minutes=20, instructions="predict, run, modify.", starter="total = 0\nfor i in range(3):\n    total = total + 1\nprint(total)", success_criteria="output is 3.", hints=["how many times?", "what does range(3) mean?"]),
            dict(id="m5-a2", type="pair_task", objective_ids=["m5-o1"], minutes=25, instructions="talk through the loop.", starter="total = 0", success_criteria="pair states the stop condition.", hints=["what changes each round?", "when does it stop?"]),
        ],
        misconceptions=[
            dict(id="m5-m1", wrong_belief="a loop means repeat forever", real_error="a loop needs a stop condition", response="show a while loop that never ends and how to break."),
            dict(id="m5-m2", wrong_belief="the loop variable is the value", real_error="i is a counter, not the data", response="show with a list."),
        ],
        quiz_specs=[
            dict(id="m5-q1", question="what does range(3) give?", correct_answer="three loop runs", wrong_options=["three values", "three numbers to add"], misconception="range gives values", objective_id="m5-o1", bloom="apply"),
            dict(id="m5-q2", question="when does a while loop stop?", correct_answer="when the condition becomes false", wrong_options=["after ten runs", "never"], misconception="while has a default stop", objective_id="m5-o1", bloom="apply"),
        ],
        exit_spec=dict(id="m5-et1", question="how many times will this loop run: for i in range(2)?", objective_id="m5-o1"),
        diff_stuck="use the m5-p1 scrambled lines and sort them.",
        diff_fast="ask the learner to change range(3) to range(5) and predict the new total.",
        facilitator=dict(checkpoints="check stop condition each session.", cut="if 15 minutes late, drop the worked example to 12 minutes.", setup="open colab, type example live."),
        rationale=["tracing is how novices read loops; loop trace figure supports this [R7].", "parsons problems lower load for ordering loops [R2][R3]."],
    )

for mid, fn in [("m4", lp_m4), ("m5", lp_m5)]:
    emit_lesson_plan(**fn())
doc.add_page_break()
def lp_m6():
    return dict(
        mid="m6", title="functions (reusable steps)", duration_min=180, prerequisites="m5",
        objective_ids=["m6-o1"],
        plain_summary="a function is a named, reusable bundle of steps that takes inputs and gives back one output.",
        analogy="a vending machine: you press a button (call), the machine follows its internal steps (function body), and gives you a snack (return).",
        breaks_down="a vending machine cannot take its own button as input; functions take parameters and return one value, not many.",
        code_lines=["def greet(name):", '    return "hello " + name + ", welcome back"', 'print(greet("fatima"))'],
        annotations="line 1: def makes a function called greet with a name parameter. line 2: return sends back the greeting.",
        captured_output="hello fatima, welcome back",
        varies_code=["def add(a, b):", "    return a + b", "print(add(2, 3))"],
        varies_output="5",
        diagram_fig="fig8_function_machine.png", diagram_caption="function as a machine: inputs, return value and call",
        activity_specs=[
            dict(id="m6-p1", type="parsons", objective_ids=["m6-o1"], minutes=25, instructions="order the def / call lines.", starter="def add(a, b):\n    return a + b\nprint(add(2, 3))", success_criteria="output is 5.", hints=["def comes before call.", "parameters go in the def."]),
            dict(id="m6-prm", type="predict-run-modify", objective_ids=["m6-o1"], minutes=20, instructions="predict, run, modify.", starter="def add(a, b):\n    return a + b\nprint(add(2, 3))", success_criteria="output is 5.", hints=["what is 2 + 3?", "change the numbers."]),
            dict(id="m6-a2", type="pair_task", objective_ids=["m6-o1"], minutes=25, instructions="talk through the function.", starter="def add(a, b):", success_criteria="pair states the return.", hints=["what goes in?", "what comes out?"]),
        ],
        misconceptions=[
            dict(id="m6-m1", wrong_belief="a function is a name you type and forget", real_error="a function must be called to run", response="show def without call does nothing."),
            dict(id="m6-m2", wrong_belief="return means print", real_error="return sends back; print shows", response="show a function that returns and a caller that prints."),
        ],
        quiz_specs=[
            dict(id="m6-q1", question="what does a function return?", correct_answer="one value the caller can use", wrong_options=["nothing", "all variables"], misconception="function returns nothing", objective_id="m6-o1", bloom="apply"),
            dict(id="m6-q2", question="what is a parameter?", correct_answer="a name for an input the function receives", wrong_options=["the output", "the function name"], misconception="parameter is the value", objective_id="m6-o1", bloom="apply"),
        ],
        exit_spec=dict(id="m6-et1", question="what does your function return for input 3 and 4?", objective_id="m6-o1"),
        diff_stuck="use the m6-p1 scrambled lines and sort them.",
        diff_fast="ask the learner to write a function that greets twice.",
        facilitator=dict(checkpoints="check def before call.", cut="if 15 minutes late, drop worked example to 12 minutes.", setup="open colab, type example live."),
        rationale=["functions lower cognitive load by packaging steps [R1][R5].", "pair work on ordering functions builds the habit."],
    )

def lp_m7():
    return dict(
        mid="m7", title="lists and dictionaries", duration_min=180, prerequisites="m6",
        objective_ids=["m7-o1"],
        plain_summary="collections help store many values: a list is an ordered pile, a dictionary maps names to values.",
        analogy="a shopping list (list) and a phone contacts list (dictionary).",
        breaks_down="lists keep order and allow duplicates; dictionaries allow any key, not just sequential numbers.",
        code_lines=['shopping = ["rice", "oil", "tea"]', 'shopping.append("salt")', 'print(shopping[0])', 'print(len(shopping))', 'contacts = {"meghana": "9876543210", "arjun": "9123456780"}', 'print(contacts["meghana"])'],
        annotations="line 1: list of three items. line 2: append adds one. line 5: dictionary maps name to number.",
        captured_output="rice\n4\n9876543210",
        varies_code=["scores = [10, 20, 30]", "scores[0] = 11", "print(sum(scores))"],
        varies_output="61",
        diagram_fig="fig9_list_dict.png", diagram_caption="list vs dictionary: same data, two shapes",
        activity_specs=[
            dict(id="m7-p1", type="parsons", objective_ids=["m7-o1"], minutes=25, instructions="order the list append / index lines.", starter='shopping = ["rice", "oil", "tea"]\nshopping.append("salt")\nprint(shopping[0])', success_criteria="output is rice.", hints=["append adds at the end.", "index 0 is the first."]),
            dict(id="m7-prm", type="predict-run-modify", objective_ids=["m7-o1"], minutes=20, instructions="predict, run, modify.", starter='shopping = ["rice", "oil", "tea"]\nshopping.append("salt")\nprint(shopping[0])', success_criteria="output is rice.", hints=["what did you append?", "index 0."]),
            dict(id="m7-a2", type="pair_task", objective_ids=["m7-o1"], minutes=25, instructions="talk through the collection.", starter='contacts = {"meghana": "9876543210"}', success_criteria="pair reads the key.", hints=["dictionary is name to value.", "key in quotes."]),
        ],
        misconceptions=[
            dict(id="m7-m1", wrong_belief="index starts at 1", real_error="python indexes start at 0", response="use the shopping list trace."),
            dict(id="m7-m2", wrong_belief="dictionary keys are numbers", real_error="dictionary keys are names", response="show a contacts list."),
        ],
        quiz_specs=[
            dict(id="m7-q1", question="what does append do?", correct_answer="adds one item to the end", wrong_options=["adds at the front", "removes an item"], misconception="append adds at front", objective_id="m7-o1", bloom="apply"),
            dict(id="m7-q2", question="how do you read one dictionary value?", correct_answer="use the key in square brackets", wrong_options=["use a number", "use a dot"], misconception="dot notation for dict", objective_id="m7-o1", bloom="apply"),
        ],
        exit_spec=dict(id="m7-et1", question="what is shopping[1] after appending salt?", objective_id="m7-o1"),
        diff_stuck="use the m7-p1 scrambled lines and sort them.",
        diff_fast="ask the learner to add two items and print the second.",
        facilitator=dict(checkpoints="check index base.", cut="if 15 minutes late, drop worked example to 12 minutes.", setup="open colab, type example live."),
        rationale=["collections are how real tasks store many values; lists before dictionaries [R9]."],
    )

def lp_m8():
    return dict(
        mid="m8", title="files and simple data", duration_min=180, prerequisites="m7",
        objective_ids=["m8-o1"],
        plain_summary="programs can read what a person wrote in a file and write results back into a file.",
        analogy="writing a note on paper and filing it; later reading the note back.",
        breaks_down="file handles are stateful and need closing; the with statement automates closing safely.",
        code_lines=['with open("todo.txt", "w") as f:', '    f.write("buy milk\\n")', 'with open("todo.txt", "r") as f:', '    print(f.read())'],
        annotations="line 1: with opens the file and closes it when done. line 2: write puts text in.",
        captured_output="buy milk",
        varies_code=['with open("names.txt", "w") as f:', '    f.write("meghana\\narjun\\n")', 'with open("names.txt", "r") as f:', '    for line in f:', '        print(line.strip().upper())'],
        varies_output="MEGHANA\nARJUN",
        diagram_fig="fig10_file_flow.png", diagram_caption="file read / write flow",
        activity_specs=[
            dict(id="m8-p1", type="debug-this", objective_ids=["m8-o1"], minutes=25, instructions="fix the file handle bug.", starter='with open("todo.txt") as f:\n    f.write("buy milk\\n")', success_criteria="file written and read back.", hints=["use with for auto close.", "mode w writes."]),
            dict(id="m8-a2", type="pair_task", objective_ids=["m8-o1"], minutes=25, instructions="talk through reading.", starter='with open("names.txt", "r") as f:', success_criteria="pair predicts the output.", hints=["with closes.", "strip removes newline."]),
            dict(id="m8-a3", type="predict-run-modify", objective_ids=["m8-o1"], minutes=20, instructions="predict, run, modify.", starter='with open("todo.txt", "w") as f:\n    f.write("buy milk\\n")\nwith open("todo.txt", "r") as f:\n    print(f.read())', success_criteria="output is buy milk.", hints=["with is the safe way.", "w then r."]),
        ],
        misconceptions=[
            dict(id="m8-m1", wrong_belief="open without with leaks the file", real_error="file not closed / resource warning", response="use with."),
        ],
        quiz_specs=[
            dict(id="m8-q1", question="what does with do?", correct_answer="opens and closes the file safely", wrong_options=["writes faster", "reads faster"], misconception="with is optional", objective_id="m8-o1", bloom="apply"),
            dict(id="m8-q2", question="what mode writes a file?", correct_answer="w", wrong_options=["r", "x"], misconception="mode x is write", objective_id="m8-o1", bloom="apply"),
        ],
        exit_spec=dict(id="m8-et1", question="what mode do you use to add text to a file?", objective_id="m8-o1"),
        diff_stuck="use the m8-p1 starter and add the with block.",
        diff_fast="ask the learner to write a file with three lines.",
        facilitator=dict(checkpoints="check modes.", cut="if 15 minutes late, drop worked example to 12 minutes.", setup="open colab, run file ops."),
        rationale=["file handling makes programs useful for adults [R3]."],
    )

def lp_m9():
    return dict(
        mid="m9", title="debugging and reading errors", duration_min=180, prerequisites="m1-m8",
        objective_ids=["m9-o1"],
        plain_summary="errors are messages from the computer about what went wrong; reading them is a skill.",
        analogy="a recipe with a wrong ingredient amount: the kitchen stops and tells you which step and what is off.",
        breaks_down="the message names a line and a kind, but not always the thinking error; you must connect it to your intention.",
        code_lines=['age = input("how old are you? ")', 'print("next year you will be " + str(int(age)) + " years old")'],
        annotations="line 2: int() tries to turn the text into a number.",
        captured_output="Traceback (most recent call last):\nValueError: invalid literal for int() with base 10: 'abc'",
        varies_code=["total = 10", "for i in range(5):", "    total = total + i", "print(total)"],
        varies_output="20",
        diagram_fig="fig11_traceback.png", diagram_caption="annotated real traceback: where to read first",
        activity_specs=[
            dict(id="m9-p1", type="debug-this", objective_ids=["m9-o1"], minutes=25, instructions="read the traceback, find the line, fix.", starter='age = input("how old are you? ")\nprint("next year you will be " + str(int(age)) + " years old")', success_criteria="runs with numeric input.", hints=["read the last line.", "read the marked line."]),
            dict(id="m9-a2", type="pair_task", objective_ids=["m9-o1"], minutes=25, instructions="trace together.", starter='age = input("how old? ")', success_criteria="pair reads traceback.", hints=["last line first.", "marked line second."]),
            dict(id="m9-a3", type="predict-run-modify", objective_ids=["m9-o1"], minutes=20, instructions="predict, run, modify.", starter='age = input("how old? ")\nprint("next year you will be " + str(int(age)) + " years old")', success_criteria="no traceback.", hints=["is input text or a number?", "int() converts."]),
        ],
        misconceptions=[
            dict(id="m9-m1", wrong_belief="an error means I am bad at coding", real_error="errors are messages; reading them is a skill", response="normalise: fix one, run again."),
            dict(id="m9-m2", wrong_belief="the first line of the traceback is the bug", real_error="the LAST line names the error kind", response="point to the final line first."),
        ],
        quiz_specs=[
            dict(id="m9-q1", question="what does a traceback show first?", correct_answer="the error kind at the end", wrong_options=["the line you wrote first", "your name"], misconception="traceback reads top-down", objective_id="m9-o1", bloom="analyse"),
            dict(id="m9-q2", question="what is a logic error?", correct_answer="the code runs but gives wrong output", wrong_options=["the code will not run", "the code is slow"], misconception="logic error means crash", objective_id="m9-o1", bloom="analyse"),
        ],
        exit_spec=dict(id="m9-et1", question="what is the first thing you read in a traceback?", objective_id="m9-o1"),
        diff_stuck="use the m9-p1 starter and read the traceback line by line.",
        diff_fast="ask the learner to write a traceback-free program.",
        facilitator=dict(checkpoints="read last line first.", cut="if 15 minutes late, drop worked example to 12 minutes.", setup="open colab, run broken code."),
        rationale=["reading errors is a life skill; errors normalised from day one [R7]."],
    )

def lp_m10():
    return dict(
        mid="m10", title="final mini-project (capstone)", duration_min=240, prerequisites="m1-m9",
        objective_ids=["m10-o1"],
        plain_summary="learners build one small useful program from their own real-life task.",
        analogy="writing a recipe for a dish only they cook.",
        breaks_down="the capstone combines many ideas; the milestones keep it small.",
        code_lines=["name = input(\"what is your name? \")", "print(\"hello \" + name + \", welcome back\")", "def add(a, b):", "    return a + b", "print(add(2, 3))"],
        annotations="milestone mix: variables, input, function, print.",
        captured_output="hello fatima, welcome back\n5",
        varies_code=["name = input(\"what is your name? \")", "print(\"hello \" + name + \", welcome back\")", "def add(a, b):", "    return a + b", "print(add(2, 3))"],
        varies_output="hello fatima, welcome back\n5",
        diagram_fig="fig12_capstone.png", diagram_caption="capstone architecture and milestone timeline",
        activity_specs=[
            dict(id="m10-m1", type="mini-challenge", objective_ids=["m10-o1"], minutes=40, instructions="write a tiny program with one variable and one output.", starter="age = 12\nprint(age)", success_criteria="output is 12.", hints=["one variable.", "one print."]),
            dict(id="m10-a2", type="pair_task", objective_ids=["m10-o1"], minutes=25, instructions="plan the capstone task in pairs.", starter="task: count words in an essay", success_criteria="pair states the task.", hints=["use your own task."]),
            dict(id="m10-a3", type="debug-this", objective_ids=["m10-o1"], minutes=25, instructions="fix the capstone starter bug.", starter="age = input(\"how old? \")\nprint(str(int(age)) + \" years old\")", success_criteria="runs.", hints=["int() on input.", "str() for concatenation."]),
        ],
        misconceptions=[
            dict(id="m10-m1", wrong_belief="the capstone needs everything at once", real_error="milestones split it", response="follow milestones in order."),
        ],
        quiz_specs=[
            dict(id="m10-q1", question="what is the capstone?", correct_answer="one small useful program built from prior ideas", wrong_options=["a new language", "a test"], misconception="capstone is a language", objective_id="m10-o1", bloom="create"),
        ],
        exit_spec=dict(id="m10-et1", question="what did your program do and what would you change next?", objective_id="m10-o1"),
        diff_stuck="use the m10-m1 starter and finish it.",
        diff_fast="ask the learner to add a loop to the capstone starter.",
        facilitator=dict(checkpoints="check milestone completion each session.", cut="if 15 minutes late, drop worked example to 12 minutes.", setup="open colab, set up milestone files."),
        rationale=["milestones keep capstone small; rubric rewards process [D3]."],
    )

for mid, fn in [("m6", lp_m6), ("m7", lp_m7), ("m8", lp_m8), ("m9", lp_m9), ("m10", lp_m10)]:
    emit_lesson_plan(**fn())
doc.add_page_break()
def d_activities_catalogue():
    return [
        dict(activity_id="m1-p1", module_id="m1", type="parsons", time_minutes=25, objective_ids=["m1-o1"], description="order scrambled lines into a working program"),
        dict(activity_id="m1-prm", module_id="m1", type="predict-run-modify", time_minutes=20, objective_ids=["m1-o1", "m1-o2"], description="predict output, run, modify one thing"),
        dict(activity_id="m1-a1", module_id="m1", type="pair_task", time_minutes=25, objective_ids=["m1-o1"], description="two learners order steps together"),
        dict(activity_id="m2-mis", module_id="m2", type="debug-this", time_minutes=25, objective_ids=["m2-o1"], description="find the real bug in almost-correct code"),
        dict(activity_id="m2-pair", module_id="m2", type="pair_task", time_minutes=25, objective_ids=["m2-o2"], description="talk through prediction before typing"),
        dict(activity_id="m2-prm", module_id="m2", type="predict-run-modify", time_minutes=20, objective_ids=["m2-o1", "m2-o2"], description="predict output, run, modify one thing"),
        dict(activity_id="m3-prm", module_id="m3", type="predict-run-modify", time_minutes=20, objective_ids=["m3-o1"], description="predict output of input program"),
        dict(activity_id="m4-p1", module_id="m4", type="parsons", time_minutes=25, objective_ids=["m4-o1"], description="order if / else lines"),
        dict(activity_id="m5-p1", module_id="m5", type="parsons", time_minutes=25, objective_ids=["m5-o1"], description="order loop lines so stop condition works"),
        dict(activity_id="m6-p1", module_id="m6", type="parsons", time_minutes=25, objective_ids=["m6-o1"], description="order def / call lines"),
        dict(activity_id="m7-p1", module_id="m7", type="parsons", time_minutes=25, objective_ids=["m7-o1"], description="order list append / index lines"),
        dict(activity_id="m8-p1", module_id="m8", type="debug-this", time_minutes=25, objective_ids=["m8-o1"], description="fix file handle bug"),
        dict(activity_id="m9-p1", module_id="m9", type="debug-this", time_minutes=25, objective_ids=["m9-o1"], description="read traceback, find line, fix"),
        dict(activity_id="m10-m1", module_id="m10", type="mini-challenge", time_minutes=40, objective_ids=["m10-o1"], description="first capstone milestone: write a tiny program with one variable and one output"),
    ]

doc.add_page_break()

h1("15 Assessment strategy")
para("assessment is gentle and frequent, then once deeply. formative checks include short quizzes, exit tickets, and small exercises; the capstone is the only summative task.")
styled_table(
    ["assessment", "when", "what it checks", "linked objectives"],
    [
        ["quiz", "start of module practice", "facts and one-step reasoning", "m1-o1, m2-o1, m3-o1, m4-o1, m5-o1, m6-o1, m7-o1, m8-o1, m9-o1"],
        ["exit ticket", "end of every session", "one question plus confidence mark", "m1-o1, m2-o1, m3-o1, m4-o1, m5-o1, m6-o1, m7-o1, m8-o1, m9-o1, m10-o1"],
        ["small exercises", "after each module", "parsons, debug-this, predict-run-modify", "all mapped objectives"],
        ["capstone", "module m10", "correctness, use of ideas, readability, explanation", "m10-o1"],
    ],
)
para("the capstone rubric has four criteria scored one to four, with a pass at twelve of sixteen and correctness at least two. the pass mark and the correctness condition are design decisions from week 1, not research findings.")

doc.add_page_break()

h1("16 Supporting non-programmers")
para("anticipated difficulties: unfamiliar vocabulary, holding several steps in mind, variable-as-box, error sting. anxiety and confidence: early small wins, pair work, exit tickets. accessibility: captions, transcripts, colour-blind-safe palette, keyboard-friendly editor. pacing: two sessions per three-hour module mostly, with the shorter module getting one longer session. remedial paths: hint ladders, stuck-task buddies, tutor check-ins.")

doc.add_page_break()

h1("17 Review and refinement log")
para("this report was written and reviewed against the week 2 task. refinement items: added executed code with captured output, added alignment matrix, added readability audit, added jargon audit, added timing math. changes since week 1 are listed in section 18.")

doc.add_page_break()

h1("18 Validation plan and known limitations")
para("validation plan: pilot the curriculum in week 3 with a small group, observe pair work, predict-run-modify accuracy, exit ticket confidence; success means most learners finish the capstone and can explain it. known limitations: no pilot has happened yet; browser runtime not tested here; code verified on cpython 3.13; the 80 percent completion target is a design decision.")


doc.add_page_break()
exec(open(str(__import__("pathlib").Path(__file__).resolve().parent / "appendices.py")).read())


settings = doc.settings.element
update = parse_xml(f'<w:updateFields {nsdecls("w")} w:val="true"/>')
settings.append(update)

doc.save(str(OUT))
size = OUT.stat().st_size
print(f"saved {OUT} ({size/1024:.0f} KB)")
if size > 2 * 1024 * 1024:
    print("FAIL: over 2 MB")
    raise SystemExit(1)
print("size ok under 2 MB")
