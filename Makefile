.PHONY: week1 check
week1:
	python3 weeks/week1/src/make_figures.py
	python3 weeks/week1/src/build_docx.py
	@if command -v soffice >/dev/null 2>&1; then soffice --headless --convert-to pdf --outdir weeks/week1/reports weeks/week1/reports/Project_Plan_Scope_Definition_Week1.docx; else echo "libreoffice not found, skipping pdf preview"; fi
	@ls -lh weeks/week1/reports/

check:
	python3 -m pytest weeks/week1/tests/ -q
