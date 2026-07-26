# Tabla revisada de guías candidatas

Estado: **candidatas, no seleccionadas**. Este archivo caracteriza las tres posiciones que venían del diseño previo, sobre secuencia real. No elige guía definitiva.

Ensamblado GRCh38.p14. Secuencia de referencia obtenida de la API REST de Ensembl para chr16:53.703.300-53.704.900. Nucleasa de referencia SpCas9, PAM NGG, protoespaciador de 20 nt. Las coordenadas del protoespaciador se informan como extremo 5′ y extremo 3′ del propio protoespaciador; la posición usada para calcular distancias es el punto medio.

Convención de signo: valores positivos indican posición corriente abajo del punto de referencia en el sentido de transcripción de *FTO* (coordenadas crecientes); valores negativos, corriente arriba.

---

## 1. Candidatas en el sitio de referencia −200 (promotor divergente)

Ninguna de las dos requiere ser elegida todavía. Se listan las dos mejores por cercanía al centro del sitio.

| Campo | Candidata C1 | Candidata C2 |
| :--- | :--- | :--- |
| Protoespaciador (5′→3′) | `CCGCTACCCCGCGAGCAAAC` | `CCTGTTTGCTCGCGGGGTAG` |
| PAM | `AGG` | `CGG` |
| Hebra | − | + |
| Extremo 5′ del protoespaciador | 53.703.961 | 53.703.939 |
| Extremo 3′ del protoespaciador | 53.703.942 | 53.703.958 |
| Intervalo ocupado | 53.703.942-53.703.961 | 53.703.939-53.703.958 |
| Punto medio | 53.703.952 | 53.703.949 |
| Contenido GC | 70 % | 65 % |
| Distancia al TSS MANE de *FTO* (53.704.156) | −204 | −207 |
| Distancia al cluster *FTO* (53.703.963) | −11 | −14 |
| Distancia al TSS MANE de *RPGRIP1L* (53.703.859) | +93 | +90 |
| Distancia al cluster *RPGRIP1L* (53.703.938) | +14 | +11 |
| Contexto estructural | intergénico entre ambos genes | intergénico, con el extremo 5′ a 1 pb del cluster de *RPGRIP1L* |
| Elemento Ensembl | promotor ENSR16_9RBJC | promotor ENSR16_9RBJC |
| cCRE ENCODE | EH38E1816376, PLS, score 682 | EH38E1816376, PLS, score 682 |
| GeneHancer | GH16J053703, Promoter/Enhancer, Elite | ídem |
| TSS anotados dentro o cerca del protoespaciador | cluster *FTO* a 2 pb del extremo 5′; cluster *RPGRIP1L* a 4 pb del extremo 3′ | cluster *RPGRIP1L* a 1 pb del extremo 5′; cluster *FTO* a 5 pb del extremo 3′ |
| Variantes anotadas en el intervalo | ninguna registrada en Ensembl 116 | ninguna registrada |
| Actividad prevista | no evaluada; requiere puntaje de herramienta de diseño | ídem |
| Especificidad prevista | no evaluada; requiere análisis de off-targets genómicos | ídem |
| Riesgo interpretativo | **máximo**: el protoespaciador queda entre los dos clusters, dentro del PLS que contiene los TSS de referencia y los inicios alternativos de ambos genes | **máximo**, por el mismo motivo |

**Marca solicitada.** Ambas candidatas de este sitio quedan a menos de 15 pb de los dos clusters simultáneamente. Cualquier deposición local de acetilación afecta el mismo bloque de nucleosomas que contiene los sitios de inicio de *FTO* y de *RPGRIP1L*. Su valor en el diseño es servir de comparador del promotor divergente, no de guía de activación preferente de *FTO*. El contenido GC de 70 % de C1 es alto y conviene tenerlo presente al evaluar actividad.

---

## 2. Candidatas en el sitio de referencia +60

| Campo | Candidata F1a | Candidata F1b |
| :--- | :--- | :--- |
| Protoespaciador (5′→3′) | `AGCTTCGCGCTCTCGTTCCT` | `GGAACGAGAGCGCGAAGCTA` |
| PAM | `CGG` | `AGG` |
| Hebra | − | + |
| Extremo 5′ del protoespaciador | 53.704.226 | 53.704.208 |
| Extremo 3′ del protoespaciador | 53.704.207 | 53.704.227 |
| Intervalo ocupado | 53.704.207-53.704.226 | 53.704.208-53.704.227 |
| Punto medio | 53.704.217 | 53.704.218 |
| Contenido GC | 60 % | 60 % |
| Distancia al TSS MANE de *FTO* | +61 | +62 |
| Distancia al cluster *FTO* | +254 | +255 |
| Distancia al TSS MANE de *RPGRIP1L* | +358 | +359 |
| Distancia al cluster *RPGRIP1L* | +279 | +280 |
| Contexto estructural | **dentro del exón 1 del transcrito MANE** (53.704.156-53.704.229), en secuencia codificante | ídem |
| Elemento Ensembl | enhancer ENSR16_BDMQQ | enhancer ENSR16_BDMQQ |
| cCRE ENCODE | borde 3′ de EH38E1816376, PLS (termina en 53.704.208) | ídem |
| GeneHancer | GH16J053703 | ídem |
| TSS anotados dentro o cerca del protoespaciador | TSS de FTO-205 en 53.704.182, a 25 pb del extremo 3′ | ídem |
| Variantes anotadas en el intervalo | **12 variantes** en 53.704.207-53.704.227, con consecuencias de tipo missense, sinónima y ganancia de codón de parada; una de ellas, rs2544857861, figura en ClinVar con significado incierto | ídem |
| Actividad prevista | no evaluada | no evaluada |
| Especificidad prevista | no evaluada | no evaluada |
| Riesgo interpretativo | describir esta guía como dirigida a un enhancer sería incorrecto | ídem |

