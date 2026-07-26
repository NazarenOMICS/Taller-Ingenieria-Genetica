---
type: notebook-source
source_id: "2a1205a7-6c05-4025-9895-e23756488c3d"
notebook_id: "dc4c4ee0-31fa-4a55-bf26-101bc3f90e8e"
slug: "q05-fto-m6a-edad"
vault_slug: "dcas9-fto-granulosa/q05-fto-m6a-edad"
project: "dcas9-fto-granulosa"
url: ""
source_type: web
status: active
date: 2026-07-14
pdf: "Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf"
related:
  - "[[Notes/Dashboards/FTO m6A vs age ovary]]"
used_in_qa: true
cited_in_count: 3
qa_notes:
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/QA/answers/2026-07-14 Q03 - what-techniques-do-these-sources-describe.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/QA/answers/2026-07-14 Q04 - what-known-limitations-or-technical-artifacts.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q05-fto-m6a-edad/QA/answers/2026-07-14 Q06 - what-gaps-remain-these-sources-regarding.md]]"
---

# alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf

## PDF

![[Research/Papers/dcas9-fto-granulosa/q05-fto-m6a-edad/alexa_2020_limits_in_the_detection_of_m6a_changes_using.pdf]]

## Source Guide

## Cited Passages

### Passage 1

The first and most widely-used method to enable transcriptome-wide studies of m6A, MeRIP-seq or m6A-seq, involves the immunoprecipitation of m6A-modified RNA fragments followed by peak detection through comparison to background gene coverage16,17. A second method was developed in 2015, miCLIP or m6A-CLIP, which involves crosslinking at the site of antibody binding to induce mutations during reverse transcription for single-nucleotide detection of methylated bases2,18. MeRIP-seq is still more often used than miCLIP, despite less precise localization of m6A to peak regions of approximately 50–200 base pairs that can contain multiple DRAC motifs, since it follows a simpler protocol, requires less starting material, and generally produces higher coverage of more transcripts. Antibodies for m6A can also detect a second base modification, N6,2′-O-dimethyladenosine (m6Am), found at a lower abundance than m6A and located at the 5′ ends of select transcripts15,18. We thus refer to the base modifications detected through MeRIP-seq collectively as m6A(m), although most are likely m6A. As of late 2018, over fifty studies used MeRIP-seq to detect m6A(m) in mammalian mRNA (Supplementary Table 1).

### Passage 2

We next analyzed the overlap of peaks among studies and found inconsistency in peak localization on transcripts as well. Within four commonly used cell types, the percent of peaks detected in one experiment that were also detected in a second varied among pairs of studies from as low as 2% of peaks to as high as 90% (median = 45%), after filtering for transcripts expressed above a mean of 10X input coverage in both to ensure sufficient expression for peak detection (Fig. 2a). In fact, peaks showed higher overlap within different cell types from the same study than within the same cell type from different studies, suggesting that MeRIP-seq data is prone to strong batch effects (Fig. 2b). While this could be due to differences among experimental protocols used (summarized in Supplementary Table 2), we were unable to identify such a link. Overall, most percent overlaps of m6A(m) peaks fell between ~30% (1st quartile) and ~60% (3rd quartile) (Fig. 2b). With rare exceptions (e.g. that described by Ke et al., 2017 in their Supplementary Fig. 8)3, most MeRIP-seq data sets do show enrichment of the m6A motif DRAC. These results indicate, however, that multiple labs running MeRIP-seq on the same cell type will detect different subsets of m6A(m) sites. Possible contributing factors in the differences among studies include cell state (e.g. different stages of the cell cycle), experimental conditions, and sequencing depth. Despite predictions that tissue or cell type would be a large factor in differences among samples, though, peaks detected in different tissues analyzed in a single experiment showed high overlap and little clustering by tissue type (Fig. 2c)54. This suggests that although there is evidence that m6A levels vary by tissue19, modified sites are consistent.

### Passage 3

Although MeRIP-seq can reveal approximate sites of m6A(m), it cannot be used to quantitatively measure the fraction of transcript copies that are methylated19. Studies of m6A variation in response to stimuli instead estimate differences at individual loci through changes in peak presence or peak height. Using these approaches, studies

### Passage 4

