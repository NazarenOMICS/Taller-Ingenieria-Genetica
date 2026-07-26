---
type: decisiones-diseno
status: current
date: 2026-07-25
source: "Ensembl GRCh38 (ENSG00000140718) + Hilton et al. 2015 + Liao et al. 2026 + Kachanov et al. 2025 + Stratigopoulos et al. 2016 (JCI) + búsqueda verificada 2026-07-25"
related:
  - "[[Notes/dcas9-fto-granulosa/ESQUELETO_OBLIGATORIO]]"
  - "[[Notes/dcas9-fto-granulosa/MAESTRO_OBLIGATORIO]]"
  - "[[Notes/dcas9-fto-granulosa/INFORME_GENERAL]]"
---

# Bitácora de decisiones de diseño (activación de FTO vía dCas9-p300)

Registro de las decisiones de diseño tomadas y de las consideraciones que las sostienen. Cada entrada lleva su estado de verificación. Este archivo existe para que las decisiones no queden solo en conversación, puesto que varias de ellas cambian la sección de Diseño Experimental del Obligatorio.

Convención de estado: **verificado** significa contrastado contra el texto de la fuente primaria; **de búsqueda** significa que proviene de resúmenes de resultados de búsqueda y todavía no se contrastó contra el texto completo; **pendiente** significa que falta el dato.

---

## D1. Transcripto de referencia y locus

**Decisión**: se toma ENST00000471389.6 (FTO-206) como transcripto de referencia.

**Fundamento**: está marcado simultáneamente MANE Select, Ensembl Canonical, GENCODE Primary, APPRIS P3 y TSL:1, con CCDS32448 y RefSeq NM_001080432.3, y codifica 505 aa. El doble marcado MANE más Canonical es el criterio más defendible frente a las 42 isoformas anotadas, de las cuales alrededor de 31 son protein_coding.

**Datos del locus**: *FTO* en GRCh38, cromosoma 16, chr16:53.701.692-54.158.512, hebra forward, 456.821 pb. Identificador de gen ENSG00000140718.

**Estado**: verificado contra el export de Ensembl del usuario (CSV de transcriptos y vista de región) y contra la API REST de Ensembl (consulta del 2026-07-26).

**TSS de referencia, verificado**: ENST00000471389 tiene start 53.704.156 y end 54.121.941 en hebra +1, ensamblado GRCh38. Ergo, **el TSS de referencia es chr16:53.704.156** y es el cero de toda la numeración relativa que se use en el trabajo.

**Advertencia**: el gen ENSG00000140718 comienza en 53.701.692, unos 2,5 kb antes que el transcripto MANE. Ese inicio corresponde a otra isoforma, de modo que usar la coordenada de inicio del gen como TSS habría corrido toda la numeración. Conviene declarar en el escrito que la referencia es el transcripto y no el gen.

---

## D2. Arquitectura bidireccional del locus, y su consecuencia

**Hecho**: *RPGRIP1L* se ubica **a menos de 100 pb corriente arriba y en orientación transcripcional opuesta a *FTO***, y es un componente estructural de la zona de transición del cilio primario.

**Estado**: verificado. Cita literal de Stratigopoulos et al. (2016), J Clin Invest: "retinitis pigmentosa GTPase regulator-interacting protein-1 like (RPGRIP1L), located <100 bp upstream and in opposite transcriptional orientation to FTO (Figure 1A), is a transition zone structural component of the primary cilium".

**Coordenadas verificadas por API REST de Ensembl (GRCh38, consulta del 2026-07-26)**

| Elemento | Coordenadas chr16 | Hebra | Posición relativa al TSS de FTO-206 |
| :--- | :--- | :--- | :--- |
| TSS de FTO-206 (ENST00000471389) | 53.704.156 | +1 | 0 |
| Gen RPGRIP1L (ENSG00000103494) | 53.598.153-53.703.938 | −1 | termina en −218 |
| TSS de RPGRIP1L canónico (ENST00000647211) | 53.703.859 | −1 | **−297** |
| Enhancer ENSR16_9RBJ8 | 53.703.398-53.703.830 | sin hebra | −758 a −326 |
| **Promoter ENSR16_9RBJC** | 53.703.831-53.704.167 | sin hebra | **−325 a +11** |
| Enhancer ENSR16_BDMQQ | 53.704.168-53.704.740 | sin hebra | **+12 a +584** |
| rs1421085 (sitio CUX1 potencial) | 53.767.042 | — | +62.886 |
| rs8050136 (sitio CUX1 documentado) | 53.782.363 | — | +78.207 |

