---
type: reference
status: current
date: 2026-07-14
source: "notebooklm:dcas9-fto-granulosa/q03-especificidad-off-target"
related:
  - "[[Notes/Dashboards/dCas9-p300 off-target specificity]]"
---

# Q01 - According to these sources, what is known specifically about dCas9-p300 (nuclease-dead CRISPRa fusion) off-target binding or off-target transcriptional activation in human cells, as distinct from wild-type Cas9 nuclease off-target cutting?

Specifically for **dCas9-p300** (a nuclease-dead Cas9 fused to the histone acetyltransferase core domain of p300), the sources highlight several key insights regarding its off-target binding and transcriptional activation in human cells, distinguishing it from wild-type (WT) Cas9 nuclease cutting.

### **Reduced Risk Compared to Wild-Type Cas9**
*   **Avoidance of Cutting Toxicity:** Unlike wild-type Cas9, which creates double-strand breaks (DSBs) that can lead to permanent mutations or "cutting-related toxicity" at copy-number-amplified loci, dCas9-p300 performs **epigenetic editing** without altering the DNA sequence  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf#Passage 2|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf#Passage 1|[3]]].
*   **Reversibility:** Because it does not modify the underlying genome, the transcriptional changes induced by dCas9-based regulatory systems are **reversible**, which reduces the long-term risks associated with unintended off-target cutting  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf#Passage 1|[3]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf#Passage 2|[4]]].

### **Binding vs. Functional Activation**
*   **Off-Target Binding Sites:** Genome-wide mapping (ChIP-seq) of dCas9 indicates that off-target binding sites are often **enriched in open chromatin regions**  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 1|[5]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/congting_2023_off_target_effects_in_crispr_cas9_gene_editing.pdf#Passage 1|[6]]].
*   **Binding Does Not Equal Activation:** There is a less stringent requirement for dCas9-DNA binding than for nuclease cleavage  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/congting_2023_off_target_effects_in_crispr_cas9_gene_editing.pdf#Passage 1|[6]]]. Sources note that while dCas9 may bind to numerous off-target sites, only a **limited number of these sites result in functional consequences** like transcriptional activation  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/congting_2023_off_target_effects_in_crispr_cas9_gene_editing.pdf#Passage 1|[6]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/yu_2015_making_sense_of_gwas_using_epigenomics_and_genome.pdf#Passage 1|[7]]].
*   **Specificity in Regulation:** CRISPR/dCas9 platforms have been described as "remarkably specific" in both DNA binding and gene regulation compared to earlier tools like TALEs or zinc fingers  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 2|[8]]].

### **Potential for "Global Epigenetic Footprints"**
*   **sgRNA-Independent Effects:** While dCas9-p300 is used for site-specific manipulation, there is ongoing research into whether the overexpression of such fusion complexes might leave a **low-level but global epigenetic footprint** across the genome  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 3|[9]]].
*   **Comparison to Other Modifiers:** This concern is based on observations of other epigenetic editors, such as **dCas9-DNMT3A**, which was found to leave methylation footprints independent of the sgRNA used  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 3|[9]]]. It is "yet to be determined" if dCas9-p300 exhibits a similar pervasive global off-target effect  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 3|[9]]].

