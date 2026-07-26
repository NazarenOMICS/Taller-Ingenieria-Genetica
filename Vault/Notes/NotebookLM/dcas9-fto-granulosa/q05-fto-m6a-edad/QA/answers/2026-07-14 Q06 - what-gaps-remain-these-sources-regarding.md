---
type: reference
status: current
date: 2026-07-14
source: "notebooklm:dcas9-fto-granulosa/q05-fto-m6a-edad"
related:
  - "[[Notes/Dashboards/FTO m6A vs age ovary]]"
---

# Q06 - What gaps remain in these sources regarding a direct, quantitative, age-stratified measurement of FTO expression and m6A levels specifically in human granulosa cells (as opposed to other ovarian cell types or other tissues)?

Based on the provided sources, several significant gaps remain regarding the direct, quantitative, and age-stratified measurement of FTO expression and m6A levels in human granulosa cells (GCs). While existing research establishes a general downward trend for FTO and an upward trend for m6A with age, the following technical and methodological gaps are identified:

### 1. Lack of Precise Stoichiometric Quantification
The most widely used method for mapping m6A in these studies is **MeRIP-seq (or m6A-seq)**  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/zhongxin_2021_the_m6a_mrna_demethylase_fto_in_granulosa_cells.pdf#Passage 10|[2]]]. However, the sources note that this technique **cannot be used to quantitatively measure the stoichiometry**—the precise fraction of transcript copies that are actually methylated  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 3|[3]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 4|[4]]]. Consequently, while researchers can detect a "peak" change, they cannot currently determine if a specific site on a target (like FOS mRNA) is 10% or 90% methylated in an aged cell  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 3|[3]]].

### 2. Low Site-Specific Resolution
Most current data on aging human GCs rely on MeRIP-seq, which has a relatively **low resolution**, localizing m6A marks to broad regions of **50–200 base pairs** rather than specific nucleotides  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 2|[5]]]. While higher-resolution methods like **miCLIP** or antibody-independent techniques exist, they have not yet been applied to create a comprehensive, single-base resolution map of the m6A epitranscriptome specifically for the aging human ovary  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiulin_2021_the_role_of_m6a_modification_in_the_biological.pdf#Passage 2|[6]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/zhongxin_2021_the_m6a_mrna_demethylase_fto_in_granulosa_cells.pdf#Passage 3|[7]]].

### 3. Limitations in Sample Purity (Mural GCs vs. Cumulus Cells)
A critical gap involves the source of the human cells themselves. One study explicitly mentions that, due to the methods of clinical sample collection (follicular aspiration for IVF), the "granulosa cell" samples obtained from patients are **actually composed primarily of cumulus cells**  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiaolan_2024_m6a_demethylase_fto_stabilized_exosomal_circbrca1_alleviates_oxidative.pdf#Passage 8|[8]]]. There is a lack of comparative, direct measurements between **mural granulosa cells** and **cumulus cells** to determine if age-related FTO/m6A changes are uniform across these distinct subpopulations  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiaolan_2024_m6a_demethylase_fto_stabilized_exosomal_circbrca1_alleviates_oxidative.pdf#Passage 8|[8]]].

### 4. Coarse Age Stratification
The sources typically utilize a **binary comparison** rather than a granular, year-by-year stratification. For example, studies often group patients into "aged" (e.g., >38 or >40 years) versus "young/normal" (e.g., <30 years)  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiaolan_2024_m6a_demethylase_fto_stabilized_exosomal_circbrca1_alleviates_oxidative.pdf#Passage 8|[8]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiaolan_2024_m6a_demethylase_fto_stabilized_exosomal_circbrca1_alleviates_oxidative.pdf#Passage 9|[9]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/honey_2025_editorial_genetics_and_epigenetics_in_ovarian_aging.pdf#Passage 2|[10]]]. This leaves a gap in understanding the **exact trajectory** of FTO decline and m6A accumulation throughout the mid-30s, which is identified as the critical period when ovarian aging begins to accelerate  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/shenglan_2024_ovarian_aging_energy_metabolism_of_oocytes.pdf#Passage 1|[11]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiaoyan_2022_the_role_of_m6a_on_female_reproduction_and.pdf#Passage 3|[12]]].

### 5. Incomplete Mapping of Other Regulators
While FTO has been the primary focus of aging GCs in this corpus, the **expression patterns of other m6A regulators**—such as the various "writers" (methyltransferases) and "readers" (YTHDF/IGF2BP proteins)—have **not been fully evaluated** in the context of the ovarian aging process  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 7|[13]]]. One review notes that the significance of m6A content and its specific regulatory changes in promoting or retarding ovarian development is still not fully understood  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 7|[13]]].

