# NotebookLM Question Planner Subagent Task

Use model: gpt-5.4-mini.

Return JSON only. Do not run tools. Do not answer the questions.

Input JSON:

{
  "slug": "q07-metodos-m6a-fos-3utr",
  "project": "dcas9-fto-granulosa",
  "vault_slug": "dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr",
  "goal": "Determinar que metodos permiten cuantificar m6A sitio-especifica sobre el 3'UTR de FOS (MeRIP-qPCR, SELECT, miCLIP) y su efecto sobre la estabilidad del mensajero (ensayos con actinomicina D).",
  "dashboard": "m6A methods FOS 3-UTR",
  "notebook_id": "b7d60267-6d14-41ad-b7b7-5b606bb8ab2a",
  "sources_json": "C:\Users\Administrator\Documents\Taller Ingenieria Genetica\runs\dcas9-fto-granulosa\q07-metodos-m6a-fos-3utr\tmp-sources-q07-metodos-m6a-fos-3utr.json"
}

Required output JSON:

{
  "slug": "q07-metodos-m6a-fos-3utr",
  "goal": "Determinar que metodos permiten cuantificar m6A sitio-especifica sobre el 3'UTR de FOS (MeRIP-qPCR, SELECT, miCLIP) y su efecto sobre la estabilidad del mensajero (ensayos con actinomicina D).",
  "dashboard": "m6A methods FOS 3-UTR",
  "notebook_id": "b7d60267-6d14-41ad-b7b7-5b606bb8ab2a",
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
