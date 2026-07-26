---
type: reference
status: current
date: 2026-07-24
source: "notebooklm:dcas9-fto-granulosa/q03-especificidad-off-target"
related:
  - "[[Notes/Dashboards/dCas9-p300 off-target specificity]]"
---

# Q05 - What gaps or limitations remain in these sources regarding direct experimental evidence of dCas9-p300-specific off-target binding or off-target transcriptomic changes in human cells (as opposed to general CRISPR-Cas9 off-target literature)?

While the sources characterize **dCas9-p300** as a potent epigenetic editor, they reveal several significant gaps and limitations regarding direct experimental evidence of its specificity in human cells, particularly when compared to the broader body of literature on general CRISPR-Cas9 off-targets.

### **Limited Scope of Human Transcriptomic Evidence**
The direct evidence for dCas9-p300 functional specificity in human cells is primarily derived from a narrow set of targeted loci.
*   **Small Sample Size of Targets:** The main human-cell transcriptomic study described (RNA-seq in HEK293T cells) focused specifically on targeting the **IL1RN promoter**  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/hilton_2015.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/hilton_2015.pdf#Passage 7|[2]]]. While this study found only two significant off-target transcripts (*KDR* and *FAM49A*), the sources do not provide similar genome-wide transcriptomic data for a broad range of other human gene targets  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/hilton_2015.pdf#Passage 7|[2]]].
*   **Reliance on a Single Cell Type:** Much of the reported high-specificity data for dCas9-p300 in humans comes from **HEK293T cells**  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/hilton_2015.pdf#Passage 7|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/hilton_2015.pdf#Passage 8|[3]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/fatemeh_2019_crispr_cpf1_proteins_structure_function_and_implications_for.pdf#Passage 3|[4]]]. The sources acknowledge that the effectiveness and potentially the specificity of these systems can be **cell context-dependent**, meaning results from HEK293T cells may not be fully generalizable to other primary human tissues  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 2|[5]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 2|[6]]].

### **Uncertainty Regarding "Global Epigenetic Footprints"**
A recurring limitation is the lack of definitive evidence regarding whether dCas9-p300 causes unintended genome-wide alterations to the epigenome.
*   **Theoretical vs. Experimental Evidence:** It is explicitly noted as **"yet to be determined"** whether the overexpression of dCas9-p300 leaves a **low-level but global epigenetic footprint** across the human genome  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 3|[7]]]. 
*   **Analogous Concerns:** This research gap is highlighted by comparisons to other editors, such as **dCas9-DNMT3A**, which was found to leave methylation footprints independent of the sgRNA sequence; however, direct confirmation of a similar pervasive effect for dCas9-p300 is absent  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 3|[7]]].

### **Reliance on Model Organisms for Functional Validation**
While human cells were used for initial activation tests, more complex studies on the **stabilization** of gene expression and functional outcomes were conducted in non-human systems.
*   **Mouse-Focused Research:** Key evidence regarding the ability of dCas9-p300 to maintain gene expression under inflammatory conditions was established in **mouse primary T cells**  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 4|[8]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 5|[9]]]. 
*   **Deferred Human Investigation:** The authors of these studies state that for future human clinical applications, they must still **"re-select gRNA sequences in the human genome and investigate off-target activity"** in subsequent research  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 6|[10]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 3|[11]]].

