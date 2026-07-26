---
type: reference-summary
status: current
date: 2026-07-14
source: "notebooklm:dcas9-fto-granulosa/q11-controles-experimentales:qa-summary"
related:
  - "[[Notes/Dashboards/CRISPRa experimental controls]]"
---

# QA Summary - dcas9-fto-granulosa/q11-controles-experimentales

Documento consolidado de las QA exportadas para este notebook. Util para redactar introducciones, comparar respuestas y localizar rapidamente que nota contiene cada argumento.

## QA incluidas

- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q01 - according-to-these-sources-what-non.md]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q02 - according-to-these-sources-what-role.md]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q03 - according-to-these-sources-what-role.md]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q04 - according-to-these-sources-e-g.md]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q05 - according-to-these-sources-e-g.md]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q06 - what-gaps-remain-these-sources-regarding.md]]

## Resumen por QA

## Q01
- Pregunta: According to these sources, what non-targeting or scrambled sgRNA controls are standard in CRISPRa experiments, and what do they control for?
- Nota completa: [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q01 - according-to-these-sources-what-non.md]]

In CRISPRa experiments, the standard use of **non-targeting**, **scrambled**, or **mutant (mismatch)** sgRNAs serves as a critical control for several factors, primarily to ensure that observed gene activation is specific to the intended target and not a result of the experimental components themselves.
## Q02
- Pregunta: According to these sources, what role does a catalytically dead/inactive effector domain (e.g., dead p300 core, dead VP64) play as a control in distinguishing genuine epigenetic activation from non-specific effects?
- Nota completa: [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q02 - according-to-these-sources-what-role.md]]

In CRISPRa and epigenome editing experiments, a **catalytically dead or inactive effector domain** (such as a dead p300 core or dead TET1 catalytic domain) serves as a critical control to prove that observed gene activation is specifically caused by the **enzymatic activity** of the effector and not by the mere physical binding of the dCas9 complex to the target locus  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 2|[2]]].
## Q03
- Pregunta: According to these sources, what is the role of a dCas9-only control (without any transcriptional effector) in CRISPRa experiments, and what artifacts can dCas9 binding alone introduce even without an effector domain?
- Nota completa: [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q03 - according-to-these-sources-what-role.md]]

In CRISPRa experiments, a **dCas9-only control** (a nuclease-dead Cas9 lacking any attached transcriptional effector) is used to establish a baseline for gene expression and to confirm that any observed activation is strictly due to the recruited effector and not the physical binding of the dCas9 protein itself  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/albert_2013_multiplexed_activation_of_endogenous_genes_by_crispr_on.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/josh_2019_mitigation_of_off_target_toxicity_in_crispr_cas9.pdf#Passage 2|[2]]]. This control is essential for proving the **necessity of the effector** for the desired biological phenotype; for instance, while a dCas9-activator fusion successfully activated the *MSI1* gene, dCas9 lacking an activation domain failed to do so  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/albert_2013_multiplexed_activation_of_endogenous_genes_by_crispr_on.pdf#Passage 1|[1]]]. In pooled library screens, dCas9-only controls help researchers distinguish between general cellular stress caused by dCas9 binding and the specific off-t...
## Q04
- Pregunta: According to these sources (e.g., comparative analyses of dCas9-VP64 variants), what additional controls or design choices (e.g., multiple independent guides, dose-response, orthogonal validation methods) are recommended to rigorously attribute an observed gene activation to the targeted CRISPRa mechanism?
- Nota completa: [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q04 - according-to-these-sources-e-g.md]]

To rigorously attribute observed gene activation to a targeted CRISPRa mechanism, the sources recommend several critical design choices and additional controls beyond standard non-targeting or inactive effector groups:
## Q05
- Pregunta: According to these sources (e.g., CRISPRa screening libraries), what controls are used at the screening/library scale to distinguish true hits from artifacts?
- Nota completa: [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q05 - according-to-these-sources-e-g.md]]

At the screening and library scale, CRISPRa experiments utilize several layers of controls to distinguish true biological hits from artifacts such as off-target toxicity, system-induced stress, and statistical noise.
## Q06
- Pregunta: What gaps remain in these sources regarding a complete, standardized control panel (non-targeting guide + catalytically dead effector + dCas9-only) specifically validated for dCas9-p300 experiments?
- Nota completa: [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q06 - what-gaps-remain-these-sources-regarding.md]]

Based on the provided sources, researchers have validated individual components of a rigorous control panel for dCas9-p300 experiments—such as the **p300CD D1398Y** catalytically dead mutant  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 3|[1]]] and **non-targeting sgRNAs**  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/yang_2019_engineered_crispra_enables_programmable_eukaryote_like_gene_activation.pdf#Passage 4|[2]]]—but several gaps remain regarding a **complete, standardized panel** specifically tailored and co-validated for the unique mechanisms of dCas9-p300.

## Sources Referenced Across QA Summary

- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/josh_2019_mitigation_of_off_target_toxicity_in_crispr_cas9.pdf|josh_2019_mitigation_of_off_target_toxicity_in_crispr_cas9.pdf]] - 30 mencion(es)
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/albert_2013_multiplexed_activation_of_endogenous_genes_by_crispr_on.pdf|albert_2013_multiplexed_activation_of_endogenous_genes_by_crispr_on.pdf]] - 19 mencion(es)
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/yang_2019_engineered_crispra_enables_programmable_eukaryote_like_gene_activation.pdf|yang_2019_engineered_crispra_enables_programmable_eukaryote_like_gene_activation.pdf]] - 17 mencion(es)
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/kendall_2018_up_down_and_out_optimized_libraries_for_crispra.pdf|kendall_2018_up_down_and_out_optimized_libraries_for_crispra.pdf]] - 11 mencion(es)
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf]] - 11 mencion(es)
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/kohei_2021_comparative_analysis_and_rational_design_of_dcas9_vp64.pdf|kohei_2021_comparative_analysis_and_rational_design_of_dcas9_vp64.pdf]] - 8 mencion(es)
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/charleen_2021_tissue_specific_activation_of_gene_expression_by_the.pdf|charleen_2021_tissue_specific_activation_of_gene_expression_by_the.pdf]] - 6 mencion(es)
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]] - 5 mencion(es)
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf|joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf]] - 3 mencion(es)
