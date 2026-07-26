# NotebookLM Question Planner Subagent Task

Use model: gpt-5.4-mini.

Return JSON only. Do not run tools. Do not answer the questions.

Input JSON:

{
  "slug": "q04-eje-fto-m6a-fos",
  "project": "dcas9-fto-granulosa",
  "vault_slug": "dcas9-fto-granulosa/q04-eje-fto-m6a-fos",
  "goal": "Determinar que evidencia respalda el eje FTO-m6A-FOS en celulas de la granulosa humanas, y en que modelos y con que controles fue validado mas alla de Jiang et al. 2021.",
  "dashboard": "FTO-m6A-FOS axis granulosa",
  "notebook_id": "0bf608b2-1812-42af-a82e-885597208929",
  "sources_json": "C:\Users\Administrator\Documents\Taller Ingenieria Genetica\runs\dcas9-fto-granulosa\q04-eje-fto-m6a-fos\tmp-sources-q04-eje-fto-m6a-fos.json"
}

Required output JSON:

{
  "slug": "q04-eje-fto-m6a-fos",
  "goal": "Determinar que evidencia respalda el eje FTO-m6A-FOS en celulas de la granulosa humanas, y en que modelos y con que controles fue validado mas alla de Jiang et al. 2021.",
  "dashboard": "FTO-m6A-FOS axis granulosa",
  "notebook_id": "0bf608b2-1812-42af-a82e-885597208929",
  "questions": [
    {
      "id": 1,
      "theme": "core-evidence",
      "question": "focused NotebookLM question",
      "status": "pending"
    }
  ]
}

Rules:

- IDs are integers.
- Create 3-8 focused questions for small corpus.
- Cover core evidence, mechanisms/comparisons, limitations/gaps.
- Do not collapse goal into one broad QA.
- Questions must force cited answers from NotebookLM.
