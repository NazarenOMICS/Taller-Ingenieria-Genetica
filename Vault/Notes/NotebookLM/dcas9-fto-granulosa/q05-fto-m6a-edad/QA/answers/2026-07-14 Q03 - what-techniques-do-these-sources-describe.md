---
type: reference
status: current
date: 2026-07-14
source: "notebooklm:dcas9-fto-granulosa/q05-fto-m6a-edad"
related:
  - "[[Notes/Dashboards/FTO m6A vs age ovary]]"
---

# Q03 - What techniques do these sources describe for quantifying m6A methylation in a site-specific manner (e.g., MeRIP-seq, SELECT, miCLIP, m6A-seq), and what are their resolution and sensitivity trade-offs?

The source material describes a wide range of techniques for quantifying m6A methylation, ranging from transcriptome-wide "peak" mapping to site-specific biochemical assays. These methods vary significantly in their **resolution** (ability to pinpoint exact modified bases) and **sensitivity** (ability to detect low-abundance modifications or quantitative differences).

### Antibody-Based Sequencing Methods
The most established techniques rely on m6A-specific antibodies to enrich methylated RNA fragments.

*   **MeRIP-seq (or m6A-seq):** 
    *   **Mechanism:** Involves the immunoprecipitation of fragmented, m6A-modified RNA followed by high-throughput sequencing  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/yunbing_2024_reading_the_m6a_encoded_epitranscriptomic_information_in_development.pdf#Passage 1|[2]]]. Methylated regions are identified as "peaks" by comparing immunoprecipitated (IP) RNA to input RNA  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiulin_2021_the_role_of_m6a_modification_in_the_biological.pdf#Passage 1|[3]]].
    *   **Resolution:** Relatively **low**. It typically localizes m6A to regions of **50–200 base pairs** rather than specific nucleotides  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 2|[4]]].
    *   **Sensitivity Trade-offs:** It follows a simpler protocol, requires less starting material, and produces high coverage across more transcripts  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 1|[1]]]. However, it is prone to **high technical noise** and batch effects; studies often show only 30–60% peak overlap even in the same cell type  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiulin_2021_the_role_of_m6a_modification_in_the_biological.pdf#Passage 1|[3]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 3|[5]]]. It cannot quantitatively measure the precise fraction of methylated transcript copies  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 4|[6]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf#Passage 1|[7]]].
*   **miCLIP (or m6A-CLIP):** 
    *   **Mechanism:** Utilizes ultraviolet **crosslinking** of antibodies to the RNA, which induces specific mutations during reverse transcription  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf#Passage 2|[8]]].
    *   **Resolution:** **High (Single-nucleotide resolution)**  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 2|[4]]].
    *   **Sensitivity Trade-offs:** The protocol is significantly more complex and requires more starting material compared to MeRIP-seq  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 1|[1]]].

### Site-Specific Quantification Techniques
These methods are typically used to validate sequencing results or to quantify methylation levels at a specific known site.

*   **SELECT (Single-base Elongation- and Ligation-based qPCR):**
    *   **Mechanism:** A radiolabeling-free method that uses Bst DNA polymerase and SplintR ligase to specifically amplify products from methylated sites  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf#Passage 3|[9]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 5|[10]]].
    *   **Resolution:** **Site-specific**; it interrogates a single targeted adenosine  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 5|[10]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 6|[11]]].
    *   **Sensitivity Trade-offs:** The abundance of qPCR products reflects the relative methylation level, making it effective for comparing samples  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 5|[10]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiulin_2021_the_role_of_m6a_modification_in_the_biological.pdf#Passage 2|[12]]].
*   **SCARLET:**
    *   **Mechanism:** Site-specific cleavage and radioactive labeling followed by ligation-assisted extraction and thin-layer chromatography  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf#Passage 1|[7]]].
    *   **Resolution:** **Single-nucleotide**  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/paz_2021_the_role_of_m6a_m5c_and_rna_modifications.pdf#Passage 1|[13]]].
    *   **Sensitivity Trade-offs:** While it is considered the "gold standard" for biochemical validation, it is extremely **challenging and impractical** for transcriptome-wide analysis, working only for highly abundant transcripts  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf#Passage 1|[7]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/paz_2021_the_role_of_m6a_m5c_and_rna_modifications.pdf#Passage 2|[14]]].
*   **MeRIP-RT-qPCR:** 
    *   **Mechanism:** Combines immunoprecipitation with quantitative PCR [15].
    *   **Resolution:** **Site-specific** [15].
    *   **Sensitivity Trade-offs:** It can capture differences in m6A-to-adenosine ratios [15]. However, it cannot reveal the precise fraction of modified transcripts and is sensitive to technical variation that can lead to spuriously significant differences  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf#Passage 1|[7]]].

