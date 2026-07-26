---
type: citation-audit
status: pass
date: 2026-07-24
source: "notebooklm:dcas9-fto-granulosa/q20-fto-otros-tejidos-cromatina:citation-audit"
related:
  - "[[Notes/Dashboards/FTO downregulation chromatin evidence in other tissues]]"
---

# Citation Audit - dcas9-fto-granulosa/q20-fto-otros-tejidos-cromatina

## Verdict

- Status: PASS
- QA notes checked: 6
- Source links: 126
- Passage-anchored links: 126
- PDF links in QA body: 0

## Broken Source Links

- None

## QA Notes Without Source Links

- None

## Interpretation

- PASS means exported QA notes link claims to existing `Sources` notes.
- WARN means QA notes are traceable, but some body links still point directly to PDFs.
- FAIL means at least one QA note lacks source links or points to missing source notes.

## Local Repair Note

- The original FAIL was caused by missing source notes under `Notes/NotebookLM/dcas9-fto-granulosa/q20-fto-otros-tejidos-cromatina/Sources/`.
- Those source notes were re-imported locally on 2026-07-25 and the previously broken links now resolve:
  - `xiulin_2021_the_role_of_m6a_modification_in_the_biological.pdf`
  - `yanlin_2023_epigenetic_regulation_in_metabolic_diseases_mechanisms_and_advances.pdf`
  - `yuqian_2023_premature_ovarian_insufficiency_a_review_on_the_role.pdf`
  - `zhang_2026_ubiquitination_dependent_regulation_of_ferroptosis_in_ischemic_heart.pdf`
- A full wrapper rerun was attempted but blocked by transient NotebookLM/DNS failure (`getaddrinfo failed`), so this audit status was repaired from verified local vault state rather than a fresh network run.
