---
type: reference
status: current
date: 2026-07-14
source: "notebooklm:dcas9-fto-granulosa/q13-riesgo-desregulacion-fto"
related:
  - "[[Notes/Dashboards/FTO dysregulation risk]]"
---

# Q03 - According to these sources (e.g., orthogonal control of mean and variability of endogenous gene expression), what strategies exist for titrating or dose-controlling CRISPRa-driven gene activation to stay within a physiological range rather than supraphysiological overexpression?

Based on the sources, several strategies exist for titrating or dose-controlling CRISPRa (CRISPR activation) to maintain endogenous gene expression within a **physiological range** and avoid the risks associated with supraphysiological overexpression.

### **1. The Tunable Noise Rheostat (TuNR) System**
The most advanced strategy described for precise titration is the **Tunable Noise Rheostat (TuNR)**, a synthetic circuit designed to independently control both the **mean expression** and the **variability (noise)** of a gene  [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 2|[2]]]. 
*   **Mechanism:** TuNR utilizes a serial cascade of two orthogonal, inducible transcriptional activators  [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 2|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 3|[3]]]. The first node is induced by **abscisic acid (ABA)**, which then drives the production of a second system (dCas9-activator) induced by **gibberellic acid (GA)**  [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 3|[3]]].
*   **Precision Titration:** By tuning the concentrations of these two small molecule inputs, researchers can achieve a **smooth continuum of expression values**  [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 4|[4]]]. This allows for the selection of specific "isomeans"—combinations of inducers that produce the same average level of expression but with different population distributions  [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 5|[5]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 6|[6]]].
*   **Modest Induction:** Unlike transgenes that can be induced over 1000-fold, TuNR applied to endogenous loci (like *NGFR* or *CXCR4*) achieved more modest, physiologically relevant increases of **3.4-fold to 7.2-fold**, comparable to endogenous human promoters  [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 2|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 7|[7]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 8|[8]]].

