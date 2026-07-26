---
type: reference
status: current
date: 2026-07-24
source: "notebooklm:dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores"
related:
  - "[[Notes/Dashboards/dCas9-p300 vs other activators]]"
---

# Q06 - What gaps remain in these sources regarding a direct head-to-head comparison of dCas9-p300 versus VP64, VPR, and SunTag-p300 specifically at the FTO locus?

Based on the provided sources, there are several significant gaps regarding a direct head-to-head comparison of **dCas9-p300**, **VP64**, **VPR**, and **SunTag-p300** at the **FTO locus**. 

While the sources offer extensive comparisons of these activators at other loci, the following specific gaps remain:

### **1. Total Absence of FTO Activation Data**
Across all 18 sources, the **FTO (Fat Mass and Obesity-associated) locus** is only mentioned in one study, and that study focuses on **gene knockout**, not activation  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kachanov_2025.pdf#Passage 2|[1]]]. 
*   **Source 10 (Kachanov et al., 2025)** investigates the role of m6A regulators on HBV cccDNA and performs an **FTO knockout** using the StCas9 nuclease system to observe effects on pgRNA levels  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kachanov_2025.pdf#Passage 2|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kachanov_2025.pdf#Passage 3|[2]]].
*   Although this same study mentions utilizing **dCas9-p300** for gene activation in its general methodology  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kachanov_2025.pdf#Passage 3|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kachanov_2025.pdf#Passage 1|[3]]], the excerpts provided do not include any data where p300 (or any other activator) is targeted to the *FTO* locus for a comparison of expression levels.

### **2. Non-Existence of 'SunTag-p300' Evaluations**
None of the provided sources evaluate a **SunTag-p300** construct—defined as a SunTag scaffold recruiting multiple p300 catalytic domains.
*   **Source 12 (Kohei et al., 2022)** explores a hybrid system called **p300+MV**, which consists of a direct dCas9-p300 fusion that also recruits **MCP-VP64** via MS2 loops on the gRNA  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 11|[4]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 4|[5]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 12|[6]]]. However, this is distinct from using the SunTag (GCN4 peptide array) to recruit multiple p300 domains.
*   **Source 7 (Christian et al., 2018)** and **Source 15 (Ronghao et al., 2023)** apply the SunTag architecture to other effectors, such as **DNMT3A** (for methylation) or **P65** (for prime editing enhancement), but not to p300  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 3|[7]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/ronghao_2023_enhancement_of_a_prime_editing_system_via_optimal.pdf#Passage 1|[8]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 5|[9]]].
*   The sources suggest that for large proteins like **p300** or **TET1-CD**, signal-amplification systems like SunTag may face **spatial and steric constraints** that limit their effectiveness compared to direct fusions  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 4|[5]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/fatma_2025_comparison_of_dcas9_activator_complexes_for_the_activation.pdf#Passage 11|[10]]].

### **3. Lack of Comparative Context at FTO**
Because there is no activation data for *FTO*, the sources cannot address locus-specific questions such as:
*   **Promoter vs. Enhancer Performance:** Although the sources note that **dCas9-p300 is uniquely capable** of activating genes from distal enhancers while VP64 and VPR are largely promoter-centric  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 1|[11]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/fatma_2025_comparison_of_dcas9_activator_complexes_for_the_activation.pdf#Passage 1|[12]]], this has not been benchmarked at the *FTO* locus, which is known for its complex enhancer-promoter interactions.
*   **Relative Potency:** While **VPR** is consistently identified as the most powerful activator at loci like *NGN3* (256-fold) and *PDX1* (19-fold)  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/fatma_2025_comparison_of_dcas9_activator_complexes_for_the_activation.pdf#Passage 25|[13]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 6|[14]]], it is unknown if this hierarchy holds at *FTO*.
*   **Off-Target Profiles:** Sources demonstrate that modular systems (like SunTag) can reduce off-target effects compared to direct fusions  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 2|[15]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/fatma_2025_comparison_of_dcas9_activator_complexes_for_the_activation.pdf#Passage 16|[16]]], but no genome-wide characterization of these tools has been performed when specifically targeting the *FTO* region.

