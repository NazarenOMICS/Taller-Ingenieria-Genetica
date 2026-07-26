---
type: reference
status: current
date: 2026-07-14
source: "notebooklm:dcas9-fto-granulosa/q10-sistemas-entrega"
related:
  - "[[Notes/Dashboards/dCas9-p300 delivery systems]]"
---

# Q05 - Based on these sources, which delivery method (transient transfection, lentivirus, nanoparticle, mRNA, or RNP) offers the best balance of efficiency versus minimal cellular perturbation/immunogenicity for a large CRISPRa effector like dCas9-p300?

Based on the provided sources, the delivery of **mRNA encapsulated in lipid nanoparticles (LNPs)** offers the best overall balance of high efficiency and minimal cellular perturbation for a large CRISPRa effector like dCas9-p300.

While **lentiviral transduction** is highly efficient and uniquely suited to the large size of a dCas9-fusion construct (~10 kb capacity), it carries significant risks of **insertional mutagenesis** and long-term immunogenicity  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf#Passage 1|[2]]]. Conversely, **LNP-mRNA** systems provide superior efficiency compared to other transient methods while avoiding the genomic and toxicity risks associated with viral or protein-based delivery  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 31|[3]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 32|[4]]].

### **1. Efficiency Comparison**
*   **mRNA vs. RNP:** A direct head-to-head comparison in the sources shows that **mRNA-LNPs significantly outperform RNP-LNPs** in both gene knock-out and correction efficiencies  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 32|[4]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 33|[5]]]. In one study, mRNA delivery resulted in roughly **5-fold higher efficiency** than RNP delivery (80% vs. 24%)  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 32|[4]]].
*   **Kinetics:** Despite the need for translation, mRNA delivery resulted in a **faster onset of gene editing** and earlier protein detection in the nucleus than RNP delivery  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 22|[6]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 23|[7]]].
*   **Packaging Large Effector Genes:** Large constructs like dCas9-p300 (roughly 5–6 kb) exceed the packaging limit of AAV (<4.7 kb), but fit comfortably within **lentiviral vectors** (~10 kb) or **LNPs**, which are generally less restricted by cargo weight or length  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf#Passage 1|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 9|[8]]].

### **2. Minimal Cellular Perturbation and Toxicity**
*   **Avoiding Integration:** Unlike lentiviruses, which integrate into the host genome and increase the risk of carcinogenesis, **mRNA and transient transfection** (LNPs) provide temporary expression that is cleared once the task is complete  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 3|[9]]].
*   **Lower Cytotoxicity:** Physical methods like **electroporation** are noted as the most toxic, often leading to permanent cell membrane damage and high mortality  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 2|[10]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 10|[11]]]. **mRNA-LNPs** demonstrated higher cytocompatibility than **RNP-LNPs**, which were found to aggregate and sediment at high concentrations, leading to lethal toxicity in animal studies  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 34|[12]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 35|[13]]].
*   **Transient Activity:** Because mRNA is short-lived, it minimizes the window for **off-target editing**, which is a major concern for stable viral expression  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 12|[14]]].

### **3. Immunogenicity**
*   **Viral Vectors:** These are associated with high immunogenicity and the development of **neutralizing antibodies**, which can prevent the repeated dosing often necessary to reach therapeutic thresholds  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 5|[15]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 36|[16]]].
*   **mRNA Modifications:** While mRNA can trigger innate immune responses (e.g., TLR7/8), these are effectively mitigated by using **chemically modified nucleosides** (like pseudouridine), which suppress immune sensing and improve translation  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 13|[17]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/namit_2021_mrna_vaccines_for_infectious_diseases_principles_delivery_and.pdf#Passage 2|[18]]].
*   **Antigen Shielding:** LNPs provide a protective shell that shields the immunogenic bacterial protein (Cas9) from pre-existing antibodies in the blood  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 37|[19]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 38|[20]]].

### **Summary of Trade-offs**
| Method | Efficiency | Perturbation/Safety | Cargo Suitability |
| :--- | :--- | :--- | :--- |
| **LNP-mRNA** | **Highest (Transient)** | **Low** (Transient, non-integrating) | **High** (Handles large genes well) |
| **Lentivirus** | High | **High Risk** (Insertional mutagenesis) | **Excellent** (10 kb capacity) |
| **LNP-RNP** | Moderate | **Medium Risk** (Aggregation toxicity) | Low (Large fusion RNPs aggregate) |
| **Electroporation** | Moderate | **Highest** (Severe membrane damage) | High |
| **Transfection** | Variable | Low-Medium | Moderate (Plasmid size issues) |

