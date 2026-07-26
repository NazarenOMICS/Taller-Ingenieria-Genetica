---
type: reference
status: current
date: 2026-07-14
source: "notebooklm:dcas9-fto-granulosa/q10-sistemas-entrega"
related:
  - "[[Notes/Dashboards/dCas9-p300 delivery systems]]"
---

# Q06 - What gaps remain in these sources regarding delivery of dCas9-p300 specifically (as opposed to Cas9 nuclease or smaller dCas9 fusions) into KGN, COV434, or primary human granulosa cells?

The provided sources reveal several significant gaps regarding the delivery of the **dCas9-p300** effector specifically into **KGN, COV434**, or **primary human granulosa cells**. While the sources discuss the general mechanics of large CRISPR effectors and experiments in rat granulosa cells, they lack specific data on these human models.

### **1. Total Absence of Data on Specific Human Cell Lines**
A primary gap is that **none of the sources mention KGN or COV434 cell lines**. These are standard human granulosa-derived tumor cell lines often used for research, but the sources focus their granulosa cell data almost exclusively on **primary rat granulosa cells**  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/pawan_2016_protein_kinase_a_a_master_kinase_of_granulosa.pdf#Passage 3|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/kasra_2020_exosomal_micrornas_derived_from_mesenchymal_stem_cells_cell.pdf#Passage 2|[2]]]. Consequently, there is no information regarding the specific transfection efficiencies or cellular perturbations these human cell lines might experience when exposed to large CRISPR constructs.

### **2. Lack of Experiments on Primary Human Granulosa Cells**
While the sources mention that exosomes can protect "ovarian granulosa cells" from stress *in vitro*  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/pawan_2016_protein_kinase_a_a_master_kinase_of_granulosa.pdf#Passage 4|[3]]], they do not provide experimental protocols or results for the delivery of dCas9-p300 into **primary human** samples. Most primary cell research in these documents utilizes:
*   **Primary rat granulosa cells:** Transduced via lentivirus to study signaling  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/pawan_2016_protein_kinase_a_a_master_kinase_of_granulosa.pdf#Passage 3|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/kasra_2020_exosomal_micrornas_derived_from_mesenchymal_stem_cells_cell.pdf#Passage 2|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/mahdi_2021_delivery_of_dcas9_crispr_system_into_the_hard.pdf#Passage 1|[4]]].
*   **Human fibroblasts (HFF):** Used as a model for "hard-to-transfect" cells via magnetofection  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/mahdi_2021_delivery_of_dcas9_crispr_system_into_the_hard.pdf#Passage 7|[5]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 4|[6]]].
*   **Primary astrocytes:** Transduced via lentiviral vectors  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf#Passage 10|[7]]].

### **3. Payload-Specific Gaps for dCas9-p300**
The sources identify dCas9-p300 as an epigenome editing tool used to boost transcriptional activation at enhancers and promoters  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 9|[8]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/li_2021_nanoparticle_delivery_of_crispr_cas9_for_genome_editing.pdf#Passage 3|[9]]]. However, they do not address the specific logistical hurdles of delivering a protein of this size compared to standard Cas9:
*   **Cargo Size Constraints:** Standard SpCas9 is roughly 4.2–4.5 kb  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 39|[10]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 33|[11]]]. Fusing the p300 catalytic domain creates a much larger genetic payload (potentially exceeding 5–6 kb). While sources mention that next-generation components are larger and thus more challenging for delivery and uptake  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf#Passage 5|[12]]], they do not provide a direct efficiency comparison for dCas9-p300 specifically.
*   **mRNA and RNP Format for Fusions:** One source concludes that **mRNA delivery is superior to RNP delivery** for CRISPR-Cas9 because it results in smaller nanoparticles and higher efficiency  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 17|[13]]]. However, this study focused on Cas9 nuclease. It remains a gap whether these benefits hold for **dCas9-p300 mRNA**, which would be significantly longer and potentially more prone to degradation or misfolding.
*   **AAV Limitations:** The sources emphasize that AAV has a strict packaging limit of **<4.7 kb**  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 39|[10]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 28|[14]]]. While they discuss using split-Cas9 systems to bypass this  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf#Passage 11|[15]]], there is no specific discussion of using split systems to deliver the dCas9-p300 fusion.

