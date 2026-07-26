---
type: reference
status: current
date: 2026-07-14
source: "notebooklm:dcas9-fto-granulosa/q01-activacion-eficiencia"
related:
  - "[[Notes/Dashboards/dCas9-p300 activation efficiency]]"
---

# Q05 - What gaps, limitations, or unanswered aspects remain in these sources regarding quantitative dCas9-p300 activation efficiency on endogenous human promoters (e.g., missing dose-response data, guide-position screens, or promoter-architecture comparisons)?

Based on the provided sources, several gaps and limitations remain regarding the quantitative understanding of **dCas9-p300** activation efficiency on endogenous human promoters. While the sources establish that the system is a potent activator, the following aspects remain largely unanswered or lack systematic data:

### 1. Missing Systematic Guide-Position Screens
The sources do not provide a high-resolution, systematic screen to determine the **optimal distance** from the transcription start site (TSS) specifically for p300 across a wide variety of human promoters. 
*   **Generalized Range:** While one source notes a general CRISPRa range of **-400 to -50 bp** for tiling, this is presented as a standard for many activators, not a result optimized for p300's unique mechanism  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf#Passage 2|[1]]].
*   **Specific gene focus:** Most quantitative data is limited to a small subset of genes (***ASCL1, MYOD1, NEUROD1, IL1RN***), leaving it unclear how these positional rules change for genes with different regulatory structures  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf#Passage 1|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 1|[3]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 9|[4]]].

### 2. Limited Promoter-Architecture Comparisons
There is a lack of comparative data analyzing how **different promoter architectures** (e.g., TATA-box vs. CpG island-rich promoters) dictate p300's efficiency.
*   **Enhancer vs. Promoter:** Sources establish that p300 can activate from both enhancers and promoters, which is unique compared to systems like dCas9-VP64  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf#Passage 1|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 1|[5]]]. However, they do not systematically quantify the efficiency of **promoter-targeted vs. enhancer-targeted** activation across different loci to see which is more robust.
*   **Basal Expression Context:** One source notes in a plant model that activation is stronger when the drought stress response is already active, suggesting chromatin "folding" matters  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf#Passage 1|[6]]]. Similar systematic comparisons of "pre-opened" vs. "highly compacted" human promoters are missing.

### 3. Lack of Systematic Dose-Response Data
The sources provide fold-change magnitudes for specific plasmid configurations but lack detailed **dose-response curves** relating the concentration of the dCas9-p300 complex to the level of mRNA induction. 
*   **Structural Efficiency:** Instead of protein dosage, the sources focus on **structural combinations** (e.g., p300 vs. p300+MV), showing that adding more activation domains via MS2-MCP enhances performance, but they do not define the saturation point for these effects  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 6|[7]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 2|[8]]].

### 4. Narrow Cell Type Diversity
Nearly all quantitative data regarding endogenous human gene activation with dCas9-p300 in these sources is derived from **HEK293T cells**  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf#Passage 1|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 1|[3]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 2|[8]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 16|[9]]]. 
*   **Primary Cell Challenges:** When tested in **primary adult human skin fibroblasts**, p300 fusions failed to improve reprogramming outcomes compared to simpler activators like VP192, suggesting its quantitative efficiency may be significantly lower or more complex in differentiated, non-immortalized cell types  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/jere_2018_human_pluripotent_reprogramming_with_crispr_activators.pdf#Passage 4|[10]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf#Passage 3|[11]]].