### **2. Inducible Promoters and Small-Molecule Titration**
Using inducible systems (e.g., **Tet-on** or **Dox-inducible**) allows for both temporal and dosage control over the dCas9-activator components  [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/julie_2023_crispri_gene_modulation_and_all_optical_electrophysiology_in.pdf#Passage 1|[9]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/julie_2023_crispri_gene_modulation_and_all_optical_electrophysiology_in.pdf#Passage 2|[10]]].
*   **Temporal Resolution:** Inducible systems allow gene activation to be turned "on" or "off" at specific times, which is critical for studying essential genes or developmental processes without causing permanent genotoxicity  [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/julie_2023_crispri_gene_modulation_and_all_optical_electrophysiology_in.pdf#Passage 1|[9]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 9|[11]]].
*   **Leakiness Control:** Serial arrangements (like TuNR) significantly reduce **basal leakiness**—the unintended expression of a gene in the absence of an inducer—by acting as a "coincidence detector" requiring two separate inputs for full activation  [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 4|[4]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 7|[7]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/julie_2023_gene_modulation_with_crispr_based_tools_in_human.pdf#Passage 1|[12]]].

### **3. Strategic Selection of Effector Domains**
The sources highlight that the choice of the transcriptional activator fused to dCas9 determines the potential range of activation:
*   **Potency Hierarchy:** First-generation activators like **VP64** typically yield modest activation  [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/julie_2023_gene_modulation_with_crispr_based_tools_in_human.pdf#Passage 2|[13]]]. More potent hybrid effectors, such as **VPR** (VP64-p65-Rta) or **SAM** (Synergistic Activation Mediator), can drive much higher levels of expression  [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 10|[14]]].
*   **Physiological Alignment:** For remaining within a physiological range, less potent effectors or modified versions like **SunTag** (which recruits multiple activators to a single dCas9) can be utilized to reach specific thresholds  [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 10|[14]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/yibing_2025_brain_targeted_nano_delivery_system_for_crispra_mediated.pdf#Passage 1|[15]]].

### **4. Guide RNA (gRNA) Design and Positioning**
The efficacy of CRISPRa is highly dependent on where the gRNA targets the promoter region relative to the **Transcription Start Site (TSS)**.
*   **Targeting Window:** Optimal activation is generally achieved by targeting a narrow window approximately **-400 to -50 bp upstream of the TSS**  [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/julie_2023_gene_modulation_with_crispr_based_tools_in_human.pdf#Passage 3|[16]]]. 
*   **Screening for Modesty:** Researchers can design and test a panel of gRNAs to identify those that provide **modest, stable activation** rather than maximal induction  [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/julie_2023_gene_modulation_with_crispr_based_tools_in_human.pdf#Passage 4|[17]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/yibing_2025_brain_targeted_nano_delivery_system_for_crispra_mediated.pdf#Passage 2|[18]]]. Proximity to the TSS serves as a predictor for efficiency, allowing researchers to "dial in" the desired level of activation by shifting the target site  [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/julie_2023_gene_modulation_with_crispr_based_tools_in_human.pdf#Passage 4|[17]]].

### **5. Endogenous Locus Activation vs. cDNA Overexpression**
A fundamental strategy for staying within a physiological range is the inherent nature of CRISPRa itself, which activates the **endogenous gene** rather than introducing exogenous cDNA  [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/yibing_2025_brain_targeted_nano_delivery_system_for_crispra_mediated.pdf#Passage 3|[19]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/yibing_2025_brain_targeted_nano_delivery_system_for_crispra_mediated.pdf#Passage 4|[20]]].
*   **Regulatory Integrity:** Because CRISPRa enhances transcription at the native genomic locus, it preserves the gene's **natural regulatory network**, including proper alternative splicing and post-translational modifications  [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/yibing_2025_brain_targeted_nano_delivery_system_for_crispra_mediated.pdf#Passage 3|[19]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/yibing_2025_brain_targeted_nano_delivery_system_for_crispra_mediated.pdf#Passage 4|[20]]]. 
*   **Reduced Aggregation Risk:** This approach minimizes the risk of **abnormal protein aggregation** or misfolding that often occurs with unregulated supraphysiological overexpression from viral or plasmid vectors  [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/yibing_2025_brain_targeted_nano_delivery_system_for_crispra_mediated.pdf#Passage 3|[19]]].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf|PDF]]
- Texto literal:
> expression and heterogeneity of transgenes and endogenous human genes. The circuit, a

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf|PDF]]
- Texto literal:
> looked to an earlier synthetic circuit that utilized a serial orientation of independent inducible transcription factors to decouple mean expression from variability34.

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf|PDF]]
- Texto literal:
> Results Characterization of a serial circuit topology with two inducible transcriptional activators. We built TuNR as a serial connection of two inducible transcriptional activation systems, where the upstream system (first node) controls production of the downstream system (second node) (Fig. 1A and Supplementary Fig. 1A). The first node consists of a Gal4 DNA-binding domain fused to half of a split abscisic acid (ABA)-binding domain, which, in the presence of ABA, assembles with its cognate heterodimer fused to a VP-16 activation domain35,36. The recruitment of the ABA-reconstituted gene product of the first node to the upstream activating sequence minimal promoter drives the expression of the second inducible system and an mRuby as a reporter for transcription at this node of the cascade. The second node consists of a Staphylococcus pyogenes nuclease-dead Cas9 (dCas9) N-terminally fused to half of a gibberellic acid (GA)-binding domain and a VPR (p65, VP65, Rta) activation domain appended to the other half of the GA binding domain. In the presence of GA, these two proteins dimerize and, upon the concomitant expression of a target guide RNA (gRNA), are able to induce expression of the gene of interest (Fig. 1A). We identified ABA and GA as small molecule inducers of choice due to their previous vetting in other mammalian systems, reversibility of cognate protein dimerization, and the independence of each heterodimerization event35–37. Moreover, we chose dCas9 as the final node of TuNR for its modularity in targeting any locus with an appropriate protospacer adjacent motif.

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 5|Pasaje 5]] | [[Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf|PDF]]
- Texto literal:
> To quantify the total noise for every combination of ABA and GA, we utilized a common noise decomposition strategy to ascertain the extrinsic and intrinsic contributions to the expression noise as shown previously8. In this analysis, the correlated expression between the two terminal fluorophores represents the extrinsic noise, or cell-to-cell variability, whereas the uncorrelated

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 6|Pasaje 6]] | [[Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf|PDF]]
- Texto literal:
> produce cellular populations with distinct means and variances in a manner consistent with transgene regulation.

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 7|Pasaje 7]] | [[Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf|PDF]]
- Texto literal:
> TuNR achieved 7.2-fold mean induction for NGFR and 3.4-fold induction for CXCR4 and (Fig. 3C, D), which are levels comparable to what other systems have achieved with CRISPRa47,48. In addition, as observed in modulating mAzami-Green, TuNR showed a negligible effect on basal levels of NGFR and CXCR4 (Fig. 3C, D), demonstrating that TuNR minimally perturbs basal gene expression due to its serial topology.

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 8|Pasaje 8]] | [[Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf|PDF]]
- Texto literal:
> We believe the main contribution of TuNR is in its ability to be a multifaceted tool towards precise gene regulation. Although the induction capabilities of TuNR and other comparable CRISPRa-based systems in activating endogenous gene expression is modest relative to transgenes, we believe that the precise regulation of the distribution of gene expression even within this limited range will be of tremendous value in future investigations. This is largely because the range of noise titration achieved by TuNR seems to be comparable to that of endogenous human promoters48,49. Furthermore, the innovation presented by TuNR takes a particular significance given recent findings that suggest that bacteria such as Bacillus subtilis have evolved to rarely be capable of independently controlling gene expression mean from variability, leading to a suggestion that similar limitations may exist in mammals50. Therefore, a tool such as TuNR that can achieve this decoupling of gene expression and variance presents an opportunity to investigate the costs or opportunities presented by the fact that variability of gene promoters might be inextricably chained to a given level of noise, or vice versa.

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/julie_2023_crispri_gene_modulation_and_all_optical_electrophysiology_in.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/julie_2023_crispri_gene_modulation_and_all_optical_electrophysiology_in.pdf|PDF]]
- Texto literal:
> Results A feasibility CRISPRi study was performed in post-differentiated iPSC-CMs targeting key genes important in cardiac electrophysiology. Comprehensive analysis using all-optical electrophysiology and a pipeline enabling correlative analysis of functional and molecular data in the same samples helped quantify the CRISPRi gene modulation in this in vitro model.

