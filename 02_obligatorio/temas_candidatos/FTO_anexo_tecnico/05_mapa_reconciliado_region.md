# Mapa reconciliado de la región FTO–RPGRIP1L

Ensamblado GRCh38.p14, coordenadas 1-based inclusivas. Ensembl release 116, GENCODE release 50. Ninguna coordenada de este archivo proviene de hg19.

Jerarquía de anotación aplicada: Ensembl 116 y GENCODE 50 como referencia estructural; MANE Select como referencia operativa para nombrar los TSS; ENCODE cCRE como clasificación epigenómica independiente; GeneHancer como evidencia integradora secundaria, sin capacidad de reemplazar la segmentación de Ensembl ni de asignar gen diana.

---

## 1. Referencias fijas

| Elemento | Coordenada | Hebra | Fuente |
| :--- | :--- | :--- | :--- |
| TSS MANE de *FTO* (ENST00000471389.6) | 53.704.156 | + | Ensembl 116 |
| TSS MANE de *RPGRIP1L* (ENST00000647211.2) | 53.703.859 | − | Ensembl 116 |
| Cluster de TSS de *FTO* | 53.703.963 | + | Ensembl 116 |
| Cluster de TSS de *RPGRIP1L* | 53.703.938 | − | Ensembl 116 |
| Exón 1 del MANE de *FTO* | 53.704.156-53.704.229 (74 pb) | + | Ensembl 116 |

Distancia entre TSS MANE: 297 pb. Distancia entre clusters: 25 pb.

---

## 2. Distribución de sitios de inicio anotados

Recuento de transcritos que inician en cada coordenada, dentro de chr16:53.703.700-53.704.300.

| Coordenada | Gen | Transcritos | Observación |
| :--- | :--- | :--- | :--- |
| 53.703.810 | RPGRIP1L | 1 | RPGRIP1L-210 |
| 53.703.830 | RPGRIP1L | 1 | RPGRIP1L-203 |
| 53.703.838 | RPGRIP1L | 1 | biotipo sin CDS definido |
| 53.703.841 | RPGRIP1L | 1 | decaimiento mediado por sinsentido |
| 53.703.844 | RPGRIP1L | 1 | RPGRIP1L-202 |
| 53.703.847 | RPGRIP1L | 1 | RPGRIP1L-221 |
| **53.703.859** | RPGRIP1L | 1 | **MANE Select**, RPGRIP1L-212 |
| 53.703.889 | RPGRIP1L | 1 | decaimiento mediado por sinsentido |
| **53.703.938** | RPGRIP1L | **12** | seis con etiqueta `gencode_primary` |
| **53.703.963** | FTO | **22** | `gencode_primary` en FTO-227, FTO-234 y FTO-239; `ens_canon_extended` en FTO-242 |
| **53.704.156** | FTO | 4 | **MANE Select**, FTO-206 |
| 53.704.158 | FTO | 3 | dos por decaimiento mediado por sinsentido |
| 53.704.182 | FTO | 1 | FTO-205 |

Advertencia obligatoria de interpretación: el número de transcritos anotados que comparten una coordenada no demuestra que ese sitio sea el más utilizado. No corresponde llamar predominante al sitio 53.703.963 sin datos de CAGE, RAMPAGE, RNA-seq 5′ o lectura larga en el modelo celular de interés.

---

## 3. Segmentación por universo de anotación

Los tres universos no coinciden. La tabla los alinea sobre las mismas coordenadas.

| Intervalo | Ensembl Regulatory Build 116 | ENCODE cCRE | GeneHancer |
| :--- | :--- | :--- | :--- |
| 53.703.191-53.703.397 | sin elemento | sin elemento | GH16J053703 |
| 53.703.398-53.703.560 | enhancer ENSR16_9RBJ8 | sin elemento | GH16J053703 |
| 53.703.561-53.703.761 | enhancer ENSR16_9RBJ8 | **EH38E1816375, PLS, score 326** | GH16J053703 |
| 53.703.762-53.703.830 | enhancer ENSR16_9RBJ8 | sin elemento | GH16J053703 |
| 53.703.831-53.703.857 | promotor ENSR16_9RBJC | sin elemento | GH16J053703 |
| 53.703.858-53.704.167 | **promotor ENSR16_9RBJC**, asignado por Ensembl a `RPGRIP1L,FTO` | **EH38E1816376, PLS, score 682** | GH16J053703 |
| 53.704.168-53.704.208 | enhancer ENSR16_BDMQQ | EH38E1816376, PLS | GH16J053703 |
| 53.704.209-53.704.521 | enhancer ENSR16_BDMQQ | sin elemento | GH16J053703 |
| 53.704.522-53.704.689 | enhancer ENSR16_BDMQQ | **EH38E1816377, pELS, score 214** | GH16J053703 |
| 53.704.690-53.704.740 | enhancer ENSR16_BDMQQ | sin elemento | GH16J053703 |
| 53.704.741-53.705.162 | sin elemento | sin elemento | GH16J053703 |