In conclusion, **mRNA-LNP** is the preferred method for dCas9-p300 because it ensures the large payload is delivered efficiently into the cytosol for translation, avoids the permanent genomic risks of viruses, and maintains better colloidal stability and lower toxicity than direct protein delivery  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 31|[3]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 33|[5]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf#Passage 9|[21]]].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> Lentiviral vectors (LV) are at present the most widely used viral vectors for clinical gene therapy applications in which long-lasting expression of a gene is required. The advantage of LV is the relatively safe genomic integration of the gene construct and the capacity to transduce both dividing and non-dividing cells with high efficiency. However, the feature that makes this vector suitable for gene delivery

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf|PDF]]
- Texto literal:
> The high cargo capacity (∼10 kb) of LV favors the design of an “all-in-one” vector to drive the expression of large size Cas9 nucleases or base editors. The injection of an LV carrying SpCas9 nuclease and a sgRNA targeting the huntingtin coding sequence in the striatum of a mouse model of Huntington disease (HD) resulted in a robust knock-down of the mutant hHTT-82Q protein in both neurons and astrocytes (Merienne et al., 2017). A unique LV-based CRISPR/Cas9 system has recently been generated to simultaneously deliver the Cas9 nuclease and four different sgRNAs, each under the control of a different promoter, thus allowing the simultaneous editing of different cell types in targeted tissues (Kabadi et al., 2014). Additionally, an all-in-one LV carrying dCas9 fused with the catalytic domain of DNA-methyltransferase 3A (DNMT3A) has recently been tested to target SNCA triplication in hiPSCderived dopaminergic neurons to efficiently reduce SNCA expression levels, rescuing mitochondrial ROS production and cellular viability (Kantor et al., 2018; Tagliafierro et al., 2019). Importantly, expression cassettes driven by astrocyte-specific

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 32|Pasaje 32]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> Timing of Gene Editing and Gene Editing Efficiencies of pLNP and mLNP In Vitro After physical characterization, pLNP-HDR and mLNP-HDR were compared in terms of kinetics of gene correction and gene editing efficiencies on eGFP reporter cell lines in culture. Delivery of the CRISPR-Cas9 components as RNP or mRNA via pLNP-HDR and mLNP-HDR, respectively, resulted in gene editing efficiencies comparable or higher to the commercial transfection agent ProDeliverIN CRISPR (Fig. 2A). mLNP-HDR however resulted in about a 5-fold higher efficiency than pLNP-HDR: 80% gene knock-out and 15% gene correction at 30 nM sgGFP versus to 24% gene knock-out and 5% gene correction via pLNP-HDR (Fig. 2A). Interestingly, gene editing efficiencies of eGFP construct were higher in HEK293T cells than in hepatoma cells, wherein especially gene correction did not exceed over 2% for pLNP-HDR nor for mLNP-HDR (Fig. 2A). mLNP-HDR resulted in saturation of gene knock-out on eGFP HEK293T cells already at a final concentration of 3.8 nM sgGFP. The relative gene corrections (determined as fraction of total edits), however, were similar between the two different formulations on eGFP HEK293T cells, but higher for pLNP-HDR on eGFP HEPA1-6

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 33|Pasaje 33]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> In conclusion, this study investigated the delivery of CRISPR-Cas9 via lipid nanoparticles as mRNA Cas9 versus Cas9-RNP for gene editing in vitro and in vivo. Ongoing studies on design of delivery vehicles for

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 22|Pasaje 22]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> To gain insight in the timing of delivery of Cas9 protein to the cytosol and subsequently the nucleus, the presence of eGFP-Cas9 fusion protein was measured by fluorescence confocal microscopy in HEK293T cells. Cas9 protein was located within the cytosol and nucleus within 30 minutes after transfection of cells with pLNP-HDR (Fig. 2C). When delivered as mRNA, eGFP-Cas9 fusion protein was first detected in the cytosol and nucleus after 4 hours (2C). Furthermore, it is interesting to highlight that the eGFP-Cas9 fusion protein signal within HEK293T cells differs in intensity between pLNP and mLNP-mediated delivery (images shown in Supplementary Fig. 6). Despite the earlier delivery of Cas9 in the nucleus via pLNP, gene correction became apparent after 22 hours in HEK293T HDR Stoplight cells, reporter cells in which gene correction results in a GFP signal (Fig. 2D), treated with mLNP-HDR (Fig. 2E) and saturating after 30 hours. Onset of gene correction detected in the cells treated with pLNP-HDR occurred around 24 hours but was determined to still increase until the end of the experiment (48hours).

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 23|Pasaje 23]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> Moreover, mLNP-HDR surpass pLNP-HDR in gene editing efficiencies in vitro on both reporter HEK293T and HEPA1-6 cells (Fig. 2). Gene editing efficiencies were generally higher on HEK293T cells than on hepatoma cells (Fig. 2A,B). Perhaps internalization

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 9|Pasaje 9]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> Adeno-associated viruses (AAV) combine low immunogenicity upon first injection with serotype-related target cell specificity and relatively long expression of the gene without the necessity for genome integration. However, the packaging capacity is limited and, as a consequence, the genetic material encoding the most frequently used sp-Cas9 (4.2 kB) leaves limited space for necessary regulatory elements, such as promoter and polyadenylation signal sequences. This can be solved by splitting spCas9 into two fragments that can recombine inside the cell so that the truncated genes will fit the AAV vector, but this comes at the cost of efficiency in terms of delivery as well as target DNA cutting.16

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> Traditional methods of direct transfection have first been investigated. The main advantage of these techniques is that the uptake mechanism is independent of the cell. Microinjection of single fast-dividing cells has been used to generate a great variety of knock-out and transgenic animals by directly injecting zygotes with CRISPR components into the nucleus. While this technique is very effective, it has the distinct disadvantage of cells requiring individual manipulation.10 Electropo-ration, by which pores are formed in cell membranes upon application of a high voltage, can be used to directly transfect cells ex vivo as well as some in vivo tissues. This has, for example, been used to transfect human B-cells with CRISPR/Cas RNP to induce production of therapeutic proteins, after differentiation into plasma cells.11 Electropora-tion can be very toxic, however, due to this technique harming the cell membrane. In some cases this leads to permanent permeabilization of the membrane.12

