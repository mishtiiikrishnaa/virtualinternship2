## virtualinternship2
one repository for the four-week virtual programming fundamentals internship in ahmedabad. the internship runs from 2 november to 30 november 2026. this week 1 task was offered on 2 november 2026 and the report was prepared on 4 november 2026.

this repo holds the week one project plan, the scope definition, and everything needed to rebuild it. later weeks will live in their own folders when their tasks are announced. i am not inventing weeks 2 to 4 here.

## weeks
| week | focus | status |
|---|---|---|
| 1 | project planning and scope definition | ready to submit |
| 2 | not started (focus added when announced) | not started |
| 3 | not started (focus added when announced) | not started |
| 4 | not started (focus added when announced) | not started |

week 1 deliverable: `weeks/week1/reports/Project_Plan_Scope_Definition_Week1.docx` — a full plan for a 30 hour programming fundamentals module for non-programmers, with a real table of contents, tables, and six diagrams. it is meant to be read by non-technical people.

## layout
```
virtualinternship2/
  README.md
  Makefile
  .gitignore
  weeks/
    week1/
      README.md
      requirements.txt
      docs/            research register, assumptions and decisions
      figures/         six png diagrams
      src/             figure generator, docx builder
      reports/         the docx (and pdf preview)
      tests/           validation tests
```

## run week 1
```sh
pip install -r weeks/week1/requirements.txt
make week1
make check
```
`make week1` rebuilds the figures and the docx. `make check` runs the tests that verify size, word count, headings, images, captions, dates, and the outcome mapping.

## why one repository
the four weeks belong together. they share the same cohort of learners, the same planning language, and the same design decisions. keeping them in one repo makes that link clear and lets later weeks build on week 1 without copying files around. when a new week is announced it will get its own folder here, and nothing will overwrite an earlier week.

this repository was drafted with ai assistance and reviewed by me.

thanks for reading. mishti.
