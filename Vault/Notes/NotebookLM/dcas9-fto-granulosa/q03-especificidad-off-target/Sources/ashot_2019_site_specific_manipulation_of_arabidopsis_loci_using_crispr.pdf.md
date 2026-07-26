---
type: notebook-source
source_id: "7d198aa7-8478-48b2-b4bf-d99c9d85f7fe"
notebook_id: "e1baac88-0719-426f-b47a-b620d48b6489"
slug: "q03-especificidad-off-target"
vault_slug: "dcas9-fto-granulosa/q03-especificidad-off-target"
project: "dcas9-fto-granulosa"
url: ""
source_type: web
status: active
date: 2026-07-14
pdf: "Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/ashot_2019_site_specific_manipulation_of_arabidopsis_loci_using_crispr.pdf"
related:
  - "[[Notes/Dashboards/dCas9-p300 off-target specificity]]"
used_in_qa: true
cited_in_count: 2
qa_notes:
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/QA/answers/2026-07-24 Q02 - what-guide-rna-mismatch-tolerance-or.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/QA/answers/2026-07-24 Q03 - what-genome-wide-profiling-methods-e.md]]"
---

# ashot_2019_site_specific_manipulation_of_arabidopsis_loci_using_crispr.pdf

## PDF

![[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/ashot_2019_site_specific_manipulation_of_arabidopsis_loci_using_crispr.pdf]]

## Source Guide

## Cited Passages

### Passage 1

To comprehensively profile the specificity of SunTag VP64-mediated activation, we examined differentially expressed genes (DEGs) in the gRNA4 RNA-seq dataset. All three profiled lines displayed highly specific activation of FWA with very few DEGs compared to a no guide control line (Supplementary Fig. 3a). To examine dCas9 binding at the FWA promoter, we performed ChIP-qPCR with T2 gRNA4 plants. We observed a strong enrichment of dCas9 at the FWA promoter compared to the control ACT7 locus, and as expected, no enrichment in Col-0 control plants (Supplementary Fig. 3b). ChIP-seq showed highly specific binding of dCas9 to the FWA promoter, with only one major off-target site (Supplementary Fig. 3c). This off-target site contains a PAM and 14 base pairs complementary to the gRNA sequence, spanning the previously reported seed region of the protospacer26. Therefore, SunTag VP64-mediated gene activation is highly specific due to the highly specific binding properties of the Cas9/gRNA complex.

### Passage 2

To test whether this system activates gene expression, we targeted the DNA methylated and silent FWA gene in Arabidopsis wild-type (Col-0) plants25. We observed ectopic activation of FWA in numerous T1 lines containing a single guide RNA (gRNA4) that targets FWA, but not in control lines that lack a guide (nog) or that lack VP64 (Supplementary Fig. 2a, b). Strong activation of FWA was also observed in the next generation T2 plants (Supplementary Fig. 2b,c). RNA-seq of T2 gRNA4 plants confirmed that FWA was robustly upregulated (Fig. 1a and Supplementary Fig. 2d). In addition to gRNA4, we tested a guide (gRNA17) that targets a region further upstream in the promoter, ~170 base pairs upstream from gRNA4. We detected FWA upregulation with gRNA17, although to a lesser extent than with gRNA4, suggesting that gRNAs placed near the transcription start site may be more effective to manipulate gene expression, as previously suggested with the SunTag system in mammalian cell lines16 (Supplementary Fig. 2e).

### Passage 3

Next, we examined genome-wide effects by RNA-seq. The two gRNAs targeting the 5′ end of EVD had perfect matches to two different ATCOPIA93 loci, one in euchromatin corresponding to the EVD locus, and another in heterochromatin corresponding to the Attrapé (ATR) locus. Both loci were highly activated, indicating that SunTag VP64 can manipulate gene expression in distinct chromatin contexts (Fig. 2a, b and Supplementary Fig. 8a, b). One neighboring TE of the same family adjacent to ATR was also upregulated (Fig. 2b). This effect might reflect co-regulation of these two TE copies and/or the presence of regulatory regions at the 3′ end. We observed robust activation of EVD and ATR, and few DEGs, in three independent T2 lines compared to a no guide control line (Supplementary Fig. 8c). Thus, SunTag VP64-mediated activation was highly specific.

