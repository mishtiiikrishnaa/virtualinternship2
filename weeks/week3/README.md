# Week 3 - Interactive Learning Module

## About
Browser-based interactive module teaching programming fundamentals.

## Layout
```
app/        HTML, CSS, JS application
figures/    diagrams and screenshots
src/        build scripts
reports/    docx and pdf
tests/      test files
docs/       submission text
assessment/ answer keys
```

## Run locally
```
cd weeks/week3/app
python3 -m http.server 8000
```
Open http://localhost:8000

## Deploy
Suitable for GitHub Pages. Point Pages to repository root; open /weeks/week3/app/.

## Build report
```
python3 src/make_figures.py
python3 src/build_docx.py
```