### 5. Unresolved Structural and Epigenetic Questions
*   **Spatial Exclusion Zones:** While one source mentions that the large size of the p300 core (and similar domains like Tet1-CD) creates **spatial accessibility issues** and potential **steric hindrance** when guides are placed close together (e.g., 118 bp), the exact "exclusion zone" is not defined  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 8|[12]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 17|[13]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 2|[14]]].
*   **Causality of the Mark:** A fundamental unanswered question noted is whether the regulatory impact is truly due to the **catalyzed epigenetic mark (H3K27ac)** or simply the physical recruitment of the large dCas9-p300 complex to the site  [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 3|[15]]].
*   **Global Off-Target Footprints:** While a global "methylation footprint" was noted for dCas9-DNMT3A, the sources state it remains to be seen if dCas9-p300 leaves similar **global off-target acetylation footprints** across the genome [16, 17].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf|PDF]]
- Texto literal:
> The application of dCas9 in forward screening using targeted transcription factors (TTFs) was shown to permit highly specific genome-scale transcription modulation (Gilbert et al., 2014; Konermann et al., 2015). Using combinations of 10 sgRNAs per gene, tiling −50 to +300 bp for repression (CRISPRi) or −400 to −50 bp for activation (CRISPRa) around the TSS to target nearly 1600 protein-encoding genes, human K562 cells were screened for growth phenotypes. In this study transcription was repressed using dCas9-KRAB and activated using dCas9-SunTag recruiting scFv– VP64 fusions (Gilbert et al., 2014). In a second screen, known as well as novel complexes and pathways involved in the response to a chimeric

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf|PDF]]
- Texto literal:
> Manipulating the epigenome and gene expression using TEMs and TTFs So far only a few studies have been published reporting the use of dCas9 fusions for epigenome editing and manipulating gene expression. The catalytic histone acetyltransferase (HAT) core domain p300 has been used to catalyse acetylation of histones in human HEK293T cells (Hilton et al., 2015). Targeting dCas9–p300 fusions to promoter regions or proximal or distant enhancers caused activation of gene expression. Increased expression upon enhancer-targeting was concomitant with enrichment in H3K27ac at the correspond- ing genomic target sites (Hilton et al., 2015). In most cases the same genes could be transactivated by dCas9-VP64 when targeted at promoters. To achieve transactivation both effectors can thus be used. The two effectors behave somewhat differently in terms of their impact on histone acetylation state, as p300 directly catalyses H3K27ac (Ogryzko et al., 1996; Delvecchio et al., 2013), whereas VP64 recruits subsequent transactivation components, amongst which is p300 (Memedula and Belmont, 2003). Also the histone acetyltransferase domain of the CREB-binding protein has been fused to dCas9 (dCas9-CBPHAT) and has been used to catalyse locus-specific acetylation of histones (Cheng et al., 2016). dCas9-CBPHAT was targeted using the Casilio (CRISPR/Cas9-Pumilio) system, which harbours an scRNA containing multiple PUF binding sites (PBS), to recruit additional CBPHAT domains via fusions with Pumilio/FBF (PUF) RNA-binding domains. Similar to dCas9-p300, targeting dCas9-CBPHAT to promoters or proximal and distal enhancer

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 9|Pasaje 9]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> vation by dCas9-VP64 [8, 9] and other CRISPRa systems [30]. Here we focused on 2VP, VP

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|PDF]]
- Texto literal:
> is to locally deposit H3K27ac marks. Therefore, in contrast to the local reduction of enhancer marks by dCas9-LSD1, recruitment of histone acetyl transferase P300 through dCas9 fusion (dCas9-P300) resulted in a significant increase in local H3K27ac levels at enhancer elements142. Importantly, unlike other dCas9-fused transactivators, which can result in induction of gene expression primarily from promoter regions, targeting dCas9-P300 allows significant gene expression induction from both promoter and enhancer regions142. Researchers have also exploited other epigenetic modifiers to manipulate additional epigenetic marks. Among these, dCas9 fusion to the PRDM9 methyltransferase fusion complex has been utilized to manipulate local H3K4me3 marks143. Notably, local induction of H3K4me3, which is a marker of active promoters, was observed to be sufficient to allow re-expression of silenced target genes in various cell types143. Histone de-acetylation has been another strategy to locally manipulate chromatin structure and function. To this end, dCas9 fusion to histone deacetylases (HDAC), specifically full-length HDAC3, has been shown to effectively reduce the H3k27ac at the target loci and reduce the gene expression of the target loci144.

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf|PDF]]
- Texto literal:
> Conclusion In addition to the use of modulators to aid the recruitment of RNA polymerase (Pol II) transcription machinery, the use of domains that modify chromatin folding is another interesting way to fine-tune gene expression. The expression of dCas9HAT allows acetylation of lysine 27 of Histone 3 (H3K27ac) favoring the unwind of chromatin and enhancing the interaction with transcriptional enhancers as the assembly of the transcriptional machinery (Fig. 5). This approach has been demonstrated in animals. In the present study, our main finding was that dCas9HAT positively regulates AREB1 and produces an enhanced drought stress response. It is noteworthy that dCas9HAT activity depends on the cellular context. The enhancer effect of dCas9HAT is stronger when the drought stress response is activated. This finding suggests that the chromatin folding at the AREB1 locus constitutes a regulatory mechanism for AREB1 gene expression. We also report that GUS expression varies based on number of sgRNAs used and their respective positions. Having a better understanding of the chromatin context of a specific locus will help in the rational design of CRISPRi/a strategies.

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 6|Pasaje 6]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> activity better than did direct VP64 fusion to the N-terminus of dCas9. dCas9-VP64+MCP-

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 16|Pasaje 16]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> paring activities in a systematic, controlled fashion. Here, we aimed to characterize and rationally

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/jere_2018_human_pluripotent_reprogramming_with_crispr_activators.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/jere_2018_human_pluripotent_reprogramming_with_crispr_activators.pdf|PDF]]
- Texto literal:
> We present a method for the efficient conversion of primary human fibroblasts into bona fide iPSCs based entirely on the transcriptional control of endogenous genes by CRISPRa. Acti-vation of core reprogramming factor promoters alone was sufficient but inefficient, whereas additional targeting of a common Alu element brought the efficiency close to established reprogramming methods (Supplementary Fig. 5c). The more complex activator domains did not improve reprogramming efficiency, which mirrors previously reported results for gene activation33, and suggests that the benefit of simple additional fused activation domains may be limited.

