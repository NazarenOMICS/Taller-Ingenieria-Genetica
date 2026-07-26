# Guion del seminario: Edición epigenética por CRISPR/dCas9

## Índice operativo

Modalidad 1 (Presentación de técnicas, 15 pts). Fecha: martes 21/07. Formato: grupo de 3, 20 minutos.
Paper base (caso central): Xiao B, Yin S, Hu Y, et al. (2019). Epigenetic editing by CRISPR/dCas9 in *Plasmodium falciparum*. *PNAS* 116(1):255-260, más su apéndice.

Qué contiene: guion oral verbatim, sin bloques de contenido visual. Registro de seminario técnico. Estructura reorganizada: 1 min de intro, marco general de la técnica, experimentos uno por uno (motivo, método, resultado, implicancia), 1 min de conclusión. Cuerpo hablado alrededor de 2.150 palabras. Convenciones: ADN y ARN (no DNA/RNA); Cas9 y dCas9 como proteína, en femenino. Datos trazables al paper y su apéndice.

Nota marcada (slide 6): el paper rotula la vía de invasión de *rh4* como "sialic acid-dependent" en un encabezado, en contradicción con su abstract y con el mecanismo (neuraminidasa); se expone la versión correcta, independiente de ácido siálico.

---

## Slide 1. Intro

Guion: La edición epigenética mediante CRISPR/dCas9 permite reprimir o activar un gen sin introducir cortes en el ADN, modificando la cromatina que lo rodea en lugar de su secuencia. El caso de referencia que vamos a presentar es el trabajo de Xiao y colaboradores, que lleva esta técnica a *Plasmodium falciparum*, el agente de la forma más grave de malaria.

---

## Slide 2. Por qué hace falta

Guion: *Plasmodium falciparum* causa cerca de medio millón de muertes anuales, de modo que disponer de herramientas para estudiar su biología tiene un interés directo. El problema es que su genoma es difícil de manipular. Su eficiencia de recombinación homóloga es baja, lo que dificulta introducir cambios dirigidos. Además, carece de la maquinaria de ARN de interferencia, así que la vía habitual para silenciar un gen de forma reversible no está disponible. Y su genoma es haploide, por lo que romper un gen esencial es letal y no deja material para estudiar su función. El CRISPR/Cas9 convencional ya se usa en el parásito para disrupción, marcado y reemplazo alélico, pero por estas mismas razones queda corto en dos casos concretos: los genes esenciales y los ARN no codificantes. Por esto, existe la necesidad de tener un sistema que sea capaz de aumentar o reducir la expresión de un gen sin romper el ADN y de manera reversible. Ese es el problema que la técnica viene a resolver.

---

## Slide 3. La receta general de la edición epigenética CRISPR

Guion: Cualquier sistema de edición con CRISPR se arma con dos piezas. La primera es una Cas9, que como ya sabemos, reconoce su blanco combinando dos elementos: el sgRNA, que aparea por complementariedad con una de las cadenas del ADN, y el PAM, NGG en este sistema, que la proteína lee directamente y sin la cual no reconoce el sitio. El corte en sí lo hacen dos dominios catalíticos distintos, RuvC y HNH, uno sobre cada cadena. Sin embargo, en el CRISPR de edición epigenética se utiliza una dCas9, una Cas9 desactivada como nucleasa mediante mutaciones D10A y H840A que inactivan los dominios catalíticos de la proteína. Como no modifican las regiones que reconocen el PAM ni el sgRNA, la dCas9 resultante viaja a la misma dirección genómica que una Cas9 activa pero no corta. La segunda pieza es un efector fusionado a esa dCas9, que puede ser de dos tipos. Un efector catalítico es una enzima que escribe o borra una marca epigenética por sí misma. Un efector reclutador no modifica de forma directa, sino que atrae hacia el sitio maquinaria endógena de la célula. Esta distinción entre efector catalítico y reclutador va a ser importante para entender los resultados.

---

## Slide 4. El efector catalítico: acetilasa o deacetilasa

