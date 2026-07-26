---
type: reference
status: current
date: 2026-07-14
source: "notebooklm:dcas9-fto-granulosa/q11-controles-experimentales"
related:
  - "[[Notes/Dashboards/CRISPRa experimental controls]]"
---

# Q02 - According to these sources, what role does a catalytically dead/inactive effector domain (e.g., dead p300 core, dead VP64) play as a control in distinguishing genuine epigenetic activation from non-specific effects?

In CRISPRa and epigenome editing experiments, a **catalytically dead or inactive effector domain** (such as a dead p300 core or dead TET1 catalytic domain) serves as a critical control to prove that observed gene activation is specifically caused by the **enzymatic activity** of the effector and not by the mere physical binding of the dCas9 complex to the target locus  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 2|[2]]].

According to the sources, these inactive controls play the following specific roles:

### 1. Distinguishing Catalytic Activity from Physical Binding
The primary role of an inactive effector is to demonstrate that the epigenetic changes (e.g., histone acetylation or DNA demethylation) are the direct result of the effector’s enzymatic function. 
*   **p300 Core:** Researchers used a catalytic inactive mutant of the p300 catalytic domain (**p300CD D1398Y**) to show that the activation of the *Foxp3* gene was strictly dependent on p300’s **autoacetylation activity**  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 2|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 3|[3]]]. The inactive mutant failed to induce the small but significant fraction of endogenous *Foxp3* expression observed with the wild-type p300 core  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 2|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 4|[4]]].
*   **TET1 Domain:** Similarly, inactive mutants of the TET1 catalytic domain (**TET1CD H1620Y** and **D1622A**) were used to confirm that DNA demethylation at the *Foxp3* CNS2 locus was dependent on **TET enzyme activity**  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 3|[3]]].