### 6. Technical Reproducibility and Confounding
Research indicates that MeRIP-seq data is prone to **high technical noise** and **strong batch effects**, with peak overlap between different studies varying from only 30% to 60%  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 2|[5]]]. There is a lack of high-replicate, multi-center quantitative data to ensure that the reported age-related m6A increases in human GCs are not artifacts of technical variation or changes in underlying gene expression [14, 15].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf|PDF]]
- Texto literal:
> The first and most widely-used method to enable transcriptome-wide studies of m6A, MeRIP-seq or m6A-seq, involves the immunoprecipitation of m6A-modified RNA fragments followed by peak detection through comparison to background gene coverage16,17. A second method was developed in 2015, miCLIP or m6A-CLIP, which involves crosslinking at the site of antibody binding to induce mutations during reverse transcription for single-nucleotide detection of methylated bases2,18. MeRIP-seq is still more often used than miCLIP, despite less precise localization of m6A to peak regions of approximately 50–200 base pairs that can contain multiple DRAC motifs, since it follows a simpler protocol, requires less starting material, and generally produces higher coverage of more transcripts. Antibodies for m6A can also detect a second base modification, N6,2′-O-dimethyladenosine (m6Am), found at a lower abundance than m6A and located at the 5′ ends of select transcripts15,18. We thus refer to the base modifications detected through MeRIP-seq collectively as m6A(m), although most are likely m6A. As of late 2018, over fifty studies used MeRIP-seq to detect m6A(m) in mammalian mRNA (Supplementary Table 1).

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/zhongxin_2021_the_m6a_mrna_demethylase_fto_in_granulosa_cells.pdf#Passage 10|Pasaje 10]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/zhongxin_2021_the_m6a_mrna_demethylase_fto_in_granulosa_cells.pdf|PDF]]
- Texto literal:
> MeRIP-seq The preparatory work of the RNA m6A-sequence was the same as for the RNA-sequence. For the follow-up procedure, m6A RNA immunoprecipitation was performed with the GenSeqTM m6A RNA IP Kit (GenSeq Inc., China) by following the manufacturer’s instructions. Both the input sample without immunoprecipitation and the m6A IP samples were used for RNA-seq library generation with the NEBNext® Ultra II Directional RNA Library.

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf|PDF]]
- Texto literal:
> Although MeRIP-seq can reveal approximate sites of m6A(m), it cannot be used to quantitatively measure the fraction of transcript copies that are methylated19. Studies of m6A variation in response to stimuli instead estimate differences at individual loci through changes in peak presence or peak height. Using these approaches, studies

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf|PDF]]
- Texto literal:
> The extent to which m6A changes on particular transcripts and whether it changes in binary presence/ absence or in degree is unclear. MeRIP-RT-qPCR could detect methylation differences in in vitro transcribed RNA. Further, we found that these changes correlated with differences in MeRIP-seq enrichment. However, neither MeRIP-seq nor MeRIP-RT-qPCR can reveal the precise fraction of transcript copies modified by m6A. In general, antibody-based methods are subject to biases, including from differences in binding efficiencies based on RNA structure and motif preferences81. There is an oft-cited but little-used method for quantification of m6A, site-specific cleavage and radioactive-labeling followed by ligation-assisted extraction and thin-layer chromatography (SCARLET)19. However, this method can be challenging, works only for highly abundant

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf|PDF]]
- Texto literal:
> We next analyzed the overlap of peaks among studies and found inconsistency in peak localization on transcripts as well. Within four commonly used cell types, the percent of peaks detected in one experiment that were also detected in a second varied among pairs of studies from as low as 2% of peaks to as high as 90% (median = 45%), after filtering for transcripts expressed above a mean of 10X input coverage in both to ensure sufficient expression for peak detection (Fig. 2a). In fact, peaks showed higher overlap within different cell types from the same study than within the same cell type from different studies, suggesting that MeRIP-seq data is prone to strong batch effects (Fig. 2b). While this could be due to differences among experimental protocols used (summarized in Supplementary Table 2), we were unable to identify such a link. Overall, most percent overlaps of m6A(m) peaks fell between ~30% (1st quartile) and ~60% (3rd quartile) (Fig. 2b). With rare exceptions (e.g. that described by Ke et al., 2017 in their Supplementary Fig. 8)3, most MeRIP-seq data sets do show enrichment of the m6A motif DRAC. These results indicate, however, that multiple labs running MeRIP-seq on the same cell type will detect different subsets of m6A(m) sites. Possible contributing factors in the differences among studies include cell state (e.g. different stages of the cell cycle), experimental conditions, and sequencing depth. Despite predictions that tissue or cell type would be a large factor in differences among samples, though, peaks detected in different tissues analyzed in a single experiment showed high overlap and little clustering by tissue type (Fig. 2c)54. This suggests that although there is evidence that m6A levels vary by tissue19, modified sites are consistent.

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiulin_2021_the_role_of_m6a_modification_in_the_biological.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/xiulin_2021_the_role_of_m6a_modification_in_the_biological.pdf|PDF]]
- Texto literal:
> frequently identified around the stop codon by whole-transcriptome m6A maps, indicating the potential functional roles for m6A7,8,14. To detect individual m6A sites, methyl-sensitive ligase, reverse transcriptase and selective dTTP (deoxythymidine triphosphate) analog have been applied15–18. To examine the chemical properties of m6A sites, all of the

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiaolan_2024_m6a_demethylase_fto_stabilized_exosomal_circbrca1_alleviates_oxidative.pdf#Passage 8|Pasaje 8]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/xiaolan_2024_m6a_demethylase_fto_stabilized_exosomal_circbrca1_alleviates_oxidative.pdf|PDF]]
- Texto literal:
> Methods Patients and samples 50 patients with POI (POI group) who were treated with in vitro fertilization or intracytoplasmic sperm injection and embryo transfer (IVF/ICSI-ET) at the Reproductive Center of the Fourth Affiliated Hospital of Jiangsu Uni-versity (Zhenjiang Maternal and Child Health Hospital) were selected from June 2021 to July 2023; 50 patients with normal ovarian reserve function (NC group) who underwent IVF/ICSI-ET due to male and/or tubal factors were selected as controls during the same period. The age and BMI of the 2 groups were compared, and the differences were not statistically significant (P > 0.05), and were comparable.

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiaolan_2024_m6a_demethylase_fto_stabilized_exosomal_circbrca1_alleviates_oxidative.pdf#Passage 9|Pasaje 9]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/xiaolan_2024_m6a_demethylase_fto_stabilized_exosomal_circbrca1_alleviates_oxidative.pdf|PDF]]
- Texto literal:
> CircBRCA1 is significantly upregulated in oxidatively damaged KGNs treated with H‑Exs Recently, the H-Exs transfer of ncRNAs (noncoding RNAs) was regarded as a novel and important mechanism of genetic exchange between cells, and the role of circRNAs in POI is receiving increasing attention. To search for circRNAs that may be associated with POIs, we analyzed data from the GEO dataset (GSE97193), including RNA-seq data of circRNAs in GCs with three advanced age (AA, > 38 years) and three young (YA, < 30 years) women undergoing IVF/ICSI-ET, and found that a total of 179 circRNAs, 61 downregulated and 118 upregulated circRNAs, were differentially expressed in GCs. The heatmap was used to illustrate the differentially expressed pattern of circRNAs (Fig. 1I). Among the top 30 most significantly downregulated circRNAs, by RT-qPCR, we verified that only hsa_circ_0043949 was significantly decreased in GCs and serum of patients with POI and in H2O2-KGNs (Fig. 1J, K), while this molecule was obviously increased in H2O2-KGNs after coculture with H-Exs (Fig. 1L). Consistently, hsa_circ_0043949 was enriched in HucMSCs/H-Exs (Supplementary Fig. 1J), and its host parental gene was associated with mitochondrial function [33–35], which was selected for our next studies. Hsa_circ_0043949 was further referred to as circBRCA1 because it consists of exons of BRCA1. As expected, FISH analysis revealed that Cy3-marked circBRCA1 in H-Exs was internalized by H2O2-KGNs (Fig. 1M).

