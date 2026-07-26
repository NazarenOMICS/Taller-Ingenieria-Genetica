---
type: notebook-source
source_id: "603e6fcf-f685-4303-86f2-3da58fbaeb04"
notebook_id: "83c9725a-d105-4f75-a11c-dc0100661c7b"
slug: "q11-controles-experimentales"
vault_slug: "dcas9-fto-granulosa/q11-controles-experimentales"
project: "dcas9-fto-granulosa"
url: ""
source_type: web
status: active
date: 2026-07-14
pdf: "Research/Papers/dcas9-fto-granulosa/q11-controles-experimentales/josh_2019_mitigation_of_off_target_toxicity_in_crispr_cas9.pdf"
related:
  - "[[Notes/Dashboards/CRISPRa experimental controls]]"
used_in_qa: true
cited_in_count: 4
qa_notes:
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q01 - according-to-these-sources-what-non.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q03 - according-to-these-sources-what-role.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q04 - according-to-these-sources-e-g.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/QA/answers/2026-07-14 Q05 - according-to-these-sources-e-g.md]]"
---

# josh_2019_mitigation_of_off_target_toxicity_in_crispr_cas9.pdf

## PDF

![[Research/Papers/dcas9-fto-granulosa/q11-controles-experimentales/josh_2019_mitigation_of_off_target_toxicity_in_crispr_cas9.pdf]]

## Source Guide

## Cited Passages

### Passage 1

CTCF motif-targeting sgRNA library design. We selected CTCF motifs in loop anchors to target as follows. We started with 6057 loops present in K562 cells and focused on the 4,892 loop anchors that had previously annotated motifs overlapping ChIP-seq peaks30 for CTCF (using STORM69), such that the CTCF motifs were convergently oriented into the loop, which is suggested to be the correct orientation for loop formation. We further restricted to 4172 loop anchor CTCF motifs that could be targeted with with at least two sgRNAs per site, as defined by our guide filtering criteria below. Some of these CTCF motif targets were in exons of genes or near the BCR-ABL amplification, which could result in growth effects unrelated to CTCF binding, so they were treated separately during analysis, resulting in a final count of 4022 Type 0 CTCF loop anchor motifs. Finally, a set of control sgRNAs targeting safe regions was added. Briefly, safe-targeting negative control sgRNAs are highly filtered to target a non-functional genomic site and avoid having severe growth effects while controlling for the effect of inducing a double strand break27. An additional 310 CTCF and Rad21 sites (Types 1–5) were selected with alternative methods (Supplementary Materials and Methods) and also targeted with sgRNAs in the library, but these were filtered out during analysis and not included in Fig. 1 for the sake of clarity and because this small alternative set was similarly confounded by off-target activity and lacking hits. For sites that passed our filtering criteria, we selected a maximum of 5 sgRNAs per site. 95% of these sgRNAs overlapped a K562 CTCF ChIP-seq peak in our CTCF ChIP-seq data.

### Passage 2

Surprisingly, we find that low-specificity sgRNAs are the dominant confounding factor not only for active Cas9 screens but also for dCas9-mediated perturbations such as CRISPRi and CRISPRa. Cas9 generates double-strand breaks (DSB), so a large number of off-targets for a given sgRNA could result in a major fitness effect due to cellular toxicity as a result of activation of the DNA damage response and apoptosis23,25–27,53, regardless of the location of off-target sites. In contrast, dCas9-recruited epigenetic perturbations do not generate DSBs, and their off-target effects are expected to be location-dependent. Interestingly, these offtarget effects cannot be fully accounted for by dCas9 binding itself, as we tested the same sgRNAs with all four CRISPR-Cas9 platforms, and nearly all sgRNAs showed unmeasurable growth effects with dCas9 alone. Future studies of the mechanisms of CRISPRi/a off-target toxicity will improve our understanding of the cellular response to these perturbations and enable improved experimental designs. This is especially relevant for non-coding screens, which may be particularly vulnerable to confounding offtarget activity given the need to target small regions with few available sgRNAs. As an example of the impact that off-target effects can have, growth screens targeting CTCF sites in K562 cells returned only hits that on closer examination were confounded by off-target activity. None of the CTCF sites that we characterized in more detail in cell lines expressing sgRNAs had a measurable impact on gene expression or chromatin states in the genomic neighborhood (Supplementary Fig. 1). Dense-tiling of those motifs also did not find concordant evidence of CTCF site essentiality from multiple high-specificity sgRNAs, which further supports the conclusion that the hits were false positives. Although this is unexpected, it is potentially consistent with recent studies that reported acute global degradation of either all CTCF protein40 or all of the loop anchor cohesin component RAD21 in cells49 did not result in dramatic changes in gene expression. Individual CTCF site deletions at the boundaries of TADs containing developmental genes were recently reported to have no effect on nearby gene expression or developmental phenotypes in mouse embryos48,50. Therefore, our results appear consistent with other evidence that individual CTCF sites are dispensable for gene regulation in many contexts.

