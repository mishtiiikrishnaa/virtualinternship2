<a id="readme-top"></a>

[![Contributors](https://img.shields.io/github/contributors/mishtiiikrishnaa/virtualinternship2.svg?style=for-the-badge)](https://github.com/mishtiiikrishnaa/virtualinternship2/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/mishtiiikrishnaa/virtualinternship2.svg?style=for-the-badge)](https://github.com/mishtiiikrishnaa/virtualinternship2/network/members)
[![Stargazers](https://img.shields.io/github/stars/mishtiiikrishnaa/virtualinternship2.svg?style=for-the-badge)](https://github.com/mishtiiikrishnaa/virtualinternship2/stargazers)
[![Issues](https://img.shields.io/github/issues/mishtiiikrishnaa/virtualinternship2.svg?style=for-the-badge)](https://github.com/mishtiiikrishnaa/virtualinternship2/issues)
[![Python](https://img.shields.io/badge/python-3.13-blue?style=for-the-badge)](https://www.python.org/)
[![License: none](https://img.shields.io/badge/license-none-red?style=for-the-badge)](#license)

### virtualinternship2

one repository for the four-week virtual programming fundamentals internship in ahmedabad. the internship runs from 2 november to 30 november 2026. the offer was received on 2 november 2026 and the week 1 report was prepared on 4 november 2026.

this repo holds the week one project plan and scope definition for a programming fundamentals module for non-programmers, plus everything needed to rebuild it. weeks 2 to 4 will get their own folders when their tasks are announced. i have not invented them here.

[**Explore the docs »**](#usage) · [View Week 1 Report](#usage) · [Report Bug](https://github.com/mishtiiikrishnaa/virtualinternship2/issues/new) · [Request Feature](https://github.com/mishtiiikrishnaa/virtualinternship2/issues/new)

## table of contents

- [about the project](#about-the-project)
- [weeks](#weeks)
- [built with](#built-with)
- [getting started](#getting-started)
- [usage](#usage)
- [layout](#layout)
- [roadmap](#roadmap)
- [why one repository](#why-one-repository)
- [contributing](#contributing)
- [license](#license)
- [contact](#contact)
- [acknowledgments](#acknowledgments)

## about the project

[![week 1 docx](https://img.shields.io/badge/report-week%201%20docx%20%7C%20~6%2C734%20words%20%7C%20348%20KB%20%7C%20word%20%7C%20docx-orange?style=for-the-badge)](weeks/week1/reports/Project_Plan_Scope_Definition_Week1.docx)

many great readme templates exist on github. this one follows [othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template) because it is clear and familiar. the project underneath it is simpler: a week 1 plan written for people who have never coded.

here is why the plan is organised this way:

- your time should go into learning and teaching, not into assembling a report from scratch
- non-programmers should not need to ask what a word means halfway through a document
- planning documents should show milestones and resources, not just good intentions

of course, no single template fits every project. i have kept the factual structure of this internship repo (weeks table, layout, run commands) and dressed it in the template style so it is easy to navigate and easy to rebuild.

([back to top](#readme-top))

## weeks

| week | focus | status |
|---|---|---|
| 1 | project planning and scope definition | ready to submit |
| 2 | not started (focus added when announced) | not started |
| 3 | not started (focus added when announced) | not started |
| 4 | not started (focus added when announced) | not started |

week 1 deliverable: `weeks/week1/reports/Project_Plan_Scope_Definition_Week1.docx` — a full plan for a 30 hour programming fundamentals module for non-programmers, with a real table of contents field, tables, and six diagrams. there is also a pdf preview in the same folder.

([back to top](#readme-top))

## built with

this section lists the major tools used to build the week 1 report. smaller helpers are listed under acknowledgments.

- [![Python](https://img.shields.io/badge/python-3.13-3776AB?style=flat-square)](https://www.python.org/)
- [![python-docx](https://img.shields.io/badge/python--docx%201.2%20%7C%20docx%20build-4B0082?style=flat-square)](https://python-docx.readthedocs.io/)
- [![matplotlib](https://img.shields.io/badge/matplotlib%20%7C%20figures-11557f?style=flat-square)](https://matplotlib.org/)
- [![pytest](https://img.shields.io/badge/pytest%20%7C%20checks-0A9EDC?style=flat-square)](https://docs.pytest.org/)
- [![LibreOffice](https://img.shields.io/badge/libreoffice%20%7C%20pdf%20preview-18A303?style=flat-square)](https://www.libreoffice.org/)
- [![GitHub](https://img.shields.io/badge/github-181717?style=flat-square)](https://github.com/)
- [![Google Colab](https://img.shields.io/badge/google%20colab%20%7C%20browser%20editor-F9AB00?style=flat-square)](https://colab.research.google.com/)

([back to top](#readme-top))

## getting started

this is how you rebuild the week 1 report from a clean clone. the commands work from the repository root.

### prerequisites

you need python and pip. libreoffice is optional, it is only used for the pdf preview and for checking that the table of contents renders.

- python 3.10 or newer
- pip
- git

```sh
python3 --version
pip3 --version
```

### installation

1. clone the repo

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

4. change git remote url to avoid accidental pushes to the wrong place

```sh
git remote set-url origin git@github.com:mishtiiikrishnaa/virtualinternship2.git
git remote -v # confirm the changes
```

([back to top](#readme-top))

## usage

use this section to open and check the report.

- open `weeks/week1/reports/Project_Plan_Scope_Definition_Week1.docx` in microsoft word
- use the table of contents field at the start of the document to jump between sections (right-click, update field, if page numbers need refreshing)
- read the pdf preview at `weeks/week1/reports/Project_Plan_Scope_Definition_Week1.pdf` for a quick visual check of figures and tables

for what each module covers and how the plan is structured, see [weeks/week1/README.md](weeks/week1/README.md).

([back to top](#readme-top))

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

weeks 2 to 4 get their own folders only when their tasks are released. nothing from a later week overwrites an earlier one.

([back to top](#readme-top))

## roadmap

- [x] week 1: project planning and scope definition
  - add changelog
  - keep dates honest (planned baseline 5 november 2026, all section 9 dates labelled planned)
  - keep docx under 2 mb
- [ ] week 2: not started (focus added when announced)
- [ ] week 3: not started (focus added when announced)
- [ ] week 4: not started (focus added when announced)

see the [open issues](https://github.com/mishtiiikrishnaa/virtualinternship2/issues) for a full list of proposed features and known issues.

([back to top](#readme-top))

## why one repository

the four weeks belong together. they share the same cohort of learners, the same planning language, and the same design decisions. keeping them in one repo makes that link clear and lets later weeks build on week 1 without copying files around. when a new week is announced it will get its own folder here, and nothing will overwrite an earlier week.

([back to top](#readme-top))

## contributing

this is a solo internship repo, so contributions are not open in the usual sense. if you find a mistake, please open an issue with the tag "enhancement" or "bug" and i will look at it. the usual open source steps are still a useful starting point if you fork it for your own internship:

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

([back to top](#readme-top))

## acknowledgments

use this space to credit the people and tools that made the report possible.

- [othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template) for the readme structure and badges. thanks.
- [harvard cs50x](https://cs50.harvard.edu/x/), [python for everybody](https://www.py4e.com/), [automate the boring stuff with python](https://automatetheboringstuff.com/2e/), [code.org](https://code.org/en-US/curriculum/computer-science-fundamentals) for public beginner course structures
- [mit teaching and learning lab](https://tll.mit.edu/teaching-resources/how-people-learn/worked-examples/) and [raspberry pi foundation](https://www.raspberrypi.org/blog/supporting-learners-with-programming-tasks-through-ai-generated-parsons-problems/) for worked examples and parsons problems
- [shields.io](https://shields.io) for the badges
- [choose an open source license](https://choosealicense.com) for the license note

this repository was drafted with ai assistance and reviewed by me.

thanks for reading. mishti.

([back to top](#readme-top))
