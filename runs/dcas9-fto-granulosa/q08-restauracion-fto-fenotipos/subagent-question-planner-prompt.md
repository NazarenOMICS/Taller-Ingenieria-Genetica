# NotebookLM Question Planner Subagent Task

Use model: gpt-5.4-mini.

Return JSON only. Do not run tools. Do not answer the questions.

Input JSON:

{
  "slug": "q08-restauracion-fto-fenotipos",
  "project": "dcas9-fto-granulosa",
  "vault_slug": "dcas9-fto-granulosa/q08-restauracion-fto-fenotipos",
  "goal": "Determinar si existen antecedentes de restauracion de FTO por sobreexpresion o por edicion epigenetica, y que fenotipos de senescencia o de daño al ADN revierten.",
  "dashboard": "FTO restoration phenotypes",
  "notebook_id": "361a29b3-7eda-4a7a-83e5-bc7b8e4c1524",
  "sources_json": "C:\Users\Administrator\Documents\Taller Ingenieria Genetica\runs\dcas9-fto-granulosa\q08-restauracion-fto-fenotipos\tmp-sources-q08-restauracion-fto-fenotipos.json"
}

Required output JSON:

{
  "slug": "q08-restauracion-fto-fenotipos",
  "goal": "Determinar si existen antecedentes de restauracion de FTO por sobreexpresion o por edicion epigenetica, y que fenotipos de senescencia o de daño al ADN revierten.",
  "dashboard": "FTO restoration phenotypes",
  "notebook_id": "361a29b3-7eda-4a7a-83e5-bc7b8e4c1524",
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