### Extracto 9
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/julie_2023_crispri_gene_modulation_and_all_optical_electrophysiology_in.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/julie_2023_crispri_gene_modulation_and_all_optical_electrophysiology_in.pdf|PDF]]
- Texto literal:
> For iPS and iPSC-CMs, CRISPRi can be viewed as a superior option for gene inhibition (knockdown) because of lower cytotoxicity, potentially higher efficiency, and a possibility for timeresolved, reversible action6, compared to standard CRISPR knockout. Cytotoxicity of standard CRISPR knockout comes from error-prone DNA repair of the double-strand breaks4,5. Dose and temporal control of gene modulation are desirable features to avoid off-target effects, chromosomal translocations, and genotoxicity23. Unlike CRISPR knockout, time-resolved CRISPRi allows the study of essential genes and their role in cellular functions. In our Dox-inducible CRISPRi system, we observed minimal side effects (Supplementary Figure 1). The choice of post-differentiated cardiomyocytes in this study was with the intent to avoid potential interferences with the differentiation process, to avoid potential TetO promoter silencing (Dox induction)13,51 during the Wnt-signaling modulation required for cardiac differentiation, and to provide testing in conditions that are a step closer to in vivo deployment for gene modulation. For full in vivo use, considerations for long-term stability are also important. However, for the described here in vitro testing, these are less relevant.

### Extracto 10
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 9|Pasaje 9]] | [[Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf|PDF]]
- Texto literal:
> upon addition of ABA, consistent with earlier experiments, suggesting that leakiness emerges from the accumulation of the first node activator (Supplementary Fig. 2B, first column). When both small molecules are present, TuNR induces expression more than either small molecule alone, reaching a maximum mAzami-Green expression of ~1000-fold when both inducers are at their highest concentration. Notably, a transcriptional activator circuit mediated by GA (rows of Supplementary Fig. 2B) achieves ~100-fold induction. As the concentration of ABA increases, so does the basal expression. This reflects a tradeoff between maximum expression and basal leakiness (Fig. 1D). The serial arrangement of the transcriptional activators attenuates this basal leakiness, while achieving a superior maximum fold-change induction when compared to a single-node circuit.

### Extracto 11
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/julie_2023_gene_modulation_with_crispr_based_tools_in_human.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/julie_2023_gene_modulation_with_crispr_based_tools_in_human.pdf|PDF]]
- Texto literal:
> The fusion of dCas to gene-regulatory proteins is also deployed for upregulation of genes (termed CRISPRa), Figs. 1G, and 2. Methods for gene activation were initially published in 2013 by using VP64 [83] and RNA polymerase (RNAP) [120]. VP64 is a strong transactivation domain that recruits the HAT p300 and activation complexes, causing DNA methylation and increased chromatin accessibility and activation of genes [89]. dCas9-VP64 is the first generation CRISPRa and achieves modest levels of activation. Effectors

