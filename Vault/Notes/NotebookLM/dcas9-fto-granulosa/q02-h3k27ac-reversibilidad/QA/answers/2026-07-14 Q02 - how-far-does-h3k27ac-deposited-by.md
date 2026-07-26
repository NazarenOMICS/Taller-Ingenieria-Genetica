---
type: reference
status: current
date: 2026-07-14
source: "notebooklm:dcas9-fto-granulosa/q02-h3k27ac-reversibilidad"
related:
  - "[[Notes/Dashboards/dCas9-p300 H3K27ac reversibility]]"
---

# Q02 - How far does the H3K27ac deposited by dCas9-p300 spread from the targeted site, according to these sources?

Based on the sources, the H3K27ac deposited by **dCas9-p300** is primarily described as being localized to the **targeted genomic sites**, though its regulatory reach can extend significantly through the three-dimensional organization of the genome.

### Localized Deposition
*   **Targeted Sites:** Sources characterize the deposition as occurring at "the corresponding genomic target sites"  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf#Passage 2|[1]]] or specifically at "target promoter sites"  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 1|[2]]]. It is used to induce "local H3K27ac levels" at enhancer elements  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 1|[3]]].
*   **Mimicking Endogenous Patterns:** The patterns of H3K27ac deposition by dCas9-p300 are noted to be **similar to those caused by endogenous inductions**, such as estrogen (E2) treatment, which typically produces defined peaks at specific binding sites  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/matthew_2019_sufficiency_analysis_of_estrogen_responsive_enhancers_using_synthetic.pdf#Passage 2|[4]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/gough_2023_dissection_of_a_non_coding_risk_locus_at.pdf#Passage 1|[5]]].

### Regional and Interacting Reach
*   **Hyper-acetylation of Regions:** One source indicates that dCas9-p300 may **"hyper-acetylate"** a targeted region  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/gough_2023_dissection_of_a_non_coding_risk_locus_at.pdf#Passage 6|[6]]]. This can lead to **non-specific regulatory effects** on other genes within that same neighborhood  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/gough_2023_dissection_of_a_non_coding_risk_locus_at.pdf#Passage 6|[6]]].
*   **Reach via Chromatin Looping:** Because dCas9-p300 is a direct histone acetylase, its activity at a target locus can influence distal genes that are physically brought into proximity through **chromatin looping**  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/gough_2023_dissection_of_a_non_coding_risk_locus_at.pdf#Passage 6|[6]]]. 
*   **Distance of Effect:** In a study of the 1p36.23 risk locus, targeting dCas9-p300 to an enhancer resulted in the upregulation of genes located approximately **200 kb upstream** (such as *TNFRSF9* and *PARK7*), likely because these genes interact with the target site via chromatin loops  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/gough_2023_dissection_of_a_non_coding_risk_locus_at.pdf#Passage 6|[6]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/gough_2023_dissection_of_a_non_coding_risk_locus_at.pdf#Passage 7|[7]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 2|[8]]].