The extent to which m6A changes on particular transcripts and whether it changes in binary presence/ absence or in degree is unclear. MeRIP-RT-qPCR could detect methylation differences in in vitro transcribed RNA. Further, we found that these changes correlated with differences in MeRIP-seq enrichment. However, neither MeRIP-seq nor MeRIP-RT-qPCR can reveal the precise fraction of transcript copies modified by m6A. In general, antibody-based methods are subject to biases, including from differences in binding efficiencies based on RNA structure and motif preferences81. There is an oft-cited but little-used method for quantification of m6A, site-specific cleavage and radioactive-labeling followed by ligation-assisted extraction and thin-layer chromatography (SCARLET)19. However, this method can be challenging, works only for highly abundant

### Passage 5

(2015). 19. Liu, N. et al. Probing N6-methyladenosine RNA modification status at single nucleotide resolution in mRNA and long noncoding

### Passage 6

Disparities between experiments were not simply due to significance thresholding or differences in peak detection. Taking the union of peaks called in two experiments for KSHV, HIV, and dsDNA treatment, we found minimal to negative correlations in changes in m6A enrichment induced by treatment at the same sites, further showing that changes with similar treatments are not reproducible (Supplementary Fig. 7e).

### Passage 7

To re-evaluate the evidence for m6A(m) changes under various conditions, we first examined the variability in m6A(m) detection across replicates, cell lines, and experiments using our own negative controls (12 replicates) as well as 24 published MeRIP-seq data sets. We then compared statistical methods to detect differences in IP enrichment using biological negative and positive controls for m6A changes. We found that these methods are limited by noise, including biological variability from changes in RNA expression and technical variability from immunoprecipitation and sequencing that limits reproducibility across studies. Our results suggest that the scale of statistically detectable m6A(m) changes in response to various stimuli is orders of magnitude lower than the scale of changes reported in many studies. However, we also found that statistical detection could miss the majority of changed sites when using only 2–3 replicates. We use our results to propose approaches to MeRIP-seq experimental design and analysis to improve reproducibility and more accurately measure differential regulation of m6A(m) in response to stimuli. These data and analyses emphasize the need for further research and alternative assays, for example recently developed endoribonuclease-based sequencing methods44,45 or direct RNA nanopore sequencing46, to resolve the extent to which m6A changes in response to specific conditions.

### Passage 8

0 20 40 60 80 100

### Passage 9

For m6A(m) peak detection, a transcript must be sufficiently expressed for enrichment by the m6A(m) antibody and for adequate sequencing coverage in both the IP and input fractions. Previous reports have suggested that m6A(m) presence does not decrease with lower mRNA expression level, and, if anything, is higher in mRNAs with lower expression as methylated transcripts tend to be less stable9,38. Peak callers, however, identify fewer peaks in genes at low expression, which we therefore assume reflects inadequate coverage for peak calling. To estimate the level of coverage necessary for peak detection, we analyzed the percent of genes with at least one, two, or three peaks relative to mean input transcript coverage in both the mouse cortex and Huh7 cell data (Fig. 1a). Based on the upper shoulders of the sigmoidal curves as the percent of genes with peaks begins to plateau, we estimate that mean gene coverage of approximately 10–50X is necessary to avoid missing peaks based on insufficient coverage. Including a wider array of samples in this analysis likewise showed an increase in the percent of transcripts with ≥1 peak as coverage rose to 10×(Supplementary Fig. 1c). Our analysis of the input RNA-seq coverage of peak regions alone again supported a similar threshold; few peaks are detected with median input read counts below 10 across replicates (Supplementary Fig. 1d). These thresholds do not mean that peaks in genes with mean coverage <10X or peaks with fewer than 10 input reads are false positives, but that the likelihood of false negatives rises with lower coverage (Supplementary Fig. 1e).

### Passage 10

Figure 1. Thresholds for peak detection. (a) m6A(m) site detection in MeRIP-seq data from mouse cortex (left) and human liver cells (Huh7, right) shows saturation of peak detection as transcript coverage approaches 10–50X for replicates at basal conditions, with peaks merged from all replicates. (b) The total number of peaks captured increases with more replicates, with single replicates capturing a median of 66–78% of total peaks depending on study. Boxes span the 1st to 3rd quartiles of distributions for random subsamples of replicates, with lines indicating the median number of peaks, and whiskers showing the minimum and maximum points within ±1.5x the interquartile distance from the boxes. Jittered points show results for each random subsample (a total of 6 subsamples per replicate number for the mouse cortex data and 12 for the Huh7 data). (c) The percent of peaks detected in at least r replicates for the same data sets.

### Passage 11

