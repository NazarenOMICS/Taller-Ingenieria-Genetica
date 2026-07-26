---
type: notebook-source
source_id: "5c4947b8-1a8a-4a6a-9961-98d632c0bb52"
notebook_id: "ef0da090-9b28-43a3-9dd4-5889790ce012"
slug: "q13-riesgo-desregulacion-fto"
vault_slug: "dcas9-fto-granulosa/q13-riesgo-desregulacion-fto"
project: "dcas9-fto-granulosa"
url: ""
source_type: web
status: active
date: 2026-07-14
pdf: "Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/julie_2023_crispri_gene_modulation_and_all_optical_electrophysiology_in.pdf"
related:
  - "[[Notes/Dashboards/FTO dysregulation risk]]"
used_in_qa: true
cited_in_count: 2
qa_notes:
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/QA/answers/2026-07-14 Q03 - according-to-these-sources-e-g.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/QA/answers/2026-07-14 Q05 - what-experimental-or-design-strategies-do.md]]"
---

# julie_2023_crispri_gene_modulation_and_all_optical_electrophysiology_in.pdf

## PDF

![[Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/julie_2023_crispri_gene_modulation_and_all_optical_electrophysiology_in.pdf]]

## Source Guide

## Cited Passages

### Passage 1

Results A feasibility CRISPRi study was performed in post-differentiated iPSC-CMs targeting key genes important in cardiac electrophysiology. Comprehensive analysis using all-optical electrophysiology and a pipeline enabling correlative analysis of functional and molecular data in the same samples helped quantify the CRISPRi gene modulation in this in vitro model.

### Passage 2

For iPS and iPSC-CMs, CRISPRi can be viewed as a superior option for gene inhibition (knockdown) because of lower cytotoxicity, potentially higher efficiency, and a possibility for timeresolved, reversible action6, compared to standard CRISPR knockout. Cytotoxicity of standard CRISPR knockout comes from error-prone DNA repair of the double-strand breaks4,5. Dose and temporal control of gene modulation are desirable features to avoid off-target effects, chromosomal translocations, and genotoxicity23. Unlike CRISPR knockout, time-resolved CRISPRi allows the study of essential genes and their role in cellular functions. In our Dox-inducible CRISPRi system, we observed minimal side effects (Supplementary Figure 1). The choice of post-differentiated cardiomyocytes in this study was with the intent to avoid potential interferences with the differentiation process, to avoid potential TetO promoter silencing (Dox induction)13,51 during the Wnt-signaling modulation required for cardiac differentiation, and to provide testing in conditions that are a step closer to in vivo deployment for gene modulation. For full in vivo use, considerations for long-term stability are also important. However, for the described here in vitro testing, these are less relevant.

### Passage 3

Over the last decade, multiple efforts have led to the development of newer CRISPR-derived tools to avoid DSBs for safer and more efficient gene control6. Some of these methods, e.g., prime editing7 and base editing8,9, that use mutant or inactive version of the Cas9 enzyme and avoid the need for DSB and HDR, have accelerated so quickly as they are now entering clinical trials. Interference and activation CRISPR (CRISPRi/a) belong to this class of approaches. They use a deactivated Cas9 (dCas9) fused to an effector (a repressor10,11 or activator12) to achieve specific and reversible gene modulation. The most common version of CRISPRi uses the Krüppel-associated box (KRAB) repression domain (dCas9-KRAB) for superior transcriptional knockdown without cytotoxic effects when compared to using active Cas9. Mandegar et al.13 reported an inducible CRISPRi platform in human iPSCs coupled with RNAseq that was not only reversible but also outperformed CRISPR with an active Cas9. They showed utility in studying genes involved in cardiac cell differentiation as well as cardiac repolarization (KCNH2), documenting phenotypic responses, i.e., prolongation of the action potential in iPSC-CMs. Limpitikul et al.14 applied CRISPRi to target calmodulin mutations associated with long QT syndrome and corrected the action potential duration in patient-derived iPSC-CMs. In the few cardiac studies that have deployed CRIS-PRi/a, the efforts have been focused on creating stable dCas9-expressing iPSC lines13,15,16. While dCas9 did not prevent followup differentiation of the iPSCs into cardiac cells of different lineage, no comprehensive comparison was done to reveal potential effects on the iPSC-CM phenotype. There is a motivation to be able to deploy the CRISPRi/a gene modulation approaches in any patient-derived iPSC-CMs for large-scale screens of loss-of-function and gain-of-function perturbations using pooled or arrayed libraries of guide RNAs, gRNAs3,17, without the need to create stable dCas9 iPSC lines, including the use of standard commercial iPSC-CMs to avoid variability associated with in house differentiation18,19. Better understanding of the direct use of CRISPRi in non-dividing human cardiomyocytes can also be informative for future in vivo deployment in the postnatal human heart.

### Passage 4

levels of KCNH2 knockdown and observed that 40% knockdown was conserved upon running the qPCR post-labeling with optical sensors for voltage and calcium and using an optogenetic actuator (Fig. 3e, left). Having molecular and functional data from the same samples enabled correlative analysis. We visualized the data for the two experimental groups: -Dox and +Dox. (Fig. 3e, middle). As our all-optical electrophysiology assay and pipeline processing outputs comprehensive multiparameter data, we used a dimension-reduction approach and visualized the two groups in a t-SNE plot. The 19 different parameters: relative mRNA quantity, spontaneous frequency, various APD and CTD features under spontaneous and paced (0.5 Hz and 1 Hz) conditions— were projected onto a latent space via t-SNE (Fig. 3e, right). Despite the mild effects of CRISPRi KCNH2 knockdown on APD prolongation, group separation was seen in this projection that integrates multiparameter information.

### Passage 5

t-SNE dimension reduction for group visualization. The t-distributed stochastic neighbor embedding (t-SNE) algorithm helps visualize high-dimensional data sets by dimension reduction67. Here, we used MATLAB to produce 2D projections of 19 different measured parameters per sample including: mRNA quantity, action potential duration at 90%, 50%, and 30% repolarization (APD80, APD50, APD30), calcium transient duration (CTD90, CTD50, and CTD30) under spontaneous conditions and when paced at 0.5 Hz and 1 Hz. Euclidean measures for the distance between data points and the expression space with perplexity value of 15 were used to visualize clustering of CRISPRi-modified and control sample sets (Fig. 3e).

### Passage 6

The highly parallel all-optical platforms, as the one deployed here, can facilitate the testing and optimization of new effectors for CRISPRi/a or other gene modulation tools, by providing a comprehensive functional readout. Traditionally, and as used here for CRISPRi on KCNH2, APD (and sometimes CTD prolongation) are often viewed as key metrics in predicting cardiotoxicity risk. These are surrogate measures of QT prolongation in the ECG, which in turn is closely linked to torsadogenicity (risk of Torsade-de-Pointes type of arrhythmias). The all-optical platforms, with ability to control rate and to measure many parameters related to phenotype, enable more comprehensive studies for better prediction of arrhythmias, for a wider range of types of abnormal electromechanical and pro-arrhythmic responses, beyond torsadogenicity. For visualization and classification in phenotyping, dimension-reduction approaches, e.g., t-SNE and voltage-calcium time-embedded loops, can be useful, as illustrated in Figs. 3e and 7g, where multidimensional data is projected in easier to understand latent spaces.