Guion: El efector catalítico que se fusiona a la dCas9 pertenece, según lo que se quiera lograr, a una de dos clases de enzima: una acetiltransferasa, o HAT, si se quiere activar, o una deacetilasa, o HDAC, si se quiere reprimir. Las dos actúan sobre la misma marca, la acetilación de las lisinas 9 y 14 de la histona H3 en la región del sitio de inicio de la transcripción, el TSS, pero en sentidos opuestos: la HAT la escribe, la HDAC la retira. Que esa marca regule la transcripción tiene una explicación electrostática. Las lisinas son residuos de carga positiva que, sin modificar, se unen con fuerza al esqueleto de fosfatos del ADN, de carga negativa, y mantienen la cromatina compacta. Cuando la acetiltransferasa transfiere grupos acetilo a esas lisinas, neutraliza su carga positiva, el contacto entre la histona y el ADN se debilita, la cromatina se relaja y el gen queda accesible: se activa. Cuando la deacetilasa retira esos grupos acetilo, la carga se restablece, la cromatina se compacta y el gen se reprime. En este trabajo esas dos enzimas no son de diseño ni tomadas de otro organismo, sino las endógenas del propio parásito, elegidas precisamente por eso, porque ya operan sobre su cromatina de forma natural: como HAT, PfGCN5, y como HDAC, PfSir2a, esta última dependiente de NAD. Antes de medir cualquier efecto sobre un gen, los autores confirman por Western blot e inmunofluorescencia que las dos construcciones se expresan al tamaño esperado y se enriquecen en el núcleo, donde reside la cromatina. Con la herramienta validada, el resto del trabajo consiste en experimentos que la ponen a prueba gen por gen.

---

## Slide 5. Activar *rh4*: unión y marca

Guion: El primer experimento busca demostrar que un efector catalítico reclutado a un gen silenciado puede activarlo. El gen elegido es *rh4*, que participa en una de las vías de invasión del glóbulo rojo y se encuentra silenciado en la cepa Dd2; partir de un gen silenciado es conveniente, porque cualquier activación se mide sobre un nivel basal casi nulo. El diseño evalúa tres condiciones sucesivas, que se repiten en los experimentos siguientes: si la dCas9 se une donde se la dirige, si deposita la marca, y si eso modifica la transcripción. Para las dos primeras se emplea inmunoprecipitación de cromatina, una técnica que permite recuperar los fragmentos de ADN a los que estaba unida una proteína, o que portaban una marca determinada, y medir después con qué frecuencia aparece cada posición del gen. Con un anticuerpo contra la etiqueta de la dCas9, se confirma que la proteína ocupa de forma alta y específica la región de *rh4* cercana al sitio guía. Con un anticuerpo contra la histona H3 acetilada, se confirma que en ese mismo tramo aparece la marca de acetilación, que se extiende por el gen algo más que la propia proteína, dado que la enzima, una vez reclutada, acetila también los nucleosomas vecinos. Queda así probado que la dCas9-GCN5 alcanza su blanco y deposita la marca esperada; resta el paso decisivo, determinar si esto se traduce en un aumento de la transcripción.

---

## Slide 6. Activar *rh4*: transcripción, fenotipo y la comparación con VPR

Guion: La transcripción se mide por RT-qPCR, normalizada a un gen constitutivo, y muestra que *rh4* alcanza al menos 113 veces más expresión en la línea editada que en la silvestre. Esa magnitud, más de cien veces sobre un gen que partía silenciado, es el dato central del experimento, porque mide la potencia del sistema para activar. La especificidad se controla midiendo en paralelo *ama1*, un gen que se expresa en el mismo estadio pero no es blanco del sistema, que no se modifica. El efecto alcanza el fenotipo: la línea editada adquiere la capacidad de invadir eritrocitos tratados con neuraminidasa, que la cepa silvestre no puede invadir. Como la neuraminidasa elimina el ácido siálico de la superficie, esa invasión corresponde a la vía independiente de ácido siálico, coherente con la función de RH4. Cabe una aclaración de precisión: el encabezado del artículo la denomina dependiente, en contradicción con su propio resumen y con el mecanismo, de modo que se expone en su versión correcta. Este experimento contrasta además las dos clases de efector sobre el mismo gen. Por un lado, uno catalítico, GCN5, que escribe la marca por sí mismo; por el otro, uno reclutador, VPR, un activador sintético de uso estándar en otros eucariotas, que no escribe la marca sino que atrae maquinaria activadora de la célula. El resultado separa la unión del efecto: VPR ocupa el sitio incluso en mayor medida que GCN5, pero deposita menos acetilación y activa menos el gen. La explicación es mecanística: como la activación de *rh4* depende de la vía de acetilación, el efector que deposita esa marca de forma directa es más eficaz que el que solo recluta maquinaria. En este sistema, entonces, el efector endógeno y catalítico supera al reclutador sintético.

