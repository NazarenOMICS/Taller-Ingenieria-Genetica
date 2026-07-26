# Panel de guías: cuatro ventanas evaluadas

Estado: **ninguna guía seleccionada**. Este archivo consolida las cuatro ventanas, ordena las candidatas por prioridad y propone un panel experimental, sin declarar ganadora.

GRCh38.p14. Secuencia de referencia obtenida de la API REST de Ensembl para chr16:53.703.300-53.704.900. Variantes obtenidas del endpoint de superposición de Ensembl 116. Nucleasa de referencia SpCas9, PAM NGG, protoespaciador de 20 nt. Distancias calculadas desde el punto medio del protoespaciador a los cuatro puntos de referencia acordados.

---

## 1. La ventana nueva: chr16:53.704.020-53.704.145

**Resultado del rastreo**: 19 sitios NGG, 12 en hebra positiva y 2 en negativa entre los listados, con el resto distribuido.

**Hallazgo que corrige la premisa de la ventana.** El objetivo declarado era encontrar una guía proximal al TSS MANE de *FTO* y anterior al comienzo del exón 1. Eso se cumple respecto del transcrito MANE, cuyo exón 1 empieza en 53.704.156. Sin embargo, **las 62 variantes anotadas en la ventana tienen todas consecuencia de tipo `5_prime_UTR_variant`**, lo cual indica que la región es exónica y corresponde a la región no traducida 5′ de los transcritos que inician en el cluster 53.703.963. La ventana es intergénica solo desde la perspectiva del MANE; desde la de las isoformas del cluster es primer exón.

**Segunda observación.** La ventana permanece íntegramente dentro del promotor Ensembl ENSR16_9RBJC (53.703.831-53.704.167) y dentro del cCRE EH38E1816376, de tipo PLS y score 682, que es el mismo elemento que contiene los sitios de inicio de ambos genes. La ventana no escapa del bloque compartido; se corre dentro de él hacia el extremo de *FTO*.

**Candidatas completas de la ventana nueva.**

| Hebra | Coordenadas | Protoespaciador | PAM | GC | Var. | ClinVar | polyT | dFTO MANE | dFTO cluster | dRPG MANE | dRPG cluster |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| + | 53.704.025-53.704.044 | `GGTGTCGCCGCGGTGCATCC` | TGG | 75 % | 11 | 0 | no | −122 | +71 | +175 | +96 |
| + | 53.704.026-53.704.045 | `GTGTCGCCGCGGTGCATCCT` | GGG | 70 % | 12 | 1 | no | −121 | +72 | +176 | +97 |
| − | 53.704.035-53.704.054 | `ACAACTCCCAGGATGCACCG` | CGG | 60 % | 10 | 2 | no | −112 | +81 | +185 | +106 |
| − | 53.704.046-53.704.065 | `TAGAAAAAACTACAACTCCC` | AGG | 35 % | 10 | 2 | no | −101 | +92 | +196 | +117 |
| + | 53.704.051-53.704.070 | `TTGTAGTTTTTTCTACTCAG` | AGG | 30 % | 12 | 1 | **sí** | −96 | +97 | +201 | +122 |
| + | 53.704.052-53.704.071 | `TGTAGTTTTTTCTACTCAGA` | GGG | 30 % | 12 | 1 | **sí** | −95 | +98 | +202 | +123 |
| + | 53.704.069-53.704.088 | `AGAGGGAGAATAGCTCCAGA` | CGG | 50 % | 9 | 0 | no | −78 | +115 | +219 | +140 |
| + | 53.704.070-53.704.089 | `GAGGGAGAATAGCTCCAGAC` | GGG | 55 % | 8 | 0 | no | −77 | +116 | +220 | +141 |
| + | 53.704.076-53.704.095 | `GAATAGCTCCAGACGGGAGC` | AGG | 60 % | **6** | 0 | no | −71 | +122 | +226 | +147 |
| − | 53.704.087-53.704.106 | `CTCAGCGTCCTGCTCCCGTC` | TGG | 70 % | 7 | 0 | no | −60 | +133 | +237 | +158 |
| + | 53.704.099-53.704.118 | `ACGCTGAGAGAACTACATGC` | AGG | 50 % | 9 | 0 | no | −48 | +145 | +249 | +170 |
| + | 53.704.102-53.704.121 | `CTGAGAGAACTACATGCAGG` | AGG | 50 % | 7 | 0 | no | −45 | +148 | +252 | +173 |
| + | 53.704.105-53.704.124 | `AGAGAACTACATGCAGGAGG` | CGG | 50 % | **6** | 0 | no | −42 | +151 | +255 | +176 |
| + | 53.704.106-53.704.125 | `GAGAACTACATGCAGGAGGC` | GGG | 55 % | 7 | 0 | no | −41 | +152 | +256 | +177 |
| + | 53.704.107-53.704.126 | `AGAACTACATGCAGGAGGCG` | GGG | 55 % | 7 | 0 | no | −40 | +153 | +257 | +178 |
| + | 53.704.113-53.704.132 | `ACATGCAGGAGGCGGGGTCC` | AGG | 70 % | **6** | 0 | no | −34 | +159 | +263 | +184 |
| + | 53.704.114-53.704.133 | `CATGCAGGAGGCGGGGTCCA` | GGG | 70 % | 7 | 0 | no | −33 | +160 | +264 | +185 |
| + | 53.704.119-53.704.138 | `AGGAGGCGGGGTCCAGGGCG` | AGG | 80 % | 9 | 0 | no | −28 | +165 | +269 | +190 |
| + | 53.704.120-53.704.139 | `GGAGGCGGGGTCCAGGGCGA` | GGG | 80 % | 10 | 0 | no | −27 | +166 | +270 | +191 |