### Passage 4

To gain a better understanding of NtDRMcd off-target activity, we profiled genome-wide methylation levels in multiple generations of SunTag NtDRMcd g4+ g10+ g18 plants. Genome-wide

### Passage 5

WGBS library preparation and analysis. For the preparation of WGBS libraries, genomic DNA was first extracted from leaves and inflorescence tissue (for Ler samples) using the DNeasy Plant Mini Kit (Qiagen). 100 ng of DNA was then used for subsequent shearing using a Covaris S2 Focused Ultrasonicator. Libraries were then prepared using either the Ovation Ultralow Methyl-Seq kit (NuGen) in conjuction with the EpiTect Bisulfite Kit (Qiagen), or the Hyper Prep Kit (KAPA Biosystems) in conjuction with either the EZ DNA Methylation-Lightning Kit (Zymo) or the EpiTect Bisulfite Kit (Qiagen). Single-end 50 bp reads were then uniquely aligned to the TAIR10 genome using BS-Seeker258. Methylation levels were then calculated for the CG, CHG, and CHH contexts. A filter was implemented to remove reads with three or more consecutively methylated cytosines in the CHH context, as previously described59. Metaplots of BS-seq data were generated with custom Python and R scripts. For methylation calculations over individual chromosomes, each chromosome was split into 100 kb bins. Methylation values were then calculated from these bins.

### Passage 6

ChIP. T2 SunTag VP64 gRNA4 and Col-0 control plants were first grown on MS plates for 2 weeks and 2 grams of tissue were then collected per sample. After grinding the tissue, samples were crosslinked in 1% formaldehyde, chromatin was extracted, and later sonicated using Bioruptor Plus (diagenode). Immunoprecipitations were performed using mouse monoclonal anti-HA.11 epitope tag antibodies (clone 16B12, Covance catalog #MMS-101R). Chromatin-protein complexes were isolated with a 1:1 mix of Protein A and Protein G Dynabeads (Invitrogen) for 3 h at 4 °C. Beads were washed with low salt buffer (2 × ), high salt buffer, LiCl buffer, and TE buffer, and complexes were eluted with elution buffer (2 × 20min at 65 °C). DNA-protein complexes were reversed crosslinked overnight at 65 °C followed by proteinase K treatment at 45 °C for 5 h. DNA was purified using phenol:chloroform, followed by NaOAc/EtOH precipitation along with GlycoBlue (Invitrogen) overnight at -20 °C. DNA was washed with 70% EtOH and resuspended with water. For ChIP-qPCR, the ACT7 locus was detected using the oligos 5′-AGCACGGATCGAATCACATA-3′ and 5′-CTCGCTGCTTCTCGAATCTT-3′. For detection of the FWA locus, oligos 5′-AAGAGTTATGGGCCGAAGC-3′ and 5′-CGCTCGTATGAATGTTGAATG-3′ were used. Libraries were prepared using the Ovation Ultralow kit (NuGen). ChIP-seq analysis was done by uniquely aligning single-end 50 bp reads to the TAIR10 genome using Bowtie56 allowing two mismatches (-v 2). Subsequently, peaks were called using MACS257 with default parameters. We identified 3 peaks, including FWA, at FDR 5% and above five-fold enrichment. An off-target peak from within this set of 3 peaks was defined by the presence of a potential gRNA binding site in proximity to a called MACS2 peak. We identified one major off-target peak for gRNA4 on chromosome 4.

### Passage 7

to quantify differences in methylation. FWA promoter region sequences were detected using oligos 5′-TTGGGTTTAGTGTTTACTTG-3′ and 5′-GAATGTTGA ATGGGATAAGGTA-3′.

### Passage 8

To test whether VP64-mediated FWA activation affected promoter methylation, we performed whole-genome bisulfite sequencing (WGBS) of T2 gRNA4 plants. Compared to Col-0 and no guide controls, T2 gRNA4 lines showed reduced CG methylation within the promoter, whereas gene body methylation downstream of the target site, as well as genome-wide methylation levels, remained unaffected (Fig. 1b and Supplementary Fig. 4a, b, c). Thus, targeted activation of silenced genes can reduce promoter methylation.