---

## Slide 7. Reprimir *eba-175*, y la lección de la posición del sgRNA

Guion: El segundo experimento evalúa el sentido inverso, la represión de un gen, con un efector catalítico opuesto. El blanco es *eba-175*, uno de los genes de invasión más expresados en la cepa 3D7, cuyo producto se une al receptor glicoforina A; su nivel elevado de expresión lo hace un buen candidato para medir represión. El sitio de inicio de la transcripción se determinó previamente por 5'-RACE, una técnica que ubica con precisión dónde comienza el ARN mensajero, y sobre ese dato se diseñó el sgRNA que dirige la dCas9-Sir2a a esa región. Los resultados reproducen la cadena anterior en sentido inverso: la inmunoprecipitación con anticuerpo contra la etiqueta confirma que la dCas9 ocupa el sitio; la que emplea anticuerpo contra H3 acetilada muestra ahora hipoacetilación, es decir, la marca fue eliminada; y la RT-qPCR muestra una reducción marcada de *eba-175*, sin cambios en *ama1* ni en la línea control con GFP. En el fenotipo, la represión reduce a menos de la mitad la invasión por la vía que depende de esta proteína. Más allá del detalle biológico, lo relevante para la técnica es que el mismo sistema, cambiando solo el efector, opera con eficacia en el sentido opuesto: activa con GCN5 y reprime con Sir2a, con lecturas moleculares y fenotípicas igual de claras en las dos direcciones.

Este experimento incluye un control del que se desprende el criterio de diseño más relevante del trabajo. Los autores probaron un segundo sgRNA para el mismo gen, ubicado mucho más lejos, a más de mil doscientas bases del sitio de inicio. Ese guía recluta igualmente la dCas9 y modifica parcialmente la acetilación en la zona, de modo que la unión se produce; sin embargo, no reprime el gen con la eficiencia del guía cercano al TSS. La conclusión separa dos hechos que podrían confundirse: que la dCas9 se una a una secuencia no garantiza que el efector tenga efecto. La marca debe depositarse o eliminarse donde influye sobre el inicio de la transcripción, y ese lugar es el entorno inmediato del TSS. De ahí el criterio práctico para diseñar uno de estos sistemas: ubicar el sitio guía lo más cerca posible del inicio de la transcripción del gen blanco.

---

## Slide 8. Reprimir un gen esencial: *PfSET1*

Guion: El tercer experimento lleva la técnica al caso que justifica todo el desarrollo: un gen esencial. *PfSET1* es una histona metiltransferasa necesaria para el estadio asexual del parásito y de función poco conocida, precisamente el tipo de gen que un knockout no permite estudiar, porque su eliminación es letal para el organismo. La represión con dCas9-Sir2a, al ser parcial y reversible, sí lo permite. El primer gráfico, una RT-qPCR como las anteriores, confirma que el sistema reduce la expresión de *PfSET1* en la línea editada respecto de los controles: la herramienta alcanzó su blanco también en este caso.

Como *PfSET1* es un regulador, reprimirlo repercute sobre otros genes, y eso es lo que se rastrea a continuación. Un análisis de secuenciación de ARN, que cuantifica la expresión de todos los genes de manera simultánea, identifica 322 genes cuya expresión disminuye como consecuencia. Para estimar la relevancia de esos genes, los autores recurren a una estrategia indirecta: dado que en *P. falciparum* no es posible generar knockouts de genes esenciales para clasificarlos, utilizan el catálogo ya publicado de una especie hermana, *Plasmodium berghei*, donde esa clasificación se realizó eliminando los genes uno por uno. El gráfico de torta resume esa clasificación de los 322 genes: la mitad son esenciales, un 31 por ciento dispensables y un 19 por ciento de crecimiento lento, es decir, en su mayoría genes relevantes para el parásito.

