---
type: reference
status: current
date: 2026-07-14
source: "notebooklm:dcas9-fto-granulosa/q02-h3k27ac-reversibilidad"
related:
  - "[[Notes/Dashboards/dCas9-p300 H3K27ac reversibility]]"
---

# Q06 - What gaps or limitations remain in these sources regarding quantitative kinetics of H3K27ac persistence and decay after dCas9-p300 withdrawal?

While the sources describe sophisticated tools for controlling the timing of **dCas9-p300** activity, they highlight several significant gaps and limitations regarding the specific **quantitative kinetics of H3K27ac persistence and decay** once the effector is withdrawn.

### 1. Lack of Granular Decay Curves for the Histone Mark
The most prominent gap is the absence of high-resolution time-course data specifically for the H3K27ac mark itself following effector removal.
*   **Protein vs. Mark Kinetics:** While sources provide precise half-life measurements for the **dCas9 protein** (e.g., a half-life of less than 15 minutes and total clearance within 1–2 hours in AID systems  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 2|[1]]]), they do not provide a corresponding numerical half-life for the **histone mark** it deposits  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 1|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf#Passage 7|[3]]]. 
*   **Broad Measurement Windows:** Transcriptional effects are often measured at broad intervals, such as 48 hours post-withdrawal, where activation is described as "largely abrogated"  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 10|[4]]]. This lacks the granularity needed to determine if the H3K27ac mark decays within minutes, hours, or many cell cycles.

### 2. The "Complex vs. Mark" Causality Gap
The sources identify a fundamental experimental challenge in distinguishing whether the observed gene activation is sustained by the **epigenetic mark** or the physical presence of the **dCas9-fusion complex**  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 1|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 5|[5]]].
*   **Occupancy Limitations:** Because the synthetic "writer" remains associated with the target site during activation, it is currently "unclear whether the regulatory activity is due to the induced epigenetic mark or the complex"  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 1|[2]]]. 
*   **Requirement for Maintenance:** One source suggests that the persistence of a mark likely requires ongoing recruitment of the writer to counteract continuous endogenous "eraser" activity (HDACs), but the exact equilibrium and decay rates of this "writer-eraser" tug-of-war are not quantitatively defined  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 5|[5]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 10|[6]]].

### 3. Missing Comparative Kinetics (mRNA vs. Mark)
There is a lack of quantitative data comparing the **rate of transcript decay** (mRNA half-life) to the **rate of H3K27ac decay** at the same locus. 
*   **Functional Lag:** The sources do not establish if there is a temporal lag between the removal of the acetyl mark and the return of transcription to baseline  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 11|[7]]].
*   **Predictive Power:** Research suggests that H3K27ac levels at distal enhancers are not fully predictive of target gene activation levels, further complicating the ability to model decay kinetics based on transcriptional readouts alone  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 9|[8]]].

### 4. Contextual Variability and "Eraser" Dynamics
The sources acknowledge that decay rates likely depend on the **local chromatin environment** and endogenous enzyme concentrations, yet these variables are not fully quantified.
*   **Passive vs. Active Decay:** The relative contribution of **passive dilution** (via cell division) versus **active erasure** (via endogenous HDACs) in decaying synthetic acetylation marks remains largely untested  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 6|[9]]].
*   **Cell-Type Specificity:** Differences in degradation efficiency have been observed between cell lines (e.g., HEK293 vs. CHO cells), suggesting that the "rules" of epigenetic decay may vary significantly across biological contexts in ways that are currently unpredictable [10, 11].

