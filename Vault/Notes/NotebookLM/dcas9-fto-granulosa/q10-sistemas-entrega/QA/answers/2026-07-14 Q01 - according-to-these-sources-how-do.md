---
type: reference
status: current
date: 2026-07-14
source: "notebooklm:dcas9-fto-granulosa/q10-sistemas-entrega"
related:
  - "[[Notes/Dashboards/dCas9-p300 delivery systems]]"
---

# Q01 - According to these sources, how do chemical transfection, electroporation, and lentiviral transduction compare in efficiency and cellular perturbation for delivering large CRISPR/dCas9 constructs?

For delivering large CRISPR/dCas9 constructs, the sources compare chemical transfection, electroporation, and lentiviral transduction based on their ability to handle large cargo, their delivery efficiency, and the level of cellular perturbation (toxicity, immunogenicity, and genomic risk).

### **Efficiency Comparison**
Efficiency varies significantly based on the cell type and the specific delivery vehicle used within each method category.

*   **Chemical Transfection:** In direct comparative studies using Vero cells, chemical methods—specifically cationic polymers—often outperformed physical and viral methods  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 1|[1]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 2|[2]]]. **TurboFect, a cationic polymer, achieved the highest efficiency in Vero cells at 46.5%**, surpassing both Lipofectamine 2000 (42%) and electroporation (~38.8%)  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 3|[3]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 4|[4]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 5|[5]]]. In easier-to-transfect cells like HEK293T, chemical methods such as **magnetofection (PEI-coated magnetic nanoparticles) and lipofection reached very high efficiencies of 85.7% and 83.2%**, respectively  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/mahdi_2021_delivery_of_dcas9_crispr_system_into_the_hard.pdf#Passage 1|[6]]]. 
*   **Electroporation:** This method is highly effective for suspension cultures and cells that are typically difficult to transfect  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 6|[7]]]. While it reached 38.8% efficiency in Vero cells under optimized voltage (300V), it was noted to be less efficient than TurboFect in that specific context  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 2|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 7|[8]]].
*   **Lentiviral Transduction:** Lentiviral vectors (LV) are highly efficient at delivering transgenes to a wide range of mammalian cells, including primary and non-dividing cells  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 1|[9]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 8|[10]]]. However, they can be hindered by cell-specific innate responses; for instance, **LV transduction in Vero cells was limited to roughly 15.2% efficiency** due to post-entry restrictions like the TRIM5 protein  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 9|[11]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 10|[12]]].

### **Cellular Perturbation and Safety**
The trade-off for high efficiency is often a significant increase in cellular stress or long-term genomic risk.

*   **Toxicity:** **Electroporation is the most toxic method**, as it relies on applying a high-voltage pulse to create nanometer-level pores in the cell membrane, which can lead to permanent permeabilization or cell death  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 6|[7]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 2|[13]]]. In Vero cell experiments, electroporation maintained a lower viability (~56–67%) compared to chemical methods  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 2|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 7|[8]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 10|[12]]]. Chemical transfection is generally less damaging to the cell membrane, though some reagents like **PEI (polyethylenimine) exhibit higher cytotoxicity** due to their high charge density and ability to depolarize mitochondria  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 6|[7]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 11|[14]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 12|[15]]].
*   **Genomic Risk:** Lentiviral transduction carries a **high risk of insertional mutagenesis** because the viral vector integrates the construct into the host cell genome  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 2|[2]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 3|[16]]]. Furthermore, the stable, long-lasting expression of Cas9 provided by LV is often considered unfavorable as it increases the window for off-target editing  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 1|[9]]]. Chemical and physical methods are typically used for transient delivery, reducing these genomic risks  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 4|[17]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/li_2021_nanoparticle_delivery_of_crispr_cas9_for_genome_editing.pdf#Passage 1|[18]]].
*   **Immunogenicity:** Viral vectors are associated with high immunogenicity, and pre-existing antibodies in humans can neutralize the vectors before they reach target cells  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 8|[10]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 5|[19]]]. Non-viral chemical vehicles like lipid nanoparticles (LNPs) can shield cargo from immune recognition, although they may still trigger innate immune responses through pathways like TLR4  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 6|[20]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 7|[21]]].

### **Suitability for Large Constructs**
The size of CRISPR/dCas9 components (approximately 160 kDa for the SpCas9 protein and ~4 kb for the gene) poses a major delivery challenge  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 8|[22]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 1|[23]]].