### Antibody-Independent High-Resolution Methods
Recent advancements aim to eliminate antibody bias, which can lead to non-specific binding and poor reproducibility [16, 17].

*   **Endoribonuclease-based Methods (e.g., m6A-REF-seq, MAZTER-seq):** 
    *   **Mechanism:** Uses m6A-sensitive enzymes (like the bacterial RNase **MazF**) that cleave RNA at specific motifs only when the adenosine is *unmodified*  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/paz_2021_the_role_of_m6a_m5c_and_rna_modifications.pdf#Passage 2|[14]]].
    *   **Resolution:** **Single-base resolution** [16].
    *   **Sensitivity Trade-offs:** They provide accurate quantification of m6A stoichiometry but are limited to specific sequence motifs (e.g., **"ACA" motifs**, which account for only ~16% of all m6A sites)  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/paz_2021_the_role_of_m6a_m5c_and_rna_modifications.pdf#Passage 2|[14]]].
*   **DART-seq:** 
    *   **Mechanism:** Fuses the cytidine deaminase **APOBEC1** to an m6A-binding YTH domain to induce C-to-U editing adjacent to m6A sites [16, 17].
    *   **Resolution:** **Single-base** [16].
    *   **Sensitivity Trade-offs:** It is antibody-free but limited to mapping only those RNAs actually bound by the specific YTH domain-containing reader used [17].