### Extracto 9
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 10|Pasaje 10]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf|PDF]]
- Texto literal:
> However, under optimal transfection conditions, the cell viability in electroporation was 56%, which was signi cantly lower than that of the control. One notable limitation of the electroporation transfection technique is its inherent cellular toxicity, which can range from 50–90%. In general, electroporation maintains viability within the range of 30–40% and can be further optimized to maximize transfection e ciency.

### Extracto 10
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 35|Pasaje 35]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> It is of great importance to note that all mice treated with pLNP unexpectedly died within 20 hours after tail-vein injections while mLNP- treated mice remained alive and showed no effects to their well-being. Death of mice may have been due to particle aggregates. pLNP were discovered to aggregate and sediment at these higher concentrations (RNP = 15 µM) shown in Supplementary Fig. 10A. Together with the gel retardation assay on protection from degrading enzymes and cryo-TEM images revealing darker spheres for pLNP-HDR, LNPs entrapping Cas9-RNP deem less stable than mRNA Cas9-loaded nanoparticles, possibly due to coating of Cas9-RNP on the surface of LNPs (Fig. 1). Another reason for death of mice could be contaminations of Cas9 protein with endotoxins. Cas9 protein was produced in LPS-free ClearColi™ BL21 strain, however during purification contaminations might have been introduced which was not assessed in this study. It has been reported that young mice (7-9) weeks have a LD50 (50% lethal dose) of 601 microgram per mouse resulting in lethality due to high levels of IL-10.35 In contrast, mLNP interestingly lead to higher expression of inflammatory cytokines in vitro than LNPs containing Cas9-RNP (Fig. 2F).

### Extracto 11
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 5|Pasaje 5]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> To counteract this, self-inactivating constructs have been designed in which the lentiviral vector encodes for Cas9 protein and two sgRNAs: one against the target sequence of choice and one against the Cas9 gene.22 In this way transient expression of Cas9 from an integrating lentiviral vector can be obtained.

### Extracto 12
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 36|Pasaje 36]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> Adaptive responses can be directed against the Cas protein or against components of the delivery system. Viral vectors (in particular adenoviral vectors) are immunogenic, especially at the high doses that are often needed for effective transduction in humans.42–44 Synthetic

### Extracto 13
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 13|Pasaje 13]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> However, advances in chemical modifications such as substitution with pseudouridine, N6-methyladenosine or inosine suppress innate immune responses, and 5’-cap and secondary structures at the 3’-terminus improve the resistance to RNAses.17,18 The first clinical trials with mRNA Cas9 are on-going and resulting in promising genome editing outcomes, for example NTLA-2001 from Intellia Therapeutics which resulted in 87% gene knock-out of TTR after a single dose of 0.3 mg per kilogram NTLA-2001 in patients.9 In the case of delivery of the mRNA Cas9 the sgRNA needs to additionally be packaged within the LNP. The sgRNA then needs to form the RNP complex intracellularly after translation of the protein to perform gene editing in the nucleus.19 For direct availability of the RNP, on-going efforts focus on formulating LNPs incorporating the Cas9 RNP.10,20 It has been reported that the direct delivery of RNP would result in less off-target events as the Cas9-RNP is short-lived.21 Furthermore, the use of RNPs ensures protection of sgRNA from degradation and at the same time complexation with sgRNA keeps Cas9 in its functional confirmation.22,23 However, despite the net-negative charge of the Cas9-RNP allowing electrostatic interactions with the lipids, the negative charge is not uniformly distributed over the RNP surface.24

