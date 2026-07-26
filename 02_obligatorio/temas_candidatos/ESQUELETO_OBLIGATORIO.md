---
type: esqueleto-obligatorio
status: current
date: 2026-07-26
version: 3
source: "02_obligatorio/consigna_y_rubrica.md + rubrica_detallada.md + 00_teoria_general/cartilla_teorico.md + 03_informe/cartilla_practico.md (ejercicios) + FTO_anexo_tecnico/ + DECISIONES_DISENO.md"
related:
  - "[[02_obligatorio/temas_candidatos/DECISIONES_DISENO]]"
  - "[[02_obligatorio/temas_candidatos/FTO_anexo_tecnico/05_mapa_reconciliado_region]]"
  - "[[02_obligatorio/temas_candidatos/FTO_anexo_tecnico/09_panel_cuatro_ventanas]]"
---

# Esqueleto del Obligatorio (activación de FTO vía dCas9-p300 en granulosa humana)

Plantilla de trabajo, no entregable. La parte A prescribe la estructura del documento a entregar. La parte B es andamiaje de trabajo y no se traslada al entregable.

---

# PARTE A. Estructura del documento a entregar

## A.0 El desajuste entre consigna y rúbrica, y cómo se resuelve

La consigna fija cinco secciones: Introducción, Objetivo, Diseño Experimental, Anexos y Bibliografía. La rúbrica, en cambio, califica siete criterios pensados para un informe experimental: Introducción y Objetivos, Metodología, Resultados, Discusión y Conclusiones, Referencias, Claridad y Cumplimiento de requisitos.

Los dos documentos no son equivalentes. Tres criterios que suman **16 de los 30 puntos** (Metodología 5, Resultados 6, Discusión y Conclusiones 5) no tienen sección propia en la estructura exigida y deben quedar dentro de Diseño Experimental.

**Regla adoptada.** El documento lleva exactamente las cinco secciones de primer nivel que pide la consigna, sin agregar ninguna, porque el criterio 7 evalúa el cumplimiento de las secciones requeridas. Los criterios de la rúbrica se satisfacen mediante **subsecciones dentro de Diseño Experimental cuyos títulos contienen la palabra clave del criterio**, de modo que el evaluador encuentre cada uno donde lo busca sin que la estructura se aparte de lo pedido.

| Sección del entregable | Nivel | Criterios de rúbrica que satisface | Puntos |
| :--- | :--- | :--- | :--- |
| 1. Introducción | primer nivel | Criterio 1, parte | 5 con el Objetivo |
| 2. Objetivo | primer nivel | Criterio 1, parte | |
| 3. Diseño Experimental | primer nivel | Criterios 2, 3 y 4 | 16 |
| 4. Anexos | primer nivel | Criterio 7 | 2 |
| 5. Bibliografía | primer nivel | Criterio 5 | 3 |
| Transversal | | Criterio 6, claridad y organización | 4 |

---

## A.1 Introducción (2,5 carillas)

**Contenido**

1. Envejecimiento ovárico y papel de las células somáticas de sostén. Por qué la granulosa es el modelo tratable frente al ovocito.
2. Eje FTO–m6A–FOS, con el alcance exacto que fija B.5. Lo que puede afirmarse: que FTO se encuentra disminuido en muestras de granulosa asociadas al envejecimiento; que su silenciamiento aumenta el fenotipo senescente en los modelos celulares utilizados; que la pérdida de FTO incrementa la modificación m6A y la estabilidad del ARNm de *FOS*; que FTO se asocia con ese ARNm; que IGF2BP2 participa como lector estabilizador del transcrito metilado; y que el silenciamiento de *FOS* rescata parcialmente el fenotipo provocado por la pérdida de FTO. Lo que **no** puede escribirse es que la sobreexpresión o reposición de FTO revierta la senescencia, restaure la homeostasis, rejuvenezca las células o normalice los marcadores de daño.
3. Presentación del gen a modificar y lógica de la intervención.

