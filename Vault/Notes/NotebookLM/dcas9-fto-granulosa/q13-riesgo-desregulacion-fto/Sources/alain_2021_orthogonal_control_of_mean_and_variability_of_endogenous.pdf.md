---
type: notebook-source
source_id: "e3fe646a-251a-4beb-b9b4-907461ed1eef"
notebook_id: "ef0da090-9b28-43a3-9dd4-5889790ce012"
slug: "q13-riesgo-desregulacion-fto"
vault_slug: "dcas9-fto-granulosa/q13-riesgo-desregulacion-fto"
project: "dcas9-fto-granulosa"
url: ""
source_type: web
status: active
date: 2026-07-14
pdf: "Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf"
related:
  - "[[Notes/Dashboards/FTO dysregulation risk]]"
used_in_qa: true
cited_in_count: 3
qa_notes:
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/QA/answers/2026-07-14 Q03 - according-to-these-sources-e-g.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/QA/answers/2026-07-14 Q05 - what-experimental-or-design-strategies-do.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/QA/answers/2026-07-14 Q06 - what-gaps-remain-these-sources-regarding.md]]"
---

# alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf

## PDF

![[Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf]]

## Source Guide

## Cited Passages

### Passage 1

expression and heterogeneity of transgenes and endogenous human genes. The circuit, a

### Passage 2

looked to an earlier synthetic circuit that utilized a serial orientation of independent inducible transcription factors to decouple mean expression from variability34.

### Passage 3

Results Characterization of a serial circuit topology with two inducible transcriptional activators. We built TuNR as a serial connection of two inducible transcriptional activation systems, where the upstream system (first node) controls production of the downstream system (second node) (Fig. 1A and Supplementary Fig. 1A). The first node consists of a Gal4 DNA-binding domain fused to half of a split abscisic acid (ABA)-binding domain, which, in the presence of ABA, assembles with its cognate heterodimer fused to a VP-16 activation domain35,36. The recruitment of the ABA-reconstituted gene product of the first node to the upstream activating sequence minimal promoter drives the expression of the second inducible system and an mRuby as a reporter for transcription at this node of the cascade. The second node consists of a Staphylococcus pyogenes nuclease-dead Cas9 (dCas9) N-terminally fused to half of a gibberellic acid (GA)-binding domain and a VPR (p65, VP65, Rta) activation domain appended to the other half of the GA binding domain. In the presence of GA, these two proteins dimerize and, upon the concomitant expression of a target guide RNA (gRNA), are able to induce expression of the gene of interest (Fig. 1A). We identified ABA and GA as small molecule inducers of choice due to their previous vetting in other mammalian systems, reversibility of cognate protein dimerization, and the independence of each heterodimerization event35–37. Moreover, we chose dCas9 as the final node of TuNR for its modularity in targeting any locus with an appropriate protospacer adjacent motif.

### Passage 4

Inducible gene expression systems both in microorganisms38–40

### Passage 5

To quantify the total noise for every combination of ABA and GA, we utilized a common noise decomposition strategy to ascertain the extrinsic and intrinsic contributions to the expression noise as shown previously8. In this analysis, the correlated expression between the two terminal fluorophores represents the extrinsic noise, or cell-to-cell variability, whereas the uncorrelated

### Passage 6

produce cellular populations with distinct means and variances in a manner consistent with transgene regulation.

### Passage 7

TuNR achieved 7.2-fold mean induction for NGFR and 3.4-fold induction for CXCR4 and (Fig. 3C, D), which are levels comparable to what other systems have achieved with CRISPRa47,48. In addition, as observed in modulating mAzami-Green, TuNR showed a negligible effect on basal levels of NGFR and CXCR4 (Fig. 3C, D), demonstrating that TuNR minimally perturbs basal gene expression due to its serial topology.

### Passage 8

We believe the main contribution of TuNR is in its ability to be a multifaceted tool towards precise gene regulation. Although the induction capabilities of TuNR and other comparable CRISPRa-based systems in activating endogenous gene expression is modest relative to transgenes, we believe that the precise regulation of the distribution of gene expression even within this limited range will be of tremendous value in future investigations. This is largely because the range of noise titration achieved by TuNR seems to be comparable to that of endogenous human promoters48,49. Furthermore, the innovation presented by TuNR takes a particular significance given recent findings that suggest that bacteria such as Bacillus subtilis have evolved to rarely be capable of independently controlling gene expression mean from variability, leading to a suggestion that similar limitations may exist in mammals50. Therefore, a tool such as TuNR that can achieve this decoupling of gene expression and variance presents an opportunity to investigate the costs or opportunities presented by the fact that variability of gene promoters might be inextricably chained to a given level of noise, or vice versa.

### Passage 9

upon addition of ABA, consistent with earlier experiments, suggesting that leakiness emerges from the accumulation of the first node activator (Supplementary Fig. 2B, first column). When both small molecules are present, TuNR induces expression more than either small molecule alone, reaching a maximum mAzami-Green expression of ~1000-fold when both inducers are at their highest concentration. Notably, a transcriptional activator circuit mediated by GA (rows of Supplementary Fig. 2B) achieves ~100-fold induction. As the concentration of ABA increases, so does the basal expression. This reflects a tradeoff between maximum expression and basal leakiness (Fig. 1D). The serial arrangement of the transcriptional activators attenuates this basal leakiness, while achieving a superior maximum fold-change induction when compared to a single-node circuit.

### Passage 10

However, despite the versatility of TuNR, it is likely to be that our ability to achieve relatively small fold changes for endogenous genes as compared to transgenes is related to a lack of clear understanding of enhancer–promoter mechanisms and corrective cellular mechanisms that counteract the action of the synthetic circuit. Understanding these effects will enable synthetic circuits to more robustly drive endogenous gene production. Tentatively, some of the induction discrepancy between endogeneous and transgenes can be bridged by modifying the terminal effector domain with a Sun-tag system, which has demonstrated robust endogenous induction capabilities48. Alternatively, using the current iteration of TuNR, one could introduce the complementary DNA of a gene of interest under a synthetic promoter (e.g., pTRE) to test whether the induction capabilities recapitulate that of the fluorescent reporters.
