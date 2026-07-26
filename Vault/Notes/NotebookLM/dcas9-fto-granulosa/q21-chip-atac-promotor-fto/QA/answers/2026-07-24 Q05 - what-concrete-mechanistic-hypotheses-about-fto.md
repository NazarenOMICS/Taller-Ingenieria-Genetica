---
type: reference
status: current
date: 2026-07-24
source: "notebooklm:dcas9-fto-granulosa/q21-chip-atac-promotor-fto"
related:
  - "[[Notes/Dashboards/Public ChIP-seq and ATAC-seq at FTO promoter]]"
---

# Q05 - What concrete mechanistic hypotheses about FTO promoter control can be generated from the public chromatin datasets, and how tentative are they?

Based on the provided sources, public chromatin datasets (such as ENCODE and Cistrome) and the computational models derived from them have generated several concrete mechanistic hypotheses regarding the control of the ***FTO*** promoter and its associated regulatory circuitry. These range from established interaction models to tentative predictions requiring further validation.

### **1. Derepression of Distal Enhancers (Highly Characterized)**
The most prominent hypothesis identifies the ***FTO*** locus as a regulatory "hub" for distant target genes.
*   **The Mechanism:** The risk allele (C) at **rs1421085**—located in the first intron of ***FTO***—disrupts a conserved motif for the **ARID5B repressor**  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf#Passage 6|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf#Passage 7|[2]]]. This leads to the "derepression" of a potent enhancer, which then forms long-range 3D chromatin interactions with the promoters of ***IRX3*** and ***IRX5***, doubling their expression and activating adipogenesis  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf#Passage 6|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf#Passage 7|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/paola_2018_using_three_dimensional_regulatory_chromatin_interactions_from_adult.pdf#Passage 2|[3]]].
*   **Dataset Support:** This is supported by **Hi-C maps** (e.g., ENCODE accession ENCSR788FB) and **H3K27ac/H3K4me3 ChIP-seq** data defining the enhancer-promoter anchors  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/paola_2018_using_three_dimensional_regulatory_chromatin_interactions_from_adult.pdf#Passage 2|[3]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 5|[4]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 13|[5]]].
*   **Tentativeness:** This is described as a **"well-characterized regulatory locus"** and is treated as a benchmark case study for noncoding variant function  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 14|[6]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yang_2026_the_orchestrated_interplay_between_dna_methylation_and_n6.pdf#Passage 1|[7]]].

### **2. Epigenetic Silencing via DNA Methylation (Disease-Specific)**
The methylation status of the ***FTO*** promoter itself is a key mechanism of control.
*   **The Mechanism:** Epigenetic "writers" **DNMT1, DNMT3A, and DNMT3B** can increase the methylation status of the ***FTO*** promoter, thereby directly **reducing its expression**  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yang_2026_the_orchestrated_interplay_between_dna_methylation_and_n6.pdf#Passage 4|[8]]]. 
*   **Dataset Support:** This hypothesis is drawn from integrated analyses of **whole-genome bisulfite sequencing (WGBS)** and gene expression datasets in models of alcohol-induced kidney injury  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yang_2026_the_orchestrated_interplay_between_dna_methylation_and_n6.pdf#Passage 4|[8]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 6|[9]]].
*   **Tentativeness:** While concrete in specific pathological models, its universality across other tissues is less defined, categorizing it as a **moderate-confidence** disease-related mechanism.

### **3. Regulation by Developmental and Androgen TFs (Predicted)**
Deep learning models (TREDNet) trained on ENCODE profiles have prioritized several transcription factors (TFs) that modulate the ***FTO*** regulatory environment in specific cell types.
*   **The Mechanism:** 
    *   **ONECUT2:** Variant rs1421085 is predicted to strengthen enhancer activity in granulosa-like cells (BMECs) by disrupting the binding of **ONECUT2**, a known suppressor of androgen receptor signaling  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 7|[10]]].
    *   **ONECUT1:** Variant rs8050136 is predicted to disrupt a binding site for **ONECUT1**, a factor essential for pancreatic development, potentially linking the locus to metabolic dysfunction  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 9|[11]]].
    *   **T-box Family (TBX20/21):** Variant rs3751812 is predicted to modulate binding sites for T-box factors in the fetal brain, which are critical for hypothalamic-pituitary lineage commitment  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/angelo_2007_genome_wide_association_scan_shows_genetic_variants_in.pdf#Passage 1|[12]]].