**Hipótesis, con la formulación acordada**: dado que la pérdida de FTO favorece la estabilización dependiente de m6A de *FOS* y el fenotipo senescente, se plantea que la activación epigenética de la expresión endógena de FTO **podría** reducir *FOS* y **atenuar parcialmente** los marcadores de senescencia. No se emplean los verbos restaurará, revertirá ni normalizará como resultados establecidos.
4. Marco conceptual de la herramienta: cromatina, H3K27ac como marca de regiones activas, dCas9 como plataforma de reconocimiento sin corte, fusión con el núcleo catalítico de p300, definición de activación mediada por CRISPR.
5. Justificación del efector, en clave afirmativa, con bibliografía verificada.
6. Delimitación de la novedad.
7. Declaración explícita de que la edición propuesta no es un knockout sino edición de regulación génica.

**Figura**: esquema del eje FTO–m6A–FOS.

**Fuentes**: dossier del tema candidato, secciones 1 y 2; `INFORME_GENERAL.md` apartado 5.6 para el punto 5.

---

## A.2 Objetivo (0,25 carillas)

Objetivo general y tres específicos, cada uno correspondiente a una capa de validación.

General, formulación acordada: **diseñar una estrategia de activación epigenética de *FTO* mediante dCas9-p300 y evaluar si el aumento de su expresión reduce el eje m6A–FOS y atenúa parcialmente el fenotipo senescente.**

No se formula el objetivo como reponer FTO para revertir la senescencia, porque eso adelantaría un resultado todavía no demostrado.

Instrumental, con la redacción acordada: determinar qué región produce la relación más favorable entre activación de *FTO* y cambio en *RPGRIP1L*.

---

## A.3 Diseño Experimental (7 carillas)

Doce subsecciones. La columna de criterio indica a cuál de la rúbrica responde cada una.

### 3.1 Estrategia general y justificación del abordaje (0,3 carillas, criterio 2)

Esquema de la estrategia en un párrafo. Justificación del efector con la formulación acordada sobre posición: la posición respecto del TSS es un determinante importante de la eficiencia, aunque dCas9-p300 presenta flexibilidad para actuar tanto desde promotores como desde enhancers, y las posiciones seleccionadas deben validarse experimentalmente. No se enuncia ninguna ventana óptima numérica.

Tabla de efectores evaluados y descartados.

### 3.2 Metodología del análisis genómico y regulatorio (0,9 carillas, criterio 2)

Sección que el evaluador buscará como Metodología. Contiene la tabla de bases de datos con qué aporta cada una, cómo se utilizó, por qué fue seleccionada y sus limitaciones declaradas, y la descripción del procedimiento de revisión.

Explicación única de la etiqueta MANE, con esta formulación: "FTO-206 y RPGRIP1L-212 fueron adoptados como transcritos de referencia porque poseen la etiqueta MANE Select, que indica concordancia entre Ensembl/GENCODE y NCBI RefSeq. Esta elección normaliza las coordenadas, pero no demuestra que sean los transcritos más utilizados en granulosa." A partir de aquí se usa siempre "TSS de referencia".

Procedimiento a describir: descarga de anotaciones desde las fuentes citadas; comparación manual entre anotaciones de distinta procedencia; control de coordenadas y de ensamblado, manteniendo GRCh38.p14 como referencia única y sin mezclar coordenadas de hg19; revisión de la secuencia de referencia y localización de los motivos PAM disponibles; contraste entre estructura génica y elementos regulatorios superpuestos; identificación y corrección de inconsistencias entre bases; y evaluación crítica de la relevancia experimental de cada elemento.

Declaración de niveles: hechos de anotación oficial, evidencia experimental publicada, e inferencias de integración.

**Fuente**: `FTO_anexo_tecnico/04_herramientas_fuentes_y_metodologia.md`.

### 3.3 Caracterización del locus FTO–RPGRIP1L (0,9 carillas, criterio 3)

Primer bloque de resultados del análisis. Disposición divergente, sitios de inicio de referencia separados por 297 pb, elemento de tipo promotor anotado por Ensembl asignado a ambos genes, y los dos clusters alternativos de inicio separados entre sí por 25 pb.

**Formulación obligatoria del alcance**: las anotaciones consultadas no identifican dentro de esta ventana una región promotora proximal demostrablemente exclusiva de *FTO*. No se enuncia como conclusión absoluta, puesto que describe el estado de las anotaciones disponibles y no una propiedad probada del locus.

