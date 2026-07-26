# Guía maestra auditada del locus humano **FTO**

## 1. Propósito y alcance exacto

Este documento reúne una extracción reproducible y revisada de la estructura del gen humano **FTO** y de los elementos reguladores anotados en su intervalo genómico. Está preparado para ser utilizado como contexto maestro por otra inteligencia artificial durante el diseño del Obligatorio del Taller de Ingeniería Genética.

La extracción se realizó bajo una definición explícita de exhaustividad:

- **Gen:** `FTO`, Ensembl Gene `ENSG00000140718`.
- **Transcrito estructural de referencia:** `ENST00000471389.6`, denominado `FTO-206`.
- **Estado del transcrito:** MANE Select, Ensembl canonical, GENCODE primary y GENCODE basic.
- **Ensamblado:** GRCh38.p14.
- **Ensembl:** release 116.
- **GENCODE:** release 50.
- **Intervalo analizado:** `chr16:53,702,356-54,121,941`.
- **Sentido:** hebra positiva.
- **Ventana upstream:** 1.800 pares de bases, es decir, **1,8 kb**, antes del TSS del transcrito MANE.
- **Sistema de coordenadas:** GFF3, coordenadas de base 1 e inclusivas.

“Todos los exones” significa los nueve exones de `ENST00000471389.6`. No significa la unión de todos los exones empleados por cualquier isoforma de FTO.

“Todos los enhancers” significa todas las entradas cuyo tipo es `enhancer` en el archivo oficial **Ensembl Regulatory Features v116** y que solapan el intervalo definido. No significa que todos esos elementos regulen FTO ni que estén activos en células de la granulosa.

## 2. Fuentes primarias y trazabilidad

La tabla se extrajo directamente de:

1. Ensembl release 116, anotación génica del cromosoma 16:
   `https://ftp.ensembl.org/pub/release-116/gff3/homo_sapiens/Homo_sapiens.GRCh38.116.chromosome.16.gff3.gz`
2. Ensembl Regulatory Features v116:
   `https://ftp.ensembl.org/pub/release-116/regulation/homo_sapiens/GRCh38/annotation/Homo_sapiens.GRCh38.regulatory_features.v116.gff3.gz`
3. Descripción del genebuild:
   `https://www.ensembl.org/Homo_sapiens/Info/Annotation`
4. Metodología del Regulatory Build:
   `https://regulation.ensembl.org/help/regulatory_build`

La anotación fue extraída automáticamente, no transcrita a ojo desde la imagen del navegador. La imagen entregada por el usuario se utilizó como verificación visual del patrón general, pero no como fuente de coordenadas.

## 3. Delimitación del locus

El transcrito MANE `ENST00000471389.6` se extiende desde:

- TSS/extremo 5′: `chr16:53,704,156`
- Extremo 3′: `chr16:54,121,941`

Como FTO se encuentra en la hebra positiva, 1.800 bp upstream corresponde a restar 1.800 al TSS:

`53,704,156 - 1,800 = 53,702,356`

Por tanto, el intervalo auditado es:

`chr16:53,702,356-54,121,941`

Su longitud total es de 419.586 bp, incluyendo ambos extremos.

## 4. Arquitectura de exones del transcrito MANE

Se recuperaron exactamente **9 exones**. Sus coordenadas son:

| Exón | Ensembl exon ID | Inicio | Fin | Longitud |
|---:|---|---:|---:|---:|
| 1 | `ENSE00003793523` | 53,704,156 | 53,704,229 | 74 bp |
| 2 | `ENSE00003499057` | 53,810,140 | 53,810,217 | 78 bp |
| 3 | `ENSE00001319762` | 53,825,864 | 53,826,491 | 628 bp |
| 4 | `ENSE00003480244` | 53,844,155 | 53,844,298 | 144 bp |
| 5 | `ENSE00003523757` | 53,873,786 | 53,873,865 | 80 bp |
| 6 | `ENSE00003575733` | 53,879,844 | 53,879,987 | 144 bp |
| 7 | `ENSE00003604517` | 53,888,832 | 53,888,951 | 120 bp |
| 8 | `ENSE00003492841` | 53,933,985 | 53,934,109 | 125 bp |
| 9 | `ENSE00001946879` | 54,111,762 | 54,121,941 | 10,180 bp |

La suma de las longitudes exónicas es de 11,573 bp. Esa suma incluye UTR y CDS porque la característica `exon` del GFF3 representa el exón completo. No debe confundirse con la longitud de la secuencia codificante.

