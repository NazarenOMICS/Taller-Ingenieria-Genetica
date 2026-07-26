---
type: notebook-source
source_id: "49227af1-333c-4504-89d0-de5d98fecfea"
notebook_id: "88cd18f7-147a-46da-adea-544dfdab4816"
slug: "q21-chip-atac-promotor-fto"
vault_slug: "dcas9-fto-granulosa/q21-chip-atac-promotor-fto"
project: "dcas9-fto-granulosa"
url: ""
source_type: web
status: active
date: 2026-07-24
pdf: "Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf"
related:
  - "[[Notes/Dashboards/Public ChIP-seq and ATAC-seq at FTO promoter]]"
used_in_qa: true
cited_in_count: 6
qa_notes:
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/QA/answers/2026-07-24 Q01 - according-to-these-sources-there-public.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/QA/answers/2026-07-24 Q02 - which-chromatin-marks-at-fto-promoter.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/QA/answers/2026-07-24 Q03 - which-transcription-factors-appear-at-or.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/QA/answers/2026-07-24 Q04 - which-cell-types-were-those-datasets.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/QA/answers/2026-07-24 Q05 - what-concrete-mechanistic-hypotheses-about-fto.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/QA/answers/2026-07-24 Q06 - what-additional-experiments-would-be-required.md]]"
---

# srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf

## PDF

![[Research/Papers/dcas9-fto-granulosa/q21-chip-atac-promotor-fto/srivastava_2026_regulatory_risk_loci_link_disrupted_androgen_response_to.pdf]]

## Source Guide

## Cited Passages

### Passage 1

Cell type–specific DL models We used a 2-phase TREDNet model developed in our lab for cell type–specific enhancer prediction [31]. The first phase of the model was pretrained on 4560 genomic and epigenomic profiles, which included DNase I hypersensitive sites (DHS), assay for transposase-accessible chromatin using sequencing (ATAC- seq), histone chromatin immunoprecipitation sequencing (ChIP-seq), and TF ChIP-seq peaks from Encyclopedia of DNA Elements (ENCODE) v4 [32]. The second phase was fine-tuned to predict cell type–specific enhancers using training datasets described below. Chromosomes 8 and 9 were held out for testing, chromosome 6 was used for validation, and other autosomal chromosomes were used to build the second-phase model.

### Passage 2

Next, we evaluated the allele-specific effects of these reSNVs on chromatin accessibility (ATAC-seq and DNase-seq) and TF binding (ChIP-seq) in corresponding cell types available from the UDACHA and ADASTRA databases [75, 76]. Our analysis revealed that,

### Passage 3

Open chromatin (DHS or ATAC-seq) and H3K27ac profiles for the causal cell types were downloaded from ENCODE [32] (Table S2 [27]). Positive datasets were defined as 2 kb regions centered on DHS or ATAC-seq peaks overlapping with H3K27ac (or H3K4me1 in fetal brain) peaks of each cell type, excluding coding sequences, promoter proximal regions (<2 kb from transcription start sites [TSS]) and ENCODE blacklisted regions [33]. A

### Passage 4