Debe quedar explícito que la segmentación en promotor y enhancer depende del universo de anotación, y que la comparación de regiones se apoya en la segmentación de Ensembl.

**Figura**: mapa del locus con ambos genes, orientaciones, los cuatro sitios de inicio, elementos de Ensembl y cCRE.

**Fuente**: `FTO_anexo_tecnico/05_mapa_reconciliado_region.md`.

### 3.4 Definición de las regiones blanco (0,7 carillas, criterios 2 y 3)

Las cuatro ventanas con nombre, ubicación, elementos superpuestos y función. W2 se documenta como analizada y retirada por su localización exónica codificante.

Las dos preguntas experimentales, con la redacción acordada. Para W3: ¿la acetilación del pELS intrónico aumenta *FTO* y produce menor coactivación de *RPGRIP1L* que la acetilación del promotor divergente? Para W4: ¿la acetilación próxima al TSS de referencia aumenta *FTO* y con qué efecto sobre *RPGRIP1L*?

Debe decirse que la clasificación de W3 como enhancer o pELS no demuestra que regule *FTO* en granulosa, y que la razón de incluir promotor y enhancer no es que ambas estrategias estén demostradas en este locus sino que no hay evidencia suficiente para elegir una a priori.

**Figura**: ventanas y candidatas sobre el mapa.

### 3.5 Diseño de guías: procedimiento y resultados (0,9 carillas, criterios 2 y 3)

Procedimiento, criterios de inclusión y exclusión, y candidatas con sus cuatro distancias.

Exclusiones ya aplicadas: corridas de cuatro o más timidinas, por terminación de la ARN polimerasa III en el sistema con promotor U6; y localización en secuencia codificante.

Pendientes: puntaje de actividad predicha, off-targets con estado de la secuencia semilla, y frecuencia poblacional de las variantes superpuestas.

**Las dos listas de prioridad, que no se mezclan.** Expectativa mecanística de activación: las candidatas promotoras de W4 y W1 tienen mayor probabilidad de activación directa que las de W3, en términos cualitativos, sin establecer cuál de W4 o W1 activará más. Interpretabilidad: W3, W4, W1, y W2 retirada.

Formulación obligatoria: W3 se presenta como la candidata más limpia para interpretar un posible efecto mediado por enhancer, no como la que probablemente más active. W4 se presenta como la más directamente orientada a la activación promotora próxima al TSS de referencia de *FTO*.

**Tabla**: candidatas con secuencia, PAM, hebra, coordenadas, GC, las cuatro distancias, elementos superpuestos y variantes.

### 3.6 Construcción del efector y clonado (0,6 carillas, criterio 2)

Arquitectura del constructo con etiqueta en el extremo amino de la dCas9; sistema de dos plásmidos; clonado por Golden Gate con enzima de tipo IIS; verificación del clon por secuenciación con cebador sobre el promotor U6.

**Figura**: mapas del constructo y del vector de guía, anotados.

### 3.7 Modelo celular, condición de envejecimiento y entrega (0,3 carillas, criterio 2)

Línea celular, inducción del fenotipo por estrés oxidativo y sistema de entrega, resueltos como decisión y no como repaso de opciones.

### 3.8 Panel experimental y controles (0,5 carillas, criterio 2)

Cinco brazos: guía W4 próxima al TSS de referencia; segunda candidata de W4 o W3 a definir tras actividad y off-targets; guía W3 en la región intrónica candidata a enhancer; guía W1 como comparador del promotor divergente; y combinación W4 más W3.

**Controles, contados aparte de los cinco brazos y sin solaparse entre sí.**

| Control | Composición | Qué descarta |
| :--- | :--- | :--- |
| Control negativo principal | dCas9-p300 con **guía no dirigida** (scrambled) | Efecto atribuible a la presencia del efector y del sistema de expresión, con independencia del sitio |
| Control de entrega | Vector vacío o vehículo de transfección, según corresponda al sistema experimental empleado | Efecto del procedimiento de entrega sobre las lecturas |
| Control mecanístico | **dCas9-p300 catalíticamente inactivo, o dCas9 sin el dominio funcional de p300, dirigido con la misma guía** que el brazo correspondiente | Separa el efecto de la acetilación del efecto del anclaje del complejo en el sitio. Es el control mecanístico ideal |