El exón 1 es corto y contiene el TSS del transcrito. El exón 9 es muy largo porque incluye una región 3′ no traducida extensa. La mayor parte del locus está compuesta por intrones, especialmente el intrón 8, que separa los exones 8 y 9.

## 5. Inventario regulador

Dentro del intervalo se recuperaron **69 características regulatorias**:

- **Enhancers:** 59
- **Promotores:** 2
- **Sitios CTCF:** 8

Los 59 enhancers tienen longitudes entre 119 y 2,141 bp, con una mediana de 397 bp.

Distribución por contexto respecto del transcrito MANE:

- **intron 1:** 22
- **intron 2:** 4
- **intron 3:** 2
- **intron 4:** 2
- **intron 6:** 1
- **intron 7:** 9
- **intron 8:** 17
- **overlaps exon 1:** 1
- **upstream:** 1

### 5.1. Elementos próximos al TSS

Tres observaciones son especialmente importantes:

1. **`ENSR16_9RBJ8`**, `chr16:53,703,398-53,703,830`, es un enhancer completamente upstream. Está dentro de la ventana de 1,8 kb y termina 326 bp antes del TSS.

2. **`ENSR16_9RBJC`**, `chr16:53,703,831-53,704,167`, está anotado como promotor y se asocia simultáneamente con **RPGRIP1L** y **FTO**. Esto muestra que el extremo 5′ de FTO se encuentra en un contexto promotor compartido o inmediatamente adyacente. La selección de guías debe evitar asumir que cualquier modificación local será exclusiva de FTO.

3. **`ENSR16_BDMQQ`**, `chr16:53,704,168-53,704,740`, está anotado como enhancer. Comienza dentro del exón 1 y se extiende hacia el intrón 1. La coexistencia de etiquetas promotor/enhancer alrededor del TSS no es una contradicción: son categorías del Regulatory Build obtenidas por integración de accesibilidad, posición respecto de TSS y marcas de histonas.

### 5.2. Regiones intrónicas candidatas a enhancer

La mayoría de los elementos anotados como enhancer se encuentra dentro de intrones. Esto es coherente con la conocida densidad reguladora del locus FTO, en particular en su región intrónica inicial. Sin embargo, la localización intrónica por sí sola no permite asignar el gen diana, y la etiqueta de la base de datos no demuestra función reguladora sobre FTO en un tipo celular determinado. Por ese motivo el término adoptado en el proyecto es **región intrónica candidata a enhancer**, o **región intrónica con firma pELS** cuando se trate de la clasificación de ENCODE.

Una región intrónica candidata a enhancer en el locus de FTO puede:

- regular FTO;
- regular un promotor alternativo de FTO;
- actuar sobre RPGRIP1L;
- establecer contactos con genes distales como IRX3 o IRX5;
- no estar activo en el tipo celular estudiado.

Por eso la tabla emplea el término **“locus_context”** y no “gen regulado”.

### 5.3. Sitios CTCF

Se identificaron ocho sitios CTCF dentro del intervalo. CTCF puede participar en la organización de límites, bucles y contactos cromatínicos. Su solapamiento con un enhancer no invalida ninguna de las dos anotaciones. Indica que una misma región puede contener una característica amplia de cromatina y un motivo CTCF más estrecho.

Para un proyecto dCas9-p300, los sitios CTCF merecen atención porque una guía colocada demasiado cerca podría, en principio, perturbar la arquitectura local por ocupación estérica, aunque dCas9 no corte el ADN.

## 6. Qué significa realmente la etiqueta “enhancer”

El Regulatory Build de Ensembl integra datos de cromatina abierta y marcas de histonas de múltiples tejidos y líneas celulares. La clasificación enhancer no equivale a una validación funcional en granulosa.

Cada fila de la tabla debe interpretarse como:

> “Región clasificada como enhancer por el Ensembl Regulatory Build v116 dentro del intervalo definido.”

No debe reformularse automáticamente como:

> “Enhancer de FTO activo en granulosa.”

Para elevar un elemento a candidato funcional en el proyecto se requiere, idealmente:

1. accesibilidad en KGN, COV434 o granulosa primaria;
2. H3K27ac o H3K4me1 en el mismo tipo celular;
3. evidencia de contacto con el promotor de FTO;
4. asociación entre actividad del elemento y expresión de FTO;
5. perturbación funcional mediante CRISPRa, CRISPRi o deleción.

## 7. Implicancias para el diseño dCas9-p300

El proyecto propone activar FTO mediante deposición dirigida de H3K27ac. El inventario muestra que el extremo 5′ no es una región reguladora simple, sino un bloque estrecho en el que se suceden:

