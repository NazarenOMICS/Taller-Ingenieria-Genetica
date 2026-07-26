---
type: reference
status: current
date: 2026-07-24
source: "notebooklm:dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores"
related:
  - "[[Notes/Dashboards/dCas9-p300 vs other activators]]"
---

# Q03 - According to these sources (e.g., modular dCas9-SunTag systems), how does the SunTag signal-amplification architecture change the potency or specificity of a recruited effector (e.g., p300) compared to a direct 1:1 dCas9-effector fusion?

The **SunTag** signal-amplification architecture fundamentally transforms the performance of recruited effectors by replacing the **1:1 dCas9-effector ratio** with a **multivalent protein scaffold** capable of recruiting many effector molecules to a single genomic locus  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/albert_2017_genetic_and_epigenetic_control_of_gene_expression_by.pdf#Passage 6|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 1|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 2|[3]]]. This shift significantly enhances **potency** through molecular signal amplification while improving **specificity** by allowing for independent tuning of system components  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/albert_2017_genetic_and_epigenetic_control_of_gene_expression_by.pdf#Passage 6|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/albert_2017_genetic_and_epigenetic_control_of_gene_expression_by.pdf#Passage 5|[4]]].

### **Potency and Signal Amplification**
The SunTag system functions as an "epitope docking station," enabling a single dCas9 protein to recruit a large array of effector proteins fused to single-chain variable fragments (scFv)  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/albert_2017_genetic_and_epigenetic_control_of_gene_expression_by.pdf#Passage 6|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 1|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 2|[3]]].
*   **Magnitude of Activation:** This architecture leads to a much higher induction of gene expression compared to direct fusions. For instance, while a direct 1:1 dCas9-VP64 fusion typically achieves a modest **2-fold** increase in expression for certain genes (e.g., *CXCR4*), the SunTag-VP64 system can boost that same gene’s expression up to **50-fold**  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/albert_2017_genetic_and_epigenetic_control_of_gene_expression_by.pdf#Passage 6|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 3|[5]]].
*   **Epigenetic Editing Efficacy:** In DNA methylation studies, modular SunTag systems (e.g., recruiting DNMT3A) exhibit "much higher induction" of methylation at target sites compared to direct fusions, which often show poor on-target performance when expression is limited to avoid side effects  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 4|[6]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 5|[7]]].
*   **Multiplexing Efficiency:** SunTag allows for effective multiplexed activation across multiple loci with induction levels comparable to single-guide experiments, a task that can be more challenging with bulky direct fusion complexes  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 6|[8]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 7|[9]]].

### **Specificity and Fidelity**
The SunTag architecture overcomes a critical "tradeoff" inherent in direct fusions, where increasing protein expression to achieve high on-target activity often results in **pervasive off-target activity**  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 8|[10]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 9|[11]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 4|[12]]].
*   **Independent Tuning:** Modular systems allow researchers to independently modulate the expression of the DNA-targeting module (dCas9-SunTag) and the effector module  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/albert_2017_genetic_and_epigenetic_control_of_gene_expression_by.pdf#Passage 5|[4]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 7|[13]]].
*   **Reduction of Off-Targets:** By limiting the abundance of the dCas9-SunTag "targeter," researchers can ensure it binds primarily to its highest-affinity on-target sites  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/albert_2017_genetic_and_epigenetic_control_of_gene_expression_by.pdf#Passage 5|[4]]]. Simultaneously, the total concentration of the effector can be restricted to avoid non-specific enzymatic activity elsewhere in the genome  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/albert_2017_genetic_and_epigenetic_control_of_gene_expression_by.pdf#Passage 5|[4]]].
*   **Fidelity Levels:** Genome-wide characterization has shown that modular SunTag systems for epigenetic modifiers (like DNMT3A) achieve the **lowest reported off-target effects** to date, whereas direct fusions often lead to "widespread off-target DNA methylation"  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 4|[6]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 9|[11]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 8|[14]]].