La formulación anterior, "dCas9-p300 sin guía dirigida", queda retirada por ambigua y por solaparse con el control negativo principal.

En todos los brazos se miden *FTO* y *RPGRIP1L*.

### 3.9 Estrategia de validación (0,6 carillas, criterio 2)

Tres capas. Primera, el sistema actuó donde debía: inmunoprecipitación de cromatina anti-etiqueta y de H3K27ac sobre la ventana dirigida, con amplicón control positivo y amplicón control negativo distal. Segunda, la transcripción respondió: expresión de *FTO* y de *RPGRIP1L*; **enriquecimiento de m6A en la región seleccionada del 3′ UTR de *FOS* mediante MeRIP-qPCR**; y estabilidad del mensajero de *FOS*. Tercera, el fenotipo se movió: panel de senescencia y daño al ADN, con lectura esperable de desacople parcial.

**Precisión sobre la resolución del método.** MeRIP-qPCR mide enriquecimiento regional y no tiene resolución de nucleótido individual, de modo que no corresponde llamarlo m6A sitio específica. El término sitio específico se reserva para métodos con resolución compatible, como SELECT o miCLIP, y solo se emplea si alguno de ellos se incorpora al diseño.

**Figura**: posición de los amplicones. **Tabla**: primers con la región donde hibrida cada conjunto.

### 3.10 Resultados esperados y criterios de decisión (0,3 carillas, criterio 3)

Los resultados esperados se separan por nivel de proximidad causal, y no se presentan como una lista homogénea.

**Resultados primarios esperados**, próximos a la intervención: aumento de *FTO*; reducción de *FOS*; disminución del enriquecimiento de m6A en la región evaluada del 3′ UTR de *FOS*; reducción de la estabilidad del ARNm de *FOS*.

**Resultado fenotípico a evaluar**, distante de la intervención y no garantizado: disminución parcial de SA-β-galactosidasa; disminución parcial de γH2AX; y los demás marcadores del panel, incorporados desde fuentes distintas de Jiang et al. (2021) y citados como tales.

La disminución de marcadores de senescencia **no se presenta como consecuencia garantizada** del aumento de FTO. La dirección de ganancia de función sobre fenotipo senescente es precisamente lo que el proyecto se propone evaluar.

Tabla que anticipa, para cada medición, el resultado compatible con la hipótesis, el resultado alternativo y la interpretación de cada caso.

**Criterios de comparación entre brazos, mantenidos separados.** El éxito de activación y la selectividad no se colapsan en una sola métrica.

1. Magnitud de activación de *FTO*.
2. Magnitud del cambio en *RPGRIP1L*.
3. Diferencia o relación normalizada entre ambos efectos.
4. Efecto sobre el eje m6A–*FOS*.
5. Efecto sobre senescencia.

La métrica matemática concreta del punto 3 se definirá más adelante, preferentemente sobre cambios expresados en escala logarítmica. No se fija en esta versión del esqueleto.

No se presentan datos de actividad ni de off-targets, que no fueron calculados.

### 3.11 Discusión, alcance y limitaciones (0,7 carillas, criterio 4)

Sección que el evaluador buscará como Discusión. Interpreta el diseño en el contexto del objetivo y lo vincula con la literatura.

1. La propuesta es una reversión parcial de una alteración epigenética, no un rejuvenecimiento ovárico.
2. FTO actúa sobre numerosos transcritos, de modo que la activación debe titularse dentro de rango fisiológico y verificarse por transcriptoma.
3. La selección de región blanco se apoya en anotación multitejido y no en evidencia de actividad en granulosa. Es la limitación central y se enuncia sin atenuantes.
4. Compartir el promotor divergente implica un riesgo alto de coactivación de *RPGRIP1L*, pero no demuestra que ambos genes vayan a responder de igual modo ni en la misma dirección.
5. La ausencia de sitios CTCF anotados describe el estado del Regulatory Build y no demuestra ausencia funcional de aislamiento.
6. No se conoce cuál sitio de inicio de *FTO* se utiliza en granulosa, motivo por el cual todas las distancias se informan contra cuatro puntos de referencia.
7. La literatura disponible sostiene con solidez la dirección de pérdida de función del eje, pero no demuestra que el aumento de FTO revierta el fenotipo senescente en granulosa. Esa ausencia no invalida el diseño: **el proyecto evalúa una dirección causal que la literatura disponible todavía no probó completamente, si la activación dirigida de FTO endógeno puede atenuar el fenotipo senescente en células de la granulosa**. Enunciarlo así es lo que define con precisión el aporte del trabajo.

