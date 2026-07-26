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

## D0. Jerarquía de fuentes y correcciones aplicadas (revisión del 2026-07-26)

Este archivo fue revisado tras incorporar el anexo técnico genómico y regulatorio. Las correcciones C1 a C8, detalladas en `FTO_anexo_tecnico/07_correcciones_afirmaciones_previas.md`, quedaron aplicadas en los apartados correspondientes.

**Jerarquía de fuentes, de cumplimiento obligatorio en todo el proyecto.**

| Fuente | Rol asignado |
| :--- | :--- |
| Ensembl 116 y GENCODE 50 | Referencia estructural para coordenadas, transcritos, exones y segmentación |
| MANE Select | Referencia operativa principal para nombrar los TSS |
| Clusters de inicio (*RPGRIP1L* 53.703.938 y *FTO* 53.703.963) | Referencias adicionales obligatorias; toda distancia se informa contra los cuatro puntos |
| ENCODE cCRE | Clasificación epigenómica independiente |
| FANTOM5 CAGE | Evidencia de iniciación transcripcional, manteniendo separadas las coordenadas hg19 |
| GeneHancer | Integración secundaria; no reemplaza la segmentación de Ensembl ni asigna gen diana por sí sola |

**Los cinco puntos que toda descripción del locus debe respetar.**

1. La región inter-TSS no es un espacio vacío entre dos sitios de inicio. Contiene dos clusters de inicio anotados, el de *RPGRIP1L* en 53.703.938 con 12 transcritos y el de *FTO* en 53.703.963 con 22 transcritos, separados entre sí por 25 pb.
2. La segmentación en enhancer y promotor depende del universo de anotación. Bajo Ensembl 116 hay tres elementos consecutivos; bajo ENCODE hay dos firmas de promotor y una de enhancer proximal con límites distintos; bajo GeneHancer hay un único bloque de 1.971 pb. Toda afirmación sobre elementos debe declarar el universo empleado.
3. Compartir el mismo elemento de firma promotora implica un riesgo alto de coactivación, pero no demuestra que ambos genes vayan a responder de igual modo ni en la misma dirección. La direccionalidad debe determinarse experimentalmente.
4. La ausencia de sitios CTCF anotados en la ventana inter-TSS describe el estado del Regulatory Build, no demuestra ausencia funcional de aislamiento ni de arquitectura cromatínica direccional.
5. El sitio de referencia +60 se ubica dentro del exón 1 codificante del transcrito MANE y, simultáneamente, dentro del elemento Ensembl ENSR16_BDMQQ, que solapa ese exón en 62 pb. Ambas cosas son ciertas a la vez y deben enunciarse juntas.

**Corrección sobre GeneHancer y *RBL2*.** El elemento GH16J053703 está asignado por GeneHancer a *FTO* y a *RPGRIP1L* con score 543 y valor 1334,5 en ambos casos, y a *RBL2* con score 17 y valor 39,03. La lectura previa, que atribuía el bloque a *RBL2*, provino de consultar únicamente el archivo filtrado de interacciones double-elite y queda retirada. *RBL2* no se incorpora al panel de lectura.

**Regla de referencia de coordenadas.** El gen ENSG00000140718 comienza en 53.701.692, unos 2,5 kb antes que el transcrito MANE, y GeneHancer ancla *FTO* en esa coordenada y *RPGRIP1L* en 53.703.938. Toda distancia informada debe declarar respecto de qué punto se calcula.

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

**Estado**: verificado, con una discrepancia entre fuentes que corresponde documentar.

Stratigopoulos et al. (2016), J Clin Invest, dice literalmente: "retinitis pigmentosa GTPase regulator-interacting protein-1 like (RPGRIP1L), located **<100 bp** upstream and in opposite transcriptional orientation to FTO (Figure 1A), is a transition zone structural component of the primary cilium".

Stratigopoulos et al. (2014), Cell Metab, del mismo grupo, dice: "RPGRIP1L (Retinitis Pigmentosa GTPase Regulator-Interacting Protein-1 Like) is located **>100bp** 5′ in the opposite transcriptional orientation of FTO (Fig. 1A)".