*   **Tentativeness:** These are labeled as **"predicted"** or **"nominated"** mechanisms  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 7|[10]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 9|[11]]]. The T-box hypothesis is explicitly noted as **tentative** because the "short temporal window of expression" for these TFs makes causal inference challenging  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/angelo_2007_genome_wide_association_scan_shows_genetic_variants_in.pdf#Passage 1|[12]]].

### **4. Stress Response Activation (Early-Stage "Hint")**
The ***FTO*** gene is hypothesized to be part of the cellular stress response network.
*   **The Mechanism:** ***FTO*** is reportedly **down-regulated** when the heat shock response transcription factor **Htf1** is inhibited  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yi_chun_2010_hypothalamic_specific_manipulation_of_fto_the_ortholog_of.pdf#Passage 1|[13]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yi_chun_2010_hypothalamic_specific_manipulation_of_fto_the_ortholog_of.pdf#Passage 2|[14]]].
*   **Dataset Support:** This stems from early experimental models integrated into broader literature reviews on obesity-related traits  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yi_chun_2010_hypothalamic_specific_manipulation_of_fto_the_ortholog_of.pdf#Passage 1|[13]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/zhang_2025_fosl2_facilitates_chromatin_accessibility_to_determine_developmental_events.pdf#Passage 5|[15]]].
*   **Tentativeness:** The sources refer to this as a **"hint"** or a "possible candidate for the mediation of ***Fto***'s actions," indicating it is an **exploratory** hypothesis that has not yet been study in detail across diverse chromatin datasets  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yi_chun_2010_hypothalamic_specific_manipulation_of_fto_the_ortholog_of.pdf#Passage 1|[13]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yi_chun_2010_hypothalamic_specific_manipulation_of_fto_the_ortholog_of.pdf#Passage 2|[14]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/zhang_2025_fosl2_facilitates_chromatin_accessibility_to_determine_developmental_events.pdf#Passage 1|[16]]].

