# Preguntas que requieren datos específicos de granulosa o KGN

Ninguna de estas preguntas puede responderse con anotación genómica de referencia. Todas requieren datos del tipo celular. Se listan con el dato mínimo que las resolvería y con la consecuencia que tiene sobre el diseño no responderlas.

---

## P1. Cuál sitio de inicio de *FTO* se usa efectivamente en granulosa

La anotación registra 22 transcritos que inician en 53.703.963 y 4 en el TSS MANE 53.704.156. El número de isoformas anotadas no informa uso real.

**Dato que la resuelve**: CAGE, RAMPAGE, RNA-seq con captura de extremo 5′ o secuenciación de lectura larga en KGN, COV434 o granulosa primaria humana.

**Consecuencia de no responderla**: las distancias de cada guía al sitio de inicio funcionalmente relevante quedan indeterminadas, y la elección entre dirigir el promotor divergente o la región corriente abajo pierde una de sus bases.

---

## P2. Si el promotor divergente está activo en granulosa y con qué firma

El elemento ENSR16_9RBJC y el cCRE EH38E1816376 provienen de conjuntos multitejido. Una firma de promotor en el agregado no implica actividad en granulosa.

**Dato que la resuelve**: ATAC-seq o DNasa para accesibilidad, y ChIP-seq de H3K27ac y H3K4me3 en el tipo celular.

**Consecuencia de no responderla**: no se puede anticipar si el efector encuentra cromatina accesible, que es el factor identificado como determinante de la magnitud de activación.

---

## P3. Nivel de expresión basal de *FTO* y de *RPGRIP1L* en el modelo

El rendimiento de la activación epigenética depende del nivel basal: los genes con expresión baja o silenciados responden mucho más que los ya activos.

**Dato que la resuelve**: RT-qPCR o RNA-seq de ambos genes en KGN joven y en KGN bajo estrés oxidativo, y en granulosa primaria estratificada por edad.

**Consecuencia de no responderla**: no se puede estimar el techo de activación alcanzable ni interpretar la magnitud relativa del efecto sobre el vecino.

---

## P4. Si *RPGRIP1L* es funcionalmente relevante en granulosa y qué implica modificarlo

Existe evidencia de cilios primarios en células de la granulosa de folículos antrales y de participación ciliar en esteroidogénesis y luteinización, pero no de la contribución específica de *RPGRIP1L* en ese tipo celular.

**Dato que la resuelve**: expresión de *RPGRIP1L* en granulosa, presencia de cilio primario en el modelo utilizado, y efecto de su modulación sobre marcadores esteroidogénicos.

**Consecuencia de no responderla**: un cambio en los desenlaces fenotípicos no puede atribuirse con seguridad a la reposición de *FTO*.

---

## P5. Si el eje CUX1 opera en granulosa

El mecanismo de las isoformas P110 y P200 sobre el elemento del primer intrón está descrito en contextos metabólico y neuronal.

**Dato que la resuelve**: expresión de *CUX1* y de sus isoformas en granulosa, y ocupancia sobre el elemento en ese tipo celular.

**Consecuencia de no responderla**: la hipótesis de pérdida de activación como causa del descenso basal de *FTO* sigue sin anclaje en el tejido de interés.

---

## P6. Estado de metilación del bloque promotor divergente en granulosa envejecida

No hay datos de metilación sobre este promotor en granulosa, ni jóvenes ni envejecidas.

**Dato que la resuelve**: secuenciación por bisulfito de la ventana 53.703.398-53.704.740, comparando granulosa joven contra envejecida o tratada con peróxido de hidrógeno.

**Consecuencia de no responderla**: la elección entre un escritor de acetilación y una estrategia combinada con desmetilación sigue apoyada en inferencia y no en dato.

---

## P7. Si existe arquitectura cromatínica que separe ambos promotores en granulosa

El Regulatory Build no registra CTCF en la ventana inter-TSS, pero eso describe la anotación agregada.

**Dato que la resuelve**: ChIP-seq de CTCF y datos de conformación de la cromatina, del tipo Hi-C o Capture-C, en granulosa.

**Consecuencia de no responderla**: no se puede anticipar si la deposición de acetilación se propaga hacia el promotor del vecino o queda contenida.

---

## P8. Cuál es el nivel de *FTO* que corresponde a granulosa joven

El criterio de éxito del diseño se definió como reponer un nivel fisiológico, no como maximizar la activación.

**Dato que la resuelve**: cuantificación de *FTO* en granulosa humana joven frente a envejecida, en el mismo ensayo y con la misma normalización que se usará en el experimento.

**Consecuencia de no responderla**: no existe umbral objetivo contra el cual comparar la activación obtenida, y la distinción entre rango fisiológico y suprafisiológico queda sin referencia.

---

## Resumen

| Pregunta | Tipo de dato | Bloquea |
| :--- | :--- | :--- |
| P1, sitio de inicio usado | CAGE, RAMPAGE o lectura larga | Cálculo de distancias funcionales |
| P2, actividad del promotor | ATAC-seq, ChIP-seq de marcas activas | Predicción de accesibilidad |
| P3, expresión basal | RT-qPCR o RNA-seq | Estimación del techo de activación |
| P4, relevancia de *RPGRIP1L* | Expresión y fenotipo ciliar | Atribución del efecto fenotípico |
| P5, eje CUX1 | Expresión y ocupancia | Anclaje del mecanismo basal |
| P6, metilación del bloque | Bisulfito | Elección del tipo de editor |
| P7, arquitectura cromatínica | CTCF y conformación | Predicción de propagación de la marca |
| P8, nivel de referencia joven | Cuantificación comparada | Definición del criterio de éxito |

Ninguna de estas preguntas invalida el diseño. Todas delimitan qué puede afirmarse por anticipado y qué debe medirse, y su enumeración explícita es el modo de declarar el alcance real del trabajo.