### Comparison to Other Modifiers
The sources contrast the reach of p300 with modifiers like **dCas9-KRAB**, which is explicitly associated with **"spreading"** repressive marks (like H3K9me3) across **tens of kilobases** through self-reinforcing mechanisms  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 3|[9]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/matthew_2019_sufficiency_analysis_of_estrogen_responsive_enhancers_using_synthetic.pdf#Passage 6|[10]]]. While p300 can affect distant loci, the sources suggest this occurs primarily through pre-existing topological interactions rather than linear spreading along the DNA strand  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/gough_2023_dissection_of_a_non_coding_risk_locus_at.pdf#Passage 6|[6]]].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf|PDF]]
- Texto literal:
> Manipulating the epigenome and gene expression using TEMs and TTFs So far only a few studies have been published reporting the use of dCas9 fusions for epigenome editing and manipulating gene expression. The catalytic histone acetyltransferase (HAT) core domain p300 has been used to catalyse acetylation of histones in human HEK293T cells (Hilton et al., 2015). Targeting dCas9–p300 fusions to promoter regions or proximal or distant enhancers caused activation of gene expression. Increased expression upon enhancer-targeting was concomitant with enrichment in H3K27ac at the correspond- ing genomic target sites (Hilton et al., 2015). In most cases the same genes could be transactivated by dCas9-VP64 when targeted at promoters. To achieve transactivation both effectors can thus be used. The two effectors behave somewhat differently in terms of their impact on histone acetylation state, as p300 directly catalyses H3K27ac (Ogryzko et al., 1996; Delvecchio et al., 2013), whereas VP64 recruits subsequent transactivation components, amongst which is p300 (Memedula and Belmont, 2003). Also the histone acetyltransferase domain of the CREB-binding protein has been fused to dCas9 (dCas9-CBPHAT) and has been used to catalyse locus-specific acetylation of histones (Cheng et al., 2016). dCas9-CBPHAT was targeted using the Casilio (CRISPR/Cas9-Pumilio) system, which harbours an scRNA containing multiple PUF binding sites (PBS), to recruit additional CBPHAT domains via fusions with Pumilio/FBF (PUF) RNA-binding domains. Similar to dCas9-p300, targeting dCas9-CBPHAT to promoters or proximal and distal enhancer

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf|PDF]]
- Texto literal:
> proved functional or biochemical specificity have been explored. One key strategy is to truncate chromatinmodifying enzymes to their catalytic core domains. A notable recent example involved the human co-activator protein p300, which functions as a histone acetyltransferase and mediates interactions with multiple transcription

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|PDF]]
- Texto literal:
> is to locally deposit H3K27ac marks. Therefore, in contrast to the local reduction of enhancer marks by dCas9-LSD1, recruitment of histone acetyl transferase P300 through dCas9 fusion (dCas9-P300) resulted in a significant increase in local H3K27ac levels at enhancer elements142. Importantly, unlike other dCas9-fused transactivators, which can result in induction of gene expression primarily from promoter regions, targeting dCas9-P300 allows significant gene expression induction from both promoter and enhancer regions142. Researchers have also exploited other epigenetic modifiers to manipulate additional epigenetic marks. Among these, dCas9 fusion to the PRDM9 methyltransferase fusion complex has been utilized to manipulate local H3K4me3 marks143. Notably, local induction of H3K4me3, which is a marker of active promoters, was observed to be sufficient to allow re-expression of silenced target genes in various cell types143. Histone de-acetylation has been another strategy to locally manipulate chromatin structure and function. To this end, dCas9 fusion to histone deacetylases (HDAC), specifically full-length HDAC3, has been shown to effectively reduce the H3k27ac at the target loci and reduce the gene expression of the target loci144.

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/matthew_2019_sufficiency_analysis_of_estrogen_responsive_enhancers_using_synthetic.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/matthew_2019_sufficiency_analysis_of_estrogen_responsive_enhancers_using_synthetic.pdf|PDF]]
- Texto literal:
> fusions were able to cause H3K27ac at targeted sites. For 18 of 19 targeted loci, we observed increased H3K27ac (Figs 2C and D, and S2C–G). Notably, at HES2-1 and HES2-3, there is significant baseline H3K27ac present, possibly because of the binding of other TFs to these sites (Table S2). For ERBSs, the patterns of acetylation are similar to E2-induced H3K27ac (Figs 2E and F, and S2D and E). We observed similar fold changes in H3K27ac when using dCas9-VP16(10x) and when using dCas9-p300(core) targeted to ERBSs

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/gough_2023_dissection_of_a_non_coding_risk_locus_at.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/gough_2023_dissection_of_a_non_coding_risk_locus_at.pdf|PDF]]
- Texto literal:
> is a direct histone acetylase. As previous Capture Hi-C data shows a clear interaction between 244

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/gough_2023_dissection_of_a_non_coding_risk_locus_at.pdf#Passage 7|Pasaje 7]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/gough_2023_dissection_of_a_non_coding_risk_locus_at.pdf|PDF]]
- Texto literal:
> (46, 47), and PARK7 has potentially important roles in cell cycle control and oxidative stress 131

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf|PDF]]
- Texto literal:
> successfully to perturb chromatin structure and these studies suggest that continued work in this area could reveal important and potentially useful regulatory principles relating to chromatin shape. For example, an ectopic repressor assay using a drug-inducible ZF-KRAB fusion protein demonstrated that KRAB-mediated repression spans tens of kilobases and is established by the longrange propagation of H3K9me3 and HP1 β [119]. This and similar approaches [38, 81] provide us with the unique ability to regulate multiple genes in tandem using a single regulator. Furthermore, transcriptional activators and repressors that are recruited site-specifically to regions more than 1 kb downstream of promoters can activate [120] and repress [121] yeast genes, respectively, when they are placed near telomeres. This effect “at a distance” is mediated by a telomere-position effect in yeast, which is analogous to the position effect variegation

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf|PDF]]
- Texto literal:
> 115. Van Bortle K, Corces VG. Nuclear organization and genome function. Annu Rev Cell Dev Biol. 2012;28:163–87.

### Extracto 9
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/matthew_2019_sufficiency_analysis_of_estrogen_responsive_enhancers_using_synthetic.pdf#Passage 6|Pasaje 6]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/matthew_2019_sufficiency_analysis_of_estrogen_responsive_enhancers_using_synthetic.pdf|PDF]]
- Texto literal:
> especially dCas9-p300(core). The contrast in how ERBSs combine to regulate transcription in the two experimental approaches suggests that the synergy between ERBSs likely occurs in cis, where the recruitment of ER and its cofactors, such as histone acetyltransferases (Hanstein et al, 1996; Shang et al, 2000), is synergistic between ERBSs. However, if the cofactors are directly recruited to the ERBSs, as is the case with CRISPRa, then synergy no longer occurs. In this model, synergy occurs when ERBSs influence one another before activation. Then, once ERBSs are activated through the binding of TFs and cofactors, ERBSs communicate with the target gene independently. There are important caveats to consider when using these synthetic activators, including the possible recruitment of cofactors that do not normally bind to a particular enhancer or potential interference with TF binding by dCas9. However, we believe that the comparison between enhancer activation and Enhancer-i has shed light on the consistent importance of individual sites as well as a key difference in how enhancers work together when bound by different transcriptional activators.

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf|daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/gough_2023_dissection_of_a_non_coding_risk_locus_at.pdf|gough_2023_dissection_of_a_non_coding_risk_locus_at.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/matthew_2019_sufficiency_analysis_of_estrogen_responsive_enhancers_using_synthetic.pdf|matthew_2019_sufficiency_analysis_of_estrogen_responsive_enhancers_using_synthetic.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf|minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/benjamin_2015_strategies_for_precision_modulation_of_gene_expression_by.pdf|benjamin_2015_strategies_for_precision_modulation_of_gene_expression_by.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf|chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf|dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/hongxin_2020_cell_cell_contact_induced_gene_editing_activation_in.pdf|hongxin_2020_cell_cell_contact_induced_gene_editing_activation_in.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf|jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/t_2018_sirt6_haploinsufficiency_induces_brafv600e_melanoma_cell_resistance_to.pdf|t_2018_sirt6_haploinsufficiency_induces_brafv600e_melanoma_cell_resistance_to.pdf]]