### **5. Resistance to Maturation-Specific Remodeling**
In reproductive biology, research into **Fosl2** provides a negative hypothesis for ***Fto*** control.
*   **The Mechanism:** While **Fosl2** is a master initiator of chromatin opening for developmental genes during follicular maturation, the ***Fto*** promoter appears to be **excluded** from this dynamic regulation  [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/zhang_2025_fosl2_facilitates_chromatin_accessibility_to_determine_developmental_events.pdf#Passage 6|[17]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/zhang_2025_fosl2_facilitates_chromatin_accessibility_to_determine_developmental_events.pdf#Passage 2|[18]]]. 
*   **Dataset Support:** **ATAC-seq** and **H3K4me3 CUT&Tag** data show that while nearby developmental genes (like *Cyp11a1*) undergo massive remodeling, ***Fto*** expression and accessibility remain **unchanged** [19-21].
*   **Tentativeness:** This is a **high-confidence** observation within the context of granulosa cell maturation, where ***Fto*** serves as a stable control in these experimental models [19].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf#Passage 7|Pasaje 7]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf|PDF]]
- Texto literal:
> and TAD boundary regions (Mei et al., 2019) (see Table 1). For example, the rs1421085 T→C substitution associated with obesity impairs the functioning of the negative regula- tory region controlling expression of the IRX3 and IRX5 genes (Claussnitzer et al., 2015). The rs1421085 locus is located in the intron of the FTO gene (Fig. 1) at a considerable distance from the transcription start sites of IRX3 and IRX5 (~520,000 and ~1,164,000 bases). Normally, the DNA region containing allele T interacts with a repressor factor ARID5B, leading to a decrease in transcriptional activity of IRX3 and IRX5 genes. In carriers of the mutant variant of the DNA sequence (allele C), the binding site of the ARID5B repressor factor is disrupted, which causes an excessively high expression of the IRX3 and IRX5 genes and activates adipogenesis (Claussnitzer et al., 2015).

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/paola_2018_using_three_dimensional_regulatory_chromatin_interactions_from_adult.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/paola_2018_using_three_dimensional_regulatory_chromatin_interactions_from_adult.pdf|PDF]]
- Texto literal:
> We focused on cortex given empirical data connecting this tissue to schizophrenia and intelligence using orthogonal functional genomic data (bulk tissue mRNA-seq, single-cell RNA-seq, enhancer marks, and open chromatin) 28,49-51. We selected an inclusive set of 16,308 genes (77.8% of all protein-coding genes, GENCODE) with any expression in adult or fetal cortex 43,44. Second, we selected eQTL SNP-gene pairs from CommonMind or GTEx (q<0.05) 18,43. Third, using our eHi-C data, we identified HCRCI in adult or fetal cortex (P<2.31x10-11, Bonferroni correction of a=0.001 for 43,222,677 possible interactions). As in ENCODE and PsychENCODE 19,52, we identified anchors that overlapped enhancers (E) or promoters (P) using cortical functional genomic data from the same developmental stage (Table S2). E were defined as the intersection of: eHi-C HindIII fragment within an anchor, open chromatin, and either a H3K27ac peak or a H3K4me3 peak overlapping the start site of a brain-expressed transcript. P were defined as brainexpressed transcripts overlapping open chromatin. We focused on 75,531 adult and 75,246 fetal cortex E-P or P-P HCRCI. Figures 8a-g show representative examples as browser tracks.

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 5|Pasaje 5]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf|PDF]]
- Texto literal:
> The identification of multiple reSNVs at several susceptibility loci is suggestive of regulatory mechanisms wherein 1 gene can be regulated by multiple enhancers, according to which, the expression of a target gene can be influenced by >1 variant [92, 103]. For example, 2 distinct variants in the FSHB locus, rs10835638 and rs11031006, alter FSHB expression, ultimately contributing to infertility [18]. These variants may occur in

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 13|Pasaje 13]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf|PDF]]
- Texto literal:
> We performed a functional assessment of PCOS susceptibility loci by integrating epigenomic data, functional assays, and a deep learning (DL)-based approach to predict regulatory single nucleotide variants (SNVs) across 11 disease-associated cell types. We further investigated their potential influence on the molecular mechanisms underlying PCOS etiology. This approach facilitated the identification of key transcription factors (TFs) involved in folliculogenesis, androgen-mediated signaling, and ovarian development, whose binding sites are predicted to be disrupted by regulatory variants. Using the well-characterized regulatory locus of FTO, which harbors distal enhancers targeting IRX3, we demonstrate how DL models combined with prior knowledge of key PCOS TFs can effectively prioritize regulatory variants.

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 14|Pasaje 14]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf|PDF]]
- Texto literal:
> 91. Smemo S, Tena JJ, Kim KH, et al. Obesity-associated var- iants within FTO form long-range functional connections with IRX3. Nature. 2014;507(7492):371-375.

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yang_2026_the_orchestrated_interplay_between_dna_methylation_and_n6.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/yang_2026_the_orchestrated_interplay_between_dna_methylation_and_n6.pdf|PDF]]
- Texto literal:
> ALKBH5 ALKBH5 expression level was increased through the hypomethylation of its promoter.

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yang_2026_the_orchestrated_interplay_between_dna_methylation_and_n6.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/yang_2026_the_orchestrated_interplay_between_dna_methylation_and_n6.pdf|PDF]]
- Texto literal:
> Yu JT, Hu XW, Chen HY, Yang Q, Li HD, Dong YH, Zhang Y, Wang JN, Jin J, Wu YG, Li J, Ge JF, Meng XM. 2021. DNA methylation of FTO promotes renal inflammation by enhancing m(6)A of PPAR-a in alcohol-induced kidney injury. Pharmacological Research 163(2):105286 DOI 10.1016/j.phrs.2020.105286.

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 6|Pasaje 6]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf|PDF]]
- Texto literal:
> We identified 12 reSNVs exhibiting significant fold changes across 9 cell types (Fig. S8 [27]). Among these, 3 variants, rs1421085, rs11642015, and rs9940128 have been validated by MPRA studies to show allelic changes in enhancer activity in mouse preadipocyte and/or neuronal cell lines [92], further supporting the predictive accuracy of TREDNet in identifying regulatory variants. Interestingly, we predicted that T-to-C substitution at rs1421085 additionally strengthens enhancer activity in BMEC, a granulosa-like cell line, by potentially disrupting the binding site of ONECUT2 (Fig. 4A, Table S9 [27]), a suppressor of androgen receptor signaling which was recently identified as a marker of follicle growth [94, 95].

