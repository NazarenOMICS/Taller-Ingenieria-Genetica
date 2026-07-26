---
type: notebook-source
source_id: "b88bde65-5643-4d19-9d2f-b0946e56ad5c"
notebook_id: "e1baac88-0719-426f-b47a-b620d48b6489"
slug: "q03-especificidad-off-target"
vault_slug: "dcas9-fto-granulosa/q03-especificidad-off-target"
project: "dcas9-fto-granulosa"
url: ""
source_type: web
status: active
date: 2026-07-14
pdf: "Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/congting_2023_off_target_effects_in_crispr_cas9_gene_editing.pdf"
related:
  - "[[Notes/Dashboards/dCas9-p300 off-target specificity]]"
used_in_qa: true
cited_in_count: 3
qa_notes:
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/QA/answers/2026-07-24 Q02 - what-guide-rna-mismatch-tolerance-or.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/QA/answers/2026-07-24 Q03 - what-genome-wide-profiling-methods-e.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/QA/answers/2026-07-24 Q04 - how-does-specificity-profile-dcas9-fusion.md]]"
---

# congting_2023_off_target_effects_in_crispr_cas9_gene_editing.pdf

## PDF

![[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/congting_2023_off_target_effects_in_crispr_cas9_gene_editing.pdf]]

## Source Guide

## Cited Passages

### Passage 1

WGS analysis of off-target effects has been well documented in cell culture studies (Smith et al., 2014; Veres et al., 2014; Iyer et al., 2015). By comparing the genome sequences before and after CRISPR/Cas9 editing, WGS can directly uncover desired and unwanted editing events. The accuracy and sensitivity of WGS in off-target detection is determined by sequencing depth, thus when

### Passage 2

Although CRISPR/Cas systems exhibit tremendous potential in translational medicine, off-target effects remain a major challenge (Fu et al., 2013; Hsu et al., 2013; Pacesa et al., 2022). The off-target effects occur when Cas9 acts on untargeted genomic sites and creates cleavages that may lead to adverse outcomes. The off-target sites are often sgRNA-dependent, since Cas9 is known to tolerate up to 3 mismatches between sgRNA and genomic DNA (Fu et al., 2013; Hsu et al., 2013; Wang et al., 2016a). In this scenario, in silico tools are useful to search for potential off-target sites in the whole genome and calculate the likelihood of an off-target editing (Naeem et al., 2020). Nevertheless, accumulative studies have proved that sgRNAindependent off-target effects also exist, urging unbiased experimental detection and validation (Richter et al., 2020; O’Geen et al., 2015). In this review, we summarize available methods for the assessment of off-target effects, indicating their advantages versus limitations. Some of these detection methods for off-targets prediction is applicable for other family of Cas nucleases, such as Cas12a (Cpf1), which also create DSBs on off-target sites (Kim et al., 2019). Furthermore, we discuss strategies to improve CRISPR/Cas9 specificity and to reduce undesired mutagenesis, which is crucial for their future application in gene therapy.

### Passage 3

Minimal read depth; eliminated background; does not require a

### Passage 4

Kuscu, C., Arslan, S., Singh, R., Thorpe, J., and Adli, M. (2014). Genome-wide analysis reveals characteristics of off-target sites bound by the Cas9 endonuclease. Nat. Biotechnol. 32 (7), 677–683. doi:10.1038/nbt.2916

### Passage 5

In addition to base editors, CRISPR/Cas9-mediated off-target effects can also be reduced by epigenetic editors (Willyard, 2017). These tools utilize enzymatically dead Cas9 (dCas9) to direct

### Passage 6

FlashFry [23] Provides information about GC contents

### Passage 7

DIG-seq [34] Uses cell-free chromatin with Digenome-seq pipeline

### Passage 8

3 Experimental detection

### Passage 9

Another more popular method to detect off-target sites in cells is called GUIDE-seq (Tsai et al., 2015). This technique relies on the delivery of double-stranded oligonucleotides (dsODNs) with known sequences, which can integrate into DSBs during NHEJ (nonhomologous end joining). The integrated dsODNs provide templates for targeted PCR amplification and sequencing of the tagged DNA fragments (Tsai et al., 2015; Malinin et al., 2021; Yaish et al., 2022) (Figure 1B). GUIDE-seq can detect off-target sites with indel frequencies as low as 0.03% (Tsai et al., 2015). GUIDE-seq is more sensitive than the IDLV method because dsODNs integrate more efficiently and precisely into DSBs, while the integration events of IDLV is low in number and can distribute as far as 500bp away from the actual DSB sites (Tsai et al., 2015; Cromer et al., 2023). A primary limitation of GUIDE-seq is relevant to the low delivery efficiency of dsODNs into cells, which results in detection of only 30%–50% of all the DSBs (Tsai et al., 2015; Pan et al., 2022).