*   **Third-Generation Single-Molecule Sequencing (Nanopore):** 
    *   **Mechanism:** Directly detects modifications by measuring current or kinetic changes as a native RNA molecule passes through a nanopore [17, 18].
    *   **Resolution:** **Single-base/Single-molecule** [17].
    *   **Sensitivity Trade-offs:** These platforms offer a way to quantify and "phase" m6A sites across entire transcripts, but algorithms for accurate, transcriptome-wide detection are still under active development  [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/paz_2021_the_role_of_m6a_m5c_and_rna_modifications.pdf#Passage 2|[14]]].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf|PDF]]
- Texto literal:
> The first and most widely-used method to enable transcriptome-wide studies of m6A, MeRIP-seq or m6A-seq, involves the immunoprecipitation of m6A-modified RNA fragments followed by peak detection through comparison to background gene coverage16,17. A second method was developed in 2015, miCLIP or m6A-CLIP, which involves crosslinking at the site of antibody binding to induce mutations during reverse transcription for single-nucleotide detection of methylated bases2,18. MeRIP-seq is still more often used than miCLIP, despite less precise localization of m6A to peak regions of approximately 50–200 base pairs that can contain multiple DRAC motifs, since it follows a simpler protocol, requires less starting material, and generally produces higher coverage of more transcripts. Antibodies for m6A can also detect a second base modification, N6,2′-O-dimethyladenosine (m6Am), found at a lower abundance than m6A and located at the 5′ ends of select transcripts15,18. We thus refer to the base modifications detected through MeRIP-seq collectively as m6A(m), although most are likely m6A. As of late 2018, over fifty studies used MeRIP-seq to detect m6A(m) in mammalian mRNA (Supplementary Table 1).

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/yunbing_2024_reading_the_m6a_encoded_epitranscriptomic_information_in_development.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/yunbing_2024_reading_the_m6a_encoded_epitranscriptomic_information_in_development.pdf|PDF]]
- Texto literal:
> The machinery for m6A modification Epigenetic modifications, including DNA methylation, RNA modification, histone modification, chromatin remodeling, and noncoding RNA regulation, play particularly crucial roles in most if not all biological processes. Since it was first discovered in the 1970s, m6A has been discovered to be the most prevalent internal modification present in the mRNAs of all higher eukaryotes [13]. Advancements in high-throughput sequencing techniques have revolutionized the study of m6A modifications, extending their understanding from prokaryotic bacteria to eukaryotic organisms including humans. In 2012, the comprehensive profiling of m6A in mammalian cells for the entire transcriptome was achieved through the development of m6A antibody-based RNA-immuno-precipitation strategies, such as m6A-seq and Methylated RNA immunoprecipitation sequencing (MeRIP-seq) [14, 15]. These innovative techniques allowed researchers to identify and study the distribution of m6A modifications across RNA molecules. Interestingly, m6A was found to be predominantly enriched in regions such as the 3′ untranslated regions (3′UTRs) and in proximity to stop codons, a feature that is highly conserved in different species [16]. M6A modifications have been identified in different RNA types, such as messenger RNA (mRNA), transfer RNA (tRNA), ribosomal RNA (rRNA), circular RNA (circRNA), microRNA (miRNA), and long noncoding RNA (lncRNA). Each mRNA molecule, on average,

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiulin_2021_the_role_of_m6a_modification_in_the_biological.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/xiulin_2021_the_role_of_m6a_modification_in_the_biological.pdf|PDF]]
- Texto literal:
> Signal Transduction and Targeted Therapy (2021) 6:74 ; https://doi.org/10.1038/s41392-020-00450-x

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf|PDF]]
- Texto literal:
> We next analyzed the overlap of peaks among studies and found inconsistency in peak localization on transcripts as well. Within four commonly used cell types, the percent of peaks detected in one experiment that were also detected in a second varied among pairs of studies from as low as 2% of peaks to as high as 90% (median = 45%), after filtering for transcripts expressed above a mean of 10X input coverage in both to ensure sufficient expression for peak detection (Fig. 2a). In fact, peaks showed higher overlap within different cell types from the same study than within the same cell type from different studies, suggesting that MeRIP-seq data is prone to strong batch effects (Fig. 2b). While this could be due to differences among experimental protocols used (summarized in Supplementary Table 2), we were unable to identify such a link. Overall, most percent overlaps of m6A(m) peaks fell between ~30% (1st quartile) and ~60% (3rd quartile) (Fig. 2b). With rare exceptions (e.g. that described by Ke et al., 2017 in their Supplementary Fig. 8)3, most MeRIP-seq data sets do show enrichment of the m6A motif DRAC. These results indicate, however, that multiple labs running MeRIP-seq on the same cell type will detect different subsets of m6A(m) sites. Possible contributing factors in the differences among studies include cell state (e.g. different stages of the cell cycle), experimental conditions, and sequencing depth. Despite predictions that tissue or cell type would be a large factor in differences among samples, though, peaks detected in different tissues analyzed in a single experiment showed high overlap and little clustering by tissue type (Fig. 2c)54. This suggests that although there is evidence that m6A levels vary by tissue19, modified sites are consistent.

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf|PDF]]
- Texto literal:
> Although MeRIP-seq can reveal approximate sites of m6A(m), it cannot be used to quantitatively measure the fraction of transcript copies that are methylated19. Studies of m6A variation in response to stimuli instead estimate differences at individual loci through changes in peak presence or peak height. Using these approaches, studies

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf|PDF]]
- Texto literal:
> The extent to which m6A changes on particular transcripts and whether it changes in binary presence/ absence or in degree is unclear. MeRIP-RT-qPCR could detect methylation differences in in vitro transcribed RNA. Further, we found that these changes correlated with differences in MeRIP-seq enrichment. However, neither MeRIP-seq nor MeRIP-RT-qPCR can reveal the precise fraction of transcript copies modified by m6A. In general, antibody-based methods are subject to biases, including from differences in binding efficiencies based on RNA structure and motif preferences81. There is an oft-cited but little-used method for quantification of m6A, site-specific cleavage and radioactive-labeling followed by ligation-assisted extraction and thin-layer chromatography (SCARLET)19. However, this method can be challenging, works only for highly abundant

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf|PDF]]
- Texto literal:
> methylation, validation assay, specific quantification of m6a rna modification, m6a rna modification, specific m6a modification,

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 5|Pasaje 5]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf|PDF]]
- Texto literal:
> (2015). 19. Liu, N. et al. Probing N6-methyladenosine RNA modification status at single nucleotide resolution in mRNA and long noncoding

### Extracto 9
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf#Passage 6|Pasaje 6]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf|PDF]]
- Texto literal:
> Disparities between experiments were not simply due to significance thresholding or differences in peak detection. Taking the union of peaks called in two experiments for KSHV, HIV, and dsDNA treatment, we found minimal to negative correlations in changes in m6A enrichment induced by treatment at the same sites, further showing that changes with similar treatments are not reproducible (Supplementary Fig. 7e).

### Extracto 10
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiulin_2021_the_role_of_m6a_modification_in_the_biological.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/xiulin_2021_the_role_of_m6a_modification_in_the_biological.pdf|PDF]]
- Texto literal:
> frequently identified around the stop codon by whole-transcriptome m6A maps, indicating the potential functional roles for m6A7,8,14. To detect individual m6A sites, methyl-sensitive ligase, reverse transcriptase and selective dTTP (deoxythymidine triphosphate) analog have been applied15–18. To examine the chemical properties of m6A sites, all of the

### Extracto 11
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/paz_2021_the_role_of_m6a_m5c_and_rna_modifications.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/paz_2021_the_role_of_m6a_m5c_and_rna_modifications.pdf|PDF]]
- Texto literal:
> wide methods and tools for rapid and quantitative detection of RNA modifications. Most of the stablished methods rely on next-generation sequencing and, as such, they are typically blind to nucleotide modifications. Consequently, indirect methods are required that are based on immunoprecipitation techniques