Las dos publicaciones del mismo grupo consignan el signo de la desigualdad de manera opuesta. La inconsistencia se registra como tal y **no se presenta ninguna de las dos cifras como directamente incorrecta**: la distancia declarada puede depender de la especie considerada, del ensamblado empleado, del transcrito tomado como referencia o de la definición del sitio de inicio, y ninguno de los dos textos explicita cuál de esos elementos usa.

**Referencia operativa del proyecto**: los **297 pb** calculados sobre GRCh38.p14 con Ensembl 116 entre los TSS de referencia definidos en D0. Las citas de 2014 y 2016 se emplean para sostener la orientación divergente y la proximidad; la cifra que se informa en el entregable es la medida.

Lo que sí queda verificado sin discrepancia en ambas publicaciones es la disposición divergente, la proximidad al sitio de inicio de *FTO* y la naturaleza de *RPGRIP1L* como componente estructural de la zona de transición del cilio primario.

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

Más importante todavía, **las anotaciones consultadas no identifican, corriente arriba del TSS de referencia de *FTO*, ninguna región demostrablemente exclusiva de *FTO***: a partir de −326 y hacia coordenadas menores ya se está dentro del cuerpo del gen *RPGRIP1L*, puesto que su TSS queda en −297 y su transcripción avanza en sentido opuesto. La ventana canónica de CRISPRa, por lo tanto, no solo es compartida sino que su extensión hacia posiciones más negativas empeora el problema en lugar de mejorarlo.

**Las regiones corriente abajo del TSS de referencia se encuentran más alejadas de los sitios de inicio de *RPGRIP1L*, pero las anotaciones disponibles no demuestran que constituyan regiones funcionalmente exclusivas de *FTO*.** En ese tramo se ubican el elemento ENSR16_BDMQQ (+12 a +584) y, mucho más adentro del primer intrón, los sitios CUX1 de rs1421085 y rs8050136.

**Corrección aplicada el 2026-07-26 (C3 y C6).** La descripción anterior trataba la región inter-TSS como el espacio entre dos sitios de inicio enfrentados. El anexo técnico muestra que esa lectura, correcta para los TSS MANE, es incompleta: dentro de esos 296 pb hay dos clusters de inicio anotados, el de *RPGRIP1L* en 53.703.938 con 12 transcritos y el de *FTO* en 53.703.963 con 22 transcritos, separados por 25 pb. Cabe aclarar que el número de transcritos anotados que comparten una coordenada no demuestra que ese sitio sea el más utilizado; establecerlo requeriría CAGE, RAMPAGE, RNA-seq de extremo 5′ o lectura larga en el modelo celular.

Asimismo, el enhancer ENSR16_BDMQQ no es un elemento situado limpiamente corriente abajo: solapa en 62 pb el exón 1 del transcrito MANE (53.704.156-53.704.229) y contiene un sitio de inicio anotado de *FTO* en 53.704.182. Y la propia existencia de tres elementos distintos es propiedad de la segmentación de Ensembl: ENCODE ubica dos firmas de promotor y una de enhancer proximal con límites diferentes, y GeneHancer fusiona toda la región en un único bloque de 1.971 pb.

---

## D3. Abandono de la ventana canónica como criterio por defecto

**Decisión**: la posición de las guías no se define por proximidad al TSS sino por evidencia, mediante un tamizaje posicional.

**Fundamento en la literatura**, con tres piezas convergentes:

1. Hilton et al. (2015) titulan el trabajo "activates genes from promoters and enhancers" y sostienen en el resumen que, a diferencia de los activadores dCas9 previos, dCas9-p300 activa genes desde enhancers y con una sola guía. Usaron cuatro guías por promotor endógeno (IL1RN, MYOD, OCT4) y también dirigieron el enhancer HS2 del locus de globina, que es distal. **Estado**: verificado contra el texto completo del PDF.
2. Liao et al. (2026), el precedente más cercano por tipo celular, no dirigió al TSS. Dividió el promotor de *ZFP42* en cuatro segmentos, P1 de −343 a −581 pb, P2 de −561 a −856, P3 de −961 a −1190 y P4 de −1574 a −1829; corrió ChIP-qPCR de H3K27ac sobre los cuatro para localizar la marca y dirigió la guía a P4, el más distal. **Estado**: verificado contra el texto completo del PDF.
3. Kachanov et al. (2025) diseñó las guías con CHOPCHOP, CCTop y el navegador de UCSC, tomando en cuenta la localización del promotor, con mención a región enhancer. **Estado**: parcial, el PDF está descolumnado y las oraciones quedan partidas.