### **Mechanistic Ambiguity and Causality Gaps**
There is a lack of experimental clarity regarding why and how the activation persists.
*   **Causality Mismatch:** It remains unclear if the observed transcriptional changes are the result of the **induced H3K27ac mark itself** (true "epigenetic memory") or the **continued physical presence** of the dCas9-p300 complex at the target site  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 2|[6]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf#Passage 8|[12]]].
*   **Need for Advanced Testing:** To resolve this, the sources suggest the need for **rapid degradation technologies** (like auxin-inducible degrons) to see if gene activation persists after the tool is removed, which is described as an ongoing research requirement  [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf#Passage 8|[12]]].

### **Lack of Standardized Benchmarks**
Unlike CRISPR knockout (CRISPRko), which benefits from well-established "gold standard" gene sets for validating screen performance, **CRISPRa lacks an obvious standard** to assess and compare the performance of different activators, including p300 [13]. This makes it difficult to quantitatively compare the specificity of dCas9-p300 against other activation platforms across different human experimental setups [13].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/hilton_2015.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/hilton_2015.pdf|PDF]]
- Texto literal:
> not observed for dCas9<supVP64</sup. Together, these results demonstrate that dCas9p300 Core is a potent programmable transcription factor that can be used to regulate gene expression from a variety of promoterproximal and promoterdistal locations.

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/fatemeh_2019_crispr_cpf1_proteins_structure_function_and_implications_for.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/fatemeh_2019_crispr_cpf1_proteins_structure_function_and_implications_for.pdf|PDF]]
- Texto literal:
> promoter based-dLbCpf1-p300core could induce transcription in the cells derived from human tissues other than fetal kidney (HEK239); Accordingly, the cell context was not the determinant factor [87].

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|PDF]]
- Texto literal:
> Considering that dCas9-p300CD-mediated gene activation is observed only in a certain fraction, but not all of the transduced cells, effectiveness of dCas9-p300CD depends on each transduced cell. Examination of original chromatin states or accessibility of epigenetic modifier to the target locus in individual cells will clarify the more effective usage of epigenome editing. For example, H3K27me3, inactive epigenetic modification, is marked at the Foxp3 promoter locus in conventional T cells [64]. Supposing that dCas9-p300CD has to rewrite this inactive mark with eraser help for transactivation, it is easy to speculate that effectiveness is decreased in such cells than H3K27 unmodified cells. Furthermore, memorization and stabilization of artificially induced epigenetic modification become issue. Our result suggested gene activation is strongly maintained in some cases. Whether this phenomenon was the results of epigenome editing or stable existence of epigenetic modifier is carefully examined in the next study.

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|PDF]]
- Texto literal:
> These aforementioned locus-specific epigenetic manipulation strategies are based on overexpression of a dCas9-fused epigenetic modifier complex. Such tools have been shown to specifically manipulate the expression of the target loci. However, whether overexpression of the fusion epigenetic complexes may leave a low level but global epigenetic footprint in the genome, as noted for the dCas9–DNMT3A fusion complex134, is yet to be determined. Therefore, novel strategies that enable local recruitment of endogenous epigenetic machineries may provide a higher precision in epigenetic editing. To this end, novel approaches such as Fkbp/Frb-based inducible recruitment for epigenome editing by Cas9 (FIRE–Cas9)145 may provide higher specificity in epigenetic editing by recruiting endogenous chromatin regulators.

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|PDF]]
- Texto literal:
> Results: In this study, we applied clustered regularly interspaced short palindromic repeats (CRISPR)-dCas9-based epigenome editing to mouse primary T cells, focusing on the Forkhead box P3 (Foxp3) gene locus, a master transcription factor of regulatory T cells (Tregs). The Foxp3 gene locus is regulated by combinatorial epigenetic modi- fications, which determine the Foxp3 expression. Foxp3 expression is unstable in transforming growth factor beta (TGF-β)-induced Tregs (iTregs), while stable in thymus-derived Tregs (tTregs). To stabilize Foxp3 expression in iTregs, we introduced dCas9-TET1CD (dCas9 fused to the catalytic domain (CD) of ten-eleven translocation dioxygenase 1 (TET1), methylcytosine dioxygenase) and dCas9-p300CD (dCas9 fused to the CD of p300, histone acetyltransferase) with guide RNAs (gRNAs) targeted to the Foxp3 gene locus. Although dCas9-TET1CD induced partial demethylation in enhancer region called conserved non-coding DNA sequences 2 (CNS2), robust Foxp3 stabilization was not observed. In contrast, dCas9-p300CD targeted to the promoter locus partly maintained Foxp3 transcription in cultured and primary T cells even under inflammatory conditions in vitro. Furthermore, dCas9-p300CD promoted expression of Treg signature genes and enhanced suppression activity in vitro.

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|PDF]]
- Texto literal:
> In this study, we established two epigenome-modifying systems based on CRISPR-dCas9 technology and applied them to the Foxp3 gene locus. We aimed to investigate the cross-talk of epigenome editing and endogenous cellular responses in primary immune cells and to lay a foundation for future clinical development. To stabilize Foxp3 expression in artificially epigenome-edited iTregs: dCas9 fused with TET1CD was targeted to the Foxp3 CNS2 locus, and dCas9 fused with p300CD to the Foxp3 promoter locus. We designed 10 gRNA sequences in each locus, screened effective sequences in T cell lines 68-41, and then applied them to mouse primary T cells. We confirmed that both systems with specific gRNAs could induce epigenetic modifications in cultured cell lines. In primary T cells, dCas9-TET1CD partially demethylated the CNS2 locus under iTreg conditions, but Foxp3 expression was not robustly stabilized by inflammatory cytokine stimuli. In contrast, dCas9-p300CD strongly activated and stabilized Foxp3 expression, particularly with TGF-β, even under inflammatory conditions.

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 5|Pasaje 5]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|PDF]]
- Texto literal:
> regions (Additional file 2: Table S1). In our study, which mainly focused on mice experiments and revealing the relationships between epigenetics and gene expression, all candidate genes were not strongly involved in direct Foxp3 induction or Treg functions to the best of our knowledge. For future clinical usage, we have to re-select gRNA sequences in the human genome and investigate off-target activity in our next study.

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 6|Pasaje 6]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|PDF]]
- Texto literal:
> Finally, we could not verify the function of epigenomeedited iTregs in the in vivo mouse model, because the transduction efficiency was not high enough to obtain a sufficient number of iTregs for disease model study. However, it has been reported that, in contrast to mice T cells, human T cells could be expanded using a rapid expansion protocol [68]. Moreover, lentivirus-mediated gene delivery methods have been established for clinical uses [69]. In our future study, we aim to apply our system to the human genome and human T cells, and expect its usage in medicine in the future.