*   **Viral Constraints:** Adeno-associated viruses (AAV) are severely limited by a packaging capacity of <4.4–4.7 kb, making them unsuitable for carrying a full SpCas9 gene alongside required regulatory elements  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 9|[24]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/li_2021_nanoparticle_delivery_of_crispr_cas9_for_genome_editing.pdf#Passage 2|[25]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf#Passage 1|[26]]]. **Lentiviral vectors have a much larger capacity (~8–10 kb)**, allowing them to carry "all-in-one" large dCas9/sgRNA constructs more easily  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 3|[16]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/mahdi_2021_delivery_of_dcas9_crispr_system_into_the_hard.pdf#Passage 2|[27]]].
*   **Non-Viral Versatility:** Chemical (nanoparticles) and physical (electroporation) methods are generally **less restricted by the molecular weight or length of the cargo** compared to viral vectors  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/li_2021_nanoparticle_delivery_of_crispr_cas9_for_genome_editing.pdf#Passage 2|[25]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/mahdi_2021_delivery_of_dcas9_crispr_system_into_the_hard.pdf#Passage 3|[28]]] [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/li_2021_nanoparticle_delivery_of_crispr_cas9_for_genome_editing.pdf#Passage 3|[29]]]. Chemical vehicles can be engineered for high packaging capacity and have been optimized to deliver dCas9 in plasmid, mRNA, or ribonucleoprotein (RNP) formats  [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/li_2021_nanoparticle_delivery_of_crispr_cas9_for_genome_editing.pdf#Passage 4|[30]]].

---

## Extractos citados verbatim

### Extracto 1
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf|PDF]]
- Texto literal:
> Results: Among the tested methods, TurboFect™ chemical transfection exhibited the highest e ciency. Optimal transfection conditions were achieved using 1 μg DNA and 4 µL TurboFect™ on 6×104 Vero cells.

### Extracto 2
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf|PDF]]
- Texto literal:
> In addition, we compared various transfection methods to identify the optimal conditions for transfection in Vero cells. The results demonstrated that TurboFect™, a chemical transfection reagent, exhibited the highest transfection e ciency in Vero cells. Nonviral delivery methods, such as chemical transfection, offer advantages over viral vector delivery, including reduced immunogenicity and a lower risk of insertional mutagenesis(33). Statistically, TurboFect™ signi cantly outperformed other chemical transfection methods, electroporation, and transduction using lentiviral vectors. Electroporation, although effective for gene delivery, resulted in a high rate of cell death, which negatively impacted transfection e ciency. On the other hand, transduction using lentiviral vector-based HIV-1 showed low e ciency in Vero cells because of the presence of an intracellular inhibitor for HIV-1 integration(34). It can be presumed that the high e ciency of TurboFect™ in creating optimal conditions in Vero cells is attributed to the formation of liposome particles, their successful transfer through the lipid membrane, evasion from degradation by lysosomes, and e cient nuclear translocation.

### Extracto 3
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf|PDF]]
- Texto literal:
> In this study, we investigated the optimal transfection conditions in the Vero cell line using various chemical transfection agents, including Lipofectamine™ 2000, TurboFect™, X-tremeGENE™ 9, and PEI MAX®. We tested different ratios of DNA concentration and chemical transfection reagent to determine the most effective combination. Our results showed that using 1 µg of each plasmid with 4 µL of TurboFect™ in 6×104 cells achieved the highest transfection e ciency (46.5%) and cell viability (94%) compared with other reagents, such as Lipofectamine™ 2000 (42% transfection e ciency and 94% cell viability).

### Extracto 4
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf|PDF]]
- Texto literal:
> In addition, the results demonstrated that Ebuffer 3 exhibited higher transfection e ciency (38.6%) than the other buffers, and this increase was statistically signi cant. The composition of the buffer signi cantly in uences the transfection e ciency. Using RPMI-1640 medium as a shock buffer simpli es the process and reduces cell damage and death after transfection. RPMI-1640 without serum and antibiotics showed higher cell survival after shock than other buffers(10). Transfection and viability remained unaffected when RPMI-1640 was used as the transfection buffer, even for cells cultured in different media(28).

### Extracto 5
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/mahdi_2021_delivery_of_dcas9_crispr_system_into_the_hard.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/mahdi_2021_delivery_of_dcas9_crispr_system_into_the_hard.pdf|PDF]]
- Texto literal:
> that the magnetofection method with an efficiency around 85.7% for HEK-293 and 28.2% for HFF.