**Distancia entre ambos TSS: 297 pb.**

**Consecuencia de diseño, ahora con base cuantitativa**: el Regulatory Build de Ensembl anota un único elemento de tipo promoter de 337 pb (53.703.831-53.704.167) que **contiene los dos TSS**, el de *RPGRIP1L* y el de *FTO*. Es una confirmación estructural independiente de que se trata de un promotor bidireccional compartido y no de dos promotores vecinos.

Más importante todavía, **no existe ninguna región corriente arriba del TSS de *FTO* que sea específica de *FTO***: a partir de −326 y hacia coordenadas menores ya se está dentro del cuerpo del gen *RPGRIP1L*, puesto que su TSS queda en −297 y su transcripción avanza en sentido opuesto. La ventana canónica de CRISPRa, por lo tanto, no solo es compartida sino que su extensión hacia posiciones más negativas empeora el problema en lugar de mejorarlo.

**El lado específico de *FTO* es el corriente abajo**, es decir, coordenadas crecientes a partir del TSS. Ahí se ubican el enhancer ENSR16_BDMQQ (+12 a +584) y, mucho más adentro del primer intrón, los sitios CUX1 de rs1421085 y rs8050136.

---

## D3. Abandono de la ventana canónica como criterio por defecto

**Decisión**: la posición de las guías no se define por proximidad al TSS sino por evidencia, mediante un tamizaje posicional.

**Fundamento en la literatura**, con tres piezas convergentes:

1. Hilton et al. (2015) titulan el trabajo "activates genes from promoters and enhancers" y sostienen en el resumen que, a diferencia de los activadores dCas9 previos, dCas9-p300 activa genes desde enhancers y con una sola guía. Usaron cuatro guías por promotor endógeno (IL1RN, MYOD, OCT4) y también dirigieron el enhancer HS2 del locus de globina, que es distal. **Estado**: verificado contra el texto completo del PDF.
2. Liao et al. (2026), el precedente más cercano por tipo celular, no dirigió al TSS. Dividió el promotor de *ZFP42* en cuatro segmentos, P1 de −343 a −581 pb, P2 de −561 a −856, P3 de −961 a −1190 y P4 de −1574 a −1829; corrió ChIP-qPCR de H3K27ac sobre los cuatro para localizar la marca y dirigió la guía a P4, el más distal. **Estado**: verificado contra el texto completo del PDF.
3. Kachanov et al. (2025) diseñó las guías con CHOPCHOP, CCTop y el navegador de UCSC, tomando en cuenta la localización del promotor, con mención a región enhancer. **Estado**: parcial, el PDF está descolumnado y las oraciones quedan partidas.

**Lectura**: la dependencia estrecha de la posición respecto del TSS es propiedad de los activadores tipo VP64 y SunTag. Aplicársela a p300 sería usar la regla de otra herramienta y desaprovechar su capacidad distintiva de actuar desde elementos distales.

---

## D4. Tamizaje posicional de cinco guías

**Decisión**: se diseñan cinco guías, una por segmento, y se ensayan individualmente para construir un perfil de activación en función de la posición. Después se combinan las dos o tres mejores para multiplexar.

**Trazabilidad de la decisión, para incluir en el entregable.** El planteo inicial siguió lo que hacen otros ensayos de edición epigenética, teselar el promotor con varias guías repartidas a lo largo de un rango amplio, tal como Liao et al. (2026) con los segmentos P1 a P4 o Hilton et al. (2015) con cuatro guías por promotor. Al caracterizar el locus apareció la disposición divergente con *RPGRIP1L* descrita en D2, y ese teselado amplio perdió sentido: hacia coordenadas negativas las guías no se alejaban del promotor de *FTO* hacia territorio propio, sino que entraban en el cuerpo del gen vecino. De ahí la decisión de concentrar el diseño en una única región, seleccionada por análisis y no por costumbre.

