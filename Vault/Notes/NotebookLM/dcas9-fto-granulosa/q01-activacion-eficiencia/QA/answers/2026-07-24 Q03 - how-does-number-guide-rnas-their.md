---
type: reference
status: current
date: 2026-07-24
source: "notebooklm:dcas9-fto-granulosa/q01-activacion-eficiencia"
related:
  - "[[Notes/Dashboards/dCas9-p300 activation efficiency]]"
---

# Q03 - How does the number of guide RNAs and their combination (multiplexing) affect dCas9-p300 activation efficiency compared to using a single guide, according to these sources?

According to the sources, the number of guide RNAs (sgRNAs) and their combination (multiplexing) affect **dCas9-p300** activation efficiency in a manner distinct from traditional activators like dCas9-VP64. While multiplexing often enhances activation, dCas9-p300 is uniquely capable of achieving robust results with a **single guide RNA** and is subject to specific physical constraints.  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/hilton_2015.pdf#Passage 8|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/hilton_2015.pdf#Passage 9|[2]]]

### Efficiency with a Single Guide RNA
Unlike first-generation activators that typically require a pool of multiple guides for robust gene induction, **dCas9-p300** can achieve high levels of transcription using only a **single sgRNA**.  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/hilton_2015.pdf#Passage 8|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/hilton_2015.pdf#Passage 9|[2]]] 
*   **Gene-Specific Results:** In human HEK293T cells, experiments targeting the ***IL1RN*** and ***MYOD*** promoters found **no significant difference** in activation magnitude between the best individual guide and a pool of four guides.  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/hilton_2015.pdf#Passage 9|[2]]]
*   **Comparison to VP64:** While dCas9-VP64 consistently requires multiple guides to reach effective levels, a single potent guide for p300 can sometimes match the efficiency of a **four-guide pool** used with VP64.  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/hilton_2015.pdf#Passage 9|[2]]]

### Synergistic and Additive Effects of Multiplexing
Multiplexing can provide further enhancement, but it often leads to **non-additive** or strictly additive results rather than the strong synergy seen in other systems.  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 12|[3]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 13|[4]]]
*   **Additive vs. Synergistic:** For the ***OCT4*** promoter, pooling four gRNAs with p300 produced **additive effects**, whereas dCas9-VP64 demonstrated synergistic effects (where the total is greater than the sum of its parts) in every case tested.  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/hilton_2015.pdf#Passage 9|[2]]]
*   **Scaffolded Enhancement:** Multiplexing three sgRNAs with the enhanced **p300+MV** system (which combines p300 with MS2-MCP-scaffolded VP64) was found to significantly increase activation of ***ASCL1*** and ***MYOD1***, even outperforming the high-potency SAM system when SAM was used with only a single guide.  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 14|[5]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf#Passage 2|[6]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 9|[7]]]

