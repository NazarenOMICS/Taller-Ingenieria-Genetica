---
type: notebook-source
source_id: "0dc4f046-5781-4a23-ac61-fe9543c91835"
notebook_id: "e1baac88-0719-426f-b47a-b620d48b6489"
slug: "q03-especificidad-off-target"
vault_slug: "dcas9-fto-granulosa/q03-especificidad-off-target"
project: "dcas9-fto-granulosa"
url: ""
source_type: web
status: active
date: 2026-07-14
pdf: "Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf"
related:
  - "[[Notes/Dashboards/dCas9-p300 off-target specificity]]"
used_in_qa: true
cited_in_count: 4
qa_notes:
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/QA/answers/2026-07-24 Q01 - according-to-these-sources-what-known.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/QA/answers/2026-07-24 Q02 - what-guide-rna-mismatch-tolerance-or.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/QA/answers/2026-07-24 Q04 - how-does-specificity-profile-dcas9-fusion.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/QA/answers/2026-07-24 Q05 - what-gaps-or-limitations-remain-these.md]]"
---

# kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf

## PDF

![[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf]]

## Source Guide

## Cited Passages

### Passage 1

Comparison of CRISPRko and CRISPRi. The dAUC and ROC-AUC metrics showed that Brunello and Dolcetto provided similar discrimination between essential and non-essential genes. We next examined the data for signs of cutting-related toxicity, as has been previously been reported to be present with CRISPRko22–24

### Passage 2

differences between sgRNA design criteria in mouse and human cells9,12.

### Passage 3

We designed a modified tracrRNA for use in lentiCRISPRv2, hereafter called tracr-v2, which removed the Pol III termination site and extended the tetraloop by 5 base pairs (Fig. 2a). To test on- and off-target activity with tracr-v2, we designed a tiling library containing all possible sgRNAs targeting EEF2, a core

### Passage 4

a

### Passage 5

In A375 cells, which were screened previously with the GeCKO and Avana libraries2,16, the Brunello library showed greater depletion of sgRNAs targeting essential genes (AUC= 0.80), while sgRNAs targeting non-essential genes showed no evidence of depletion (AUC= 0.42; Fig. 1b). Conversely, non-targeting sgRNAs were among the least depleted (AUC= 0.16), evidence of the well-described cutting effect in CRISPRko screens, whereby dsDNA breaks lead to detectable effects on cell growth; this is magnified in extreme cases such as copy number amplified target sites or promiscuous sgRNAs16,22–24.

### Passage 6

Interestingly, one gene set, “Systemic Lupus Erythematosus,” was an outlier in this comparison. When we compared the performance of each individual gene in this set, we saw that numerous histone genes were essential when assessed by CRISPRko but not by CRISPRi in both A375 and HT29 cells (Fig. 4d; Supplementary Figure 4a; Supplementary Data 4). This observed difference between gene knockout and knockdown may represent a false positive with CRISPRko or a false negative with CRISPRi. A simple explanation is that regions containing histone clusters46 are copy number amplified and therefore show cutting toxicity with CRISPRko. However, neither region of chromosome 1 or 6 shows evidence of high copy number in A375 or HT29 cells (Fig. 4e; Supplementary Figure 4b). Additionally, several nonhistone genes near the histone clusters on chromosome 1 show comparable depletion with Brunello and Dolcetto in A375 cells (Fig. 4f), further suggesting that these regions are neither copy number amplified nor inaccessible to CRISPRi reagents.

### Passage 7

As with CRISPRi, sgRNA location is essential for effective gene upregulation. We again used FANTOM to annotate the TSS, but instead targeted a window that was 150–75 nucleotides upstream of the TSS, based on re-analysis of previous data18,40

### Passage 8

Unlike CRISPRko and CRISPRi, CRISPRa lacks an obvious gold standard gene set with which to assess screen performance and compare previously published screens (Supplementary Table 5). Therefore, to assess performance, we performed a vemurafenib-resistance screen similar to that previously executed

### Passage 9

To design the library, we first selected sgRNAs in this optimal window, and further ranked them by Rule Set 2, which is effective for CRISPRi sgRNAs16, and the number of off-target sites. In order to fulfill a quota of 6 sgRNAs per gene, we successively relaxed these three criteria (Supplementary Table 2). The resulting library, named Dolcetto, was divided into Sets A and B, with the former containing the top three selected sgRNAs. This library was cloned into a modified version of lentiGuide (pXPR_050); we opted to use tracr-v2 both because the limited window of CRISPRi activity may mitigate the risk of off-target effects and because previous CRISPRi studies have used a modified tracrRNA18,19.

### Passage 10

Upregulation of genes through CRISPRa likewise represents a complementary method for pooled screening that can reveal the function of lowly-expressed genes and pathways more effectively modulated by gene activation. When we compared CRISPRa and ORF screens for resistance to MEK inhibitors, we found that the technologies identified a number of common top hits, but also numerous unique ones; the large majority of these novel genes identified by CRISPRa validated in a secondary screen. Both technologies have sources of false negatives and positives that may explain these differential hits. Sources of false negatives for ORF technology include overexpression of an irrelevant splice isoform; for CRISPRa, false negatives may arise when the target gene is not effectively overexpressed, due to poor sgRNA design, inaccurate TSS annotation, or inaccessible chromatin environment. False positives can occur in ORF screens when an ORF is overexpressed to a level never achieved by the cell endogenously and, in CRISPRa screens, when multiple genes are upregulated at bidirectional promoters. Therefore, both ORF and CRISPRa screens are valuable and complementary elements of the pooled screening toolbox.