### **4. Safety and Immunogenicity in Granulosa Cells**
The sources discuss general toxicities, such as the lethal aggregation of Cas9-RNP LNPs in mice [16] or the inflammatory cytokine release triggered by mRNA LNPs [17]. There is a complete lack of information on:
*   Whether human granulosa cells exhibit specific **innate immune responses** to the lipids or large mRNA transcripts required for dCas9-p300.
*   The **off-target epigenetic effects** of dCas9-p300 in human granulosa cells. One source notes that dCas9-fused modifiers can leave a "global epigenetic footprint" independent of the sgRNA [18], but this has not been validated in a granulosa cell context.

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/pawan_2016_protein_kinase_a_a_master_kinase_of_granulosa.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/pawan_2016_protein_kinase_a_a_master_kinase_of_granulosa.pdf|PDF]]
- Texto literal:
> Granulosa Cell Culture and Lentiviral Transduction. All experimental protocols involving the use of animal were approved by and conducted in accordance with the guidelines of the University of Pittsburgh Institutional Animal Care and Use Committee. Sexually immature female rats (24 day old) were purchased from Hilltop Lab Animals (Scottdale, PA) and ovaries were isolated and GCs collected as described previously1. For viral transduction, isolated granulosa cells were suspended into M199 containing 8 μ g/ml polybrene (hexadimethrin bromide, catalog item 52495; Fluka/Sigma-Aldrich Corp., St. Louis, MO). For each well of a 12-well culture plate, GCs were placed into individual 5 ml polypropylene culture tubes in a total volume of 0.3 ml that contained 8 μ g/ml polybrene, ~2.5 × 106 GCs and 5 × 106 PFU of either the PKA-CQR or EGFP lentiviral vectors. Tubes were centrifuged in an Eppendorf 5810 R centrifuge for four 30 min. intervals at 1,200 × g at 37 C. After each 30 min. centrifugation, cell pellets were gently resuspended and after the final centrifugation, the entire 0.3 ml of the transduction mixture was transferred into individual wells of a 12-well tissue culture plates previously coated with donor calf serum that contained 0.7 ml M199 with 30 ng/ml testosterone. Cells were exposed to FSH at the time of plating as described in the figure legends.

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/kasra_2020_exosomal_micrornas_derived_from_mesenchymal_stem_cells_cell.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/kasra_2020_exosomal_micrornas_derived_from_mesenchymal_stem_cells_cell.pdf|PDF]]
- Texto literal:
> 81. Sun L, Li D, Song K, Wei J, Yao S, Li Z, Su X, Ju X, Chao L, Deng X. Exosomes derived from human umbilical cord mesenchymal stem cells protect against cisplatin-induced ovarian granulosa cell stress and apoptosis in vitro. Sci Rep. 2017;7(1):2552.

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/pawan_2016_protein_kinase_a_a_master_kinase_of_granulosa.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/pawan_2016_protein_kinase_a_a_master_kinase_of_granulosa.pdf|PDF]]
- Texto literal:
> Results and Discussion Signaling pathways activated by FSH and by PKA-CQR. The ideal experimental paradigm to estab- lish whether PKA is sufficient to activate intracellular signaling pathways that are associated with FSH stimulation of GC differentiation would be to conduct a detailed timecourse of phospho-protein expression in response to FSH and PKA-CQR. However, the inherent difficulty in comparing the intracellular signaling pathways activated by FSH versus PKA-CQR in GCs is that the time-course for FSH activation is rapid and transient such that maximal stimulation typically occurs within the first 20 min. and declines to near basal levels by 60 min.7. By contrast, activation of signaling pathways by PKA-CQR is dependent upon the time required for the expression of the len-tivirus-directed recombinant protein. During this period, the catalytic activity of the recombinant protein in GCs would progressively increase such that a rapid activation in PKA activity, within the time frame seen with FSH, could not be achieved. We explored a number of approaches that would enable us to acutely activate PKA-CQR in GCs. These included a chemical genetic approach of mutating the ATP binding pocket within PKA-CQR to confer unique sensitivity to a novel reversible inhibitor that could subsequently be washed out to initiate kinase activity17 as well as the construction of a PKA-CQR estrogen receptor fusion protein that would permit rapid activation of PKA by tamoxifen18. In results not reported herein, we found that neither approach was successful in generating a recombinant PKA-CQR mutant that could be acutely activated in GCs. Accordingly, we conducted a timecourse of PKA activity in GCs transduced with the lentiviral PKA-CQR using the phosphorylation of CREB (P-CREB) as an index of activity because CREB is directly phosphorylated by PKA at Ser1338. We found that 24 hr. post transduction with the PKA-CQR lentiviral vector was the earliest timepoint that we observed consistent phosphorylation of CREB to an extent similar to that seen following stimulation with FSH. Therefore in all experiments reported herein, we evaluated the activation of signaling pathways by PKA-CQR 24 hr. after viral transduction of GCs and compared the extent of activation of the pathways with FSH following stimulation for 20 min. and 24 hr.

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/mahdi_2021_delivery_of_dcas9_crispr_system_into_the_hard.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/mahdi_2021_delivery_of_dcas9_crispr_system_into_the_hard.pdf|PDF]]
- Texto literal:
> that the magnetofection method with an efficiency around 85.7% for HEK-293 and 28.2% for HFF.

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/mahdi_2021_delivery_of_dcas9_crispr_system_into_the_hard.pdf#Passage 7|Pasaje 7]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/mahdi_2021_delivery_of_dcas9_crispr_system_into_the_hard.pdf|PDF]]
- Texto literal:
> Lipofectamine. The transfection efficiency was determined as EGF intensity to be around 28.2% for

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|PDF]]
- Texto literal:
> is to locally deposit H3K27ac marks. Therefore, in contrast to the local reduction of enhancer marks by dCas9-LSD1, recruitment of histone acetyl transferase P300 through dCas9 fusion (dCas9-P300) resulted in a significant increase in local H3K27ac levels at enhancer elements142. Importantly, unlike other dCas9-fused transactivators, which can result in induction of gene expression primarily from promoter regions, targeting dCas9-P300 allows significant gene expression induction from both promoter and enhancer regions142. Researchers have also exploited other epigenetic modifiers to manipulate additional epigenetic marks. Among these, dCas9 fusion to the PRDM9 methyltransferase fusion complex has been utilized to manipulate local H3K4me3 marks143. Notably, local induction of H3K4me3, which is a marker of active promoters, was observed to be sufficient to allow re-expression of silenced target genes in various cell types143. Histone de-acetylation has been another strategy to locally manipulate chromatin structure and function. To this end, dCas9 fusion to histone deacetylases (HDAC), specifically full-length HDAC3, has been shown to effectively reduce the H3k27ac at the target loci and reduce the gene expression of the target loci144.

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf#Passage 10|Pasaje 10]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf|PDF]]
- Texto literal:
> et al., 2016) and histones (i.e., LSD1, a histone demethylase that removes H3K4me2) (Kearns et al., 2015) or promote histone H3K27 acetylation (i.e., p300 catalytic domain) (Hilton et al., 2015) can be applied to activate target genes. A complete list of Cas9-based tools for epigenome editing has been reviewed in (Liu and Jaenisch, 2019).

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 9|Pasaje 9]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> Adeno-associated viruses (AAV) combine low immunogenicity upon first injection with serotype-related target cell specificity and relatively long expression of the gene without the necessity for genome integration. However, the packaging capacity is limited and, as a consequence, the genetic material encoding the most frequently used sp-Cas9 (4.2 kB) leaves limited space for necessary regulatory elements, such as promoter and polyadenylation signal sequences. This can be solved by splitting spCas9 into two fragments that can recombine inside the cell so that the truncated genes will fit the AAV vector, but this comes at the cost of efficiency in terms of delivery as well as target DNA cutting.16