### 5. Identification of "Short-Term" Memory Mechanisms
The sources characterize histone deacetylation (the reversal of p300 activity) as a mechanism with **"no memory,"** but they note that many other histone modifications have yet to be rigorously tested for their epigenetic properties or "temporal epigenetic memory" using these new tools  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf#Passage 7|[3]]]. Identifying which specific marks provide "flexible" versus "permanent" memory is cited as a key area for future research  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 6|[9]]].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|PDF]]
- Texto literal:
> Identifying the causal link between epigenetic marks and gene expression remains a central goal of chromatin biology. Thus, these aforementioned studies using dCas9 as a guidable platform to edit locus-specific epigenetic information will be an indispensable tool to achieve this. Now that the tools that enable us to alter the epigenome are in place, the next phase is to utilize them to better characterize regulatory elements and cellular states. To this end, researchers have already applied dCas9-based epigen-ome-editing tools for a number of exciting purposes including high-throughput screenings to characterize functional distal enhancers146, targeted reprogramming of lineage specifica-tion147,148, generation of induced pluripotent stem cells149, and reversal of HIV latency150. One of the remaining challenges is to elucidate the causal relationship between the presence of an epigenetic mark and its regulatory impact. Since the dCas9-fused epigenetic modifier remains associated with the target site, it is unclear whether the regulatory activity is due to the induced epigenetic mark or the complex. To this end, recent efforts using rapid and reversible epigenome-editing approaches are highly notable145. Future studies that enable rapid degradation of the targeting complex at the target site, such as with auxin-inducible degron technology151, should allow us to further characterize the functional consequences of epigenetic marks and investigate the associated temporal epigenetic memory for each mark.

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf|PDF]]
- Texto literal:
> proved functional or biochemical specificity have been explored. One key strategy is to truncate chromatinmodifying enzymes to their catalytic core domains. A notable recent example involved the human co-activator protein p300, which functions as a histone acetyltransferase and mediates interactions with multiple transcription

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf#Passage 7|Pasaje 7]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf|PDF]]
- Texto literal:
> Thus, the fraction of proviruses that lack robust histone 513 methylation, i.e., those that are not “fully silenced” or in “deep latency” will be most responsive to 514 HDACi when used as an LRA. Consistent with this model, longer durations or repeated exposure 515 to HDACi can catch more proviruses in an inducible state(Archin et al., 2017; Shan et al., 2014) 516 likely by tipping the equilibrium towards active proviral gene expression. By contrast, in 517 productively infected activated CD4 T cells, histone acetylation, both globally and at the provirus, 518 is high but is undergoing rapid acetyl group removal by HDACs, leading to a higher sensitivity to 519 HDACis.

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 10|Pasaje 10]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf|PDF]]
- Texto literal:
> Rapid advances in targeted epigenome editors Cells use a system of chromatin effectors and associated histone and DNA modifications to modulate and establish gene-expression states. A central goal has been to try to link these modifications to specific functional roles, such as transcriptional activation and repression [2, 3, 13]. To date, our knowledge of chromatin-effector functions has largely derived from the pharmacological inhibition or genetic knockout of histone-modifying enzymes. More recently, precise and comprehensive genome-wide maps of chromatin modifications have been generated, mapped to transcriptomes, and used to provide further correlative evidence for chromatin functions [14]. Nevertheless, these two approaches—genome-wide perturbations and mapping analyses—neither account for potential pleiotropic effects nor directly demonstrate causal

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 5|Pasaje 5]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf|PDF]]
- Texto literal:
> of epigenetic regulation lie ahead. Researchers could work to harness any potential restricted or conditional epigenetic inheritance of histone modifications for developing “short-term” or “flexible” epigenetic memory circuitry [99], which could be intentionally designed to maintain the edited epigenome state for a short period of time. For example, there may be instances, in normal development or for transient therapeutic applications, that require that genes are regulated such that they are suppressed for a short period of time and subsequently reactivated. The repressive state of a gene could be induced with repressive histone methyltransferases and later (before one cell cycle is completed or within very few cell divisions) reversed by either demethylases or a passive histone dilution mechanism. By contrast, complete and permanent repression of genes could be achieved with the incorporation of DNA-methylation-mediated gene silencing [25, 56]. It is important to note that there is evidence to suggest that transiently induced DNA methylation is not maintained, highlighting the

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 10|Pasaje 10]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf|PDF]]
- Texto literal:
> Orthogonal, auxin degradable dCas9 variants. Natural gene networks often rely on fast switching interactions of multiple transcriptional activators, repressors and other chromatin modifying factors with cohorts of responsive target promoters. To enable recreation of such behaviours in artificial systems, allowing rapid and diverse, independently controllable functional activity, we sought to expand our system by developing a set of orthogonal, auxin-degradable synthetic transcription factors. We first replaced the S. pyogenes dCas9 cDNA in our AID vector with a small multiple cloning site upstream of an HA-tag, into which we inserted several alternative, orthogonal CRISPR effector proteins (S. thermophiles 1 dCas9, S. aureus dCas9, A.s Cpf1, L.b Cpf1 and F.n Cpf1)15, 16. Western blots of HEK293 and CHO-K1 cells transfected with this set revealed the auxin induced degradation potential of these orthogonal AID-tagged factors (Supplementary Fig. 4a, b). Remarkably the AID-Cpf1 factors showed a clear difference in response to the drug between the cell lines. Although the reason is presently unclear, this could be due to differences in the expression levels of some auxiliary factors (e.g., SCF complex subunits) in combination with reduced accessibility of the IAA17

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 11|Pasaje 11]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf|PDF]]
- Texto literal:
> (Supplementary Fig. 5a). We first attached the ecDDD to S. pyogenes dCas9. Though some residual protein was detectable by Western blot, stability of the fusion protein was greatly improved by addition of TMP (Supplementary Fig. 5b). Next we constructed ecDDD tagged versions of the set of orthogonal dCas9 or Cpf1 proteins (S. thermophiles 1 dCas9, S. aureus dCas9, As.Cpf1, Lb.Cpf1 and Fn.Cpf1). With the exception of a moderate effect on SadCas9, the addition of the ecDDD degron did not appear to affect the stability of the set of orthogonal Cas9 or Cpf1 proteins when transfected in HEK293FT cells (Supplementary Fig. 5c). To investigate whether cell-type specific characteristics would affect degradation efficiency we next tested the effect of the degron-tag in CHO-K1 cells. CHO cells are an important resource in the biotechnology industry and a valuable target for systems that enable the drug controlled manipulation of gene expression output17. Interestingly the sensitivity of our panel of degrontagged Cas9 or Cpf1 proteins to proteosomal degradation is markedly enhanced in CHO cells compared with 293 cells, showing a clear difference in drug dependent stability of the fusion proteins for most of the constructs in both the AID and ecDDD degron tagged sets (Supplementary Fig. 5d).

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 6|Pasaje 6]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf|PDF]]
- Texto literal:
> importance of multivalent deposition of functionally related epigenetic marks for truly stable reprogramming [57]. Either short-term or long-term epigenetic memory could be a valuable feature of many applications, including gene and cell therapy. Finally, while the epigenetic maintenance of chromatin and gene expression states has been demonstrated in several cellular systems, exciting but challenging work lies ahead in using epigenome editing tools to study the long-term heritability of chromatin modifications (such as DNA methylation [92, 98]) across generations of complex organisms such as mice.

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
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/hongxin_2020_cell_cell_contact_induced_gene_editing_activation_in.pdf|hongxin_2020_cell_cell_contact_induced_gene_editing_activation_in.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/matthew_2019_sufficiency_analysis_of_estrogen_responsive_enhancers_using_synthetic.pdf|matthew_2019_sufficiency_analysis_of_estrogen_responsive_enhancers_using_synthetic.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/t_2018_sirt6_haploinsufficiency_induces_brafv600e_melanoma_cell_resistance_to.pdf|t_2018_sirt6_haploinsufficiency_induces_brafv600e_melanoma_cell_resistance_to.pdf]]
