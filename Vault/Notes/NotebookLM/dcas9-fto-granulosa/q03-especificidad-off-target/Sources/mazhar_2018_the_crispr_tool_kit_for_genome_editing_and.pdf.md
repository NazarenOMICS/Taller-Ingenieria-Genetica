---
type: notebook-source
source_id: "b3678d5a-9f29-4abb-a50c-5e914e81d936"
notebook_id: "e1baac88-0719-426f-b47a-b620d48b6489"
slug: "q03-especificidad-off-target"
vault_slug: "dcas9-fto-granulosa/q03-especificidad-off-target"
project: "dcas9-fto-granulosa"
url: ""
source_type: web
status: active
date: 2026-07-14
pdf: "Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf"
related:
  - "[[Notes/Dashboards/dCas9-p300 off-target specificity]]"
used_in_qa: true
cited_in_count: 5
qa_notes:
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/QA/answers/2026-07-24 Q01 - according-to-these-sources-what-known.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/QA/answers/2026-07-24 Q02 - what-guide-rna-mismatch-tolerance-or.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/QA/answers/2026-07-24 Q03 - what-genome-wide-profiling-methods-e.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/QA/answers/2026-07-24 Q04 - how-does-specificity-profile-dcas9-fusion.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/QA/answers/2026-07-24 Q05 - what-gaps-or-limitations-remain-these.md]]"
---

# mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf

## PDF

![[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]]

## Source Guide

## Cited Passages

### Passage 1

In addition to these studies that expand the targeting scope of CRISPR tools, researchers are actively developing novel ways to increase the targeting specificity of the CRISPR-Cas9 system. Understanding the extent of off-target effects of CRISPR-Cas9 targeting has been one major goal. Given that CRISPR systems have evolved as a defense system against viruses that tend to frequently mutate, a slightly less specific CRISPR system would be advantageous to bacteria. Indeed, the early efforts to understand CRISPR targeting specificity highlighted this fact and demonstrated that the system may potentially have off-target effects61– 65. In addition to these initial studies, researchers utilized alternative genome-wide tools to understand CRISPR-Cas9 targeting specificity. To this end, we and others have used the chromatin immunoprecipitation and high throughput sequencing (ChIP-Seq) approach to map DNA binding sites of catalytically inactive SpCas9 in vivo66,67. These whole-genome mapping studies

### Passage 2

These aforementioned locus-specific epigenetic manipulation strategies are based on overexpression of a dCas9-fused epigenetic modifier complex. Such tools have been shown to specifically manipulate the expression of the target loci. However, whether overexpression of the fusion epigenetic complexes may leave a low level but global epigenetic footprint in the genome, as noted for the dCas9–DNMT3A fusion complex134, is yet to be determined. Therefore, novel strategies that enable local recruitment of endogenous epigenetic machineries may provide a higher precision in epigenetic editing. To this end, novel approaches such as Fkbp/Frb-based inducible recruitment for epigenome editing by Cas9 (FIRE–Cas9)145 may provide higher specificity in epigenetic editing by recruiting endogenous chromatin regulators.

### Passage 3

is to locally deposit H3K27ac marks. Therefore, in contrast to the local reduction of enhancer marks by dCas9-LSD1, recruitment of histone acetyl transferase P300 through dCas9 fusion (dCas9-P300) resulted in a significant increase in local H3K27ac levels at enhancer elements142. Importantly, unlike other dCas9-fused transactivators, which can result in induction of gene expression primarily from promoter regions, targeting dCas9-P300 allows significant gene expression induction from both promoter and enhancer regions142. Researchers have also exploited other epigenetic modifiers to manipulate additional epigenetic marks. Among these, dCas9 fusion to the PRDM9 methyltransferase fusion complex has been utilized to manipulate local H3K4me3 marks143. Notably, local induction of H3K4me3, which is a marker of active promoters, was observed to be sufficient to allow re-expression of silenced target genes in various cell types143. Histone de-acetylation has been another strategy to locally manipulate chromatin structure and function. To this end, dCas9 fusion to histone deacetylases (HDAC), specifically full-length HDAC3, has been shown to effectively reduce the H3k27ac at the target loci and reduce the gene expression of the target loci144.

### Passage 4

the easiest ways to increase the targeting specificity is changing the delivery method of the Cas9-sgRNA complex. In contrast to plasmid-based delivery, direct delivery of Cas9-sgRNA as a ribonucleotide protein (RNP) complex results in more transient Cas9 activity and hence less off-target effects74,75. Additionally, tandem targeting a locus with two separate sgRNAs utilizing either the nickase Cas9 (nCas9)62,76 or catalytically inactive Cas9 (dCas9)77,78 fused to the DNA cleavage domain of the Fok I substantially reduces the off-target activity of WT Cas9. Since these approaches require two separate guide RNAs to be in a certain proximal distance, the probability of off-target modification is substantially reduced. In parallel to these approaches, inducible Cas9 approaches using small molecule chemicals79, optical light80,81, and ligand-dependent allosteric regulation82 to control temporal and spatial activities of the Cas9/sgRNA complex have also improved targeting specificity. In addition to such engineering approaches at the Cas9 protein, efforts also focused on modifying the sgRNA scaffold to increase the targeting specificity. Interestingly, both increasing65 and decreasing83 the length of the sgRNA guiding sequence by a few base pairs have been reported to enhance the targeting specificity. Furthermore, incorporating ligand-responsive self-cleaving catalytic RNAs (aptazymes) into guide RNA may allow temporal control over the targeting activities of the CRISPR-Cas9 complex84.

### Passage 5

Utilizing CRISPR-Cas9 beyond genome editing So far, the review has focused on the basic mechanism of CRISPR targeting and some of the recent approaches that have been utilized to monitor or improve the targeting specificity of CRISPR-Cas9. Due to its robustness and flexibility, CRISPR is becoming a versatile tool with applications that are transforming not only genome-editing studies, but also many other genome and chromatin manipulation efforts. As summarized in Fig. 3, these alternative application areas are largely possible because of the programmable targeting capacity of catalytically inactive dead

### Passage 6

Identifying the causal link between epigenetic marks and gene expression remains a central goal of chromatin biology. Thus, these aforementioned studies using dCas9 as a guidable platform to edit locus-specific epigenetic information will be an indispensable tool to achieve this. Now that the tools that enable us to alter the epigenome are in place, the next phase is to utilize them to better characterize regulatory elements and cellular states. To this end, researchers have already applied dCas9-based epigen-ome-editing tools for a number of exciting purposes including high-throughput screenings to characterize functional distal enhancers146, targeted reprogramming of lineage specifica-tion147,148, generation of induced pluripotent stem cells149, and reversal of HIV latency150. One of the remaining challenges is to elucidate the causal relationship between the presence of an epigenetic mark and its regulatory impact. Since the dCas9-fused epigenetic modifier remains associated with the target site, it is unclear whether the regulatory activity is due to the induced epigenetic mark or the complex. To this end, recent efforts using rapid and reversible epigenome-editing approaches are highly notable145. Future studies that enable rapid degradation of the targeting complex at the target site, such as with auxin-inducible degron technology151, should allow us to further characterize the functional consequences of epigenetic marks and investigate the associated temporal epigenetic memory for each mark.

### Passage 7

66. Kuscu, C., Arslan, S., Singh, R., Thorpe, J. & Adli, M. Genome-wide analysis reveals characteristics of off-target sites bound by the Cas9 endonuclease. Nat. Biotechnol. 32, 677–683 (2014).

### Passage 8

Meganucleases Zinc finger nucleases