### Passage 3

N A

### Passage 4

In the full screen data, we observed a striking bias for low specificity scores among the sgRNAs that confer large fitness effects (p= 1.1e−31, Fisher’s exact test, Fig. 1e). Indeed, the majority (76%) of CTCF motif-targeting sgRNAs that have guidelevel log2(fold-change) ≤−2 also had GuideScan specificity scores ≤0.2 (on a scale of 0 to 1, where 0 indicates least specificity or greatest off-target activity), representing an 8.4-fold odds ratio. In the case of our CTCF screen, 4% of CTCF loop anchors had strong evidence of essentiality (Guide enrichment log2(foldchange) ≤−2) with a single sgRNA, but only 0.2% had such evidence from multiple sgRNAs (Fig. 1f). This disparity is unexpected given that the sgRNAs targeting the same site should have similar effects but is consistent with the sgRNAs having different off-target effects. After filtering for high-specificity sgRNAs with the GuideScan score, the number of CTCF loop anchors with evidence of essentiality from multiple sgRNAs dropped to zero (out of 2968 motifs targeted with multiple highspecificity sgRNAs). Together, these results experimentally validated the new GuideScan specificity score as an effective predictor of off-target activity and a more useful parameter for screen filtering than the absolute number of off-target sites or a previous aggregate specificity score.

### Passage 5

high-specificity and low-specificity sgRNAs had strong growth effects when targeting exons of essential genes but no effect in the neighboring introns (Fig. 2b), demonstrating that the dense-tiling screen can discern the short functionally relevant sequences of coding exons from background with high fidelity. Strikingly, the great majority (93%) of sgRNAs tiled within the 1 kb CTCF loop anchor regions that had a strong fitness effect were, again, lowspecificity guides with GuideScan scores ≤0.2 (p= 2.3e−233, Fisher’s exact test, Supplementary Fig. 3E). While the previous motif-targeting library only used 2–5 sgRNAs per motif, this dense-tiling library included all possible guides overlapping a window of +/−20 bp of the CTCF motif centers. Despite this increase in sgRNA density, after filtering with GuideScan scores, we still found zero CTCF motifs with evidence of essentiality from multiple high-specificity sgRNAs (Fig. 2c and Supplemen-tary Fig. 3F, G). We therefore concluded that the observed hits in the CTCF screens were consistent with off-target activity. This result suggests (but does not conclusively prove) that the CTCF loop anchors we tested in K562 are not essential for cell growth in normal conditions, which appears consistent with recent observations that degron-mediated depletion of loop anchor proteins can have minimal effects on transcription40,48–51. Notably, functional redundancy of CTCF sites or inefficient genome editing could also lead to false negatives. While we could not fully explain why no CTCF sites were convincing hits in these screens, we consistently found strong evidence that GuideScan scores reveal confounding off-target activity and set out to explore the utility of this approach on other non-coding CRISPR screens.

### Passage 6

Dense-tiling CTCF loop anchors with pooled Cas9 screens. To further test whether off-target activity could explain the hits from the CTCF motif screen, we designed a dense-tiling sgRNA library targeting 270 CTCF sites, including full tiling of each such site (all possible sgRNAs within 1 kb), using up to 400 sgRNAs per site (Fig. 2a). We chose CTCF sites from four categories: hits called by casTLE analysis before filtering with GuideScan scores, the Hi-C loop partners of these hits, non-hits, and the loop partners of the non-hits (see Methods section). We expected three possible results from densely tiling the loop anchors: (1) truly essential CTCF motifs would result in a strong peak of signal from highspecificity sgRNAs that generate indels near the motif (i.e., +/−20 bp), (2) regions that were essential for reasons distinct from the CTCF motif, such as being copy number amplified23,25,26,47, would result in uniformly strong growth effects from both low-specificity and high-specificity sgRNAs irrespective of whether the sgRNAs overlap the motifs, and (3) non-functional motifs would only have strong signal from lowspecificity sgRNAs, if any. This dense-tiling screen was performed at high coverage (~12,000 cells per sgRNA) and yielded highly reproducible guide effect measurements (r2= 0.92, Supplemen-tary Fig. 3A). As expected, positive control sgRNAs targeting ten essential genes were strongly depleted (Supplementary Fig. 3B). We observed uniform depletion of high-specificity and lowspecificity sgRNAs tiling regions near the BCR-ABL amplification but not elsewhere (Supplementary Fig. 3C, D), as expected. Both