We then assigned target genes to the pcosSNVs using the ENCODE-rE2G model (https://github.com/EngreitzLab/ENCODE_ rE2G) that predicts enhancer–gene interactions across various cell types by integrating enhancer activity, 3D chromatin interactions, and DNase I hypersensitivity maps. Applying a threshold corresponding to 70% recall, derived from the model’s CRISPR-validated benchmark dataset, we identified 128 target genes linked to pcosSNVs across 323 cell types (Table S5 [27]), many of which have not been previously associated with PCOS. The most pleiotropic loci, each connected to >10 target genes, were located near IRF1 and ERBB3, underscoring extensive distal enhancer regulation (Table S5 [27]). Notably, rs2706385 and rs2706386, situated upstream of the IRF1 promoter, were predicted to regulate RAD50 across multiple cell types, including those representing developmental lineages (Table S5 [27]). This enhancer–gene pair was further supported by ChIA-PET–derived chromatin interactions observed in the WTC11 developmental cell line (ENCODE accession ENCSR543HLV). Mouse knockout stud- ies have demonstrated a critical role for RAD50 in follicle develop- ment [56]. In addition, functional enrichment analysis of the 128 target genes revealed significant overrepresentation of genes in this locus within the JAK–STAT signaling pathway, including IL3/ 4/5/9 and CSF2, which are known STAT pathway components (Table S4 [27]). Interestingly, JAK–STAT signaling has been impli- cated in the primordial-to-follicular phase transition during folliculogenesis [55]. Together, these findings suggest that certain pcosSNVs reside within pleiotropic enhancers that may contribute to PCOS pathophysiology through distinct molecular mechanisms.

### Passage 5

The identification of multiple reSNVs at several susceptibility loci is suggestive of regulatory mechanisms wherein 1 gene can be regulated by multiple enhancers, according to which, the expression of a target gene can be influenced by >1 variant [92, 103]. For example, 2 distinct variants in the FSHB locus, rs10835638 and rs11031006, alter FSHB expression, ultimately contributing to infertility [18]. These variants may occur in

### Passage 6

We identified 12 reSNVs exhibiting significant fold changes across 9 cell types (Fig. S8 [27]). Among these, 3 variants, rs1421085, rs11642015, and rs9940128 have been validated by MPRA studies to show allelic changes in enhancer activity in mouse preadipocyte and/or neuronal cell lines [92], further supporting the predictive accuracy of TREDNet in identifying regulatory variants. Interestingly, we predicted that T-to-C substitution at rs1421085 additionally strengthens enhancer activity in BMEC, a granulosa-like cell line, by potentially disrupting the binding site of ONECUT2 (Fig. 4A, Table S9 [27]), a suppressor of androgen receptor signaling which was recently identified as a marker of follicle growth [94, 95].

### Passage 7

We also identified another reSNV within this locus, rs8050136, where C-to-A substitution is predicted as an enhancer- strengthening variant in the pancreas and liver (Fig. 4A). This variant colocalizes with an eQTL for IRX3 in the pancreas, where it regulates the conversion of β cells to ϵ cells, directly linking it to type 2 diabetes [97]. Notably, rs8050136 is also predicted to dis- rupt the binding site of ONECUT1, a TF essential for pancreatic development (Fig. 4A). However, no allelic differences were predicted in KGN or related granulosa-like cell types, suggesting that this variant is unlikely to have direct consequences on PCOS pathophysiology.

### Passage 8

In addition to rs1421085, G-to-A substitution at rs9940128 was predicted as enhancer-damaging variant in BMECs and HUVECs and was found to localize within regions forming chromatin contacts with the promoters of IRX3 and IRX5 in HUVECs (Fig. 4B). Another variant within this locus, rs7193144, was predicted to exhibit nominal allele-specific regulatory differences in KGN cells, granulosa-like cell lines, BMECs, and HUVECs (Table S9 [27]). Notably, this variant was also predicted to modulate the binding site of the AR and to display allele-specific regulatory activity in pancreas and adipocyte, making it a compelling candidate for mediating the pleiotropic effects of IRX3/IRX5 dysregulation across these cell types through disrupted androgen signaling.

### Passage 9

The allelic effects of variants in this locus may also impact IRX3/IRX5-mediated functions in hypothalamic neurons (Fig. S7 [27]), as demonstrated in mice [92]. In this regard, we predicted rs3751812 as a regulatory variant in fetal brain which is located within binding sites of T-box family TFs (Fig. 4A). Members of the T-box family play a critical role in the commitment of hypothalamus and pituitary lineages from neuronal precursors

### Passage 10

Epigenomic datasets for ovary, adrenal gland, liver, adipocyte, and pancreas were obtained from ENCODE. In the absence of primary human GC data, H3K27ac peaks from KGN cells were used as a proxy. To capture broader regulatory features, we additionally incorporated brain microvascular endothelial cells (BMECs), mammary epithelial cells, and human umbilical vein endothelial cells (HUVECs) as GC proxies based on (1) similarity of their H3K27ac profiles to those of KGN cells (Jaccard similarity index), (2) availability of chromatin accessibility profiles, and (3) availability of chromatin contact maps for downstream target gene analyses (Table S8 [27]). Similarly, in the absence of pituitary and hypothalamic epigenomic profiles, we included the fetal brain. We also incorporated WTC11, a developmental cell line, to capture regulatory variants active during early development, as fetal development has been implicated in PCOS onset later in life [66]. Cell type–specific epigenomic data used to trait the models are provided in Table S2 [27]. The DL models demonstrated robust performance, achieving an area under the receiver operating characteristic curve ranging from 0.9 to 0.98 and an area under the precision-recall curve ranging from 0.54 to 0.84 across the 11 cell types (Fig. 2A).

### Passage 11

We adapted TREDNet to predict allele-specific enhancer activity of pcosSNVs across causal cell types implicated in PCOS. Putative cell type–specific enhancers used to train the model were defined as accessible chromatin regions (identified by DNase-seq or ATAC-seq) that overlapped with H3K27ac peaks. Accordingly, we sought to identify all relevant cell types with available epigenomic data. The primary pathogenic cell types implicated in PCOS include theca and GCs, ovary, adrenal gland, liver, pancreas, hypothalamus, and pituitary, which collectively regulate folliculogenesis through signaling pathways that modulate androgen, estrogen, SHBG, and insulin levels [3]. In addition, adipocytes play a key role in driving insulin resistance, another hallmark of PCOS [3].

### Passage 12

Abstract A major challenge in deciphering the complex genetic landscape of polycystic ovary syndrome (PCOS) lies in the limited understanding of how susceptibility loci drive molecular mechanisms across diverse phenotypes. To address this, we integrated molecular and epigenomic annotations from proposed causal cell types and employed a deep learning (DL) framework to predict cell type–specific regulatory effects of PCOS-risk variants. Our analysis revealed that these variants affect key transcription factor–binding sites, including NR4A1/2, NHLH2, FOXA1, and WT1, which regulate gonadotropin signaling, folliculogenesis, and steroidogenesis across brain and endocrine cell types. The DL model, which showed strong concordance with reporter assay data, identified enhancer-disrupting activity in ∼20% of risk variants. Notably, many of these variants disrupt transcription factors involved in androgen-mediated signaling, providing molecular insights into hyperandrogenemia in PCOS. Variants prioritized by the model were more pleiotropic and exerted stronger regulatory effects on gene expression compared with other risk variants. Using the IRX3-FTO locus as a case study, we demonstrate how regulatory disruptions in tissues such as the fetal brain, pancreas, adipocytes, and endothelial cells may link obesity- associated mechanisms to PCOS pathogenesis via neuronal development, metabolic dysfunction, and impaired folliculogenesis. Collectively, our findings highlight the utility of integrating DL models with epigenomic data to uncover disease-relevant variants, reveal cross-tissue regulatory effects, and refine mechanistic understanding of PCOS.

### Passage 13

We performed a functional assessment of PCOS susceptibility loci by integrating epigenomic data, functional assays, and a deep learning (DL)-based approach to predict regulatory single nucleotide variants (SNVs) across 11 disease-associated cell types. We further investigated their potential influence on the molecular mechanisms underlying PCOS etiology. This approach facilitated the identification of key transcription factors (TFs) involved in folliculogenesis, androgen-mediated signaling, and ovarian development, whose binding sites are predicted to be disrupted by regulatory variants. Using the well-characterized regulatory locus of FTO, which harbors distal enhancers targeting IRX3, we demonstrate how DL models combined with prior knowledge of key PCOS TFs can effectively prioritize regulatory variants.

### Passage 14

91. Smemo S, Tena JJ, Kim KH, et al. Obesity-associated var- iants within FTO form long-range functional connections with IRX3. Nature. 2014;507(7492):371-375.

### Passage 15

Although our framework advances variant-to-function interpretation to better understand the regulatory landscape of PCOS, it remains constrained by the availability of comprehensive multi-omic datasets required to dissect converging disease mechanisms. First, our analyses used variants in LD blocks without stratifying by superpopulation, which may overlook ancestry-specific phenotypes that exhibit substantial variation in clinical presentation [104] and are important for understanding how genetic background influences disease risk and therapeutic response. Addressing this limitation will require large-scale association studies in diverse cohorts to enable robust, population-informed genetic associations. Second, our analysis of regulatory variants was limited to those occurring within putative enhancers. However, variants can impact gene regulation beyond enhancer activity. Variants located in silencers or insulators may disrupt distal enhancer interactions, as ob- served with IRX3, emphasizing the need for Hi-C data from patho- genic cell types to resolve target genes not identifiable through eQTL analysis. Moreover, trans-regulatory effects of risk variants, whether through TFs encoded by susceptibility loci (PROX1, PPARG, and IRF1) or noncoding RNAs that contribute to epige- nomic regulation of gene expression, also warrant systematic investigation. Third, disease susceptibility may arise at TFBSs independent of sequence variation. Gene expression can be modulated by epigenetic modifications at regulatory elements

### Passage 16

A central challenge in this endeavor lies in estimating the effect sizes of noncoding variants, which constitute over 90% of disease-associated loci. These variants act through context- dependent regulatory mechanisms that remain poorly understood without systematic genetic and epigenetic characterization in relevant cell types. Nevertheless, integrative analyses such as the one presented here, along with emerging computational and experimental frameworks for regulatory annotation and variant-to-function mapping, are progressively illuminating these mechanisms. Scaling such approaches to large GWAS and whole-genome or exome sequencing datasets will be crucial for translating genetic discoveries into individualized disease risk assessment and therapeutic insight.

### Passage 17

To assess the regulatory impact of reSNVs, we evaluated the enrichment of host TFBSs. For each TF, enrichment was calculated by comparing the density of its binding motifs overlapping reSNVs against a background set of control SNVs. The background consisted of a specifically curated set of 71 000 nonoverlapping SNVs within a 100 kb window centered on pcosSNVs (Materials and methods). This localized background enabled us to investigate the regulation of target genes within the context of PCOS-specific biological processes, particularly for ubiquitously expressed genes. Several TFs showed significant enrich- ment at reSNV loci, including FOXA1, a pioneer factor in estrogen and androgen signaling [69]; LHX4, involved in pituitary development [70]; NHLH2, associated with GnRH signaling [71]; WT1, a regulator of GC proliferation [72]; PLAG1, involved in oocyte reserve maintenance [73]; and NR4A1, which regulates steroidogenesis [74] (hypergeometric, P < 10−2, Fig. 2D). Notably, we observed a 2.7-fold enrichment of PPARG-binding sites, a significant finding given PPARG’s role as a known susceptibility locus for PCOS. We also found enrichment of TFs associated with neur- onal signaling, such as TBX21, POU6F1, and NKX6.2. While not pre- viously linked to PCOS, these TFs represent promising candidates for involvement in neuroendocrine regulation. These findings highlight the capacity of our model to identify transcriptional regulators with potential functional roles in the diverse phenotypic manifestations of PCOS.

### Passage 18

To evaluate TREDNet’s ability to predict regulatory variants, we examined the correlation between TREDNet-predicted differences in allele-specific enhancer activity and those determined through a massively parallel reporter assay (MPRA) in the developing human brain and stem cell–derived adipocytes using our model trained on fetal brains and adipocytes [67, 68]. We compared allele-specific TREDNet scores across all assayed alleles and those showing significant changes in reporter activity (Materials and methods) and observed a significantly higher

### Passage 19

In total, we identified 12 reSNVs that have been experimentally validated as enhancer-disrupting variants in adipocytes and fetal brain through MPRA studies (Table S11 [27]) [67, 68]. Of note, epigenomic data from fetal brain used by the DL model failed to capture the regulatory impact of pathogenic variants in the FSHB locus, including rs10835638 and rs11031006, which have been experimentally shown to reduce FSHB expression restricted to the pituitary gland [18]. This underscores the necessity of incorporating additional, relevant cell types for a more comprehensive study of the regulatory landscape of PCOS, when

### Passage 20

and metabolic phenotypes of PCOS [3]. Given the widespread ex- pression of AR, disruptions in circulating androgen levels impact peripheral cell types expressing AR and may have broader consequences, such as insulin resistance and altered adipogenesis, independent of classical reproductive symptoms like oligomenorrhea [100]. Moreover, regulatory variants often exert extensive pleiotropic effects [101, 102]. Therefore, PCOS-associated causal variants may contribute to disease pathophysiology through both variant pleiotropy and disrupted neuroendocrine signaling. In this context, we discuss our findings using predicted regulatory variants in the FTO locus within this framework, highlighting potential cell type–specific mechanisms by which altered androgen signaling and regulatory variant pleiotropy may drive PCOS pathogenesis.
