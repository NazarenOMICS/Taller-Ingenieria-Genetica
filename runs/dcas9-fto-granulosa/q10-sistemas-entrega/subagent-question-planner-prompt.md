# NotebookLM Question Planner Subagent Task

Use model: gpt-5.4-mini.

Return JSON only. Do not run tools. Do not answer the questions.

Input JSON:

{
  "slug": "q10-sistemas-entrega",
  "project": "dcas9-fto-granulosa",
  "vault_slug": "dcas9-fto-granulosa/q10-sistemas-entrega",
  "goal": "Determinar que sistemas de entrega (transfeccion transitoria, lentivirus, nanoparticulas, ARN mensajero o ribonucleoproteina) son viables y menos perturbadores para dCas9-p300 en KGN, COV434 y granulosa primaria.",
  "dashboard": "dCas9-p300 delivery systems",
  "notebook_id": "c260e72e-2999-41de-a676-fa883c7298a5",
  "sources_json": "C:\Users\Administrator\Documents\Taller Ingenieria Genetica\runs\dcas9-fto-granulosa\q10-sistemas-entrega\tmp-sources-q10-sistemas-entrega.json"
}

Required output JSON:

{
  "slug": "q10-sistemas-entrega",
  "goal": "Determinar que sistemas de entrega (transfeccion transitoria, lentivirus, nanoparticulas, ARN mensajero o ribonucleoproteina) son viables y menos perturbadores para dCas9-p300 en KGN, COV434 y granulosa primaria.",
  "dashboard": "dCas9-p300 delivery systems",
  "notebook_id": "c260e72e-2999-41de-a676-fa883c7298a5",
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