### 2. Identifying Non-Specific Steric Interference (CRISPRi Effects)
The use of dead effectors helps researchers identify unintended negative effects on transcription caused by the dCas9 protein itself. The sources note that dCas9 can physically block the transcriptional apparatus, a process used intentionally in CRISPR interference (CRISPRi)  [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/albert_2013_multiplexed_activation_of_endogenous_genes_by_crispr_on.pdf#Passage 1|[5]]]. 
*   In one study, the **TET1CD catalytic inactive mutant** actually decreased *Foxp3* expression, revealing that the dCas9-effector complex can have a **negative/repressive effect** on transcription simply by remaining at the targeted locus and impeding the interaction of endogenous transcription factors [6].
*   Comparing the active effector to this inactive baseline allows researchers to measure the "net" activation after accounting for this inherent binding interference [6].

### 3. Proving Necessity of the Effector for the Phenotype
Inactive controls establish that the dCas9-DNA binding event alone is insufficient to produce the desired biological outcome.
*   Experiments targeting the *MSI1* gene showed that while dCas9 fused to an activation domain (VP48) induced expression, **dCas9 lacking an activation domain** entirely failed to activate the gene [7].
*   This confirms that the recruitment of the transcriptional machinery or the modification of the chromatin state—rather than just the localization of the dCas9 protein—is the driver of the genuine epigenetic activation [7, 8].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q11-controles-experimentales/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|PDF]]
- Texto literal:
> DNMT3a to the CNS2 locus after stimulation, leading to Foxp3 loss even in nTregs [46]. We speculated that dCas9-TET1CD targeted to the CNS2 locus competes with methyltransferases under inflammatory conditions, resulting in earlier loss of demethylation function than under iTreg conditions. In fact, Foxp3 mean fluorescence intensity (MFI) was greater in dCas9-TET1CD than in TET1CD catalytic inactive mutant under iTreg conditions (Fig. 3c), but was weakened by inflammatory stimuli.

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q11-controles-experimentales/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|PDF]]
- Texto literal:
> Statistical analysis All values are presented as the means ± standard devia- tions (SDs). Unpaired Student’s t tests were used, and p < 0.05 was defined as statistically significant.

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q11-controles-experimentales/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|PDF]]
- Texto literal:
> Then, we examined the maintenance of Foxp3 by dCas9-p300CD in iTregs. The stability of Foxp3 under inflammatory cytokines was investigated (same as Addi-tional file 3: Figure S1). We observed that iTregs cotransduced with dCas9-p300CD and #P-4 retained a high amount of Foxp3 compared with #P-3 under inflammatory conditions (Fig. 6a). We confirmed this maintenance is actually dependent on p300CD autoacetylation activity by co-transduction with p300 catalytic inactive mutant (Fig. 6b). Moreover, the Treg signature genes CD25 and CTLA-4 were slightly but significantly upregulated under IL-12 conditions in #P-4 transduced iTregs (Fig. 6c). Finally, we examined the iTreg suppression activity in vitro. iTregs co-transduced with dCas9-p300CD and gRNA were sorted (Additional file 3: Figure S4a). Splenic DCs were used as antigen-presenting cells, and the proliferation of effector T cells was further suppressed by #P-4 transduced iTregs, which correlated with Foxp3 stabilization (Fig. 6d). Similar tendency was observed in comparison with catalytic activity (Additional file 3: Figure S4b). These data showed that applying dCas9-p300CD to primary T cells, especially iTregs, could modify both transcription and cell function. These data also clarified one aspect of the Foxp3 transcriptional activation mechanisms (Fig. 7b).

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/albert_2013_multiplexed_activation_of_endogenous_genes_by_crispr_on.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q11-controles-experimentales/albert_2013_multiplexed_activation_of_endogenous_genes_by_crispr_on.pdf|PDF]]
- Texto literal:
> We tested whether CRISPR-on can activate a sin-gle-copy transgene in mouse embryonic stem cells (mESCs). For this, dCas9VP48 was co-transfected with sgTetO into KH2MSI1 ESCs carrying a Tet- inducible Musashi1 (MSI1) transgene at the Col1A1 locus and the rtTA-M2 in the Rosa26 locus [23] (Supplementary information, Figure S3). Transient transfection of dCas9VP48 alone did not activate MSI1 expression (Supplementary information, Figure S3 Lane 1), while co-transfection of dCas9VP48 with sgTetO or addition of doxycycline (positive control) activated MSI1 expression (Supplementary information, Figure S3 Lane 2 and 7). Neither expression of dCas9VP48 with a mutant TetO sgRNA (sgTetO-mut) carrying mismatches to the TetO binding sites (Supplementary information, Figure S3 Lane 3) nor expression of sgTetO with dCas9 lacking an activation domain activated MSI1 expression (Supplementary information, Figure S3 Lane 4).

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/albert_2013_multiplexed_activation_of_endogenous_genes_by_crispr_on.pdf|albert_2013_multiplexed_activation_of_endogenous_genes_by_crispr_on.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf|masahiro_2017_stabilization_of_foxp3_expression_by_crispr_dcas9_based.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/charleen_2021_tissue_specific_activation_of_gene_expression_by_the.pdf|charleen_2021_tissue_specific_activation_of_gene_expression_by_the.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/hongyi_2020_applications_of_genome_editing_technology_in_the_targeted.pdf|hongyi_2020_applications_of_genome_editing_technology_in_the_targeted.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf|joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/josh_2019_mitigation_of_off_target_toxicity_in_crispr_cas9.pdf|josh_2019_mitigation_of_off_target_toxicity_in_crispr_cas9.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/karthik_2021_cancer_immune_evasion_through_loss_of_mhc_class.pdf|karthik_2021_cancer_immune_evasion_through_loss_of_mhc_class.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/kendall_2018_up_down_and_out_optimized_libraries_for_crispra.pdf|kendall_2018_up_down_and_out_optimized_libraries_for_crispra.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/kohei_2021_comparative_analysis_and_rational_design_of_dcas9_vp64.pdf|kohei_2021_comparative_analysis_and_rational_design_of_dcas9_vp64.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/leena_2017_gene_editing_and_crop_improvement_using_crispr_cas9.pdf|leena_2017_gene_editing_and_crop_improvement_using_crispr_cas9.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/lesca_2016_circular_non_coding_rna_anril_modulates_ribosomal_rna.pdf|lesca_2016_circular_non_coding_rna_anril_modulates_ribosomal_rna.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/rachel_2018_plant_growth_promoting_rhizobacteria_context_mechanisms_of_action.pdf|rachel_2018_plant_growth_promoting_rhizobacteria_context_mechanisms_of_action.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/sarah_2025_epigenetic_motifs_distinguishing_endogenous_from_exogenous_retroviral_integrants.pdf|sarah_2025_epigenetic_motifs_distinguishing_endogenous_from_exogenous_retroviral_integrants.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/simon_2017_rapid_and_reversible_epigenome_editing_by_endogenous_chromatin.pdf|simon_2017_rapid_and_reversible_epigenome_editing_by_endogenous_chromatin.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/vidisha_2013_long_noncoding_rna_malat1_controls_cell_cycle_progression.pdf|vidisha_2013_long_noncoding_rna_malat1_controls_cell_cycle_progression.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q11-controles-experimentales/Sources/yang_2019_engineered_crispra_enables_programmable_eukaryote_like_gene_activation.pdf|yang_2019_engineered_crispra_enables_programmable_eukaryote_like_gene_activation.pdf]]