### Extracto 6
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 6|Pasaje 6]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf|PDF]]
- Texto literal:
> Chemical transfection strategies involve the use of various substances, such as Ca2 + phosphatepolycation and dendrimers, to facilitate the transfer of DNA across cell membranes. Cationic polymers, such as poly-L-lysine, lipopolyamine, and polyamidoamine, have been studied as potential vehicles for delivering nucleic acids, showing e cient transfection without damaging cellular membranes (7, 8).

### Extracto 7
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 7|Pasaje 7]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf|PDF]]
- Texto literal:
> Optimizing the electroporation conditions for different buffers and voltages in the Vero cell line

### Extracto 8
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> Lentiviral vectors (LV) are at present the most widely used viral vectors for clinical gene therapy applications in which long-lasting expression of a gene is required. The advantage of LV is the relatively safe genomic integration of the gene construct and the capacity to transduce both dividing and non-dividing cells with high efficiency. However, the feature that makes this vector suitable for gene delivery

### Extracto 9
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 8|Pasaje 8]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf|PDF]]
- Texto literal:
> Virus-mediated transfection or transduction uses viral vectors to introduce speci c nucleic acid sequences into host cells. Lentiviral transduction is highly e cient in delivering transgenes to mammalian cells, especially primary cells that are di cult to transfect. However, viral transduction carries the risk of cytotoxicity and viral infection. Optimizing transfection conditions is crucial for achieving high e ciency and consistency because different cell strains have speci c requirements. The heterogeneity in transfection e ciency among cell types emphasizes the need for comparative studies to determine the most effective method for each cell type (11). Enhanced gene transfer techniques speci c to Vero cells, which are commonly used in vaccine development and gene therapy, are essential for successful gene expression studies.

### Extracto 10
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 10|Pasaje 10]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf|PDF]]
- Texto literal:
> However, under optimal transfection conditions, the cell viability in electroporation was 56%, which was signi cantly lower than that of the control. One notable limitation of the electroporation transfection technique is its inherent cellular toxicity, which can range from 50–90%. In general, electroporation maintains viability within the range of 30–40% and can be further optimized to maximize transfection e ciency.

### Extracto 11
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> Traditional methods of direct transfection have first been investigated. The main advantage of these techniques is that the uptake mechanism is independent of the cell. Microinjection of single fast-dividing cells has been used to generate a great variety of knock-out and transgenic animals by directly injecting zygotes with CRISPR components into the nucleus. While this technique is very effective, it has the distinct disadvantage of cells requiring individual manipulation.10 Electropo-ration, by which pores are formed in cell membranes upon application of a high voltage, can be used to directly transfect cells ex vivo as well as some in vivo tissues. This has, for example, been used to transfect human B-cells with CRISPR/Cas RNP to induce production of therapeutic proteins, after differentiation into plasma cells.11 Electropora-tion can be very toxic, however, due to this technique harming the cell membrane. In some cases this leads to permanent permeabilization of the membrane.12

### Extracto 12
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 11|Pasaje 11]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf|PDF]]
- Texto literal:
> According to the results obtained from Fig. 1c, X-tremeGENE™ 9 transfection reagent showed optimum transfection e ciency at a rate of 1 µg:4 µL of DNA/reagent. The estimated optimum number of GFP-positive cells was 24.5%, which was signi cantly different from the other DNA/reagent rates (p ≤ 0.05, Fig. 1C). Cell viability (~ 91%) was observed at this ratio, and there were no signi cant differences between these and control cells (p ≤ 0.05, Fig. 2C).

### Extracto 13
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf#Passage 12|Pasaje 12]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf|PDF]]
- Texto literal:
> TurboFect™ has lower toxicity than Lipofectamine, which contributes to its higher transfection e ciency and cell viability. Choosing TurboFect™ allows researchers to achieve a balance between effective transfection and high cell viability in Vero cells. We observed lower transfection e ciency with X-tremeGENE™ 9 and PEI MAX®. PEI, although a cationic polymer, exhibited higher cytotoxicity. It can induce toxicity by depolarizing mitochondria and stimulating immune responses. High-molecular-weight PEI (HMW PEI) can form stable polyplexes, but its noncleavable structure increases cytotoxicity(20). PEI– DNA complexes can activate genes involved in cellular responses, including apoptosis, stress responses, and oncogenesis(21).

