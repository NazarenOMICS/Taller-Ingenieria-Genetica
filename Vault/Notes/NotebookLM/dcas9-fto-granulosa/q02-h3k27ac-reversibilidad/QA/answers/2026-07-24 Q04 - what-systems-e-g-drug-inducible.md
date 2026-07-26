---
type: reference
status: current
date: 2026-07-24
source: "notebooklm:dcas9-fto-granulosa/q02-h3k27ac-reversibilidad"
related:
  - "[[Notes/Dashboards/dCas9-p300 H3K27ac reversibility]]"
---

# Q04 - What systems (e.g., drug-inducible, degron, optogenetic) have been used in these sources to achieve temporal control of dCas9-p300 activity, and how precisely can activation be turned on and off?

The sources describe several systems for achieving temporal control of **dCas9-p300** and other CRISPR-based effectors, ranging from rapid protein degradation switches to light-activated modules. These systems allow researchers to "gate" activation to specific time windows with varying levels of speed and reversibility.

### 1. Degron-Based Systems (AID and ecDHFR)
Degron systems regulate the **stability and degradation** of the protein pool, offering high precision for "turning off" activation.
*   **Auxin-Inducible Degron (AID):** This system uses an IAA17 peptide tag on the dCas9 protein  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 3|[1]]]. In the presence of the plant hormone **auxin**, the dCas9-effector complex is rapidly ubiquitinated and degraded by the proteasome  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 3|[1]]].
    *   **Precision and Kinetics:** Clearance of the protein pool is extremely fast, taking only **1 to 2 hours**, with an estimated protein half-life of **less than 15 minutes**  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 1|[2]]].
    *   **Reversibility:** Upon washing out the auxin, detectable protein reappears within **30 minutes** and returns to maximum levels within **3 to 7 hours**  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 1|[2]]]. Transcriptional upregulation of endogenous genes is "largely abrogated" when measured 48 hours after starting degradation  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 4|[3]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 5|[4]]].
*   **ecDHFR (ecDDD) System:** This functions in the opposite direction; the dCas9 or its effector is intrinsically unstable and degraded until it is stabilized by the addition of the drug **trimethoprim (TMP)**  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 6|[5]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/hongxin_2020_cell_cell_contact_induced_gene_editing_activation_in.pdf#Passage 1|[6]]]. 
    *   **"Stereo-tuner" Control:** One source describes a "stereo-tuner" system combining an AID-tagged dCas9 with an ecDHFR-tagged effector domain, allowing a gene's activity to be finely tuned in both directions using two independent drugs  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/hongxin_2020_cell_cell_contact_induced_gene_editing_activation_in.pdf#Passage 2|[7]]].

### 2. Drug-Inducible and Small-Molecule Switches
*   **Tet-on/Doxycycline (Dox) Systems:** One study utilized a **synNotch-Tet-Cas9:p300 system**  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf#Passage 1|[8]]]. In this configuration, activation of target immune genes (e.g., *CCL19*, *IL2*) requires two inputs: spatial contact with a specific "sender" cell and the temporal addition of **Doxycycline**  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf#Passage 1|[8]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf#Passage 2|[9]]]. 
*   **Chemically Induced Dimerization (CID):** These systems use split fragments of dCas9 or its effector that remain inactive until a small molecule, such as **rapamycin**, triggers their assembly  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf#Passage 3|[10]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf#Passage 2|[11]]]. 
*   **Hormone-Binding Domains:** Systems using domains like **ERT2** sequester the dCas9-effector in the cytoplasm until **4-hydroxytamoxifen (4-HT)** is added, triggering its translocation into the nucleus to begin activity  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/benjamin_2015_strategies_for_precision_modulation_of_gene_expression_by.pdf#Passage 2|[12]]].
*   **Limitations:** A major drawback cited for many drug-inducible systems (like Dox and IPTG) is **"leaky" expression**, where activation occurs even in the absence of the inducer  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf#Passage 4|[13]]].

### 3. Optogenetic (Light-Controlled) Systems
Optogenetics provides the highest spatial and temporal resolution, using light to trigger activity.
*   **Blue Light Recruitment:** Utilizing light-sensitive **CRY2 and CIB1** proteins, a dCas9 can be held at the target site while the p300 effector is only recruited when blue light (~450 nm) is applied  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf#Passage 3|[14]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf#Passage 5|[15]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf#Passage 6|[16]]]. 
*   **Split-dCas9 Magnets:** Photoinducible dimerization domains called **Magnets (pMag/nMag)** can be used to reassemble split-dCas9 fragments in response to blue light  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf#Passage 6|[16]]].
*   **Precision:** These processes are characterized as **"rapid and reversible"**  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf#Passage 3|[14]]]. Activation is turned on by light exposure and can be reversed simply by returning the cells to a dark environment  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf#Passage 5|[15]]].

