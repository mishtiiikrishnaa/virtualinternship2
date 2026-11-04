<a id="readme-top"></a>

[![Contributors](https://img.shields.io/github/contributors/mishtiiikrishnaa/virtualinternship2.svg?style=for-the-badge)](https://github.com/mishtiiikrishnaa/virtualinternship2/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/mishtiiikrishnaa/virtualinternship2.svg?style=for-the-badge)](https://github.com/mishtiiikrishnaa/virtualinternship2/network/members)
[![Stargazers](https://img.shields.io/github/stars/mishtiiikrishnaa/virtualinternship2.svg?style=for-the-badge)](https://github.com/mishtiiikrishnaa/virtualinternship2/stargazers)
[![Issues](https://img.shields.io/github/issues/mishtiiikrishnaa/virtualinternship2.svg?style=for-the-badge)](https://github.com/mishtiiikrishnaa/virtualinternship2/issues)
[![Python](https://img.shields.io/badge/python-3.13-blue?style=for-the-badge)](https://www.python.org/)
[![Report](https://img.shields.io/badge/report-~6%2C734%20words%20%7C%20348%20KB%20%7C%20docx%20%7C%20word-orange?style=for-the-badge)](reports/Project_Plan_Scope_Definition_Week1.docx)

### week 1 — project planning and scope definition

this folder holds the week one project plan for a programming fundamentals module for non-programmers. it is meant to be read by someone who has never coded, so the language is plain and every jargon term is explained.

[**Explore the docs »**](#usage) · [View the Report](reports/Project_Plan_Scope_Definition_Week1.docx) · [Report Bug](https://github.com/mishtiiikrishnaa/virtualinternship2/issues/new) · [Request Feature](https://github.com/mishtiiikrishnaa/virtualinternship2/issues/new)

## table of contents

- [about the project](#about-the-project)
- [the module in 5 lines](#the-module-in-5-lines)
- [built with](#built-with)
- [getting started](#getting-started)
- [usage](#usage)
- [layout](#layout)
- [roadmap](#roadmap)
- [honest limitations](#honest-limitations)
- [contributing](#contributing)
- [license](#license)
- [contact](#contact)

## about the project

[![week 1 docx](https://img.shields.io/badge/report-docx%20%7C%20tables%20%7C%20toc%20%7C%206%20figures-%231F4E5F?style=for-the-badge)](reports/Project_Plan_Scope_Definition_Week1.docx)

many great readme templates exist. this one follows [othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template). what changed is the shape of the content: it is a rebuild guide for a single internship week.

here is why the folder is organised this way:

- the report should be reproducible from scripts, not hand-edited after generation
- figures and tests should live beside the report they support
- a clean clone should behave the same as this one

([back to top](#readme-top))

## the module in 5 lines

python, in the browser, no installs.

10 modules, 30 teaching hours, for adults or students who have never coded.

thinks in steps in modules 1-3, chooses and repeats in 4-5, groups steps in 6, organises data in 7, uses files in 8, reads errors in 9, builds a mini-project in 10.

worked examples, parsons problems, pair work, and predict-run-modify tasks throughout.

short quizzes, exit tickets, small exercises, and a capstone rubric.

([back to top](#readme-top))

## built with

- [![Python](https://img.shields.io/badge/python-3.13-3776AB?style=flat-square)](https://www.python.org/)
- [![python-docx](https://img.shields.io/badge/python--docx%201.2%20%7C%20docx%20build-4B0082?style=flat-square)](https://python-docx.readthedocs.io/)
- [![matplotlib](https://img.shields.io/badge/matplotlib%20%7C%20figures-11557f?style=flat-square)](https://matplotlib.org/)
- [![pytest](https://img.shields.io/badge/pytest%20%7C%20checks-0A9EDC?style=flat-square)](https://docs.pytest.org/)
- [![LibreOffice](https://img.shields.io/badge/libreoffice%20%7C%20pdf%20preview-18A303?style=flat-square)](https://www.libreoffice.org/)

([back to top](#readme-top))

## getting started

### prerequisites

- python 3.10 or newer
- pip
- git
- libreoffice (optional, for the pdf preview only)

```sh
python3 --version
```

### installation

1. clone the repo (from the project root)

```sh
git clone git@github.com:mishtiiikrishnaa/virtualinternship2.git
cd virtualinternship2
```

2. install the python dependencies

```sh
pip install -r weeks/week1/requirements.txt
```

3. build the figures and the report

```sh
make week1
```

4. run the checks

```sh
make check
```

([back to top](#readme-top))

## usage

- open `weeks/week1/reports/Project_Plan_Scope_Definition_Week1.docx` in microsoft word
- use the table of contents field at the start of the document to jump between sections
- read the pdf preview at `weeks/week1/reports/Project_Plan_Scope_Definition_Week1.pdf` for a quick visual check

for the research notes behind the plan, see `weeks/week1/docs/research_register.md`. for the assumptions and decisions, see `weeks/week1/docs/assumptions_and_decisions.md`. the 275 word submission text is in `weeks/week1/docs/submission_text.txt`.

([back to top](#readme-top))

## layout

```
week1/
  README.md
  requirements.txt
  docs/            research register, assumptions and decisions, submission text
  figures/         six png diagrams
  src/             make_figures.py, build_docx.py
  reports/         the docx (and pdf preview)
  tests/           test_docx.py (pytest)
```

([back to top](#readme-top))

## roadmap

- [x] week 1: project planning and scope definition
  - add changelog
  - keep dates honest (planned baseline 5 november 2026)
  - keep docx under 2 mb
- [ ] week 2: not started (focus added when announced)
- [ ] week 3: not started (focus added when announced)
- [ ] week 4: not started (focus added when announced)

([back to top](#readme-top))

## honest limitations

- timeline dates in section 9 are planned, not done. baseline is 5 november 2026 (planned), first working day after the report date. they skip weekends and the 25 november 2026 holiday.
- references are public sources found on 4 november 2026. where i only saw an abstract i marked the entry to check before citing.
- effort is 120 planned hours matching the resource table. it is a planning figure, not a quote.
- the docx toc is a live word field. open in word and choose update field to get page numbers in the toc itself.

([back to top](#readme-top))

## contributing

this is a solo internship repo. if you find a mistake, please open an issue with the tag "enhancement" or "bug" and i will look at it.

1. fork the project
2. create your feature branch (`git checkout -b feature/AmazingFeature`)
3. commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. push to the branch (`git push origin feature/AmazingFeature`)
5. open a pull request

([back to top](#readme-top))

## license

no license file is included in this repository. it is for internship submission and review only. please ask before reusing the text or figures.

([back to top](#readme-top))

## contact

mishti krishna - [github @mishtiiikrishnaa](https://github.com/mishtiiikrishnaa)

project link: [https://github.com/mishtiiikrishnaa/virtualinternship2](https://github.com/mishtiiikrishnaa/virtualinternship2)

this repository was drafted with ai assistance and reviewed by me.

thanks for reading. mishti.

([back to top](#readme-top))