### Extracto 14
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 5|Pasaje 5]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> To counteract this, self-inactivating constructs have been designed in which the lentiviral vector encodes for Cas9 protein and two sgRNAs: one against the target sequence of choice and one against the Cas9 gene.22 In this way transient expression of Cas9 from an integrating lentiviral vector can be obtained.

### Extracto 15
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 6|Pasaje 6]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> to a template DNA either double- or single-stranded.26,27 Such DNA templates require two flanking regions complementary to the DSB ends to mediate annealing and additionally contain the corrected gene. Homology directed repair is restricted to S/G2 phase of mitosis, however, it is particularly interesting in the field of gene editing for therapeutic applications.27

### Extracto 16
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 7|Pasaje 7]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> Despite the low costs and stability of plasmid DNA, recent efforts focus on delivering the cargo formats Cas9 mRNA or Cas9 RNP via

### Extracto 17
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 8|Pasaje 8]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> There are several formats in which the sgRNA and Cas protein can be delivered into the cell to achieve therapeutic gene editing. These have been summarized in Fig. 1A. The endonuclease is problematic to deliver, due to the high molecular weight of the protein (158.9 kDa for spCas9) and the gene length (around 4 kb). The gene can be delivered either as an expression plasmid or by viral vectors which need to be imported into the nucleus for transcription. Additionally, it can be de-

### Extracto 18
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|PDF]]
- Texto literal:
> Naturally found Cas9 variants are large proteins, which adds particular limitation when it comes to their packaging and delivery into different cell types via Lenti or Adeno Associated viruses (AAV). For example, the widely used SpCas9 protein is

### Extracto 19
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf#Passage 9|Pasaje 9]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|PDF]]
- Texto literal:
> Adeno-associated viruses (AAV) combine low immunogenicity upon first injection with serotype-related target cell specificity and relatively long expression of the gene without the necessity for genome integration. However, the packaging capacity is limited and, as a consequence, the genetic material encoding the most frequently used sp-Cas9 (4.2 kB) leaves limited space for necessary regulatory elements, such as promoter and polyadenylation signal sequences. This can be solved by splitting spCas9 into two fragments that can recombine inside the cell so that the truncated genes will fit the AAV vector, but this comes at the cost of efficiency in terms of delivery as well as target DNA cutting.16

### Extracto 20
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/li_2021_nanoparticle_delivery_of_crispr_cas9_for_genome_editing.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/li_2021_nanoparticle_delivery_of_crispr_cas9_for_genome_editing.pdf|PDF]]
- Texto literal:
> Additionally, the virus is limited to delivering CRISPR/Cas9 DNA, and its load capacity is minimal (Chew et al., 2016). For example, adeno-associated viruses can only load up to 4.7 kb DNA sequences (Zincarelli et al., 2008). Therefore, their ability to deliver the CRISPR/Cas9 system safely and efficiently remains to be determined. Electroporation is the most common physical method to transfer CRISPR/Cas systems into cells. Single-cell microinjection, another physical delivery tool of CRISPR/Cas9, has been widely used in embryo gene editing and transgenic animal production. The transfer of Cas9 DNA or protein components has shown high transduction efficiency and low cytotoxicity. However, microinjection is time-consuming and labor intensive, which limits its application to a small number of species.

### Extracto 21
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf#Passage 1|Pasaje 1]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf|PDF]]
- Texto literal:
> The high cargo capacity (∼10 kb) of LV favors the design of an “all-in-one” vector to drive the expression of large size Cas9 nucleases or base editors. The injection of an LV carrying SpCas9 nuclease and a sgRNA targeting the huntingtin coding sequence in the striatum of a mouse model of Huntington disease (HD) resulted in a robust knock-down of the mutant hHTT-82Q protein in both neurons and astrocytes (Merienne et al., 2017). A unique LV-based CRISPR/Cas9 system has recently been generated to simultaneously deliver the Cas9 nuclease and four different sgRNAs, each under the control of a different promoter, thus allowing the simultaneous editing of different cell types in targeted tissues (Kabadi et al., 2014). Additionally, an all-in-one LV carrying dCas9 fused with the catalytic domain of DNA-methyltransferase 3A (DNMT3A) has recently been tested to target SNCA triplication in hiPSCderived dopaminergic neurons to efficiently reduce SNCA expression levels, rescuing mitochondrial ROS production and cellular viability (Kantor et al., 2018; Tagliafierro et al., 2019). Importantly, expression cassettes driven by astrocyte-specific