**Lectura**: la dependencia estrecha de la posición respecto del TSS es propiedad de los activadores tipo VP64 y SunTag. Aplicársela a p300 sería usar la regla de otra herramienta y desaprovechar su capacidad distintiva de actuar desde elementos distales.

---

## D4. Tamizaje posicional del bloque regulatorio

> **Estado: formulación histórica superada, reemplazada por la revisión del 2026-07-26.** El apartado se conserva por trazabilidad. La decisión vigente es la siguiente: **el diseño actual compara guías individuales pertenecientes a W4, W3 y W1, más un brazo combinado W4 + W3. W2 queda retirada de las candidatas preferidas.** Las secuencias definitivas siguen pendientes. El panel completo y sus controles están en la versión 3 del esqueleto, apartado 3.8.

**Decisión histórica, superada**: se diseñan cinco guías, una por segmento, y se ensayan individualmente para construir un perfil de activación en función de la posición. Después se combinan las dos o tres mejores para multiplexar.

**Trazabilidad de la decisión, para incluir en el entregable.** El planteo inicial siguió lo que hacen otros ensayos de edición epigenética, teselar el promotor con varias guías repartidas a lo largo de un rango amplio, tal como Liao et al. (2026) con los segmentos P1 a P4 o Hilton et al. (2015) con cuatro guías por promotor. Al caracterizar el locus apareció la disposición divergente con *RPGRIP1L* descrita en D2, y ese teselado amplio perdió sentido: hacia coordenadas negativas las guías no se alejaban del promotor de *FTO* hacia territorio propio, sino que entraban en el cuerpo del gen vecino. De ahí la decisión de concentrar el diseño en una única región, seleccionada por análisis y no por costumbre.

### D4.1 Comparación de regiones blanco candidatas

**Destino: material entregable, sección de Diseño Experimental del Obligatorio.** Se documenta porque la elección de región es la decisión de diseño de mayor peso del trabajo y su justificación es evaluable.

Criterios de comparación aplicados: probabilidad de activar *FTO*, riesgo de modificar *RPGRIP1L*, respaldo bibliográfico del tipo de elemento, capacidad de generar evidencia propia sobre la pregunta de especificidad, costo en extensión y complejidad, e interpretabilidad de un resultado negativo.

**Opción A. Enhancer del lado de *FTO*, con dos posiciones dentro del elemento y un comparador en el promotor compartido.**
A favor: se trata de una **región intrónica candidata a enhancer, incluida por Ensembl dentro de ENSR16_BDMQQ y clasificada por ENCODE como pELS EH38E1816377**, que es el primer elemento anotado situado corriente abajo del TSS de referencia y por lo tanto más alejado de los sitios de inicio de *RPGRIP1L*; Hilton et al. (2015) documentan activación por dCas9-p300 desde enhancers; muestrear dos posiciones dentro del elemento cubre la variabilidad guía a guía; y el comparador en el promotor divergente permite generar datos propios sobre si la elección de región importa en este locus. Un resultado negativo sigue siendo interpretable, puesto que el comparador distingue entre región inadecuada y sistema que no funciona.
En contra: el comparador, por diseño, puede afectar al vecino. **Ninguna de las dos anotaciones, ni la de Ensembl ni la de ENCODE, demuestra que esa región regule *FTO* en granulosa.**

**Opción B. Solo el enhancer del lado de *FTO*, sin comparador.**
A favor: es el diseño de menor riesgo sobre *RPGRIP1L* entre los proximales y el más económico en extensión.
En contra: sin comparador, la afirmación de que se eligió la región correcta queda sin respaldo experimental propio y depende del argumento bibliográfico. Un resultado negativo no distingue entre elemento equivocado y falla del sistema, que es la peor situación posible en un trabajo de diseño.

