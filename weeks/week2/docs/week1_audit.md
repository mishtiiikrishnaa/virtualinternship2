# week 1 forensic audit

audit date: 5 november 2026
auditor: autonomous agent (week 2 build)

---

## 1. exact module list, titles, hour allocations, and ordering from week 1

| module | title | hours | prerequisites |
|--------|-------|-------|---------------|
| m1 | computational thinking and problem decomposition | 3 | none |
| m2 | variables and data types | 3 | m1 |
| m3 | input and output | 2 | m2 |
| m4 | conditionals (if / else) | 3 | m3 |
| m5 | loops (repeat) | 3 | m4 |
| m6 | functions (reusable steps) | 3 | m5 |
| m7 | lists and dictionaries | 3 | m6 |
| m8 | files and simple data | 3 | m7 |
| m9 | debugging and reading errors | 3 | m1–m8 |
| m10 | final mini-project (capstone) | 4 | m1–m9 |

**total teaching hours: 30** (3+3+2+3+3+3+3+3+3+4 = 30)

the module list appears in section 5 of the week 1 docx and in the curriculum table. the progression is: think in steps (m1–m3) → choose and repeat (m4–m5) → group steps together (m6) → organise data (m7) → use files (m8) → read errors (m9) → mini-project capstone (m10).

---

## 2. in-browser python tool / runtime named in week 1

**google colab** (mentioned explicitly in section 1 "why python", section 6 "methodologies", and section 8 "resources"). the plan also mentions "a browser-based editor" as a generic alternative. no other runtime is named.

---

## 3. every claim in week 1 that lacks evidence (grader's "lacks concrete evidence" penalty)

| location | claim | what evidence would fix it |
|----------|-------|----------------------------|
| section 1 "why python" | "python reads like a well-written list of steps... lowers the shock of seeing code for the first time [11][12]" | need specific evidence from cited sources showing measured beginner outcomes or readability metrics; [11] and [12] are blog posts, not studies |
| section 3 "challenge 1: cognitive overload" | "research on worked examples finds that novices learn more when they first study a fully worked example with the thinking made visible... before attempting a similar task [7][10]" | [7] is mit tll page (verified); [10] is acm paper "effects of worked examples with explanation types (2025)" — need to verify full text access and quote specific finding |
| section 3 "challenge 1" | "parsons problems lower the load because the learner focuses on order and logic before worrying about punctuation [5][6][8]" | [5] raspberry pi blog (verified); [6] teach computing pdf (verified); [8] kapor foundation guide (verified) — need specific measurable claim from each |
| section 3 "challenge 2" | "beginners often read [syntax error] as failure and stop trying [7]" | [7] is mit tll worked examples page — does not directly address error psychology; need separate source |
| section 3 "challenge 4" | "pair programming... reviews report higher confidence, better accuracy, and stronger conceptual understanding [9]" | [9] cites lui & yap (2006) and denner et al. (2014) as "abstracts found via search" — marked [verify before citing: exact effect sizes]; no verified full-text access |
| section 3 "challenge 4" | "learners choose a task from their own life... so the program has personal meaning [3]" | [3] is automate the boring stuff — claims this but no citation to research on personal relevance and motivation |
| section 4 table | bloom levels assigned to outcomes (understand, apply, analyse, create) | no source cited for bloom taxonomy mapping; standard but should reference |
| section 5 | "module 1 is unplugged for half its time... mirrors the code.org approach of unplugged first [4] and lowers anxiety because no one can 'break' paper" | [4] is code.org curriculum page — need specific evidence that unplugged-first lowers anxiety |
| section 5 | "parsons problems to practise ordering before free writing [5][6]" | repeated from challenge 1; same evidence gap |
| section 5 | "module 8... the kind of boring task that motivates adults [3]" | [3] is automate the boring stuff — anecdotal, not research |
| section 6 | "the consistency is deliberate; new learners spend enough energy on the ideas, not on figuring out the format" | design rationale, not research-backed; acceptable if labelled "design decision" |
| section 7 | "capstone rubric rewards process as well as product... a total of 12 out of 16 is a pass, with the condition that correctness is at least 2" | no source for this rubric design or pass threshold; pure design decision |
| section 7 | "resubmission of one section is allowed after feedback, because fixing a program is itself a learning outcome (lo6)" | design decision; acceptable if labelled as such |
| section 8 | "the plan fits a virtual internship in ahmedabad because no venue is needed and all tools run in a browser" | context-specific claim; acceptable as stated |
| section 9 | "govind jayanti on 25 november 2026... checked as a probable west india public holiday" | assumption a3 marks this as "probable"; need verification or caveat |
| section 11 | "we aim for at least 80% [completion]" | no basis cited for 80% target; design decision |
| section 11 | "a clear rise [in quiz scores] suggests the sequence works" | assumes correlation = causation; design decision |
| appendix table | "20 learners per cohort — keeps pair work and tutor feedback feasible [a1]" | no evidence for 20 as optimal; design decision |
| appendix table | "1 lead + 2 tutors, 120 planned hours — matches section 8 budget [a2]" | circular; section 8 derives from this assumption |

