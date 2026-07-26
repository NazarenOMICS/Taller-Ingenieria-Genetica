---
type: reference
status: current
date: 2026-07-14
source: "notebooklm:dcas9-fto-granulosa/q11-controles-experimentales"
related:
  - "[[Notes/Dashboards/CRISPRa experimental controls]]"
---

# Q06 - What gaps remain in these sources regarding a complete, standardized control panel (non-targeting guide + catalytically dead effector + dCas9-only) specifically validated for dCas9-p300 experiments?

Based on the provided sources, researchers have validated individual components of a rigorous control panel for dCas9-p300 experiments—such as the **p300CD D1398Y** catalytically dead mutant  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 3|[1]]] and **non-targeting sgRNAs**  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/yang_2019_engineered_crispra_enables_programmable_eukaryote_like_gene_activation.pdf#Passage 4|[2]]]—but several gaps remain regarding a **complete, standardized panel** specifically tailored and co-validated for the unique mechanisms of dCas9-p300.

The following gaps in standardization and validation remain in the sources:

### 1. Side-by-Side Comparison of Steric Artifacts (dCas9-only vs. Dead p300)
While sources acknowledge that dCas9 binding alone can cause **transcriptional repression** via steric hindrance  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/kohei_2021_comparative_analysis_and_rational_design_of_dcas9_vp64.pdf#Passage 5|[3]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/kendall_2018_up_down_and_out_optimized_libraries_for_crispra.pdf#Passage 7|[4]]], a gap exists in standardizing a panel that distinguishes the physical bulk of the dCas9 protein from the additional bulk of a dead effector domain.
*   **The "Protein Bulk" Gap:** One study notes that the **TET1CD catalytic inactive mutant** actually decreased gene expression because the dCas9-effector complex physically impeded endogenous transcription factors  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 5|[5]]]. 
*   **The p300 Specificity Gap:** The sources do not explicitly provide a side-by-side validation of **dCas9-only** versus **dCas9-p300-dead** to determine if the relatively large p300 core domain  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 1|[6]]] introduces unique non-catalytic artifacts (such as "clouding" or specific protein-protein interactions) beyond the baseline interference of dCas9 alone  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/kendall_2018_up_down_and_out_optimized_libraries_for_crispra.pdf#Passage 7|[4]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 2|[7]]].

### 2. Standardization of "Neutral" sgRNA Controls for Epigenetic Readouts
Most standardized non-targeting controls (NTCs) were optimized for **viability screens** using VP64-based systems (e.g., the Calabrese library) to measure fitness effects  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/yang_2019_engineered_crispra_enables_programmable_eukaryote_like_gene_activation.pdf#Passage 4|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/albert_2013_multiplexed_activation_of_endogenous_genes_by_crispr_on.pdf#Passage 3|[8]]]. 
*   **Readout Gap:** There is a gap in validated NTC sets specifically screened for **epigenetic neutrality**. While Source 11 uses mismatched guides as negative controls for *Foxp3*  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 3|[9]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 4|[10]]], the sources lack a "standardized" set of 1,000 NTCs (similar to those in Source 7) that have been rigorously proven *not* to affect global histone acetylation levels when used with the p300 core  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf#Passage 3|[11]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/kohei_2021_comparative_analysis_and_rational_design_of_dcas9_vp64.pdf#Passage 6|[12]]].

### 3. Footprinting and Global Off-Target Standardization
The sources highlight a critical gap in understanding the **global epigenetic footprint** of dCas9-p300. 
*   **Off-Target Validation Gap:** While dCas9-p300 is shown to be highly specific at the transcriptome level  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/kohei_2021_comparative_analysis_and_rational_design_of_dcas9_vp64.pdf#Passage 1|[13]]], the sources note that other epigenetic modifiers (like dCas9-fused methyltransferases) can leave **global off-target footprints** independent of sgRNA targeting  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/yang_2019_engineered_crispra_enables_programmable_eukaryote_like_gene_activation.pdf#Passage 5|[14]]]. 
*   **Missing Control:** A standardized protocol for using a dead effector and dCas9-only to baseline these "low-level but global" epigenetic modifications across the entire epigenome—rather than just the transcriptome—is not fully established in these excerpts [15, 16].