**Opción C. Solo el promotor bidireccional compartido.**
A favor: es la región donde se ensambla la maquinaria basal y, por lo tanto, la que probablemente rinda mayor activación de *FTO*; es lo que haría un diseño convencional de CRISPRa; convierte la coactivación en objeto de estudio.
En contra: es exactamente la región que la arquitectura del locus desaconseja. El problema no es de seguridad sino de atribución: si el fenotipo de senescencia se mueve, no hay forma de separar la contribución de *FTO* de la de *RPGRIP1L*, y el desenlace del proyecto es justamente ese fenotipo.

**Opción D. Sitios CUX1 del primer intrón (rs1421085 y rs8050136).**
A favor: son elementos con función regulatoria documentada sobre *FTO*, con mecanismo descrito de isoformas activadora y represora; están a decenas de kilobases del vecino, de modo que el riesgo de coactivación proximal es el más bajo; y Hilton et al. (2015) muestran que p300 activa desde elementos distales.
En contra: la evidencia proviene de contexto metabólico y neuronal, no ovárico; la isoforma P110 activa los promotores mínimos de *FTO* y de *RPGRIP1L*, de modo que ni siquiera garantiza especificidad; a 63 y 78 kb del TSS la eficiencia de activación es más variable y un resultado negativo aporta poca información; la región está implicada en efectos a larga distancia sobre otros genes, lo que abre un segundo frente de especificidad; y explicar CUX1, los SNP y el contexto de obesidad consume extensión y desvía la narrativa del envejecimiento ovárico.

**Selección histórica: opción A. Estado: superada, reemplazada por la revisión del 2026-07-26.** Se conserva por trazabilidad. Su fundamento era que concentraba el diseño en una sola región y que un resultado negativo conservaba interpretabilidad gracias al comparador.

**Diseño vigente.** Ya no consiste en dos guías en una región más un comparador. El panel actual compara cuatro cosas: activación promotora próxima mediante W4; activación de una región intrónica con firma pELS mediante W3; activación del centro del promotor divergente mediante W1; y la combinación W4 más W3. W2 queda documentada como analizada y retirada.

### D4.2 Panel final de guías

**Decisión de resolución.** Una versión intermedia de este diseño contemplaba cuatro guías teseladas cada 140 pb dentro del enhancer. Se descartó tras verificar que ninguno de los tres precedentes trabaja a esa resolución: Xiao et al. (2019) compararon dos sgRNA para *rh4* separados por cientos de pares de bases, uno en el entorno del TSS y otro a +767, con rendimientos distintos; Liao et al. (2026) repartieron cuatro segmentos a lo largo de 1,5 kb; y Hilton et al. (2015) usaron cuatro guías por promotor pero cotransfectadas como combinación, sin compararlas entre sí. Teselar a 140 pb habría producido diferencias probablemente indistinguibles por qPCR y habría consumido el presupuesto de guías sin separar nada. La información proviene de contrastar elementos, no posiciones dentro de un mismo elemento.

**Panel: clasificación provisional revisada el 2026-07-26. Ninguna guía está seleccionada.**

| Sitio | Clasificación provisional | Fundamento |
| :--- | :--- | :--- |
| −200 | **Comparador del promotor divergente.** No se presenta como guía preferente de *FTO* | Las mejores candidatas quedan a menos de 15 pb de los dos clusters simultáneamente, dentro del elemento de firma promotora que contiene todos los sitios de inicio principales de ambos genes |
| +60 | **Retirado del grupo de candidatas preferidas.** Se conserva en la tabla como candidato exónico problemático o eventual comparador | Cae dentro del exón 1 codificante del transcrito MANE; la unión de dCas9 tan próxima al inicio y dentro de secuencia codificante puede introducir efectos difíciles de separar de la acetilación, y falta conocer la frecuencia poblacional de las doce variantes que solapan el protoespaciador |
| +450 | **Candidato regulatorio provisional de menor ambigüedad** | Cae sobre el cCRE EH38E1816377 de tipo enhancer proximal, es intrónico y no tiene sitios de inicio anotados en 300 pb a la redonda. No se selecciona hasta completar actividad y análisis de off-targets |
| chr16:53.704.020-53.704.145 | **Ventana adicional en evaluación**, incorporada el 2026-07-26 | Busca una guía proximal al TSS MANE de *FTO*, no exónica respecto del MANE y menos centrada entre los dos clusters. Resultados en `FTO_anexo_tecnico/09_panel_cuatro_ventanas.md` |