### Extracto 9
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 7|Pasaje 7]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf|PDF]]
- Texto literal:
> We also identified another reSNV within this locus, rs8050136, where C-to-A substitution is predicted as an enhancer- strengthening variant in the pancreas and liver (Fig. 4A). This variant colocalizes with an eQTL for IRX3 in the pancreas, where it regulates the conversion of β cells to ϵ cells, directly linking it to type 2 diabetes [97]. Notably, rs8050136 is also predicted to dis- rupt the binding site of ONECUT1, a TF essential for pancreatic development (Fig. 4A). However, no allelic differences were predicted in KGN or related granulosa-like cell types, suggesting that this variant is unlikely to have direct consequences on PCOS pathophysiology.

### Extracto 10
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf#Passage 9|Pasaje 9]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf|PDF]]
- Texto literal:
> The allelic effects of variants in this locus may also impact IRX3/IRX5-mediated functions in hypothalamic neurons (Fig. S7 [27]), as demonstrated in mice [92]. In this regard, we predicted rs3751812 as a regulatory variant in fetal brain which is located within binding sites of T-box family TFs (Fig. 4A). Members of the T-box family play a critical role in the commitment of hypothalamus and pituitary lineages from neuronal precursors

### Extracto 11
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yi_chun_2010_hypothalamic_specific_manipulation_of_fto_the_ortholog_of.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/yi_chun_2010_hypothalamic_specific_manipulation_of_fto_the_ortholog_of.pdf|PDF]]
- Texto literal:
> Autònoma de Barcelona, Barcelona, Spain, 3 CIBER de Diabetes y Enfermedades Metabólicas Asociadas (CIBERDEM), Barcelona, Spain

### Extracto 12
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/zhang_2025_fosl2_facilitates_chromatin_accessibility_to_determine_developmental_events.pdf#Passage 5|Pasaje 5]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/zhang_2025_fosl2_facilitates_chromatin_accessibility_to_determine_developmental_events.pdf|PDF]]
- Texto literal:
> In this study, we characterized the reorganization of chromatin accessibility that precipitates extensive transcriptomic alterations associated with GCs across different follicular maturation phases in