### **Constraints: Effector Size and Condensate Dynamics**
While the SunTag system generally increases potency, its effectiveness is limited by the **physical and spatial properties** of the recruited proteins.
*   **Spatial Hindrance for Large Effectors:** For large proteins like the **p300 catalytic core** or **TET1-CD**, signal amplification can be counterproductive  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 5|[15]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/yujuan_2025_dynamic_properties_of_transcriptional_condensates_modulate_crispra_mediated.pdf#Passage 1|[16]]]. The sheer size of the amplified complex can create **steric hindrances**, making it difficult for the dCas9 complex to access the DNA properly or for the effector to land on its target  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/yujuan_2025_dynamic_properties_of_transcriptional_condensates_modulate_crispra_mediated.pdf#Passage 8|[17]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/yujuan_2025_dynamic_properties_of_transcriptional_condensates_modulate_crispra_mediated.pdf#Passage 6|[18]]]. In some reporter studies, p300 recruitment via scaffolding showed limited activity compared to smaller activators due to these spatial constraints  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 5|[15]]].
*   **Scaffold Number and "Solid" Condensates:** Increasing the number of SunTag repeats (e.g., to 10 or more) can lead to the formation of **solid-like transcriptional condensates**  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/yujuan_2025_dynamic_properties_of_transcriptional_condensates_modulate_crispra_mediated.pdf#Passage 9|[19]]]. These solid structures sequester essential endogenous co-activators like **p300 and MED1**, rendering them ineffective and resulting in a loss of gene activation capability  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/yujuan_2025_dynamic_properties_of_transcriptional_condensates_modulate_crispra_mediated.pdf#Passage 9|[19]]]. 
*   **Optimal Configuration:** Research suggests that scaffolds with fewer repeats (e.g., ~3x) often achieve the highest activation because they form dynamic, **"liquid-like" condensates** that facilitate more efficient transcriptional bursting and recruitment of the cellular machinery  [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/yujuan_2025_dynamic_properties_of_transcriptional_condensates_modulate_crispra_mediated.pdf#Passage 9|[19]]].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/albert_2017_genetic_and_epigenetic_control_of_gene_expression_by.pdf#Passage 6|Pasaje 6]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/albert_2017_genetic_and_epigenetic_control_of_gene_expression_by.pdf|PDF]]
- Texto literal:
> Several attempts have been made to improve the efficiency of CRISPRa. One approach is to amplify the activation signal from the transcriptional activator VP6466,72. This is achieved by fusing a scaffold to dCas9 that is able to recruit many copies of VP64. This scaffold consists of a tandem array of antibody epitopes, named SunTag array, which can specifically interact and recruit multiples copies of a single-chain variable fragment (scFv) fused to VP64 (Figure 2B)66,72. This system can significantly increase the expression of endogenous genes, e.g. CXCR4, up to 50-fold in human

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf|PDF]]
- Texto literal:
> versus off-target methylation with the direct fusion system. A redesigned, modular system for

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf|PDF]]
- Texto literal:
> single-chain antibody, scFv-GCN4, subsequently referred to as αGCN4) to be recruited to a

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/albert_2017_genetic_and_epigenetic_control_of_gene_expression_by.pdf#Passage 5|Pasaje 5]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/albert_2017_genetic_and_epigenetic_control_of_gene_expression_by.pdf|PDF]]
- Texto literal:
> erythroleukemia K562 cells with a single sgRNA as compared to a 2-fold increase observed with dCas9–VP64 fusion73. Using dCas9–SunTag, potent activation of CXCR4 is shown to promote cell migration72.

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf|PDF]]
- Texto literal:
> unambiguously assess the functional consequences of DNA methylation. To address this, we

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf|PDF]]
- Texto literal:
> transfected. The change in DNA methylation (∆mCG) was calculated by subtracting the average

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 5|Pasaje 5]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf|PDF]]
- Texto literal:
> methylation deposition was observed between the dC9Sun-D3A system and the direct fusion

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 6|Pasaje 6]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf|PDF]]
- Texto literal:
> with dC9Sun-D3A, compared to pervasive off-target binding and methylation by the dC9-D3A

### Extracto 9
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 7|Pasaje 7]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf|PDF]]
- Texto literal:
> D3A and dC9-D3A-high. Indeed, western blot on protein extractions from cells before and after

### Extracto 10
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 8|Pasaje 8]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf|PDF]]
- Texto literal:
> of the single fusion to reduce off-target methylation levels resulted in poor induction of on-target

### Extracto 11
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf#Passage 9|Pasaje 9]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf|PDF]]
- Texto literal:
> addressed is the potential for off-target DNA methylation induction, which could lead to non-

### Extracto 12
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 7|Pasaje 7]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> vs. miniCMV. The strength of TRE3G induction was in the order of VP+MV>2VP>p300+MV>VP. Error bars

### Extracto 13
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 5|Pasaje 5]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> regarding the incorporation of the DNA demethylase Tet1-CD for CRISPRa using the SunTag