### Extracto 9
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/honey_2025_editorial_genetics_and_epigenetics_in_ovarian_aging.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/honey_2025_editorial_genetics_and_epigenetics_in_ovarian_aging.pdf|PDF]]
- Texto literal:
> health outcomes. Ovarian aging is a multidimensional process characterized by a progressive

### Extracto 10
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/shenglan_2024_ovarian_aging_energy_metabolism_of_oocytes.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/shenglan_2024_ovarian_aging_energy_metabolism_of_oocytes.pdf|PDF]]
- Texto literal:
> society, women often postpone childbirth due to a variety of factors, including economics, careers, and lifestyles [3]. However, as humans age, fertility rates begin to decline around 30 years of age and become clinically relevant between the ages of 35 and 40, after which they continue to decline significantly. [4]. The decline in fertility associated with women’s age has become an important issue that troubles modern women.

### Extracto 11
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiaoyan_2022_the_role_of_m6a_on_female_reproduction_and.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/xiaoyan_2022_the_role_of_m6a_on_female_reproduction_and.pdf|PDF]]
- Texto literal:
> However, the expression pattern of m6A methyltransferase and reader in ovarian aging process have not been fully evaluated. Moreover, we don’t know the significance of m6A content and changes of its regulators as well as how to promote ovarian development. In the future, the significance of m6A and its regulators in the regulation of ovarian life cycle should be further studied.