Todas las candidatas de esta ventana comparten: elemento Ensembl promotor ENSR16_9RBJC; cCRE EH38E1816376 de tipo PLS; GeneHancer GH16J053703 de tipo Promoter/Enhancer y categoría Elite; y ausencia de sitios de inicio anotados dentro del propio protoespaciador, con el más próximo, el cluster de *FTO*, a 71 pb o más.

**Dos descartes automáticos.** Las candidatas de 53.704.051 y 53.704.052 contienen una corrida de seis timidinas. Un tramo de cuatro o más T en el protoespaciador actúa como señal de terminación de la ARN polimerasa III y trunca el transcrito del ARN guía expresado desde un promotor U6, que es el sistema del vector del curso. Quedan excluidas por razón técnica, con independencia de su posición.

**Ninguna candidata de esta ventana queda por debajo de seis variantes anotadas superpuestas.** La densidad es de 62 variantes en 126 pb.

---

## 2. Tabla final de las cuatro ventanas

| Ventana | Referencia | Elemento Ensembl | cCRE ENCODE | Contexto estructural | Sitios NGG | Var. mínimas por candidata | Ambigüedad de gen diana |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| W1 | −200 | promotor ENSR16_9RBJC | EH38E1816376, PLS, 682 | intergénico entre ambos clusters | 11 en ±35 pb | 0 | máxima |
| W2 | +60 | enhancer ENSR16_BDMQQ | borde de EH38E1816376, PLS | exón 1 codificante del MANE | 14 en ±35 pb | 12, con una entrada ClinVar | baja frente a *RPGRIP1L*, alta en cuanto a naturaleza del elemento |
| W3 | +450 | enhancer ENSR16_BDMQQ | EH38E1816377, pELS, 214 | intrón 1 del MANE | 3 en ±35 pb | 4, todas intrónicas | la más baja |
| W4 | 53.704.020-53.704.145 | promotor ENSR16_9RBJC | EH38E1816376, PLS, 682 | 5′ UTR exónica de las isoformas del cluster; intergénica solo respecto del MANE | 19 en la ventana | 6 | intermedia |

**Comparación directa que motivó la ventana nueva.** W4 se aleja de *RPGRIP1L* de manera sustancial respecto de W1: la mejor candidata de W4 queda a +255 del TSS MANE de *RPGRIP1L* y a +176 de su cluster, frente a +93 y +14 en W1. En ese sentido el objetivo se cumple. Lo que no logra es salir del elemento compartido: sigue dentro del mismo promotor Ensembl y del mismo PLS de ENCODE, y es exónica para las isoformas del cluster.

---

## 3. Candidatas ordenadas por prioridad

Orden provisional, sujeto a completar actividad y especificidad. Ninguna está seleccionada.

| Prioridad | Candidata | Ventana | Motivo |
| :--- | :--- | :--- | :--- |
| 1 | `TGGTCTCTGAGGACTGAGAT` CGG, +, 53.704.573-53.704.592 | W3 | Única que coincide con elemento de tipo enhancer en Ensembl y en ENCODE simultáneamente; intrónica; sin sitios de inicio en 300 pb; solo cuatro variantes, todas intrónicas; GC 50 % |
| 2 | `AGAGAACTACATGCAGGAGG` CGG, +, 53.704.105-53.704.124 | W4 | La menos cargada de variantes de su ventana junto con otras dos, sin entradas ClinVar, GC 50 %, sin corrida de T; a −42 del TSS MANE de *FTO* y a +255 del de *RPGRIP1L* |
| 3 | `GAATAGCTCCAGACGGGAGC` AGG, +, 53.704.076-53.704.095 | W4 | Seis variantes, sin ClinVar, GC 60 %; alternativa a la anterior con 29 pb más de separación del TSS MANE |
| 4 | `TGCAGTCAGCTGTGTTTCTT` TGG, +, 53.704.613-53.704.632 | W3 | Segunda posición dentro del pELS, GC 45 %; cubre variabilidad de guía dentro del mismo elemento |
| 5 | `CCGCTACCCCGCGAGCAAAC` AGG, −, 53.703.942-53.703.961 | W1 | Comparador del promotor divergente; sin variantes anotadas; GC 70 %, que es alto |
| 6 | `CCTGTTTGCTCGCGGGGTAG` CGG, +, 53.703.939-53.703.958 | W1 | Comparador alternativo; extremo 5′ a 1 pb del cluster de *RPGRIP1L* |
| Conservada aparte | `AGCTTCGCGCTCTCGTTCCT` CGG, −, 53.704.207-53.704.226 | W2 | Candidato exónico problemático; se retiene documentado, no como preferido |

