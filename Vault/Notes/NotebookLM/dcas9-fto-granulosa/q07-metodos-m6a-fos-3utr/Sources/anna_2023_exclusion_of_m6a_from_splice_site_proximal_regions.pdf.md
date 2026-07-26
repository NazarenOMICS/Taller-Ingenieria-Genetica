---
type: notebook-source
source_id: "047ce909-242c-4805-98c4-719783fe6c50"
notebook_id: "b7d60267-6d14-41ad-b7b7-5b606bb8ab2a"
slug: "q07-metodos-m6a-fos-3utr"
vault_slug: "dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr"
project: "dcas9-fto-granulosa"
url: ""
source_type: web
status: active
date: 2026-07-14
pdf: "Research/Papers/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/anna_2023_exclusion_of_m6a_from_splice_site_proximal_regions.pdf"
related:
  - "[[Notes/Dashboards/m6A methods FOS 3-UTR]]"
used_in_qa: true
cited_in_count: 4
qa_notes:
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/QA/answers/2026-07-14 Q01 - according-to-these-sources-how-does.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/QA/answers/2026-07-14 Q04 - according-to-these-sources-how-do.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/QA/answers/2026-07-14 Q05 - what-known-limitations-biases-or-artifacts.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/QA/answers/2026-07-14 Q06 - what-gaps-remain-these-sources-regarding.md]]"
---

# anna_2023_exclusion_of_m6a_from_splice_site_proximal_regions.pdf

## PDF

![[Research/Papers/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/anna_2023_exclusion_of_m6a_from_splice_site_proximal_regions.pdf]]

## Source Guide

## Cited Passages

### Passage 1

7

### Passage 2

* -Corresponding authors:

### Passage 3

1

### Passage 4

Transcriptome-wide m6A topologies are predictably driven via exclusion from splice junctions

### Passage 5

Implementation of m6Apred-1 and m6Apred-2 models Gene models for roughly 20,000 ‘canonical’ human and mouse genes were downloaded from the ‘UCSC Known Genes’ annotation table in the UCSC genome browser. For each gene we identified all ‘eligible’ DRACH motifs, and furthermore recorded their distance from the nearest exon-intron junction. In m6Apred-1, each of the motifs was considered methylated. In m6Apred-2, an eligible DRACH motif was only considered methylated if its distance to the nearest splice junction exceeded 100 nt. With the exception of analyses in Fig. S5C, also motifs within 100 nt from the transcript start or end site were considered non-eligible by m6Apred-2, based on the finding that m6A is also depleted in the vicinity of polyadenylation sites. To mimic the regional enrichment in m6A-seq, every site predicted to undergo methylation was modeled as a gaussian over a 200 bp region centered at the methylated site. The values along this gaussian were derived using the density function of a gaussian distribution (mean=0, sd=4), which were calculated for 100 values distributed at fixed intervals between 0 and 9 using the dnorm() function in R, and min-max normalized, to distribute between 0 and 1. The final predicted enrichment value at each position along the gene was defined as the sum of all signals (stemming from zero, one or potentially multiple gaussians) overlapping this position (see Supplementary code).

### Passage 6

To evaluate the performance of this model, we assessed its ability to capture m6A features at three different resolutions: individual m6a sites, m6A levels within and between genes, and meta-gene features. To validate the ability of m6Apred-2 to accurately detect individual m6A sites, we sought to investigate what fraction of the predicted sites could be confirmed on the basis of experimental data. We compiled an assembly of high-confidence m6A sites detected via distinct experimental single-nucleotide resolution methods (miCLIP 35, SAC-seq 39, miCLIP2 40, DART-seq 37 and GLORI 41). We then assessed the overlap between the predicted methylation status and the experimental measurements across 7,268 genes that had been pre-filtered based on expression-levels. While all sets of measurements provided substantial support to predictions by our model (Fig. 3D), the most compelling results were observed via the recently established GLORI approach, which experimentally validates ~62% of all sites that we predict to undergo methylation, whereas only 6.3% of sites that we predict not to undergo methylation are experimentally supported by the GLORI dataset. Combining all datasets, 71% of the predicted methylated sites were experimentally validated, in comparison to 12% of the predicted negative ones (Fig. 3D), lending considerable support to the predictive power of m6Apred-2.

### Passage 7

To explore the possibility of an inhibitive effect of introns on methylation, we examined the distribution of 81,518 methylation sites, identified in human cells at single-nucleotide resolution by six m6A-miCLIP experiments 35, with respect to the intron-exon junction. Remarkably, we found m6A depleted from both the 5’ and 3’ ends of long internal exons, as well as from the 5’ of last exons, plateauing at a distance of ~200 nt from splice junctions (Fig. 2D, S2A-D). The size of this ‘m6A exclusion zone’ was fixed, and did not depend on the length of the internal exon (Fig. 2D, S2B). Similar results were obtained on the basis of 25,879 m6A sites identified via