### **Unique Potency at Enhancers and Promoters**
*   **Single gRNA Efficiency:** A specific characteristic of dCas9-p300 is its high potency; it can successfully activate target genes from **both promoter and enhancer regions** using only a **single guide RNA**  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/yu_2015_making_sense_of_gwas_using_epigenomics_and_genome.pdf#Passage 2|[10]]]. In contrast, other dCas9 activators (such as dCas9-VP64) often require multiple gRNAs to achieve comparable levels of gene expression [11].
*   **Direct Acetylation:** This efficiency is attributed to the fact that p300 **directly regulates histone acetylation** (specifically increasing local **H3K27ac** levels), whereas activators like VP64 must recruit endogenous histone acetyltransferases to the site  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/yu_2015_making_sense_of_gwas_using_epigenomics_and_genome.pdf#Passage 2|[10]]].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf|PDF]]
- Texto literal:
> Comparison of CRISPRko and CRISPRi. The dAUC and ROC-AUC metrics showed that Brunello and Dolcetto provided similar discrimination between essential and non-essential genes. We next examined the data for signs of cutting-related toxicity, as has been previously been reported to be present with CRISPRko22–24

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf|PDF]]
- Texto literal:
> a biofilm or adding peptides recognized by target cell recep-tors.232,334,335 Designing environmentally responsive nanoparticles according to the target organ microenvironment enhances gene drug enrichment, such as variations in pH, reactive oxygen species (ROS), and adenosine triphosphate (ATP) levels.33 The nanomaterial shell disintegrates in a specific environment, exposing the core, which then enters the cell through endocytosis. However, when the microenvironment in certain diseased tissues does not differ significantly from that of other tissues, constructing a nanoparticle that is induced by multiple conditions to release its contents is a feasible method for disease-specific targeting. In addition, light-, magnetic-, and ultrasound-responsive CRISPR/Cas9 delivery systems have been developed to support precision delivery.33 When applied to the treatment of human diseases, the administration of drugs by in situ injection prevents them from being transported in the blood flow throughout the body. Regulating the expression of target genes may require a more modest CRISPRa or CRISPRi approach, and the changes imposed by CRISPR/dCas9-based transcriptional regulatory systems are reversible compared to altering genomic sequences to silence genes.59,143

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|PDF]]
- Texto literal:
> In addition to these studies that expand the targeting scope of CRISPR tools, researchers are actively developing novel ways to increase the targeting specificity of the CRISPR-Cas9 system. Understanding the extent of off-target effects of CRISPR-Cas9 targeting has been one major goal. Given that CRISPR systems have evolved as a defense system against viruses that tend to frequently mutate, a slightly less specific CRISPR system would be advantageous to bacteria. Indeed, the early efforts to understand CRISPR targeting specificity highlighted this fact and demonstrated that the system may potentially have off-target effects61– 65. In addition to these initial studies, researchers utilized alternative genome-wide tools to understand CRISPR-Cas9 targeting specificity. To this end, we and others have used the chromatin immunoprecipitation and high throughput sequencing (ChIP-Seq) approach to map DNA binding sites of catalytically inactive SpCas9 in vivo66,67. These whole-genome mapping studies

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/congting_2023_off_target_effects_in_crispr_cas9_gene_editing.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/congting_2023_off_target_effects_in_crispr_cas9_gene_editing.pdf|PDF]]
- Texto literal:
> WGS analysis of off-target effects has been well documented in cell culture studies (Smith et al., 2014; Veres et al., 2014; Iyer et al., 2015). By comparing the genome sequences before and after CRISPR/Cas9 editing, WGS can directly uncover desired and unwanted editing events. The accuracy and sensitivity of WGS in off-target detection is determined by sequencing depth, thus when

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/yu_2015_making_sense_of_gwas_using_epigenomics_and_genome.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/yu_2015_making_sense_of_gwas_using_epigenomics_and_genome.pdf|PDF]]
- Texto literal:
> or the clustered regularly interspaced short palindromic repeats (CRISPRs) have allowed researchers to investigate functionality of genomic elements in the endogenous context in almost any organism [90]. Using these genomic engineering platforms, regulatory elements can be deleted from the genome without the introduction of exogenous sequences. In addition, the same genomic platforms can be used to epigenetically alter the genomic sequences containing a risk-associated SNP.

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|PDF]]
- Texto literal:
> These aforementioned locus-specific epigenetic manipulation strategies are based on overexpression of a dCas9-fused epigenetic modifier complex. Such tools have been shown to specifically manipulate the expression of the target loci. However, whether overexpression of the fusion epigenetic complexes may leave a low level but global epigenetic footprint in the genome, as noted for the dCas9–DNMT3A fusion complex134, is yet to be determined. Therefore, novel strategies that enable local recruitment of endogenous epigenetic machineries may provide a higher precision in epigenetic editing. To this end, novel approaches such as Fkbp/Frb-based inducible recruitment for epigenome editing by Cas9 (FIRE–Cas9)145 may provide higher specificity in epigenetic editing by recruiting endogenous chromatin regulators.

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|PDF]]
- Texto literal:
> is to locally deposit H3K27ac marks. Therefore, in contrast to the local reduction of enhancer marks by dCas9-LSD1, recruitment of histone acetyl transferase P300 through dCas9 fusion (dCas9-P300) resulted in a significant increase in local H3K27ac levels at enhancer elements142. Importantly, unlike other dCas9-fused transactivators, which can result in induction of gene expression primarily from promoter regions, targeting dCas9-P300 allows significant gene expression induction from both promoter and enhancer regions142. Researchers have also exploited other epigenetic modifiers to manipulate additional epigenetic marks. Among these, dCas9 fusion to the PRDM9 methyltransferase fusion complex has been utilized to manipulate local H3K4me3 marks143. Notably, local induction of H3K4me3, which is a marker of active promoters, was observed to be sufficient to allow re-expression of silenced target genes in various cell types143. Histone de-acetylation has been another strategy to locally manipulate chromatin structure and function. To this end, dCas9 fusion to histone deacetylases (HDAC), specifically full-length HDAC3, has been shown to effectively reduce the H3k27ac at the target loci and reduce the gene expression of the target loci144.

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/yu_2015_making_sense_of_gwas_using_epigenomics_and_genome.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/yu_2015_making_sense_of_gwas_using_epigenomics_and_genome.pdf|PDF]]
- Texto literal:
> To achieve the opposite effect, investigators have used domains such as VP64, an activating domain that recruits HATs, as well as the enzymatic domain of the p300 HAT to increase the levels of active epigenetic marks at regulatory elements. Gao et al. modified enhancers that regulate the Oct 4 gene using either TALE-VP64 or dCas9-VP64. These enhancers are normally only active in embryonic stem cells and are marked by the repressive histone modification H3K27me3 in mouse embryonic fibroblasts. They found that dCas9-VP64 less robustly activates the Oct4 enhancers compared to TALE-VP64; in addition, TALE-VP64 constructs targeted to these enhancers decreased levels of H3K27me3 and increased levels of the active marks H3K27Ac and H3K4me1 [103]. Polstein et al. used TALE-VP64 and dCas9-VP64 for comparison in genome-wide DNA binding, gene expression, and DHS-seq [94]. Although both platforms demonstrated high specificity in DNA binding and gene expression assay, there were several differences. Namely, ChIP-seq signals at the target sites were higher for dCas9-VP64 than for TALE-VP64, whereas gene expression was greater using TALE-VP64. The authors speculate that perhaps the dissociation of genomic DNA caused by the RNA-DNA interactions mediated by the guide RNA affected nearby transcription complexes; they suggest that new dCas9-based activator platforms may show more robust transcriptional activity [105]. A recent study showed that the catalytic domain of the HAT P300 (P300core) fused to dCas9 could activate target enhancers and promoters. In this study, a single gRNA targeting an enhancer region with dCas9-P300 core was sufficient to activate target gene expression, whereas other dCas9 activators required several gRNAs to achieve high levels of gene expression [106]. The authors suggested that the P300 domain may be superior to the VP64 domain because P300 directly regulates histone acetylation whereas VP64 must recruit

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/congting_2023_off_target_effects_in_crispr_cas9_gene_editing.pdf|congting_2023_off_target_effects_in_crispr_cas9_gene_editing.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf|kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf|tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/yu_2015_making_sense_of_gwas_using_epigenomics_and_genome.pdf|yu_2015_making_sense_of_gwas_using_epigenomics_and_genome.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/ashot_2019_site_specific_manipulation_of_arabidopsis_loci_using_crispr.pdf|ashot_2019_site_specific_manipulation_of_arabidopsis_loci_using_crispr.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/fatemeh_2019_crispr_cpf1_proteins_structure_function_and_implications_for.pdf|fatemeh_2019_crispr_cpf1_proteins_structure_function_and_implications_for.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/hongyi_2020_applications_of_genome_editing_technology_in_the_targeted.pdf|hongyi_2020_applications_of_genome_editing_technology_in_the_targeted.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf]]