### 3.12 Conclusiones (0,3 carillas, criterio 4)

Cierre breve que recoge qué queda establecido por el diseño, qué queda como hipótesis a contrastar y qué decisión experimental resuelve cada brazo del panel.

---

## A.4 Anexos

| Anexo | Contenido |
| :--- | :--- |
| A1 | Secuencia anotada de las cuatro ventanas con sitios de inicio, elementos regulatorios, candidatas y PAM marcados |
| A2 | Tabla completa de candidatas con las cuatro distancias, elementos superpuestos, variantes y, cuando estén disponibles, puntajes de actividad y off-targets |
| A3 | Oligos duplex de cada guía en el formato del protocolo 1 |
| A4 | Mapa y secuencia anotada del constructo |
| A5 | Mapa y secuencia anotada del vector de guía |
| A6 | Tabla de primers |
| A7 | Archivos exportados de Benchling en formato GenBank |

---

## A.5 Bibliografía

Formato autor-año consistente, sin mezclar con sistema numérico. Ninguna afirmación se traslada sin contrastarla contra su pasaje literal.

---

## A.6 Presupuesto de extensión

| Sección | Carillas |
| :--- | :--- |
| 1. Introducción | 2,50 |
| 2. Objetivo | 0,25 |
| 3. Diseño Experimental | 7,00 |
| Total sin anexos ni bibliografía | **9,75** |

**No se recorta todavía.** Un presupuesto estimado en el entorno de 10 a 10,5 carillas sigue siendo compatible con la indicación de "alrededor de 10". La decisión de recortar se toma cuando exista texto redactado y pueda evaluarse qué contenido resulta redundante, no sobre el esqueleto. Las subsecciones que a priori tolerarían compresión son 3.7 y 3.10, pero no se marcan como recorte comprometido.

---

# PARTE B. Andamiaje de trabajo, no se traslada al entregable

## B.1 Criterio unificado de lenguaje

| Entidad | Nombre a usar | Identificador o coordenada |
| :--- | :--- | :--- |
| Transcrito de referencia de *FTO* | transcrito de referencia de *FTO* | FTO-206, ENST00000471389.6 |
| Sitio de inicio del transcrito de referencia de *FTO* | TSS de referencia de *FTO* | chr16:53.704.156 |
| Cluster alternativo de inicio de *FTO* | inicio alternativo de *FTO* | cluster en chr16:53.703.963 |
| Transcrito de referencia de *RPGRIP1L* | transcrito de referencia de *RPGRIP1L* | RPGRIP1L-212, ENST00000647211.2 |
| Sitio de inicio del transcrito de referencia de *RPGRIP1L* | TSS de referencia de *RPGRIP1L* | chr16:53.703.859 |
| Cluster alternativo de inicio de *RPGRIP1L* | inicio alternativo de *RPGRIP1L* | cluster en chr16:53.703.938 |
| Bloque regulatorio compartido | promotor divergente FTO–RPGRIP1L | ENSR16_9RBJC, chr16:53.703.831-53.704.167 |
| Región del intrón 1 con firma de elemento regulador | región intrónica candidata a enhancer | región W3, pELS EH38E1816377 |

**Nota sobre la elección de términos.** No se usan los calificativos "principal" ni "secundario" para los sitios de inicio. La selección de un transcrito de referencia normaliza las coordenadas, pero no establece una jerarquía biológica de uso en granulosa, y esos dos calificativos serían demasiado fuertes para lo que la evidencia permite afirmar.