El detalle de candidatas reales con secuencia, PAM, distancias a los cuatro puntos de referencia, elementos solapados y variantes está en `FTO_anexo_tecnico/06_tabla_guias_candidatas.md` y en `FTO_anexo_tecnico/09_panel_cuatro_ventanas.md`.

**Por qué dos guías en el elemento blanco y no una.** El rendimiento de las guías de CRISPRa es marcadamente variable de guía a guía, incluso entre posiciones próximas, y ese es el modo de falla más frecuente del sistema. Con una sola guía, un resultado negativo no permite distinguir entre elemento inadecuado y guía defectuosa. Con dos, el resultado negativo conserva interpretabilidad. Xiao et al. (2019) ilustran el punto: sus dos sgRNA sobre el mismo gen produjeron efectos de magnitud distinta.

**Multiplexado. Formulación histórica superada, reemplazada por la revisión del 2026-07-26.** Este apartado sostenía que no se destinaba un brazo propio a la combinación de guías y que el multiplexado quedaba como contingencia. **El diseño vigente sí incluye un brazo propio: el brazo 5 combina W4 más W3**, siguiendo el criterio de Hilton et al. (2015) y Liao et al. (2026).

**Descartado del panel**: una guía en el enhancer del lado de *RPGRIP1L* (ENSR16_9RBJ8, −758 a −326). Preguntaba si ese elemento alimenta la transcripción de *FTO*, que es una cuestión secundaria, y el contraste de especificidad ya queda cubierto por gCOMP.

Las posiciones son orientativas y se ajustarán a la disponibilidad de PAM NGG al correr el diseño en CRISPOR sobre las secuencias de chr16:53.704.168-53.704.740 y chr16:53.703.906-53.704.106.

**Lo que el diseño pone a prueba**: si las guías de la región intrónica candidata a enhancer activan *FTO* con menor efecto sobre *RPGRIP1L* que el comparador del promotor divergente, se genera evidencia propia sobre si la ventana canónica era o no la opción adecuada en este locus.

**Mejora sobre el precedente**: Liao et al. (2026) incluyeron un control de especificidad posicional, verificando que el enriquecimiento de H3K27ac aumentó en el segmento dirigido y no en los otros tres del mismo promotor, pero no reportan medición de genes vecinos. El diseño propuesto conserva ese control posicional y le agrega el control de gen vecino.

**Fundamento del ensayo individual**: Hilton et al. (2015) muestran que dCas9-p300 activa con una sola guía, de modo que probar de a una es interpretable y no requiere multiplexar para ver señal.

**Rendimiento para el entregable**: el perfil de activación por posición es una figura propia, alimenta el criterio de Resultados de la rúbrica, y responde de una sola vez las dos preguntas de la oral sobre cómo se determinaron las eficiencias y qué se descartó.

**Límite acordado, formulación histórica**: no más de cinco guías, para que el contenido no se desborde. En el diseño vigente el panel tiene cuatro brazos con guías individuales, correspondientes a W4, W3 y W1, más un quinto brazo de combinación W4 más W3.

---

## D5. RPGRIP1L como lector de especificidad

**Decisión vigente**: se mide el ARNm de *RPGRIP1L* en todos los brazos del panel. La formulación anterior, según la cual el criterio de selección pasaba a ser la relación entre activación de *FTO* y activación de *RPGRIP1L*, queda **superada por la revisión del 2026-07-26**, porque colapsaba en una sola métrica dos preguntas distintas y fijaba una razón matemática que todavía no está definida.

Los criterios se mantienen separados: magnitud de activación de *FTO*; magnitud del cambio en *RPGRIP1L*; diferencia o relación normalizada entre ambos efectos, pendiente de definición; efecto sobre el eje m6A–*FOS*; y efecto sobre senescencia. La métrica concreta del tercer punto se definirá más adelante, preferentemente sobre cambios en escala logarítmica, y no se fija en esta versión.

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