### **Summary of Target Genes Used for Comparisons**
In contrast to the missing *FTO* data, head-to-head comparisons in these sources are restricted to:
*   **Pancreatic Genes:** *PDX1, NGN3, INS, MAFA, NKX6.2, PAX4*  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/fatma_2025_comparison_of_dcas9_activator_complexes_for_the_activation.pdf#Passage 25|[13]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/fatma_2025_comparison_of_dcas9_activator_complexes_for_the_activation.pdf#Passage 26|[17]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 13|[18]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/agustin_2023_epigenetic_reactivation_of_tumor_suppressor_genes_with_crispra.pdf#Passage 1|[19]]].
*   **Developmental/Neuronal Genes:** *ASCL1, MYOD1, NEUROD1, Neurog2, Sox1*  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 11|[4]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/agustin_2023_epigenetic_reactivation_of_tumor_suppressor_genes_with_crispra.pdf#Passage 4|[20]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/agustin_2023_epigenetic_reactivation_of_tumor_suppressor_genes_with_crispra.pdf#Passage 3|[21]]].
*   **Tumor Suppressors:** *HHIP, MT1M, PZP, TTC36, CPS1, CDKN2A*  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 3|[22]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/mahata_2023_compact_engineered_human_mechanosensitive_transactivation_modules_enable_potent.pdf#Passage 4|[23]]].
*   **General Benchmarks:** *HBG1, TTN, IL1RN, ACE2, CXCR4, OCT4* [25-27].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kachanov_2025.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/kachanov_2025.pdf|PDF]]
- Texto literal:
> Knockout of the FTO eraser gene also led to a significant increase in pgRNA levels (FTO KO2 M: 21.01; p = 0.0002) (Fig. 4B). It was previously found that METTL3/METTL14 knockdown led to a decrease in pgRNA reverse transcription, while FTO knockdown, on the contrary, led to its enhancement. Similarly, double knockdown of METTL3/METTL14 increased the expression of HBc and HBs proteins, while knockdown of ALKBH5 and FTO genes decreased HBc and HBs levels [15].

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kachanov_2025.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/kachanov_2025.pdf|PDF]]
- Texto literal:
> A chimeric protein consisting of dCas9 with p300 histone acetyltransferase fused to it was used to activate gene expression. The dCas9 protein lacks its nucleolytic activity due to point mutations in the nucleolytic domains but retains the ability to target the DNA strand. Such delivery of p300 to the distal enhancer region allows activation of transcription of the target gene [29]. Guide RNAs for gene expression activation were selected for promoter regions by means of the CHOPCHOP software [28] for SpCas9 so that there were no off-target interactions with two or fewer nucleotide mismatches and the target sequence was 20 nucleotides in length (Table 2).

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 11|Pasaje 11]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> activity better than did direct VP64 fusion to the N-terminus of dCas9. dCas9-VP64+MCP-

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf|PDF]]
- Texto literal:
> unambiguously assess the functional consequences of DNA methylation. To address this, we

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/ronghao_2023_enhancement_of_a_prime_editing_system_via_optimal.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/ronghao_2023_enhancement_of_a_prime_editing_system_via_optimal.pdf|PDF]]
- Texto literal:
> P65 improves prime editing at different genomic loci in the PE system To validate the above results, we further assessed the effect of P65 on PE system with base-substitution edits and deletion edits at more genomic loci, including EMX1, PSMB2, HEK2, HIRA, VEGFA, and VISTA. We first transfectedHEK293T cells with vectors encoding 2*GCN4-PE2, P65-scFv, and pegRNAs and measured prime editing results by deep sequencing. Compared with the original PE2 system, the PE2 Suntag system that recruited the P65 protein through protein interaction was

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 5|Pasaje 5]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> regarding the incorporation of the DNA demethylase Tet1-CD for CRISPRa using the SunTag

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|PDF]]
- Texto literal:
> is to locally deposit H3K27ac marks. Therefore, in contrast to the local reduction of enhancer marks by dCas9-LSD1, recruitment of histone acetyl transferase P300 through dCas9 fusion (dCas9-P300) resulted in a significant increase in local H3K27ac levels at enhancer elements142. Importantly, unlike other dCas9-fused transactivators, which can result in induction of gene expression primarily from promoter regions, targeting dCas9-P300 allows significant gene expression induction from both promoter and enhancer regions142. Researchers have also exploited other epigenetic modifiers to manipulate additional epigenetic marks. Among these, dCas9 fusion to the PRDM9 methyltransferase fusion complex has been utilized to manipulate local H3K4me3 marks143. Notably, local induction of H3K4me3, which is a marker of active promoters, was observed to be sufficient to allow re-expression of silenced target genes in various cell types143. Histone de-acetylation has been another strategy to locally manipulate chromatin structure and function. To this end, dCas9 fusion to histone deacetylases (HDAC), specifically full-length HDAC3, has been shown to effectively reduce the H3k27ac at the target loci and reduce the gene expression of the target loci144.

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/fatma_2025_comparison_of_dcas9_activator_complexes_for_the_activation.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/fatma_2025_comparison_of_dcas9_activator_complexes_for_the_activation.pdf|PDF]]
- Texto literal:
> in pancreatic development. To optimize this process, we compared three activator domains

