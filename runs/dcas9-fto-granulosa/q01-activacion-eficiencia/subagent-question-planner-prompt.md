# NotebookLM Question Planner Subagent Task

Use model: gpt-5.4-mini.

Return JSON only. Do not run tools. Do not answer the questions.

Input JSON:

{
  "slug": "q01-activacion-eficiencia",
  "project": "dcas9-fto-granulosa",
  "vault_slug": "dcas9-fto-granulosa/q01-activacion-eficiencia",
  "goal": "Determinar la eficiencia de activacion transcripcional de dCas9-p300 sobre promotores endogenos humanos y de que depende: posicion de la guia respecto al TSS, numero/combinacion de guias, arquitectura del promotor.",
  "dashboard": "dCas9-p300 activation efficiency",
  "notebook_id": "d1d79b7f-7751-4fa1-84ac-110bc93c9954",
  "sources_json": "C:\Users\Administrator\Documents\Taller Ingenieria Genetica\runs\dcas9-fto-granulosa\q01-activacion-eficiencia\tmp-sources-q01-activacion-eficiencia.json"
}

Required output JSON:

{
  "slug": "q01-activacion-eficiencia",
  "goal": "Determinar la eficiencia de activacion transcripcional de dCas9-p300 sobre promotores endogenos humanos y de que depende: posicion de la guia respecto al TSS, numero/combinacion de guias, arquitectura del promotor.",
  "dashboard": "dCas9-p300 activation efficiency",
  "notebook_id": "d1d79b7f-7751-4fa1-84ac-110bc93c9954",
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
