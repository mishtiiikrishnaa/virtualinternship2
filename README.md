<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Python][python-shield]][python-url]
[![License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/mishtiiikrishnaa/virtualinternship2">
    <img src="weeks/week1/figures/fig2_learner_journey.png" alt="Learner journey from never coded to built something" width="640" height="228">
  </a>

<h3 align="center">Virtual Programming Fundamentals Internship — Project Plan and Scope Definition</h3>

  <p align="center">
    A week 1 project plan for a programming fundamentals module for non-programmers — written for people who have never written a line of code.
    <br />
    <a href="#usage"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="weeks/week1/reports/Project_Plan_Scope_Definition_Week1.docx">View the Week 1 Report</a>
    &middot;
    <a href="https://github.com/mishtiiikrishnaa/virtualinternship2/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/mishtiiikrishnaa/virtualinternship2/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#weeks">Weeks</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#layout">Layout</a></li>
    <li><a href="#why-one-repository">Why One Repository</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Curriculum structure — 10 modules building to a capstone][product-screenshot]]

One repository for the four-week Virtual Programming Fundamentals Internship in Ahmedabad. The internship runs from 2 to 30 November 2026; this Week 1 report was prepared on 4 November 2026.

This repo holds the Week 1 project plan and scope definition for a programming fundamentals module for non-programmers, plus everything needed to rebuild it. Weeks 2 to 4 will get their own folders when their tasks are announced.

<!-- Weeks -->
### Weeks

| Week | Focus | Status |
|---|---|---|
| 1 | Project planning and scope definition | Ready to submit |
| 2 | Not started (focus added when announced) | Not started |
| 3 | Not started (focus added when announced) | Not started |
| 4 | Not started (focus added when announced) | Not started |

Week 1 deliverable: `weeks/week1/reports/Project_Plan_Scope_Definition_Week1.docx` — a full plan for a 30-hour programming fundamentals module for non-programmers, with a real table of contents field, tables, and six diagrams. There is also a PDF preview in the same folder.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- BUILT WITH -->
### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgments section. Here are a few examples.

