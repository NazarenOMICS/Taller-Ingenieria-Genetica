---
type: notebook-source
source_id: "577d0136-4a1e-4d5e-a2f1-e49eb25013ef"
notebook_id: "997cd2ff-f1d7-42e0-9026-f046a1d2c7dd"
slug: "q14-dcas9p300-vs-otros-activadores"
vault_slug: "dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores"
project: "dcas9-fto-granulosa"
url: ""
source_type: web
status: active
date: 2026-07-14
pdf: "Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/yujuan_2025_dynamic_properties_of_transcriptional_condensates_modulate_crispra_mediated.pdf"
related:
  - "[[Notes/Dashboards/dCas9-p300 vs other activators]]"
used_in_qa: true
cited_in_count: 4
qa_notes:
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/QA/answers/2026-07-24 Q01 - according-to-these-sources-e-g.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/QA/answers/2026-07-24 Q02 - according-to-these-sources-what-mechanistic.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/QA/answers/2026-07-24 Q03 - according-to-these-sources-e-g.md]]"
  - "[[Notes/NotebookLM/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/QA/answers/2026-07-24 Q05 - according-to-these-sources-do-these.md]]"
---

# yujuan_2025_dynamic_properties_of_transcriptional_condensates_modulate_crispra_mediated.pdf

## PDF

![[Research/Papers/dcas9-fto-granulosa/q14-dcas9p300-vs-otros-activadores/yujuan_2025_dynamic_properties_of_transcriptional_condensates_modulate_crispra_mediated.pdf]]

## Source Guide

## Cited Passages

### Passage 1

Transcription factors (TFs) play a central role in eukaryotic gene regulation1–3. They consist of a DNA-binding domain (DBD) for sequence recognition and an activation domain (AD) that interacts with other transcriptional regulators to facilitate transcription4–6. To activate gene expression, nuclease-dead Cas9 (dCas9) variants have been fused to ADs, creating CRISPR activation (CRISPRa) systems7–9. Initially, dCas9-VP64 was developed as the first-generation activator, but it had limited efficiency10–13. To improve CRISPRa, second-

### Passage 2

CRISPRa tools modulate transcriptional bursting kinetics Numerous studies have shown that increasing the number of activation domains (ADs) recruited by each dCas9 is an effective strategy for optimizing CRISPRa7–9. The VPR system, which concatenates three ADs, can recruit more ADs when combined with the SunTag design than the corresponding PH system. Therefore, we utilized the SunTag system to construct SunTag3xVPR, SunTag5xVPR, and SunTag10xVPR systems and compared their performance with the VP64, SAM, VPR and SunTag10xPH systems (Fig. 1a). By tracing nascent transcripts produced at the sites of miniCMV-TriTagmTagBFP, we observed transcriptional bursts upon CRISPR activation, alternating between active (on) and inactive (off) states (Fig. 1b, c). Using this system, we examined how different CRISPRa systems regulate transcriptional bursting by analyzing burst duration, pause duration, and burst amplitude as indicators of transcriptional activity. Intriguingly, we observed significant variations in burst durations among all systems, while the duration of transcriptional silencing remained relatively consistent at around 13min. The dCas9-VP64 system displayed the shortest burst duration (14min), while the VPR and SAM systems exhibited burst durations of around 25min. The 10xPH system showed significantly extended burst durations (70min). Notably, the 3xVPR system demonstrated robust RNA production from miniCMV, outperforming the 10xPH system, with an average burst duration of approximately 95min. However, the 5xVPR and 10xVPR systems had shorter average burst durations compared to the 3xVPR system, at 37 and 50min, respectively (Fig. 1d). Furthermore, the burst amplitude of the 3xVPR system is comparable to that of the 10xPH system, yet significantly higher thanother systems (Fig. 1e). These findings collectively illustrate the capacity of CRISPRa tools to enhance transcriptional activation by prolonging burst durations and increasing burst amplitude. Additionally, our results uncover an unexpected phenomenon indicating a potential decline in the efficiency of CRISPR-SunTag activators as the number of SunTag-AD arrays increases.

### Passage 3

