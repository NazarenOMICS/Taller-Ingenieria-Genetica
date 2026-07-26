# NotebookLM Question Planner Subagent Task

Use model: gpt-5.4-mini.

Return JSON only. Do not run tools. Do not answer the questions.

Input JSON:

{
  "slug": "q05-fto-m6a-edad",
  "project": "dcas9-fto-granulosa",
  "vault_slug": "dcas9-fto-granulosa/q05-fto-m6a-edad",
  "goal": "Determinar como varian la expresion de FTO y el nivel global de m6A en el ovario y en la granulosa con la edad, y con que tecnicas se cuantifican de forma sitio-especifica.",
  "dashboard": "FTO m6A vs age ovary",
  "notebook_id": "dc4c4ee0-31fa-4a55-bf26-101bc3f90e8e",
  "sources_json": "C:\Users\Administrator\Documents\Taller Ingenieria Genetica\runs\dcas9-fto-granulosa\q05-fto-m6a-edad\tmp-sources-q05-fto-m6a-edad.json"
}

Required output JSON:

{
  "slug": "q05-fto-m6a-edad",
  "goal": "Determinar como varian la expresion de FTO y el nivel global de m6A en el ovario y en la granulosa con la edad, y con que tecnicas se cuantifican de forma sitio-especifica.",
  "dashboard": "FTO m6A vs age ovary",
  "notebook_id": "dc4c4ee0-31fa-4a55-bf26-101bc3f90e8e",
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