### Extracto 12
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/julie_2023_gene_modulation_with_crispr_based_tools_in_human.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/julie_2023_gene_modulation_with_crispr_based_tools_in_human.pdf|PDF]]
- Texto literal:
> for CRISPRi, developed later, such as SunTag [85], SAM [86], and VPR [84], Fig. 2, all exhibit enhanced activation of genes, compared to the initially developed dCas9-VP64 [83], and provide flexible alternatives for experimental design. SunTag is an activation system that utilizes a scaffold of multiple VP64 activators to the dCas9 to parallelize the action of the transcriptional machinery to be recruited per gene, demonstrating a stronger activation with a single gRNA compared to dCas9-VP64 [85]. SunTag outperforms first generation activators but exhibits lower activation levels than SAM. SAM utilizes the dCas9-VP64 fusion protein and engineered sgRNAs to increase transcription. The engineering involves modifying portions of the gRNA into MS2-targeting aptamers [86], which then recruit additional activation domains; heat-shock factor 1 (HSF1) and the p65 subunit of the NF-κB complex. SAM has been shown to exhibit the most efficient levels of activation for singlegene targets. VPR – VP64/p65/Rta [84] was designed to activate transcription using three potent effectors—VP64, p64 and Rta—fused to dCas9. Despite its lower activation efficiencies compared to SAM, VPR is attractive for delivery because it offers a single-component system. For multiplexed gene regulation, SAM, SunTag and VPR have shown similar activation capacity. Newer hybrid methods for gene activation are emerging, such as SunTag-p65-HSF1

### Extracto 13
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf#Passage 10|Pasaje 10]] | [[Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf|PDF]]
- Texto literal:
> However, despite the versatility of TuNR, it is likely to be that our ability to achieve relatively small fold changes for endogenous genes as compared to transgenes is related to a lack of clear understanding of enhancer–promoter mechanisms and corrective cellular mechanisms that counteract the action of the synthetic circuit. Understanding these effects will enable synthetic circuits to more robustly drive endogenous gene production. Tentatively, some of the induction discrepancy between endogeneous and transgenes can be bridged by modifying the terminal effector domain with a Sun-tag system, which has demonstrated robust endogenous induction capabilities48. Alternatively, using the current iteration of TuNR, one could introduce the complementary DNA of a gene of interest under a synthetic promoter (e.g., pTRE) to test whether the induction capabilities recapitulate that of the fluorescent reporters.

### Extracto 14
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/yibing_2025_brain_targeted_nano_delivery_system_for_crispra_mediated.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/yibing_2025_brain_targeted_nano_delivery_system_for_crispra_mediated.pdf|PDF]]
- Texto literal:
> targeting the promoter region of the gene of interest. The choice of sgRNA binding site is critical,

### Extracto 15
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/julie_2023_gene_modulation_with_crispr_based_tools_in_human.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/julie_2023_gene_modulation_with_crispr_based_tools_in_human.pdf|PDF]]
- Texto literal:
> CRISPRi/a methods have also provided new opportunities to study cardiac disease pathogenesis and to develop better treatments in an otherwise difficult to study field. Mandegar et al. [130] were the first to develop an inducible CRISPRi platform in human iPSCs and follow up RNAseq to show that it outperformed CRISPR with an active Cas9, in addition to offering reversible gene modulation. Proximity to the transcription start site (TSS) in designing gRNAs was good efficiency predictor. In addition to showing utility and specificity of CRISPRi knockdown of genes implicated in cardiac cell differentiation and illustrating temporary gene modulation of exogenous targets (e.g. calcium sensor GCaMP), they also found expected phenotypic consequences (action potential prolongation) of CRISPRi reduction of the HERG potassium ion channel in the

### Extracto 16
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/julie_2023_gene_modulation_with_crispr_based_tools_in_human.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/julie_2023_gene_modulation_with_crispr_based_tools_in_human.pdf|PDF]]
- Texto literal:
> With any genetic modulation method, proper introduction of CRISPR tools and successful gene perturbation should be tested. Delivery of CRISPR tools using plasmids, mRNA, protein, or lentiviral vectors can be challenging in terminally differential cells, such as cardiomyocytes. Transduction by viral particles or lipofection and electroporation methods need to be optimized for each cell type and model organism. Although commercial gRNA libraries are available, a panel of gRNAs targeting different loci of each gene need to be evaluated to identify the efficiency of perturbation, e.g. by qPCR, which can be quite tedious or by newer sequencing methods [72]. Additionally, confirmation of each gene