### 4. Dose-Response and Saturation Standards for p300
There is a gap in standardizing the **titration of p300 components** to account for its high potency.
*   **Saturation Gap:** Unlike VP64, the p300 core can be more potent than traditional activation domains [17]. However, sources indicate that excessive recruitment of large proteins can lead to **spatial constraints** that limit activation [18, 19]. 
*   **Standardization Gap:** A standard control panel does not yet include a "dose-response baseline" that identifies the exact concentration where the benefits of p300 recruitment are negated by the steric interference of the large complex, which would be essential for a "standardized" experimental setup [19, 20].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q11-controles-experimentales/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|PDF]]
- Texto literal:
> Statistical analysis All values are presented as the means ± standard devia- tions (SDs). Unpaired Student’s t tests were used, and p < 0.05 was defined as statistically significant.

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/yang_2019_engineered_crispra_enables_programmable_eukaryote_like_gene_activation.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q11-controles-experimentales/yang_2019_engineered_crispra_enables_programmable_eukaryote_like_gene_activation.pdf|PDF]]
- Texto literal:
> Given that many CRISPRa systems in eukaryotes were built by fusing the activation domain to dCas9 directly3,5, we asked if the same could be applied to the PspF activation domain. The HTH domain truncated PspF was fused to dCas9 and CRISPRa was attempted, but was unsuccessful (Supplementary Fig. 1c). This result was within expectation given that PspF must assemble as a hexamer to function, and dCas9 probably interfered with the assembly process as it was relatively bulky24,25.

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/kendall_2018_up_down_and_out_optimized_libraries_for_crispra.pdf#Passage 7|Pasaje 7]] | [[Research/Papers/dcas9-fto-granulosa/q11-controles-experimentales/kendall_2018_up_down_and_out_optimized_libraries_for_crispra.pdf|PDF]]
- Texto literal:
> We also used the same selection heuristics as for CRISPRi (Supplementary Table 2), successively relaxing location, on-target sequence score, and potential off-targets to select the six best sgRNAs for each gene, which were then divided into Set A (the top three sgRNAs) and Set B (the next three sgRNAs). This library, named Calabrese, was cloned into the pXPR_502 library vector, which contains the modified tracrRNA described above as well as the transcriptional activation domains p65-HSF1. Unlike CRISPRko and CRISPRi, CRISPRa lacks an obvious gold standard gene set with which to assess screen performance in negative selection screens. Previously, the SAM system was screened for vemurafenib resistance in A375 cells20; this library contains 3 sgRNAs per gene and was screened in duplicate in two vectors, one of which conferred zeocin resistance and one puromycin resistance; the pairwise correlation for biological replicates with the same selection marker was 0.04 and 0.24, respectively.

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 5|Pasaje 5]] | [[Research/Papers/dcas9-fto-granulosa/q11-controles-experimentales/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|PDF]]
- Texto literal:
> In this study, we established two epigenome-modifying systems based on CRISPR-dCas9 technology and applied them to the Foxp3 gene locus. We aimed to investigate the cross-talk of epigenome editing and endogenous cellular responses in primary immune cells and to lay a foundation for future clinical development. To stabilize Foxp3 expression in artificially epigenome-edited iTregs: dCas9 fused with TET1CD was targeted to the Foxp3 CNS2 locus, and dCas9 fused with p300CD to the Foxp3 promoter locus. We designed 10 gRNA sequences in each locus, screened effective sequences in T cell lines 68-41, and then applied them to mouse primary T cells. We confirmed that both systems with specific gRNAs could induce epigenetic modifications in cultured cell lines. In primary T cells, dCas9-TET1CD partially demethylated the CNS2 locus under iTreg conditions, but Foxp3 expression was not robustly stabilized by inflammatory cytokine stimuli. In contrast, dCas9-p300CD strongly activated and stabilized Foxp3 expression, particularly with TGF-β, even under inflammatory conditions.

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q11-controles-experimentales/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|PDF]]
- Texto literal:
> is to locally deposit H3K27ac marks. Therefore, in contrast to the local reduction of enhancer marks by dCas9-LSD1, recruitment of histone acetyl transferase P300 through dCas9 fusion (dCas9-P300) resulted in a significant increase in local H3K27ac levels at enhancer elements142. Importantly, unlike other dCas9-fused transactivators, which can result in induction of gene expression primarily from promoter regions, targeting dCas9-P300 allows significant gene expression induction from both promoter and enhancer regions142. Researchers have also exploited other epigenetic modifiers to manipulate additional epigenetic marks. Among these, dCas9 fusion to the PRDM9 methyltransferase fusion complex has been utilized to manipulate local H3K4me3 marks143. Notably, local induction of H3K4me3, which is a marker of active promoters, was observed to be sufficient to allow re-expression of silenced target genes in various cell types143. Histone de-acetylation has been another strategy to locally manipulate chromatin structure and function. To this end, dCas9 fusion to histone deacetylases (HDAC), specifically full-length HDAC3, has been shown to effectively reduce the H3k27ac at the target loci and reduce the gene expression of the target loci144.

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q11-controles-experimentales/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|PDF]]
- Texto literal:
> These aforementioned locus-specific epigenetic manipulation strategies are based on overexpression of a dCas9-fused epigenetic modifier complex. Such tools have been shown to specifically manipulate the expression of the target loci. However, whether overexpression of the fusion epigenetic complexes may leave a low level but global epigenetic footprint in the genome, as noted for the dCas9–DNMT3A fusion complex134, is yet to be determined. Therefore, novel strategies that enable local recruitment of endogenous epigenetic machineries may provide a higher precision in epigenetic editing. To this end, novel approaches such as Fkbp/Frb-based inducible recruitment for epigenome editing by Cas9 (FIRE–Cas9)145 may provide higher specificity in epigenetic editing by recruiting endogenous chromatin regulators.

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q11-controles-experimentales/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|PDF]]
- Texto literal:
> Identifying the causal link between epigenetic marks and gene expression remains a central goal of chromatin biology. Thus, these aforementioned studies using dCas9 as a guidable platform to edit locus-specific epigenetic information will be an indispensable tool to achieve this. Now that the tools that enable us to alter the epigenome are in place, the next phase is to utilize them to better characterize regulatory elements and cellular states. To this end, researchers have already applied dCas9-based epigen-ome-editing tools for a number of exciting purposes including high-throughput screenings to characterize functional distal enhancers146, targeted reprogramming of lineage specifica-tion147,148, generation of induced pluripotent stem cells149, and reversal of HIV latency150. One of the remaining challenges is to elucidate the causal relationship between the presence of an epigenetic mark and its regulatory impact. Since the dCas9-fused epigenetic modifier remains associated with the target site, it is unclear whether the regulatory activity is due to the induced epigenetic mark or the complex. To this end, recent efforts using rapid and reversible epigenome-editing approaches are highly notable145. Future studies that enable rapid degradation of the targeting complex at the target site, such as with auxin-inducible degron technology151, should allow us to further characterize the functional consequences of epigenetic marks and investigate the associated temporal epigenetic memory for each mark.

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q11-controles-experimentales/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf|PDF]]
- Texto literal:
> The activation of promoters via histone H3K27 acetylation through the use of dCas9p300Core domains has been evaluated in animal cells, and the dCas9p300Core domains have been shown to be more potent than activation domains21,34,35. Further studies have also reported that the over-expression of histone deacetylases (HDACs) plays a role in the ABA response and that the use of an HDAC inhibitor induces hyperacetylation and increases AREB1