### Extracto 12
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/paz_2021_the_role_of_m6a_m5c_and_rna_modifications.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/paz_2021_the_role_of_m6a_m5c_and_rna_modifications.pdf|PDF]]
- Texto literal:
> nucleotide (PacBio) [309]. Or by current changes as the native RNA molecule is pulled through a membrane pore (ONT) [310]. Although the detection of modifications using ONT direct RNA sequencing is already a reality [311], yet current efforts have not yielded an efficient and accurate RNA modification detection algorithm, largely due to the challenges in the alignment and re-squiggling of RNA current intensities. But emerging alternative base-calling strategies such as EpiNano algorithms which identifies m6A from RNA reads with an overall accuracy of ~90%, open new avenues to explore additional RNA modifications in the future [312]. The dynamic expression patterns of writer, reader and

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf|alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/paz_2021_the_role_of_m6a_m5c_and_rna_modifications.pdf|paz_2021_the_role_of_m6a_m5c_and_rna_modifications.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf|xin_2025_select_based_quantification_of_site_specific_m6a_modification.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiulin_2021_the_role_of_m6a_modification_in_the_biological.pdf|xiulin_2021_the_role_of_m6a_modification_in_the_biological.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/yunbing_2024_reading_the_m6a_encoded_epitranscriptomic_information_in_development.pdf|yunbing_2024_reading_the_m6a_encoded_epitranscriptomic_information_in_development.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/chen_2025_molecular_and_genetic_insights_into_human_ovarian_aging.pdf|chen_2025_molecular_and_genetic_insights_into_human_ovarian_aging.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/honey_2025_editorial_genetics_and_epigenetics_in_ovarian_aging.pdf|honey_2025_editorial_genetics_and_epigenetics_in_ovarian_aging.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/lijie_2023_igf2bp3_promotes_the_progression_of_colorectal_cancer_and.pdf|lijie_2023_igf2bp3_promotes_the_progression_of_colorectal_cancer_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/liuer_2019_functions_of_n6_methyladenosine_and_its_role_in.pdf|liuer_2019_functions_of_n6_methyladenosine_and_its_role_in.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/mengmeng_2024_exploring_the_transcriptomic_and_m6a_landscape_of_human.pdf|mengmeng_2024_exploring_the_transcriptomic_and_m6a_landscape_of_human.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/ngela_2014_multi_tissue_omics_analyses_reveal_molecular_regulatory_networks.pdf|ngela_2014_multi_tissue_omics_analyses_reveal_molecular_regulatory_networks.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/seth_2018_nuclear_m6a_reader_ythdc1_regulates_alternative_polyadenylation_and.pdf|seth_2018_nuclear_m6a_reader_ythdc1_regulates_alternative_polyadenylation_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/shaoke_2022_the_transcriptome_wide_n6_methyladenosine_m6a_map_profiling.pdf|shaoke_2022_the_transcriptome_wide_n6_methyladenosine_m6a_map_profiling.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/shenglan_2024_ovarian_aging_energy_metabolism_of_oocytes.pdf|shenglan_2024_ovarian_aging_energy_metabolism_of_oocytes.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/wei_chao_2022_autophagy_induction_promoted_by_m6a_reader_ythdf3_through.pdf|wei_chao_2022_autophagy_induction_promoted_by_m6a_reader_ythdf3_through.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xia_2024_comprehensive_analysis_of_key_m6a_rna_modification_related.pdf|xia_2024_comprehensive_analysis_of_key_m6a_rna_modification_related.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiangyu_2024_single_cell_sequencing_to_multi_omics_technologies_and.pdf|xiangyu_2024_single_cell_sequencing_to_multi_omics_technologies_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiaolan_2024_m6a_demethylase_fto_stabilized_exosomal_circbrca1_alleviates_oxidative.pdf|xiaolan_2024_m6a_demethylase_fto_stabilized_exosomal_circbrca1_alleviates_oxidative.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xiaoyan_2022_the_role_of_m6a_on_female_reproduction_and.pdf|xiaoyan_2022_the_role_of_m6a_on_female_reproduction_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/xin_2025_m6a_rna_immunoprecipitation_merip_v1.pdf|xin_2025_m6a_rna_immunoprecipitation_merip_v1.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/yuqian_2023_premature_ovarian_insufficiency_a_review_on_the_role.pdf|yuqian_2023_premature_ovarian_insufficiency_a_review_on_the_role.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/Sources/zhongxin_2021_the_m6a_mrna_demethylase_fto_in_granulosa_cells.pdf|zhongxin_2021_the_m6a_mrna_demethylase_fto_in_granulosa_cells.pdf]]
