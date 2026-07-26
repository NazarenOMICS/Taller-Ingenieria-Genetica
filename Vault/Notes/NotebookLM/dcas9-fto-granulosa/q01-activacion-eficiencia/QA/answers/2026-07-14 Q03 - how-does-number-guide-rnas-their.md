---
type: reference
status: current
date: 2026-07-14
source: "notebooklm:dcas9-fto-granulosa/q01-activacion-eficiencia"
related:
  - "[[Notes/Dashboards/dCas9-p300 activation efficiency]]"
---

# Q03 - How does the number of guide RNAs and their combination (multiplexing) affect dCas9-p300 activation efficiency compared to using a single guide, according to these sources?

According to the sources, using multiple guide RNAs (multiplexing) to target **dCas9-p300** to a single gene generally **significantly enhances activation efficiency** compared to using a single guide, although this effect is subject to important spatial and structural constraints  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 6|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 9|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf#Passage 2|[3]]].

### Synergistic Enhancement and Magnitudes
*   **Significant Increases:** For endogenous human genes like ***ASCL1*** and ***MYOD1***, multiplexing with the enhanced p300 system (dCas9-p300+MCP-VP64, or **p300+MV**) achieved higher activation levels than even the potent SAM system could achieve with a single guide  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 6|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 10|[4]]].
*   **Gene-Specific Scaling:** In HEK293T cells, multiplexing three sgRNAs for the ***IL1RN*** gene with p300+MV led to a substantial increase in mRNA expression over a single guide, although in this specific instance, it did not surpass the efficiency of a single-guide SAM system  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 9|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 7|[5]]].
*   **General Synergistic Effect:** The sources note that higher efficiency is typically obtained as more sgRNAs are added, exerting a synergistic effect on transcriptional activation  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf#Passage 2|[3]]].

### Constraints and Negative Effects of Multiplexing
Despite the potential for synergy, several sources highlight limitations where multiplexing can be less effective or even detrimental:

*   **Steric Hindrance:** Because the p300 core domain is a **relatively large protein**, its size can create spatial constraints  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 8|[6]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 11|[7]]]. If multiple sgRNAs are targeted to adjacent sites too close to one another (e.g., **118 bp apart**), the resulting **steric hindrance** may destabilize the protein complexes on the DNA, potentially resulting in **lower gene expression** than that achieved by a single sgRNA  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf#Passage 3|[8]]].
*   **Non-Additive Effects:** Some studies have observed a **non-additive effect** when dCas9-p300 is targeted to multiple adjacent sites to induce histone acetylation, where the combined activation does not linearly reflect the number of guides used  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 12|[9]]].
*   **Limited Sensitivity on Repetitive Sites:** In exogenous reporter experiments (using the TRE3G promoter with seven binding sites), the enhancement of expression by p300+MV was notably **limited compared to smaller activators** like VP64-based systems, which is attributed to the spatial limitations of the large p300 protein  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 8|[6]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 13|[10]]].

