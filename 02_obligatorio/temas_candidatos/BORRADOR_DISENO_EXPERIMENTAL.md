---
type: borrador-entregable
status: en-curso
date: 2026-07-26
source: "ESQUELETO_OBLIGATORIO.md v3 + DECISIONES_DISENO.md + FTO_anexo_tecnico/"
---

# Borrador de la sección 3, Diseño Experimental

Texto destinado al entregable. Cada subsección lleva su estado. Solo el texto marcado como cerrado se considera definitivo.

---

## 3.1 Estrategia general y justificación del abordaje

**Estado: cerrada el 2026-07-26.** Extensión aproximada 0,55 carillas. La tabla comparativa de efectores evaluados se traslada al anexo, por documentar alternativas consideradas durante la elección del abordaje y no la arquitectura del sistema.

Sobre ese marco general, el diseño adopta cuatro decisiones que conviene explicitar antes de describir el locus.

La primera es intervenir el locus endógeno de *FTO* en lugar de introducir una copia adicional del gen, de modo que la transcripción quede sujeta a la arquitectura regulatoria propia del sitio y no a un promotor heterólogo. La segunda deriva de esa misma arquitectura: puesto que las anotaciones consultadas no identifican una región promotora próxima demostrablemente exclusiva de *FTO*, no existe fundamento suficiente para elegir de antemano una única región de intervención, y el diseño compara varias regiones regulatorias con un mismo efector.

La tercera decisión es el efector, una Cas9 catalíticamente inactiva (dCas9) fusionada al dominio catalítico de la acetiltransferasa p300. Hilton et al. (2015) demostraron que esta fusión activa genes endógenos tanto desde regiones promotoras como desde elementos potenciadores, propiedad especialmente adecuada para un diseño que compara con un mismo efector regiones de naturaleza y posición diferentes. Deposita además acetilación de la lisina 27 de la histona H3 de manera localizada, lo cual permite verificar por inmunoprecipitación de cromatina que el sistema actuó en el sitio dirigido, en lugar de inferirlo únicamente a partir del cambio de expresión. Por último, los dos antecedentes más próximos al proyecto emplean este mismo efector: su aplicación en células de la granulosa porcina (Liao et al., 2026) y la activación de *FTO* endógeno en una línea celular humana (Kachanov et al., 2025).

Cabe aclarar que p300 no es necesariamente el activador de mayor magnitud. En una comparación directa entre dominios activadores sobre dos genes en células HEK293, VPR resultó más eficaz que VP64 y que p300 (Akçakale Kaba et al., 2025). Este resultado, obtenido sobre otros genes, con cuatro ARN guía y en un contexto celular diferente, no puede extrapolarse al locus de *FTO* ni al modelo de granulosa. Asimismo, en la literatura revisada no se identificó una comparación directa entre activadores sobre este locus. Ergo, la cuarta decisión consiste en tratar tanto la eficacia como la región de mayor rendimiento como cuestiones a determinar experimentalmente, y no como supuestos del diseño.

### Notas de trabajo de 3.1, no se trasladan al entregable

**Citas verificadas contra texto completo**: Hilton et al. (2015), Liao et al. (2026), Kachanov et al. (2025).

**Auditoría del último párrafo, resuelta el 2026-07-26.** De las tres afirmaciones originales se conserva una sola, con respaldo verificado contra texto completo.

*Conservada*: Akçakale Kaba F, Akıncı E, Cengiz MF, Kaba A (2025). *Comparison of dCas9-activator complexes for the activation of PDX1 and NGN3 pancreatic genes using the CRISPR system*. Trakya University Journal of Natural Sciences 26(1):49-59. DOI 10.23902/trkjnat.1622077. Pasaje literal: "we compared three activator domains (VP64, VPR, and p300) and found VPR to be the most effective". Se acota explícitamente su alcance en el propio texto.

*Retirada de 3.1, reservada para la subsección de entrega o para la Discusión*: Meneghini V et al. (2021), Frontiers in Genome Editing, DOI 10.3389/fgeed.2021.644319. Pasaje literal: "AAV delivery of base and epigenome editors is complicated by the low cargo capacity of the AAV genome". Demuestra una limitación específica de los vectores adenoasociados por capacidad de carga, no una dificultad general de entrega, y el diseño emplea transfección transitoria.

*Retirada por atribución incorrecta, conservada en notas de alternativas evaluadas*: Weltner J et al. (2018), Nature Communications 9:2643, DOI 10.1038/s41467-018-05067-x. El trabajo evaluó la adición del dominio p300 a activadores que ya contenían VP192, según consta en métodos ("dCas9VPP300 was cloned by PCR amplifying the P300 core domain from human cDNA and cloning it after the VP192 domain"), y no dCas9-p300 como efector independiente. No sirve para afirmar dependencia del contexto celular de dCas9-p300. En el corpus figuraba como "jere_2018", que es el nombre de pila del primer autor.