### 4. Physical Control (Heat)
*   **Heat-Shock Promoters:** dCas9-p300 expression can be driven by a heat-shock promoter (**Phsp**) [18]. 
*   **Precision:** Activation is triggered by heating cells (e.g., to **33°C for 1 hour**) and can be switched off by simply **cooling the cells back to 20°C** [18]. This system has been shown to produce robust, time-dependent target gene editing in model organisms like *C. elegans* [18].

### Summary of Precision and On/Off Dynamics
| System | "On" Trigger | "Off" Trigger | Precision/Kinetics |
| :--- | :--- | :--- | :--- |
| **AID Degron** | Wash-out Auxin | Add Auxin | **Off in 1–2 hrs**; Half-life <15 min  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 1|[2]]]. |
| **ecDHFR** | Add TMP | Wash-out TMP | Concentration-dependent stabilization  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/hongxin_2020_cell_cell_contact_induced_gene_editing_activation_in.pdf#Passage 1|[6]]]. |
| **Optogenetic** | Blue Light | Darkness | Rapid and reversible  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf#Passage 3|[14]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf#Passage 5|[15]]]. |
| **Tet-on** | Doxycycline | Wash-out Dox | Often suffers from background **leakiness**  [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf#Passage 4|[13]]]. |
| **Heat-Shock** | 33°C Heat | 20°C Cooling | Robust and time-dependent [18]. |

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf|PDF]]
- Texto literal:
> We proceeded to produce stable cell lines with the AID-dCas9-PR construct via Flp mediated integration into transcriptionally competent genomic landing sites in HEK293Trex-FlpIn and CHO-K1 derived cell lines. Functional activity of the integrated AID-dCas9-PR transactivator was confirmed via transfection of fluorescent or luciferase reporters under control of artificial gRNA binding site containing promoters and co-transfection of the corresponding guide RNAs. Addition of auxin to the medium severely reduced reporter output, to below detectable level in the case of the fluorescent reporters (Supplementary Fig. 2c). Similarly, targeting a number of endogenous genes via transfection of mixes of expression plasmids for 3 or 4 sgRNAs to sites within the same promoter region (RasL11a and Arpc1b in CHO cells (Fig. 2b) and ASCL1, IL1RN, OLIG2 and SOX9 in HEK293 cells (Fig. 2c)) resulted in clear transcriptional upregulation, which was markedly reduced in the presence of auxin.

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf|PDF]]
- Texto literal:
> The ecDHFR destabilising domain (ecDDD) is an unfolded, structurally unstable domain derived from the Escherichia coli dihydrofolate reductase (DHFR) gene, which was evolved for enhanced instability by introduction of two additional missense mutations (R12Y/Y110I), which when fused to proteins of interest similarly targets the fusion protein for rapid proteasomal degradation12. In contrast to the AID the ecDDD does not require any additional factors to function in mammalian cells. The small-molecule drug trimethoprim (TMP) can bind and

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 5|Pasaje 5]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf|PDF]]
- Texto literal:
> stabilise the ecDDD in the fusion protein and prevent its proteosomal degradation in a concentration dependent manner12.

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf#Passage 6|Pasaje 6]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf|PDF]]
- Texto literal:
> TMP, addition of the drug effects stabilisation in a concentration-dependent manner (Fig. 5b). We show that attachment of the ecDHFR degron does not affect the ability of the fusion protein to induce transcriptional activation in conjunction with AID-dCas9 (Fig. 5c). Using our luciferase assay we show that addition of TMP and/or auxin to the culture medium can up and down regulate the expression of luciferase from a responsive promoter (Fig. 5c). Tagging of a different aptamer binding protein, utilising the PP7 aptamer, with the ecDDD degron was recently also shown to be effective for tunable transcriptional activation18. Here we combine stabilisation of the ecDDD tagged MCP-effector module with the tunable degradation of the AID-dCas9 protein. We call this system ‘stereo-tuner dCas9’, and envisage that combination of the domain-less AID-dCas9 DNA binding module with various ecDHFR-MCP-effector domain plasmids will allow precisely targetable functional activities that can be finely tuned in opposite directions by two independent small molecule drugs.

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/hongxin_2020_cell_cell_contact_induced_gene_editing_activation_in.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/hongxin_2020_cell_cell_contact_induced_gene_editing_activation_in.pdf|PDF]]
- Texto literal:
> To develop a more precisely controlled device, we introduced the Tet-on system to generate a synNotch-Tet-Cas9: p300 system which was controlled by both CD19+ cells and Dox (Doxycycline) treatment (Fig. 2A). The T2A-puro-TRE-Cas9:p300 cassette was knocked-in at the AAVS1 locus through HITI (Fig. S9A) and the validated knocked-in clone C2 was transduced with the eZ3 system to establish stable cell lines (Fig. S9B and S9C). The expression of the Cas9:p300 fusion protein and MYOD was up-regulated only when both CD19+ cells and Dox were applied (Fig. S9D and

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/hongxin_2020_cell_cell_contact_induced_gene_editing_activation_in.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/hongxin_2020_cell_cell_contact_induced_gene_editing_activation_in.pdf|PDF]]
- Texto literal:
> S9E). PD-1 and CTLA4 were edited and CCL19 and IL2 were significantly up-regulated only in the presence of both CD19+ cells and Dox (Figs. 2D, 2E and S7B). Therefore, the alternative system synNotch-Tet-Cas9:p300 could control gene regulation via a spatiotemporal manner, giving that cellcell contact provided a spatial control and that the time of adding Dox provided a temporal control.

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf|PDF]]
- Texto literal:
> Through various optimizations, the final Cas9 variant (iCas) has higher editing capability at numerous sites with the addition of 4-HT but lower endonuclease activity in the absence of 4-HT.63 Therefore, temporal control over CRISPR/Cas9 gene editing can be conducted by adding 4-HT, which shows good results in improving gene-specific editing and reducing offtarget effects. Another mechanism using small molecules to control the

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf|PDF]]
- Texto literal:
> Zetsche et al. engineered a split Cas9 protein that was generated at two different split sites (Arg535 and Glu573) and produced C- and N-terminal Cas9 fragments that were bound with FK506 binding protein 12 (FKBP) and the FKBP rapamycin binding domain (FRB), respectively (Fig. 3c).66 The conditional reconstitution and activation of split-Cas9 was achieved via rapamycin-induced heterodimerization (Fig. 3d).66 Furthermore, to spatially separate the two fragments into different cellular compartments and prevent them from spontaneous reconstitution, a nuclear localization signal (NLS) and a nuclear export signal (NES) were attached to the C- and N-terminal Cas9 fragments, respectively, leading to decreased basal activity of the cas9 protein in the absence of rapamycin (Fig. 3c, d).