**Nota sobre W3.** Ensembl la incluye dentro de un elemento clasificado como enhancer, ENSR16_BDMQQ, y ENCODE la clasifica como pELS, EH38E1816377. Ninguna de esas anotaciones demuestra que la región regule *FTO* en granulosa. Por eso el término principal es **región intrónica candidata a enhancer**, y cuando haga falta abreviar, **región intrónica con firma pELS**. La pregunta experimental sigue siendo si la acetilación de esa región aumenta *FTO*.

Para cada guía se informan siempre las cuatro distancias. Ninguna coordenada se presenta como "el TSS real" de *FTO*.

### Nombres y función de las cuatro ventanas

| Ventana | Nombre | Ubicación | Función |
| :--- | :--- | :--- | :--- |
| W1 | centro del promotor divergente | prácticamente entre los inicios alternativos de ambos genes | comparador de activación del bloque compartido |
| W2 | primer exón codificante de *FTO* | exón 1 del transcrito de referencia | región problemática, retirada |
| W3 | región intrónica candidata a enhancer | intrón 1, aproximadamente +426 y +466, pELS EH38E1816377 | brazo de activación de una región intrónica con firma de elemento regulador |
| W4 | región promotora próxima al TSS de referencia de *FTO* | aproximadamente −42 y −71; también 5′ UTR de isoformas del inicio alternativo | brazo de activación promotora orientado al transcrito de referencia |

## B.2 Método canónico del curso

| Fuente | Qué establece | Uso |
| :--- | :--- | :--- |
| Ejercicio 1 (FOXO4) | Región genómica y transcritos, elección del locus | Ensembl para el locus y los sitios de inicio |
| Ejercicio 5 (Reg1) | CRISPOR, off-targets, eficiencia, secuencia semilla | CRISPOR para el panel, con el cambio de criterio de B.3 |
| Ejercicio 16 | Identificadores Ensembl | Se citan los identificadores de gen y transcrito |
| Cartilla teórica §3 | SpCas9, PAM NGG, dominios RuvC y HNH | Justifica dCas9 como la misma plataforma sin corte |
| Cartilla teórica §4 | Golden Gate, enzimas Tipo IIS | Clonado de los oligos de guía |
| Protocolo 1 | Oligos con extremos CACCG y AAAC, T4 PNK, ligación | Diseño de los oligos duplex |
| Cartilla teórica §5 | Genotipado por heterodúplex y secuenciación | No aplica: sin corte no hay indel que genotipar |

## B.3 Qué cambia al pasar de diseño para knockout a diseño para CRISPRa

1. El blanco deja de ser un exón temprano y pasa a ser una región regulatoria, que en este locus no es única.
2. Los puntajes de eficiencia de corte pierden significado biológico; se reportan declarando que no son el criterio de selección.
3. El off-target pasa de rotura de doble cadena a unión sin corte con posible deposición de acetilación en una región no buscada.
4. La secuencia semilla sigue siendo el determinante de especificidad de la unión.
5. El multiplexado pasa a servir para sumar efectores sobre regiones regulatorias.
6. No hay genotipado de edición; la verificación es inmunoprecipitación de cromatina y expresión.
7. Se agrega un requisito que el diseño de knockout no tiene: por tratarse de un promotor divergente, toda lectura incluye el gen vecino.

## B.4 Estado de la evidencia

La clasificación no dice "sólido" sin especificar la dirección.

**Evidencia sólida en modelos celulares.** La pérdida de FTO favorece la estabilización de *FOS* dependiente de m6A y contribuye a un fenotipo senescente. El silenciamiento de *FOS* produce un rescate parcial del efecto de la pérdida de FTO. Ambos en COV434 y KGN, con senescencia inducida por peróxido de hidrógeno a 50 µM.

**Evidencia clínica asociativa.** FTO se encuentra reducido en muestras humanas de células de la granulosa vinculadas al envejecimiento ovárico. Los tamaños muestrales no deben fusionarse en una misma frase: la medición de m6A total por colorimetría se hizo sobre **seis pares** de ovarios envejecidos y control, mientras que la cuantificación por RT-PCR empleó **n = 15 para FTO** y n = 10 para los demás genes.

**Evidencia limitada de ganancia de función.** La sobreexpresión de FTO disminuyó *FOS* en las líneas evaluadas, según la figura suplementaria S3.

