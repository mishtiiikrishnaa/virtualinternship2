## what this week produced
a full project plan for a programming fundamentals module for non-programmers. it is meant to be read by someone who has never coded, so the language is plain and every jargon term is explained.

the deliverable is `weeks/week1/reports/Project_Plan_Scope_Definition_Week1.docx` (about 348 kb, well under the 2 mb limit). it has a real table of contents field, headings, tables, and six diagrams. there is also a pdf preview made by libreoffice in the same folder.

## the module in 5 lines
python, in the browser, no installs.
10 modules, 30 teaching hours, for adults or students who have never coded.
thinks in steps in modules 1-3, chooses and repeats in 4-5, groups steps in 6, organises data in 7, uses files in 8, reads errors in 9, builds a mini-project in 10.
worked examples, parsons problems, pair work, and predict-run-modify tasks throughout.
short quizzes, exit tickets, small exercises, and a capstone rubric.

## rebuild it yourself
```sh
pip install -r weeks/week1/requirements.txt
make week1
make check
```
`make week1` rebuilds the figures and the docx and tries to make a pdf preview. `make check` runs the pytest suite.

## file tree
```
week1/
  README.md
  requirements.txt
  docs/            research register, assumptions and decisions
  figures/         six png diagrams
  src/             make_figures.py, build_docx.py
  reports/         the docx (and pdf preview)
  tests/           test_docx.py (pytest)
```

## honest limitations
- timeline dates in section 9 are planned, not done. baseline is 5 november 2026 (planned), first working day after the report date. they skip weekends and the 25 november 2026 holiday.
- references are public sources found on 4 november 2026. where i only saw an abstract i marked the entry to check before citing.
- effort is 120 planned hours matching the resource table. it is a planning figure, not a quote.
- the docx toc is a live word field. open in word and choose update field to get page numbers in the toc itself.

this repository was drafted with ai assistance and reviewed by me.

thanks for reading. mishti.
