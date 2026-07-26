# NotebookLM Question Planner Subagent Task

Use model: gpt-5.4-mini.

Return JSON only. Do not run tools. Do not answer the questions.

Input JSON:

{
  "slug": "q09-marcadores-senescencia",
  "project": "dcas9-fto-granulosa",
  "vault_slug": "dcas9-fto-granulosa/q09-marcadores-senescencia",
  "goal": "Determinar que marcadores de senescencia y de daño al ADN (SA-beta-galactosidasa, gammaH2AX, p21, p16) son estandar en modelos de envejecimiento de la granulosa, y cual es su lectura esperable ante una reversion parcial.",
  "dashboard": "Senescence markers granulosa",
  "notebook_id": "c93512be-32e2-4343-a469-9c294ffc840b",
  "sources_json": "C:\Users\Administrator\Documents\Taller Ingenieria Genetica\runs\dcas9-fto-granulosa\q09-marcadores-senescencia\tmp-sources-q09-marcadores-senescencia.json"
}

Required output JSON:

{
  "slug": "q09-marcadores-senescencia",
  "goal": "Determinar que marcadores de senescencia y de daño al ADN (SA-beta-galactosidasa, gammaH2AX, p21, p16) son estandar en modelos de envejecimiento de la granulosa, y cual es su lectura esperable ante una reversion parcial.",
  "dashboard": "Senescence markers granulosa",
  "notebook_id": "c93512be-32e2-4343-a469-9c294ffc840b",
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
