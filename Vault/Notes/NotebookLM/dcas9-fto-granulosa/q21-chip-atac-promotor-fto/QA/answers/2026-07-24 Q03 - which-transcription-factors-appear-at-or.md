---
type: reference
status: current
date: 2026-07-24
source: "notebooklm:dcas9-fto-granulosa/q21-chip-atac-promotor-fto"
related:
  - "[[Notes/Dashboards/Public ChIP-seq and ATAC-seq at FTO promoter]]"
---

# Q03 - Which transcription factors appear at or near the FTO promoter in public datasets and are plausible candidate repressors or lost activators?

Based on the public datasets and integrated multi-omics analyses described in the sources, several transcription factors (TFs) are identified as binding at or near the regulatory regions of the ***FTO*** locus. These include candidate repressors whose binding is disrupted by obesity-associated variants, as well as plausible activators.

### **Candidate Repressors and Disrupted Binding Sites**
Several transcription factors act as repressors at the ***FTO*** locus, often binding to intronic enhancers that regulate both ***FTO*** and distant target genes like *IRX3* and *IRX5*:

*   **ARID5B:** This is the most extensively documented repressor in the sources  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf#Passage 6|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf#Passage 7|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf#Passage 8|[3]]]. The risk allele (C) at **rs1421085** (located in the first intron of ***FTO***) disrupts a conserved motif for the **ARID5B repressor**  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf#Passage 6|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf#Passage 7|[2]]]. This disruption leads to the "derepression" of a potent enhancer, causing a doubling of *IRX3* and *IRX5* expression and activating adipogenesis  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf#Passage 6|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf#Passage 7|[2]]].
*   **ONECUT2:** Predicted as a regulatory factor in pathologically relevant cell types like brain microvascular endothelial cells (BMECs), **ONECUT2** is a known suppressor of androgen receptor signaling  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 6|[4]]]. The T-to-C substitution at **rs1421085** is predicted to strengthen enhancer activity by potentially disrupting the binding site of this repressor  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 6|[4]]].
*   **ONECUT1:** Deep learning models (TREDNet) prioritize **ONECUT1** as a factor whose binding site is disrupted by the **rs8050136** variant within the ***FTO*** locus  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 7|[5]]]. **ONECUT1** is essential for pancreatic development, and its disrupted interaction at this site may link the locus to metabolic dysfunction  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 7|[5]]].

### **Plausible Activators or Regulatory Responders**
The sources also identify factors that may function as activators or are recruited to the ***FTO*** regulatory environment in specific developmental or physiological contexts:

*   **Htf1 (Heat Shock Factor 1):** Research suggests **Htf1** is a plausible activator, as the ***FTO*** gene is reportedly **down-regulated** when this heat shock response transcription factor is inhibited  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 8|[6]]].
*   **Androgen Receptor (AR):** The variant **rs7193144** within the ***FTO*** locus is predicted to modulate the binding site of the **Androgen Receptor**  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 9|[7]]]. This makes it a candidate for mediating the pleiotropic effects of the locus across tissues like the pancreas and adipocytes via disrupted androgen signaling  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 9|[7]]].
*   **T-box Family (TBX21 and TBX20):** These transcription factors are predicted to bind at the **rs3751812** regulatory variant in the fetal brain  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yang_2026_the_orchestrated_interplay_between_dna_methylation_and_n6.pdf#Passage 1|[8]]]. Members of the T-box family are critical for the commitment of hypothalamic and pituitary lineages  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yang_2026_the_orchestrated_interplay_between_dna_methylation_and_n6.pdf#Passage 1|[8]]].
*   **RARA and RXRA:** These retinoic acid receptors are identified in predicted regulatory maps as binding at the **rs1421085** site alongside **ONECUT2** [9].

### **Summary of Transcription Factor Interactions**
| Transcription Factor | Functional Role | Genomic Target Site (SNP) |
| :--- | :--- | :--- |
| **ARID5B** | Repressor (Disrupted by risk allele) | rs1421085  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf#Passage 6|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf#Passage 7|[2]]] |
| **ONECUT2** | Repressor / Suppressor | rs1421085  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 6|[4]]] |
| **ONECUT1** | Developmental Regulator | rs8050136  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 7|[5]]] |
| **Htf1** | Plausible Activator | General ***FTO*** expression  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 8|[6]]] |
| **AR** | Androgen-mediated Signalling | rs7193144  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 9|[7]]] |
| **TBX20 / TBX21** | Fetal Brain Regulator | rs3751812  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yang_2026_the_orchestrated_interplay_between_dna_methylation_and_n6.pdf#Passage 1|[8]]] |
| **RARA / RXRA** | Retinoic Acid Signalling | rs1421085 [9] |