### Extracto 9
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|PDF]]
- Texto literal:
> Identifying the causal link between epigenetic marks and gene expression remains a central goal of chromatin biology. Thus, these aforementioned studies using dCas9 as a guidable platform to edit locus-specific epigenetic information will be an indispensable tool to achieve this. Now that the tools that enable us to alter the epigenome are in place, the next phase is to utilize them to better characterize regulatory elements and cellular states. To this end, researchers have already applied dCas9-based epigen-ome-editing tools for a number of exciting purposes including high-throughput screenings to characterize functional distal enhancers146, targeted reprogramming of lineage specifica-tion147,148, generation of induced pluripotent stem cells149, and reversal of HIV latency150. One of the remaining challenges is to elucidate the causal relationship between the presence of an epigenetic mark and its regulatory impact. Since the dCas9-fused epigenetic modifier remains associated with the target site, it is unclear whether the regulatory activity is due to the induced epigenetic mark or the complex. To this end, recent efforts using rapid and reversible epigenome-editing approaches are highly notable145. Future studies that enable rapid degradation of the targeting complex at the target site, such as with auxin-inducible degron technology151, should allow us to further characterize the functional consequences of epigenetic marks and investigate the associated temporal epigenetic memory for each mark.

### Extracto 10
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf#Passage 8|Pasaje 8]] | [[Research/Papers/dcas9-fto-granulosa/q03-especificidad-off-target/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf|PDF]]
- Texto literal:
> Unlike CRISPRko and CRISPRi, CRISPRa lacks an obvious gold standard gene set with which to assess screen performance and compare previously published screens (Supplementary Table 5). Therefore, to assess performance, we performed a vemurafenib-resistance screen similar to that previously executed

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/fatemeh_2019_crispr_cpf1_proteins_structure_function_and_implications_for.pdf|fatemeh_2019_crispr_cpf1_proteins_structure_function_and_implications_for.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/hilton_2015.pdf|hilton_2015.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf|kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/ashot_2019_site_specific_manipulation_of_arabidopsis_loci_using_crispr.pdf|ashot_2019_site_specific_manipulation_of_arabidopsis_loci_using_crispr.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/congting_2023_off_target_effects_in_crispr_cas9_gene_editing.pdf|congting_2023_off_target_effects_in_crispr_cas9_gene_editing.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/hongyi_2020_applications_of_genome_editing_technology_in_the_targeted.pdf|hongyi_2020_applications_of_genome_editing_technology_in_the_targeted.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf|tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q03-especificidad-off-target/Sources/yu_2015_making_sense_of_gwas_using_epigenomics_and_genome.pdf|yu_2015_making_sense_of_gwas_using_epigenomics_and_genome.pdf]]