### Extracto 14
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/yujuan_2025_dynamic_properties_of_transcriptional_condensates_modulate_crispra_mediated.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/yujuan_2025_dynamic_properties_of_transcriptional_condensates_modulate_crispra_mediated.pdf|PDF]]
- Texto literal:
> mean ± SEM (n = 3 biological replicates). Each dot represents a biological replicate. Dots of the same color indicate that they are from the same batchof experiments. P values were determined by one-way ANOVA, comparing to the negative control (NC, dCas9 + sgNEUROD1) group. e A diagram summarizing the findings of this study. Increasing the number of SunTag-AD arrays (e.g., 3xVPR and 3xVPRF) results in liquid-like condensates and boosts the transcriptional activation of the CRISPRa-SunTagplatform.However, when the numberof SunTag scaffolds is increased to 10 or more, solid-like condensates form, sequestering co-activators such as p300 and MED1, which exhibit low dynamicity and liquidity, significantly reducing activation strength. We propose that optimal phase separation, reflecting appropriate multivalent interactions within the CRISPRa platform, creates a conducive microenvironment around the transcription start site for efficient activation. Source data are provided as a Source Data file.

### Extracto 15
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/yujuan_2025_dynamic_properties_of_transcriptional_condensates_modulate_crispra_mediated.pdf#Passage 8|Pasaje 8]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/yujuan_2025_dynamic_properties_of_transcriptional_condensates_modulate_crispra_mediated.pdf|PDF]]
- Texto literal:
> expression64–67. We performed antibody staining for endogenous Mediator complex subunit 1 (MED1) and directly imaged HaloTag-labeled endogenous p300 in living cells generated through CRISPR knockin. We found that both co-activators were enriched in condensates formed by 3xVPR, 10xVPR, 3xVPRF, and 10xVPRF, with colocalization ratios ranging from 81.8% to 99.5% (Fig. 6a–d). Further quantitative analysis indicated that the total fluorescence intensity of MED1 and p300within the condensates was significantly greater in the 10xVPR system than in the 3xVPR system. Correspondingly, the average nucleoplasmic signal of both co-activators outside the condensates was reduced in the 10xVPR system compared to the 3xVPR system. This trend was also observed in the 10xVPRF and 3xVPRF systems (Fig. 6e, f). These observations suggest that fewer MED1 and p300 molecules freely diffuse outside the condensates in the 10xVPR and 10xVPRF systems. Through 1,6-HD treatment and FRAP analysis, we found that the liquidity of p300wasconsistentwith thatofCRISPRa condensates. Specifically, p300 exhibited high liquidity in 3xVPR and 3xVPRF, whereas its liquidity was significantly reduced in 10xVPR and 10xVPRF (Fig. 6g, h). These results revealed that low liquidity in CRISPRa condensates can trap co-activators, resulting in the loss of gene activation capability. Our findings suggest that the dynamicity and liquidity of transcriptional condensates are crucial for effective transcriptional activity.

### Extracto 16
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/yujuan_2025_dynamic_properties_of_transcriptional_condensates_modulate_crispra_mediated.pdf#Passage 6|Pasaje 6]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/yujuan_2025_dynamic_properties_of_transcriptional_condensates_modulate_crispra_mediated.pdf|PDF]]
- Texto literal:
> CRISPRa tools modulate transcriptional bursting kinetics Numerous studies have shown that increasing the number of activation domains (ADs) recruited by each dCas9 is an effective strategy for optimizing CRISPRa7–9. The VPR system, which concatenates three ADs, can recruit more ADs when combined with the SunTag design than the corresponding PH system. Therefore, we utilized the SunTag system to construct SunTag3xVPR, SunTag5xVPR, and SunTag10xVPR systems and compared their performance with the VP64, SAM, VPR and SunTag10xPH systems (Fig. 1a). By tracing nascent transcripts produced at the sites of miniCMV-TriTagmTagBFP, we observed transcriptional bursts upon CRISPR activation, alternating between active (on) and inactive (off) states (Fig. 1b, c). Using this system, we examined how different CRISPRa systems regulate transcriptional bursting by analyzing burst duration, pause duration, and burst amplitude as indicators of transcriptional activity. Intriguingly, we observed significant variations in burst durations among all systems, while the duration of transcriptional silencing remained relatively consistent at around 13min. The dCas9-VP64 system displayed the shortest burst duration (14min), while the VPR and SAM systems exhibited burst durations of around 25min. The 10xPH system showed significantly extended burst durations (70min). Notably, the 3xVPR system demonstrated robust RNA production from miniCMV, outperforming the 10xPH system, with an average burst duration of approximately 95min. However, the 5xVPR and 10xVPR systems had shorter average burst durations compared to the 3xVPR system, at 37 and 50min, respectively (Fig. 1d). Furthermore, the burst amplitude of the 3xVPR system is comparable to that of the 10xPH system, yet significantly higher thanother systems (Fig. 1e). These findings collectively illustrate the capacity of CRISPRa tools to enhance transcriptional activation by prolonging burst durations and increasing burst amplitude. Additionally, our results uncover an unexpected phenomenon indicating a potential decline in the efficiency of CRISPR-SunTag activators as the number of SunTag-AD arrays increases.