### D4.1 Comparación de regiones blanco candidatas

**Destino: material entregable, sección de Diseño Experimental del Obligatorio.** Se documenta porque la elección de región es la decisión de diseño de mayor peso del trabajo y su justificación es evaluable.

Criterios de comparación aplicados: probabilidad de activar *FTO*, riesgo de modificar *RPGRIP1L*, respaldo bibliográfico del tipo de elemento, capacidad de generar evidencia propia sobre la pregunta de especificidad, costo en extensión y complejidad, e interpretabilidad de un resultado negativo.

**Opción A. Enhancer del lado de *FTO*, con dos posiciones dentro del elemento y un comparador en el promotor compartido.**
A favor: el enhancer ENSR16_BDMQQ es el primer elemento regulatorio anotado que pertenece al territorio de *FTO* y no al compartido; Hilton et al. (2015) documentan activación por dCas9-p300 desde enhancers; muestrear dos posiciones dentro del elemento cubre la variabilidad guía a guía; y el comparador en el promotor compartido permite demostrar con datos propios que la elección de elemento importa en este locus. Un resultado negativo sigue siendo interpretable, puesto que el comparador distingue entre elemento inadecuado y sistema que no funciona.
En contra: el comparador, por diseño, puede afectar al vecino.

**Opción B. Solo el enhancer del lado de *FTO*, sin comparador.**
A favor: es el diseño de menor riesgo sobre *RPGRIP1L* entre los proximales y el más económico en extensión.
En contra: sin comparador, la afirmación de que se eligió la región correcta queda sin respaldo experimental propio y depende del argumento bibliográfico. Un resultado negativo no distingue entre elemento equivocado y falla del sistema, que es la peor situación posible en un trabajo de diseño.

**Opción C. Solo el promotor bidireccional compartido.**
A favor: es la región donde se ensambla la maquinaria basal y, por lo tanto, la que probablemente rinda mayor activación de *FTO*; es lo que haría un diseño convencional de CRISPRa; convierte la coactivación en objeto de estudio.
En contra: es exactamente la región que la arquitectura del locus desaconseja. El problema no es de seguridad sino de atribución: si el fenotipo de senescencia se mueve, no hay forma de separar la contribución de *FTO* de la de *RPGRIP1L*, y el desenlace del proyecto es justamente ese fenotipo.

**Opción D. Sitios CUX1 del primer intrón (rs1421085 y rs8050136).**
A favor: son elementos con función regulatoria documentada sobre *FTO*, con mecanismo descrito de isoformas activadora y represora; están a decenas de kilobases del vecino, de modo que el riesgo de coactivación proximal es el más bajo; y Hilton et al. (2015) muestran que p300 activa desde elementos distales.
En contra: la evidencia proviene de contexto metabólico y neuronal, no ovárico; la isoforma P110 activa los promotores mínimos de *FTO* y de *RPGRIP1L*, de modo que ni siquiera garantiza especificidad; a 63 y 78 kb del TSS la eficiencia de activación es más variable y un resultado negativo aporta poca información; la región está implicada en efectos a larga distancia sobre otros genes, lo que abre un segundo frente de especificidad; y explicar CUX1, los SNP y el contexto de obesidad consume extensión y desvía la narrativa del envejecimiento ovárico.

**Selección: opción A.** Es la única que convierte el hallazgo sobre la arquitectura del locus en evidencia propia en lugar de dejarlo como argumento; concentra el diseño en una sola región, que es el criterio pedido; el costo del comparador es una fila de tabla; y es la única en la que un resultado negativo conserva interpretabilidad. El panel se resuelve con tres guías, número que constituye el piso del diseño: por debajo se pierde la capacidad de distinguir entre elemento inadecuado y guía defectuosa, y por encima se compra resolución que el sistema de lectura no puede medir.

### D4.2 Panel final de guías