### Extracto 12
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 7|Pasaje 7]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf|PDF]]
- Texto literal:
> To re-evaluate the evidence for m6A(m) changes under various conditions, we first examined the variability in m6A(m) detection across replicates, cell lines, and experiments using our own negative controls (12 replicates) as well as 24 published MeRIP-seq data sets. We then compared statistical methods to detect differences in IP enrichment using biological negative and positive controls for m6A changes. We found that these methods are limited by noise, including biological variability from changes in RNA expression and technical variability from immunoprecipitation and sequencing that limits reproducibility across studies. Our results suggest that the scale of statistically detectable m6A(m) changes in response to various stimuli is orders of magnitude lower than the scale of changes reported in many studies. However, we also found that statistical detection could miss the majority of changed sites when using only 2–3 replicates. We use our results to propose approaches to MeRIP-seq experimental design and analysis to improve reproducibility and more accurately measure differential regulation of m6A(m) in response to stimuli. These data and analyses emphasize the need for further research and alternative assays, for example recently developed endoribonuclease-based sequencing methods44,45 or direct RNA nanopore sequencing46, to resolve the extent to which m6A changes in response to specific conditions.

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf|alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/honey_2025_editorial_genetics_and_epigenetics_in_ovarian_aging.pdf|honey_2025_editorial_genetics_and_epigenetics_in_ovarian_aging.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/shenglan_2024_ovarian_aging_energy_metabolism_of_oocytes.pdf|shenglan_2024_ovarian_aging_energy_metabolism_of_oocytes.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiaolan_2024_m6a_demethylase_fto_stabilized_exosomal_circbrca1_alleviates_oxidative.pdf|xiaolan_2024_m6a_demethylase_fto_stabilized_exosomal_circbrca1_alleviates_oxidative.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiaoyan_2022_the_role_of_m6a_on_female_reproduction_and.pdf|xiaoyan_2022_the_role_of_m6a_on_female_reproduction_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiulin_2021_the_role_of_m6a_modification_in_the_biological.pdf|xiulin_2021_the_role_of_m6a_modification_in_the_biological.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/zhongxin_2021_the_m6a_mrna_demethylase_fto_in_granulosa_cells.pdf|zhongxin_2021_the_m6a_mrna_demethylase_fto_in_granulosa_cells.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/chen_2025_molecular_and_genetic_insights_into_human_ovarian_aging.pdf|chen_2025_molecular_and_genetic_insights_into_human_ovarian_aging.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/lijie_2023_igf2bp3_promotes_the_progression_of_colorectal_cancer_and.pdf|lijie_2023_igf2bp3_promotes_the_progression_of_colorectal_cancer_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/liuer_2019_functions_of_n6_methyladenosine_and_its_role_in.pdf|liuer_2019_functions_of_n6_methyladenosine_and_its_role_in.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/mengmeng_2024_exploring_the_transcriptomic_and_m6a_landscape_of_human.pdf|mengmeng_2024_exploring_the_transcriptomic_and_m6a_landscape_of_human.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/ngela_2014_multi_tissue_omics_analyses_reveal_molecular_regulatory_networks.pdf|ngela_2014_multi_tissue_omics_analyses_reveal_molecular_regulatory_networks.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/paz_2021_the_role_of_m6a_m5c_and_rna_modifications.pdf|paz_2021_the_role_of_m6a_m5c_and_rna_modifications.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/seth_2018_nuclear_m6a_reader_ythdc1_regulates_alternative_polyadenylation_and.pdf|seth_2018_nuclear_m6a_reader_ythdc1_regulates_alternative_polyadenylation_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/shaoke_2022_the_transcriptome_wide_n6_methyladenosine_m6a_map_profiling.pdf|shaoke_2022_the_transcriptome_wide_n6_methyladenosine_m6a_map_profiling.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/wei_chao_2022_autophagy_induction_promoted_by_m6a_reader_ythdf3_through.pdf|wei_chao_2022_autophagy_induction_promoted_by_m6a_reader_ythdf3_through.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xia_2024_comprehensive_analysis_of_key_m6a_rna_modification_related.pdf|xia_2024_comprehensive_analysis_of_key_m6a_rna_modification_related.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiangyu_2024_single_cell_sequencing_to_multi_omics_technologies_and.pdf|xiangyu_2024_single_cell_sequencing_to_multi_omics_technologies_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xin_2025_m6a_rna_immunoprecipitation_merip_v1.pdf|xin_2025_m6a_rna_immunoprecipitation_merip_v1.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf|xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/yunbing_2024_reading_the_m6a_encoded_epitranscriptomic_information_in_development.pdf|yunbing_2024_reading_the_m6a_encoded_epitranscriptomic_information_in_development.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/yuqian_2023_premature_ovarian_insufficiency_a_review_on_the_role.pdf|yuqian_2023_premature_ovarian_insufficiency_a_review_on_the_role.pdf]]