### Physical Constraints and Limitations
The sources highlight that the large physical size of the p300 core domain creates limitations when using multiple guides:  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 10|[8]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 11|[9]]]
*   **Steric Hindrance:** Because the dCas9-p300 complex is large, placing multiple sgRNAs too close to one another can cause **steric hindrance**.  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 10|[8]]] In a plant model, using two sgRNAs separated by only **118 bp** resulted in **lower gene expression** than using either guide alone, as the complexes may have destabilized each other on the DNA.  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 10|[8]]]
*   **Repetitive Site Sensitivity:** In experiments using the **TRE3G promoter** (which contains seven repetitive binding sites), the p300+MV system showed **limited increases in activity** compared to smaller activators like VP64 variants.  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 11|[9]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/jere_2018_human_pluripotent_reprogramming_with_crispr_activators.pdf#Passage 3|[10]]] This is attributed to the **spatial constraints** of the p300 core, which is described as a "relatively large protein" that may struggle to access crowded binding sites.  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 11|[9]]]
*   **Saturation:** The sources suggest that dCas9-p300 does not display the same degree of synergy with additional guides or TALEs as smaller, non-enzymatic activators do.  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 13|[4]]]

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/hilton_2015.pdf#Passage 9|Pasaje 9]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/hilton_2015.pdf|PDF]]
- Texto literal:
> dCas9p300 Core is more potent than existing engineered transcription factors made with single activator domains. Although synergy among other synthetic transcriptional activators, including dCas9<supVP64</sup (refs. 8,15-17,19-22,24,25), has been widely observed, the p300 Core effector domain did not display similar synergy with either additional gRNAs or TALEs (Figs. 5 and 6 and Supplementary Figs. 3 and 5) or in combination with VP64 (Supplementary Fig. 7). Moreover, the p300 Core effector was capable of robustly activating gene expression through a single gRNA at promoters and characterized enhancers (Figs. 5 and 6 and Supplementary Fig. 3). This effector was also capable of potent gene activation when targeted by a single TALE recognition site (Fig. 6 and Supplementary Fig. 5). Notably, certain loci appear to be less Nature America, Inc. All rights reserved.responsive to transactivation by the localization of a single dCas9p300 Core effector to a corresponding regulatory region (Fig. 5e-g and Supplementary Fig. 3). This does not appear to be related to chromatin accessibility based on ENCODE data (Supplementary Fig. 8), but may be related to transcription factor occupancy or competition (including endogenous p300; Supplementary Figs. 3 and 8), gRNA and genetic composition<sup46</sup, transcription start site proximity<sup14</sup, and/or the underlying local epigenetic circuitry, none of which are mutually exclusive. These factors are relevant to the function of all programmable DNAbinding proteins and their effects may be mitigated by the use of optimal gRNAs.

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 12|Pasaje 12]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> activity better than did direct VP64 fusion to the N-terminus of dCas9. dCas9-VP64+MCP-

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 13|Pasaje 13]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> vation by dCas9-VP64 [8, 9] and other CRISPRa systems [30]. Here we focused on 2VP, VP

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 14|Pasaje 14]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> higher activity than 2VP with multiplexed gRNAs (Fig 4C). Further analyses showed that the

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf|PDF]]
- Texto literal:
> Challenge of the dCas9 constructs in a GUS reporter system. To evaluate the dCas9HAT construct, we set up a surrogate reporter system based on regulation of GUS reporter gene expression. We used the 170-bp minimal truncated version of the Glycine max ubiquitin promoter, herein designated GmUcesMin28,29. We selected two sgRNAs near the transcription start site (TSS) of GmUcesMin (Fig. 2A, Table S2). The efficiency of dCas9HAT in activating the GUS reporter system was quantified by its enzymatic activity. Seedlings of stably transformed Arabidopsis lines expressing dCas9HAT were incubated with Agrobacterium carrying Ti plasmids to perform transient ectopic expression of GmUcesMin-GUS in combination with the expression of one or two sgRNAs. Significantly elevated enzymatic activity was observed for sgRNA1 (~2.4-fold increase) and sgRNA2 (~2-fold increase), while enzymatic activity was elevated ~1.4-fold for the combination of the two sgRNAs. This result indicates that the expression of dCas9HAT enhanced the expression of the GUS gene in trans when targeted to GmUcesMin promoter. Remarkably, some substantial differences were noted depending on the location of the sgRNA and/or the sgRNA combination. Previous studies have suggested that the distance of the sgRNA from the TSS might influence the transcriptional regulation of the gene of interest. While some studies have reported that a specific sgRNA binding distance from the TSS (−50 bp to +300 bp) corresponds to higher target gene expression30,31, others have pointed out that dCas9 might generate steric hindrance and thus interfere with transcriptional machinery activities21,32. Regarding the construct GmUcesMin, our two sgRNAs are separated only by 118 bp. Considering the 3D conformation of the DNA, the 30 bp length occupied by the dCas9 on DNA33 and the space taken by the HAT domain, a steric hindrance effect could be responsible for destabilizing locally the protein complexes standing on DNA. Compared to the use of only one sgRNA, this collateral effect might result to lower gene expression rather than improve it.

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 10|Pasaje 10]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> plexing in exogenous genes by utilizing the miniCMV promoter reporter, which has only one

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 11|Pasaje 11]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> regarding the incorporation of the DNA demethylase Tet1-CD for CRISPRa using the SunTag

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/jere_2018_human_pluripotent_reprogramming_with_crispr_activators.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/jere_2018_human_pluripotent_reprogramming_with_crispr_activators.pdf|PDF]]
- Texto literal:
> We present a method for the efficient conversion of primary human fibroblasts into bona fide iPSCs based entirely on the transcriptional control of endogenous genes by CRISPRa. Acti-vation of core reprogramming factor promoters alone was sufficient but inefficient, whereas additional targeting of a common Alu element brought the efficiency close to established reprogramming methods (Supplementary Fig. 5c). The more complex activator domains did not improve reprogramming efficiency, which mirrors previously reported results for gene activation33, and suggests that the benefit of simple additional fused activation domains may be limited.

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/hilton_2015.pdf|hilton_2015.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/jere_2018_human_pluripotent_reprogramming_with_crispr_activators.pdf|jere_2018_human_pluripotent_reprogramming_with_crispr_activators.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf|joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf|daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kenly_2020_prevention_of_tumor_risk_associated_with_the_reprogramming.pdf|kenly_2020_prevention_of_tumor_risk_associated_with_the_reprogramming.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf|tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf]]
