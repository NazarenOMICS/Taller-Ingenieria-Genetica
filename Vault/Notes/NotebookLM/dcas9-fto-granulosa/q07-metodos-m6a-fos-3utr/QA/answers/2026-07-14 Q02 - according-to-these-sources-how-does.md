---
type: reference
status: current
date: 2026-07-14
source: "notebooklm:dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr"
related:
  - "[[Notes/Dashboards/m6A methods FOS 3-UTR]]"
---

# Q02 - According to these sources, how does the SELECT method (single-base elongation- and ligation-based qPCR amplification) work for site-specific m6A quantification, and how does its resolution compare to MeRIP?

The **SELECT method** (single-base elongation- and ligation-based qPCR amplification) is a site-specific technique used to quantify m6A modification at specific adenosine residues  [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf#Passage 2|[2]]].

### **How the SELECT Method Works**
The method relies on the ability of m6A modifications to hinder the efficiency of DNA polymerase and ligase  [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/zhiyuan_2023_exon_intron_boundary_inhibits_m6a_deposition_enabling_m6a.pdf#Passage 1|[3]]]. The process involves the following steps:

*   **Annealing:** Total RNA is mixed with two specially designed DNA probes, known as **Up and Down primers**, which are complementary to the sequences flanking the interrogated adenosine site  [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf#Passage 3|[4]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/yang_2022_chronic_corticosterone_disrupts_the_circadian_rhythm_of_crh.pdf#Passage 1|[5]]].
*   **Elongation and Ligation:** An enzyme mixture containing **Bst 2.0 DNA polymerase**, **SplintR ligase**, and ATP is added to the annealed RNA-DNA complex  [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/yang_2022_chronic_corticosterone_disrupts_the_circadian_rhythm_of_crh.pdf#Passage 1|[5]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf#Passage 4|[6]]]. 
*   **Hindrance by m6A:** The DNA polymerase elongates the Up primer by a single base to meet the Down primer, and the ligase then joins them. However, if the target adenosine is **m6A-modified**, this elongation and ligation process is significantly impeded  [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/zhiyuan_2023_exon_intron_boundary_inhibits_m6a_deposition_enabling_m6a.pdf#Passage 1|[3]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/yang_2022_chronic_corticosterone_disrupts_the_circadian_rhythm_of_crh.pdf#Passage 1|[5]]].
*   **qPCR Quantification:** The resulting ligated DNA products are amplified and quantified using **real-time qPCR** with common primers  [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf#Passage 2|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf#Passage 4|[6]]]. 
*   **Data Interpretation:** Because the modification blocks the reaction, the abundance of the final qPCR products is **inversely proportional** to the level of m6A modification at that specific site  [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf#Passage 2|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/zhiyuan_2023_exon_intron_boundary_inhibits_m6a_deposition_enabling_m6a.pdf#Passage 1|[3]]].

### **Resolution Comparison: SELECT vs. MeRIP**
The SELECT method offers significantly higher resolution than traditional MeRIP techniques:

*   **SELECT Resolution:** It provides **single-nucleotide (site-specific) resolution**, allowing researchers to interrogate and quantify modification levels at a precise adenosine residue  [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/hao_2024_mettl3_drives_heart_failure_by_regulating_spp1_and.pdf#Passage 1|[7]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/mengnuo_2020_the_emerging_roles_of_n6_methyladenosine_m6a_deregulation.pdf#Passage 1|[8]]].
*   **MeRIP Resolution:** In contrast, MeRIP (both MeRIP-seq and MeRIP-qPCR) identifies enriched **"peaks"** or regions rather than specific modified bases  [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 1|[9]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/mengnuo_2020_the_emerging_roles_of_n6_methyladenosine_m6a_deregulation.pdf#Passage 2|[10]]]. Its resolution is limited by the size of the RNA fragments used, typically localizing the modification to a window of **100–200 nucleotides**  [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 1|[9]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/mengnuo_2020_the_emerging_roles_of_n6_methyladenosine_m6a_deregulation.pdf#Passage 2|[10]]].

While SELECT provides superior resolution for individual sites, it requires prior knowledge of the target site (often predicted by tools like SRAMP or identified via broad MeRIP-seq screens), whereas MeRIP-seq can be used for unbiased transcriptome-wide mapping  [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/hao_2024_mettl3_drives_heart_failure_by_regulating_spp1_and.pdf#Passage 1|[7]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/mengnuo_2020_the_emerging_roles_of_n6_methyladenosine_m6a_deregulation.pdf#Passage 1|[8]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/neha_2026_a_novel_method_for_the_identification_and_quantification.pdf#Passage 1|[11]]].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf|PDF]]
- Texto literal:
> methylation, validation assay, specific quantification of m6a rna modification, m6a rna modification, specific m6a modification,

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/zhiyuan_2023_exon_intron_boundary_inhibits_m6a_deposition_enabling_m6a.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/zhiyuan_2023_exon_intron_boundary_inhibits_m6a_deposition_enabling_m6a.pdf|PDF]]
- Texto literal:
> m6A quantification by SELECT method The constructs of minigenes were transfected to HEK293T, and total RNA was extracted after 48 h. The elongation and ligation-based qPCR amplification method SELECT30 was used to quantify the m6A modification. For each RAC site in mRNA, the Ct value of m6A sites was first normalized to two non-RAC sites at each construct to calculate the m6A signal level for each site; the fold change of intensity for each m6A site was calculated by comparing their normalized Ct

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf|PDF]]
- Texto literal:
> specific quantification of m6A RNA modification using total RNA, followed by qPCR-based detection of SELECT

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/yang_2022_chronic_corticosterone_disrupts_the_circadian_rhythm_of_crh.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/yang_2022_chronic_corticosterone_disrupts_the_circadian_rhythm_of_crh.pdf|PDF]]
- Texto literal:
> added to the membrane for 2 h at room temperature with gentle shaking and then developed with enhanced chemiluminescence. Methylene blue staining was used to verify that equal amount mRNA spotted on the membrane.

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/hao_2024_mettl3_drives_heart_failure_by_regulating_spp1_and.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/hao_2024_mettl3_drives_heart_failure_by_regulating_spp1_and.pdf|PDF]]
- Texto literal:
> Mettl3, we employed SRAMP prediction server (https://www.cuilab.cn/sramp), a sequence-based m6A modi cation site predictor, and found three sites in Spp1 mRNA, at positions 18, 309, and 559, and one site in Fos mRNA, at position 786 (Fig. 5g). Then we used single-base elongation-and ligation-based qPCR ampli cation method (SELECT) assay to examine whether Mettl3 undergoes m6A modi cation through two sites (Spp1 mRNA: position 18; Fos mRNA: position 786). The results showed that Mettl3 increased the m6A modi cation of Spp1 and Fos at those two positions (Fig. 5h, i). These data

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/mengnuo_2020_the_emerging_roles_of_n6_methyladenosine_m6a_deregulation.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/mengnuo_2020_the_emerging_roles_of_n6_methyladenosine_m6a_deregulation.pdf|PDF]]
- Texto literal:
> Future prospects New m6A profiling technologies m6A detection and quantification can be achieved by high-speed liquid chromatography after labeling with radioactive [methyl-H3] methionine or LC-MS/MS with deuterium-labeled AdoMet [32, 81]. These methods allow the detection and comparison of the overall m6A level with high sensitivity. However, sequence-specific information is lost during RNase digestion; therefore, the above methods are not suitable for studying m6A modification at specific adenosine residues. SELECT, a single-base elongation and ligation-based qPCR amplification method, has been developed for measuring m6A levels at specific adenosine residues [82]. SELECT is a flexible and convenient approach and is expected to facilitate the detailed characterization of site-specific m6A modifications in the future. Beyond site-specific studies, many groups have also developed various highthroughput assays to delineate the m6A modification profiles on a transcriptome-wide scale. Methylated RNA immunoprecipitation sequencing (MeRIP-Seq or m6A-seq) is the mainstay method for transcriptome-wide m6A profiling. This technique, analogous to ChIP-Seq in the mapping of histone modifications, relies on a specific anti-m6A antibody to pull down m6A-containing RNA fragments, which can then be mapped by next generation sequencing (NGS). Through this approach, more than 10,000 putative m6A modification sites have been identified in the human transcriptome, more commonly

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf|PDF]]
- Texto literal:
> The first and most widely-used method to enable transcriptome-wide studies of m6A, MeRIP-seq or m6A-seq, involves the immunoprecipitation of m6A-modified RNA fragments followed by peak detection through comparison to background gene coverage16,17. A second method was developed in 2015, miCLIP or m6A-CLIP, which involves crosslinking at the site of antibody binding to induce mutations during reverse transcription for single-nucleotide detection of methylated bases2,18. MeRIP-seq is still more often used than miCLIP, despite less precise localization of m6A to peak regions of approximately 50–200 base pairs that can contain multiple DRAC motifs, since it follows a simpler protocol, requires less starting material, and generally produces higher coverage of more transcripts. Antibodies for m6A can also detect a second base modification, N6,2′-O-dimethyladenosine (m6Am), found at a lower abundance than m6A and located at the 5′ ends of select transcripts15,18. We thus refer to the base modifications detected through MeRIP-seq collectively as m6A(m), although most are likely m6A. As of late 2018, over fifty studies used MeRIP-seq to detect m6A(m) in mammalian mRNA (Supplementary Table 1).

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/neha_2026_a_novel_method_for_the_identification_and_quantification.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/neha_2026_a_novel_method_for_the_identification_and_quantification.pdf|PDF]]
- Texto literal:
> low resolution, antibody-associated bias, higher RNA input requirements, and the need for next-generation sequencing infrastructure [31]. Higher-resolution approaches, including miCLIP, SCARLET, SELECT, DART-seq, GLORI, and enzyme-based methods such as MAZTER-seq, enable site- and transcript-specific detection of m6A modifications. However, these methods involve complex workflows and require specialized reagents, recombinant proteins, or motif-dependent detection strategies [30]. Sequencing-based approaches depend on deep sequencing to obtain sufficient coverage and statistical significance, making them expensive and less practical for routine laboratory use [34]. Lim-ited coverage and technical variability may also increase false-positive and false-negative detection rates and affect reproducibility across studies [34–37]. To address these limitations, we have developed a cost-effective, ELISA-based colorimetric quantification method termed Methylation6A Quantification for Genes (MAQ-G), incorporating comple- mentary capture oligonucleotides (CCOs) designed to target m6A-binding motifs in mRNA transcripts identified through the m6A-FINDiT pipeline. This technique is ultra-sensitive, enabling targeted detection of m6A-modified RNA via complementary capture ssDNA, thereby selectively enriching specific m6A-containing transcripts without the need for recombinant RNA-binding proteins or motif-specific antibodies. MAQ-G utilizes a universal m6A-specific antibody, making the approach more flexible and economically sustainable across different target transcripts. The method is highly sensitive and can detect RNA inputs as low as 100 pg. This increased sensitivity and sequence specificity expand the feasibility of m6A analysis in limited biological samples and support broader application of transcript-specific epitranscriptomic studies and high-throughput research.

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf|alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/hao_2024_mettl3_drives_heart_failure_by_regulating_spp1_and.pdf|hao_2024_mettl3_drives_heart_failure_by_regulating_spp1_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/mengnuo_2020_the_emerging_roles_of_n6_methyladenosine_m6a_deregulation.pdf|mengnuo_2020_the_emerging_roles_of_n6_methyladenosine_m6a_deregulation.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/neha_2026_a_novel_method_for_the_identification_and_quantification.pdf|neha_2026_a_novel_method_for_the_identification_and_quantification.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf|xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/yang_2022_chronic_corticosterone_disrupts_the_circadian_rhythm_of_crh.pdf|yang_2022_chronic_corticosterone_disrupts_the_circadian_rhythm_of_crh.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/zhiyuan_2023_exon_intron_boundary_inhibits_m6a_deposition_enabling_m6a.pdf|zhiyuan_2023_exon_intron_boundary_inhibits_m6a_deposition_enabling_m6a.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/anna_2023_exclusion_of_m6a_from_splice_site_proximal_regions.pdf|anna_2023_exclusion_of_m6a_from_splice_site_proximal_regions.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/christopher_2022_detection_of_m6a_from_direct_rna_sequencing_using.pdf|christopher_2022_detection_of_m6a_from_direct_rna_sequencing_using.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/ci_2024_methylated_lncrnas_suppress_apoptosis_of_gastric_cancer_stem.pdf|ci_2024_methylated_lncrnas_suppress_apoptosis_of_gastric_cancer_stem.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/cristina_2023_the_mrna_methyltransferase_mettl3_modulates_cytokine_mrna_stability.pdf|cristina_2023_the_mrna_methyltransferase_mettl3_modulates_cytokine_mrna_stability.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/jie_2021_histone_lactylation_drives_oncogenesis_by_facilitating_m6a_reader.pdf|jie_2021_histone_lactylation_drives_oncogenesis_by_facilitating_m6a_reader.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/jingang_2023_exosome_targeted_delivery_of_mettl14_regulates_nfatc1_m6a.pdf|jingang_2023_exosome_targeted_delivery_of_mettl14_regulates_nfatc1_m6a.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/lei_2023_rna_modification_mechanisms_and_therapeutic_targets.pdf|lei_2023_rna_modification_mechanisms_and_therapeutic_targets.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/lijuan_2021_a_neural_m6a_ythdf_pathway_is_required_for.pdf|lijuan_2021_a_neural_m6a_ythdf_pathway_is_required_for.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/paper_2024_m6a_reader_hnrnpc_facilitates_adipogenesis_by_regulating_cytoskeletal.pdf|paper_2024_m6a_reader_hnrnpc_facilitates_adipogenesis_by_regulating_cytoskeletal.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/song_2020_an_oncopeptide_regulates_m6a_recognition_by_the_m6a.pdf|song_2020_an_oncopeptide_regulates_m6a_recognition_by_the_m6a.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/wei_2021_role_of_m6a_methyltransferase_component_virma_in_multiple.pdf|wei_2021_role_of_m6a_methyltransferase_component_virma_in_multiple.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/xiaoyu_2024_ginger_inhibits_the_invasion_of_ovarian_cancer_cells.pdf|xiaoyu_2024_ginger_inhibits_the_invasion_of_ovarian_cancer_cells.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/xin_2025_m6a_rna_immunoprecipitation_merip_v1.pdf|xin_2025_m6a_rna_immunoprecipitation_merip_v1.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/yanhua_2021_role_of_hakai_in_m6a_modification_pathway_in.pdf|yanhua_2021_role_of_hakai_in_m6a_modification_pathway_in.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/yingpeng_2021_mettl3_dependent_m6a_modification_programs_t_follicular_helper.pdf|yingpeng_2021_mettl3_dependent_m6a_modification_programs_t_follicular_helper.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/yuanhui_2019_m6a_in_mrna_coding_regions_promotes_translation_via.pdf|yuanhui_2019_m6a_in_mrna_coding_regions_promotes_translation_via.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/Sources/zhongxin_2021_the_m6a_mrna_demethylase_fto_in_granulosa_cells.pdf|zhongxin_2021_the_m6a_mrna_demethylase_fto_in_granulosa_cells.pdf]]