### Passage 7

chr16: 84118062–84119082

### Passage 8

target site number, could be predicted by the recently developed GuideScan specificity score.

### Passage 9

To address this question, we performed a genome-wide noncoding screen for essential CTCF sites in chromatin loop anchors in the K562 leukemia cell line. We discovered that the dominant source of signal in our screen was not due to deregulated gene expression but was instead consistent with CRISPR-Cas9 offtarget activity causing reductions in cell fitness, despite filtering the sgRNAs to have no perfect or 1-mismatch off-target sites. We found that the recently developed GuideScan-aggregated Cutting Frequency Determination (CFD) specificity score accurately predicted sgRNAs with confounding off-target activity and outperformed a previous score, as well as the simple number of off-

### Passage 10

Discussion Here, we found that off-target activity confounds Cas9, CRISPRi, and CRISPRa screens for essential regulatory elements in K562 cells by conducting several screens using sgRNA libraries designed to edit motifs and tile regions of interest in an unbiased fashion. Notably, these sgRNAs had already been filtered to lack 0–1 mismatch off-target sites; i.e., this confounding activity was found in sgRNAs with only 2+ mismatch off-target sites, which may have passed previous design requirements. Importantly, use of GuideScan aggregate specificity scores to identify sgRNAs with only 2+ mismatch off-targets and their propensity to mediate Cas9 binding/cutting could resolve most of these issues. We present a strategy and software to use this score to filter screens for essential non-coding elements.

### Passage 11

Our findings have implications for the design and analysis of future screens. Given that (1) validation experiments of individual screen hits are time-intensive and low-throughput, and (2) there is a growing interest in global analyses of aggregated non-coding screen data, computational models for filtering out low-specificity sgRNAs are crucial to identify bona fide hits and to diagnose systemic problems before data aggregation. We find that offtarget effects on cell fitness are not predictable solely from the absolute number of off-target sites for these sgRNAs, although that simple metric is often used when designing and ranking sgRNAs. In contrast, we find that the data-driven GuideScan specificity score, which accounts for the position and type of mismatches to provide a weighted assessment of Cas9’s affinity

### Passage 12

We questioned whether these off-target growth effects were purely a function of the absolute number of off-target sites or specific to a subset of off-target sites. We and others have shown that, in the context of coding gene screens, the number of perfect matches or 1-mismatch off-targets correlates with growth phenotypes27,28. However, the analyses presented here do not include any sgRNAs with perfect genomic matches at any other place in the genome, nor sgRNAs with 1-mismatch off-targets. Across all four CRISPR-Cas9 platforms used in the tiling screens, the GuideScan score was predictive of off-target effects on cell fitness (Fig. 3c and Supplementary Fig. 6A), yet there was very weak correlation between growth effects and the absolute number of off-target sites (with 2 or 3 mismatches each), especially for CRISPRi/a (Supplementary Fig. 6B, C). Indeed, some outlier sgRNAs with thousands of off-target sites had no effects on growth. Thus, when designing and interpreting screens, the propensity to bind or cut as captured by the specificity score should be considered, rather than simply the number of off-target binding locations. These propensities are predicted for each off-target location by the CFD score44 as a weighted function of the mismatch number, position, and nucleotide identity, and then aggregated across all off-target locations into a GuideScan aggregate specificity score. Lastly, the optimal GuideScan score cutoff for filtering out false positives while retaining library density varies slightly but is approximately 0.2 for CRISPRi/a and Cas9 (Supplemen-tary Fig. 6D).

### Passage 13

