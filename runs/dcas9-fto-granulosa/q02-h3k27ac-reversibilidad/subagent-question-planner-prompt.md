# NotebookLM Question Planner Subagent Task

Use model: gpt-5.4-mini.

Return JSON only. Do not run tools. Do not answer the questions.

Input JSON:

{
  "slug": "q02-h3k27ac-reversibilidad",
  "project": "dcas9-fto-granulosa",
  "vault_slug": "dcas9-fto-granulosa/q02-h3k27ac-reversibilidad",
  "goal": "Determinar la magnitud y persistencia de la marca H3K27ac depositada por dCas9-p300, y cuanto dura la activacion transcripcional una vez retirado el editor (reversibilidad y control temporal).",
  "dashboard": "dCas9-p300 H3K27ac reversibility",
  "notebook_id": "cc690df9-1e9b-4c72-873c-91e915a72f5d",
  "sources_json": "C:\Users\Administrator\Documents\Taller Ingenieria Genetica\runs\dcas9-fto-granulosa\q02-h3k27ac-reversibilidad\tmp-sources-q02-h3k27ac-reversibilidad.json"
}

Required output JSON:

{
  "slug": "q02-h3k27ac-reversibilidad",
  "goal": "Determinar la magnitud y persistencia de la marca H3K27ac depositada por dCas9-p300, y cuanto dura la activacion transcripcional una vez retirado el editor (reversibilidad y control temporal).",
  "dashboard": "dCas9-p300 H3K27ac reversibility",
  "notebook_id": "cc690df9-1e9b-4c72-873c-91e915a72f5d",
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
