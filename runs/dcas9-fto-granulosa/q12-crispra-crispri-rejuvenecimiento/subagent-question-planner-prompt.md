# NotebookLM Question Planner Subagent Task

Use model: gpt-5.4-mini.

Return JSON only. Do not run tools. Do not answer the questions.

Input JSON:

{
  "slug": "q12-crispra-crispri-rejuvenecimiento",
  "project": "dcas9-fto-granulosa",
  "vault_slug": "dcas9-fto-granulosa/q12-crispra-crispri-rejuvenecimiento",
  "goal": "Determinar si se ha aplicado edicion epigenomica (CRISPRa o CRISPRi) al rejuvenecimiento de tejido reproductivo o a la reversion parcial del envejecimiento en otros tejidos, y con que resultados.",
  "dashboard": "CRISPRa CRISPRi rejuvenation",
  "notebook_id": "b12f5e97-10fe-4024-bf49-afab0fd1c866",
  "sources_json": "C:\Users\Administrator\Documents\Taller Ingenieria Genetica\runs\dcas9-fto-granulosa\q12-crispra-crispri-rejuvenecimiento\tmp-sources-q12-crispra-crispri-rejuvenecimiento.json"
}

Required output JSON:

{
  "slug": "q12-crispra-crispri-rejuvenecimiento",
  "goal": "Determinar si se ha aplicado edicion epigenomica (CRISPRa o CRISPRi) al rejuvenecimiento de tejido reproductivo o a la reversion parcial del envejecimiento en otros tejidos, y con que resultados.",
  "dashboard": "CRISPRa CRISPRi rejuvenation",
  "notebook_id": "b12f5e97-10fe-4024-bf49-afab0fd1c866",
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
