# Guion + diseño de slides: Edición epigenética por CRISPR/dCas9

## Índice operativo

Modalidad 1 (Presentación de técnicas, 15 pts). Fecha: martes 21/07. Formato: grupo de 3, 20 minutos.
Paper base (caso central): Xiao B, Yin S, Hu Y, et al. (2019). Epigenetic editing by CRISPR/dCas9 in *Plasmodium falciparum*. *PNAS* 116(1):255-260, más su apéndice.

Qué contiene: por cada slide, primero el contenido de la diapositiva (diseño estético y funcional, listo para armar el pptx) y debajo el guion oral verbatim. Registro de seminario técnico. Datos trazables al paper y su apéndice.

Nota marcada (slide 8): el paper rotula la vía de invasión de *rh4* como "sialic acid-dependent" en un encabezado, en contradicción con su abstract y con el mecanismo (neuraminidasa); se expone la versión correcta, independiente de ácido siálico.

---

## Sistema de diseño (aplica a todos los slides)

1. Formato 16:9, plantilla uniforme en los 14 slides.
2. Paleta: fondo oscuro (gris carbón o azul noche), texto claro y dos colores de acento coherentes con la Figura 1 del paper, verde para activación (GCN5, ON) y rojo para represión (Sir2a, OFF).
3. Tipografía sans-serif (Inter, Calibri o similar); títulos grandes, cuerpo mínimo.
4. Regla de contenido: poco texto en pantalla, una figura por slide como protagonista; el peso de la explicación lo lleva el orador con este guion.
5. Pie de página constante: "Xiao et al., 2019, PNAS 116(1):255-260" y número de slide.
6. Recorte de figuras del PDF original a resolución de impresión, con los paneles relevantes ampliados y rótulos legibles a distancia.

---

## Slide 1. Portada

Contenido del slide:
1. Título grande centrado: "Edición epigenética con CRISPR/dCas9". Subtítulo: "Reprimir y activar genes sin cortar el ADN. *Plasmodium falciparum* como caso (Xiao et al., 2019)".
2. Elemento visual: esquema minimalista de dCas9 con un sgRNA y una histona acetilada, en los dos colores de acento.
3. Pie: integrantes del grupo, materia y fecha.
4. Diseño: fondo oscuro pleno, sin sobrecarga; una sola imagen conceptual.

Guion: La edición epigenética mediante CRISPR/dCas9 es una estrategia que reprime o activa genes sin introducir cortes en el ADN. El caso de referencia es el trabajo de Xiao y colaboradores, publicado en PNAS en 2019, que implementa la técnica en *Plasmodium falciparum*, agente de la forma más grave de malaria. El principio es la reprogramación de la transcripción mediante la modificación de la cromatina en el entorno del gen, y no de su secuencia.

---

## Slide 2. El problema: editar el genoma de *P. falciparum*

Contenido del slide:
1. Título: "El problema: un genoma difícil de editar".
2. Tres íconos con etiqueta corta, en fila: recombinación homóloga baja, sin RNAi, genoma haploide.
3. Dato de impacto arriba a la derecha, en grande: "≈ 500.000 muertes/año".
4. Diseño: los tres obstáculos como la idea central; nada de párrafos en pantalla.

Guion: *Plasmodium falciparum* causa la forma más grave de malaria, con cerca de medio millón de muertes anuales, lo que sostiene el interés en su biología. Su manipulación genética enfrenta tres limitaciones. La eficiencia de recombinación homóloga es baja, lo que dificulta introducir cambios dirigidos. Carece de la maquinaria de RNA de interferencia, de modo que la vía habitual de silenciamiento reversible no está disponible. Y su genoma es haploide, por lo que la disrupción de un gen esencial resulta letal e impide estudiar su función. El CRISPR/Cas9 convencional ya se aplicó al parásito para disrupción génica, marcado y reemplazo alélico, pero mantiene limitaciones frente a dos categorías, los genes esenciales y los ARN no codificantes situados en exones o intrones. El trabajo cubre esa carencia con un sistema que regula la expresión sin romper el ADN y de manera reversible.

---

## Slide 3. Marco: acetilación de histonas y transcripción

Contenido del slide:
1. Título: "La marca: acetilación de H3 en el TSS".
2. Esquema: nucleosoma con colas de histona; una lisina acetilada con "gen ON" y una desacetilada con "gen OFF".
3. Dos cajas enfrentadas: PfGCN5 (HAT, escribe, verde) y PfSir2a (HDAC dependiente de NAD, borra, rojo).
4. Diseño: eje central escribir/borrar; los colores de acento anticipan las dos herramientas.

