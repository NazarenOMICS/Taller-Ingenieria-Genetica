# NotebookLM Question Planner Subagent Task

Use model: gpt-5.4-mini.

Return JSON only. Do not run tools. Do not answer the questions.

Input JSON:

{
  "slug": "q14-dcas9p300-vs-otros-activadores",
  "project": "dcas9-fto-granulosa",
  "vault_slug": "dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores",
  "goal": "Determinar que diferencias funcionales existen entre activar FTO con dCas9-p300 y hacerlo con otros activadores (VP64, VPR, SunTag-p300) sobre este mismo locus.",
  "dashboard": "dCas9-p300 vs other activators",
  "notebook_id": "997cd2ff-f1d7-42e0-9026-f046a1d2c7dd",
  "sources_json": "C:\Users\Administrator\Documents\Taller Ingenieria Genetica\runs\dcas9-fto-granulosa\q14-dcas9p300-vs-otros-activadores\tmp-sources-q14-dcas9p300-vs-otros-activadores.json"
}

Required output JSON:

{
  "slug": "q14-dcas9p300-vs-otros-activadores",
  "goal": "Determinar que diferencias funcionales existen entre activar FTO con dCas9-p300 y hacerlo con otros activadores (VP64, VPR, SunTag-p300) sobre este mismo locus.",
  "dashboard": "dCas9-p300 vs other activators",
  "notebook_id": "997cd2ff-f1d7-42e0-9026-f046a1d2c7dd",
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