### Extracto 9
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/li_2021_nanoparticle_delivery_of_crispr_cas9_for_genome_editing.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/li_2021_nanoparticle_delivery_of_crispr_cas9_for_genome_editing.pdf|PDF]]
- Texto literal:
> However, regardless of the delivery cargo, it is challenging for the CRISPR/Cas9 to enter cells. Due to its considerable molecular weight (the genetic size of Cas9 ~4.5 kb) and its poor stability, finding a more suitable nano-delivery method for the various Cas9 components is vital. When designing and preparing a delivery system, it is necessary to focus on maintaining the nuclease activity of Cas9 and protecting the RNP against proteases, nucleases, antibodies, and T cell recognition in the serum and body fluids. Once entering the target cell, the delivery system should help the RNP be released from the endosome to the cytoplasm and enable its function.

### Extracto 10
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 39|Pasaje 39]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> The emerging technologies face challenges as well, however. The main challenge will again be in design of delivery vehicles to expand from ex vivo applications to in vivo.46,53,54 These newer gene editing molecular components are even larger than CRISPR-Cas9, which could result in larger nanoparticles and thereby more challenges in delivery, circulation, and tissue and cellular uptake. Additionally, studies investigating the risk of off-target events need to be performed and ethical concerns need to be addressed.

### Extracto 11
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 33|Pasaje 33]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> In conclusion, this study investigated the delivery of CRISPR-Cas9 via lipid nanoparticles as mRNA Cas9 versus Cas9-RNP for gene editing in vitro and in vivo. Ongoing studies on design of delivery vehicles for