### Summary of Targeted Genes and Cell Types
The effects of multiplexed dCas9-p300 were primarily measured on:
*   **Endogenous Human Genes:** *ASCL1*, *MYOD1*, and *IL1RN* in **HEK293T cells**  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 9|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 1|[11]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf#Passage 2|[12]]].
*   **Endogenous Plant Genes:** *AREB1* in **Arabidopsis** (using the similar AtHAT1 histone acetyltransferase fusion), where tandem targeting was used  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 14|[13]]].
*   **Exogenous Reporters:** Minimal CMV and TRE3G promoters (the latter containing seven binding sites) in **HEK293T cells**  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 10|[4]]].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 6|Pasaje 6]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> activity better than did direct VP64 fusion to the N-terminus of dCas9. dCas9-VP64+MCP-

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 9|Pasaje 9]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> vation by dCas9-VP64 [8, 9] and other CRISPRa systems [30]. Here we focused on 2VP, VP

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf|PDF]]
- Texto literal:
> Validity. When CRISPR/dCas9 carrying activating or repressing structural domains is used to regulate gene expression, the upregulation or knockdown of the gene might not be sufficient to achieve a therapeutic effect. The CRISPRa system is divided into two parts: the sgRNA/Cas9 complex, which plays a targeting role, and the activating structural domain, which enhances transcrip-tion.59,321 In general, when performing gene editing, only one sgRNA targeting the target site will be designed. Maeder et al. designed sgRNAs at four positions near the transcriptional start site of the target gene to obtain higher gene activation efficiency.322 The transcriptional activation efficiency of multiple sgRNAs exerted a certain synergistic effect, and higher efficiency was obtained when more sgRNAs were present. Moreover, the transcriptional activation efficiency of sgRNAs at each position is not the same but is strongly linked to the cell and gene.

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 10|Pasaje 10]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> higher activity than 2VP with multiplexed gRNAs (Fig 4C). Further analyses showed that the

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 11|Pasaje 11]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> regarding the incorporation of the DNA demethylase Tet1-CD for CRISPRa using the SunTag

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf|PDF]]
- Texto literal:
> Challenge of the dCas9 constructs in a GUS reporter system. To evaluate the dCas9HAT construct, we set up a surrogate reporter system based on regulation of GUS reporter gene expression. We used the 170-bp minimal truncated version of the Glycine max ubiquitin promoter, herein designated GmUcesMin28,29. We selected two sgRNAs near the transcription start site (TSS) of GmUcesMin (Fig. 2A, Table S2). The efficiency of dCas9HAT in activating the GUS reporter system was quantified by its enzymatic activity. Seedlings of stably transformed Arabidopsis lines expressing dCas9HAT were incubated with Agrobacterium carrying Ti plasmids to perform transient ectopic expression of GmUcesMin-GUS in combination with the expression of one or two sgRNAs. Significantly elevated enzymatic activity was observed for sgRNA1 (~2.4-fold increase) and sgRNA2 (~2-fold increase), while enzymatic activity was elevated ~1.4-fold for the combination of the two sgRNAs. This result indicates that the expression of dCas9HAT enhanced the expression of the GUS gene in trans when targeted to GmUcesMin promoter. Remarkably, some substantial differences were noted depending on the location of the sgRNA and/or the sgRNA combination. Previous studies have suggested that the distance of the sgRNA from the TSS might influence the transcriptional regulation of the gene of interest. While some studies have reported that a specific sgRNA binding distance from the TSS (−50 bp to +300 bp) corresponds to higher target gene expression30,31, others have pointed out that dCas9 might generate steric hindrance and thus interfere with transcriptional machinery activities21,32. Regarding the construct GmUcesMin, our two sgRNAs are separated only by 118 bp. Considering the 3D conformation of the DNA, the 30 bp length occupied by the dCas9 on DNA33 and the space taken by the HAT domain, a steric hindrance effect could be responsible for destabilizing locally the protein complexes standing on DNA. Compared to the use of only one sgRNA, this collateral effect might result to lower gene expression rather than improve it.

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 12|Pasaje 12]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> plexing in exogenous genes by utilizing the miniCMV promoter reporter, which has only one

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 13|Pasaje 13]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> scription of endogenous and exogenous genes, we generated expression plasmids for dCas9

### Extracto 9
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf|PDF]]
- Texto literal:
> Molecular and phenotypic characterization of dCas9HAT-sgA. We next inquired whether AREB1 gene expression could be regulated by dCas9HAT. We designed two sgRNAs to target the endogenous promoter of AtAREB1 (Fig. 3A). One sgRNA is located at 3′ from the TSS (−479 bp), and the second is in the 5′ UTR (+356 bp). The two sgRNAs (sg-pAREB1.1 and sg-pAREB1.2) were cloned in tandem within a single T-DNA and transformed into the Arabidopsis dCas9HAT transgenic lines to generate dCas9HAT-sgA. We verified AREB1 gene expression in three transgenic lines by real-time qPCR (Fig. 3B). In each experiment, the control line was the parental line, dCas9HAT. We observed a slight but significant 1.7-fold increase in AREB1 expression in the dCas9HAT-sgA1 line and a 2-fold increase in the dCas9HAT-sgA2 line compared to that in the control line, sug- gesting that targeting dCas9HAT to the AREB1 gene could trigger its transcription. Three weeks after germination, the rosette diameter in the dCas9HAT-sgA2 and dCas9HAT-sgA1 plants was ~3-fold smaller than in the controls (Figs 3C, S3A,B). The leaf length was also smaller for both lines, respectively, than in the control line (Fig. S3C). These results suggest that the mutant caused a dwarf phenotype under normal plant growth conditions. They also corroborate phenotypic traits related to drought stress shown by Fujita et al.12, in which the over-expression of the constitutive form of AREB1, AREB1ΔQT, presented smaller phenotypes and the areb1 mutants had larger rosettes. Interestingly, we observed that without water deficit, AREB1 is slightly positively regulated, indicating that dCas9HAT activates AREB1 apart of the context of drought.

### Extracto 10
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 14|Pasaje 14]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> ties, as targets for transcriptional activation of exogenous genes by CRISPRa. As shown in Fig

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf|joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf|tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf|daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/jere_2018_human_pluripotent_reprogramming_with_crispr_activators.pdf|jere_2018_human_pluripotent_reprogramming_with_crispr_activators.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kenly_2020_prevention_of_tumor_risk_associated_with_the_reprogramming.pdf|kenly_2020_prevention_of_tumor_risk_associated_with_the_reprogramming.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]]