**No demostrado.** Que aumentar FTO revierta la senescencia o restaure la homeostasis en granulosa. Qué sitio de inicio de *FTO* se utiliza en el modelo. Si W3 funciona como enhancer de *FTO* en ese tipo celular. Si el promotor está accesible o pierde H3K27ac durante el envejecimiento. La actividad y la especificidad de las guías concretas. Los off-targets. Las frecuencias poblacionales de todas las variantes. La selectividad real entre *FTO* y *RPGRIP1L*.

**Sólido, independiente del eje biológico.** Que dCas9-p300 puede depositar H3K27ac y activar desde promotores y desde enhancers. Que existen antecedentes de edición epigenómica en granulosa, aunque no sobre este locus humano. La arquitectura divergente, las coordenadas, las secuencias, los PAM y las anotaciones. La existencia de candidatas de W4 próximas al TSS de referencia. La localización intrónica y la clasificación como pELS de W3. La localización exónica y problemática de W2.

**Regla de atribución.** Antes de asignar a otra fuente la demostración de reversión por ganancia de función, debe verificarse que incluya aumento o restauración de FTO, granulosa o modelo claramente comparable, medición de marcadores de senescencia, comparación experimental adecuada y evidencia causal de rescate. Ganancia de función en otro tejido, o sola disminución de *FOS*, se clasifica como apoyo de plausibilidad. No se reemplaza una cita incorrecta por evidencia indirecta.

## B.5 Auditoría de Jiang et al. (2021): completada el 2026-07-26

Detalle en `FTO_anexo_tecnico/11_auditoria_jiang_2021.md`. La marca de "pendiente de auditoría textual final" se retira de las afirmaciones verificadas y se conserva únicamente para la reversión de senescencia por ganancia de función de FTO, mientras no se identifique la fuente que efectivamente la sostiene.

**Verificado y elevado a sólido**: descenso de FTO y aumento de m6A en granulosa de ovarios envejecidos, sobre seis pares de muestras clínicas humanas, de naturaleza correlativa; eje FTO–m6A–FOS con encadenamiento causal completo en la dirección de pérdida de función, incluidos MeRIP-seq, MeRIP-qPCR, actinomicina D, minigenes con 3′ UTR silvestre y mutado, y el lector IGF2BP2; y *FOS* como efector, cuyo silenciamiento alivia **parcialmente** el fenotipo.

**Precisiones que deben trasladarse al entregable**: el estudio es exclusivamente humano y exclusivamente in vitro o ex vivo, sin modelo animal ni experimentos in vivo; las líneas son COV434 y KGN; la senescencia no es espontánea sino **inducida con peróxido de hidrógeno 50 µM**; y los marcadores empleados son γH2A.X y β-galactosidasa, sin p16 ni p21.

**No sostenido por esta fuente**: que aumentar FTO revierta el fenotipo senescente. Lo único reportado sobre ganancia de función es que la sobreexpresión de FTO reduce *FOS*, en figura suplementaria S3.

## B.6 Inventario de figuras y tablas

| Id | Contenido | Subsección | Estado |
| :--- | :--- | :--- | :--- |
| F1 | Eje FTO–m6A–FOS | 1 | Pendiente |
| F2 | Mapa del locus | 3.3 | Pendiente |
| F3 | Ventanas y candidatas | 3.4 | Pendiente |
| F4 | Constructo y vector | 3.6 | Pendiente |
| F5 | Amplicones de inmunoprecipitación | 3.9 | Pendiente |
| T1 | Efectores evaluados | 3.1 | Derivable |
| T2 | Bases de datos y metodología | 3.2 | Derivable |
| T3 | Candidatas con las cuatro distancias | 3.5 | Parcial |
| T4 | Panel de brazos y controles | 3.8 | Definido |
| T5 | Primers | 3.9 | Pendiente |
| T6 | Resultados esperados | 3.10 | Pendiente |

## B.7 Correspondencia con la presentación oral

La elección de la estrategia se responde con 3.1 y 3.4; los programas utilizados, con 3.2; la determinación de eficiencias, con 3.5 y la aclaración de que los puntajes de corte no son el criterio; los resultados descartados, con la retirada de W2, las candidatas excluidas por corrida de timidinas y los efectores descartados de T1.