To ensure significant peak changes detected by each of the tools reflected changes in IP enrichment independent of differential gene expression, we measured the correlation between changes in IP read counts at peak sites and changes in input read counts across their encompassing genes. For significant peaks (FDR-adjusted p-value <0.05) from the positive controls, correlation between log2 fold change in peak IP and gene input read counts was low for the GLMs and QNB (Pearson’s R = 0.10 to 0.22) but reached 0.55 (p = 5.8E-87) for MeTDiff (Fig. 3c). The higher correlation for MeTDiff was driven by peaks with proportional changes in IP and input levels, which suggests that MeTDiff often detects differential expression of methylated genes rather than differential methylation. Therefore, published studies that have used MeTDiff may actually be detecting differential expression and not differential methylation22,65. Indeed, plotting coverage for genes reported as differentially methylated in one of these studies, with the y-axis scaled separately per condition, confirmed that changes in m6A identified by MeTDiff were proportional to changes in gene expression (Fig. 3d)22. Given these results, QNB or the GLM implementations are better methods than MeTDiff to detect differential methylation. Taking the intersect of significant peaks for the GLMs and QNB may help determine the most probable sites of m6A changes, while taking the union of predictions provides a less conservative approach to selecting sites for further validation (Fig. 3e). However, additional filters are needed for robust peak change detection as there were still significant peaks for which the difference between peak log2 fold change and gene log2 fold change was close to zero, particularly with QNB (Supplementary Fig. 6e). For microarray and RNA-seq data, a filter of absolute log2 fold change >1 has been recommended to reduce false positive rates66; in the remainder of our analyses, we implemented a similar filter for absolute difference in peak and gene log2 fold change ≥1 to the combined predictions from QNB and the two GLMs, with an additional filter where noted for peak read counts ≥10 across all replicates and conditions to ensure sufficient coverage for consistent peak detection (as discussed in Fig. 1a).

### Passage 12

Detection of changes in peaks between conditions. Following m6A(m) peak detection, many studies compare the expression of peaks between two conditions to predict peak changes. While looking at plots of IP and input gene coverage under different conditions can help evaluate the evidence for these changes33, statistical

### Passage 13

Disparities in the methods used to detect changes in m6A(m) peaks also play a role in differing conclusions among studies. Here, we analyzed four statistical methods to detect changes in peaks and found that three of these methods showed uniform or conservatively shifted p-value distributions and were able to identify changes in m6A(m) independent of changes in gene expression. We therefore suggest that these statistical methods, in combination with filters for input levels in both conditions and the difference in log2 fold change between peaks and genes, can be used to identify candidate m6A(m) sites from MeRIP-seq data for further analysis and validation (Fig. 6). Based on our results, while MeTDiff works for peak detection, we do not recommend MeTDiff for peak change detection as it does not control well for differences in gene expression (Fig. 3). Similar to others33, we found that plotting predicted m6A changes was invaluable and that appropriate scaling for gene coverage could reveal changes proportional to gene expression. In addition, plotting the standard deviation in transcript coverage can help assess typical variation in peak height among replicates. We note that both differential methylation of a gene and methylation of a gene that is differentially expressed could be important, but they should not be conflated when considering the role of m6A in transcript regulation.

### Passage 14

open

### Passage 15

We next used our peaks validated with MeRIP-RT-qPCR to estimate the number of replicates necessary for detection of changes with either the GLM or QNB methods. Using a permutation test, we downsampled infected and uninfected replicates and reran statistical detection of changes. We found that approximately 6–9 replicates

### Passage 16

Figure 5. MeRIP-RT-qPCR validation and replicates necessary for the detection of peak changes. (a) Relative enrichment of the indicated amounts of an in vitro transcribed standard containing unmodified A or m6A, as measured by MeRIP-RT-qPCR. Data are shown for two independent replicates of three technical replicates each as IP enrichment over input relative to pulldown of a positive control spike-in, with the 0.1 fmol (0.01 m6A: 0.09 A) sample normalized to 1. Bars represent mean ± SEM of two independent replicates. ***p ≤ 0.005 by unpaired Student’s t-test. b-d) Linear regression of relative m6A enrichment from (a). Points and error bars mark mean ± SEM of two independent replicates. (c) Change in MeRIP-RT-qPCR vs. MeRIP-seq enrichment for peaks detected as significantly differentially expressed with infection of Huh7 cells by dengue virus, Zika virus, and hepatitis C virus. (d) Number of replicates of infected vs. uninfected cells needed to detect the peaks in (c). Replicates were randomly subsampled 10 times to calculate the fraction of subsamples in which peaks were called as significant by the GLMs or QNB. Boxes span the 1st to 3rd quartiles, with medians indicated. Whiskers show the minimum and maximum points within ±1.5x the interquartile distance from the boxes. Results for each subsample of replicates are shown as jittered points.
