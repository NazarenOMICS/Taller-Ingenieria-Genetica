---
type: reference
status: current
date: 2026-07-14
source: "notebooklm:dcas9-fto-granulosa/q03-especificidad-off-target"
related:
  - "[[Notes/Dashboards/dCas9-p300 off-target specificity]]"
---

# Q05 - What gaps or limitations remain in these sources regarding direct experimental evidence of dCas9-p300-specific off-target binding or off-target transcriptomic changes in human cells (as opposed to general CRISPR-Cas9 off-target literature)?

While the sources describe **dCas9-p300** as a potent and potentially specific tool for epigenetic editing, they identify several significant gaps and limitations regarding direct experimental evidence of its specificity in human cells.

### **Uncertainty of Global Epigenetic Footprints**
A primary gap identified in the sources is whether the overexpression of dCas9-p300 leads to unintended, widespread changes in the epigenome.
*   **Lack of Proof:** It is explicitly stated that while site-specific manipulation is the goal, it is **"yet to be determined"** if overexpressing these fusion complexes leaves a **"low-level but global epigenetic footprint"** across the genome  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 2|[1]]]. 
*   **Analogy to Other Modifiers:** This concern is speculative, based on observations of other epigenetic editors like **dCas9-DNMT3A**, which was found to leave methylation footprints independent of the sgRNA used  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 2|[1]]]. Direct genome-wide evidence confirming or refuting a similar pervasive effect for dCas9-p300 is not provided in these sources.

### **Limitations in Human Cell Experimental Data**
Much of the detailed functional evidence in the sources comes from model organisms or specific cell lines, leaving gaps for broad human application.
*   **Model Organism Focus:** Key studies on p300-mediated stabilization of gene expression (such as the *Foxp3* locus) were conducted in **mouse primary T cells**  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 3|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 4|[3]]].
*   **Deferred Human Validation:** Authors of the mouse studies acknowledge that for human clinical usage, they must still **"re-select gRNA sequences in the human genome and investigate off-target activity in our next study"**  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 4|[3]]].
*   **Cell Context Sensitivity:** The sources note that p300 effectiveness is highly dependent on the **original chromatin state** (e.g., existing H3K27me3 marks) of the target cell, suggesting that specificity results in one human cell type may not be generalizable to others  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 1|[4]]].

### **Mechanistic Ambiguity: Memory vs. Presence**
There is a lack of experimental clarity regarding the longevity and cause of the transcriptional changes induced by dCas9-p300.
*   **Causality Gap:** It remains unclear if the observed gene activation is a result of the **newly induced epigenetic mark** itself (true "epigenetic memory") or simply the **continued physical presence** of the dCas9-p300 complex at the target site  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 1|[4]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 6|[5]]].
*   **Requirement for Degron Studies:** To resolve this, the sources suggest that future research utilizing **rapid degradation technologies** (like auxin-inducible degrons) is necessary to see if the activation persists once the p300 fusion protein is removed  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 6|[5]]].

### **Binding vs. Functional Activation Mismatch**
The sources highlight a disconnect between where dCas9 binds and where it actually functions, which complicates specificity assessments.
*   **Less Stringent Binding:** Mapping studies (ChIP-seq) indicate that dCas9 has **less stringent requirements for DNA binding** than for nuclease cleavage, often associating with many off-target sites in open chromatin  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 5|[6]]].
*   **Functional Evidence Gap:** While general dCas9 binding is well-documented, the sources provide **limited direct evidence** mapping the subset of those sites where p300 actually succeeds in inducing functional **off-target transcriptional activation**  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 2|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 5|[6]]].

