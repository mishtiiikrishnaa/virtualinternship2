.PHONY: week1 week2 check
week1:
	python3 weeks/week1/src/make_figures.py
	python3 weeks/week1/src/build_docx.py
	@if command -v soffice >/dev/null 2>&1; then soffice --headless --convert-to pdf --outdir weeks/week1/reports weeks/week1/reports/Project_Plan_Scope_Definition_Week1.docx; else echo "libreoffice not found, skipping pdf preview"; fi
	@ls -lh weeks/week1/reports/

week2:
	python3 weeks/week2/src/make_figures.py
	python3 weeks/week2/src/build_docx.py
	@if command -v soffice >/dev/null 2>&1; then soffice --headless --convert-to pdf --outdir weeks/week2/reports weeks/week2/reports/Curriculum_Lesson_Plans_Week2.docx; else echo "libreoffice not found, skipping pdf preview"; fi
	@ls -lh weeks/week2/reports/

check:
	python3 -m pytest weeks/week1/tests/ weeks/week2/tests/ -q