`enhancer upstream → promotor RPGRIP1L/FTO → enhancer que solapa exón 1`

Esto tiene varias consecuencias.

### 7.1. No diseñar por “inicio del gen”

La guía debe diseñarse respecto del TSS de `ENST00000471389.6`, no respecto del límite externo de `ENSG00000140718` ni respecto de una coordenada tomada de RefSeq sin reconciliación.

### 7.2. Proteger RPGRIP1L

El promotor `ENSR16_9RBJC` está asociado con FTO y RPGRIP1L. Por tanto, la validación debe incluir expresión de RPGRIP1L. Una activación de FTO acompañada de cambios en RPGRIP1L no sería necesariamente un efecto off-target de secuencia; podría ser un efecto cis local de la acetilación.

### 7.3. Priorizar un panel de guías

No existe fundamento para elegir una sola guía antes de evaluar:

- distancia al TSS;
- superposición con el promotor;
- superposición con el enhancer proximal;
- solapamiento con exón 1;
- presencia de CTCF;
- variantes frecuentes;
- especificidad genómica;
- cromatina accesible en granulosa.

Conviene diseñar varias guías teseladas y probarlas individualmente antes de combinarlas.

### 7.4. Distinguir activación de edición cromatínica

Una guía puede aumentar FTO sin que el aumento dependa de H3K27ac, por ejemplo por reclutamiento indirecto o perturbación local. Por eso se necesitan:

- dCas9-p300 catalíticamente activa;
- p300 catalíticamente inactiva;
- dCas9 sin efector;
- guía no dirigida;
- medición de H3K27ac en el locus;
- medición de FTO;
- medición de RPGRIP1L.

## 8. Límites de este inventario

Este archivo no incluye automáticamente:

- enhancers distales fuera del intervalo que contacten FTO;
- GeneHancer, ENCODE cCRE o FANTOM5 como universos separados;
- actividad específica por tejido;
- contactos Hi-C, promoter capture Hi-C o Micro-C;
- variantes y haplotipos;
- motivos de factores de transcripción;
- secuencia genómica;
- guías CRISPR;
- resultados experimentales en granulosa.

Estos datos deben incorporarse como capas adicionales y conservar su fuente original. No deben mezclarse con los 59 enhancers Ensembl como si fueran una única ontología.

## 9. Reglas maestras para otra IA

La IA que lea estos archivos debe cumplir las siguientes reglas:

1. Usar siempre GRCh38 y coordenadas 1-based inclusive al leer estas tablas.
2. No convertir coordenadas a BED sin restar 1 al inicio.
3. No decir que FTO “tiene 59 enhancers”. Decir que se identificaron 59 características Ensembl tipo enhancer dentro del intervalo definido.
4. No afirmar que los 59 regulan FTO.
5. No afirmar que están activos en granulosa.
6. No mezclar los 9 exones MANE con el conjunto agregado de exones de todas las isoformas.
7. Mantener la versión completa `ENST00000471389.6`.
8. Tratar `ENSR16_9RBJC` como promotor asociado tanto a RPGRIP1L como a FTO.
9. Considerar `ENSR16_9RBJ8`, `ENSR16_9RBJC` y `ENSR16_BDMQQ` como el bloque regulador proximal prioritario, pero no como dianas ya validadas.
10. Requerir validación de H3K27ac, expresión de FTO y expresión de genes vecinos.
11. Separar hechos, inferencias y propuestas experimentales.
12. Ante discrepancias futuras, priorizar el GFF3 oficial de la versión indicada y registrar el cambio de versión.

## 10. Archivos adjuntos y forma de lectura

- `FTO_anotacion_estructural_regulatoria_Ensembl116.xlsx`: libro principal con hojas de resumen, exones, enhancers, todos los elementos regulatorios y controles de calidad.
- `FTO_exones_MANE_Ensembl116_GRCh38.csv`: tabla plana de exones.
- `FTO_enhancers_Ensembl116_GRCh38_1p8kb_upstream.csv`: tabla plana de enhancers.
- `FTO_todos_elementos_regulatorios_Ensembl116_GRCh38_1p8kb_upstream.csv`: enhancers, promotores y CTCF.
- Este documento: interpretación, limitaciones y reglas de uso.

La IA debe comenzar por la hoja `README`, después leer `Exones_MANE`, luego `Enhancers`, y finalmente `Todos_regulatorios`. La hoja `QC_y_lectura` contiene las restricciones semánticas que deben mantenerse durante todo análisis posterior.