**Estado**: verificado contra el texto completo de Stratigopoulos et al. (2011), J Biol Chem, y de Stratigopoulos et al. (2016), J Clin Invest.

**Citas literales de la fuente primaria de 2011**: "FTO and RPGRIP1L (a ciliary gene located in close proximity to the transcriptional start site of FTO) are regulated by isoforms P200 and P110 of the transcription factor, CUX1. This regulation occurs via a single AATAAATA regulatory site (conserved in the mouse) within the FTO intronic region associated with adiposity in humans. Single nucleotide polymorphism rs8050136 (located in this regulatory site) affects binding affinities of P200 and P110. Promoter-probe analysis revealed that binding of P200 to this site represses FTO, whereas binding of P110 increases transcriptional activity from the FTO as well as RPGRIP1L minimal promoters".

**Calificación metodológica que debe acompañar siempre a esta cita.** La evidencia de 2011 proviene de ensayos de desplazamiento de movilidad electroforética y de ensayos de promotor con gen reportero de luciferasa, construidos con **promotores mínimos** de *FTO* y de *RPGRIP1L* amplificados a partir de ADN genómico de fibroblastos primarios humanos homocigotos para uno u otro alelo de rs8050136, y ensayados en líneas hipotalámicas y de neuroblastoma murinas.

**Formulación precisa, de uso obligatorio**: los experimentos demostraron unión a secuencias promotoras y modulación de construcciones reporteras en los modelos ensayados, pero no regulación del locus endógeno en granulosa.

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

**Fundamento**: con el tamizaje posicional del panel, la selección empírica de la región queda dentro del propio experimento. El mapeo conserva valor porque indica si el segmento ganador coincide con el que pierde acetilación con la edad, que es el eslabón mecanístico, pero no hace falta resolverlo antes de empezar.

**Efecto secundario**: ahorra espacio en las diez carillas y vuelve el diseño defendible sin depender de un dato que la literatura no tiene.

---

## D9. Alternativas evaluadas y descartadas

Se registran para la tabla de alternativas del Diseño Experimental y para la pregunta de la oral sobre resultados descartados.

| Alternativa | A favor | En contra | Estado |
| :--- | :--- | :--- | :--- |
| Reprimir *FOS* con dCas9-KRAB | Efector proximal del fenotipo; evita el problema del mecanismo promotor de *FTO*; KRAB es una carga mucho menor que el core de p300, lo cual alivia entrega | *FOS* es un gen de respuesta temprana inmediata con función fisiológica en granulosa, y la represión sostenida es difícil de titular; trata el efector y deja intacta la desregulación de m6A sobre el resto del transcriptoma; H3K9me3 es una marca con capacidad de propagación, menos controlable que la acetilación | Descartada, se argumenta en el escrito |
| Reprimir el escritor *METTL3* | Actúa sobre la misma vía por el extremo opuesto | Efecto aún más global que activar *FTO*; se aleja del eje descrito en granulosa | Descartada |
| dCas9-TET1 sobre el promotor de *FTO* | Sería el efector coherente si el mecanismo fuese hipermetilación | No hay ningún dato de metilación sobre el promotor de *FTO* en granulosa, de modo que carecería de sustrato verificado que revertir | Descartada, con la salvedad de que si el mapeo mostrara hipermetilación densa, una estrategia combinada TET1 más p300 pasaría a ser preferible |
| Sobreexpresión convencional de *FTO* | Constituye una alternativa conceptual de ganancia de función | **La evidencia actualmente auditada no demuestra que revierta el fenotipo senescente en granulosa.** Además, no corresponde a una estrategia de edición epigenética del locus endógeno, pierde el control de la arquitectura regulatoria y no responde a la consigna del mismo modo | Descartada como estrategia. La afirmación previa de que era la maniobra con evidencia fenotípica directa en granulosa queda **retirada por la revisión del 2026-07-26**, y no se reasigna a Wang, Li ni Zhang sin auditoría textual |

---

## D10. Referencias nuevas incorporadas por esta línea de trabajo

