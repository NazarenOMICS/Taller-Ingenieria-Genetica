---
type: reference
status: current
date: 2026-07-24
source: "notebooklm:dcas9-fto-granulosa/q03-especificidad-off-target"
related:
  - "[[Notes/Dashboards/dCas9-p300 off-target specificity]]"
---

# Q04 - How does the specificity profile of dCas9 fusion-based CRISPR activators compare to the off-target profile of catalytically active Cas9 nuclease editing, according to these sources?

The specificity profile of **dCas9 fusion-based CRISPR activators (CRISPRa)** differs from **catalytically active Cas9 nuclease editing** primarily in the nature of the genomic modification, the resulting cellular toxicity, and the stringency of the requirements for functional activity versus physical binding.

### **Permanent vs. Reversible Modifications**
*   **Active Cas9:** Induces double-strand breaks (DSBs) that are repaired by error-prone pathways like non-homologous end joining (NHEJ), resulting in **permanent and irreversible** insertions and deletions (indels) or chromosomal translocations  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/congting_2023_off_target_effects_in_crispr_cas9_gene_editing.pdf#Passage 17|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/congting_2023_off_target_effects_in_crispr_cas9_gene_editing.pdf#Passage 18|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf#Passage 10|[3]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf#Passage 3|[4]]].
*   **dCas9 Activators:** Utilize a nuclease-dead Cas9 that does not cut DNA. Its effects on gene expression are **reversible and transient**, modulating the transcriptome without altering the underlying DNA sequence  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf#Passage 3|[5]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf#Passage 1|[6]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf#Passage 2|[7]]].

### **Cutting-Related Toxicity and Growth Defects**
*   **Active Cas9:** A major differentiator is **"cutting-related toxicity,"** which occurs when Cas9 creates DSBs. This effect is particularly severe at copy-number amplified loci, where multiple cuts can lead to significant cell growth defects or death  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf#Passage 1|[6]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf#Passage 4|[8]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/yu_2015_making_sense_of_gwas_using_epigenomics_and_genome.pdf#Passage 4|[9]]]. 
*   **dCas9 Activators:** These systems **mitigate cutting-related toxicity** because they do not introduce genomic breaks  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf#Passage 1|[6]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/yu_2015_making_sense_of_gwas_using_epigenomics_and_genome.pdf#Passage 4|[9]]]. In negative selection screens, dCas9-based systems show little to no difference in growth between non-targeting guides and guides targeting non-essential genes, whereas active Cas9 shows a clear "cutting effect"  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/yu_2015_making_sense_of_gwas_using_epigenomics_and_genome.pdf#Passage 4|[9]]].

### **Binding Specificity vs. Functional Specificity**
*   **Less Stringent Binding:** Sources note that the requirements for dCas9 DNA-binding are **"less stringent"** than for the catalytic cleavage performed by active Cas9  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/hongyi_2020_applications_of_genome_editing_technology_in_the_targeted.pdf#Passage 2|[10]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 5|[11]]]. ChIP-seq mapping reveals that dCas9 associates with many off-target sites—often enriched in **open chromatin regions**—that do not result in functional gene activation  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/hongyi_2020_applications_of_genome_editing_technology_in_the_targeted.pdf#Passage 2|[10]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 5|[11]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf#Passage 7|[12]]].
*   **High Functional Specificity:** Despite widespread physical binding, the actual **transcriptional off-target effects** of dCas9 fusions are reported to be "remarkably specific"  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf#Passage 7|[12]]]. For instance, RNA-seq profiling of **dCas9-p300** targeting the *IL1RN* promoter in human HEK293T cells showed only two unintended transcripts significantly induced above background  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 1|[13]]].

### **Positional and Spatial Constraints**
*   **Active Cas9:** Can be targeted to various locations within a gene (e.g., any coding exon) to achieve functional disruption through indels  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 2|[14]]].
*   **dCas9 Activators:** Exhibit high **spatial specificity**, meaning they only function within a narrow window near the **transcription start site (TSS)**. For example, CRISPRa is typically effective only when targeted approximately **150 to 75 nucleotides upstream** of the TSS [16-18].

