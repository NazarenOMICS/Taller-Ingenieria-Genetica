---
type: notebook-source
source_id: "55afc9cb-d63a-4027-afaa-8adf5d7cd00a"
notebook_id: "b7d60267-6d14-41ad-b7b7-5b606bb8ab2a"
slug: "q07-metodos-m6a-fos-3utr"
vault_slug: "dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr"
project: "dcas9-fto-granulosa"
url: ""
source_type: web
status: active
date: 2026-07-14
pdf: "Research/Papers/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/lijuan_2021_a_neural_m6a_ythdf_pathway_is_required_for.pdf"
related:
  - "[[Notes/Dashboards/m6A methods FOS 3-UTR]]"
used_in_qa: true
cited_in_count: 4
qa_notes:
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/QA/answers/2026-07-14 Q01 - according-to-these-sources-how-does.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/QA/answers/2026-07-14 Q03 - according-to-these-sources-how-does.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/QA/answers/2026-07-14 Q04 - according-to-these-sources-how-do.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/QA/answers/2026-07-14 Q05 - what-known-limitations-biases-or-artifacts.md]]"
---

# lijuan_2021_a_neural_m6a_ythdf_pathway_is_required_for.pdf

## PDF

![[Research/Papers/dcas9-fto-granulosa/q07-metodos-m6a-fos-3utr/lijuan_2021_a_neural_m6a_ythdf_pathway_is_required_for.pdf]]

## Source Guide

## Cited Passages

### Passage 1

For m6A-RIP-qPCR, the mRNAs were immunoprecipitated using α-m6A according to the procedure shown above. The IP-mRNAs were then reverse transcribed and amplified following the same protocol. The enrichment of m6A was quantified using qPCR as reported. The sequences of qPCR primers are listed in Supplementary Dataset 6.

### Passage 2

We examined this more closely by directly examining the behavior of m6A targets. We reasoned that targets with systematically higher levels of methylation—that is, genes with increasing proportions of methylated transcripts—would be more sensitive to loss of the m6A pathway. However, while our miCLIP libraries provide Mettl3-dependent peaks and single nucleotide resolution mapping of m6A sites in the transcriptome, it is not possible to infer overall methylation levels. A solution to this limitation, grouping targets by number of sites/ peaks, has been adopted by others31,68 and proposes that targets with increasing numbers of peaks/sites may have more individual transcripts with at least one m6A modification. Therefore, we binned genes by numbers of Mettl3-dependent m6A peaks.

### Passage 3

m6A individual-nucleotide-resolution cross-linking and immunoprecipitation (miCLIP). miCLIP libraries were prepared by subjecting RNA samples to the established protocol66 with the minor changes described below. Briefly, total RNA was collected from <1-week-old w1118 (wild type) and Mettl3[null] (mutant) female heads using TRIzol RNA extraction. Poly(A)+ RNA was enriched using two rounds of selection. RNAs were fragmented, incubated with α-m6A (202 003 Synaptic Systems) and crosslinked twice in a Stratalinker 2400 (Stratagene) using 150 mJ/cm2. Crosslinked RNAs were immunoprecipitated using Protein A/G magnetic beads (Thermo) and washed under high salt conditions to reduce nonspecific binding. Samples were radiolabeled with T4 PNK (NEB), ligated to a 3′ adaptor using T4 RNA Ligase I (NEB), and purified using SDS–polyacrylamide gel electrophoresis (SDS–PAGE) and nitrocellulose membrane transfer. RNA fragments containing crosslinked antibody peptides were recovered from the membrane using proteinase K (Invitrogen) digestion.

### Passage 4

We examined C-to-T crosslinking-induced mutations following adenosine residues (CIMs), which have been taken to represent individual m6A site in miCLIP data61,66. In particular,

### Passage 5

Mutations were called using the CIMS software package100. To identify putative m6A sites, C-to-T transitions with preceding A nucleotides were extracted and filtered such that the number of mutations that support the mismatch (m) > 1 and 0.01 <m/k < 0.5, where k is the number of unique tags that span the mismatch position.

### Passage 6

Recovered fragments were subjected to library preparation. First-strand cDNA synthesis was performed using SuperScript III (Life Technologies) and iCLIPbarcoded primers, which contain complementarity to the 3′ adaptor on the RNA. cDNAs were purified using denaturing PAGE purification, circularized using CircLigase II (EpiCentre), annealed to the iCLIP Cut Oligo, and digested using

### Passage 7

For input libraries, poly(A)+ RNAs were fragmented and directly subjected to radiolabelling and 3′ adaptor ligation. All subsequent steps are as listed above. Libraries were paired-end sequenced on an Illumina HiSeq2500 instrument at the New York Genome Center (NYGC).

### Passage 8

autonomous requirements of m6A writers working via Ythdf, but not Ythdc1. Furthermore,

### Passage 9

Using Mettl3-KO cells, we performed RNA decay assays of validated m6A targets and control transcripts. Following inhibition of transcription using actinomycin D, we observed a range of transcript levels across different loci, but none of these were significantly different between wild-type and m6A-deficient cells (Fig. 6F). Overall, our analyses using S2 cells and intact nervous system indicate that mRNA stability of m6A-containing transcripts is neither substantially nor directionally influenced by loss of m6A in Drosophila, in contrast to m6A in mammals.

### Passage 10

−4 −2 0 2 4 log2Fold Change

### Passage 11

ptc-gal4; UAS-HA-YTHDF / tub-GFP GFP DsRed Merge

### Passage 12

Mapping the Mettl3-dependent m6A methylome in Drosophila. To link these brain-function defects to the underlying molecular landscape of RNA methylation, we sequenced m6A sites from polyadenylated transcripts using miCLIP61. Although we previously reported miCLIP datasets from Drosophila embryos55, we recognized that there can be background association in such data. Thus, individual sequencing “peaks” need to be interpreted cautiously. To provide a stringent basis to infer the existence of m6A at given sites, we analyzed companion input and miCLIP libraries from dissected heads, which are highly enriched for neurons, comparing wild-type and deletion mutants of Mettl3, which encodes the catalytic methyltransferase subunit essential for mRNA modification (e.g. Fig. 1 and Supplementary Dataset 2).

### Passage 13

The miCLIP libraries from Mettl3 mutants proved especially valuable, because they allowed us to distinguish m6A-IP loci that were clearly genetically dependent on endogenous Mettl3 (Fig. 4A, Supplementary Fig. 8a). Reciprocally, numerous regions of the transcriptome were significantly enriched in miCLIP libraries compared to input, but whose signals persisted in Mettl3 mutants (Fig. 4B, Supplementary Fig. 8b). These might conceivably represent transcript regions modified by another factor62, but cannot at this point be easily distinguished from non-specific pulldown. In general, the Mettl3-independent peaks were globally present in weaker m6A peaks (Fig. 4C), suggesting they are functionally less relevant. Therefore, we applied stringent filtering to focus our attention on the rich set of clearly Mettl3-dependent peaks (Fig. 4A–C). In addition, as we employed strong selection for polyadenylated transcripts for input, we prioritized studies of annotated genes. Altogether, our analyses (see the “Methods” section) yielded 3874 Mettl3-dependent peaks from 1635 genes. Since a subset of these called regions contained clear local minima, we applied PeakSplitter63 to arrive at 4686 head m6A peaks (Supplementary Dataset 3).