### Extracto 9
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf|PDF]]
- Texto literal:
> Challenge of the dCas9 constructs in a GUS reporter system. To evaluate the dCas9HAT construct, we set up a surrogate reporter system based on regulation of GUS reporter gene expression. We used the 170-bp minimal truncated version of the Glycine max ubiquitin promoter, herein designated GmUcesMin28,29. We selected two sgRNAs near the transcription start site (TSS) of GmUcesMin (Fig. 2A, Table S2). The efficiency of dCas9HAT in activating the GUS reporter system was quantified by its enzymatic activity. Seedlings of stably transformed Arabidopsis lines expressing dCas9HAT were incubated with Agrobacterium carrying Ti plasmids to perform transient ectopic expression of GmUcesMin-GUS in combination with the expression of one or two sgRNAs. Significantly elevated enzymatic activity was observed for sgRNA1 (~2.4-fold increase) and sgRNA2 (~2-fold increase), while enzymatic activity was elevated ~1.4-fold for the combination of the two sgRNAs. This result indicates that the expression of dCas9HAT enhanced the expression of the GUS gene in trans when targeted to GmUcesMin promoter. Remarkably, some substantial differences were noted depending on the location of the sgRNA and/or the sgRNA combination. Previous studies have suggested that the distance of the sgRNA from the TSS might influence the transcriptional regulation of the gene of interest. While some studies have reported that a specific sgRNA binding distance from the TSS (−50 bp to +300 bp) corresponds to higher target gene expression30,31, others have pointed out that dCas9 might generate steric hindrance and thus interfere with transcriptional machinery activities21,32. Regarding the construct GmUcesMin, our two sgRNAs are separated only by 118 bp. Considering the 3D conformation of the DNA, the 30 bp length occupied by the dCas9 on DNA33 and the space taken by the HAT domain, a steric hindrance effect could be responsible for destabilizing locally the protein complexes standing on DNA. Compared to the use of only one sgRNA, this collateral effect might result to lower gene expression rather than improve it.

### Extracto 10
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf#Passage 17|Pasaje 17]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|PDF]]
- Texto literal:
> vs. miniCMV. The strength of TRE3G induction was in the order of VP+MV>2VP>p300+MV>VP. Error bars

### Extracto 11
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|PDF]]
- Texto literal:
> Identifying the causal link between epigenetic marks and gene expression remains a central goal of chromatin biology. Thus, these aforementioned studies using dCas9 as a guidable platform to edit locus-specific epigenetic information will be an indispensable tool to achieve this. Now that the tools that enable us to alter the epigenome are in place, the next phase is to utilize them to better characterize regulatory elements and cellular states. To this end, researchers have already applied dCas9-based epigen-ome-editing tools for a number of exciting purposes including high-throughput screenings to characterize functional distal enhancers146, targeted reprogramming of lineage specifica-tion147,148, generation of induced pluripotent stem cells149, and reversal of HIV latency150. One of the remaining challenges is to elucidate the causal relationship between the presence of an epigenetic mark and its regulatory impact. Since the dCas9-fused epigenetic modifier remains associated with the target site, it is unclear whether the regulatory activity is due to the induced epigenetic mark or the complex. To this end, recent efforts using rapid and reversible epigenome-editing approaches are highly notable145. Future studies that enable rapid degradation of the targeting complex at the target site, such as with auxin-inducible degron technology151, should allow us to further characterize the functional consequences of epigenetic marks and investigate the associated temporal epigenetic memory for each mark.

### Extracto 12
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q01-activacion-eficiencia/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|PDF]]
- Texto literal:
> These aforementioned locus-specific epigenetic manipulation strategies are based on overexpression of a dCas9-fused epigenetic modifier complex. Such tools have been shown to specifically manipulate the expression of the target loci. However, whether overexpression of the fusion epigenetic complexes may leave a low level but global epigenetic footprint in the genome, as noted for the dCas9–DNMT3A fusion complex134, is yet to be determined. Therefore, novel strategies that enable local recruitment of endogenous epigenetic machineries may provide a higher precision in epigenetic editing. To this end, novel approaches such as Fkbp/Frb-based inducible recruitment for epigenome editing by Cas9 (FIRE–Cas9)145 may provide higher specificity in epigenetic editing by recruiting endogenous chromatin regulators.

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf|daan_2017_dcas9_a_versatile_tool_for_epigenome_editing.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/jere_2018_human_pluripotent_reprogramming_with_crispr_activators.pdf|jere_2018_human_pluripotent_reprogramming_with_crispr_activators.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf|joaquin_2019_improved_drought_stress_tolerance_in_arabidopsis_by_crispr.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf|kohei_2022_comparative_analysis_of_dcas9_vp64_variants_and_multiplexed.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/kenly_2020_prevention_of_tumor_risk_associated_with_the_reprogramming.pdf|kenly_2020_prevention_of_tumor_risk_associated_with_the_reprogramming.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q01-activacion-eficiencia/Sources/tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf|tianxiang_2023_crispr_cas9_therapeutics_progress_and_prospects.pdf]]