### **Potential for Epigenomic Off-Targets**
*   While avoiding permanent mutations, dCas9 activators like **dCas9-p300** could theoretically leave a **low-level global epigenetic footprint** across the genome [19]. This concern arises from observations of other epigenetic editors, such as dCas9-DNMT3A, which was found to leave methylation marks independent of the sgRNA sequence, although it is yet to be determined if dCas9-p300 exhibits a similar pervasive effect [19, 20].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/congting_2023_off_target_effects_in_crispr_cas9_gene_editing.pdf#Passage 17|Pasaje 17]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/congting_2023_off_target_effects_in_crispr_cas9_gene_editing.pdf|PDF]]
- Texto literal:
> The Cas9/sgRNA complex produces site-specific DNA double-strand breaks (DSBs), stimulating homology-directed repair (HDR) or non-homologous end joining (NHEJ) pathways to achieve genome editing. HDR is an accurate but inefficient mechanism, which utilizes a homologous donor template to repair DNA cleavages (Li et al., 2019; Fu

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf#Passage 10|Pasaje 10]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf|PDF]]
- Texto literal:
> Chromosomal disorganization. The safety of CRISPR-based geneediting technology is a key topic of concern for researchers. The cleavage of double-stranded DNA by Cas9 usually triggers NHEJ repair, and these repaired DNA strands are usually missing a few base pairs or have a few added base pairs, which is the expected result. However, when verifying editing efficiency, researchers found that massive base deletions and chromosomal structural translocations sometimes occurred.320,330–332 These errors may lead to positional diseases such as malignant tumors and are obviously not acceptable in clinical applications, although the probability of their occurrence is low.110,333

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf|PDF]]
- Texto literal:
> In A375 cells, which were screened previously with the GeCKO and Avana libraries2,16, the Brunello library showed greater depletion of sgRNAs targeting essential genes (AUC= 0.80), while sgRNAs targeting non-essential genes showed no evidence of depletion (AUC= 0.42; Fig. 1b). Conversely, non-targeting sgRNAs were among the least depleted (AUC= 0.16), evidence of the well-described cutting effect in CRISPRko screens, whereby dsDNA breaks lead to detectable effects on cell growth; this is magnified in extreme cases such as copy number amplified target sites or promiscuous sgRNAs16,22–24.

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf|PDF]]
- Texto literal:
> Comparison of CRISPRko and CRISPRi. The dAUC and ROC-AUC metrics showed that Brunello and Dolcetto provided similar discrimination between essential and non-essential genes. We next examined the data for signs of cutting-related toxicity, as has been previously been reported to be present with CRISPRko22–24

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/yu_2015_making_sense_of_gwas_using_epigenomics_and_genome.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/yu_2015_making_sense_of_gwas_using_epigenomics_and_genome.pdf|PDF]]
- Texto literal:
> or the clustered regularly interspaced short palindromic repeats (CRISPRs) have allowed researchers to investigate functionality of genomic elements in the endogenous context in almost any organism [90]. Using these genomic engineering platforms, regulatory elements can be deleted from the genome without the introduction of exogenous sequences. In addition, the same genomic platforms can be used to epigenetically alter the genomic sequences containing a risk-associated SNP.

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf#Passage 7|Pasaje 7]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf|PDF]]
- Texto literal:
> As with CRISPRi, sgRNA location is essential for effective gene upregulation. We again used FANTOM to annotate the TSS, but instead targeted a window that was 150–75 nucleotides upstream of the TSS, based on re-analysis of previous data18,40

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|PDF]]
- Texto literal:
> In accordance with a previous report, we confirmed that dCas9-p300CD could induce gene expression through histone acetylation. Like Hilton et al. [7], we observed that a single gRNA sequence is sufficient for transcriptional activation, and that this sequence is located approximately 60-bp upstream from the transcriptional start site. Additionally, we investigated the potential effects of dCas9-p300CD from two points of view. First, we clarified that artificial histone acetylation

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|PDF]]
- Texto literal:
> These aforementioned locus-specific epigenetic manipulation strategies are based on overexpression of a dCas9-fused epigenetic modifier complex. Such tools have been shown to specifically manipulate the expression of the target loci. However, whether overexpression of the fusion epigenetic complexes may leave a low level but global epigenetic footprint in the genome, as noted for the dCas9–DNMT3A fusion complex134, is yet to be determined. Therefore, novel strategies that enable local recruitment of endogenous epigenetic machineries may provide a higher precision in epigenetic editing. To this end, novel approaches such as Fkbp/Frb-based inducible recruitment for epigenome editing by Cas9 (FIRE–Cas9)145 may provide higher specificity in epigenetic editing by recruiting endogenous chromatin regulators.

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/congting_2023_off_target_effects_in_crispr_cas9_gene_editing.pdf|congting_2023_off_target_effects_in_crispr_cas9_gene_editing.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/hongyi_2020_applications_of_genome_editing_technology_in_the_targeted.pdf|hongyi_2020_applications_of_genome_editing_technology_in_the_targeted.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf|kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf|tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/yu_2015_making_sense_of_gwas_using_epigenomics_and_genome.pdf|yu_2015_making_sense_of_gwas_using_epigenomics_and_genome.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/ashot_2019_site_specific_manipulation_of_arabidopsis_loci_using_crispr.pdf|ashot_2019_site_specific_manipulation_of_arabidopsis_loci_using_crispr.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/fatemeh_2019_crispr_cpf1_proteins_structure_function_and_implications_for.pdf|fatemeh_2019_crispr_cpf1_proteins_structure_function_and_implications_for.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/hilton_2015.pdf|hilton_2015.pdf]]
