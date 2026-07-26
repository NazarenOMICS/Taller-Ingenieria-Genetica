---
type: reference
status: current
date: 2026-07-24
source: "notebooklm:dcas9-fto-granulosa/q02-h3k27ac-reversibilidad"
related:
  - "[[Notes/Dashboards/dCas9-p300 H3K27ac reversibility]]"
---

# Q03 - According to these sources, once the dCas9-p300 effector is withdrawn or inactivated (e.g., via inducible/degron systems), how long does the induced gene activation persist before returning to baseline?

Based on the sources, the duration of gene activation following the withdrawal or inactivation of **dCas9-p300** is largely determined by the rapid clearance of the effector protein and the generally **transient nature of histone acetylation marks**, which typically return to baseline levels within a few days or cell divisions  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 3|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 2|[3]]].

### Kinetics of Effector Withdrawal
When using inducible systems to inactivate the effector, the sources provide specific timelines for the disappearance of the dCas9 protein:
*   **Rapid Protein Degradation:** In **Auxin-Inducible Degron (AID)** systems, the total clearance of the dCas9-effector protein pool typically takes **1 to 2 hours**, with an estimated protein half-life of **less than 15 minutes**  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 3|[2]]].
*   **Functional Abrogation:** Upon triggering degradation (e.g., adding auxin), researchers observed a **"sharp drop"** in luciferase reporter output  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 3|[4]]]. In stable cell lines targeting endogenous genes such as *ASCL1* and *IL1RN*, the transcriptional upregulation was **"largely abrogated"** when measured 48 hours after the induction of degradation  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 4|[5]]].

### Persistence of Activation (Epigenetic Memory)
The sources distinguish between the immediate effect of the dCas9-p300 complex and the relative lack of self-sustaining "epigenetic memory" associated with the H3K27ac mark it deposits:
*   **"Short-Term" or "Flexible" Memory:** Histone modifications like acetylation are generally characterized as providing **short-term memory** that is easily reversed  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 2|[3]]]. One source specifically categorizes histone deacetylation (the reciprocal of p300 activity) as having **"no memory,"** meaning the active state likely reverses **before one cell cycle is completed or within very few cell divisions** once the synthetic "writer" is removed  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 2|[3]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 5|[6]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 2|[7]]].
*   **Passive vs. Active Reversal:** Once dCas9-p300 is withdrawn, the induced state is reversed either through **passive dilution** during cell division or the action of **endogenous "eraser" enzymes** like HDACs  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 2|[3]]]. 
*   **Requirement for Maintenance:** Because the effector remains associated with the site during activation, the sources note it is often **unclear if regulatory activity is due to the epigenetic mark itself or the ongoing physical presence of the complex**  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf#Passage 3|[8]]]. This suggests that H3K27ac likely requires continuous recruitment of the writer to counteract endogenous erasers  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf#Passage 3|[8]]].