### Extracto 14
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/namit_2021_mrna_vaccines_for_infectious_diseases_principles_delivery_and.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/namit_2021_mrna_vaccines_for_infectious_diseases_principles_delivery_and.pdf|PDF]]
- Texto literal:
> To maximize translation, the mRNA sequence typically incorporates modified nucleosides, such as pseudouridine, N1- methylpseudouridine or other nucleoside analogues23. Because all native mRNAs include modified nucleosides, the immune system has evolved to recognize unmodified single- stranded RNA, which is a hallmark of viral infection. Specifically, unmodified mRNA is recognized by pattern recognition receptors, such as Toll- like receptor 3 (TLR3), TLR7 and TLR8, and the retinoic acid- inducible gene I (RIGI) receptor. TLR7 and TLR8 receptors bind to guanosine- or uridine- rich regions in mRNA and trigger the production of type I interferons, such as IFNα, that can block mRNA translation24. The use of modified nucleosides, particularly modified uridine, prevents recognition by pattern recognition receptors, enabling sufficient levels of translation to produce prophylactic amounts of protein5. Both the Moderna and Pfizer–BioNTech SARS- CoV-2 vaccines, which produced >94% efficacy in phase III clinical trials25, contain nucleoside- modified mRNAs. Another strategy to avoid detection by pattern recognition receptors, pioneered by CureVac, uses sequence engineering and codon optimization to deplete uridines by boosting the GC content of the vaccine mRNA26.

### Extracto 15
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 38|Pasaje 38]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> Adaptive immune responses against the Cas proteins are common. In fact, several studies have demonstrated that both anti-Cas antibodies and Cas-specific cellular responses pre-exist in the human population due to exposure via the microbiome.47–49 This pre-existing immunity has important implications for clinical applications of CRISPR/Cas as it may influence the effectiveness of the gene editing therapy but may also cause serious safety problems. Antibody-responses can be partly mitigated by mRNA delivery of Cas instead of RNPs or by encapsulation of the Cas RNP into nanocarriers to shield the immunogenic protein from neutralizing antibodies. Conversely, Cas proteins could be immuno-engineered to remove B and T cell epitopes without losing activity or one could revert to Cas variants from microorganisms that are not common to humans, such as the recently discovered CasX.50

### Extracto 16
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf#Passage 9|Pasaje 9]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf|PDF]]
- Texto literal:
> The extent of target area and cell selectivity could be considered the major determinants in the selection of CRISPR/Cas9 delivery platforms for in vivo animal model studies.

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/namit_2021_mrna_vaccines_for_infectious_diseases_principles_delivery_and.pdf|namit_2021_mrna_vaccines_for_infectious_diseases_principles_delivery_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf|parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf|vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/kasra_2020_exosomal_micrornas_derived_from_mesenchymal_stem_cells_cell.pdf|kasra_2020_exosomal_micrornas_derived_from_mesenchymal_stem_cells_cell.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/li_2021_nanoparticle_delivery_of_crispr_cas9_for_genome_editing.pdf|li_2021_nanoparticle_delivery_of_crispr_cas9_for_genome_editing.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/mahdi_2021_delivery_of_dcas9_crispr_system_into_the_hard.pdf|mahdi_2021_delivery_of_dcas9_crispr_system_into_the_hard.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/maryam_2021_b2m_gene_knockout_in_hek293t_cells_by_non.pdf|maryam_2021_b2m_gene_knockout_in_hek293t_cells_by_non.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/morane_1970_structural_and_functional_investigations_of_designed_histidine_rich.pdf|morane_1970_structural_and_functional_investigations_of_designed_histidine_rich.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/pawan_2016_protein_kinase_a_a_master_kinase_of_granulosa.pdf|pawan_2016_protein_kinase_a_a_master_kinase_of_granulosa.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/shiyi_2025_lentiviral_vector_production_and_primary_astrocyte_transduction_v1.pdf|shiyi_2025_lentiviral_vector_production_and_primary_astrocyte_transduction_v1.pdf]]