**Decisión de resolución.** Una versión intermedia de este diseño contemplaba cuatro guías teseladas cada 140 pb dentro del enhancer. Se descartó tras verificar que ninguno de los tres precedentes trabaja a esa resolución: Xiao et al. (2019) compararon dos sgRNA para *rh4* separados por cientos de pares de bases, uno en el entorno del TSS y otro a +767, con rendimientos distintos; Liao et al. (2026) repartieron cuatro segmentos a lo largo de 1,5 kb; y Hilton et al. (2015) usaron cuatro guías por promotor pero cotransfectadas como combinación, sin compararlas entre sí. Teselar a 140 pb habría producido diferencias probablemente indistinguibles por qPCR y habría consumido el presupuesto de guías sin separar nada. La información proviene de contrastar elementos, no posiciones dentro de un mismo elemento.

**Panel definitivo: tres guías.**

| Guía | Posición relativa al TSS de FTO-206 | Región | Función en el diseño |
| :--- | :--- | :--- | :--- |
| gFTO-1 | aproximadamente +60 | Enhancer ENSR16_BDMQQ, extremo proximal | Evalúa activación desde el elemento propio de *FTO* |
| gFTO-2 | aproximadamente +450 | Enhancer ENSR16_BDMQQ, extremo distal | Segunda posición dentro del mismo elemento, separada unos 390 pb de la anterior |
| gCOMP | aproximadamente −200 | Promotor compartido ENSR16_9RBJC | Comparador; contrasta el elemento propio contra el compartido y evalúa el efecto sobre *RPGRIP1L* |

**Por qué dos guías en el elemento blanco y no una.** El rendimiento de las guías de CRISPRa es marcadamente variable de guía a guía, incluso entre posiciones próximas, y ese es el modo de falla más frecuente del sistema. Con una sola guía, un resultado negativo no permite distinguir entre elemento inadecuado y guía defectuosa. Con dos, el resultado negativo conserva interpretabilidad. Xiao et al. (2019) ilustran el punto: sus dos sgRNA sobre el mismo gen produjeron efectos de magnitud distinta.

**Multiplexado como contingencia.** No se destina un brazo propio a la combinación de guías. Si ninguna guía individual alcanza el umbral de activación definido, se evalúa la cotransfección de gFTO-1 y gFTO-2, siguiendo el criterio de Hilton et al. (2015) y Liao et al. (2026).

**Descartado del panel**: una guía en el enhancer del lado de *RPGRIP1L* (ENSR16_9RBJ8, −758 a −326). Preguntaba si ese elemento alimenta la transcripción de *FTO*, que es una cuestión secundaria, y el contraste de especificidad ya queda cubierto por gCOMP.

Las posiciones son orientativas y se ajustarán a la disponibilidad de PAM NGG al correr el diseño en CRISPOR sobre las secuencias de chr16:53.704.168-53.704.740 y chr16:53.703.906-53.704.106.

**Lo que el diseño pone a prueba**: si las guías del enhancer propio activan *FTO* con menor efecto sobre *RPGRIP1L* que el comparador del promotor compartido, queda demostrado con datos propios que la ventana canónica no era la opción correcta en este locus.

**Mejora sobre el precedente**: Liao et al. (2026) incluyeron un control de especificidad posicional, verificando que el enriquecimiento de H3K27ac aumentó en el segmento dirigido y no en los otros tres del mismo promotor, pero no reportan medición de genes vecinos. El diseño propuesto conserva ese control posicional y le agrega el control de gen vecino.

**Fundamento del ensayo individual**: Hilton et al. (2015) muestran que dCas9-p300 activa con una sola guía, de modo que probar de a una es interpretable y no requiere multiplexar para ver señal.

**Rendimiento para el entregable**: el perfil de activación por posición es una figura propia, alimenta el criterio de Resultados de la rúbrica, y responde de una sola vez las dos preguntas de la oral sobre cómo se determinaron las eficiencias y qué se descartó.

**Límite acordado**: no más de cinco guías, para que el contenido no se desborde.

---

## D5. RPGRIP1L como lector de especificidad

**Decisión**: se mide el ARNm de *RPGRIP1L* para cada una de las cinco guías, y el criterio de selección deja de ser la activación de *FTO* en términos absolutos y pasa a ser la **relación entre activación de *FTO* y activación de *RPGRIP1L***.