### Extracto 22
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/mahdi_2021_delivery_of_dcas9_crispr_system_into_the_hard.pdf#Passage 2|Pasaje 2]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/mahdi_2021_delivery_of_dcas9_crispr_system_into_the_hard.pdf|PDF]]
- Texto literal:
> advantages such as high transduction efficiency and long term transgene expression ,but their

### Extracto 23
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/mahdi_2021_delivery_of_dcas9_crispr_system_into_the_hard.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/mahdi_2021_delivery_of_dcas9_crispr_system_into_the_hard.pdf|PDF]]
- Texto literal:
> can be engineered to target the interest cell or tissues. Also, this approach represents both higher

### Extracto 24
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/li_2021_nanoparticle_delivery_of_crispr_cas9_for_genome_editing.pdf#Passage 3|Pasaje 3]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/li_2021_nanoparticle_delivery_of_crispr_cas9_for_genome_editing.pdf|PDF]]
- Texto literal:
> However, regardless of the delivery cargo, it is challenging for the CRISPR/Cas9 to enter cells. Due to its considerable molecular weight (the genetic size of Cas9 ~4.5 kb) and its poor stability, finding a more suitable nano-delivery method for the various Cas9 components is vital. When designing and preparing a delivery system, it is necessary to focus on maintaining the nuclease activity of Cas9 and protecting the RNP against proteases, nucleases, antibodies, and T cell recognition in the serum and body fluids. Once entering the target cell, the delivery system should help the RNP be released from the endosome to the cytoplasm and enable its function.

### Extracto 25
- Fuente: [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/li_2021_nanoparticle_delivery_of_crispr_cas9_for_genome_editing.pdf#Passage 4|Pasaje 4]] | [[Research/Papers/dcas9-fto-granulosa/q10-sistemas-entrega/li_2021_nanoparticle_delivery_of_crispr_cas9_for_genome_editing.pdf|PDF]]
- Texto literal:
> Currently, nanocarriers are ideal delivery platforms for the CRISPR/Cas9 system, including cationic LNPs, DNA nanoparticles, lipid complexes, gold-based nanoparticles, and zeolite imidazole frameworks. They have been used for in vitro RNP delivery under extensive development and application efforts (Figure 2; Yin et al., 2016). Table 1 lists the current nanoplatforms for CRISPR/Cas9 delivery.

---

## Sources Referenced

- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf|johanna_1970_lipid_nanoparticle_mediated_delivery_of_crispr_cas9_for.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/li_2021_nanoparticle_delivery_of_crispr_cas9_for_genome_editing.pdf|li_2021_nanoparticle_delivery_of_crispr_cas9_for_genome_editing.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/mahdi_2021_delivery_of_dcas9_crispr_system_into_the_hard.pdf|mahdi_2021_delivery_of_dcas9_crispr_system_into_the_hard.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf|mazhar_2018_the_crispr_tool_kit_for_genome_editing_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf|parisa_2024_comparing_chemical_transfection_electroporation_and_lentiviral_vector_transduction.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf|vasco_2021_delivery_platforms_for_crispr_cas9_genome_editing_of.pdf]]


## Uncited Sources

These sources were in the notebook but NotebookLM did not provide granular citations for them:

- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/kasra_2020_exosomal_micrornas_derived_from_mesenchymal_stem_cells_cell.pdf|kasra_2020_exosomal_micrornas_derived_from_mesenchymal_stem_cells_cell.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/maryam_2021_b2m_gene_knockout_in_hek293t_cells_by_non.pdf|maryam_2021_b2m_gene_knockout_in_hek293t_cells_by_non.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/morane_1970_structural_and_functional_investigations_of_designed_histidine_rich.pdf|morane_1970_structural_and_functional_investigations_of_designed_histidine_rich.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/namit_2021_mrna_vaccines_for_infectious_diseases_principles_delivery_and.pdf|namit_2021_mrna_vaccines_for_infectious_diseases_principles_delivery_and.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/pawan_2016_protein_kinase_a_a_master_kinase_of_granulosa.pdf|pawan_2016_protein_kinase_a_a_master_kinase_of_granulosa.pdf]]
- [[Notes/NotebookLM/dcas9-fto-granulosa/q10-sistemas-entrega/Sources/shiyi_2025_lentiviral_vector_production_and_primary_astrocyte_transduction_v1.pdf|shiyi_2025_lentiviral_vector_production_and_primary_astrocyte_transduction_v1.pdf]]