Guion: El fundamento es la regulación de la transcripción por modificaciones de histonas. El ADN se organiza sobre histonas, y las marcas químicas depositadas en la región del sitio de inicio de la transcripción, el TSS, determinan el nivel de expresión del gen. La marca relevante es la acetilación de las lisinas 9 y 14 de la histona H3: su presencia relaja la cromatina y favorece la transcripción, mientras que su remoción la compacta y reprime el gen. Los efectores empleados son enzimas endógenas del parásito. La activación recae en PfGCN5, una acetiltransferasa que deposita la marca; la represión, en PfSir2a, una deacetilasa dependiente de NAD que la elimina de varias lisinas de las histonas H3 y H4.

---

## Slide 4. El salto conceptual: de cortar a reclutar

Contenido del slide:
1. Título: "De nucleasa a sistema de direccionamiento: el dCas9".
2. Esquema del complejo Cas9-sgRNA sobre el ADN, con el PAM (NGG) marcado junto al sitio blanco y los dos dominios catalíticos etiquetados: RuvC (corta la cadena no apareada) y HNH (corta la cadena apareada con el sgRNA).
3. Comparación lado a lado: izquierda, Cas9 silvestre con los dos dominios activos (doble corte, "cambio permanente"); derecha, dCas9 con D10A sobre RuvC y H840A sobre HNH, los dos dominios tachados (sin corte, "reprograma, reversible"), y el efector fusionado al final.
4. Diseño: mismo esquema base a ambos lados para que se vea que solo cambian los dos dominios catalíticos; el PAM y la región de apareamiento con el sgRNA se dibujan igual en las dos versiones, remarcando que el reconocimiento no cambia.

Guion: Conviene detenerse en el mecanismo del Cas9 antes de ver cómo se lo desactiva, porque de ahí sale toda la lógica del sistema. El Cas9 de tipo silvestre reconoce su blanco mediante dos elementos combinados: el sgRNA, una secuencia de unas veinte bases que aparea por complementariedad con una de las dos cadenas de ADN, y el PAM, una secuencia corta, NGG en este sistema, ubicada justo al lado del sitio blanco. El PAM no forma parte de la guía de ARN; lo reconoce directamente la proteína Cas9, y esa lectura es la que habilita que el ADN se abra localmente y se pruebe el apareamiento con el sgRNA. Sin un PAM contiguo, Cas9 no reconoce esa posición, por más que la secuencia coincida con la guía. Una vez que la unión se confirma, entran en juego dos dominios catalíticos distintos: RuvC, que corta la cadena de ADN no apareada con el sgRNA, y HNH, que corta la cadena apareada. Los dos cortes juntos producen la ruptura de doble cadena que después se repara y deja el cambio permanente de secuencia.

Las mutaciones D10A y H840A apagan, cada una, uno de esos dos dominios: D10A inactiva RuvC, H840A inactiva HNH. Con las dos mutaciones combinadas, ninguna cadena se corta, y el resultado es un Cas9 completamente muerto como nucleasa. El punto central es que ambas mutaciones caen dentro de los dominios catalíticos y no tocan las regiones que reconocen el PAM ni las que sostienen el apareamiento con el sgRNA: la maquinaria de reconocimiento y direccionamiento queda intacta, solo se pierde la capacidad de cortar. Por eso el dCas9 sigue viajando exactamente a la misma dirección genómica que un Cas9 activo, guiado por la misma combinación de sgRNA y PAM, pero sin dejar ninguna ruptura a su paso. Al fusionarle una enzima epigenética en el extremo, ese mecanismo de direccionamiento intacto se reutiliza para llevar la actividad de acetilar o desacetilar hasta el TSS del gen elegido, en lugar de llevar unas tijeras. La secuencia permanece intacta y el efecto es reversible. Es el mismo principio de CRISPR de interferencia y de activación, con efectores de acetilación en lugar de los dominios represores habituales.

---

## Slide 5. Diseño de las dos herramientas (Fig. 1 A y B)

Contenido del slide:
1. Título: "Una sola arquitectura, dos funciones".
2. Figura: recorte de Fig. 1 A y B (los dos esquemas de la proteína recombinante).
3. Barra de dominios simplificada superpuesta o al pie: Hsp86 - 3xFLAG - NLS - dCas9 - NLS - linker GS3 - efector, con el efector resaltado (GCN5 verde / Sir2a rojo).
4. Diseño: destacar que solo cambia el bloque final; el resto es idéntico.