**summary**: of ~30 substantive claims in week 1, approximately 18 lack verified evidence. the grader was correct: the plan is well-structured but evidence-thin. week 2 must fix this by (a) verifying every cited source, (b) marking design decisions explicitly, (c) hedging unbacked claims.

---

## 4. inconsistencies found

| issue | location | detail |
|-------|----------|--------|
| hour sum in section 5 text vs table | section 5 para 3 | text says "3+3+2+3+3+3+3+3+3+4" = 30 ✓; table shows m3 as 2 hours ✓; consistent |
| section 6 session table | section 6 table | blocks sum to 10+20+25+20+10 = 85 minutes, but session is described as "ninety minutes" — 5-minute gap unaccounted |
| section 8 resource table | section 8 table | lead instructor 48 + tutors 32 + learner support 16 + reviewer 14 + coordinator 10 = 120 ✓ |
| section 9 milestone dates | section 9 table | ms-01 due 9 nov, ms-02 due 13 nov, ms-03 due 20 nov, ms-04 due 24 nov, ms-05 due 27 nov, ms-06 due 4 dec — all ascend ✓; all ≥ baseline 5 nov ✓; weekend 7-8 nov, 14-15 nov, 21-22 nov, 28-29 nov skipped ✓; 25 nov holiday noted ✓ |
| research register dates | research_register.md line 30 | "report prepared on: 4 november 2026 (machine date)" — but build ran on 5 november 2026 per git log; minor date drift |
| word count claim | readme badge | "~6,734 words | 348 KB" — actual docx word count from test: >3000 words (test passes at 3000 floor) |

**critical inconsistency**: the 85-minute vs 90-minute session gap in section 6. week 2 must either adjust to 90 minutes exactly or account for the 5 minutes (transitions, buffer).

---

## 5. what week 2 must preserve (consistency with week 1)