Tres discordancias relevantes. Primero, ENCODE clasifica como promotor (PLS) una subregión que Ensembl clasifica como enhancer (ENSR16_9RBJ8). Segundo, el PLS de mayor puntaje, EH38E1816376, cubre en 350 pb los sitios de inicio de referencia y los inicios alternativos de los dos genes, incluidos ambos MANE y ambos clusters. Tercero, GeneHancer no segmenta: fusiona 1.971 pb en un único elemento Elite de tipo Promoter/Enhancer.

Consecuencia operativa: la afirmación "esta guía cae en un elemento distinto del promotor compartido" es verdadera bajo Ensembl y falsa bajo GeneHancer. Toda descripción de una guía debe declarar el universo de anotación que se está usando.

---

## 4. Asignación de genes por GeneHancer

Interacciones registradas para GH16J053703 en el conjunto completo de UCSC, ordenadas por puntaje.

| Gen | Score | Valor | Extensión del arco |
| :--- | :--- | :--- | :--- |
| FTO | 543 | 1334,5 | 53.701.691-53.705.162 |
| RPGRIP1L | 543 | 1334,5 | 53.703.191-53.705.162 |
| RBL2 | 17 | 39,03 | 53.433.976-53.705.162 |

El elemento está asignado por GeneHancer principalmente a *FTO* y a *RPGRIP1L*, con puntaje idéntico entre ambos y treinta veces superior al de *RBL2*. El registro de *RBL2* corresponde a una interacción elemento-gen a larga distancia, con anclaje del gen a unos 270 kb, y no implica pertenencia del promotor a *RBL2* ni evidencia de regulación en granulosa.

Los anclajes génicos que usa GeneHancer no coinciden con los TSS MANE: para *FTO* ancla en 53.701.692 y para *RPGRIP1L* en 53.703.938, es decir, en el cluster y no en el MANE.

---

## 5. Sitios CTCF

En el intervalo chr16:53.702.356-54.121.941 el Regulatory Build 116 registra ocho sitios CTCF, el más próximo en 53.744.515-53.744.536, todos dentro del cuerpo del gen y ninguno entre los dos promotores.

Interpretación admisible: el Ensembl Regulatory Build no registra un sitio CTCF en la ventana inter-TSS. No corresponde concluir a partir de ese dato la ausencia absoluta de aislamiento o de arquitectura cromatínica direccional en la región, para lo cual harían falta datos de ocupancia de CTCF y de conformación de la cromatina en el tipo celular de interés.

---

## 6. Inventario espacial ampliado

En chr16:53.702.356-54.121.941, que comprende 1.800 pb corriente arriba del TSS MANE más todo el transcrito, el Regulatory Build 116 registra 69 elementos: 59 de tipo enhancer, 2 promotores y 8 sitios CTCF. El segundo promotor se ubica en 53.999.959-54.000.165.

Este recuento es un inventario espacial. No implica que *FTO* posea funcionalmente 59 enhancers, ni que esos elementos regulen *FTO*, ni que estén activos en células de la granulosa.

---

## 7. Clasificación de las afirmaciones de este mapa

| Categoría | Contenido |
| :--- | :--- |
| Hechos de anotación oficial | Todas las coordenadas, identificadores, tipos de elemento, recuentos de transcritos y asignaciones de gen de las secciones 1 a 6 |
| Evidencia experimental publicada | Ninguna afirmación de este archivo proviene de literatura experimental |
| Inferencias de integración | Las tres discordancias entre universos de la sección 3 y la consecuencia operativa derivada |
| Decisiones de diseño | Ninguna. Este archivo no selecciona guías ni modifica el esquema experimental |