Guion: La proteína recombinante tiene una arquitectura común a las dos versiones. De extremo a extremo incluye el promotor Hsp86, un epitope 3xFLAG en el extremo amino para su detección, una señal de localización nuclear, el dCas9 con las dos mutaciones, una segunda señal de localización, un conector flexible de glicina y serina, y el dominio efector en el extremo carboxilo. La única diferencia entre activación y represión es ese dominio terminal: PfGCN5 para depositar acetilación, PfSir2a para removerla. Las dos señales de localización dirigen la proteína al núcleo; el conector flexible otorga una conformación extendida que permite al efector alcanzar las histonas sin impedimento del dCas9. La expresión es episomal, desde un plásmido, sin integración en el genoma.

---

## Slide 6. Validación: expresión y localización nuclear (Fig. 1 C-F)

Contenido del slide:
1. Título: "Expresión y localización nuclear".
2. Figura: recorte de Fig. 1 C-D (Western blot) y E-F (inmunofluorescencia con solapamiento FLAG/DAPI).
3. Dos etiquetas guía: "se expresa (WB)" y "colocaliza con el núcleo (IFA)".
4. Diseño: dividir el slide en dos mitades, expresión a la izquierda, localización a la derecha.

Guion: El primer requisito es confirmar que la proteína se expresa y alcanza el núcleo. Los ensayos de Western blot con anticuerpo anti-Cas9 muestran las dos construcciones al tamaño esperado, con actina como control de carga. La inmunofluorescencia con anti-FLAG localiza la proteína, y su señal coincide con la tinción de DAPI, lo que confirma el enriquecimiento nuclear de ambas versiones. Una línea con dCas9 fusionado a GFP, sin actividad epigenética, funciona como control negativo en los ensayos posteriores. Verificadas la expresión y la localización, corresponde evaluar el efecto sobre la transcripción.

---

## Slide 7. Activación de *rh4*: unión y marca (Fig. 2 A-C)

Contenido del slide:
1. Título: "Activación de *rh4*: ocupancia y acetilación".
2. Figura: recorte de Fig. 2 A (mapa del gen con el sgRNA cerca del TSS), B (ChIP anti-FLAG) y C (ChIP anti-acetil-H3).
3. Secuencia lógica visible como tres pasos, con los dos primeros resaltados: unión, marca, transcripción (este último pendiente).
4. Diseño: la barra "unión, marca, transcripción" se reutiliza en los slides 7 a 9 para dar continuidad.

Guion: El primer ensayo funcional es de activación, sobre el gen *rh4*, que participa en una de las vías de invasión del eritrocito y se encuentra silenciado en la cepa Dd2. Ese estado silenciado permite medir la activación sobre un nivel basal bajo. El diseño evalúa tres condiciones sucesivas: unión del dCas9 al blanco, depósito de la marca y cambio transcripcional. La inmunoprecipitación de cromatina con anti-FLAG, con doce juegos de primers que recorren el locus, muestra ocupancia alta y específica de dCas9-GCN5 en la región de *rh4*. La inmunoprecipitación con anti-acetil-H3 confirma la hiperacetilación de H3 en el mismo locus, coherente con la actividad de la acetiltransferasa. Verificadas la unión y la marca, resta el efecto sobre la transcripción.

---

## Slide 8. Activación de *rh4*: transcripción y fenotipo (Fig. 2 D-E)

Contenido del slide:
1. Título: "Activación de *rh4*: 113× y cambio de invasión".
2. Figura: recorte de Fig. 2 D (RT-qPCR) y E (invasión).
3. Dato ancla en grande: "*rh4* ≥ 113×"; nota lateral "*ama1* sin cambios (control)".
4. Diseño: la barra de pasos ahora con los tres completos. Rotular la vía como independiente de ácido siálico.