### Extracto 13
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/zhang_2025_fosl2_facilitates_chromatin_accessibility_to_determine_developmental_events.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/zhang_2025_fosl2_facilitates_chromatin_accessibility_to_determine_developmental_events.pdf|PDF]]
- Texto literal:
> Given that GAAs are responsible for strong downstreamGDGs, we comprehensively analyzed GDG dynamics in response to Fosl2 disruption. At global levels, numerousdevelopmental signalingpathways, including the G2M checkpoint pathway, were significantly disrupted upon Fosl2 suppression (Supplementary Fig. 5d). A plethora of GDGs were significantly downregulated after Fosl2 knockdown, including Cyp11a1, Star, Fshr and other well-recognized growth and differentiation-associated GC genes that are proximal to GAAs (Sup-plementary Fig. 5e); however, this downregulation was in stark contrast to the stable expression of a randomly selected control gene set (Fig. 5c). Moreover, after examining Fosl2 enrichment in both gene sets, we found GDGs displayed pronounced Fosl2 enrichments at their TSSs (Fig. 5d). Consistent with this observation, in distal genomic regions, we demonstrated substantially stronger binding signals in proximity to GDGs when compared to the random gene set, highlighting its essential role on harboring the wave of GDGs both at their promoters and within distal regions (Fig. 5e). To further elucidate Fosl2-driven GAA functions in shaping GDG transcriptomic repertoires, we examined accessibility densities in these gene sets in Fosl2 knockdown cells. We found that GDGs exhibited a substantial reduction in accessibility densities compared with randomly selected genes, aligning with the observed downregulation of GDG expression following Fosl2 suppression (Fig. 5f). Two representative GDGs, Fshr and Mapk1, which were proximal to GAAs, displaying elevated gene expression and augmented Fosl2 binding at the ovulatory phase47,53. Nevertheless, the transcription program and accessibility density of these two GDGs were robustly decreased after Fosl2 knockdown. Consistently, fluorescence intensities of these two GDGs were also correspondingly attenuated after Fosl2 knockdown (Fig. 5g, left). In comparison, the selected Fto and Gapdh, which belong to a random gene set displayed unchanged expression both during follicular maturation and Fosl2 silencing scenarios (Fig. 5g, right). Collectively, our data substantiate a model wherein Fosl2 binding to GAAs consolidates an open chromatin conformation, thereby orchestrating a broad transcriptional program of GDGs, which is fundamental to multiple developmental processes.

### Extracto 14
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/zhang_2025_fosl2_facilitates_chromatin_accessibility_to_determine_developmental_events.pdf#Passage 6|Pasaje 6]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/zhang_2025_fosl2_facilitates_chromatin_accessibility_to_determine_developmental_events.pdf|PDF]]
- Texto literal:
> one-sided Fisher’s exact test. e Heatmaps showing the different clusters of Fosl2 binding signals with CUT&Tag and their mapping in ATAC-seq peaks at the different maturation phases and peaks following Fosl2 suppression (left). The enrichment of normalized ATAC-seq peaks after Fosl2 knockdown is also shown both in antral- and ovulatory-specific clusters (right). f IGV views displaying the Fosl2 CUT&Tag, ATAC-seq signals under differentmaturation phases and signals in Fosl2-silenced cells in representative Tgfb1, Cyp11a1, Cdc20 and Hspa6 from ovulatory-specific (left) and antral-specific (right) clusters. ChIP-qPCR is also used to measure the relative H3K4me3 levels after Fosl2 knockdown within these genes. IgG is used as the negative control. The enrichment is normalized to a 1:10 dilution of the input. Error bars indicate themean ± S.E.M. (n = 3 biological replicates). The p value was generated from a two-sided Student’s t test. N.S. not significant, ***p <0.001. Source data are provided as a Source Data file.