**Fundamento**: dado que ambos genes comparten región promotora, la coactivación de *RPGRIP1L* es algo que puede ocurrir y que hay que evaluar experimentalmente. No se asume que ocurrirá ni que no ocurrirá. La arquitectura del locus aporta así un control de especificidad que no hay que inventar.

**Por qué importa medirlo en granulosa**: *RPGRIP1L* participa en la compuerta ciliar, entre otras cosas asegurando la cantidad adecuada de CEP290 en la zona de transición, y actúa sobre la vía Sonic Hedgehog y GLI; sus mutaciones causan ciliopatías graves (síndrome de Joubert tipo 7, síndrome de Meckel-Gruber tipo 5). En el ovario se han descrito cilios primarios en células de la granulosa de folículos antrales, la ablación de IFT88 produce disfunción ovárica con efecto sobre la síntesis o secreción de estrógenos, y hay evidencia de que los cilios primarios regulan enzimas esteroidogénicas y la secreción de progesterona durante la luteinización. Ergo, un cambio en *RPGRIP1L* podría alterar esteroidogénesis y confundir la lectura fenotípica del experimento.

**Estado**: la ubicación y la función de zona de transición están verificadas; la función ciliar detallada y la evidencia sobre cilios en granulosa son de búsqueda y requieren contraste contra los textos completos antes de citarse en el entregable.

### D5.1 Análisis del riesgo real de coactivar RPGRIP1L

Se hace explícito porque condiciona si el proyecto avanza o cambia de blanco. Conclusión anticipada: **avanza**, con la coactivación medida y no asumida.

**Riesgo de toxicidad: no documentado.** Prácticamente toda la literatura sobre RPGRIP1L es de pérdida de función, donde el fenotipo es grave (ciliopatías). El único reporte de sobreexpresión que aparece corresponde a la región coiled-coil CC12 en células NIH/3T3, que acorta el cilio primario de manera dependiente de la formación de dímeros; se trata de un fragmento y no de la proteína completa, de modo que se comporta como dominante negativo y no prueba que un aumento moderado de la proteína entera sea nocivo. La bibliografía no aborda de forma extensa el exceso estequiométrico de RPGRIP1L en la zona de transición.

**Riesgo real: de atribución, no de daño.** Si los cilios primarios modulan esteroidogénesis y luteinización en granulosa, un cambio en RPGRIP1L podría mover las lecturas fenotípicas y adjudicarse erróneamente a la reposición de FTO. El problema, por lo tanto, es de interpretación del experimento y se resuelve midiendo, que es exactamente lo que el diseño ya prevé.

**Argumento del techo de activación.** CRISPRa rinde mucho más sobre genes con expresión basal baja o silenciados que sobre genes ya activos. Si RPGRIP1L está bien expresado en granulosa, el cambio relativo alcanzable sería pequeño aunque la marca se deposite. Es una hipótesis verificable midiendo la expresión basal de ambos genes en el modelo antes de intervenir, y conviene incorporar esa medición al diseño.

**Dos mecanismos distintos de interferencia, que no conviene mezclar.** El primero es la deposición de H3K27ac sobre nucleosomas de la región compartida, que es específico del efector p300. El segundo es la ocupación estérica de la propia dCas9 dentro de una región reguladora compartida, que es independiente del dominio efector y está descrito como una limitación general de CRISPRa en promotores solapados. El segundo mecanismo afectaría igual a un dCas9-VP64 o a cualquier otra fusión.

**La dirección del efecto sobre el vecino no está determinada.** En promotores bidireccionales, la transcripción divergente puede producir interferencia transcripcional que reprime al gen vecino en lugar de activarlo. Ergo, RPGRIP1L podría subir, bajar o no moverse, y el diseño no debe asumir ninguna de las tres.

**Decisión**: se avanza con la estrategia. La coactivación pasa a ser una variable medida con dirección no asumida, y su caracterización en un promotor bidireccional con elemento regulatorio compartido documentado constituye conocimiento propio del trabajo, con independencia de que la hipótesis principal se confirme.

---

## D6. El elemento CUX1 del intrón 1 de FTO

