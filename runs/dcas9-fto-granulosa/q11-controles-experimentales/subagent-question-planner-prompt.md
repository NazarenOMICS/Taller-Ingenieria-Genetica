# NotebookLM Question Planner Subagent Task

Use model: gpt-5.4-mini.

Return JSON only. Do not run tools. Do not answer the questions.

Input JSON:

{
  "slug": "q11-controles-experimentales",
  "project": "dcas9-fto-granulosa",
  "vault_slug": "dcas9-fto-granulosa/q11-controles-experimentales",
  "goal": "Determinar que controles experimentales distinguen de forma rigurosa el efecto epigenetico dirigido de artefactos (guia no dirigida, dominio p300 cataliticamente inactivo, dCas9 sin efector).",
  "dashboard": "CRISPRa experimental controls",
  "notebook_id": "83c9725a-d105-4f75-a11c-dc0100661c7b",
  "sources_json": "C:\Users\Administrator\Documents\Taller Ingenieria Genetica\runs\dcas9-fto-granulosa\q11-controles-experimentales\tmp-sources-q11-controles-experimentales.json"
}

Required output JSON:

{
  "slug": "q11-controles-experimentales",
  "goal": "Determinar que controles experimentales distinguen de forma rigurosa el efecto epigenetico dirigido de artefactos (guia no dirigida, dominio p300 cataliticamente inactivo, dCas9 sin efector).",
  "dashboard": "CRISPRa experimental controls",
  "notebook_id": "83c9725a-d105-4f75-a11c-dc0100661c7b",
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
