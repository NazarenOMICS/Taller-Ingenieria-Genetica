---
type: block-summary
status: current
date: 2026-07-14
source: "notebooklm:dcas9-fto-granulosa/q11-controles-experimentales:block-summary"
related:
  - "[[Notes/Dashboards/CRISPRa experimental controls]]"
---

# CRISPRa experimental controls - NotebookLM block summary

Resumen sintético y reutilizable para escritura, compilado a partir de QA exportadas del notebook.

## QA fuente

- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q01 - according-to-these-sources-what-non.md]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q02 - according-to-these-sources-what-role.md]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q03 - according-to-these-sources-what-role.md]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q04 - according-to-these-sources-e-g.md]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q05 - according-to-these-sources-e-g.md]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q06 - what-gaps-remain-these-sources-regarding.md]]

## Referencias bibliográficas clave del bloque

- Sin referencias consolidadas

## Fuentes núcleo del bloque

- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/albert_2013_multiplexed_activation_of_endogenous_genes_by_crispr_on.pdf|albert_2013_multiplexed_activation_of_endogenous_genes_by_crispr_on.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/yang_2019_engineered_crispra_enables_programmable_eukaryote_like_gene_activation.pdf|yang_2019_engineered_crispra_enables_programmable_eukaryote_like_gene_activation.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/josh_2019_mitigation_of_off_target_toxicity_in_crispr_cas9.pdf|josh_2019_mitigation_of_off_target_toxicity_in_crispr_cas9.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/kendall_2018_up_down_and_out_optimized_libraries_for_crispra.pdf|kendall_2018_up_down_and_out_optimized_libraries_for_crispra.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/charleen_2021_tissue_specific_activation_of_gene_expression_by_the.pdf|charleen_2021_tissue_specific_activation_of_gene_expression_by_the.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/kohei_2021_comparative_analysis_and_rational_design_of_dcas9_vp64.pdf|kohei_2021_comparative_analysis_and_rational_design_of_dcas9_vp64.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf|joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf]]

## Hilo central del bloque

- In CRISPRa experiments, the standard use of **non-targeting**, **scrambled**, or **mutant (mismatch)** sgRNAs serves as a critical control for several factors, primarily to ensure that observed gene activation is specific to the intended target and not a result of the experimental components themselves.
- In CRISPRa and epigenome editing experiments, a **catalytically dead or inactive effector domain** (such as a dead p300 core or dead TET1 catalytic domain) serves as a critical control to prove that observed gene activation is specifically caused by the **enzymatic activity** of the effector and not by the mere physical binding of the dCas9 complex to the target locus  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 2|[2...
- In CRISPRa experiments, a **dCas9-only control** (a nuclease-dead Cas9 lacking any attached transcriptional effector) is used to establish a baseline for gene expression and to confirm that any observed activation is strictly due to the recruited effector and not the physical binding of the dCas9 protein itself  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/albert_2013_multiplexed_activation_of_endogenous_genes_by_crispr_on.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/josh_2019_mitigation_of_off_target_toxicity_in_crispr_cas9.pdf#Passage 2|[2]]]. This control is essential for proving the **necessity of the effec...
- To rigorously attribute observed gene activation to a targeted CRISPRa mechanism, the sources recommend several critical design choices and additional controls beyond standard non-targeting or inactive effector groups:
- At the screening and library scale, CRISPRa experiments utilize several layers of controls to distinguish true biological hits from artifacts such as off-target toxicity, system-induced stress, and statistical noise.
- Based on the provided sources, researchers have validated individual components of a rigorous control panel for dCas9-p300 experiments—such as the **p300CD D1398Y** catalytically dead mutant  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 3|[1]]] and **non-targeting sgRNAs**  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/yang_2019_engineered_crispra_enables_programmable_eukaryote_like_gene_activation.pdf#Passage 4|[2]]]—but several gaps remain regarding a **complete, standardized panel** specifically tailored and co-validated for the unique mechanisms o...

## Resumen por QA

## [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q01 - according-to-these-sources-what-non.md]]

In CRISPRa experiments, the standard use of **non-targeting**, **scrambled**, or **mutant (mismatch)** sgRNAs serves as a critical control for several factors, primarily to ensure that observed gene activation is specific to the intended target and not a result of the experimental components themselves.
## [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q02 - according-to-these-sources-what-role.md]]

In CRISPRa and epigenome editing experiments, a **catalytically dead or inactive effector domain** (such as a dead p300 core or dead TET1 catalytic domain) serves as a critical control to prove that observed gene activation is specifically caused by the **enzymatic activity** of the effector and not by the mere physical binding of the dCas9 complex to the target locus  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 2|[2...
## [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q03 - according-to-these-sources-what-role.md]]

In CRISPRa experiments, a **dCas9-only control** (a nuclease-dead Cas9 lacking any attached transcriptional effector) is used to establish a baseline for gene expression and to confirm that any observed activation is strictly due to the recruited effector and not the physical binding of the dCas9 protein itself  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/albert_2013_multiplexed_activation_of_endogenous_genes_by_crispr_on.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/josh_2019_mitigation_of_off_target_toxicity_in_crispr_cas9.pdf#Passage 2|[2]]]. This control is essential for proving the **necessity of the effec...
## [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q04 - according-to-these-sources-e-g.md]]

To rigorously attribute observed gene activation to a targeted CRISPRa mechanism, the sources recommend several critical design choices and additional controls beyond standard non-targeting or inactive effector groups:
## [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q05 - according-to-these-sources-e-g.md]]

At the screening and library scale, CRISPRa experiments utilize several layers of controls to distinguish true biological hits from artifacts such as off-target toxicity, system-induced stress, and statistical noise.
## [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q06 - what-gaps-remain-these-sources-regarding.md]]

Based on the provided sources, researchers have validated individual components of a rigorous control panel for dCas9-p300 experiments—such as the **p300CD D1398Y** catalytically dead mutant  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 3|[1]]] and **non-targeting sgRNAs**  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/yang_2019_engineered_crispra_enables_programmable_eukaryote_like_gene_activation.pdf#Passage 4|[2]]]—but several gaps remain regarding a **complete, standardized panel** specifically tailored and co-validated for the unique mechanisms o...

## Gaps y puntos a reforzar

- No se detectaron gaps explícitos en las QA exportadas.
