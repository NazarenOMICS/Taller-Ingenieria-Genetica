---
type: reference
status: current
date: 2026-07-14
source: "notebooklm:dcas9-fto-granulosa/q01-activacion-eficiencia"
related:
  - "[[Notes/Dashboards/dCas9-p300 activation efficiency]]"
---

# Q01 - According to these sources, what magnitude of transcriptional activation (fold-change in mRNA/expression) does dCas9-p300 achieve on endogenous human gene promoters, and on which genes/cell types was this measured?

In human cells, the **dCas9-p300** transcriptional activator (utilizing the catalytic histone acetyltransferase core domain) achieves activation magnitudes typically ranging from **100-fold to 300-fold** relative to non-induced controls, depending on the target gene  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 2|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 3|[3]]].

Measurements of these expression levels were performed primarily on the following endogenous human gene promoters in **HEK293T cells**:

*   **ASCL1:** Activation observed at approximately **150–200 fold**  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 2|[2]]].
*   **MYOD1:** Activation observed at approximately **100-fold**  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 2|[2]]].
*   **NEUROD1:** Activation observed at approximately **300-fold**  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 2|[2]]].

The sources note that dCas9-p300 is particularly effective at **NEUROD1**, showing stronger activation than simpler VP64-based systems at that specific locus  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 4|[4]]]. While dCas9-p300 is also capable of activating genes from distal enhancers by directly catalyzing **H3K27ac** (a signal for active transcription), its performance on promoters is comparable to other second-generation activators like SunTag-VP  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 4|[4]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf#Passage 1|[5]]]. 

Additionally, combining dCas9-p300 with supplementary activation domains via **MS2-MCP scaffolding** (creating a "p300+MV" system) can further enhance these magnitudes, achieving nearly **10,000-fold** activation for *ASCL1* and over **1,000-fold** for *IL1RN* when multiple guide RNAs are used  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 5|[6]]]. However, the sources also indicate that dCas9-p300 fusions did not improve outcomes in reprogramming primary human skin fibroblasts compared to other activators like dCas9-VP192 [7].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> scaffolding (to make p300+MV) enhanced transcriptional activation vs. p300 alone. Direct fusion of VP64 to the N-

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> did the other systems. SunTag-VP, VP+MV and p300 similarly activated ASCL1 andMYOD1, but p300 activated

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf|PDF]]
- Texto literal:
> Manipulating the epigenome and gene expression using TEMs and TTFs So far only a few studies have been published reporting the use of dCas9 fusions for epigenome editing and manipulating gene expression. The catalytic histone acetyltransferase (HAT) core domain p300 has been used to catalyse acetylation of histones in human HEK293T cells (Hilton et al., 2015). Targeting dCas9–p300 fusions to promoter regions or proximal or distant enhancers caused activation of gene expression. Increased expression upon enhancer-targeting was concomitant with enrichment in H3K27ac at the correspond- ing genomic target sites (Hilton et al., 2015). In most cases the same genes could be transactivated by dCas9-VP64 when targeted at promoters. To achieve transactivation both effectors can thus be used. The two effectors behave somewhat differently in terms of their impact on histone acetylation state, as p300 directly catalyses H3K27ac (Ogryzko et al., 1996; Delvecchio et al., 2013), whereas VP64 recruits subsequent transactivation components, amongst which is p300 (Memedula and Belmont, 2003). Also the histone acetyltransferase domain of the CREB-binding protein has been fused to dCas9 (dCas9-CBPHAT) and has been used to catalyse locus-specific acetylation of histones (Cheng et al., 2016). dCas9-CBPHAT was targeted using the Casilio (CRISPR/Cas9-Pumilio) system, which harbours an scRNA containing multiple PUF binding sites (PBS), to recruit additional CBPHAT domains via fusions with Pumilio/FBF (PUF) RNA-binding domains. Similar to dCas9-p300, targeting dCas9-CBPHAT to promoters or proximal and distal enhancer

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 5|Pasaje 5]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> tested. Error bars indicate the mean ± SE (n = 3). Statistical analysis was performed using one-way ANOVA with

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf|daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/jere_2018_human_pluripotent_reprogramming_with_crispr_activators.pdf|jere_2018_human_pluripotent_reprogramming_with_crispr_activators.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf|joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kenly_2020_prevention_of_tumor_risk_associated_with_the_reprogramming.pdf|kenly_2020_prevention_of_tumor_risk_associated_with_the_reprogramming.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf|tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf]]