### Extracto 17
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/yujuan_2025_dynamic_properties_of_transcriptional_condensates_modulate_crispra_mediated.pdf#Passage 9|Pasaje 9]] | [[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/yujuan_2025_dynamic_properties_of_transcriptional_condensates_modulate_crispra_mediated.pdf|PDF]]
- Texto literal:
> By examining the hallmark behaviors62 of phase separation (Sup-plementary Table 1), we conclude that 3xVPR and 3xVPRF form liquidlike transcriptional condensates through phase separation. On the other hand, the higher presence of scaffold sequences in the 10xVPR, 10xVPRF, PCP-12xVPRF, and PCP-40xVPRF systems facilitates the formation of more extensive molecular networks, resulting in solid-like transcriptional condensateswith reduceddynamicity and liquidity.We validated the localization of CRISPR activators and their activation capacities in HCT116 cells, and the results were consistent with those obtained inHeLa cells (Supplementary Fig. 14). To assess the specificity of CRISPR-SunTag activators forming TF condensates, we performed RNA-seq analysis on samples where individual CRISPRa systems (VPR, VPRF, 3xVPR and 3xVPRF) targeted HSPB8. The correlation in gene expression between each activator and the control sample was highly similar (R > 0.98), indicating that none of the activators broadly influenced gene expression. Notably, HSPB8 was consistently the most upregulated gene across all samples, demonstrating the activators’ high specificity (Supplementary Fig. 15a). Additionally, single-cell quantitative analysis via fluorescence imaging showed that only the

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/albert_2017_genetic_and_epigenetic_control_of_gene_expression_by.pdf|albert_2017_genetic_and_epigenetic_control_of_gene_expression_by.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf|christian_2018_a_modular_dcas9_suntag_dnmt3a_epigenome_editing_system.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/yujuan_2025_dynamic_properties_of_transcriptional_condensates_modulate_crispra_mediated.pdf|yujuan_2025_dynamic_properties_of_transcriptional_condensates_modulate_crispra_mediated.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/agustin_2023_epigenetic_reactivation_of_tumor_suppressor_genes_with_crispra.pdf|agustin_2023_epigenetic_reactivation_of_tumor_suppressor_genes_with_crispra.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/alexander_2022_engineering_the_next_generation_of_car_t_cells.pdf|alexander_2022_engineering_the_next_generation_of_car_t_cells.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/andreas_2020_activation_of_silent_secondary_metabolite_gene_clusters_by.pdf|andreas_2020_activation_of_silent_secondary_metabolite_gene_clusters_by.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/anil_2021_mechanisms_of_enhancer_action_the_known_and_the.pdf|anil_2021_mechanisms_of_enhancer_action_the_known_and_the.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf|chenya_2021_spatiotemporal_control_of_crispr_cas9_gene_editing.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/fatma_2025_comparison_of_dcas9_activator_complexes_for_the_activation.pdf|fatma_2025_comparison_of_dcas9_activator_complexes_for_the_activation.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/jorge_2021_transcription_activation_is_enhanced_by_multivalent_interactions_independent.pdf|jorge_2021_transcription_activation_is_enhanced_by_multivalent_interactions_independent.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kachanov_2025.pdf|kachanov_2025.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf|kendall_2018_optimized_libraries_for_crispr_cas9_genetic_screens_with.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/mahata_2023_compact_engineered_human_mechanosensitive_transactivation_modules_enable_potent.pdf|mahata_2023_compact_engineered_human_mechanosensitive_transactivation_modules_enable_potent.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/ronghao_2023_enhancement_of_a_prime_editing_system_via_optimal.pdf|ronghao_2023_enhancement_of_a_prime_editing_system_via_optimal.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/tessa_2022_a_modular_dcas9_based_recruitment_platform_for_combinatorial.pdf|tessa_2022_a_modular_dcas9_based_recruitment_platform_for_combinatorial.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf|tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf]]