El siguiente es un mapa de calor, que se lee así: cada fila es un gen y cada columna, uno de ocho momentos del ciclo; el color indica cuánto se expresa ese gen en ese momento, de menos a más. Muestra que el 72 por ciento de los genes esenciales afectados se expresa sobre todo en las etapas tardías, trofozoíto y esquizonte, las formas maduras, lo que anticipa dónde debería notarse el efecto.

El fenotipo lo confirma con el último gráfico, una citometría de flujo. La citometría mide, parásito por parásito, cuánto ADN tiene cada uno mediante un colorante que se une al ADN; como el parásito acumula ADN a medida que madura, esa medición indica en qué punto del ciclo está la población. Comparada con los controles a los mismos tiempos, la línea con *PfSET1* reprimido avanza más lento: presenta un retraso de crecimiento que se inicia en el estadio de trofozoíto, justo donde se expresan los genes afectados, y que no aparece en los controles.

La implicancia es la demostración más fuerte de la potencia de la técnica: es lo bastante robusta como para interrogar genes esenciales, un terreno vedado al knockout, y para traducir una represión parcial en un fenotipo medible, algo que hasta entonces ninguna herramienta resolvía de manera adecuada en este organismo.

---

## Slide 9. Hasta dónde llega la técnica

Guion: Dos rasgos de la técnica quedan por evaluar a escala genómica, su especificidad y su alcance. Para esto se generaron dos gráficos suplementarios. El primero compara los transcriptomas completos por secuenciación de ARN, en un gráfico de dispersión donde cada punto es un gen y los que no cambian caen sobre la diagonal. Casi todos quedan sobre ella: la edición altera pocos genes fuera del blanco. Las únicas excepciones son *pebl*, que se activa junto a *rh4* por compartir un promotor bidireccional, lo que a su vez muestra que la técnica alcanza elementos no codificantes, y *stevor* en la represión; un solo candidato fuera de blanco es la medida de su alta especificidad. El segundo grafica la densidad de sitios PAM en los promotores del genoma: más de 261 mil NGG y 727 mil NGA, cobertura amplia sobre casi todos los cerca de 5.700 genes del parásito. Así, casi cualquier gen es un blanco posible, y la limitación real no es encontrar un sitio, sino ubicarlo cerca del TSS.

---

## Slide 10. La edición no es permanente

Guion: La técnica no modifica el ADN, y su efecto descansa en dos elementos que no perduran. Primero, la dCas9 con su efector se expresa de forma episomal, desde un plásmido que se pierde si no se mantiene. Segundo, la propia marca de acetilación es dinámica: no se copia como la secuencia del ADN, sino que las enzimas de la célula la renuevan y la retiran, así que sin el efector que la deposita revierte al estado basal. Por eso el cambio no es permanente ni se hereda de forma estable entre generaciones. Para estudiar la función de un gen eso no es una desventaja, es justamente lo que lo hace reversible, y delimita su uso: sirve para interrogar un gen, no para un cambio definitivo o heredable, que es el terreno del knockout o de la edición de base y de prime.

---

## Slide 11. Conclusión

Guion: El CRISPR epigenético convierte a la dCas9 en un controlador programable de la expresión génica: en lugar de romper el genoma, dirige a voluntad la actividad de un gen hacia arriba o hacia abajo, sin tocar la secuencia y de forma reversible. Su verdadera potencia está en la modularidad del efector, porque el mismo sistema de direccionamiento puede acoplarse a cualquier actividad que modifique la cromatina, no solo acetilación, sino también metilación de histonas o del ADN, y escribir o borrar la marca que se elija. De ahí un amplio abanico de aplicaciones: estudiar la función de genes, incluidos los esenciales y los no codificantes, sin recurrir a un cambio permanente; reprogramar estados celulares; y, a futuro, intervenir la regulación génica con fines terapéuticos, sin las cicatrices ni los riesgos de un corte en el ADN. El trabajo de Xiao y colaboradores respalda ese potencial al llevar la técnica, por primera vez, a un organismo tan refractario como *Plasmodium falciparum*.

---

## Referencia

Xiao B, Yin S, Hu Y, Sun M, Wei J, Huang Z, Wen Y, Dai X, Chen H, Mu J, Cui L, Jiang L (2019). Epigenetic editing by CRISPR/dCas9 in *Plasmodium falciparum*. *PNAS* 116(1):255-260.