**Sobre la traducción del término.** La fuente primaria dice literalmente "the catalytic core of the human acetyltransferase p300" (Hilton et al., 2015), de modo que tanto "núcleo catalítico" como "dominio catalítico" son defendibles. Se adopta "dominio catalítico" por ser la forma más habitual en la literatura en español.

---
## 3.2 Metodología del análisis genómico y regulatorio

**Estado: cerrada el 2026-07-26.** Extensión aproximada 0,7 carillas incluyendo la tabla.

El análisis del locus se apoyó en las fuentes reunidas en la Tabla 1, seleccionadas para cubrir cuatro funciones distintas: la anotación estructural del gen y sus transcritos, la clasificación epigenómica de los elementos regulatorios, la evidencia de iniciación transcripcional, y la integración de asociaciones entre elementos y genes. Conviene distinguir la fuente biológica de la herramienta empleada para consultarla y de la empleada para procesar el resultado, puesto que las interfaces de consulta programática y las rutinas de análisis son medios de acceso y de procesamiento, y no fuentes de evidencia en sí mismas.

El análisis se realizó sobre el ensamblado de *Homo sapiens* GRCh38.p14, con la anotación de Ensembl release 116 y GENCODE release 50. Como transcritos de referencia se adoptaron *FTO-206* y *RPGRIP1L-212*, porque poseen la etiqueta MANE Select, que indica concordancia entre Ensembl/GENCODE y NCBI RefSeq. Esta elección normaliza las coordenadas, pero no demuestra que sean los transcritos más utilizados en granulosa. En adelante se emplea la expresión sitio de inicio de la transcripción de referencia, abreviada como TSS de referencia.

Todas las coordenadas se expresan en base 1 con extremos inclusivos. Las consultas al navegador UCSC devuelven coordenadas en base 0 con extremo final exclusivo, de modo que se normalizaron antes de integrarlas en las tablas. Las coordenadas de los picos CAGE de FANTOM5 disponibles en hg19 se utilizaron únicamente como evidencia cualitativa de iniciación transcripcional divergente, sin integrarlas en las tablas construidas sobre GRCh38 ni emplearlas para el diseño de guías.

Las anotaciones se extrajeron y procesaron de forma programática, mediante las interfaces de consulta de Ensembl y del navegador UCSC y con rutinas de análisis en Python, y se compararon, reconciliaron y verificaron de manera manual. El procedimiento comprendió el control de coordenadas y de ensamblado entre fuentes, la inspección de la secuencia genómica de referencia de la región y la comprobación de la disponibilidad general de motivos PAM NGG compatibles con SpCas9, el contraste entre la estructura del gen y los elementos regulatorios superpuestos, y la identificación y corrección de las inconsistencias detectadas entre bases.

Cabe aclarar que los conjuntos de elementos regulatorios empleados son agregados de múltiples tipos celulares y no informan actividad en un tipo celular determinado. Por ese motivo, a lo largo del trabajo se distinguen tres niveles de afirmación: los hechos de anotación oficial, la evidencia experimental publicada y las inferencias derivadas de integrar fuentes distintas. Las decisiones de diseño se enuncian por separado y se identifican como tales.

**Tabla 1. Fuentes de anotación consultadas.**

| Fuente | Qué aporta | Uso en este trabajo | Limitación declarada |
| :--- | :--- | :--- | :--- |
| Ensembl release 116 y GENCODE release 50 | Genes, transcritos y exones | Anotación estructural del locus, con descarga por la interfaz de consulta programática de Ensembl | Anotación de referencia; no informa actividad en un tipo celular determinado |
| Ensembl Regulatory Build, release 116 | Promotores, enhancers y sitios de unión de CTCF | Segmentación regulatoria de la región y lectura de los genes asociados a cada elemento | Conjunto agregado a partir de múltiples tipos celulares; no informa actividad en granulosa |
| MANE Select | Concordancia entre Ensembl/GENCODE y NCBI RefSeq | Fijación de los transcritos de referencia y normalización de coordenadas | No informa uso relativo de los transcritos en el tejido de interés |
| ENCODE cCRE | Clasificación epigenómica de elementos candidatos | Clasificación independiente, contrastada con la segmentación de Ensembl, consultada por la interfaz del navegador UCSC | Deriva de un conjunto de tipos celulares que no incluye granulosa humana |
| GeneHancer | Asociaciones integradas entre elementos regulatorios y genes | Evidencia integradora secundaria, complementaria a la asignación de genes asociados de Ensembl, consultada por la interfaz del navegador UCSC | Fusiona en un único bloque elementos que otras bases segmentan; no reemplaza la segmentación de Ensembl |
| FANTOM5 CAGE | Evidencia de iniciación transcripcional | Respaldo cualitativo de la iniciación divergente en la región | Coordenadas disponibles en hg19, no integradas a las tablas construidas sobre GRCh38 |