Pendientes de sumar a la bibliografía consolidada de `INFORME_GENERAL.md` una vez verificados los metadatos completos.

| Referencia | Identificador | Estado del metadato |
| :--- | :--- | :--- |
| Stratigopoulos et al. (2016). *Hypomorphism of Fto and Rpgrip1l causes obesity in mice*. J Clin Invest | DOI 10.1172/JCI85526, PMID 27064284 | DOI y PMID verificados; texto completo consultado |
| Stratigopoulos et al. (2011). *Cut-like homeobox 1 (CUX1) regulates expression of the FTO and RPGRIP1L genes and coordinates leptin receptor signaling*. J Biol Chem 286(3):2155-2170 | DOI 10.1074/jbc.M110.188482, PMID 21037323 | Verificado; texto completo consultado en copia local HTML |
| Stratigopoulos et al. (2014). *Hypomorphism for RPGRIP1L, a ciliary gene vicinal to the FTO locus, causes increased adiposity in mice*. Cell Metab 19(5):767-779 | DOI 10.1016/j.cmet.2014.04.009, PMID 24807221 | Verificado; texto completo consultado en copia local HTML |

Copias locales de texto completo, obtenidas en formato HTML por indisponibilidad del binario PDF: `Search/manual-reinforce-pdfs/stratigopoulos_2011_cux1_fto_rpgrip1l.html`, `..._2014_rpgrip1l_fto_locus.html` y `..._2016_fto_rpgrip1l_obesity.html`.

---

## 11. Qué falta para cerrar el bloque de diseño

Los tres primeros puntos pendientes (TSS exacto, coordenadas de *RPGRIP1L* y distancia entre TSS, y Regulatory Build) quedaron resueltos el 2026-07-26 mediante consulta a la API REST de Ensembl y están volcados en D1, D2 y D4.

**Resueltos el 2026-07-26.**

1. TSS de referencia, coordenadas de *RPGRIP1L* y distancia entre ambos, mediante consulta a la API REST de Ensembl. Volcados en D1 y D2.
2. Regulatory Build de la región, con los tres elementos y sus límites. Volcado en D2.
3. **Verificación de los textos completos de Stratigopoulos et al. (2011, JBC) y (2014, Cell Metab)**, sobre copias locales de texto completo en formato HTML. Detalle en `FTO_anexo_tecnico/10_aporte_serie_stratigopoulos.md`.
4. **Solapamiento de ENSR16_BDMQQ con el exón 1** del transcrito de referencia: el elemento abarca 53.704.168-53.704.740 y solapa en 62 pb el exón 1, que va de 53.704.156 a 53.704.229, continuando luego en el primer intrón.
5. **Búsqueda ampliada de sitios CTCF**: el Regulatory Build registra ocho sitios en chr16:53.702.356-54.121.941, el más próximo en 53.744.515, todos dentro del cuerpo del gen y ninguno en la ventana inter-TSS.

**Pendientes reales.**

1. Ejecución de CRISPOR sobre las secuencias de las ventanas, con versión y genoma declarados.
2. Actividad predicha de cada protoespaciador.
3. Análisis de off-targets a escala genómica, con desapareamientos, ubicación y estado de la secuencia semilla.
4. Frecuencias poblacionales de las variantes que solapan cada protoespaciador.
5. Selección definitiva de guías.
6. Archivos GenBank exportados desde Benchling y armado de los anexos.

## 12. Registro de consultas a la API de Ensembl

Endpoints utilizados el 2026-07-26, para poder rehacer la consulta y para citar el método en el escrito.

| Consulta | Endpoint |
| :--- | :--- |
| Transcripto MANE de *FTO* | `rest.ensembl.org/lookup/id/ENST00000471389` |
| Gen *RPGRIP1L* | `rest.ensembl.org/lookup/symbol/homo_sapiens/RPGRIP1L` |
| Transcripto canónico de *RPGRIP1L* | `rest.ensembl.org/lookup/id/ENST00000647211` |
| Elementos regulatorios de la región | `rest.ensembl.org/overlap/region/human/16:53698000-53712000?feature=regulatory` |
| Variantes | `rest.ensembl.org/variation/human/rs8050136` y `rs1421085` |