**Hecho**: existe un elemento cis-regulatorio dentro del **primer intrón de *FTO***, en la región asociada a adiposidad, reconocido por el factor de transcripción CUX1. El alelo protector de obesidad en el SNP rs8050136 favorece la unión de la isoforma **P110, que actúa como activador de la expresión de *FTO* y de *RPGRIP1L***; el alelo de riesgo es ocupado preferentemente por la isoforma **P200, que actúa como represor transcripcional**. Un segundo elemento CUX1 potencial se ubica en rs1421085.

**Estado**: verificado contra el texto completo de Stratigopoulos et al. (2016), J Clin Invest.

**Dato adicional verificado del mismo trabajo**: en neuronas derivadas de iPSC humanas hubo efectos de dosis alélica sobre la expresión de *FTO*, *RPGRIP1L* y *AKTIP*, mientras que la expresión de otros genes vecinos, incluidos *IRX3*, *IRX5* y *RBL2*, no se alteró.

**Tres consecuencias**

1. **Corrige nuestro propio informe.** El Bloque C, apoyado en q15, sostiene que ninguna fuente identifica un represor unido al promotor de *FTO* y que el descenso se describe como pérdida de activación. CUX1 P200 es un represor con mecanismo documentado, aunque sobre un elemento intrónico y en contexto metabólico, no en granulosa ni sobre el promotor proximal. Hay que matizar la afirmación, no borrarla.
2. **Refuerza D3.** El elemento funcional documentado para *FTO* no está en el promotor proximal sino dentro del intrón 1, lo cual sostiene que la ventana canónica no es el único blanco razonable.
3. **No resuelve la especificidad.** P110 activa los promotores mínimos de *FTO* y de *RPGRIP1L*, de modo que mudar el blanco al intrón 1 tampoco separa a los dos genes.

**Consideración adicional**: la región del intrón 1 de *FTO* ha sido propuesta como elemento de acción a distancia sobre *IRX3* e *IRX5*. Si se decidiera dirigir guías a esa región, esos genes deberían incorporarse al panel de lectura de especificidad. El propio trabajo de 2016 no observó cambios en ellos, pero la posibilidad debe evaluarse en el modelo propio.

---

## D7. Etiqueta en la dCas9

**Decisión**: incorporar una etiqueta (3xFLAG o HA) en el extremo amino de la dCas9 del constructo.

**Fundamento**: sirve simultáneamente para verificar expresión del efector por western, para hacer ChIP anti-etiqueta que demuestre ocupancia física del complejo sobre la ventana dirigida, y para distinguir el efector exógeno de proteínas endógenas. El propio vector del curso, pX459 (Addgene 62988), lleva 3xFLAG en el extremo amino de la Cas9, de modo que la decisión es consistente con el material de cátedra.

**Estado**: la presencia de 3xFLAG en pX459 fue verificada leyendo el archivo de secuencia del repositorio.

---

## D8. Reubicación de la etapa 0

**Decisión**: el mapeo de H3K27ac en granulosa joven contra envejecida deja de ser una compuerta que bloquea el ensayo de activación y pasa a cumplir dos funciones, informar dónde teselar y permitir interpretar el resultado del tamizaje.

**Fundamento**: con el tamizaje posicional de cinco guías, la selección empírica de la región queda dentro del propio experimento. El mapeo conserva valor porque indica si el segmento ganador coincide con el que pierde acetilación con la edad, que es el eslabón mecanístico, pero no hace falta resolverlo antes de empezar.

**Efecto secundario**: ahorra espacio en las diez carillas y vuelve el diseño defendible sin depender de un dato que la literatura no tiene.

---

## D9. Alternativas evaluadas y descartadas

Se registran para la tabla de alternativas del Diseño Experimental y para la pregunta de la oral sobre resultados descartados.