---

### Notas de trabajo de 3.2, no se trasladan al entregable

**EPDnew** no figura en la tabla porque no se consultó de forma independiente: apareció como fuente integrada dentro de la anotación de GeneHancer. Se menciona en el anexo con esa aclaración.

**Al anexo**: endpoints exactos consultados, fechas de consulta, versiones y coordenadas de cada llamada.

**Decisión operativa pendiente**: ejecutar CRISPOR y declarar versión y genoma empleados. Hasta entonces, la tabla no incluye herramientas de diseño de guías, que corresponden a 3.5.

---

## 3.3 Caracterización del locus FTO–RPGRIP1L: arquitectura divergente y promotor compartido

**Estado: cerrada el 2026-07-26.** Extensión aproximada 0,9 carillas apoyándose en la figura del locus.

El locus presenta una disposición divergente. *FTO* se transcribe en sentido creciente de coordenadas y *RPGRIP1L* en sentido opuesto, de modo que ambos genes inician su transcripción alejándose uno del otro y comparten la región comprendida entre sus extremos 5′ (Figura 2). Su consecuencia inmediata es que la región corriente arriba de *FTO* es, simultáneamente, la región corriente arriba de *RPGRIP1L*.

Los sitios de inicio de referencia de ambos genes están separados por 297 pares de bases. Esa distancia no delimita, sin embargo, un intervalo vacío. Dentro de él se ubican además dos agrupamientos de inicio alternativos, uno por gen, separados entre sí por apenas 25 pares de bases. El número de transcritos anotados que comparte cada coordenada no permite establecer cuál de esos inicios se utiliza preferentemente en células de la granulosa. Esta arquitectura es consistente con los picos CAGE de FANTOM5 asociados a ambos genes, que aportan evidencia independiente de iniciación transcripcional divergente.

Sobre ese intervalo, el Ensembl Regulatory Build anota un único elemento de tipo promotor que contiene los sitios de inicio de los dos genes y que la propia base asigna de manera simultánea a *FTO* y a *RPGRIP1L*. No se trata, por lo tanto, de una interpretación derivada de la proximidad entre coordenadas, sino de una asignación explícita de la anotación.

La segmentación de la región depende de la base consultada. Ensembl distingue tres elementos consecutivos, un promotor flanqueado por dos elementos clasificados como enhancer; ENCODE identifica dos firmas de promotor y una de enhancer proximal, con límites que no coinciden con los anteriores; y GeneHancer engloba la región en un único bloque clasificado a la vez como promotor y enhancer. Ergo, afirmar que una posición determinada pertenece a un elemento o a otro es una afirmación relativa al universo de anotación empleado, y este trabajo adopta la segmentación de Ensembl como referencia, según se declaró en la metodología.

De lo anterior se desprende que las anotaciones consultadas no identifican dentro del intervalo analizado una región promotora próxima demostrablemente exclusiva de *FTO*. Esta observación tiene dos consecuencias directas sobre el diseño. La primera es de atribución: cualquier modificación introducida sobre el bloque compartido puede afectar la transcripción de ambos genes, de modo que un cambio en el fenotipo no podría atribuirse exclusivamente a *FTO* sin verificar simultáneamente el comportamiento de *RPGRIP1L*. La segunda es de medición: toda lectura experimental debe incluir los dos genes, y toda posición de intervención debe caracterizarse por su distancia a los dos TSS de referencia y a los dos inicios alternativos.

Cabe mencionar que *RPGRIP1L* codifica un componente de la zona de transición del cilio primario. Por lo tanto, un cambio en su expresión constituye una posible fuente de confusión biológica, aunque sus consecuencias específicas en células de la granulosa no están establecidas. Compartir la misma firma promotora eleva el riesgo de afectar ambos genes, pero no demuestra coactivación ni permite anticipar la dirección o la magnitud de las respuestas.

---

### Notas de trabajo de 3.3, no se trasladan al entregable

**Al anexo o a la figura**: identificadores de cada elemento regulatorio, coordenadas exactas de los cuatro sitios de inicio, recuento de transcritos por agrupamiento, límites de cada elemento en los tres universos de anotación, y la tabla de alineación entre ellos.

**Referencia no incorporada**: Trinklein et al. (2004) sobre abundancia de promotores bidireccionales en el genoma humano. El dato es correcto y está verificado, pero no sostiene ninguna decisión del proyecto y se decidió no abrir una referencia adicional. Queda disponible por si hiciera falta en la defensa oral.