### Extracto 12
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf#Passage 5|Pasaje 5]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf|PDF]]
- Texto literal:
> AAV delivery of base and epigenome editors is complicated by the low cargo capacity of the AAV genome. An innovative strategy to overcome this limitation is based on the design of dual intein-split AAV vectors. The first N-intein vector harbors the cytidine or adenine deaminase enzyme fused to the N-terminal portion of nCas9 and is flanked by the N-terminal intein moiety from the Nostoc punctiforme (Npu). The second N-intein vector carries the C-terminal intein moiety fused to the C-terminal portion of nCas9 in frame with the UGI (only for CBE) and a second expression cassette for the sgRNA (Villiger et al., 2018; Levy et al., 2020; Lim et al., 2020). Split inteins associate posttranslationally in a traceless manner, allowing the fusion of the N-and C-terminal portions of nCas9 enzyme in the co-transfected cells and the generation of a fully functional enzyme. Integration of intein-split CBEs and ABEs in optimized vectors (PHP.eB and Anc80) enabled the efficient and robust base editing of DNMT1 upon ICV and retro-orbital injections leading to the correction of Npc1I1061T mutation in a mouse model of Niemann–Pick disease type C (Levy et al., 2020).

### Extracto 13
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 28|Pasaje 28]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> LNPs encapsulating Cas9-RNP or mRNA Cas9 were compared on stimulation of inflammatory cytokines after treatment of DCs with LNPs via qPCR. mLNP-HDR triggered 13-fold higher expression of IFN-α to mDCs while pLNP-HDR resulted in a 5-fold expression at 30 nM sgRNA (Fig. 2F). Cytokines TRAF6 and TNF-α were only expressed 3-fold and 5-fold, respectively, higher than mDCs after treatment with pLNP-HDR, while mLNP-HDR upregulated expression of IL-12 and IL-10.

### Extracto 14
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf#Passage 11|Pasaje 11]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf|PDF]]
- Texto literal:
> Beside the sgRNA-dependent off-target effects that could be prevented by using high-fidelity dCas9, the permanent expression of an epigenome editor may produce non-specific epigenetic modifications resulting in long-range epigenetic changes that could influence the expression of other nontarget genes (Groner et al., 2010). Galonska et al. (2018) observed genome-wide gRNA-independent off-target activity, by tracking the dCas9–DNMT3A footprint in a murine embryonic stem cell line and in two somatic human cell lines. A combination of KRAB, DNMT3A, and DNMT3L has recently been applied to provide stable and highly specific DNA methylation at the target locus, which is increased in the presence of CpG-free boundaries flanking the targeted CpG islands that could prevent the spreading of the epigenetic modifications to neighboring genes and reduce off-target effects (Amabile et al., 2016).

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/kasra_2020_exosomal_micrornas_derived_from_mesenchymal_stem_cells_cell.pdf|kasra_2020_exosomal_micrornas_derived_from_mesenchymal_stem_cells_cell.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/li_2021_nanoparticle_delivery_of_crispr_cas9_for_genome_editing.pdf|li_2021_nanoparticle_delivery_of_crispr_cas9_for_genome_editing.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/mahdi_2021_delivery_of_dcas9_crispr_system_into_the_hard.pdf|mahdi_2021_delivery_of_dcas9_crispr_system_into_the_hard.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/pawan_2016_protein_kinase_a_a_master_kinase_of_granulosa.pdf|pawan_2016_protein_kinase_a_a_master_kinase_of_granulosa.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf|vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/maryam_2021_b2m_gene_knockout_in_hek293t_cells_by_non.pdf|maryam_2021_b2m_gene_knockout_in_hek293t_cells_by_non.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/morane_1970_structural_and_functional_investigations_of_designed_histidine_rich.pdf|morane_1970_structural_and_functional_investigations_of_designed_histidine_rich.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/namit_2021_mrna_vaccines_for_infectious_diseases_principles_delivery_and.pdf|namit_2021_mrna_vaccines_for_infectious_diseases_principles_delivery_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf|parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/shiyi_2025_lentiviral_vector_production_and_primary_astrocyte_transduction_v1.pdf|shiyi_2025_lentiviral_vector_production_and_primary_astrocyte_transduction_v1.pdf]]