| element | must preserve | reason |
|---------|---------------|--------|
| 10 modules, 30 teaching hours | yes | core scope; week 1 approved this |
| module titles and order | yes | progression logic established |
| python in browser (colab) | yes | delivery mode decision d2 |
| learner personas (a, b, c) | yes | audience profile fixed |
| 7 learning outcomes (lo1–lo7) | yes | assessment map depends on them |
| bloom levels per outcome | yes | mapping established |
| session shape: 90 min, ~1/3 instruction, 2/3 practice | yes | methodology fixed |
| four teaching methods: worked examples, parsons, pair, predict-run-modify | yes | research-backed (with caveats) |
| assessment types: quizzes, exit tickets, small exercises, capstone | yes | assessment map fixed |
| capstone rubric: 4 criteria, 1-4 scale, pass at 12/16 with correctness ≥2 | yes | summative assessment fixed |
| 120 planned hours across 5 roles | yes | budget fixed |
| 6-phase timeline with 6 milestones from 5 nov 2026 baseline | yes | project plan fixed |
| risk table (r1–r6) | yes | risk register fixed |
| success metrics (completion ≥80%, quiz rise, confidence rise, capstone pass) | yes | evaluation criteria fixed |
| glossary terms | yes | shared vocabulary |
| colour palette (navy #1f4e5f, teal #2a9d8f, amber #e9c46a, coral #e76f51, grey #6c757d) | yes | visual identity |
| docx style: georgia body, calibri headings, navy headings, shaded table headers, live toc field, page numbers in footer, alt text on images | yes | professional layout standard |
| file naming: `project_plan_scope_definition_week1.docx` pattern | yes | naming convention |

---

## 6. what week 2 must correct / extend (documented changes since week 1)

| change | reason |
|--------|--------|
| fix session timing: 90 minutes exactly accounted for | week 1 had 85-minute sum |
| move from "planned" module list to full lesson plans with minute-by-minute tables | week 2 deliverable requirement |
| add executed code examples with real output for every snippet | rule r2: every code example is executed |
| add activities with starter files, solutions, and automated checks | week 2 deliverable requirement |
| extend research register with verified sources only; mark design decisions explicitly | fix week 1 evidence weakness |
| add evidence map table: finding → source → design decision → module location | week 2 requirement |
| add alignment matrix (objectives × activities × assessments) with coverage check | week 2 requirement |
| add readability audit (flesch-kincaid grade ≤8 for learner-facing text) | week 2 requirement |
| add jargon audit (every term defined at first use or in glossary) | week 2 requirement |
| add 12+ figures including memory diagrams, flowcharts, loop traces, traceback annotations | week 2 requirement (min 12) |
| produce single-source-of-truth data files (yaml/json) for all curriculum content | rule r1 |
| all hours, minutes, percentages computed from data, not hand-typed | rule r6, r7 |
| docx under 2 mb with compressed figures | hard constraint |
| submission_text.txt 230–280 words for portal | week 2 deliverable |

---

## 7. key data extracted for week 2 curriculum.yaml

```yaml
modules:
  - id: m1
    title: "computational thinking and problem decomposition"
    hours: 3
    minutes: 180
    prerequisites: []
    concepts_introduced: ["algorithm", "step-by-step instruction", "decomposition", "sequence"]
  - id: m2
    title: "variables and data types"
    hours: 3
    minutes: 180
    prerequisites: ["m1"]
    concepts_introduced: ["variable", "assignment", "data type", "string", "integer", "float"]
  - id: m3
    title: "input and output"
    hours: 2
    minutes: 120
    prerequisites: ["m2"]
    concepts_introduced: ["input()", "print()", "prompt", "display"]
  - id: m4
    title: "conditionals (if / else)"
    hours: 3
    minutes: 180
    prerequisites: ["m3"]
    concepts_introduced: ["if", "else", "elif", "boolean expression", "comparison operator"]
  - id: m5
    title: "loops (repeat)"
    hours: 3
    minutes: 180
    prerequisites: ["m4"]
    concepts_introduced: ["while", "for", "range", "iteration", "loop variable", "break"]
  - id: m6
    title: "functions (reusable steps)"
    hours: 3
    minutes: 180
    prerequisites: ["m5"]
    concepts_introduced: ["def", "return", "parameter", "argument", "function call", "scope"]
  - id: m7
    title: "lists and dictionaries"
    hours: 3
    minutes: 180
    prerequisites: ["m6"]
    concepts_introduced: ["list", "index", "append", "dictionary", "key", "value", "iteration over collection"]
  - id: m8
    title: "files and simple data"
    hours: 3
    minutes: 180
    prerequisites: ["m7"]
    concepts_introduced: ["open", "read", "write", "with statement", "csv basics"]
  - id: m9
    title: "debugging and reading errors"
    hours: 3
    minutes: 180
    prerequisites: ["m1","m2","m3","m4","m5","m6","m7","m8"]
    concepts_introduced: ["traceback", "syntax error", "runtime error", "logic error", "debugging strategy"]
  - id: m10
    title: "final mini-project (capstone)"
    hours: 4
    minutes: 240
    prerequisites: ["m1","m2","m3","m4","m5","m6","m7","m8","m9"]
    concepts_introduced: []  # capstone applies all prior concepts

total_teaching_minutes: 1800
total_teaching_hours: 30

session_duration_minutes: 90
sessions_per_module: 2  # 3 hours = 2 × 90 min, except m3 (120 min = 1.33 sessions), m10 (240 min = 2.67 sessions)
total_sessions: 20  # approx, to be computed precisely
```

---

## 8. runtime verification note

week 1 chose google colab / browser editor. this environment (cpython 3.13.7) cannot directly test colab behaviour. week 2 must:
- verify all code runs on cpython 3.10+ (standard library only)
- note in known limitations: "verified on cpython 3.13; not run in browser runtime"
- avoid: blocking input() loops, os-level calls, threads, network access, non-standard-lib packages