Guion: La RT-qPCR, normalizada al gen constitutivo seril-tRNA sintetasa, muestra que *rh4* alcanza al menos 113 veces más transcripción en la línea editada que en la silvestre, mientras que *ama1*, gen del mismo estadio usado como control, no varía, lo que indica especificidad. El efecto se traslada al fenotipo: la línea editada invade eritrocitos tratados con neuraminidasa, capacidad ausente en la cepa silvestre. Su tasa de invasión sobre esas células desializadas se aproxima a la registrada sobre eritrocitos sin tratar, mientras que la silvestre permanece en valores bajos. La neuraminidasa elimina el ácido siálico de la superficie, de modo que esa invasión corresponde a la vía independiente de ácido siálico, consistente con la función de PfRH4. El encabezado del artículo la denomina dependiente, en contradicción con su propio resumen y con el mecanismo; se expone en su versión correcta. La comparación con VPR, un activador eucariota estándar, indica que la enzima endógena GCN5 es más potente en este organismo.

---

## Slide 9. Represión de *eba-175* (Fig. 3)

Contenido del slide:
1. Título: "Represión de *eba-175* con dCas9-Sir2a".
2. Figura: recorte de Fig. 3 completa (A mapa, B ChIP-FLAG, C hipoacetilación, D RT-qPCR, E invasión).
3. Barra de pasos en rojo (represión); dato ancla "*eba-175* baja, invasión por quimotripsina reducida".
4. Diseño: reflejar el slide 7-8 pero en el color de represión, para que se lea como ensayo inverso.

Guion: El ensayo complementario evalúa la represión sobre *eba-175*, uno de los genes de invasión más expresados en la cepa 3D7, cuyo producto se une a glicoforina A y media la vía dependiente de ácido siálico. Su expresión elevada lo hace adecuado para medir represión. El sitio de inicio de la transcripción se determinó por 5'-RACE, y sobre ese dato se diseñó el sgRNA que dirige dCas9-Sir2a al TSS. Los resultados reproducen la secuencia anterior en sentido inverso: la inmunoprecipitación con anti-FLAG confirma la ocupancia del dCas9; la de acetil-H3, la hipoacetilación del locus a lo largo de siete juegos de primers; y la RT-qPCR, una caída marcada de *eba-175*, sin cambios en *ama1* ni en el control con GFP. En el fenotipo, la represión reduce la invasión de eritrocitos tratados con quimotripsina, dependiente de esa proteína, a menos de la mitad del valor de la cepa silvestre. Los dos ensayos establecen la regulación en ambas direcciones.

---

## Slide 10. Lección de diseño: la posición del sgRNA importa (Fig. S4)

Contenido del slide:
1. Título: "Criterio de diseño: el sgRNA, cerca del TSS".
2. Figura: recorte de Fig. S4 (EBA175sgRNA2 lejos del TSS: une y marca, pero no reprime bien).
3. Contraste de dos casos: sgRNA cerca del TSS, represión eficaz; sgRNA lejos, une pero no regula.
4. Diseño: diapositiva de conclusión operativa, con la regla enunciada en una línea grande.

Guion: Un segundo sgRNA para *eba-175*, situado a más de mil doscientas bases corriente arriba del TSS, permite evaluar el efecto de la posición. Ese guía recluta el dCas9 y modifica la acetilación en la región, de modo que la unión se produce; no obstante, no reprime el gen con la eficiencia del guía dirigido al TSS. La conclusión operativa es que la unión del dCas9 no basta: el efector debe depositar o remover la marca donde tiene consecuencia transcripcional, es decir, en el entorno inmediato del sitio de inicio. El mismo comportamiento se observó para *rh4*. En el diseño de estos sistemas, el sitio guía debe ubicarse lo más cerca posible del TSS del gen blanco.

---

## Slide 11. Alcance a genes esenciales: *PfSET1* (Fig. 4)

Contenido del slide:
1. Título: "Genes esenciales inaccesibles por knockout: *PfSET1*".
2. Figura: recorte de Fig. 4 A (RT-qPCR), B (distribución de fenotipos: 50% esencial, 31% dispensable, 19% lento) y D (citometría, retraso de crecimiento).
3. Datos ancla: "322 genes a la baja", "retraso desde trofozoíto".
4. Diseño: la torta y la citometría como protagonistas; el mapa de calor (panel C) opcional si hay espacio.

Guion: El sistema se aplica luego a un gen esencial, *PfSET1*, una histona metiltransferasa necesaria para el estadio asexual y de función poco caracterizada, inaccesible por knockout dado que su disrupción es letal. La represión reversible con dCas9-Sir2a evita esa limitación. El análisis por RNA-seq identifica 322 genes regulados a la baja; de sus ortólogos en *Plasmodium berghei*, la mitad son esenciales, un 31 por ciento dispensables y un 19 por ciento asociados a crecimiento lento. De los 68 genes esenciales, el 72 por ciento se expresa en trofozoíto y esquizonte, según el perfil de expresión en ocho puntos del ciclo eritrocítico. En concordancia, la citometría de flujo registra un retraso del crecimiento que comienza en el estadio de trofozoíto y no aparece en los controles. El resultado vincula la represión con un fenotipo definido y demuestra la aplicabilidad de la técnica a genes esenciales.