**Marca solicitada.** Este sitio no debe describirse como guía en enhancer. Cae dentro del exón 1 del transcrito MANE y, según las consecuencias de las variantes que allí se anotan, dentro de secuencia codificante. Formalmente pertenece al elemento Ensembl de tipo enhancer ENSR16_BDMQQ, que solapa el exón 1 en 62 pb, de modo que la etiqueta del Regulatory Build y la estructura del transcrito coexisten en la misma coordenada. La descripción correcta es que la guía se dirige a la porción exónica del elemento ENSR16_BDMQQ, inmediatamente corriente abajo del TSS MANE. La densidad de variantes anotadas en el protoespaciador es el valor más alto de las tres posiciones y debe evaluarse su frecuencia poblacional antes de considerarla.

---

## 3. Candidatas en el sitio de referencia +450

La disponibilidad de PAM en esta ventana es baja: solo tres sitios NGG en ±35 pb, frente a once y catorce en las ventanas anteriores.

| Campo | Candidata F2a | Candidata F2b |
| :--- | :--- | :--- |
| Protoespaciador (5′→3′) | `TGGTCTCTGAGGACTGAGAT` | `TGCAGTCAGCTGTGTTTCTT` |
| PAM | `CGG` | `TGG` |
| Hebra | + | + |
| Extremo 5′ del protoespaciador | 53.704.573 | 53.704.613 |
| Extremo 3′ del protoespaciador | 53.704.592 | 53.704.632 |
| Intervalo ocupado | 53.704.573-53.704.592 | 53.704.613-53.704.632 |
| Punto medio | 53.704.582 | 53.704.622 |
| Contenido GC | 50 % | 45 % |
| Distancia al TSS MANE de *FTO* | +426 | +466 |
| Distancia al cluster *FTO* | +619 | +659 |
| Distancia al TSS MANE de *RPGRIP1L* | +723 | +763 |
| Distancia al cluster *RPGRIP1L* | +644 | +684 |
| Contexto estructural | intrón 1 del transcrito MANE | intrón 1 |
| Elemento Ensembl | enhancer ENSR16_BDMQQ | enhancer ENSR16_BDMQQ |
| cCRE ENCODE | **EH38E1816377, pELS, score 214** | **EH38E1816377, pELS** |
| GeneHancer | GH16J053703 | ídem |
| TSS anotados dentro o cerca del protoespaciador | ninguno en ±300 pb | ninguno en ±300 pb |
| Variantes anotadas en el intervalo | 4 variantes, todas con consecuencia de tipo intrónica | no consultado |
| Actividad prevista | no evaluada | no evaluada |
| Especificidad prevista | no evaluada | no evaluada |
| Riesgo interpretativo | el más bajo de los tres sitios en cuanto a ambigüedad de gen diana | ídem |

**Marca solicitada.** Este sitio efectivamente cae sobre el pELS EH38E1816377 y está libre de sitios de inicio anotados en un radio de 300 pb. Es la única de las tres posiciones que coincide simultáneamente con un elemento de tipo enhancer en Ensembl y con una firma de tipo enhancer proximal en ENCODE. Bajo la segmentación de GeneHancer, en cambio, sigue perteneciendo al mismo bloque que el promotor divergente.

---

## 4. Resumen comparativo

| Sitio | Ambigüedad de gen diana | Coincidencia Ensembl y ENCODE | Densidad de variantes | Disponibilidad de PAM |
| :--- | :--- | :--- | :--- | :--- |
| −200 | máxima | promotor en ambos universos | nula | alta (11 sitios en ±35 pb) |
| +60 | baja respecto de *RPGRIP1L*, alta respecto de la naturaleza del elemento | enhancer en Ensembl, promotor en ENCODE | alta, en secuencia codificante | alta (14 sitios) |
| +450 | la más baja | enhancer en Ensembl, enhancer proximal en ENCODE | baja, intrónica | baja (3 sitios) |

---

## 5. Lo que falta para poder seleccionar

1. Puntajes de actividad predicha para cada protoespaciador, con herramienta y versión declaradas.
2. Análisis de sitios fuera de blanco a escala genómica, con número de desapareamientos y ubicación exónica o no exónica, según el criterio del ejercicio 5 de la cartilla.
3. Frecuencia poblacional de las variantes que solapan cada protoespaciador, en particular las doce del sitio +60.
4. Verificación de la secuencia semilla de cada candidata frente a sus sitios fuera de blanco.
5. Decisión sobre si se conserva el sitio +60 dado su carácter exónico y codificante.

---

## 6. Clasificación de las afirmaciones de este archivo

| Categoría | Contenido |
| :--- | :--- |
| Hechos de anotación oficial | Secuencias, coordenadas, PAM, contenido GC, elementos Ensembl, cCRE, GeneHancer, variantes y sus consecuencias |
| Evidencia experimental publicada | Ninguna |
| Inferencias de integración | Las lecturas de riesgo interpretativo de cada sitio y el resumen comparativo de la sección 4 |
| Decisiones de diseño | Ninguna. No se selecciona guía |