---

## 4. Recomendación de panel experimental

Propuesta, no decisión. Cinco brazos, cuatro guías individuales y una combinación.

| Brazo | Composición | Qué pregunta responde |
| :--- | :--- | :--- |
| A | Candidata 1, W3, pELS intrónico | ¿Activa *FTO* el elemento de tipo enhancer proximal, que es el más alejado de los sitios de inicio de ambos genes? |
| B | Candidata 4, W3, segunda posición del mismo pELS | ¿El resultado del brazo A es propiedad del elemento o de esa guía en particular? |
| C | Candidata 2, W4, proximal al TSS MANE dentro del bloque compartido | ¿Rinde más una guía próxima al inicio del MANE, y a qué costo sobre *RPGRIP1L*? |
| D | Candidata 5, W1, comparador del promotor divergente | ¿Cuál es el efecto sobre ambos genes al acetilar el punto de máxima ambigüedad? |
| E | Combinación de A y B | ¿Sumar guías dentro del mismo elemento incrementa la activación, como reportan Hilton et al. (2015) y Liao et al. (2026)? |

Lectura obligatoria en todos los brazos: *FTO* y *RPGRIP1L* medidos simultáneamente, más el panel de controles ya definido, es decir, guía no dirigida, efector catalíticamente inactivo y dCas9 sin efector.

Criterio de comparación entre brazos: además de la activación absoluta de *FTO*, la relación entre el cambio en *FTO* y el cambio en *RPGRIP1L*.

Si hubiera que reducir a cuatro brazos por espacio o costo, el candidato a eliminar es el brazo C, dado que su información se solapa parcialmente con la del brazo D en cuanto a proximidad al bloque compartido.

---

## 5. Separación entre lo resoluble por bioinformática y lo que exige el modelo celular

**Resoluble por bioinformática, y pendiente de ejecutar.**

1. Puntajes de actividad predicha de cada protoespaciador, con herramienta y versión declaradas. No se ejecutó aquí; requiere CRISPOR o equivalente.
2. Búsqueda de sitios fuera de blanco a escala genómica, con número de desapareamientos, ubicación exónica o no exónica y estado de la secuencia semilla. No se ejecutó aquí; requiere alineamiento contra el genoma completo, que excede lo que se puede hacer con consultas a la API.
3. Frecuencia poblacional de cada variante que solapa los protoespaciadores. Es consultable por identificador en Ensembl o gnomAD; en este archivo se informa el recuento y la presencia de entradas ClinVar, no la frecuencia.
4. Verificación de corridas de cuatro o más timidinas en cada candidata, ya realizada.
5. Contenido GC y estructura secundaria previsible del ARN guía.
6. Confirmación de la superposición exacta de cada protoespaciador con exones, elementos regulatorios y sitios de inicio, ya realizada.

**Solo resoluble en KGN o granulosa.** Corresponden a las preguntas P1 a P8 del archivo 08, que se conservan como limitaciones declaradas del proyecto y no como requisitos que impidan avanzar.

1. Cuál sitio de inicio de *FTO* se utiliza efectivamente en el modelo.
2. Si el promotor divergente está accesible y activo en granulosa.
3. Nivel de expresión basal de *FTO* y de *RPGRIP1L* en el modelo.
4. Relevancia funcional de *RPGRIP1L* en granulosa y consecuencia de modificarlo.
5. Si el eje CUX1 opera en ese tipo celular.
6. Estado de metilación del bloque promotor en granulosa envejecida.
7. Si existe arquitectura cromatínica que separe ambos promotores.
8. Nivel de *FTO* correspondiente a granulosa joven, que define el criterio de éxito.

La ausencia de datos celulares sobre el sitio de inicio utilizado obliga a informar cada distancia contra los cuatro puntos de referencia, pero no invalida el diseño.

---

## 6. Clasificación de las afirmaciones de este archivo

| Categoría | Contenido |
| :--- | :--- |
| Hechos de anotación oficial | Secuencias, coordenadas, PAM, contenido GC, elementos Ensembl, cCRE, GeneHancer, recuentos de variantes y sus consecuencias |
| Evidencia experimental publicada | La referencia a Hilton et al. (2015) y Liao et al. (2026) sobre multiplexado, y el criterio de terminación por corrida de timidinas en promotores de ARN polimerasa III |
| Inferencias de integración | Las lecturas de ambigüedad de gen diana, el orden de prioridad de la sección 3 y la propuesta de panel de la sección 4 |
| Decisiones de diseño | Ninguna guía seleccionada. La clasificación provisional de las cuatro ventanas está registrada en `DECISIONES_DISENO.md`, apartado D4.2 |