### Extracto 9
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 6|Pasaje 6]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf|PDF]]
- Texto literal:
> with dC9Sun-D3A, compared to pervasive off-target binding and methylation by the dC9-D3A

### Extracto 10
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf|PDF]]
- Texto literal:
> single-chain antibody, scFv-GCN4, subsequently referred to as αGCN4) to be recruited to a

### Extracto 11
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 13|Pasaje 13]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> scription of endogenous and exogenous genes, we generated expression plasmids for dCas9

### Extracto 12
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/agustin_2023_epigenetic_reactivation_of_tumor_suppressor_genes_with_crispra.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/agustin_2023_epigenetic_reactivation_of_tumor_suppressor_genes_with_crispra.pdf|PDF]]
- Texto literal:
> Collectively, these data indicate that epi-drugs derepress a subset of TSGs, albeit non-selectively. Moreo-ver, unexpected significant transcriptional repression was observed for TSGs having basal levels of expression

### Extracto 13
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/agustin_2023_epigenetic_reactivation_of_tumor_suppressor_genes_with_crispra.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/agustin_2023_epigenetic_reactivation_of_tumor_suppressor_genes_with_crispra.pdf|PDF]]
- Texto literal:
> Moreover, CRISPRa outperformed the epi-drug treatments (5-aza or SAHA, all concentrations tested) in upregulating HHIP, MT1M, PZP, TTC36, and CPS1, whereas 5-aza, but not SAHA led to a higher activation of MT1E, miR-122-5p, PTGR1, and TMEM106A com- pared to CRISPRa. Only the highest doses of SAHA (2 and 4 µM) exceeded CRISPRa-based upregulation of PTGR1 and CDKN2A (Additional file 15: Data S4).

### Extracto 14
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> vation by dCas9-VP64 [8, 9] and other CRISPRa systems [30]. Here we focused on 2VP, VP

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/agustin_2023_epigenetic_reactivation_of_tumor_suppressor_genes_with_crispra.pdf|agustin_2023_epigenetic_reactivation_of_tumor_suppressor_genes_with_crispra.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf|christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/fatma_2025_comparison_of_dcas9_activator_complexes_for_the_activation.pdf|fatma_2025_comparison_of_dcas9_activator_complexes_for_the_activation.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kachanov_2025.pdf|kachanov_2025.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/mahata_2023_compact_engineered_human_mechanosensitive_transactivation_modules_enable_potent.pdf|mahata_2023_compact_engineered_human_mechanosensitive_transactivation_modules_enable_potent.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/ronghao_2023_enhancement_of_a_prime_editing_system_via_optimal.pdf|ronghao_2023_enhancement_of_a_prime_editing_system_via_optimal.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/albert_2017_genetic_and_epigenetic_control_of_gene_expression_by.pdf|albert_2017_genetic_and_epigenetic_control_of_gene_expression_by.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/alexander_2022_engineering_the_next_generation_of_car_t_cells.pdf|alexander_2022_engineering_the_next_generation_of_car_t_cells.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/andreas_2020_activation_of_silent_secondary_metabolite_gene_clusters_by.pdf|andreas_2020_activation_of_silent_secondary_metabolite_gene_clusters_by.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/anil_2021_mechanisms_of_enhancer_action_the_known_and_the.pdf|anil_2021_mechanisms_of_enhancer_action_the_known_and_the.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf|chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/jorge_2021_transcription_activation_is_enhanced_by_multivalent_interactions_independent.pdf|jorge_2021_transcription_activation_is_enhanced_by_multivalent_interactions_independent.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf|kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/tessa_2022_a_modular_dcas9_based_recruitment_platform_for_combinatorial.pdf|tessa_2022_a_modular_dcas9_based_recruitment_platform_for_combinatorial.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf|tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/yujuan_2025_dynamic_properties_of_transcriptional_condensates_modulate_crispra_mediated.pdf|yujuan_2025_dynamic_properties_of_transcriptional_condensates_modulate_crispra_mediated.pdf]]
