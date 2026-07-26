# NotebookLM Question Planner Subagent Task

Use model: gpt-5.4-mini.

Return JSON only. Do not run tools. Do not answer the questions.

Input JSON:

{
  "slug": "q03-especificidad-off-target",
  "project": "dcas9-fto-granulosa",
  "vault_slug": "dcas9-fto-granulosa/q03-especificidad-off-target",
  "goal": "Determinar el perfil de especificidad y de efectos fuera de blanco de dCas9-p300 en celulas humanas, tanto a nivel de union de las guias como de cambios transcriptomicos globales.",
  "dashboard": "dCas9-p300 off-target specificity",
  "notebook_id": "e1baac88-0719-426f-b47a-b620d48b6489",
  "sources_json": "C:\Users\Administrator\Documents\Taller Ingenieria Genetica\runs\dcas9-fto-granulosa\q03-especificidad-off-target\tmp-sources-q03-especificidad-off-target.json"
}

Required output JSON:

{
  "slug": "q03-especificidad-off-target",
  "goal": "Determinar el perfil de especificidad y de efectos fuera de blanco de dCas9-p300 en celulas humanas, tanto a nivel de union de las guias como de cambios transcriptomicos globales.",
  "dashboard": "dCas9-p300 off-target specificity",
  "notebook_id": "e1baac88-0719-426f-b47a-b620d48b6489",
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