expression64–67. We performed antibody staining for endogenous Mediator complex subunit 1 (MED1) and directly imaged HaloTag-labeled endogenous p300 in living cells generated through CRISPR knockin. We found that both co-activators were enriched in condensates formed by 3xVPR, 10xVPR, 3xVPRF, and 10xVPRF, with colocalization ratios ranging from 81.8% to 99.5% (Fig. 6a–d). Further quantitative analysis indicated that the total fluorescence intensity of MED1 and p300within the condensates was significantly greater in the 10xVPR system than in the 3xVPR system. Correspondingly, the average nucleoplasmic signal of both co-activators outside the condensates was reduced in the 10xVPR system compared to the 3xVPR system. This trend was also observed in the 10xVPRF and 3xVPRF systems (Fig. 6e, f). These observations suggest that fewer MED1 and p300 molecules freely diffuse outside the condensates in the 10xVPR and 10xVPRF systems. Through 1,6-HD treatment and FRAP analysis, we found that the liquidity of p300wasconsistentwith thatofCRISPRa condensates. Specifically, p300 exhibited high liquidity in 3xVPR and 3xVPRF, whereas its liquidity was significantly reduced in 10xVPR and 10xVPRF (Fig. 6g, h). These results revealed that low liquidity in CRISPRa condensates can trap co-activators, resulting in the loss of gene activation capability. Our findings suggest that the dynamicity and liquidity of transcriptional condensates are crucial for effective transcriptional activity.

### Passage 4

mean ± SEM (n = 3 biological replicates). Each dot represents a biological replicate. Dots of the same color indicate that they are from the same batchof experiments. P values were determined by one-way ANOVA, comparing to the negative control (NC, dCas9 + sgNEUROD1) group. e A diagram summarizing the findings of this study. Increasing the number of SunTag-AD arrays (e.g., 3xVPR and 3xVPRF) results in liquid-like condensates and boosts the transcriptional activation of the CRISPRa-SunTagplatform.However, when the numberof SunTag scaffolds is increased to 10 or more, solid-like condensates form, sequestering co-activators such as p300 and MED1, which exhibit low dynamicity and liquidity, significantly reducing activation strength. We propose that optimal phase separation, reflecting appropriate multivalent interactions within the CRISPRa platform, creates a conducive microenvironment around the transcription start site for efficient activation. Source data are provided as a Source Data file.

### Passage 5

By examining the hallmark behaviors62 of phase separation (Sup-plementary Table 1), we conclude that 3xVPR and 3xVPRF form liquidlike transcriptional condensates through phase separation. On the other hand, the higher presence of scaffold sequences in the 10xVPR, 10xVPRF, PCP-12xVPRF, and PCP-40xVPRF systems facilitates the formation of more extensive molecular networks, resulting in solid-like transcriptional condensateswith reduceddynamicity and liquidity.We validated the localization of CRISPR activators and their activation capacities in HCT116 cells, and the results were consistent with those obtained inHeLa cells (Supplementary Fig. 14). To assess the specificity of CRISPR-SunTag activators forming TF condensates, we performed RNA-seq analysis on samples where individual CRISPRa systems (VPR, VPRF, 3xVPR and 3xVPRF) targeted HSPB8. The correlation in gene expression between each activator and the control sample was highly similar (R > 0.98), indicating that none of the activators broadly influenced gene expression. Notably, HSPB8 was consistently the most upregulated gene across all samples, demonstrating the activators’ high specificity (Supplementary Fig. 15a). Additionally, single-cell quantitative analysis via fluorescence imaging showed that only the

### Passage 6

Discussion The continuous improvement of CRISPRa technology is guided by a common principle: maximizing the recruitment of transcriptional activators near the transcription start site using the dCas9 system9,76–79. This strategy is analogous to the mechanism of super-enhancer activation, where TFs are highly enriched at transcription sites20. To achieve this goal, many CRISPR activators utilized SunTag to generate a repeating peptide array fused with multiple copies of activator domains (ADs)16–18. However, there is still much to explore and understand regarding the basic features of CRISPRa-mediated gene activation. In this study, we comprehensively compared different CRISPRa systems via quantitatively assessing transcriptional dynamics within the same cellular context. We discovered that the transcriptional activation capacity canbe enhancedby increasing thenumberof SunTag-AD arrays in CRISPR activators within a certain range. How-ever, exceeding this range, such as having ten copies of VPR, results in loosing activation capability. This observed pattern appears to be consistent across a wide range of SunTag activators by testing genes with varying expression levels in different cell types.

### Passage 7

