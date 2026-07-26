# NotebookLM Question Planner Subagent Task

Use model: gpt-5.4-mini.

Return JSON only. Do not run tools. Do not answer the questions.

Input JSON:

{
  "slug": "q06-ros-fto-senescencia",
  "project": "dcas9-fto-granulosa",
  "vault_slug": "dcas9-fto-granulosa/q06-ros-fto-senescencia",
  "goal": "Determinar que relacion causal esta documentada entre el estres oxidativo (ROS o peroxido de hidrogeno), el descenso de FTO y la senescencia en celulas somaticas del ovario.",
  "dashboard": "ROS FTO senescence",
  "notebook_id": "ed51dcbd-977c-4cf0-9c1b-01abfe96bdc8",
  "sources_json": "C:\Users\Administrator\Documents\Taller Ingenieria Genetica\runs\dcas9-fto-granulosa\q06-ros-fto-senescencia\tmp-sources-q06-ros-fto-senescencia.json"
}

Required output JSON:

{
  "slug": "q06-ros-fto-senescencia",
  "goal": "Determinar que relacion causal esta documentada entre el estres oxidativo (ROS o peroxido de hidrogeno), el descenso de FTO y la senescencia en celulas somaticas del ovario.",
  "dashboard": "ROS FTO senescence",
  "notebook_id": "ed51dcbd-977c-4cf0-9c1b-01abfe96bdc8",
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