### Extracto 9
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/kohei_2021_comparative_analysis_and_rational_design_of_dcas9_vp64.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q11-controles-experimentales/kohei_2021_comparative_analysis_and_rational_design_of_dcas9_vp64.pdf|PDF]]
- Texto literal:
> the TRE3G promoter. On the other hand, dCas9-p300+MCP-VP64, which has the largest size, showed only limited increases in activity with increased numbers of binding sites in the TRE3G promoter compared to other systems.

### Extracto 10
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/yang_2019_engineered_crispra_enables_programmable_eukaryote_like_gene_activation.pdf#Passage 5|Pasaje 5]] | [[Research/Papers/dcas9-fto-granulosa/q11-controles-experimentales/yang_2019_engineered_crispra_enables_programmable_eukaryote_like_gene_activation.pdf|PDF]]
- Texto literal:
> We observed that our transformants from the library had colonies with different intensities of purple color, which directly reflected the individual differences in violacein production (Fig. 6b). We then classified colonies into three bins of violacein production, and for each bin, retrieved their individual sgRNA transcription profiles by sequencing the sgRNA generator cassettes from the five colonies (Fig. 6b). We ended up analyzing four profiles for each bin (see Online Methods). Among the three genes experiencing different activation patterns, the promoter strengths for sgRNA activating vioA correlated most with violacein production (Fig. 6d), suggesting its role as the limiting factor in the production pathway. It should be noted that the overall strength of the violacein pathway was heavily influence by the level of the dxCas9 and the activator (Supplementary Fig. 15). These two factors thus served as additional gain tuning knobs for optimization of the entire pathway.

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/albert_2013_multiplexed_activation_of_endogenous_genes_by_crispr_on.pdf|albert_2013_multiplexed_activation_of_endogenous_genes_by_crispr_on.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf|joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/kendall_2018_up_down_and_out_optimized_libraries_for_crispra.pdf|kendall_2018_up_down_and_out_optimized_libraries_for_crispra.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/kohei_2021_comparative_analysis_and_rational_design_of_dcas9_vp64.pdf|kohei_2021_comparative_analysis_and_rational_design_of_dcas9_vp64.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/yang_2019_engineered_crispra_enables_programmable_eukaryote_like_gene_activation.pdf|yang_2019_engineered_crispra_enables_programmable_eukaryote_like_gene_activation.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/charleen_2021_tissue_specific_activation_of_gene_expression_by_the.pdf|charleen_2021_tissue_specific_activation_of_gene_expression_by_the.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/hongyi_2020_applications_of_genome_editing_technology_in_the_targeted.pdf|hongyi_2020_applications_of_genome_editing_technology_in_the_targeted.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/josh_2019_mitigation_of_off_target_toxicity_in_crispr_cas9.pdf|josh_2019_mitigation_of_off_target_toxicity_in_crispr_cas9.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/karthik_2021_cancer_immune_evasion_through_loss_of_mhc_class.pdf|karthik_2021_cancer_immune_evasion_through_loss_of_mhc_class.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/leena_2017_gene_editing_and_crop_improvement_using_crispr_cas9.pdf|leena_2017_gene_editing_and_crop_improvement_using_crispr_cas9.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/lesca_2016_circular_non_coding_rna_anril_modulates_ribosomal_rna.pdf|lesca_2016_circular_non_coding_rna_anril_modulates_ribosomal_rna.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/rachel_2018_plant_growth_promoting_rhizobacteria_context_mechanisms_of_action.pdf|rachel_2018_plant_growth_promoting_rhizobacteria_context_mechanisms_of_action.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/sarah_2025_epigenetic_motifs_distinguishing_endogenous_from_exogenous_retroviral_integrants.pdf|sarah_2025_epigenetic_motifs_distinguishing_endogenous_from_exogenous_retroviral_integrants.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/simon_2017_rapid_and_reversible_epigenome_editing_by_endogenous_chromatin.pdf|simon_2017_rapid_and_reversible_epigenome_editing_by_endogenous_chromatin.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/vidisha_2013_long_noncoding_rna_malat1_controls_cell_cycle_progression.pdf|vidisha_2013_long_noncoding_rna_malat1_controls_cell_cycle_progression.pdf]]
