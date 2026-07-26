# Afirmaciones previas que deben corregirse

Lista explícita de afirmaciones ya escritas en el material del proyecto que el anexo técnico obliga a corregir, matizar o retirar. Se indica dónde está cada una, qué dice hoy, qué corresponde decir y con qué respaldo.

Estado de aplicación: **ninguna corrección fue aplicada todavía**. Este archivo las enumera para decisión.

---

## C1. Atribución de GeneHancer a RBL2

**Dónde**: informe de integración entregado en conversación el 2026-07-26, apartado de hallazgos.

**Qué dije**: que GeneHancer no vincula el bloque promotor con *FTO* en su nivel de mayor confianza, sino con *RBL2*.

**Qué corresponde decir**: en el conjunto completo de interacciones de GeneHancer, GH16J053703 está asignado a *FTO* y a *RPGRIP1L* con score 543 y valor 1334,5 en ambos casos, y a *RBL2* con score 17 y valor 39,03. La asignación principal del elemento es a los dos genes del promotor divergente. El registro de *RBL2* corresponde a una interacción a larga distancia y no implica pertenencia del promotor a ese gen.

**Origen del error**: la lectura se hizo sobre el archivo filtrado `ucsc_geneHancerInteractionsDoubleElite.json`, donde los vínculos con *FTO* y *RPGRIP1L* para ese elemento no aparecen. La consulta correcta es el archivo completo `ucsc_geneHancerInteractions.json`.

**Prioridad**: alta. Es un error mío de lectura y afecta la interpretación del gen diana.

---

## C2. Descripción del elemento del lado de FTO como enhancer

**Dónde**: `DECISIONES_DISENO.md`, apartados D4.1 y D4.2, donde el elemento ENSR16_BDMQQ se describe como el primer elemento regulatorio que pertenece al territorio de *FTO*, y las guías dirigidas allí se llaman guías en enhancer.

**Qué corresponde decir**: ENSR16_BDMQQ abarca 53.704.168-53.704.740 y solapa en 62 pb el exón 1 del transcrito MANE, que va de 53.704.156 a 53.704.229. Además contiene un sitio de inicio anotado de *FTO* en 53.704.182. Una guía ubicada en torno a +60 cae dentro del exón 1 y, según las consecuencias de las variantes anotadas allí, dentro de secuencia codificante. La descripción correcta distingue la porción exónica del elemento de su porción intrónica.

**Prioridad**: alta. Afecta cómo se nombra una de las tres candidatas.

---

## C3. Tratamiento del promotor compartido como región única y homogénea

**Dónde**: `DECISIONES_DISENO.md`, apartado D2, y el argumento general de la región inter-TSS de 296 pb.

**Qué corresponde decir**: la región inter-TSS no está vacía entre dos sitios de inicio. Contiene dos clusters densos de sitios de inicio anotados, el de *RPGRIP1L* en 53.703.938 con 12 transcritos y el de *FTO* en 53.703.963 con 22 transcritos, separados entre sí por 25 pb. La descripción de la región como el espacio entre dos TSS enfrentados es correcta en cuanto a los MANE, pero incompleta en cuanto a la arquitectura real.

**Prioridad**: alta. Cambia la caracterización de la candidata de −200.

---

## C4. Formulación sobre la inevitabilidad de la coactivación

**Dónde**: informe de integración del 2026-07-26, inferencia de integración número tres, donde se afirma que la coactivación deja de ser una hipótesis de vecindad y pasa a ser una consecuencia de arquitectura.

**Qué corresponde decir**: compartir un mismo PLS que contiene los sitios de inicio de ambos genes eleva de manera considerable el riesgo de coactivación, pero no la convierte en consecuencia inevitable. La direccionalidad y la magnitud del efecto sobre cada gen deben determinarse experimentalmente.

**Prioridad**: media. Es una corrección de grado, no de hecho.

---

## C5. Ausencia de CTCF interpretada como ausencia de aislamiento

**Dónde**: informe de integración del 2026-07-26, donde se afirma que no hay aislador anotado entre los dos promotores y se presenta como caída de una hipótesis previa.

**Qué corresponde decir**: el Ensembl Regulatory Build 116 no registra sitios CTCF en la ventana inter-TSS; el más próximo está en 53.744.515. Eso describe el estado de la anotación, no demuestra ausencia de aislamiento ni de arquitectura cromatínica direccional, para lo cual se requerirían datos de ocupancia y de conformación de la cromatina en el tipo celular de interés.

**Prioridad**: media.

---

## C6. Segmentación tratada como propiedad del locus

**Dónde**: `DECISIONES_DISENO.md`, apartado D4.1, donde la comparación de regiones blanco se apoya en la existencia de elementos distintos.

**Qué corresponde decir**: la existencia de elementos distintos depende del universo de anotación. Bajo Ensembl 116 hay tres elementos consecutivos; bajo ENCODE hay dos firmas de promotor y una de enhancer proximal con límites que no coinciden con los de Ensembl; bajo GeneHancer hay un solo bloque de 1.971 pb que engloba a todos. La comparación de regiones blanco sigue siendo válida, pero debe declarar explícitamente que se apoya en la segmentación de Ensembl.

**Prioridad**: alta. Es la premisa sobre la que se eligió la región blanco.

---

## C7. Discordancia entre Ensembl y ENCODE en la clasificación del elemento corriente arriba

**Dónde**: no está escrita en ningún archivo; se registra como omisión a incorporar.

**Qué corresponde agregar**: la subregión 53.703.561-53.703.761, que Ensembl incluye dentro del enhancer ENSR16_9RBJ8, está clasificada por ENCODE como firma de promotor (EH38E1816375, PLS, score 326). Es una segunda firma de promotor en la región, corriente arriba de ambos MANE, sin sitios de inicio anotados en el conjunto de transcritos consultado.

**Prioridad**: baja para el diseño actual, dado que ninguna candidata cae allí; relevante para la descripción del locus.

---

## C8. Uso del gen como referencia de coordenadas

**Dónde**: riesgo latente, ya advertido en `DECISIONES_DISENO.md` apartado D1.

**Qué corresponde mantener**: el gen ENSG00000140718 comienza en 53.701.692, unos 2,5 kb antes que el transcrito MANE. GeneHancer, además, ancla *FTO* en esa coordenada y *RPGRIP1L* en 53.703.938, es decir, en el cluster y no en el MANE. Toda distancia informada debe declarar respecto de qué punto se calcula.

**Prioridad**: alta como regla permanente.

---

## Resumen de prioridades

| Corrección | Prioridad | Afecta a |
| :--- | :--- | :--- |
| C1, atribución a RBL2 | Alta | Interpretación del gen diana |
| C2, elemento del lado de FTO | Alta | Descripción de la candidata +60 |
| C3, arquitectura de la región inter-TSS | Alta | Descripción de la candidata −200 |
| C6, segmentación dependiente del universo | Alta | Premisa de elección de región blanco |
| C8, referencia de coordenadas | Alta | Todas las distancias informadas |
| C4, inevitabilidad de la coactivación | Media | Formulación del riesgo |
| C5, lectura de la ausencia de CTCF | Media | Formulación de la arquitectura |
| C7, segunda firma de promotor | Baja | Descripción del locus |