### Extracto 9
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf|PDF]]
- Texto literal:
> their active domains – to dCas9 and expressing them as a single recombinant protein (Fig. 2.2A). Transcription activator domains (VP64, p65) or repressor domains (KRAB, SID) have been fused to dCas9 to specifically increase or decrease target gene expression (Gilbert et al., 2013; Maeder et al., 2013b; Perez-Pinera et al., 2013; Lawhorn et al., 2014). Single dCas9–effector fusions are com- monly targeted to adjacent sites using multiple different sgRNAs for maximum impact. In an effort to obtain maximum activation a combination of three different effectors (VP64, p65 and Rta) has been fused in succession to dCas9, resulting in a ~100-fold increase in transactivation of the target genes compared to dCas9-VP64 alone (Chavez et al., 2015). A basic strategy towards achieving temporal control of dCas9–effector target binding is inducible expression of dCas9 or the sgRNA, e.g. by using a doxycycline (González et al., 2014; Wang et al., 2014; Dow et al., 2015) or IPTG-responsive promoter. However, this approach suffers from leaky expression in the absence of an inducer.

### Extracto 10
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/benjamin_2015_strategies_for_precision_modulation_of_gene_expression_by.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/benjamin_2015_strategies_for_precision_modulation_of_gene_expression_by.pdf|PDF]]
- Texto literal:
> Combinatorial biotechnology (Epi)genome editing systems allow not only for fusing a genome editing system to an effector but they can also

### Extracto 11
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf|PDF]]
- Texto literal:
> protein by light induction. For example, some studies have reported an optogenetic two-hybrid system, which contains two independent components: a genomic anchor (dCas9 system) fused to the light-sensitive cryptochrome-interacting basic-helix-loop-helix (CIB1) protein to form the dCas9-CIB1 complex and a cryptochrome circadian clock 2 (CRY2) fused to a different effector domain (activating effectors) to form the CRY2-activator complex (Fig. 6a).29,136–138 Under the stimulation of blue light (peak ~450 nm), the CIB1-effector complex could be recruited to form the biopolymer dCas9-CIB1-CYR2-effector complex, expanding the activation functionality of Cas9 (Fig. 6a).29,136,138,139 Moreover, incubating cells in the dark can reverse this activation.29,138

