# NotebookLM Question Planner Subagent Task

Use model: gpt-5.4-mini.

Return JSON only. Do not run tools. Do not answer the questions.

Input JSON:

{
  "slug": "q20-fto-otros-tejidos-cromatina",
  "project": "dcas9-fto-granulosa",
  "vault_slug": "dcas9-fto-granulosa/q20-fto-otros-tejidos-cromatina",
  "goal": "Buscar si en otros tejidos con caída de FTO por estrés oxidativo existe evidencia a nivel de cromatina o unión de factores de transcripción que explique esa disminución.",
  "dashboard": "FTO downregulation chromatin evidence in other tissues",
  "notebook_id": "c8863563-1f8a-4836-929a-3e22dd7d61a0",
  "sources_json": "C:\Users\Administrator\Documents\Taller Ingenieria Genetica\runs\dcas9-fto-granulosa\q20-fto-otros-tejidos-cromatina\tmp-sources-q20-fto-otros-tejidos-cromatina.json"
}

Required output JSON:

{
  "slug": "q20-fto-otros-tejidos-cromatina",
  "goal": "Buscar si en otros tejidos con caída de FTO por estrés oxidativo existe evidencia a nivel de cromatina o unión de factores de transcripción que explique esa disminución.",
  "dashboard": "FTO downregulation chromatin evidence in other tissues",
  "notebook_id": "c8863563-1f8a-4836-929a-3e22dd7d61a0",
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