* [![Python][Python.js]][Python-url]
* [![python-docx][python-docx.js]][python-docx-url]
* [![matplotlib][matplotlib.js]][matplotlib-url]
* [![pytest][pytest.js]][pytest-url]
* [![LibreOffice][LibreOffice.js]][LibreOffice-url]
* [![GitHub][GitHub.js]][GitHub-url]
* [![Google Colab][Colab.js]][Colab-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally. To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

* python 3.10 or newer

  ```sh
  python3 --version
  ```

* pip

  ```sh
  pip3 --version
  ```

* git

  ```sh
  git --version
  ```

* libreoffice (optional — only for the PDF preview)

  ```sh
  soffice --version
  ```

### Installation

1. Clone the repo

   ```sh
   git clone git@github.com:mishtiiikrishnaa/virtualinternship2.git
   cd virtualinternship2
   ```

2. Install Python dependencies

   ```sh
   pip install -r weeks/week1/requirements.txt
   ```

3. Build the figures and the report

   ```sh
   make week1
   ```

4. Run the checks

   ```sh
   make check
   ```

5. Change git remote url to avoid accidental pushes to base project

   ```sh
   git remote set-url origin git@github.com:mishtiiikrishnaa/virtualinternship2.git
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

* Open `weeks/week1/reports/Project_Plan_Scope_Definition_Week1.docx` in Microsoft Word. Use the table of contents field at the start of the document to jump between sections (right-click → Update Field if the numbers need refreshing).
* Read the PDF preview at `weeks/week1/reports/Project_Plan_Scope_Definition_Week1.pdf` for a quick visual check of the figures and tables.
* For what each module covers and how the plan is structured, see [weeks/week1/README.md](weeks/week1/README.md).

_For more examples, please refer to the [Documentation](weeks/week1/README.md)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LAYOUT -->
## Layout

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

Weeks 2 to 4 get their own folders only when their tasks are released. Nothing from a later week overwrites an earlier one.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- WHY ONE REPOSITORY -->
## Why One Repository

The four weeks belong together. They share the same cohort of learners, the same planning language, and the same design decisions. Keeping them in one repo makes that link clear and lets later weeks build on Week 1 without copying files around. When a new week is announced it will get its own folder here, and nothing will overwrite an earlier week.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Week 1: Project planning and scope definition
  - Add CHANGELOG
  - Keep dates honest (planned baseline 5 November 2026, all Section 9 dates labelled planned)
  - Keep the .docx under 2 MB
- [ ] Week 2: Not started (focus added when announced)
- [ ] Week 3: Not started (focus added when announced)
- [ ] Week 4: Not started (focus added when announced)

See the [open issues](https://github.com/mishtiiikrishnaa/virtualinternship2/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

This is a solo internship repo, so contributions are not open in the usual sense. If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/mishtiiikrishnaa/virtualinternship2/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=mishtiiikrishnaa/virtualinternship2" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

No license file is included in this repository. It is for internship submission and review only. Please ask before reusing the text or figures.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Best-README-Template by othneildrew](https://github.com/othneildrew/Best-README-Template) for the README structure and badges
* [Harvard CS50x](https://cs50.harvard.edu/x/), [Python for Everybody](https://www.py4e.com/), [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/2e/), [Code.org](https://code.org/en-US/curriculum/computer-science-fundamentals) for public beginner course structures
* [MIT Teaching and Learning Lab](https://tll.mit.edu/teaching-resources/how-people-learn/worked-examples/) and [Raspberry Pi Foundation](https://www.raspberrypi.org/blog/supporting-learners-with-programming-tasks-through-ai-generated-parsons-problems/) for worked examples and Parsons problems
* [Shields.io](https://shields.io) for the badges
* [Choose an Open Source License](https://choosealicense.com)

This repository was drafted with AI assistance and reviewed by me.

Thanks for reading. Mishti.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/mishtiiikrishnaa/virtualinternship2.svg?style=for-the-badge
[contributors-url]: https://github.com/mishtiiikrishnaa/virtualinternship2/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/mishtiiikrishnaa/virtualinternship2.svg?style=for-the-badge
[forks-url]: https://github.com/mishtiiikrishnaa/virtualinternship2/network/members
[stars-shield]: https://img.shields.io/github/stars/mishtiiikrishnaa/virtualinternship2.svg?style=for-the-badge
[stars-url]: https://github.com/mishtiiikrishnaa/virtualinternship2/stargazers
[issues-shield]: https://img.shields.io/github/issues/mishtiiikrishnaa/virtualinternship2.svg?style=for-the-badge
[issues-url]: https://github.com/mishtiiikrishnaa/virtualinternship2/issues
[license-shield]: https://img.shields.io/badge/license-none-red.svg?style=for-the-badge
[license-url]: #license
[python-shield]: https://img.shields.io/badge/python-3.13-blue.svg?style=for-the-badge
[python-url]: https://www.python.org/
[product-screenshot]: weeks/week1/figures/fig1_curriculum_structure.png
<!-- Shields.io badges. You can a comprehensive list with many more badges at: https://github.com/inttter/md-badges -->
[Python.js]: https://img.shields.io/badge/python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[python-docx.js]: https://img.shields.io/badge/python--docx-4B0082?style=for-the-badge
[python-docx-url]: https://python-docx.readthedocs.io/
[matplotlib.js]: https://img.shields.io/badge/matplotlib-11557f?style=for-the-badge
[matplotlib-url]: https://matplotlib.org/
[pytest.js]: https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white
[pytest-url]: https://docs.pytest.org/
[LibreOffice.js]: https://img.shields.io/badge/libreoffice-18A303?style=for-the-badge&logo=libreoffice&logoColor=white
[LibreOffice-url]: https://www.libreoffice.org/
[GitHub.js]: https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white
[GitHub-url]: https://github.com/
[Colab.js]: https://img.shields.io/badge/google%20colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=black
[Colab-url]: https://colab.research.google.com/
