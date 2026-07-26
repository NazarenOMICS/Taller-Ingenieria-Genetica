---
type: reference
status: current
date: 2026-07-24
source: "notebooklm:dcas9-fto-granulosa/q01-activacion-eficiencia"
related:
  - "[[Notes/Dashboards/dCas9-p300 activation efficiency]]"
---

# Q01 - According to these sources, what magnitude of transcriptional activation (fold-change in mRNA/expression) does dCas9-p300 achieve on endogenous human gene promoters, and on which genes/cell types was this measured?

In human cells, the **dCas9-p300** transcriptional activator (specifically the catalytic histone acetyltransferase core domain) typically achieves activation magnitudes ranging from **100-fold to 300-fold** relative to non-induced controls when targeted to endogenous promoters  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 1|[1]]].

Measurements of these expression levels were performed primarily on the following endogenous human genes in **HEK293T cells**  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/hilton_2015.pdf#Passage 1|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 2|[3]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 3|[4]]]:

*   **NEUROD1:** Observed activation at approximately **300-fold**  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 1|[1]]]. Sources note that dCas9-p300 is particularly effective at this specific locus, showing stronger activation than simpler VP64-based systems  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 4|[5]]].
*   **ASCL1:** Observed activation at approximately **150–200 fold**  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 1|[1]]].
*   **MYOD1:** Observed activation at approximately **100-fold**  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/hilton_2015.pdf#Passage 1|[2]]].
*   **IL1RN:** Described as "high levels" of transcription, significantly higher than first-generation dCas9-VP64 systems  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/hilton_2015.pdf#Passage 1|[2]]].

### Enhanced Magnitudes via Multiplexing and Scaffolding
The magnitude of activation can be significantly increased by using multiple guide RNAs (multiplexing) or by combining the p300 core with additional activation domains via MS2-MCP scaffolding (the **p300+MV** system)  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 5|[6]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 6|[7]]]:

*   **Synergistic Activation:** Utilizing the enhanced p300+MV system with **multiple gRNAs** achieved nearly **10,000-fold** activation for *ASCL1* and over **1,000-fold** for *IL1RN* in HEK293T cells  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 7|[8]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 8|[9]]].
*   **MYOD1 Multiplexing:** With the p300+MV system and multiplexed guides, activation reached approximately **1,000-fold**  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 7|[8]]].

### Measurements in Other Human Cell Types
While HEK293T cells provided the primary quantitative data for promoter activation, the system was also tested in **primary adult human skin fibroblasts** during cellular reprogramming experiments  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/jere_2018_human_pluripotent_reprogramming_with_crispr_activators.pdf#Passage 1|[10]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/jere_2018_human_pluripotent_reprogramming_with_crispr_activators.pdf#Passage 2|[11]]]. However, in this specific differentiated cell context, dCas9-p300 fusions **did not improve reprogramming outcomes** compared to other activators like dCas9-VP192  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 1|[12]]]. p300 has also been used to activate genes from distal enhancers in human cells by catalyzing **H3K27ac**, a signal for active transcription [13, 14].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> paring activities in a systematic, controlled fashion. Here, we aimed to characterize and rationally

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> scription of endogenous and exogenous genes, we generated expression plasmids for dCas9

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> did the other systems. SunTag-VP, VP+MV and p300 similarly activated ASCL1 andMYOD1, but p300 activated

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 5|Pasaje 5]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> and exhibit great versatility for various cell types and developmental stages in vivo, different

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 6|Pasaje 6]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> way ANOVA with Tukey’s multiple comparisons test. ��, P<0.01; ���, P<0.005 vs. non-induced control, #, P<0.05; ###, P<0.005 vs. VP.

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 8|Pasaje 8]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> tested. Error bars indicate the mean ± SE (n = 3). Statistical analysis was performed using one-way ANOVA with

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/jere_2018_human_pluripotent_reprogramming_with_crispr_activators.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/jere_2018_human_pluripotent_reprogramming_with_crispr_activators.pdf|PDF]]
- Texto literal:
> Development of reprogramming approaches for faithful recapitulation of cellular phenotypes is an important task, considering the increasing pace with which reprogrammed cells are moving toward clinical trials21. Here we describe a method for

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|PDF]]
- Texto literal:
> is to locally deposit H3K27ac marks. Therefore, in contrast to the local reduction of enhancer marks by dCas9-LSD1, recruitment of histone acetyl transferase P300 through dCas9 fusion (dCas9-P300) resulted in a significant increase in local H3K27ac levels at enhancer elements142. Importantly, unlike other dCas9-fused transactivators, which can result in induction of gene expression primarily from promoter regions, targeting dCas9-P300 allows significant gene expression induction from both promoter and enhancer regions142. Researchers have also exploited other epigenetic modifiers to manipulate additional epigenetic marks. Among these, dCas9 fusion to the PRDM9 methyltransferase fusion complex has been utilized to manipulate local H3K4me3 marks143. Notably, local induction of H3K4me3, which is a marker of active promoters, was observed to be sufficient to allow re-expression of silenced target genes in various cell types143. Histone de-acetylation has been another strategy to locally manipulate chromatin structure and function. To this end, dCas9 fusion to histone deacetylases (HDAC), specifically full-length HDAC3, has been shown to effectively reduce the H3k27ac at the target loci and reduce the gene expression of the target loci144.

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/hilton_2015.pdf|hilton_2015.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/jere_2018_human_pluripotent_reprogramming_with_crispr_activators.pdf|jere_2018_human_pluripotent_reprogramming_with_crispr_activators.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf|daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf|joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kenly_2020_prevention_of_tumor_risk_associated_with_the_reprogramming.pdf|kenly_2020_prevention_of_tumor_risk_associated_with_the_reprogramming.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf|tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf]]