**Estado de la afirmación sobre *RPGRIP1L***: verificada. La localización como componente estructural de la zona de transición del cilio primario consta literalmente en Stratigopoulos et al. (2016), texto completo auditado. No requiere reformulación por falta de respaldo; el alcance quedó acotado a que sus consecuencias en granulosa no están establecidas.

**Sobre FANTOM5**: la advertencia acerca de las coordenadas en hg19 no se repite acá, puesto que ya quedó establecida en 3.2.

**Dependencia**: esta subsección requiere la Figura 2, que todavía no está producida. Sin ella, la explicación de la arquitectura obliga a enumerar coordenadas en prosa.

---
## 3.4 Definición y justificación de las regiones blanco

**Estado: cerrada el 2026-07-26.** Extensión aproximada 450 palabras, sin contar el pie de figura.

Puesto que las anotaciones consultadas no permiten elegir de antemano una única región de intervención, se caracterizaron cuatro regiones del entorno regulatorio proximal. Tres se conservaron para su comparación experimental y una se retiró durante el proceso de selección. Las cuatro quedan englobadas por un mismo elemento integrado de GeneHancer, de modo que esa clasificación no las distingue entre sí (Figura 3).

El centro del promotor divergente *FTO*–*RPGRIP1L* se ubica entre los dos inicios alternativos, algo más de doscientos pares de bases corriente arriba del TSS de referencia de *FTO* y menos de cien del de *RPGRIP1L*. Ensembl lo clasifica como promotor y ENCODE le asigna la firma de promotor de mayor puntaje de la región. Permite evaluar el efecto de acetilar el elemento promotor compartido y es, por posición, la región de mayor ambigüedad respecto del gen afectado.

La región promotora próxima al TSS de referencia de *FTO* se sitúa algunas decenas de pares de bases corriente arriba de ese sitio y comparte con la anterior el elemento de Ensembl y la firma de ENCODE. Esta región se encuentra corriente arriba del exón 1 del transcrito de referencia, pero forma parte de la 5′ UTR exónica de isoformas que comienzan en el inicio alternativo de *FTO*, de modo que no corresponde describirla como intergénica. Permite evaluar la activación desde una posición orientada al transcrito de referencia, aunque continúa perteneciendo al mismo elemento promotor compartido.

La región codificante del exón 1 del transcrito de referencia de *FTO* fue analizada durante la selección y retirada del panel. Se ubica inmediatamente corriente abajo del TSS de referencia, dentro de secuencia codificante, y presenta una densidad elevada de variantes anotadas. El retiro responde a un criterio interpretativo: la unión del complejo tan próxima al inicio y sobre secuencia codificante introduce un riesgo de ocupación estérica cuyos efectos serían difíciles de separar de los de la acetilación dirigida.

La región intrónica con firma pELS se ubica algunos cientos de pares de bases corriente abajo del TSS de referencia, ya dentro del primer intrón. Ensembl la incluye en un elemento clasificado como enhancer y ENCODE le asigna una firma de enhancer proximal. Es la única región conservada que coincide simultáneamente con una clasificación de tipo enhancer en ambos universos de anotación. Es además la más alejada de los sitios de inicio de *RPGRIP1L* y permite evaluar si la acetilación de un elemento regulador intrónico aumenta la expresión de *FTO* y produce un cambio menor en *RPGRIP1L* que la intervención sobre el promotor divergente.

Tres advertencias atraviesan estas descripciones. Una clasificación como enhancer o como firma de enhancer proximal no demuestra que la región regule *FTO* en granulosa, de modo que la región intrónica no debe denominarse enhancer de *FTO*. La pertenencia de una posición a un elemento o a otro depende de la base consultada. Y el contexto estructural de una región puede ser exónico para unos transcritos e intergénico para otros, según cuál se tome como referencia.

### Notas de trabajo de 3.4, no se trasladan al entregable

**Figura 3**: las cuatro regiones representadas como bloques sobre el mapa del locus, con los dos TSS de referencia y los dos inicios alternativos señalados. Sin protoespaciadores, sin PAM y sin coordenadas de puntos medios.

**Deliberadamente ausentes**: distancias exactas, protoespaciadores, motivos PAM, puntajes, variantes individuales y toda posición calculada desde protoespaciadores. Corresponden a 3.5 y al anexo.

**Sitios CUX1**: excluidos por decisión registrada. Se documentan en el anexo, se mencionan brevemente en la Discusión y quedan disponibles para la defensa oral.

**Nomenclatura**: tras el primer uso completo, los nombres se abrevian cuando la referencia es inequívoca. No se emplean siglas ni se recuperan los códigos históricos de ventanas.