### Passage 10

IDLV, GUIDE-seq and LAM–HTGTSmeasure the DSB-derived DNA fragments to indirectly infer the presence of DSBs. Alternatively, DSB can be directly detected by BLESS (direct in situ breaks labeling, enrichment on streptavidin and next-generation sequencing), which captures DSBs in situ via the ligation of biotinylated linkers to cleavage sites in fixed cells (Crosetto et al., 2013) (Figure 1D). BLESS demonstrates a false positive rate lower than 1% (Crosetto et al., 2013; Yan et al., 2017; Kim et al., 2019), validating the accuracy of this method. The predominant limitation of this technique is that BLESS only captures DSBs that are present at the moment of sample fixation, which underrepresents the off-target events. Therefore, BLESS demands millions of cells to reduce the false negative rate.

### Passage 11

To enhance the sensitivity of BLESS and reduce its requirement on cell number, BLISS (breaks labeling in situ and sequencing) technology was developed (Yan et al., 2017). BLISS ligates DSB ends with adapters containing the T7 promoter, so the tagged DNA fragments can be linearly amplified via T7-mediated transcription before sequencing (Yan et al., 2017; Ballarino et al., 2021). Compared to BLESS, BLISS demands only a few thousand cells and demonstrates a higher sensitivity. For example, Winston et al. performed side-by-side comparison between BLISS and BLESS to detect the off-target sites of validated sgRNAs targeting EMX1 or VEGFA (Yan et al., 2017). For the sgRNA targeting EMX1, BLESS uncovered 6 off-target sites, all of which are included in the 10 genuine off-target sites that BLISS discovered. Similarly, for the sgRNA targeting VEGFA, besides the 16 off-target sites that were detected by both methods, BLISS identified 27 additional offtarget sites that are not found by BLESS (Yan et al., 2017). Thus the sensitivity of BLISS is more than two folds higher than BLESS.

### Passage 12

3.3 In vivo detection

### Passage 13

Both IDLV and GUIDE-seq rely on the DNA insertion activity during NHEJ. However, DSBs can also lead to chromosome translocation and rearrangement. To better detect such DSBs, LAM–HTGTS was developed (Frock et al., 2015; Hu et al., 2016). In this technique, mammalian cells are cultured with Cas9 nuclease to create “bait” and “prey” DSBs. The “bait” DSBs are the sites that are previously known to be cleaved by the nuclease, while the “prey” DSBs are the unknown off-target sites that are expected to ligate with the “bait” site after chromosome rearrangement. The bait-prey junctions can be linearly amplified and enriched using a biotinylated primer. Then these DNA are ligated to adaptors and

### Passage 14

Low validation rate; affected by antibody specificity and chromatin

### Passage 15

Digenome-seq is a highly sensitive method that can identify indels with 0.1% frequency or lower (Kim et al., 2015). In this method, genomic DNA is firstly extracted from cells and incubated with Cas9/sgRNA ribonucleoprotein (RNP) complex for gene editing. The edited DNA is next analyzed by wholegenome sequencing (WGS) to detect sequences accurately sharing one end, which indicates the loci where DSBs exist. The current Digenome-seq pipeline is equipped with a refined scoring algorithm and allows off-target sites screening involving multiple sgRNA (Kim et al., 2016). Due to the high background of non-specific DSBs in the purified DNA samples, Digenome-seq requires high sequencing coverage (~400–500 million reads for human genome) thus the sequencing cost can be relatively high (Kim et al., 2019). The demand for a high-quality reference genome also limits its broader use in uncommon organisms (Figure 1A).

### Passage 16

Ju, H., Kim, D., and Oh, Y. K. (2022). Lipid nanoparticle-mediated CRISPR/Cas9 gene editing and metabolic engineering for anticancer immunotherapy. Asian J. Pharm. Sci. 17 (5), 641–652. doi:10.1016/j.ajps.2022.07.005

### Passage 17

induced by DSBs

### Passage 18

References

### Passage 19

Wang, X., Wu, Y., and Yee, J. K. (2021). Detection of CRISPR/Cas9-Generated offtarget effect by integration-defective lentiviral vector.MethodsMol. Biol. 2162, 243–260. doi:10.1007/978-1-0716-0687-2_14

### Passage 20

The Cas9/sgRNA complex produces site-specific DNA double-strand breaks (DSBs), stimulating homology-directed repair (HDR) or non-homologous end joining (NHEJ) pathways to achieve genome editing. HDR is an accurate but inefficient mechanism, which utilizes a homologous donor template to repair DNA cleavages (Li et al., 2019; Fu

### Passage 21

Has false positives