Impact of low-specificity sgRNAs on non-coding screen design. Finally, we investigated the extent to which non-coding elements can be targeted with high-specificity sgRNA libraries. To address this question, we characterized the distribution of GuideScan specificity scores for a number of possible screen designs. We observed that our tiling screen and CTCF site screen libraries contained significantly more low-specificity sgRNAs than Bru-nello44, a genome-wide coding gene-targeting library (p < 0.0001, Mann–Whitney test, Fig. 4a), reflecting the inherently poorer specificity of sgRNA libraries that densely tile regions or target relatively small motifs. We then designed libraries targeting all candidate cis-regulatory elements (or ccREs) which were identified in the ENCODE SCREEN databases55,56. At the time of our analysis, the SCREEN databases contained 1.31 million individual ccREs, with a median length over 200 bp (Supplementary Fig. 10A). We specifically focused on CRISPRi/a epigenetic perturbation designs and imposed a minimum requirement of including at least 5 sgRNAs of sufficiently high specificity for each element (to enable robust statistical analyses of functional effects at the element level). We find that 89% of SCREEN cCREs can be targeted with ≥5 sgRNAs at a GuideScan cutoff of 0.2 (Supple-mentary Fig. 10B) although this varies by type of target element. For example, we find that 62% of human lncRNA TSS elements can be targeted with ≥5 CRISPRi sgRNAs with a specificity score >0.2, even when selecting sgRNAs from a conservative window of only +/−100 bp from the TSS (Fig. 4b). Overall, most ccREs can be targeted with epigenome editing tools even after filtering the sgRNAs that are most likely to be confounded by off-target effects.

### Passage 14

Maintain in cell culture

### Passage 15

RT-qPCR experiments. RNA from 100,000 K562 cells was extracted with RNA QuickExtract (Lucigen QER090150). RNA was treated with DNaseI from the same kit, reverse transcribed with AMV RT (Sigma 10109118001), and then cDNA were quantified in multiplex TaqMan qPCR reactions using commercially available probe sets (Thermo Fisher 4453320) and TaqMan FastAdvanced Master mix (Thermo Fisher 4444556). Three to four technical qPCR replicates were used for each biological replicate.

### Passage 16

−8

### Passage 17

To better understand the mechanistic basis for these fitness effects, we characterized the transcriptional and chromatin landscape of K562 cell lines carrying mutations induced by individual sgRNAs with validated growth effects. We chose hits where 2–3 sgRNAs targeting the same CTCF site had strong fitness effects and where changes in distal gene regulation could affect a gene that was essential in our previous Cas9 and CRISPRi/ a gene screens in K562. First, we sought to confirm that sgRNAs targeting CTCF sites can disrupt CTCF binding by performing CTCF ChIP-seq on Cas9-expressing cells transduced with individual sgRNAs. Indeed, Cas9-induced indels specifically eliminated CTCF binding at the targeted CTCF, while CTCF occupancy at untargeted sites in the immediate vicinity or elsewhere in the genome remained unchanged (Supplementary Fig. 1A, B). However, a case-by-case examination of each site revealed a more complex picture. For two sites, where either only a single CTCF motif was present or the central CTCF motif relative to the ChIP-seq peak was the target of the sgRNA, we observed complete elimination of CTCF binding as expected (Supplemen-tary Fig. 1c, right-hand side panels). In two other cases, multiple clustered CTCF motifs were present within the ChIP-seq peak; CRISPR-Cas9 perturbation specifically resulted in elimination of ChIP-seq signal over the targeted motif, as could be expected (middle panels). The last two cases (left-hand side panels) featured a site within a peak that is not strongly occupied in these K562 cells and a guide targeting a site nearby but outside the observed ChIP-seq peak, likely due to misannotation of the loop anchor motif. These last two examples naturally raised questions regarding the source of their reproducible fitness effects.

### Passage 18

To minimize off-target effects, we filtered out sgRNAs that had exact or 1-mismatch off-target instances within another CTCF site or inside exons of GENCODEv1970 genes, to avoid confounding activity from targeting multiple CTCF sites or knocking out genes. We also filtered out guides with >2 0-mismatch, >10 1-mismatch, >50 2-mismatch, or >200 3-mismatch genome-wide off-targets. We defined off-target matches by aligning the guides to the hg19 version of the human genome using BWA ‘aln’ with the flags -N -n 4 -o 0 -k 0 -l 771. However, the screen data presented in Fig. 1 and Supplementary Fig. 8 is further filtered more stringently to only display sgRNAs with no perfectly matching and no 1-mismatch off-target sites as defined by the GuideScan search algorithm. We also filtered out guides with too low (<20%) or too high (>80%) GC content and guides containing confounding oligonucleotides that might affect the expression of the guide or PCR steps, where confounding oligonucleotides are defined as those that either end in GGGGG, contain TTTT, or contain restriction cut sites (CTGCAG, GAAGAC, GTCTTC, CCANNNNNNTGG, GCTNAGC).