### **Technological Hurdles in Verification**
*   **Transduction Efficiency:** In primary cell studies, researchers reported they **"could not verify the function... in the in vivo mouse model"** because the transduction efficiency was too low to obtain enough edited cells for a robust disease model study  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf#Passage 8|[7]]]. This suggests that low efficiency can be a barrier to gathering high-quality, large-scale specificity data.
*   **Lack of Gold Standards:** Unlike CRISPR knockout (CRISPRko), which has "gold standard" gene sets for validation, **CRISPRa lacks an obvious standard** to assess and compare the performance of different activators like p300 [8].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|PDF]]
- Texto literal:
> These aforementioned locus-specific epigenetic manipulation strategies are based on overexpression of a dCas9-fused epigenetic modifier complex. Such tools have been shown to specifically manipulate the expression of the target loci. However, whether overexpression of the fusion epigenetic complexes may leave a low level but global epigenetic footprint in the genome, as noted for the dCas9–DNMT3A fusion complex134, is yet to be determined. Therefore, novel strategies that enable local recruitment of endogenous epigenetic machineries may provide a higher precision in epigenetic editing. To this end, novel approaches such as Fkbp/Frb-based inducible recruitment for epigenome editing by Cas9 (FIRE–Cas9)145 may provide higher specificity in epigenetic editing by recruiting endogenous chromatin regulators.

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|PDF]]
- Texto literal:
> Results: In this study, we applied clustered regularly interspaced short palindromic repeats (CRISPR)-dCas9-based epigenome editing to mouse primary T cells, focusing on the Forkhead box P3 (Foxp3) gene locus, a master transcription factor of regulatory T cells (Tregs). The Foxp3 gene locus is regulated by combinatorial epigenetic modi- fications, which determine the Foxp3 expression. Foxp3 expression is unstable in transforming growth factor beta (TGF-β)-induced Tregs (iTregs), while stable in thymus-derived Tregs (tTregs). To stabilize Foxp3 expression in iTregs, we introduced dCas9-TET1CD (dCas9 fused to the catalytic domain (CD) of ten-eleven translocation dioxygenase 1 (TET1), methylcytosine dioxygenase) and dCas9-p300CD (dCas9 fused to the CD of p300, histone acetyltransferase) with guide RNAs (gRNAs) targeted to the Foxp3 gene locus. Although dCas9-TET1CD induced partial demethylation in enhancer region called conserved non-coding DNA sequences 2 (CNS2), robust Foxp3 stabilization was not observed. In contrast, dCas9-p300CD targeted to the promoter locus partly maintained Foxp3 transcription in cultured and primary T cells even under inflammatory conditions in vitro. Furthermore, dCas9-p300CD promoted expression of Treg signature genes and enhanced suppression activity in vitro.

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|PDF]]
- Texto literal:
> regions (Additional file 2: Table S1). In our study, which mainly focused on mice experiments and revealing the relationships between epigenetics and gene expression, all candidate genes were not strongly involved in direct Foxp3 induction or Treg functions to the best of our knowledge. For future clinical usage, we have to re-select gRNA sequences in the human genome and investigate off-target activity in our next study.

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|PDF]]
- Texto literal:
> Considering that dCas9-p300CD-mediated gene activation is observed only in a certain fraction, but not all of the transduced cells, effectiveness of dCas9-p300CD depends on each transduced cell. Examination of original chromatin states or accessibility of epigenetic modifier to the target locus in individual cells will clarify the more effective usage of epigenome editing. For example, H3K27me3, inactive epigenetic modification, is marked at the Foxp3 promoter locus in conventional T cells [64]. Supposing that dCas9-p300CD has to rewrite this inactive mark with eraser help for transactivation, it is easy to speculate that effectiveness is decreased in such cells than H3K27 unmodified cells. Furthermore, memorization and stabilization of artificially induced epigenetic modification become issue. Our result suggested gene activation is strongly maintained in some cases. Whether this phenomenon was the results of epigenome editing or stable existence of epigenetic modifier is carefully examined in the next study.

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 6|Pasaje 6]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|PDF]]
- Texto literal:
> Identifying the causal link between epigenetic marks and gene expression remains a central goal of chromatin biology. Thus, these aforementioned studies using dCas9 as a guidable platform to edit locus-specific epigenetic information will be an indispensable tool to achieve this. Now that the tools that enable us to alter the epigenome are in place, the next phase is to utilize them to better characterize regulatory elements and cellular states. To this end, researchers have already applied dCas9-based epigen-ome-editing tools for a number of exciting purposes including high-throughput screenings to characterize functional distal enhancers146, targeted reprogramming of lineage specifica-tion147,148, generation of induced pluripotent stem cells149, and reversal of HIV latency150. One of the remaining challenges is to elucidate the causal relationship between the presence of an epigenetic mark and its regulatory impact. Since the dCas9-fused epigenetic modifier remains associated with the target site, it is unclear whether the regulatory activity is due to the induced epigenetic mark or the complex. To this end, recent efforts using rapid and reversible epigenome-editing approaches are highly notable145. Future studies that enable rapid degradation of the targeting complex at the target site, such as with auxin-inducible degron technology151, should allow us to further characterize the functional consequences of epigenetic marks and investigate the associated temporal epigenetic memory for each mark.

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 5|Pasaje 5]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|PDF]]
- Texto literal:
> Finally, we could not verify the function of epigenomeedited iTregs in the in vivo mouse model, because the transduction efficiency was not high enough to obtain a sufficient number of iTregs for disease model study. However, it has been reported that, in contrast to mice T cells, human T cells could be expanded using a rapid expansion protocol [68]. Moreover, lentivirus-mediated gene delivery methods have been established for clinical uses [69]. In our future study, we aim to apply our system to the human genome and human T cells, and expect its usage in medicine in the future.

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf#Passage 8|Pasaje 8]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf|PDF]]
- Texto literal:
> Unlike CRISPRko and CRISPRi, CRISPRa lacks an obvious gold standard gene set with which to assess screen performance and compare previously published screens (Supplementary Table 5). Therefore, to assess performance, we performed a vemurafenib-resistance screen similar to that previously executed

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf|kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/ashot_2019_site_specific_manipulation_of_arabidopsis_loci_using_crispr.pdf|ashot_2019_site_specific_manipulation_of_arabidopsis_loci_using_crispr.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/congting_2023_off_target_effects_in_crispr_cas9_gene_editing.pdf|congting_2023_off_target_effects_in_crispr_cas9_gene_editing.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/fatemeh_2019_crispr_cpf1_proteins_structure_function_and_implications_for.pdf|fatemeh_2019_crispr_cpf1_proteins_structure_function_and_implications_for.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/hongyi_2020_applications_of_genome_editing_technology_in_the_targeted.pdf|hongyi_2020_applications_of_genome_editing_technology_in_the_targeted.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf|tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/yu_2015_making_sense_of_gwas_using_epigenomics_and_genome.pdf|yu_2015_making_sense_of_gwas_using_epigenomics_and_genome.pdf]]