### Extracto 12
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf|PDF]]
- Texto literal:
> dimerize upon rapamycin induction (Banaszynski et al., 2005; Zetsche et al., 2015b) (Fig. 2.2C). Using a split-dCas9 system fused to VP64, expression of target genes was shown to be specifically induced in the presence of rapamycin (Zetsche et al., 2015b). Another strategy involves reassembly of split-dCas9 by photoinducible dimerization domains termed Magnets (pMag and nMag) (Fig. 2.2C) in response to exposure to blue light (Kawano et al., 2015; Nihongaki et al., 2015a).

### Extracto 13
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf#Passage 5|Pasaje 5]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf|PDF]]
- Texto literal:
> The second strategy is to change the Cas9 nuclease activity by light induction. For example, Nihongaki et al. described an engineered photoactivatable split Cas9 (termed paCas9) comprising nitrogen- and carbon-terminal fragments that are fused to light-inducible dimerization domains (pMag and nMag) (Fig. 6b).140 Without light stimulation, each split fragment from Cas9 is inactivated. However, blue light illumination can promote the heterodimerization of split Cas9 fragments via pMag-nMag interactions, leading to the restoration of Cas9 activity (Fig. 6b).140,141 Furthermore, paCas9 and wild-type Cas9 have similar nuclease activity and targeting specificity. Thus, paCas9 can be utilized in genome editing and genomic modifications, allowing the possibility to conduct spatiotemporal control of CRISPR gene editing via the spatiotemporal control of blue light irradiation. In contrast to paCas9, a different photoswitchable Cas9 was designed (named psCas9) that employs a single-polypeptide architecture (Fig. 6d).142 The REC2 and PI domains of psCas9 were inserted by the photodissociable dimeric fluorescent protein (pdDronpa1) (Fig. 6d).132,143 Without treatment with 500-nm light, the inserted pdDronpa1 domains homodimerize and subsequently sterically inhibit psCas9 activity. However, following the illumination with 500-nm light, pdDronpa1 dissociates, resulting in the restoration of the Cas9 activity, genome editing functions, and transcriptional upregulation (Fig. 6d).132,142,143 A similar study by Richter et al. developed a Cas9-RsLOV2 monomer, which was constructed by the fusion of Cas9 and the R. sphaeroides LOV domain (RsLOV) (Fig. 6c).144 Without light stimulation, two Cas9-RsLOV2 monomers can homodimerize, causing severe steric inhibition of Cas9 activity. However, under blue light shock, the Cas9-RsLOV2 dimer can dissociate and revert to the Cas9-RsLOV2 monomer, which has high nuclease activity and targeting specificity (Fig. 6c).132,144 Another way to change Cas9 activity

### Extracto 14
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf#Passage 6|Pasaje 6]] | [[Research/Papers/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf|PDF]]
- Texto literal:
> promoter (Phsp) of CRISPR/Cas9 cassettes (Fig. 7), resulting in conditional gene editing in different cell types at different developmental stages.18,55,148 For example, Shen et al. reported that the CRISPR/Cas9 plasmid controlled by heat shock

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/benjamin_2015_strategies_for_precision_modulation_of_gene_expression_by.pdf|benjamin_2015_strategies_for_precision_modulation_of_gene_expression_by.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf|chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf|daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf|dirk_2017_drug_tunable_multidimensional_synthetic_gene_control_using_inducible.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/hongxin_2020_cell_cell_contact_induced_gene_editing_activation_in.pdf|hongxin_2020_cell_cell_contact_induced_gene_editing_activation_in.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/gough_2023_dissection_of_a_non_coding_risk_locus_at.pdf|gough_2023_dissection_of_a_non_coding_risk_locus_at.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/hilton_2015.pdf|hilton_2015.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf|jackson_2022_a_histone_deacetylase_network_regulates_epigenetic_reprogramming_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/liao_2026.pdf|liao_2026.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/matthew_2019_sufficiency_analysis_of_estrogen_responsive_enhancers_using_synthetic.pdf|matthew_2019_sufficiency_analysis_of_estrogen_responsive_enhancers_using_synthetic.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf|minhee_2016_the_epigenome_the_next_substrate_for_engineering.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q02-h3k27ac-reversibilidad/Sources/t_2018_sirt6_haploinsufficiency_induces_brafv600e_melanoma_cell_resistance_to.pdf|t_2018_sirt6_haploinsufficiency_induces_brafv600e_melanoma_cell_resistance_to.pdf]]