### Extracto 15
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/zhang_2025_fosl2_facilitates_chromatin_accessibility_to_determine_developmental_events.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/zhang_2025_fosl2_facilitates_chromatin_accessibility_to_determine_developmental_events.pdf|PDF]]
- Texto literal:
> randomly selected genes (left, n = 2068) and GDGs (right, n = 2068) in distal genomic regions under different maturation phases. In a–c and e, the p value was generated from a two-sided Wilcoxon rank-sum test. Boxplot summary statistics are: center line: median; upper/lower hinges: 75th and 25th percentiles, upper and lowerwhiskers represent the data extending from the hinge to atmost 1.5 times the interquartile range. f Heatmaps and enrichment plots showing normalized read densities of ATAC-seq signals for randomly selected genes and GDGs after Fosl2 knockdown. Tracks are centered at the TSS and extend ±3 kb. g IGV views displaying the Fosl2 CUT&Tag under differentmaturation phases, ATAC-seq and RNA-seq signals following Fosl2 suppression in representative Fshr, Mapk1, Fto and Gapdh from GDGs (left) and randomly selected genes (right) subsets. h Immunofluorescence staining of the aforementioned genes after Fosl2 knockdown in pGC. The position of the nucleolus is indicated by DAPI staining. Results shown are representative of n = 3 biologically independent experiments with similar results. Scale bar, 40μm.

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/angelo_2007_genome_wide_association_scan_shows_genetic_variants_in.pdf|angelo_2007_genome_wide_association_scan_shows_genetic_variants_in.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf|e_2021_disease_associated_genetic_variants_in_the_regulatory_regions.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/paola_2018_using_three_dimensional_regulatory_chromatin_interactions_from_adult.pdf|paola_2018_using_three_dimensional_regulatory_chromatin_interactions_from_adult.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf|srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yang_2026_the_orchestrated_interplay_between_dna_methylation_and_n6.pdf|yang_2026_the_orchestrated_interplay_between_dna_methylation_and_n6.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yi_chun_2010_hypothalamic_specific_manipulation_of_fto_the_ortholog_of.pdf|yi_chun_2010_hypothalamic_specific_manipulation_of_fto_the_ortholog_of.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/zhang_2025_fosl2_facilitates_chromatin_accessibility_to_determine_developmental_events.pdf|zhang_2025_fosl2_facilitates_chromatin_accessibility_to_determine_developmental_events.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/anthony_2018_shared_genetic_contribution_to_type_1_and_type.pdf|anthony_2018_shared_genetic_contribution_to_type_1_and_type.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/carrasco_2026_novel_genome_editing_approaches_to_manipulate_apical_meristem.pdf|carrasco_2026_novel_genome_editing_approaches_to_manipulate_apical_meristem.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/haiyan_2024_ythdf2_upregulation_and_subcellular_localization_dictate_cd8_t.pdf|haiyan_2024_ythdf2_upregulation_and_subcellular_localization_dictate_cd8_t.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/huan_2023_scm6a_seq_reveals_single_cell_landscapes_of_the.pdf|huan_2023_scm6a_seq_reveals_single_cell_landscapes_of_the.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/jiang_2025_fto_mediated_m_lt_sup_gt_6_lt.pdf|jiang_2025_fto_mediated_m_lt_sup_gt_6_lt.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/joshi_2024_epidecoder_a_functional_exploration_tool_for_epigenetic_and.pdf|joshi_2024_epidecoder_a_functional_exploration_tool_for_epigenetic_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/madhusudhan_2019_atac_seq_reveals_alterations_in_open_chromatin_in.pdf|madhusudhan_2019_atac_seq_reveals_alterations_in_open_chromatin_in.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/paper_2024_eacr_2024_innovative_cancer_science_10_13_june.pdf|paper_2024_eacr_2024_innovative_cancer_science_10_13_june.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/wu_2026_n6_methyladenosine_modification_in_the_context_of_viral.pdf|wu_2026_n6_methyladenosine_modification_in_the_context_of_viral.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yang_2026_epigenetic_regulation_of_uterine_smooth_muscle_tumors_histone.pdf|yang_2026_epigenetic_regulation_of_uterine_smooth_muscle_tumors_histone.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yige_2023_epigenetic_and_transcriptomic_characterization_reveals_progression_markers_and.pdf|yige_2023_epigenetic_and_transcriptomic_characterization_reveals_progression_markers_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yongli_2024_pan_cistrome_analysis_of_the_leaf_accessible_chromatin.pdf|yongli_2024_pan_cistrome_analysis_of_the_leaf_accessible_chromatin.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/Sources/yunxia_2021_a_compendium_and_comparative_epigenomics_analysis_of_cis.pdf|yunxia_2021_a_compendium_and_comparative_epigenomics_analysis_of_cis.pdf]]