Activation features of CRISPR-SunTag activators To determine the optimal assembly of activation domains for robust gene activation, we engineered different CRISPRa-SunTag systems with threeor ten arrays of ADs. Each array comprisedone, two, or three distinct ADs (Fig. 2a and Supplementary Fig. 8a). The common components in each comparison group (dCas9-3xADs vs. dCas9-10xADs) are scFV-AD and sgRNA. To ensure that the differences in gene activation are not due to varying expression levels of dCas9 fused with three or tenGCN4peptide arrays,weperformedWestern blot and flow cytometry analyses. Using GFP as the indicator, both methods indicated consistent expression levels of dCas9 fused with either 3 or 10 GCN4 peptide arrays (Supplementary Fig. 8b). We then evaluated the activation capacity using exogenous (miniCMV) and endogenous (HSPB1,HPDL and LMNA) reporter systemsby fluorescent imaging and FCM analysis. When fusing scFv with a single AD, including VP64, p65, Rta and HSF1, the highest activation efficiency was observed with 3xVP64 and 10xp65. Of note, VP64 consists of four VP16 copies (Sup-plementary Fig. 8c–f). We further compared 3x/10x/24xVP64 and 3x/ 10x/24xp65 systems and found that increasing the number of AD copies to 24 significantly reduced the activation strength. The activation ratio of 3xVP64 was higher than that of 10xVP64, but the activation strengthwas slightlyweaker than thatof 10xVP64 (Supplementary Fig. 9). Notably, 10xVP64 is the first developed CRISPR-SunTag systems16. When scFv was fused with two or three ADs, SunTag activators containing three copies of GCN4 repeats exhibitedmuch higher activation efficiency than those with ten copies (Fig. 2b–e). This consistent conclusion was observed for both single sgRNA and three sgRNAs used for CRISPRa. These results suggest that, in the SunTag system, harboring more copies of ADs does not necessarily lead to higher activation. Thus, it is crucial to determine the optimal number

### Passage 8

Results Visualization of CRISPRa-mediated gene activation at the singlecell level To better understand CRISPRa systems, we utilized our previously developed TriTag system49 to simultaneously image nascent RNA production and protein expression levels in live cells. We applied a miniCMV promoter to facilitate TriTagmTagBFP expression and a sgRNA targeting this promoter for CRISPRa. Using a lentiviral vector, we established a stable cell line by integrating miniCMV-TriTagmTagBFP into theHeLa cell genome. In this system, newly transcribedRNAswouldbe detected by stdMCP-tdTomato, while mTagBFP expression can be quantified through fluorescent imaging (Supplementary Fig. 1a). To conduct a comparative analysis of various CRISPRa systems, we used theDox-inducible TRE3G promoter for dCas9 expression and the CMV promoter for co-factors (Supplementary Fig. 1b). The dCas9-VP64,

### Passage 9

generation activators have been developed, including VPR (dCas9-VP64-p65-Rta)14, SAM (dCas9-VP64/sgRNA-p65-HSF1)15, SunTag10xVP64

### Passage 10

Incorporating multivalent molecules into the CRISPRa platform is likely an effective strategy to enhance gene activation80. IDR-rich proteins often have increased effective valence through nucleic acid binding or direct oligomerization81–84. FUS IDR (FUSn) has been proposed to function as a transcriptional activation domain that can recruit TFs and Pol II and mediate transcription68,85–87. Gene activation in the CRISPRa system increased with additional FUS IDRs, but excessive FUSn (e.g., ≥10) resulted in condensate resistance to 1,6-HD and reduced gene activation. Substituting the FUS IDR with NUP98 IDR or SMN1 resulted in condensates that were highly

### Passage 11

The term “transcriptional condensate” refers to nuclear compartments that concentrate biomolecules involved in transcription without implying that the formation of these structures is exclusively driven by phase separation26. Transcriptional condensates have been hypothesized to concentrate high levels of TFs and co-activators, which super-enhancers can trigger to regulate key cell identity genes20,24,91. The controversy surrounding the role of transcriptional condensates in gene activation could be explained by various factors, including the compositions or properties of condensates, as well as cell-type and gene-specific effects26,81,92. The material properties of heterotypic condensates depend on the relative abundance and interaction strengths of individual factors93–96. By manipulating the compositions and properties of CRISPRa-based transcriptional condensates, we found that gene activation strength correlates positively with the dynamicity and liquidity of condensates rather than the overall condensate formation. Additionally, our real-time imaging demonstrated that transcriptional condensates formed by 3xVPR and 3xVPRF were closely associated with transcription sites at certain time points. Under these conditions, transcription levels were significantly higher than when no condensates were present at the transcription sites. Our findings imply that these dCas9-guided transcriptional condensates may play a regulatory role in facilitating RNA bursts. However, the active transcription may also occur outside of condensates25,97. Based on our studies, we propose that an optimal phase-separated CRISPRa system could generate transcriptional condensates, which may not be visible but effectively concentrate transcription factors and coactivators near transcription sites through dynamic interactions with surrounding molecules (Fig. 7e). While larger, detectable condensates may not directly drive transcriptional activation, but must retain fluidity and dynamicity to facilitate the free diffusion of molecules. Collectively, our findings emphasize the significance of maintaining balanced homotypic and heterotypic interactions to ensure the proper functionality of condensates89,98.

### Passage 12

CRISPRa provides precise, versatile, and scalable methods for gene activation, enabling the study of gene function and regulation, as