| Alternativa | A favor | En contra | Estado |
| :--- | :--- | :--- | :--- |
| Reprimir *FOS* con dCas9-KRAB | Efector proximal del fenotipo; evita el problema del mecanismo promotor de *FTO*; KRAB es una carga mucho menor que el core de p300, lo cual alivia entrega | *FOS* es un gen de respuesta temprana inmediata con función fisiológica en granulosa, y la represión sostenida es difícil de titular; trata el efector y deja intacta la desregulación de m6A sobre el resto del transcriptoma; H3K9me3 es una marca con capacidad de propagación, menos controlable que la acetilación | Descartada, se argumenta en el escrito |
| Reprimir el escritor *METTL3* | Actúa sobre la misma vía por el extremo opuesto | Efecto aún más global que activar *FTO*; se aleja del eje descrito en granulosa | Descartada |
| dCas9-TET1 sobre el promotor de *FTO* | Sería el efector coherente si el mecanismo fuese hipermetilación | No hay ningún dato de metilación sobre el promotor de *FTO* en granulosa, de modo que carecería de sustrato verificado que revertir | Descartada, con la salvedad de que si el mapeo mostrara hipermetilación densa, una estrategia combinada TET1 más p300 pasaría a ser preferible |
| Sobreexpresión de *FTO* por transgén | Es la maniobra con evidencia fenotípica directa en granulosa | No es edición epigenómica, pierde el control de la arquitectura regulatoria del locus y no responde a la consigna del mismo modo | Descartada como estrategia, se usa como referencia de efecto esperable |

---

## D10. Referencias nuevas incorporadas por esta línea de trabajo

Pendientes de sumar a la bibliografía consolidada de `INFORME_GENERAL.md` una vez verificados los metadatos completos.

| Referencia | Identificador | Estado del metadato |
| :--- | :--- | :--- |
| Stratigopoulos et al. (2016). *Hypomorphism of Fto and Rpgrip1l causes obesity in mice*. J Clin Invest | DOI 10.1172/JCI85526, PMID 27064284 | DOI y PMID verificados; texto completo consultado |
| Stratigopoulos et al. (2011). *Cut-like homeobox 1 (CUX1) regulates expression of the FTO and RPGRIP1L genes and coordinates leptin receptor signaling*. J Biol Chem | PMID 21037323 | DOI pendiente de verificar |
| Stratigopoulos et al. (2014). *Hypomorphism for RPGRIP1L, a ciliary gene vicinal to the FTO locus, causes increased adiposity in mice*. Cell Metab | PMID 24807221 | DOI pendiente de verificar |

---

## 11. Qué falta para cerrar el bloque de diseño

Los tres primeros puntos pendientes (TSS exacto, coordenadas de *RPGRIP1L* y distancia entre TSS, y Regulatory Build) quedaron resueltos el 2026-07-26 mediante consulta a la API REST de Ensembl y están volcados en D1, D2 y D4.

Queda pendiente:

1. Verificación de los textos completos de Stratigopoulos et al. (2011, JBC) y (2014, Cell Metab) antes de citarlos en el entregable. El acceso a PubMed y PMC devolvió reCAPTCHA y el sitio de JBC no entregó contenido.
2. Descarga de la secuencia FASTA de las cinco ventanas para importar a Benchling y correr el diseño de guías en CRISPOR.
3. Confirmar si el enhancer ENSR16_BDMQQ solapa el exón 1 de FTO-206 o cae ya en el primer intrón, dato menor para la unión de dCas9 pero relevante para describir con precisión el blanco.
4. Verificar si el Regulatory Build anota sitios CTCF en la región ampliada, puesto que la consulta se hizo sobre chr16:53.698.000-53.712.000 y no devolvió ninguno; conviene ampliar la ventana antes de afirmar que no existen.

## 12. Registro de consultas a la API de Ensembl

Endpoints utilizados el 2026-07-26, para poder rehacer la consulta y para citar el método en el escrito.

| Consulta | Endpoint |
| :--- | :--- |
| Transcripto MANE de *FTO* | `rest.ensembl.org/lookup/id/ENST00000471389` |
| Gen *RPGRIP1L* | `rest.ensembl.org/lookup/symbol/homo_sapiens/RPGRIP1L` |
| Transcripto canónico de *RPGRIP1L* | `rest.ensembl.org/lookup/id/ENST00000647211` |
| Elementos regulatorios de la región | `rest.ensembl.org/overlap/region/human/16:53698000-53712000?feature=regulatory` |
| Variantes | `rest.ensembl.org/variation/human/rs8050136` y `rs1421085` |
