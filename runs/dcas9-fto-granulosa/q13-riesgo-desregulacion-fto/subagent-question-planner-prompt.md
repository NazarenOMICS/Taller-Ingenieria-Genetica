# NotebookLM Question Planner Subagent Task

Use model: gpt-5.4-mini.

Return JSON only. Do not run tools. Do not answer the questions.

Input JSON:

{
  "slug": "q13-riesgo-desregulacion-fto",
  "project": "dcas9-fto-granulosa",
  "vault_slug": "dcas9-fto-granulosa/q13-riesgo-desregulacion-fto",
  "goal": "Determinar cuales son los riesgos de la desregulacion global asociada a FTO por su multiplicidad de blancos de m6A, y como se acota una activacion fisiologica frente a una suprafisiologica.",
  "dashboard": "FTO dysregulation risk",
  "notebook_id": "ef0da090-9b28-43a3-9dd4-5889790ce012",
  "sources_json": "C:\Users\Administrator\Documents\Taller Ingenieria Genetica\runs\dcas9-fto-granulosa\q13-riesgo-desregulacion-fto\tmp-sources-q13-riesgo-desregulacion-fto.json"
}

Required output JSON:

{
  "slug": "q13-riesgo-desregulacion-fto",
  "goal": "Determinar cuales son los riesgos de la desregulacion global asociada a FTO por su multiplicidad de blancos de m6A, y como se acota una activacion fisiologica frente a una suprafisiologica.",
  "dashboard": "FTO dysregulation risk",
  "notebook_id": "ef0da090-9b28-43a3-9dd4-5889790ce012",
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