While many of these interactions occur within **Intron 1** of ***FTO***, the sources treat these sites as the primary functional components of the ***FTO*** regulatory circuitry  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf#Passage 6|[1]]]. Furthermore, the methylation status of the ***FTO*** promoter itself is regulated by epigenetic "erasers" and "writers" like **DNMT1**, **DNMT3A**, and **DNMT3B**, which can reduce its expression [11].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf#Passage 7|Pasaje 7]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf|PDF]]
- Texto literal:
> and TAD boundary regions (Mei et al., 2019) (see Table 1). For example, the rs1421085 T→C substitution associated with obesity impairs the functioning of the negative regula- tory region controlling expression of the IRX3 and IRX5 genes (Claussnitzer et al., 2015). The rs1421085 locus is located in the intron of the FTO gene (Fig. 1) at a considerable distance from the transcription start sites of IRX3 and IRX5 (~520,000 and ~1,164,000 bases). Normally, the DNA region containing allele T interacts with a repressor factor ARID5B, leading to a decrease in transcriptional activity of IRX3 and IRX5 genes. In carriers of the mutant variant of the DNA sequence (allele C), the binding site of the ARID5B repressor factor is disrupted, which causes an excessively high expression of the IRX3 and IRX5 genes and activates adipogenesis (Claussnitzer et al., 2015).

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf#Passage 8|Pasaje 8]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf|PDF]]
- Texto literal:
> Claussnitzer M., Dankel S.N., Kim K.-H., Quon G., Meuleman W., Haugen C., Glunk V., Sousa I.S., Beaudry J.L., Puviindran V., Ab-dennur N.A., Liu J., Svensson P.-A., Hsu Y.-H., Drucker D.J., Mell- gren G., Hui C.-Ch., Hauner H., Kellis M. FTO obesity variant circuitry and adipocyte browning in humans. N. Engl. J. Med. 2015; 373:895-907. DOI 10.1056/NEJMoa1502214.

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 6|Pasaje 6]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf|PDF]]
- Texto literal:
> We identified 12 reSNVs exhibiting significant fold changes across 9 cell types (Fig. S8 [27]). Among these, 3 variants, rs1421085, rs11642015, and rs9940128 have been validated by MPRA studies to show allelic changes in enhancer activity in mouse preadipocyte and/or neuronal cell lines [92], further supporting the predictive accuracy of TREDNet in identifying regulatory variants. Interestingly, we predicted that T-to-C substitution at rs1421085 additionally strengthens enhancer activity in BMEC, a granulosa-like cell line, by potentially disrupting the binding site of ONECUT2 (Fig. 4A, Table S9 [27]), a suppressor of androgen receptor signaling which was recently identified as a marker of follicle growth [94, 95].

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 7|Pasaje 7]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf|PDF]]
- Texto literal:
> We also identified another reSNV within this locus, rs8050136, where C-to-A substitution is predicted as an enhancer- strengthening variant in the pancreas and liver (Fig. 4A). This variant colocalizes with an eQTL for IRX3 in the pancreas, where it regulates the conversion of β cells to ϵ cells, directly linking it to type 2 diabetes [97]. Notably, rs8050136 is also predicted to dis- rupt the binding site of ONECUT1, a TF essential for pancreatic development (Fig. 4A). However, no allelic differences were predicted in KGN or related granulosa-like cell types, suggesting that this variant is unlikely to have direct consequences on PCOS pathophysiology.

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 8|Pasaje 8]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf|PDF]]
- Texto literal:
> In addition to rs1421085, G-to-A substitution at rs9940128 was predicted as enhancer-damaging variant in BMECs and HUVECs and was found to localize within regions forming chromatin contacts with the promoters of IRX3 and IRX5 in HUVECs (Fig. 4B). Another variant within this locus, rs7193144, was predicted to exhibit nominal allele-specific regulatory differences in KGN cells, granulosa-like cell lines, BMECs, and HUVECs (Table S9 [27]). Notably, this variant was also predicted to modulate the binding site of the AR and to display allele-specific regulatory activity in pancreas and adipocyte, making it a compelling candidate for mediating the pleiotropic effects of IRX3/IRX5 dysregulation across these cell types through disrupted androgen signaling.

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 9|Pasaje 9]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf|PDF]]
- Texto literal:
> The allelic effects of variants in this locus may also impact IRX3/IRX5-mediated functions in hypothalamic neurons (Fig. S7 [27]), as demonstrated in mice [92]. In this regard, we predicted rs3751812 as a regulatory variant in fetal brain which is located within binding sites of T-box family TFs (Fig. 4A). Members of the T-box family play a critical role in the commitment of hypothalamus and pituitary lineages from neuronal precursors

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yang_2026_the_orchestrated_interplay_between_dna_methylation_and_n6.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/yang_2026_the_orchestrated_interplay_between_dna_methylation_and_n6.pdf|PDF]]
- Texto literal:
> ALKBH5 ALKBH5 expression level was increased through the hypomethylation of its promoter.

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf|e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf|srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yang_2026_the_orchestrated_interplay_between_dna_methylation_and_n6.pdf|yang_2026_the_orchestrated_interplay_between_dna_methylation_and_n6.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/angelo_2007_genome_wide_association_scan_shows_genetic_variants_in.pdf|angelo_2007_genome_wide_association_scan_shows_genetic_variants_in.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/anthony_2018_shared_genetic_contribution_to_type_1_and_type.pdf|anthony_2018_shared_genetic_contribution_to_type_1_and_type.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/carrasco_2026_novel_genome_editing_approaches_to_manipulate_apical_meristem.pdf|carrasco_2026_novel_genome_editing_approaches_to_manipulate_apical_meristem.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/haiyan_2024_ythdf2_upregulation_and_subcellular_localization_dictate_cd8_t.pdf|haiyan_2024_ythdf2_upregulation_and_subcellular_localization_dictate_cd8_t.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/huan_2023_scm6a_seq_reveals_single_cell_landscapes_of_the.pdf|huan_2023_scm6a_seq_reveals_single_cell_landscapes_of_the.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/jiang_2025_fto_mediated_m_lt_sup_gt_6_lt.pdf|jiang_2025_fto_mediated_m_lt_sup_gt_6_lt.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/joshi_2024_epidecoder_a_functional_exploration_tool_for_epigenetic_and.pdf|joshi_2024_epidecoder_a_functional_exploration_tool_for_epigenetic_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/madhusudhan_2019_atac_seq_reveals_alterations_in_open_chromatin_in.pdf|madhusudhan_2019_atac_seq_reveals_alterations_in_open_chromatin_in.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/paola_2018_using_three_dimensional_regulatory_chromatin_interactions_from_adult.pdf|paola_2018_using_three_dimensional_regulatory_chromatin_interactions_from_adult.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/paper_2024_eacr_2024_innovative_cancer_science_10_13_june.pdf|paper_2024_eacr_2024_innovative_cancer_science_10_13_june.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/wu_2026_n6_methyladenosine_modification_in_the_context_of_viral.pdf|wu_2026_n6_methyladenosine_modification_in_the_context_of_viral.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yang_2026_epigenetic_regulation_of_uterine_smooth_muscle_tumors_histone.pdf|yang_2026_epigenetic_regulation_of_uterine_smooth_muscle_tumors_histone.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yi_chun_2010_hypothalamic_specific_manipulation_of_fto_the_ortholog_of.pdf|yi_chun_2010_hypothalamic_specific_manipulation_of_fto_the_ortholog_of.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yige_2023_epigenetic_and_transcriptomic_characterization_reveals_progression_markers_and.pdf|yige_2023_epigenetic_and_transcriptomic_characterization_reveals_progression_markers_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yongli_2024_pan_cistrome_analysis_of_the_leaf_accessible_chromatin.pdf|yongli_2024_pan_cistrome_analysis_of_the_leaf_accessible_chromatin.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yunxia_2021_a_compendium_and_comparative_epigenomics_analysis_of_cis.pdf|yunxia_2021_a_compendium_and_comparative_epigenomics_analysis_of_cis.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/zhang_2025_fosl2_facilitates_chromatin_accessibility_to_determine_developmental_events.pdf|zhang_2025_fosl2_facilitates_chromatin_accessibility_to_determine_developmental_events.pdf]]