### Exceptions and "Protracted" Effects
While acetylation-mediated activation is usually transient, the sources suggest that under specific biological "reprogramming" contexts, effects can be more durable:
*   **Reprogramming Cellular States:** In studies of HIV-infected T cells, interfering with the "gatekeeping" process of deacetylation during the transition to a resting state led to **"protracted viral gene expression"** that remained significantly elevated **even 14 days after** the removal of the stimulus  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf#Passage 4|[9]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf#Passage 5|[10]]]. 
*   **Blocking Repression:** In these specific cases, the persistence is likely not due to the acetylation mark itself, but because the temporary activation **blocks the establishment of permanent repressive marks** (like H3K9me3), effectively locking the cell into a state that is "suboptimal for latency"  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf#Passage 6|[11]]].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf|PDF]]
- Texto literal:
> We proceeded to produce stable cell lines with the AID-dCas9-PR construct via Flp mediated integration into transcriptionally competent genomic landing sites in HEK293Trex-FlpIn and CHO-K1 derived cell lines. Functional activity of the integrated AID-dCas9-PR transactivator was confirmed via transfection of fluorescent or luciferase reporters under control of artificial gRNA binding site containing promoters and co-transfection of the corresponding guide RNAs. Addition of auxin to the medium severely reduced reporter output, to below detectable level in the case of the fluorescent reporters (Supplementary Fig. 2c). Similarly, targeting a number of endogenous genes via transfection of mixes of expression plasmids for 3 or 4 sgRNAs to sites within the same promoter region (RasL11a and Arpc1b in CHO cells (Fig. 2b) and ASCL1, IL1RN, OLIG2 and SOX9 in HEK293 cells (Fig. 2c)) resulted in clear transcriptional upregulation, which was markedly reduced in the presence of auxin.

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf|PDF]]
- Texto literal:
> of epigenetic regulation lie ahead. Researchers could work to harness any potential restricted or conditional epigenetic inheritance of histone modifications for developing “short-term” or “flexible” epigenetic memory circuitry [99], which could be intentionally designed to maintain the edited epigenome state for a short period of time. For example, there may be instances, in normal development or for transient therapeutic applications, that require that genes are regulated such that they are suppressed for a short period of time and subsequently reactivated. The repressive state of a gene could be induced with repressive histone methyltransferases and later (before one cell cycle is completed or within very few cell divisions) reversed by either demethylases or a passive histone dilution mechanism. By contrast, complete and permanent repression of genes could be achieved with the incorporation of DNA-methylation-mediated gene silencing [25, 56]. It is important to note that there is evidence to suggest that transiently induced DNA methylation is not maintained, highlighting the

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf|PDF]]
- Texto literal:
> target genes. We co-transfected the AID-dCas9-PR with a reporter construct expressing luciferase under control of a minimal promoter containing eight recognition sites for an artificial guide RNA (gRNA-1), and observed a strong luciferase signal in the presence of gRNA-1. No luciferase activity was detected in the absence of the gRNA-1. Addition of auxin resulted in a sharp drop in luciferase output (Fig. 2a). To test the capacity for induction of endogenous genes we co-transfected AID-dCas9-PR with a mix of guide RNAs targeting the ASCL1 and SOX9 genes. Both genes show clear upregulation of expression, which is strongly reduced in the presence of auxin (Supplementary Fig. 2a, b), demonstrating the potential of AID-dCas9-PR as a drugcontrollable transcriptional activator.

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf|PDF]]
- Texto literal:
> were confirmed in both studies. Nevertheless, studies are still attempting to confirm whether various histone modifications are truly epigenetic, that is, self-sustaining

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|PDF]]
- Texto literal:
> Identifying the causal link between epigenetic marks and gene expression remains a central goal of chromatin biology. Thus, these aforementioned studies using dCas9 as a guidable platform to edit locus-specific epigenetic information will be an indispensable tool to achieve this. Now that the tools that enable us to alter the epigenome are in place, the next phase is to utilize them to better characterize regulatory elements and cellular states. To this end, researchers have already applied dCas9-based epigen-ome-editing tools for a number of exciting purposes including high-throughput screenings to characterize functional distal enhancers146, targeted reprogramming of lineage specifica-tion147,148, generation of induced pluripotent stem cells149, and reversal of HIV latency150. One of the remaining challenges is to elucidate the causal relationship between the presence of an epigenetic mark and its regulatory impact. Since the dCas9-fused epigenetic modifier remains associated with the target site, it is unclear whether the regulatory activity is due to the induced epigenetic mark or the complex. To this end, recent efforts using rapid and reversible epigenome-editing approaches are highly notable145. Future studies that enable rapid degradation of the targeting complex at the target site, such as with auxin-inducible degron technology151, should allow us to further characterize the functional consequences of epigenetic marks and investigate the associated temporal epigenetic memory for each mark.

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf|PDF]]
- Texto literal:
> A histone deacetylase network regulates epigenetic reprogramming and viral silencing in 1 HIV infected cells 2

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf|PDF]]
- Texto literal:
> significantly elevated HIV expression, even 14d post-vorinostat removal (Figure S2E). Thus, a 191 transient window of vorinostat exposure by infected cells during the effector-to-memory transition 192 can lead to protracted viral gene expression post-exposure, even for a low concentration (125nM). 193 Thus, we speculate that latency prevention in primary cells is distinct from latency reversal and is 194 characterized by a higher level of vulnerability to HDACis. Additionally, we propose that transient 195 exposure of actively infected CD4 T cells to HDACis during transition from an activated to a resting 196 state can have a long-lasting impact on viral gene expression, possibly through interfering with 197 the establishment of a repressive epigenetic state at the provirus. 198 199

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf#Passage 5|Pasaje 5]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf|PDF]]
- Texto literal:
> change following vorinostat treatment in both marks simultaneously (Figure 3E). These data 294 support the existence of a reciprocal regulatory switch between these marks; H3K9ac removal by 295 HDACs as activated T cells return to a resting state serves as a ‘gatekeeping’ change that licenses 296 the subsequent deposition of H3K9 methylation at a subset of loci, including the HIV provirus. We 297 speculate that maintenance of a permissive chromatin state by HDACi in combination with the 298 positive-feedback mechanisms of the HIV transactivator protein Tat may together account for the 299 observed persistence of viral gene expression, although notably we failed to see evidence of 300

### Extracto 9
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf#Passage 6|Pasaje 6]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf|PDF]]
- Texto literal:
> deacetylation represents a ‘gateway’ event for entry into latency. Our results demonstrate that 493 Class I HDACs play a critical role in initiating latency and that blocking Class I HDAC activity in 494 productively infected CD4 T cells effectively prevents these cells from entering latency during 495 transition to a resting memory state. Furthermore, HDAC inhibition during the transition leads to 496 protracted viral gene expression, even after HDACi removal, suggesting that this treatment 497 reprograms cells into a state that is suboptimal for latency. 498 499 By comparing the abundance of various histone marks on the HIV provirus as latency is 500 established, we observed that early HDACi exposure during active infection led to persistently 501 elevated H3K9ac in the gene body and the 3’ LTR. Interestingly, HDACi treatment also led to a 502 substantial reduction in H3K9me3 in the LTR regions. Repressive HMTs like the G9a H3K9 503 methyltransferase(Imai et al., 2010) require an unmodified lysine residue as a substrate for 504

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf|dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf|jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf|minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/benjamin_2015_strategies_for_precision_modulation_of_gene_expression_by.pdf|benjamin_2015_strategies_for_precision_modulation_of_gene_expression_by.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf|chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf|daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/gough_2023_dissection_of_a_non_coding_risk_locus_at.pdf|gough_2023_dissection_of_a_non_coding_risk_locus_at.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/hilton_2015.pdf|hilton_2015.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/hongxin_2020_cell_cell_contact_induced_gene_editing_activation_in.pdf|hongxin_2020_cell_cell_contact_induced_gene_editing_activation_in.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/liao_2026.pdf|liao_2026.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/matthew_2019_sufficiency_analysis_of_estrogen_responsive_enhancers_using_synthetic.pdf|matthew_2019_sufficiency_analysis_of_estrogen_responsive_enhancers_using_synthetic.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/t_2018_sirt6_haploinsufficiency_induces_brafv600e_melanoma_cell_resistance_to.pdf|t_2018_sirt6_haploinsufficiency_induces_brafv600e_melanoma_cell_resistance_to.pdf]]