### Extracto 17
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/yibing_2025_brain_targeted_nano_delivery_system_for_crispra_mediated.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/yibing_2025_brain_targeted_nano_delivery_system_for_crispra_mediated.pdf|PDF]]
- Texto literal:
> genomic sequence. In gene therapy, CRISPRa—formed by fusing a dCas9 with transcriptional

### Extracto 18
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/yibing_2025_brain_targeted_nano_delivery_system_for_crispra_mediated.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/yibing_2025_brain_targeted_nano_delivery_system_for_crispra_mediated.pdf|PDF]]
- Texto literal:
> have shown that either exogenous overexpression or enhanced endogenous Arc expression can

### Extracto 19
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/yibing_2025_brain_targeted_nano_delivery_system_for_crispra_mediated.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/yibing_2025_brain_targeted_nano_delivery_system_for_crispra_mediated.pdf|PDF]]
- Texto literal:
> good controllability, safety, and reversibility—qualities particularly valuable in therapeutic research

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf|alain_2021_orthogonal_control_of_mean_and_variability_of_endogenous.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/julie_2023_crispri_gene_modulation_and_all_optical_electrophysiology_in.pdf|julie_2023_crispri_gene_modulation_and_all_optical_electrophysiology_in.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/julie_2023_gene_modulation_with_crispr_based_tools_in_human.pdf|julie_2023_gene_modulation_with_crispr_based_tools_in_human.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/yibing_2025_brain_targeted_nano_delivery_system_for_crispra_mediated.pdf|yibing_2025_brain_targeted_nano_delivery_system_for_crispra_mediated.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/alexander_2020_direct_rna_sequencing_reveals_m6a_modifications_on_adenovirus.pdf|alexander_2020_direct_rna_sequencing_reveals_m6a_modifications_on_adenovirus.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/anni_2021_hyperinsulinemia_in_obesity_inflammation_and_cancer.pdf|anni_2021_hyperinsulinemia_in_obesity_inflammation_and_cancer.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/beijian_2021_m6a_demethylase_fto_attenuates_cardiac_dysfunction_by_regulating.pdf|beijian_2021_m6a_demethylase_fto_attenuates_cardiac_dysfunction_by_regulating.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/bernard_2012_diabetes_and_hypertension_is_there_a_common_metabolic.pdf|bernard_2012_diabetes_and_hypertension_is_there_a_common_metabolic.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/dipanjana_2026_fto_dependent_m6a_rna_dysregulation_underlies_memory_deficits.pdf|dipanjana_2026_fto_dependent_m6a_rna_dysregulation_underlies_memory_deficits.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/hao_2021_mettl3_mediated_m6a_rna_methylation_promotes_the_anti.pdf|hao_2021_mettl3_mediated_m6a_rna_methylation_promotes_the_anti.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/hongyi_2020_applications_of_genome_editing_technology_in_the_targeted.pdf|hongyi_2020_applications_of_genome_editing_technology_in_the_targeted.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/neal_2020_defining_the_atpome_reveals_cross_optimization_of_metabolic.pdf|neal_2020_defining_the_atpome_reveals_cross_optimization_of_metabolic.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/paz_2021_the_role_of_m6a_m5c_and_rna_modifications.pdf|paz_2021_the_role_of_m6a_m5c_and_rna_modifications.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/roland_2024_lim_domain_only_4_lmo4_enhances_cd8_t.pdf|roland_2024_lim_domain_only_4_lmo4_enhances_cd8_t.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/stephanie_2022_crispr_based_approaches_for_gene_regulation_in_non.pdf|stephanie_2022_crispr_based_approaches_for_gene_regulation_in_non.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/xingxing_2023_overexpression_of_fto_inhibits_excessive_proliferation_and_promotes.pdf|xingxing_2023_overexpression_of_fto_inhibits_excessive_proliferation_and_promotes.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/xiulin_2021_the_role_of_m6a_modification_in_the_biological.pdf|xiulin_2021_the_role_of_m6a_modification_in_the_biological.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q13-riesgo-desregulacion-fto/Sources/yanlin_2023_epigenetic_regulation_in_metabolic_diseases_mechanisms_and_advances.pdf|yanlin_2023_epigenetic_regulation_in_metabolic_diseases_mechanisms_and_advances.pdf]]