---

## Slide 12. Especificidad y targetabilidad genómica (Fig. S5 y S8)

Contenido del slide:
1. Título: "Especificidad y cobertura genómica".
2. Figura: recorte de Fig. S5 (scatter de transcriptoma, off-target bajo) y Fig. S8 (densidad de PAM).
3. Datos ancla: "pocos off-target", "*pebl* co-activado (promotor bidireccional)", "261.196 NGG + 727.817 NGA, cobertura >173×".
4. Diseño: dos mitades, especificidad a la izquierda, cobertura genómica a la derecha.

Guion: La especificidad y el alcance se evalúan a escala genómica. La comparación de los transcriptomas completos por RNA-seq muestra pocos cambios fuera del blanco, con un único off-target candidato relevante, el gen stevor. La excepción esperable es *pebl*, un pseudogen que se activa junto con *rh4* por compartir un promotor bidireccional; el dato fija un límite, la co-regulación de genes con promotor compartido, y a la vez indica que la técnica alcanza elementos no codificantes. El rastreo del genoma identifica, para el PAM ya descrito, más de 261 mil sitios del tipo NGG y más de 727 mil del tipo NGA en las regiones promotoras, con una cobertura superior a 173 veces sobre los cerca de 5.712 genes del parásito. Prácticamente cualquier gen es blanco posible, y la restricción efectiva no es la disponibilidad de sitio sino su proximidad al TSS.

---

## Slide 13. Ventajas, límites y lugar entre las técnicas

Contenido del slide:
1. Título: "Balance y ubicación".
2. Dos columnas: Ventajas (reversible, sin corte, genes esenciales y no codificantes, activar y reprimir) y Límites (posición del sgRNA, promotores bidireccionales, expresión episomal variable).
3. Franja inferior de contexto: KO por Cas9 y edición de base/prime (cambian secuencia) frente a CRISPRi/CRISPRa y este trabajo (no cambian secuencia).
4. Diseño: única excepción a la regla de "poco texto", por ser slide de síntesis; frases cortas, no párrafos.

Guion: Las ventajas de la técnica son la reversibilidad, la ausencia de corte de doble cadena, el acceso a genes esenciales y a ARN no codificantes, y la regulación en las dos direcciones con efectores endógenos. Sus limitaciones son la dependencia de la posición del sgRNA respecto del TSS, la co-regulación de promotores bidireccionales y la variabilidad de expresión propia de un sistema episomal. En el panorama de edición, comparte el principio de CRISPR de interferencia y de activación, basados en dCas9 con un efector, y se distingue del knockout por Cas9 y de la edición de base o de prime, que modifican la secuencia. Su aporte específico es demostrar que efectores de acetilación endógenos cumplen esa función en un organismo sin edición epigenética previa. Como proyección, los autores plantean el multiplexado con sistemas tipo Cpf1 para actuar sobre familias multigénicas.

---

## Slide 14. Conclusiones

Contenido del slide:
1. Título: "Conclusiones".
2. Tres líneas cortas: activar/reprimir sin editar la secuencia; control de invasión (*rh4*, *eba-175*) y acceso a un esencial (*PfSET1*); cobertura genómica casi total.
3. Cierre visual: repetir el esquema de portada para cerrar el arco.
4. Pie con la referencia completa del paper.

Guion: La fusión de una acetiltransferasa o una deacetilasa a un dCas9 permite activar o reprimir genes en *Plasmodium falciparum* de forma específica y sin modificar la secuencia. El trabajo lo demuestra sobre dos vías de invasión, con *rh4* y *eba-175*, con lectura molecular y fenotípica, y sobre un gen esencial, *PfSET1*, mediante represión reversible. El sistema amplía las herramientas de genética funcional y epigenética del parásito, con una cobertura genómica prácticamente completa.

---

## Referencia

Xiao B, Yin S, Hu Y, Sun M, Wei J, Huang Z, Wen Y, Dai X, Chen H, Mu J, Cui L, Jiang L (2019). Epigenetic editing by CRISPR/dCas9 in *Plasmodium falciparum*. *PNAS* 116(1):255-260.
