---
type: informe-general
status: current
date: 2026-07-15
source: "sintesis:dcas9-fto-granulosa:21-preguntas"
related:
  - "[[Notes/dcas9-fto-granulosa/PLAN]]"
  - "[[Notes/dcas9-fto-granulosa/CONCLUSIONES_CLAVE]]"
---

> **Actualización auditada (2026-07-24):** se reforzaron y re-ejecutaron con `citation_audit_status: pass` los notebooks q01/q02/q03/q08/q14 incorporando Hilton et al. (2015), Liao et al. (2026) y Kachanov et al. (2025). La conclusión central se ajusta: sí existe un precedente directo de activación endógena de *FTO* por dCas9-p300 (Kachanov et al., 2025, en HepG2), pero sigue sin existir antecedente en granulosa o en tejido reproductivo. Detalle en [[Notes/dcas9-fto-granulosa/CONCLUSIONES_CLAVE]].
>
> **Actualización consolidada (2026-07-25):** se integraron además los notebooks q15–q21, todos con `citation_audit_status: pass`, incluyendo la reparación local verificada de q20. Esta segunda tanda no cambia la conclusión de viabilidad general, pero sí refina el marco mecanístico: no hay evidencia directa de que la caída de *FTO* en granulosa se explique ya por metilación del promotor, pérdida de H3K27ac o represores promotor-específicos demostrados en esa célula; lo que existe hoy es un conjunto de hipótesis transferibles desde otros tejidos y datasets públicos que todavía requieren validación causal directa en granulosa.

# Activación de FTO vía dCas9-p300 en células de la granulosa humana como estrategia de reversión parcial de la senescencia ovárica

**Informe integrador — Taller de Ingeniería Genética**
**Fecha:** 2026-07-15
**Fuente:** síntesis de 21 investigaciones documentales realizadas con NotebookLM (EZresearchLM), sobre un corpus auditado en dos tandas. Las 14 preguntas originales más las 7 preguntas mecanísticas adicionales (q15–q21) quedaron con auditoría de citas verificada, con la salvedad de que q20 requirió una reparación local verificada de enlaces de fuentes tras una falla transitoria de rerun por DNS/NotebookLM. Cada afirmación de este informe remite a una nota de QA trazable en `GranulosaVault\Notes\NotebookLM\dcas9-fto-granulosa\`.

---

## 1. Resumen ejecutivo

Este informe integra la evidencia recopilada para evaluar la viabilidad de una estrategia de edición epigenómica dirigida — activación transcripcional de *FTO* mediante dCas9-p300 (CRISPRa) en células de la granulosa humana — como intervención para revertir parcialmente la senescencia ovárica asociada a la edad.

La evidencia se organiza en dos bloques que convergen en una misma pregunta de diseño experimental:

- **Bloque A** examina si dCas9-p300 es una herramienta de activación transcripcional suficientemente potente, específica, controlable y comparativamente ventajosa frente a otros activadores CRISPR (VP64, VPR, SunTag).
- **Bloque B** examina si *FTO* es un blanco biológicamente justificado: existe un eje FTO–m6A–FOS bien documentado en granulosa humana (Jiang et al., 2021), FTO decae con la edad mientras que el m6A global aumenta, el estrés oxidativo causa ese decaimiento, y restaurar FTO (por sobreexpresión) revierte marcadores de senescencia y daño al ADN.

**Conclusión central:** la evidencia respalda la lógica de la estrategia — el blanco (FTO) está bien justificado mecanísticamente y dCas9-p300 es una herramienta de activación robusta y bien caracterizada en términos generales — y, tras el refuerzo auditado del corpus, **sí existe un antecedente directo de activación endógena de *FTO* con dCas9-p300, pero fuera del contexto ovárico: Kachanov et al. (2025) en células HepG2**. Sigue sin existir, en el corpus revisado, un antecedente directo en células de la granulosa (KGN, COV434 o primarias) ni en tejido reproductivo. La propuesta es, por tanto, novedosa en su contexto biológico aunque ya no absolutamente inédita como maniobra técnica. La tanda mecanística q15–q21 además delimitó mejor la incertidumbre restante: todavía no está demostrado qué capa promotor-específica explica la caída basal de *FTO* en granulosa envejecida/estresada (metilación, acetilación, ocupación de TFs o accesibilidad). Los mayores vacíos de evidencia están en: eficiencia y especificidad de dCas9-p300 medida en el propio locus de *FTO* en granulosa, controles experimentales co-validados específicamente para este sistema, entrega eficiente de una carga grande (~5–6 kb) en líneas de granulosa, y resolución causal del mecanismo promotor de caída de *FTO*. Estos vacíos no invalidan la estrategia, pero definen exactamente qué experimentos preliminares (proof-of-concept) son indispensables antes de escalar el proyecto.

---

## 2. Introducción y objetivo

El envejecimiento ovárico y la insuficiencia ovárica prematura (POI) se asocian a senescencia de las células de la granulosa, acompañada de un aumento global de la metilación m6A del ARN y una caída de la demetilasa FTO, lo cual estabiliza el ARNm de *FOS* y dispara un programa de envejecimiento celular (Jiang et al., 2021). Este hallazgo abre una hipótesis de intervención: si restaurar farmacológicamente FTO revierte fenotipos de senescencia (Wang et al., 2021a; Zhang et al., 2022b), ¿podría lograrse el mismo efecto de forma más controlada y localizada mediante edición epigenómica dirigida — activando el propio promotor endógeno de *FTO* con un sistema CRISPRa, en lugar de sobreexpresarlo desde un transgén?

dCas9-p300 (Hilton et al., 2015; incorporado y auditado posteriormente en q01–q03) es el activador CRISPR de elección para esta pregunta porque, a diferencia de VP64/VPR, deposita una marca de histona (H3K27ac) en el locus objetivo — es decir, edita el estado epigenético en vez de simplemente reclutar maquinaria transcripcional de forma transitoria.

Dicho esto, la propuesta no debe leerse como una invitación a lanzar un CRISPRa "a ciegas" sobre *FTO*. En el estado actual de la evidencia, antes de fijar definitivamente el efector conviene caracterizar el estado del locus en granulosa envejecida o estresada con un panel mínimo de ensayos epigenéticos: expresión de *FTO* por RT-qPCR/western, metilación del promotor por bisulfito dirigido, marcas de histona por ChIP-qPCR/CUT&RUN/CUT&Tag (al menos H3K27ac, H3K4me3 y H3K27me3), accesibilidad por ATAC-seq y, si emergen candidatos plausibles, ocupación de factores de transcripción o represores en el promotor. Ese mapeo previo no es un refinamiento accesorio: es la forma de distinguir si el locus está hipermetilado, desacetilado, cerrado o privado de activadores, y por lo tanto de decidir con mejor fundamento si p300 solo es suficiente o si haría falta otra estrategia.

El objetivo de este trabajo fue reunir, de forma sistemática y con trazabilidad completa a las fuentes primarias, la evidencia necesaria para diseñar un experimento de activación de *FTO* vía dCas9-p300 en modelos de granulosa humana (KGN, COV434, granulosa primaria), cubriendo tanto la herramienta (dCas9-p300) como el blanco biológico (FTO) y su contexto de senescencia.

---

## 3. Bloque A — Mecanismo de activación transcripcional con dCas9-p300

### 3.1 Eficiencia de activación (q01)

El corpus adquirido para esta pregunta fue el más débil de las 14 investigaciones: de 69 candidatos identificados solo 7 PDFs de acceso abierto resultaron descargables, y varios eran tangenciales (CRISPR en *Arabidopsis*, reprogramación de células madre). El hallazgo cuantitativo principal proviene casi en su totalidad de un único estudio comparativo (Omachi & Miner, 2022): dCas9-p300 alcanza magnitudes de activación de **100 a 300 veces** sobre el nivel basal, dependiendo del gen blanco. La posición de la guía respecto al TSS es un factor crítico de eficiencia, aunque el sistema muestra más flexibilidad posicional que otros activadores. El uso de múltiples guías (multiplexado) mejora significativamente la activación respecto de una guía única, sujeto a restricciones espaciales. La arquitectura del promotor y la accesibilidad de la cromatina local son determinantes fundamentales, porque el sistema actúa modificando directamente el estado epigenético para superar barreras físicas a la transcripción.

**Brecha:** faltan datos sistemáticos de dosis-respuesta, barridos de posición de guía, y comparaciones de arquitectura promotora específicamente para dCas9-p300 (más allá del estudio de Omachi & Miner). No hay ningún dato de eficiencia de activación medido en el locus de *FTO*.

### 3.2 Marca H3K27ac y reversibilidad (q02)

Con un corpus más sólido (11 fuentes), se estableció que dCas9-p300 deposita un enriquecimiento robusto de H3K27ac en promotores y potenciadores dirigidos (Laufer & Singh, 2015; Zhuo et al., 2021; Brocken et al., 2017; Adli, 2018; Park et al., 2016). Esta marca se localiza mayormente en el sitio dirigido, aunque su alcance regulatorio puede extenderse a través de la organización tridimensional del genoma. Crucialmente para el diseño de un experimento controlable: **la marca H3K27ac es transitoria y decae relativamente rápido** una vez que se retira el escritor sintético (dCas9-p300), y la activación transcripcional vuelve a la línea basal — no hay evidencia de "memoria epigenética" fuerte auto-sostenida, a diferencia de otras marcas (Park et al., 2016). La duración de la activación tras retirar el efector depende de la velocidad de aclaramiento del propio efector de la célula. El corpus describe sistemas sofisticados de control temporal (interruptores químicos, módulos fotoactivables, degrones inducibles por fármaco) que permiten "encender y apagar" la actividad de dCas9-p300 en ventanas de tiempo específicas, aunque varían en velocidad y en el nivel de fuga basal ("leakiness") (Kleinjan et al., 2017).

**Brecha:** faltan cinéticas cuantitativas específicas de persistencia y decaimiento de H3K27ac tras la retirada del efector.

### 3.3 Especificidad y efectos fuera de blanco (q03)

Este fue el corpus más débil junto con q01 (9 fuentes, con poca evidencia *directamente* sobre dCas9-p300 y mucha sobre CRISPR-Cas9 nucleasa en general). Los hallazgos disponibles indican que la especificidad de dCas9-p300 depende de la tolerancia a desapareamientos (mismatches) de la guía, sensibilidades de secuencia regionales y accesibilidad de cromatina (Guo et al., 2023). El perfil de especificidad de los activadores basados en fusiones dCas9 difiere sustancialmente del de la edición con Cas9 nucleasa activa: la naturaleza de la modificación genómica, las consecuencias funcionales de la actividad fuera de blanco y los riesgos de toxicidad específicos son distintos (unión sin corte de ADN vs. rotura de doble cadena). Los métodos de perfilado genómico disponibles (ChIP-seq, CUT&RUN, GUIDE-seq, RNA-seq) permiten evaluar tanto la unión física como los efectos transcriptómicos globales.

**Brecha:** aun después del refuerzo con Hilton et al. (2015), la evidencia experimental *directa* sobre especificidad de dCas9-p300 en células humanas sigue siendo escasa frente a la abundante literatura general de off-targets de CRISPR-Cas9. El refuerzo sí mejora materialmente la base empírica: Hilton et al. documenta en HEK293T una activación off-target transcriptómica limitada (dos transcritos por encima del umbral estadístico al dirigir *IL1RN*) y confirma la activación robusta con una sola guía cerca del TSS. La brecha más consecuente pasa a ser la ausencia de datos de especificidad medidos en el locus de *FTO* o en granulosa.

### 3.4 Controles experimentales rigurosos (q11)

Con un corpus de 17 fuentes se estableció un panel de controles estándar en CRISPRa que, combinados, permiten atribuir con rigor la activación observada al mecanismo epigenético dirigido:

- **Guía no dirigida / scrambled**: controla que la activación no derive de componentes del sistema en sí (Cheng et al., 2013; Tycko et al., 2019).
- **Efector catalíticamente inactivo** (p300 muerto, p300CD D1398Y): demuestra que la activación depende de la actividad enzimática y no de la mera unión física del complejo dCas9 al locus (Okada et al., 2017).
- **dCas9 solo, sin efector**: establece la línea basal y confirma que la activación depende del efector reclutado y no de la unión de dCas9 per se — en Cheng et al. (2013), dCas9-activador activó *MSI1* con éxito mientras que dCas9 sin dominio de activación no lo hizo.
- **Guías múltiples independientes, dosis-respuesta y validación ortogonal** son recomendados como controles adicionales para atribución rigurosa (Omachi et al., 2021).
- A escala de cribado (*screening*), se usan capas adicionales de control para distinguir hits verdaderos de artefactos de toxicidad o ruido estadístico (Sanson et al., 2018).

**Brecha:** aunque cada componente individual del panel de controles está validado por separado, **no existe un panel completo y estandarizado co-validado específicamente para dCas9-p300** (a diferencia de VP64/VP64r, donde el panel está mejor consolidado).

### 3.5 Riesgo de desregulación global por activar FTO (q13)

Este bloque conecta directamente el mecanismo (Bloque A) con el blanco biológico (Bloque B): activar *FTO* no es como activar un gen cualquiera, porque FTO actúa como "borrador" (eraser) global de m6A sobre miles de transcritos. El corpus (18 fuentes, sólido) documenta fenotipos no deseados de la desregulación de FTO en tejidos distintos al ovario: déficits de memoria por estrés temprano (Banerjee et al., 2026), disfunción cardíaca (Zhang et al., 2021b), y el vínculo original de FTO con obesidad y fenotipos metabólicos, identificado originalmente por GWAS como el principal factor de susceptibilidad genética a la obesidad y el IMC elevado (Cheung & Li, 2012; Jiang et al., 2021b [rol de m6A]; Wu et al., 2023), incluyendo asociaciones con hiperinsulinemia (Zhang et al., 2021a). Esto crea un riesgo real de efectos pleiotrópicos transcriptoma-amplios si la activación excede el rango fisiológico.

El corpus sí ofrece una vía de mitigación concreta: existen estrategias de control ortogonal de la media y la variabilidad de expresión génica endógena que permiten **titular la activación CRISPRa dentro de un rango fisiológico** en lugar de sobreexpresión suprafisiológica (Bonny et al., 2021) — un antecedente directamente aplicable al diseño de la construcción dCas9-p300 para FTO, por ejemplo mediante promotores inducibles graduables o sistemas de control de dosis del propio efector.

**Brecha:** no hay ningún dato que cuantifique o acote directamente el riesgo de activación suprafisiológica de FTO específicamente vía dCas9-p300 en granulosa — esta es un área que el propio proyecto debería generar experimentalmente (p. ej., RNA-seq global tras activación a distintas dosis, comparado contra el transcriptoma de granulosa envejecida vs. joven).

### 3.6 dCas9-p300 frente a otros activadores: VP64, VPR, SunTag (q14)

Corpus fuerte (17 fuentes), incluyendo un estudio de comparación directa entre complejos activadores dCas9 (Kaba et al., 2025). Los hallazgos clave:

- **Mecanismo**: dCas9-p300 es un *modificador epigenético* (deposita H3K27ac, cambiando el estado de la cromatina), mientras que VP64/VPR son *factores de transcripción sintéticos* que reclutan maquinaria transcripcional sin necesariamente modificar marcas de cromatina (Lo & Qi, 2017).
- **Comparación de magnitud**: dCas9-p300 se compara de forma variable con VP64/VPR según si el blanco es un promotor o un potenciador, y según el gen específico (Kaba et al., 2025).
- **SunTag**: la arquitectura de amplificación de señal SunTag transiciona de una relación 1:1 dCas9-efector a un andamiaje multivalente que recluta muchos efectores por sitio genómico, potenciando la señal y permitiendo ajuste independiente de los componentes del sistema (Swain et al., 2022; Pflueger et al., 2018).
- **Memoria epigenética diferencial**: dCas9-p300 deja una firma funcional distinta a VP64/VPR porque habilita **regulación sostenida a largo plazo** en vez de solo reclutamiento transcripcional inmediato (Kaba et al., 2025) — esto es relevante porque, combinado con el hallazgo de q02 reforzado con Hilton et al. (2015) y Liao et al. (2026), sugiere que la persistencia de la activación depende más de mantener el efector presente que de una "memoria" auto-sostenida por la histona.
- **Dependencia de contexto**: los distintos activadores muestran sensibilidad diferencial al posicionamiento de nucleosomas y al estado de cromatina activa vs. silente en el locus blanco.

**Brecha crítica**: el corpus sigue sin ofrecer una comparación cabeza-a-cabeza de dCas9-p300 contra VP64, VPR o SunTag específicamente en el locus de *FTO*. Sin embargo, tras incorporar Kachanov et al. (2025), ya no es correcto afirmar ausencia total de información sobre *FTO*: existe al menos un precedente directo de activación endógena de *FTO* con dCas9-p300 en HepG2, aunque no comparativo y fuera del contexto de granulosa.

---

## 4. Bloque B — Eje FTO–m6A–FOS y senescencia en granulosa

### 4.1 Evidencia del eje FTO–m6A–FOS (q04)

El corpus (16 fuentes) confirmó y contextualizó ampliamente el hallazgo seminal de Jiang et al. (2021, *Cell Death & Disease*): la demetilasa m6A FTO en células de la granulosa retarda el envejecimiento ovárico dependiente de *FOS*. El mecanismo propuesto: FTO desmetila el ARNm de *FOS* (m6A), lo cual **desestabiliza** ese transcrito; cuando FTO decae, el m6A de *FOS* aumenta, el ARNm se estabiliza y se acumula, disparando el programa de senescencia. El estudio original usó muestras clínicas humanas, líneas de granulosa y una batería de técnicas de biología molecular y alto rendimiento. Más allá del estudio original, el corpus identifica soporte independiente y contexto ampliado en Li et al. (2024) (FTO regula el envejecimiento de la granulosa vía MMP2/ERK), Zhu et al. (2024) (FTO estabiliza circBRCA1 exosomal, vía miR-642a-5p/FOXO1, aliviando daño por estrés oxidativo), y revisiones de Sun et al. (2022b) y Shi et al. (2023, POI). Los controles experimentales usados por Jiang et al. (2021) para demostrar especificidad m6A-FOS incluyeron manipulación de FTO (knockdown/sobreexpresión) — documentados en detalle en la nota de QA correspondiente.

### 4.2 FTO y m6A en función de la edad (q05)

Corpus muy fuerte (22 fuentes, incluyendo el paper de multi-ómica de núcleo único de Jin et al., 2025, *Nature Aging*). Confirmación cuantitativa y direccional clara: **FTO disminuye significativamente con la edad** en ovario y granulosa, mientras que el **nivel global de m6A aumenta significativamente** con la edad (Jiang et al., 2021c [zhongxin]; Shi et al., 2023). Los estudios de multi-ómica de célula única/núcleo único de envejecimiento ovárico humano caracterizan un declive celular acelerado, cambios en vías de señalización, y una desregulación específica del epitranscriptoma m6A impulsada por la pérdida de FTO (Jin et al., 2025). El corpus también documenta en detalle las técnicas de cuantificación disponibles (MeRIP-seq/m6A-seq de mapeo transcriptómico amplio hasta ensayos bioquímicos sitio-específicos), con sus compensaciones de resolución y sensibilidad, y las limitaciones técnicas conocidas de MeRIP-seq (baja reproducibilidad, sesgos de anticuerpo, confusión estadística) (McIntyre et al., 2020).

**Brecha:** la relación FTO↓/m6A↑ con la edad está bien establecida a nivel de tendencia general, pero faltan mediciones cuantitativas, sitio-específicas y estratificadas por edad, hechas *específicamente* en células de la granulosa humanas (a diferencia de otros tipos celulares ováricos u otros tejidos).

### 4.3 Estrés oxidativo, FTO y senescencia (ROS→FTO↓→senescencia) (q06)

Corpus bueno (19 fuentes tras el ajuste). El eje causal **ROS/H₂O₂ → FTO↓ → m6A↑ → FOS↑ → senescencia** cuenta con **evidencia causal directa** (no solo correlativa), mediante experimentos de pérdida de función y rescate, principalmente en células de la granulosa humanas (Jiang et al., 2021c). La señalización de Nrf2 actúa como puente crítico entre el estrés oxidativo y la regulación de m6A, promoviendo protección celular o permitiendo senescencia según su estado (Zhang et al., 2025 [helou]; Guo et al., 2022 [jun]; Xie et al., 2020; Shi et al., 2023). Existe evidencia específica de esta relación en granulosa humana, además de observaciones similares (menos detalladas) en osteoblastos y tejido cardíaco (Zhang et al., 2025; Zhao et al., 2021).

**Brecha:** persisten preguntas abiertas sobre la cadena causal completa específicamente en células somáticas ováricas (más allá de granulosa) y sobre umbrales cuantitativos de ROS que disparan el decaimiento de FTO.

### 4.4 Métodos de cuantificación m6A sitio-específica sobre el 3'UTR de FOS (q07)

Corpus fuerte (24 fuentes) que caracteriza en detalle los tres métodos solicitados:

- **MeRIP-qPCR** (m6A-IP-qPCR): cuantifica enriquecimiento relativo de ARN m6A en regiones específicas de un transcrito; se usa para validar hallazgos de MeRIP-seq o investigar genes candidatos puntuales (Ci et al., 2024; Yu et al., 2021).
- **SELECT**: técnica de amplificación qPCR basada en elongación y ligación de base única, para cuantificación sitio-específica de m6A en residuos de adenosina puntuales (Xu et al., 2025).
- **miCLIP**: logra resolución de nucleótido único combinando inmunoprecipitación con entrecruzamiento UV (McIntyre et al., 2020; Chen et al., 2020).
- **Ensayos de pulso con actinomicina D (ActD)**: método estándar para medir estabilidad de ARNm y calcular vida media de transcritos específicos, permitiendo determinar cómo la modificación m6A (y sus escritores/lectores/borradores) influye en la tasa de degradación (Cheng et al., 2024; Jiang et al., 2021c; Ci et al., 2024).

Las limitaciones técnicas y sesgos conocidos (especificidad de anticuerpos, falsos positivos, límites de resolución) están bien documentados para estos métodos en general.

**Brecha:** el corpus no reporta métodos específicamente validados sobre el **3'UTR de *FOS*** en particular — la aplicación de MeRIP-qPCR/SELECT/miCLIP a este transcrito puntual, más allá del contexto general de envejecimiento ovárico e infarto de miocardio, queda como trabajo por hacer.

### 4.5 Restauración de FTO y reversión de fenotipos (q08)

Corpus muy fuerte (23 fuentes) con hallazgos directamente aplicables al proyecto. La sobreexpresión de FTO protege a las células de la granulosa humanas actuando como **proteína retardadora de senescencia** que revierte desórdenes epigenéticos y restaura la homeostasis celular (Jiang et al., 2021c). Mecanísticamente, FTO desestabiliza el ARNm de *FOS* (relacionado con envejecimiento), estabiliza *MMP2* activando la vía ERK (Li et al., 2024), y estabiliza *MIS12* contrarrestando la senescencia (Zhang et al., 2022b). Los mecanismos se dividen en dependientes e independientes de m6A. Existen antecedentes de reversión de fenotipos de envejecimiento ovárico mediante intervenciones celulares/moleculares (células madre mesenquimales de médula ósea revierten el perfil de metilación m6A del ARN asociado a envejecimiento ovárico en células de la granulosa envejecidas — Tian et al., 2023), consistentemente identificando la restauración de FTO como mecanismo central de estos efectos protectores.

Sobre **daño al ADN**: la restauración de FTO (sobreexpresión o estabilización funcional) **disminuye** significativamente los niveles de marcadores de daño al ADN o protege a las células de su acumulación.

Las intervenciones para restaurar FTO se agrupan en tres enfoques: **sobreexpresión directa** (transgén/plásmido — la mayoría de la evidencia disponible), **edición epigenética sitio-específica** (CRISPRa — sin ejemplos reportados en el corpus), e **indirectos** (exosomas de células madre, moléculas pequeñas — p. ej. vitamina C, Chong et al., 2019).

**Brecha crítica y central para este proyecto:** tras incorporar Kachanov et al. (2025), el corpus ya no sostiene una ausencia total de restauración/activación de *FTO* mediante edición epigenética/CRISPRa: existe un precedente directo en HepG2 donde dCas9-p300 activa *FTO* endógeno con efecto biológico aguas abajo. Aun así, toda la evidencia de **reversión de fenotipos de senescencia en granulosa** sigue proviniendo de sobreexpresión por transgén o de intervenciones indirectas; no hay todavía un precedente CRISPRa en granulosa. La novedad del proyecto del Taller se mantiene, pero queda acotada al contexto reproductivo/ovárico y al fenotipo de senescencia.

### 4.6 Marcadores de senescencia y daño al ADN (q09)

Corpus aceptable (8 fuentes tras el ajuste). Se estableció el panel estándar solicitado:

- **SA-β-galactosidasa**: ensayo citoquímico ampliamente usado para identificar células senescentes detectando actividad de β-galactosidasa mediante sustrato cromogénico X-Gal.
- **p16 (CDKN2A) y p21 (CDKN1A)**: biomarcadores primarios e inhibidores de quinasas dependientes de ciclina que indican arresto del ciclo celular permanente e irreversible; la supresión de p16 alivia el fenotipo secretor asociado a senescencia (SASP) (Buj et al., 2020).
- **γH2AX**: indicador primario de roturas de doble cadena de ADN, mediante fosforilación de H2AX en serina-139 por quinasas ATM/ATR (Stefanou et al., 2015; Tanabe et al., 2014).
- Estos marcadores se han aplicado específicamente en modelos de células de la granulosa de ratón, ovocitos fetales y envejecimiento ovárico, aunque de forma fragmentada respecto al contexto único del ovario humano.

**Lectura esperable ante una reversión parcial**: no se manifestaría como una normalización uniforme de todos los biomarcadores, sino como un **desacople del estado senescente** — por ejemplo, reducción de la actividad secretora (SASP) mientras persisten elevados algunos marcadores de arresto del ciclo, o mejora en la eficiencia de reparación de ADN sin eliminación completa de la población senescente. Este matiz es importante para interpretar correctamente resultados de un experimento de activación parcial de FTO.

### 4.7 Sistemas de entrega para dCas9-p300 (q10)

Corpus bueno (11 fuentes). Para cargas grandes tipo dCas9-p300 (~5–6 kb), los principales desafíos giran en torno a restricciones de empaquetamiento, estabilidad coloidal y barreras celulares de entrada/escape (comparado con cargos CRISPR estándar más pequeños). Se han usado plataformas de magnetofección, vectores virales, sistemas lipídicos y exosomas modificados para constructos dCas9 (Ghanbarlou et al., 2021; Meneghini et al., 2021; Duan et al., 2021). Para líneas derivadas de granulosa (KGN, COV434) y otras células primarias/tipo madre difíciles de transfectar, se identifican como enfoques principales la transducción lentiviral, magnetofección, electroporación y entrega basada en exosomas (Jamour et al., 2024). Basado en el corpus, el **ARNm encapsulado en nanopartículas lipídicas (LNP)** ofrece el mejor balance general entre alta eficiencia y mínima perturbación celular para un efector CRISPRa grande como dCas9-p300.

**Brecha:** el corpus discute la mecánica general de efectores CRISPR grandes y experimentos en granulosa de rata, pero **carece de datos específicos en los modelos humanos KGN, COV434 o granulosa primaria humana** para la entrega de dCas9-p300 en particular.

### 4.8 Antecedentes de rejuvenecimiento epigenómico con CRISPRa/CRISPRi (q12)

Corpus fuerte (16 fuentes), incluyendo un antecedente directamente relevante en su título: "Rejuvenation of cells by epigenetic editing" (Wang & Pei, 2018). Se documentan enfoques de CRISPRa/CRISPRi y fusiones dCas9 relacionadas usados para revertir marcadores de envejecimiento y rejuvenecer funciones celulares modulando expresión génica sin alterar la secuencia de ADN subyacente (Caobi et al., 2020; Zhang et al., 2021c). Mecanísticamente, la edición epigenética dirigida representa una filosofía de **modulación específica** de impulsores puntuales del envejecimiento, en contraste con el **"reinicio global"** de la reprogramación celular tipo factores de Yamanaka (Simpson et al., 2021). Este trabajo se ha demostrado *in vivo* (no solo en cultivo) en tejidos como corazón, hígado y páncreas (Chatterjee et al., 2024; Ji et al., 2023).

**Hallazgo crítico y explícito:** el corpus establece de forma directa que **no hay ninguna aplicación reportada de edición epigenómica (CRISPRa/CRISPRi) específicamente para rejuvenecimiento de tejido reproductivo** (ovario, testículo, granulosa) — esta es la brecha de literatura más clara y contundente de todo el corpus, y confirma que el proyecto propuesto se encuentra en territorio genuinamente inexplorado dentro de la medicina reproductiva, aunque con precedente metodológico sólido en otros tejidos.

---

## 5. Bloque C — Mecanismo promotor del silenciamiento de FTO (q15)

### 5.1 Metilación del promotor de FTO

No existe en el corpus de q15 evidencia directa de que la metilación del ADN en el promotor de FTO o en una isla CpG proximal explique la caída de su transcripción bajo estrés oxidativo, envejecimiento o contexto ovárico. Este dato es informativo y no meramente negativo, puesto que las mismas fuentes que trabajan sobre granulosa sí midieron metilación de promotores en otros genes del mismo tejido: el caso verificado contra pasaje literal es la hipometilación del promotor de AR en granulosa de pacientes con síndrome de ovario poliquístico (PCOS), con el consiguiente aumento de expresión (Desmawati et al., 2018). Cabe aclarar que las respuestas de q15 consignan además hipermetilación pronunciada de los promotores de Atg5 y LC3B en ovario de rata envejecida, atribuida a Yamada et al. (2025), y un aumento de la metilación del promotor de LEP por liraglutida en granulosa de pacientes con PCOS y obesidad, atribuido a Su et al. (2025), pero ninguna de esas dos afirmaciones se ancla a un pasaje verbatim del corpus (del trabajo sobre leptina solo se extrajo el título, de modo que ni siquiera la dirección del efecto queda verificada), razón por la cual no se las toma aquí como dato. Ninguna de estas fuentes aporta, en cualquier caso, secuenciación por bisulfito ni un método equivalente aplicado sobre el locus de FTO en granulosa; la metilación del promotor de FTO permanece, en consecuencia, como una hipótesis sin verificación directa en el tejido de interés.

### 5.2 Acetilación de histonas y desacetilasas

Tampoco hay evidencia ni una propuesta explícita de que la pérdida de H3K27ac o la desacetilación mediada por HDACs en el promotor de FTO expliquen su caída en granulosa o en modelos de estrés oxidativo. El corpus sí documenta acetilación de histonas en el ovario, pero referida a otros loci: H3K27ac en el locus de Traf2, con efecto sobre la proliferación de células madre germinales femeninas, y descenso de H3K9ac y H3K27ac en el ovario de la generación F1 tras exposición a cromo hexavalente, junto con un aumento de expresión de DNMT3a y DNMT3b y apoptosis folicular (Li et al., 2025b). Ninguna fuente reporta ChIP-seq ni ChIP-qPCR sobre el promotor de FTO en granulosa, de modo que esta vía queda, al igual que la metilación, en el terreno de la hipótesis transferida desde otros loci del mismo tejido.

### 5.3 Factores de transcripción y ausencia de represores identificados

Esta es la única vía con apoyo relativamente directo, aunque conviene precisar con exactitud su alcance. SP1 aparece como activador positivo que induce la transcripción de FTO, y su pérdida bajo estrés oxidativo se propone como causa del descenso. Cabe aclarar, no obstante, que en los extractos verbatim de q15 esa afirmación no se ancla a datos primarios sino a una entrada de la lista de referencias de una revisión (Li et al., 2026), que remite a su vez a Chen et al. (2024, FASEB J 38(20):e70118), donde FTO activado transcripcionalmente por SP1 mejora la injuria renal aguda por isquemia-reperfusión mediante autofagia dependiente de Ambra1/ULK1; se trata de una cita secundaria, no incorporada al corpus auditado, que además corresponde a un trabajo distinto del "Chen et al., 2024" ya presente en la bibliografía consolidada. Corresponde corregir aquí que el tejido de esa demostración es riñón y no cardiomiocito, dado que varias respuestas de q15 lo consignaron erróneamente como cardiomiocito. Asimismo, la misma afirmación sobre SP1 aparece atribuida a cuatro fuentes distintas según la respuesta de q15 que se consulte (Wang et al., 2020; Li et al., 2026; Kordowitzki et al., 2024; Kuai et al., 2026), lo que indica un desajuste del mapeo entre cita y fuente en la exportación y no una confirmación independiente múltiple.

Sobre C/EBPα, en el contexto del oncometabolito R-2HG en leucemia mieloide aguda se reporta que la supresión de CEBPA inhibe la transcripción de FTO; el pasaje anclado describe además la cascada FTO/m6A/MYC/CEBPA, en la que FTO opera aguas arriba y reduce la estabilidad de los transcritos de MYC y CEBPA, de modo que la direccionalidad no queda unívoca dentro de la misma fuente (Wang et al., 2020). La pregunta q16 aportó por separado evidencia de unión directa de C/EBPα al promotor de FTO, también en leucemia mieloide aguda y contextos metabólicos, no en granulosa. Sobre el receptor de andrógenos, su activación se asocia a un aumento de FTO en granulosa de pacientes con PCOS, en una retroalimentación positiva que agrava el hiperandrogenismo (Kuai et al., 2026). El punto central de este apartado es que ninguna fuente identifica un represor que se una al promotor de FTO; el descenso se describe consistentemente como pérdida de activación y no como represión activa.

### 5.4 Variantes de secuencia en el locus de FTO

No hay reportes de mutaciones promotoras, variantes cis-regulatorias ni alteraciones estructurales que silencien o reduzcan la transcripción de FTO en granulosa ni en ningún otro tejido. La única variante consistentemente citada, rs9939609, es intrónica (se ubica en el primer intrón), se asocia a susceptibilidad a PCOS y a mayor androgenemia, y en granulosa de pacientes con PCOS se vincula a FTO aumentado y no silenciado (Kuai et al., 2026; European Society of Human Genetics, 2022). Este es el matiz más incómodo que aporta q15 al marco del proyecto y debe quedar señalado como tal: la única evidencia de nivel genómico específica de granulosa apunta en dirección opuesta a la caída de FTO que motiva la intervención, puesto que proviene de un contexto patológico distinto (PCOS) al del envejecimiento ovárico.

### 5.5 Qué queda demostrado y qué no

Conviene distinguir explícitamente dos niveles de evidencia. A nivel fenotípico la evidencia es fuerte y convergente: FTO disminuye en ARNm y en proteína en granulosa humana con la edad, en insuficiencia ovárica prematura, bajo peróxido de hidrógeno, bajo cadmio y tras cisplatino o ciclofosfamida (Wang et al., 2021a; Zhu et al., 2024; Yu et al., 2024; Shi et al., 2023; Liu et al., 2023b; Kuai et al., 2026). A nivel promotor, en cambio, la evidencia es nula: no hay ChIP ni bisulfito sobre el promotor de FTO en granulosa, la mayor parte de los datos disponibles proviene de modelos murinos de insuficiencia ovárica prematura y de la línea inmortalizada KGN, y una de las fuentes señala explícitamente que la verificación en ovario humano in vivo está limitada por los requisitos clínicos y éticos de acceso a muestras (Wang et al., 2021a). El experimento discriminante que queda pendiente consiste en separar el silenciamiento epigenético activo (metilación o desacetilación) de la pérdida pasiva de activación (pérdida de unión de SP1), lo que exige una aproximación de multi-ómica integrada sobre el promotor de FTO en granulosa humana (Li et al., 2025b).

Corresponde dejar asentado un problema de trazabilidad detectado al contrastar las afirmaciones de q15 contra los pasajes literales del corpus, puesto que se trata de un desajuste sistemático entre cita y fuente en la exportación y no de un error aislado. Se identificaron cuatro casos. Dos afirmaciones carecen de anclaje verbatim localizable en cualquier archivo del corpus: la hipermetilación de los promotores de Atg5 y LC3B, y la acetilación diferencial de los promotores de StAR y Cyp19a1. Otras dos son reales pero figuraban bajo la fuente equivocada: el efecto del cromo hexavalente sobre la acetilación de histonas, que pertenece a Li et al. (2025b) y aparecía atribuido a Liu et al. (2023a), y la cascada R-2HG/CEBPA, que pertenece a Wang et al. (2020) y aparecía atribuida a Kuai et al. (2026). A esto se suma la cuádruple atribución de la afirmación sobre SP1 ya descrita. La consecuencia operativa es directa: el estado `pass` de la auditoría automática de citas no protege contra esta clase de error, porque verifica que los enlaces resuelvan dentro del vault y no que la afirmación corresponda a la fuente enlazada; ergo, toda afirmación de q15 que se traslade al informe del Obligatorio debe contrastarse previamente contra su pasaje literal.

### 5.6 Consecuencia sobre la elección del editor epigenético

Lo que sigue debe leerse como una inferencia de diseño y no como un hecho ya demostrado. Si el mecanismo dominante fuese la pérdida de activación y no el silenciamiento activo por metilación, un editor desmetilante del tipo dCas9-TET1 carecería de sustrato que revertir, mientras que un escritor de acetilación como p300 opera por una vía compatible con reponer la activación perdida. A esto se agrega un argumento de robustez: p300 no depende de cuál sea la causa basal, puesto que impone la marca activadora aguas abajo de cualquiera de los mecanismos candidatos. El contrapunto honesto es que, si el mecanismo real resultara ser una hipermetilación densa del promotor, la eficiencia de p300 podría quedar limitada por la accesibilidad de la cromatina, factor ya identificado como determinante en el apartado 3.1; en ese escenario, un editor combinado del tipo TET1 más p300 pasaría a ser preferible. Ergo, el mapeo del promotor de FTO en granulosa no es un experimento accesorio sino una decisión de diseño previa a la elección del editor.

---

## 6. Síntesis integradora: viabilidad de activar FTO vía dCas9-p300 en granulosa

Integrando ambos bloques, la cadena lógica de la estrategia propuesta queda así:

```
Edad ↑ → estrés oxidativo (ROS) ↑ → FTO ↓ (evidencia causal directa, q06)
       → m6A global ↑ y m6A en FOS ↑ (q05, q07)
       → ARNm de FOS estabilizado ↑ (q04)
       → senescencia + daño al ADN en granulosa (q04, q09)

Intervención propuesta: dCas9-p300 dirigido al promotor endógeno de FTO
       → activación transcripcional local (q01: 100-300x en otros genes)
       → depósito de H3K27ac, reversible al retirar el efector (q02)
       → restaura FTO → desestabiliza FOS → revierte senescencia
         (extrapolado de q08: sobreexpresión de FTO ya demostrado que hace esto)
```

**Lo que la evidencia respalda con solidez:**
1. El blanco biológico (FTO) está mecanísticamente bien justificado y su restauración (por sobreexpresión, no aún por CRISPRa) ya demostró revertir senescencia y daño al ADN en granulosa humana (q08).
2. dCas9-p300 es una herramienta de activación potente (100–300x) y reversible al retirar el efector (q01, q02), con un repertorio de sistemas de control temporal disponibles.
3. Existen estrategias conocidas para titular la activación CRISPRa dentro de un rango fisiológico, mitigando el riesgo de desregulación pleiotrópica de FTO (q13).
4. Existen sistemas de entrega viables (LNP-mRNA como mejor balance; lentivirus/electroporación como alternativas) aplicables en principio a líneas de granulosa (q10).
5. Existe un panel de controles experimentales estándar (guía no dirigida, efector catalíticamente muerto, dCas9 solo) para atribuir rigurosamente el efecto (q11).

**Lo que constituye la novedad real del proyecto (no hay antecedente directo):**
1. No existe ningún estudio en granulosa o tejido reproductivo que haya activado el locus de *FTO* con dCas9-p300 ni con otro activador CRISPR; sí existe un precedente fuera de ese contexto, Kachanov et al. (2025), en HepG2.
2. No hay antecedentes de restauración de FTO mediante edición epigenética/CRISPRa en granulosa ni asociados a reversión de senescencia ovárica — la evidencia fenotípica sigue siendo por sobreexpresión de transgén o intervenciones indirectas (q08), aunque ya no puede hablarse de ausencia absoluta de CRISPRa sobre *FTO*.
3. No hay antecedentes de edición epigenómica CRISPRa/CRISPRi aplicada a rejuvenecimiento de tejido reproductivo (q12).
4. No hay datos de eficiencia, especificidad o entrega de dCas9-p300 específicamente en KGN, COV434 o granulosa primaria humana (q03, q10).

Esto no es una debilidad del proyecto — es, de hecho, su justificación como aporte original: se trata de aplicar una herramienta madura (dCas9-p300) a un blanco validado (FTO) en un contexto (granulosa humana, senescencia ovárica) que la literatura no ha explorado todavía. El riesgo experimental reside en la ejecución (eficiencia real, especificidad real, magnitud de reversión real en este locus y este tipo celular), no en la lógica del diseño.

### 6.1 Refinamiento mecanístico posterior (q15–q21)

La segunda tanda de preguntas no alteró la conclusión de viabilidad del proyecto, pero sí estrechó con más precisión la hipótesis mecanística que conviene tratar como modelo de trabajo y separó con claridad lo demostrado de lo plausible.

1. **q15 — mecanismo promotor de silenciamiento de FTO:** ninguna de las vías candidatas (metilación del promotor, pérdida de H3K27ac por HDACs, variantes cis o un represor promotor-específico) quedó demostrada en granulosa humana; la única con apoyo relativamente directo es la pérdida de activación transcripcional (SP1) extrapolada con cautela desde otros tejidos. El desarrollo completo, incluidas las salvedades de trazabilidad de esa cita y sus consecuencias de diseño, se presenta en el Bloque C (§5).
2. **q16 — C/EBPα en el promotor de FTO:** sí existe evidencia de unión directa de C/EBPα al promotor de *FTO*, pero sobre todo en AML y contextos metabólicos; no en granulosa. La extrapolación a pérdida de *FTO* por estrés oxidativo en granulosa es débil e indirecta.
3. **q17 — metilación del promotor de FTO en otros tejidos:** la metilación del promotor de *FTO* sí está descrita como regulador transcripcional en obesidad y trastornos metabólicos, pero no como mecanismo ya demostrado específicamente para estrés oxidativo, envejecimiento ovárico o granulosa. Además, el corpus no identifica una DNMT o TET concreta como regulador directo del promotor de *FTO*.
4. **q18 — analogía con ALKBH5:** el promotor de **ALKBH5** muestra regulación transcripcional real en contextos reproductivos e hipóxicos, pero la extrapolación a *FTO* es incompleta porque ambos "erasers" no responden igual a estrés y envejecimiento.
5. **q19 — genes comparables como Klotho/SIRT1:** el patrón comparativo más fuerte para genes antienvejecimiento es un silenciamiento epigenético tripartito por hipermetilación, unión de represores y reclutamiento de HDACs. Ese patrón genera una hipótesis plausible para *FTO* en granulosa, pero sigue siendo una hipótesis de trabajo, no una demostración directa.
6. **q20 — otros tejidos con caída de FTO:** fuera de granulosa, el corazón/cardiomiocito es el tejido con evidencia más concreta de caída de *FTO* bajo estrés oxidativo y daño metabólico, con puentes hacia mecanismos de cromatina, actividad de factores de transcripción y metilación. La auditoría de q20 quedó finalmente en `pass` tras reparar localmente los `Sources` links rotos y verificar que todos resolvían dentro del vault.
7. **q21 — datasets públicos ChIP-seq/ATAC-seq:** existen datasets públicos (ENCODE, Cistrome y afines) que perfilan el locus/promotor de *FTO* y permiten generar hipótesis mecanísticas útiles sobre marcas de cromatina, accesibilidad y factores de transcripción candidatos. Sin embargo, esos datasets todavía son evidencia de contexto regulatorio y no prueba causal de por qué cae *FTO* en granulosa envejecida; exigen validación funcional específica en granulosa.

En conjunto, q15–q21 endurecen la interpretación: la propuesta de activar *FTO* con dCas9-p300 sigue bien justificada, pero la causa promotor-específica de la caída basal de *FTO* en granulosa permanece abierta. Por lo tanto, el proyecto no sólo debe probar rescate fenotípico, sino también resolver qué capa regulatoria (metilación, acetilación, TFs, accesibilidad) gobierna realmente el promotor de *FTO* en ese contexto.

### 6.2 Chequeo puntual posterior sobre Kachanov (QA auxiliar 2026-07-25)

Se ejecutó además una QA auxiliar específica en NotebookLM para preguntar si Kachanov et al. (2025) aportaba evidencia directa sobre por qué *FTO* estaría basalmente bajo o reprimido, y cuáles de sus resultados constituían el mejor indicio de transferibilidad hacia un proyecto en granulosa. Esa QA terminó con `citation_audit_status: pass`, pero el notebook auxiliar no recuperó a Kachanov entre las fuentes finalmente citadas. En consecuencia, este paso no añadió soporte trazable nuevo para reinterpretar a Kachanov como evidencia del estado represivo del promotor de *FTO*.

La conclusión metodológicamente más honesta permanece entonces sin cambios: Kachanov sigue siendo útil como antecedente de factibilidad técnica — activación endógena de *FTO* con efecto biológico downstream en una célula humana — pero no como demostración de por qué *FTO* cae o permanece reprimido en granulosa. Dicho de otro modo, refuerza la plausibilidad de que el efector pueda funcionar; no resuelve el mecanismo basal que el proyecto todavía necesita mapear.

### Diseño experimental sugerido (derivado directamente de las brechas identificadas)

1. **Prueba de concepto de activación**: transfectar dCas9-p300 + guías dirigidas al promotor de *FTO* en KGN/COV434, con el panel completo de controles (q11) y medir activación de FTO por qPCR/western, siguiendo el diseño de multiplexado de guías de Omachi & Miner (2022).
2. **Verificación mecanística**: confirmar que la activación de FTO reduce m6A en el 3'UTR de *FOS* (MeRIP-qPCR o SELECT, q07) y reduce la estabilidad/abundancia del ARNm de *FOS* (ensayo con actinomicina D).
3. **Verificación fenotípica**: medir el panel de senescencia (SA-β-gal, p16, p21, γH2AX, q09) esperando un desacople parcial, no normalización completa, en un modelo de granulosa envejecida/estresada oxidativamente (H₂O₂, q06).
4. **Control de dosis y especificidad**: usar un sistema de activación titulable (Bonny et al., 2021) y perfilar el transcriptoma global (RNA-seq) para descartar activación suprafisiológica de FTO y sus efectos pleiotrópicos (q13).
5. **Entrega**: evaluar ARNm-LNP como primera opción por su balance eficiencia/perturbación (q10), con lentivirus como alternativa de respaldo.

---

## 7. Limitaciones y brechas de evidencia transversales

- **Corpus aún selectivo en q01 y q03**: el refuerzo con Hilton et al. (2015) mejoró de forma material la base empírica sobre eficiencia y especificidad, pero la evidencia sigue descansando en pocos estudios comparativos y de caracterización directa. Ya no queda como tarea pendiente de biblioteca; sí permanece como limitación de amplitud del estado del arte.
- **Ausencia total de datos sobre el locus de FTO** en la literatura de comparación de activadores CRISPR (q14) y de especificidad (q03): esto es esperable dado que la propuesta es novedosa, pero implica que cualquier estimación de eficiencia/especificidad en este proyecto será la primera de su tipo.
- **Causa promotor-específica aún no resuelta para la caída de FTO en granulosa**: la segunda tanda q15–q21 dejó claro que ni la metilación del promotor, ni la pérdida de H3K27ac, ni la ocupación de C/EBPα, ni los datos públicos de cromatina alcanzan todavía para establecer un mecanismo causal único en granulosa. Hoy sólo existe un espacio de hipótesis priorizadas (detalle en el Bloque C, §5). A esto se agregan tres precisiones. Primero, la única evidencia de nivel genómico específica de granulosa (la variante rs9939609 en contexto de PCOS) se asocia a FTO aumentado y no a su caída, por lo que no sirve como modelo de la pérdida de FTO que motiva el proyecto. Segundo, la vía mejor apoyada dentro del corpus, la activación por SP1, descansa sobre una cita secundaria dentro de una revisión (Li et al., 2026, que remite a Chen et al., 2024, FASEB J) y no sobre datos primarios incorporados al corpus auditado. Tercero, el estado `pass` de la auditoría de citas de q15 verifica que los enlaces a fuentes resuelvan dentro del vault, no que la atribución de cada afirmación a su fuente sea correcta; el contraste contra los pasajes literales mostró que en q15 el desajuste entre cita y fuente es sistemático y no puntual, con dos afirmaciones sin anclaje verbatim, dos atribuidas a la fuente equivocada y una (la activación de FTO por SP1) atribuida a cuatro fuentes distintas según la respuesta consultada, según se detalla en el Bloque C.
- **Necesidad de caracterización epigenética previa al diseño del efector**: dado que no está resuelto si la caída de *FTO* responde a metilación del promotor, pérdida de H3K27ac, cierre cromatínico o pérdida de activadores, el proyecto requiere un paso previo explícito de caracterización del locus antes de interpretar un CRISPRa como ensayo mecanístico. El panel mínimo razonable incluye bisulfito dirigido del promotor, ChIP-qPCR/CUT&RUN/CUT&Tag para H3K27ac-H3K4me3-H3K27me3, accesibilidad por ATAC-seq y medición de ocupación de TFs candidatos. Sin esa capa previa, cualquier resultado de activación con p300 sería informativo en términos operativos, pero ambiguo en términos de mecanismo causal.
- **Ausencia de antecedentes CRISPRa/CRISPRi en tejido reproductivo** (q12): no hay literatura de la que extrapolar directamente parámetros de dosis o cinética esperables en ovario/granulosa; los antecedentes más cercanos son de corazón, hígado y páncreas.
- **Fragmentación de marcadores de senescencia en el contexto ovárico humano específico** (q09): el panel está bien validado en general, pero rara vez co-validado como panel único en granulosa humana.
- **Limitaciones metodológicas conocidas de los métodos m6A** (MeRIP-seq: baja reproducibilidad, sesgo de anticuerpo) deben tenerse en cuenta al diseñar la verificación mecanística (q05, q07).
- Dos preguntas (q06, q13) requirieron degradar de obligatoria a opcional una fuente puntual que resultó genuinamente bajo paywall sin ruta de acceso abierto (Gao et al., 2025 sobre Nrf2/m6A en núcleo pulposo, y Kachanov et al., 2025 sobre m6A y VHB); el corpus recuperado cubre igualmente bien las preguntas subyacentes mediante fuentes alternativas.

---

## 8. Conclusiones

1. FTO es un blanco terapéutico mecanísticamente sólido para revertir senescencia en granulosa humana: su decaimiento con la edad y con estrés oxidativo está bien documentado, y su restauración (aunque solo probada por sobreexpresión, no por CRISPRa en granulosa) ya revierte marcadores de senescencia y daño al ADN.
2. dCas9-p300 es una herramienta de activación transcripcional madura, potente y controlable temporalmente, con un marco de controles experimentales establecido y estrategias conocidas para acotar el riesgo de sobreactivación.
3. La combinación específica — dCas9-p300 dirigido a *FTO* en granulosa humana — no tiene antecedente directo en la literatura relevada para granulosa o tejido reproductivo. El proyecto del Taller constituiría, de ejecutarse, la primera demostración de este enfoque en ese contexto biológico, aunque ya no la primera activación absoluta de *FTO* por dCas9-p300 en células humanas.
4. Las brechas identificadas (especificidad de dCas9-p300 en el locus de FTO, entrega eficiente en KGN/COV434, panel de controles co-validado, umbral fisiológico vs. suprafisiológico de activación de FTO, y mecanismo promotor-causal de la caída basal de *FTO* en granulosa) definen directamente los experimentos preliminares necesarios antes de avanzar a un diseño a mayor escala.

---

## 9. Bibliografía consolidada

*Fuentes citadas a lo largo de este informe, ordenadas alfabéticamente por primer autor. Metadatos (autores, año, DOI) extraídos automáticamente de los registros de búsqueda bibliográfica del pipeline EZresearchLM; no se han generado citas de memoria.*

- **Adli, 2018** — Mazhar Adli (2018). *The CRISPR tool kit for genome editing and beyond*. DOI: 10.1038/s41467-018-04252-2.
- **Ahmad et al., 2026** — Rizwan Ahmad; Mohammad Yusuf Hasan (2026). *Deciphering Reactive Oxygen Species with Cutting-Edge Aging Research*. DOI: 10.5772/intechopen.1014497.
- **Asgarpour et al., 2020** — Kasra Asgarpour et al. (2020). *Exosomal microRNAs derived from mesenchymal stem cells: cell-to-cell messages*. DOI: 10.1186/s12964-020-00650-6.
- **Banerjee et al., 2026** — Dipanjana Banerjee et al. (2026). *FTO-dependent m6A RNA dysregulation underlies memory deficits induced by early-life stress*. DOI: 10.64898/2026.03.30.715262.
- **Bao et al., 2024** — Shenglan Bao; Tailang Yin; Su Liu (2024). *Ovarian aging: energy metabolism of oocytes*. DOI: 10.1186/s13048-024-01427-y.
- **Bennett et al., 2020** — Neal K. Bennett et al. (2020). *Defining the ATPome reveals cross-optimization of metabolic pathways*. DOI: 10.1038/s41467-020-18084-6.
- **Bonny et al., 2021** — Alain R. Bonny et al. (2021). *Orthogonal control of mean and variability of endogenous genes in a human cell line*. DOI: 10.1038/s41467-020-20467-8.
- **Borch et al., 2021** — Borch Jensen M; Marblestone A (2021). *In vivo Pooled Screening: A Scalable Tool to Study the Complexity of Aging and Age-Related Disease*. DOI: 10.3389/fragi.2021.714926.
- **Brocken et al., 2017** — Daan J.W. Brocken; Mariliis Tark-Dame; Remus T. Dame (2017). *dCas9: A Versatile Tool for Epigenome Editing*. DOI: 10.21775/cimb.026.015.
- **Brunet et al., 2022** — Anne Brunet; Margaret A. Goodell; Thomas A. Rando (2022). *Ageing and rejuvenation of tissue stem cells and their niches*. DOI: 10.1038/s41580-022-00510-w.
- **Buj et al., 2020** — Raquel Buj; Kelly E. Leon; Katherine M. Aird (2020). *Suppression of p16 alleviates the senescence-associated secretory phenotype*. DOI: 10.1101/2020.08.19.257717.
- **Caobi et al., 2020** — Allen Caobi et al. (2020). *The Impact of CRISPR-Cas9 on Age-related Disorders: From Pathology to Therapy*. DOI: 10.14336/ad.2019.0927.
- **Cecchino et al., 2021** — Gustavo Nardini Cecchino; Juan A. García-Velasco; Eduardo Rial (2021). *Reproductive senescence impairs the energy metabolism of human granulosa cells*. DOI: 10.1101/2021.03.11.434795.
- **Chatterjee et al., 2024** — Chatterjee S et al. (2024). *Telomerase is essential for cardiac differentiation and sustained metabolism of human cardiomyocytes*. DOI: 10.1007/s00018-024-05239-7.
- **Chaudhary et al., 2021** — Namit Chaudhary; Drew Weissman; Kathryn A. Whitehead (2021). *mRNA vaccines for infectious diseases: principles, delivery and clinical translation*. DOI: 10.1038/s41573-021-00283-5.
- **Chen et al., 2020** — Mengnuo Chen; Chun-Ming Wong (2020). *The emerging roles of N6-methyladenosine (m6A) deregulation in liver carcinogenesis*. DOI: 10.1186/s12943-020-01172-y.
- **Chen et al., 2023** — Ronghao Chen et al. (2023). *Enhancement of a prime editing system via optimal recruitment of the pioneer transcription factor P65*. DOI: 10.1038/s41467-023-35919-0.
- **Chen et al., 2024** — Yunbing Chen; Ziyu Zhou; Yanxi Chen; Di Chen (2024). *Reading the m6A-encoded epitranscriptomic information in development and diseases*. DOI: 10.1186/s13578-024-01293-7.
- **Cheng et al., 2013** — Albert W. Cheng et al. (2013). *Multiplexed activation of endogenous genes by CRISPR-on, an RNA-guided transcriptional activator system*. DOI: 10.1038/cr.2013.122.
- **Cheng et al., 2024** — Hao Cheng et al. (2024). *METTL3 drives heart failure by regulating Spp1 and Fos m6A modification in myocardial infarction*. DOI: 10.21203/rs.3.rs-4207910/v1.
- **Cheung & Li, 2012** — Bernard M.Y. Cheung; Chao Li (2012). *Diabetes and Hypertension: Is There a Common Metabolic Pathway?*. DOI: 10.1007/s11883-012-0227-2.
- **Chong et al., 2019** — Taylor Lee Chong; Emily L. Ahearn; Luisa Cimmino (2019). *Reprogramming the Epigenome With Vitamin C*. DOI: 10.3389/fcell.2019.00128.
- **Choudhari et al., 2026** — Neha Choudhari et al. (2026). *A novel method for the identification and quantification of N6-methyladenosine motifs in RNA transcripts*. DOI: 10.1007/s11033-026-12270-3.
- **Ci et al., 2024** — Ci Y; Zhang Y; Zhang X (2024). *Methylated lncRNAs suppress apoptosis of gastric cancer stem cells via the lncRNA-miRNA/protein axis*. DOI: 10.1186/s11658-024-00568-8.
- **Dabrowska et al., 2018** — Magdalena Dabrowska et al. (2018). *Precise Excision of the CAG Tract from the Huntingtin Gene by Cas9 Nickases*. DOI: 10.3389/fnins.2018.00075.
- **Desmawati et al., 2018** — Desmawati; Ririn Rahmala Febri; Andon Hestiantoro; Asmarinah (2018). *DNA methylation of the androgen receptor gene promoter in the granulosa cells of polycystic ovary syndrome patients*. DOI: 10.1088/1742-6596/1073/3/032078.
- **Ding et al., 2025** — Ding F et al. (2025). *The interplay of cellular senescence and reprogramming shapes the biological landscape of aging and cancer*. DOI: 10.3389/fcell.2025.1593096.
- **Domenico et al., 2017** — Emanuela De Domenico et al. (2017). *Overactive type 2 cannabinoid receptor induces meiosis in fetal gonads and impairs ovarian reserve*. DOI: 10.1038/cddis.2017.496.
- **Duan et al., 2021** — Li Duan et al. (2021). *Nanoparticle Delivery of CRISPR/Cas9 for Genome Editing*. DOI: 10.3389/fgene.2021.673286.
- **European Society of Human Genetics, 2022** — Abstracts from the 54th European Society of Human Genetics (ESHG) Conference (2022). DOI: 10.1038/s41431-021-01026-1.
- **Fu et al., 2025** — Yujuan Fu et al. (2025). *Dynamic properties of transcriptional condensates modulate CRISPRa-mediated gene activation*. DOI: 10.1038/s41467-025-56735-8.
- **Ghanbarlou et al., 2021** — Mahdi Mohammadi Ghanbarlou et al. (2021). *Delivery of dCas9 CRISPR System Into the Hard Transfection Cells by Magnetofection Approach*. DOI: 10.21203/rs.3.rs-999842/v1.
- **Ginley-Hidinger et al., 2019** — Matthew Ginley-Hidinger et al. (2019). *Sufficiency analysis of estrogen responsive enhancers using synthetic activators*. DOI: 10.26508/lsa.201900497.
- **Gough et al., 2023** — Gough OJ et al. (2023). *Dissection of a non-coding risk locus at 1p36.23 identifies ERRFI1 as a novel gene in the pathogenesis of psoriasis and psoriatic arthritis*. DOI: 10.1101/2023.12.04.569945.
- **Guo et al., 2022** — Jun Guo et al. (2022). *Aging and aging-related diseases: from molecular mechanisms to interventions and treatments*. DOI: 10.1038/s41392-022-01251-0.
- **Guo et al., 2023** — Congting Guo; Xiaoteng Ma; Fei Gao; Yuxuan Guo (2023). *Off-target effects in CRISPR/Cas9 gene editing*. DOI: 10.3389/fbioe.2023.1143157.
- **Han et al., 2023a** — Julie Han et al. (2023). *CRISPRi gene modulation and all-optical electrophysiology in post-differentiated human iPSC-cardiomyocytes*. DOI: 10.1038/s42003-023-05627-y.
- **Han et al., 2023b** — Julie Han; Emilia Entcheva (2023). *Gene Modulation with CRISPR-based Tools in Human iPSC-Cardiomyocytes*. DOI: 10.1007/s12015-023-10506-4.
- **He et al., 2019** — Liuer He et al. (2019). *Functions of N6-methyladenosine and its role in cancer*. DOI: 10.1186/s12943-019-1109-9.
- **Hendra et al., 2022** — Christopher Hendra et al. (2022). *Detection of m6A from direct RNA sequencing using a multiple instance learning framework*. DOI: 10.1038/s41592-022-01666-1.
- **Hilton et al., 2015** — Isaac B. Hilton et al. (2015). *Epigenome editing by a CRISPR-Cas9-based acetyltransferase activates genes from promoters and enhancers*. Nature Biotechnology 33:510–517. DOI: 10.1038/nbt.3199. *(Referencia fundacional del sistema dCas9-p300; incorporada posteriormente al corpus reforzado de q01/q02/q03.)*
- **Huang et al., 2020** — Hongxin Huang et al. (2020). *Cell-cell contact-induced gene editing/activation in mammalian cells using a synNotch-CRISPR/Cas9 system*. DOI: 10.1007/s13238-020-00690-1.
- **Huang et al., 2023** — Erqing Huang; Lijuan Chen (2023). *RNA N6-methyladenosine modification in female reproductive biology and pathophysiology*. DOI: 10.1186/s12964-023-01078-4.
- **Hunt et al., 2021** — Charleen Hunt et al. (2021). *Tissue-specific activation of gene expression by the Synergistic Activation Mediator (SAM) CRISPRa system in mice*. DOI: 10.1038/s41467-021-22932-4.
- **Jamour et al., 2024** — Parisa Jamour et al. (2024). *Comparing Chemical Transfection, Electroporation, and Lentiviral Vector Transduction to Achieve Optimal Transfection Conditions in the Vero Cell Line*. DOI: 10.21203/rs.3.rs-3894744/v1.
- **Jean-Baptiste, 1970** — Quetsia Jean-Baptiste. *Senescence And The Senescence Associated Secretory Phenotype In Salivary Hypofunction*. DOI: 10.54014/2f5r-h13w.
- **Ji et al., 2023** — Shuaifei Ji et al. (2023). *Cellular rejuvenation: molecular mechanisms and potential therapeutic interventions for diseases*. DOI: 10.1038/s41392-023-01343-5.
- **Jiang et al., 2021** — Jiang ZX; Wang YN; Li ZY; Dai ZH; He Y; Chu K; Gu JY; Ji YX; Sun NX; Yang F; Li W (2021). *The m6A mRNA demethylase FTO in granulosa cells retards FOS-dependent ovarian aging*. Cell Death & Disease 12:744. DOI: 10.1038/s41419-021-04016-9. PMID: 34315853.
- **Jiang et al., 2021b** — Xiulin Jiang et al. (2021). *The role of m6A modification in the biological functions and diseases*. DOI: 10.1038/s41392-020-00450-x.
- **Jin et al., 2025** — Chen Jin et al. (2025). *Molecular and Genetic Insights Into Human Ovarian Aging From Single-Nuclei Multi-omics Analyses*. Nature Aging. DOI: 10.1097/ogx.0000000000001382.
- **Jin et al., 2026** — Jin Z et al. (2026). *FTO-mediated m6A demethylation regulates PGC-1α-dependent mitochondrial biogenesis to attenuate aluminum-induced neuronal senescence*. DOI: 10.1038/s41598-026-51674-w.
- **Kaba et al., 2025** — Fatma Akçakale Kaba et al. (2025). *Comparison of dCas9-activator complexes for the activation of PDX1 and NGN3 pancreatic genes using the CRISPR system*. DOI: 10.23902/trkjnat.1622077.
- **Kachanov et al., 2025** — Aleksandr V. Kachanov et al. (2025). *The m6A methylation system limits hepatitis B virus replication*. DOI: 10.18097/PBMCR1509. PMID: 40326019.
- **Kan et al., 2021** — Lijuan Kan et al. (2021). *A neural m6A/Ythdf pathway is required for learning and memory in Drosophila*. DOI: 10.1038/s41467-021-21537-1.
- **Kim et al., 2023** — Jae Ho Kim; Stephen L. Brown; Marcia N. Gordon (2023). *Radiation-induced senescence: therapeutic opportunities*. DOI: 10.1186/s13014-022-02184-2.
- **Kleinjan et al., 2017** — Dirk A. Kleinjan et al. (2017). *Drug-tunable multidimensional synthetic gene control using inducible degron-tagged dCas9 effectors*. DOI: 10.1038/s41467-017-01222-y.
- **Kordowitzki et al., 2024** — Kordowitzki P; Graczyk S; Haghani A; Klutstein M (2024). *Oocyte Aging: A Multifactorial Phenomenon in A Unique Cell*. DOI: 10.14336/ad.2023.0527.
- **Kuai et al., 2026** — Kuai Y; Yi Y; Li X; Wang Z; Zheng Y; Li Y; Li Y (2026). *Unravelling Multilayered RNA Modification Networks in Female Reproduction*. DOI: 10.3390/biom16040571.
- **Laufer & Singh, 2015** — Benjamin I. Laufer; Shiva M. Singh (2015). *Strategies for precision modulation of gene expression by epigenome editing: an overview*. DOI: 10.1186/s13072-015-0023-7.
- **Liao et al., 2026** — Wenbo Liao et al. (2026). *HDAC2-mediated H3K27ac governs ZFP42 transcription and autophagy in granulosa cells of pigs*. DOI: 10.1016/j.lfs.2026.124527.
- **Li et al., 2020** — Hongyi Li et al. (2020). *Applications of genome editing technology in the targeted therapy of human diseases: mechanisms, advances and prospects*. DOI: 10.1038/s41392-019-0089-y.
- **Li et al., 2023a** — Tianxiang Li et al. (2023). *CRISPR/Cas9 therapeutics: progress and prospects*. DOI: 10.1038/s41392-023-01309-7.
- **Li et al., 2023b** — Xia Li et al. (2023). *Inflammation and aging: signaling pathways and intervention therapies*. DOI: 10.1038/s41392-023-01502-8.
- **Li et al., 2024** — Li L / Linshuang Li et al. (2024). *Fat Mass and Obesity-Associated Protein Regulates Granulosa Cell Aging by Targeting Matrix Metalloproteinase-2 Gene Via an N6-Methyladenosine-YTHDF2-Dependent Pathway in Aged Mice*. DOI: 10.1007/s43032-024-01632-6. PMID: 38995602.
- **Li et al., 2025a** — Chunhong Li et al. (2025). *Cellular senescence: from homeostasis to pathological implications and therapeutic strategies*. DOI: 10.3389/fimmu.2025.1534263.
- **Li et al., 2025b** — Li J; Liao Q; Guo Y; Zhang J; Zhang R; Liu Q; Liu H (2025). *Mechanism of crosstalk between DNA methylation and histone acetylation in ovarian aging*. DOI: 10.1080/15592294.2025.2528563.
- **Li et al., 2026** — Li L; Sun Y; Zheng W; Li L; Feng Y; Qi M; Li H (2026). *The Role of N6-Methyladenosine Modification in Health and Disease*. DOI: 10.1002/mco2.70767.
- **Liu et al., 2019** — Yang Liu; Xinyi Wan; Baojun Wang (2019). *Engineered CRISPRa enables programmable eukaryote-like gene activation in bacteria*. DOI: 10.1038/s41467-019-11479-0.
- **Liu et al., 2022** — Chang Liu et al. (2022). *Transcriptome-wide N6-methyladenine methylation in granulosa cells of women with decreased ovarian reserve*. DOI: 10.1186/s12864-022-08462-3.
- **Liu et al., 2023a** — Ruochen Liu et al. (2023). *Methylation across the central dogma in health and diseases: new therapeutic strategies*. DOI: 10.1038/s41392-023-01528-y.
- **Liu et al., 2023b** — Liu S; Jia Y; Meng S; Luo Y; Yang Q; Pan Z (2023). *Mechanisms of and Potential Medications for Oxidative Stress in Ovarian Granulosa Cells*. DOI: 10.3390/ijms24119205.
- **Lo & Qi, 2017** — Albert Lo; Lei S. Qi (2017). *Genetic and epigenetic control of gene expression by CRISPR-Cas systems*. DOI: 10.12688/f1000research.11113.1.
- **Lu, 2025** — Yibing Lu (2025). *Brain-Targeted Nano delivery System for CRISPRa-Mediated Activation of the Arc Gene in Alzheimer's Disease*. DOI: 10.54097/7axcw386.
- **Luo et al., 2023** — Zhiyuan Luo et al. (2023). *Exon-intron boundary inhibits m6A deposition, enabling m6A distribution hallmark, longer mRNA half-life and flexible protein coding*. DOI: 10.1038/s41467-023-39897-1.
- **Mahata et al., 2023** — Mahata B et al. (2023). *Compact engineered human mechanosensitive transactivation modules enable potent and versatile synthetic transcriptional control*. DOI: 10.1038/s41592-023-02036-1.
- **McIntyre et al., 2020** — Alexa B. R. McIntyre et al. (2020). *Limits in the detection of m6A changes using MeRIP/m6A-seq*. DOI: 10.1038/s41598-020-63355-3.
- **Melnik, 2015** — Bodo C. Melnik (2015). *Milk: an epigenetic amplifier of FTO-mediated transcription? Implications for Western diseases*. DOI: 10.1186/s12967-015-0746-z.
- **Meneghini et al., 2021** — Vasco Meneghini et al. (2021). *Delivery Platforms for CRISPR/Cas9 Genome Editing of Glial Cells in the Central Nervous System*. DOI: 10.3389/fgeed.2021.644319.
- **Muela-Zarzuela et al., 2024** — Inés Muela-Zarzuela et al. (2024). *NLRP1 inflammasome promotes senescence and senescence-associated secretory phenotype*. DOI: 10.1007/s00011-024-01892-7.
- **Nombela et al., 2021** — Paz Nombela; Borja Miguel-López; Sandra Blanco (2021). *The role of m6A, m5C and Ψ RNA modifications in cancer: Novel therapeutic opportunities*. DOI: 10.1186/s12943-020-01263-w.
- **Okada et al., 2017** — Masahiro Okada et al. (2017). *Stabilization of Foxp3 expression by CRISPR-dCas9-based epigenome editing in mouse primary T cells*. DOI: 10.1186/s13072-017-0129-1.
- **Omachi et al., 2021** — Kohei Omachi; Jeffrey H. Miner (2021). *Comparative Analysis and Rational Design of dCas9-VP64 Variants for CRISPR Activation* (preprint). DOI: 10.1101/2021.08.13.456279.
- **Omachi et al., 2022** — Kohei Omachi; Jeffrey H. Miner (2022). *Comparative analysis of dCas9-VP64 variants and multiplexed guide RNAs mediating CRISPR activation*. DOI: 10.1371/journal.pone.0270008.
- **Paixão et al., 2019** — Joaquin Felipe Roca Paixão et al. (2019). *Improved drought stress tolerance in Arabidopsis by CRISPR/dCas9 fusion with a Histone AcetylTransferase*. DOI: 10.1038/s41598-019-44571-y.
- **Panigrahi & O'Malley, 2021** — Anil K. Panigrahi; Bert W. O'Malley (2021). *Mechanisms of enhancer action: the known and the unknown*. DOI: 10.1186/s13059-021-02322-1.
- **Papikian et al., 2019** — Ashot Papikian et al. (2019). *Site-specific manipulation of Arabidopsis loci using CRISPR-Cas9 SunTag systems*. DOI: 10.1038/s41467-019-08736-7.
- **Park et al., 2016** — Minhee Park; Albert J. Keung; Ahmad S. Khalil (2016). *The epigenome: the next substrate for engineering*. DOI: 10.1186/s13059-016-1046-5.
- **Peterson et al., 2022** — Jackson J. Peterson et al. (2022). *A histone deacetylase network regulates epigenetic reprogramming and viral silencing in HIV infected cells*. DOI: 10.1101/2022.05.09.491199.
- **Pflueger et al., 2018** — Christian Pflueger et al. (2018). *A modular dCas9-SunTag DNMT3A epigenome editing system overcomes pervasive off-target activity of direct fusion dCas9-DNMT3A constructs*. DOI: 10.1101/266130.
- **Price et al., 2020** — Alexander M. Price et al. (2020). *Direct RNA sequencing reveals m6A modifications on adenovirus RNA are necessary for efficient splicing*. DOI: 10.1038/s41467-020-19787-6.
- **Puri et al., 2016** — Pawan Puri et al. (2016). *Protein Kinase A: A Master Kinase of Granulosa Cell Differentiation*. DOI: 10.1038/srep28132.
- **Qiu et al., 2023** — Lei Qiu et al. (2023). *RNA modification: mechanisms and therapeutic targets*. DOI: 10.1186/s43556-023-00139-x.
- **Reddi, 2025** — Honey V. Reddi (2025). *Editorial: Genetics and epigenetics in ovarian aging*. DOI: 10.3389/fendo.2025.1555914.
- **Safari et al., 2019** — Fatemeh Safari et al. (2019). *CRISPR Cpf1 proteins: structure, function and implications for genome editing*. DOI: 10.1186/s13578-019-0298-7.
- **Sanson et al., 2018** — Kendall R Sanson et al. (2018). *Optimized libraries for CRISPR-Cas9 genetic screens with multiple modalities*. DOI: 10.1038/s41467-018-07901-8.
- **Schüller et al., 2020** — Andreas Schüller et al. (2020). *Activation of silent secondary metabolite gene clusters by nucleosome map-guided positioning of the synthetic transcription factor VPR-dCas9*. DOI: 10.1101/2020.04.02.022053.
- **Sgro et al., 2023** — Agustin Sgro et al. (2023). *Epigenetic reactivation of tumor suppressor genes with CRISPRa technologies as precision therapy for hepatocellular carcinoma*. DOI: 10.1186/s13148-023-01482-0.
- **Shi et al., 2023** — Yuqian Shi et al. (2023). *Premature ovarian insufficiency: a review on the role of oxidative stress and the application of antioxidants*. DOI: 10.3389/fendo.2023.1172481.
- **Simpson et al., 2021** — Daniel J. Simpson; Nelly Olova; Tamir Chandra (2021). *Cellular reprogramming and epigenetic rejuvenation*. DOI: 10.1186/s13148-021-01158-7.
- **Stefanou et al., 2015** — Dimitra Stefanou et al. (2015). *Aberrant DNA Damage Response Pathways May Predict the Outcome of Platinum Chemotherapy in Ovarian Cancer*. DOI: 10.1371/journal.pone.0117654.
- **Su et al., 2025** — Lina Su; Xiaoxia Hao; Wenhong Lu (2025). *Effects of Liraglutide on Leptin Promoter Methylation in Ovarian Granulosa Cells*. DOI: 10.1620/tjem.2025.j009.
- **Sun et al., 2022a** — Jin Sun et al. (2022). *The Potential Role of m6A RNA Methylation in the Aging Process and Aging-Associated Diseases*. DOI: 10.3389/fgene.2022.869950.
- **Sun et al., 2022b** — Sun X; Lu J; Li H; Huang B (2022). *The Role of m6A on Female Reproduction and Fertility: From Gonad Development to Ovarian Aging*. DOI: 10.3389/fcell.2022.884295. PMID: 35712673.
- **Swain et al., 2022** — Tessa Swain et al. (2022). *A modular dCas9-based recruitment platform for combinatorial epigenome editing*. DOI: 10.1101/2022.07.01.498378.
- **Tak & Farnham, 2015** — Yu Gyoung Tak; Peggy Farnham (2015). *Making sense of GWAS: using epigenomics and genome engineering to understand the functional relevance of SNPs in non-coding regions of the human genome*. DOI: 10.1186/s13072-015-0050-4.
- **Tanabe et al., 2014** — Manabu Tanabe et al. (2014). *Melatonin protects the integrity of granulosa cells by reducing oxidative stress in nuclei, mitochondria, and plasma membranes in mice*. DOI: 10.1262/jrd.2014-105.
- **Tang et al., 2019** — Zehan Tang et al. (2019). *Nrf2 drives oxidative stress-induced autophagy in nucleus pulposus cells via a Keap1/Nrf2/p62 feedback loop to protect intervertebral disc from degeneration*. DOI: 10.1038/s41419-019-1701-3.
- **Tian et al., 2023** — Chuan Tian et al. (2023). *Bone Marrow Mesenchymal Stem Cells Reversed Ovarian Aging-related m6A RNA Methylation Modification Profile in Aged Granulosa Cells*. DOI: 10.1007/s12015-022-10485-y.
- **Trojanowski et al., 2021** — Jorge Trojanowski et al. (2021). *Transcription activation is enhanced by multivalent interactions independent of phase separation*. DOI: 10.1101/2021.01.27.428421.
- **Tycko et al., 2019** — Josh Tycko et al. (2019). *Mitigation of off-target toxicity in CRISPR-Cas9 screens for essential non-coding elements*. DOI: 10.1038/s41467-019-11955-7.
- **Uzonyi et al., 2023** — Anna Uzonyi et al. (2023). *Exclusion of m6A from splice-site proximal regions by the exon junction complex dictates m6A topologies and mRNA stability*. DOI: 10.1016/j.molcel.2022.12.026.
- **Walther, 1970** — Johanna Walther. *Lipid Nanoparticle-Mediated Delivery of CRISPR-Cas9 for Therapeutic Gene Correction*. DOI: 10.33540/2032.
- **Wang & Pei, 2018** — Tao Wang; Duanqing Pei (2018). *Rejuvenation of β cells by epigenetic editing*. DOI: 10.1172/jci124583.
- **Wang et al., 2020** — Tianyi Wang; Shan Kong; Mei Tao; Shaoqing Ju (2020). *The potential role of RNA N6-methyladenosine in Cancer progression*. DOI: 10.1186/s12943-020-01204-7.
- **Wang et al., 2021a** — Rongli Wang; Xinyuan Yang (2021). *Overexpression of FTO Protects Human Granulosa Cells From Cisplatin-Induced Injury*. DOI: 10.21203/rs.3.rs-929583/v1.
- **Wang et al., 2021b** — Yanhua Wang et al. (2021). *Role of Hakai in m6A modification pathway in Drosophila*. DOI: 10.1038/s41467-021-22424-5.
- **Weltner et al., 2018** — Jere Weltner et al. (2018). *Human pluripotent reprogramming with CRISPR activators*. DOI: 10.1038/s41467-018-05067-x.
- **Wen et al., 2025** — Jianting Wen et al. (2025). *New insights into the role of cellular senescence and rheumatic diseases*. DOI: 10.3389/fimmu.2025.1557402.
- **Wu et al., 2023** — Yanlin Wu et al. (2023). *Epigenetic regulation in metabolic diseases: mechanisms and advances in clinical study*. DOI: 10.1038/s41392-023-01333-7.
- **Xie et al., 2020** — Na Xie et al. (2020). *NAD+ metabolism: pathophysiologic mechanisms and therapeutic potential*. DOI: 10.1038/s41392-020-00311-7.
- **Xu et al., 2025** — Xin Xu; Yujuan Wang (2025). *SELECT-based quantification of site-specific m6A modification*. DOI: 10.17504/protocols.io.q26g77rzqgwz/v1.
- **Yamada et al., 2025** — Yamada K; Ito M; Nunomura H; Nishigori T; Furuta A; Yoshida M; Yamaki A; Shozu K; Yasuda I; Tsuda S; Shima T; Nakashima A (2025). *Interplay of Oxidative Stress, Autophagy, and Rubicon in Ovarian Follicles*. DOI: 10.3390/antiox14080919.
- **Yang et al., 2022** — Yang Yang et al. (2022). *Chronic corticosterone disrupts the circadian rhythm of CRH expression and m6A RNA methylation in the chicken hypothalamus*. DOI: 10.1186/s40104-022-00677-4.
- **Yang et al., 2023** — Jingang Yang et al. (2023). *Exosome-targeted delivery of METTL14 regulates NFATc1 m6A methylation levels to correct osteoclast-induced bone resorption*. DOI: 10.1038/s41419-023-06263-4.
- **Yao et al., 2021** — Yingpeng Yao et al. (2021). *METTL3-dependent m6A modification programs T follicular helper cell differentiation*. DOI: 10.1038/s41467-021-21594-6.
- **Yu et al., 2021** — Jie Yu et al. (2021). *Histone lactylation drives oncogenesis by facilitating m6A reader protein YTHDF2 expression in ocular melanoma*. DOI: 10.1186/s13059-021-02308-z.
- **Yu et al., 2024** — Xinru Yu et al. (2024). *The role of epigenetics in women's reproductive health: the impact of environmental factors*. DOI: 10.3389/fendo.2024.1399757.
- **Zhang et al., 2017** — Xia Zhang et al. (2017). *miR-22 suppresses tumorigenesis and improves radiosensitivity of breast cancer cells by targeting Sirt1*. DOI: 10.1186/s40659-017-0133-8.
- **Zhang et al., 2021a** — Anni Zhang et al. (2021). *Hyperinsulinemia in Obesity, Inflammation, and Cancer*. DOI: 10.4093/dmj.2020.0250.
- **Zhang et al., 2021b** — Beijian Zhang et al. (2021). *m6A demethylase FTO attenuates cardiac dysfunction by regulating glucose uptake and glycolysis in mice with pressure overload-induced heart failure*. DOI: 10.1038/s41392-021-00699-w.
- **Zhang et al., 2021c** — Huimin Zhang et al. (2021). *Application of the CRISPR/Cas9-based gene editing technique in basic research, diagnosis, and therapy of cancer*. DOI: 10.1186/s12943-021-01431-6.
- **Zhang et al., 2022a** — Lei Zhang et al. (2022). *Cellular senescence: a key therapeutic target in aging and diseases*. DOI: 10.1172/jci158450.
- **Zhang et al., 2022b** — Sheng Zhang et al. (2022). *FTO stabilizes MIS12 and counteracts senescence*. DOI: 10.1007/s13238-022-00914-6.
- **Zhang et al., 2024** — Xiaoyu Zhang et al. (2024). *Ginger inhibits the invasion of ovarian cancer cells SKOV3 through CLDN7, CLDN11 and CD274 m6A methylation modifications*. DOI: 10.1186/s12906-024-04431-3.
- **Zhang et al., 2025** — Helou Zhang et al. (2025). *Narrowband ultraviolet B radiation attenuates nucleus pulposus pyroptosis to ameliorate intervertebral disc degeneration by activating NRF2/KEAP1 antioxidant pathway*. DOI: 10.3389/fimmu.2025.1663674.
- **Zhao et al., 2021** — Fanpeng Zhao et al. (2021). *METTL3-dependent RNA m6A dysregulation contributes to neurodegeneration in Alzheimer's disease through aberrant cell cycle events*. DOI: 10.1186/s13024-021-00484-x.
- **Zhu et al., 2020** — Song Zhu et al. (2020). *An oncopeptide regulates m6A recognition by the m6A reader IGF2BP1 and tumorigenesis*. DOI: 10.1038/s41467-020-15403-9.
- **Zhu et al., 2021** — Xudong Zhu et al. (2021). *Inflammation, epigenetics, and metabolism converge to cell senescence and ageing: the regulation and intervention*. DOI: 10.1038/s41392-021-00646-9.
- **Zhu et al., 2024** — Xiaolan Zhu / Zhu X et al. (2024). *M6A demethylase FTO-stabilized exosomal circBRCA1 alleviates oxidative stress-induced granulosa cell damage via the miR-642a-5p/FOXO1 axis*. DOI: 10.1186/s12951-024-02583-5. PMID: 38918838.
- **Zhuang et al., 2023** — Xingxing Zhuang et al. (2023). *Overexpression of FTO inhibits excessive proliferation and promotes the apoptosis of human glomerular mesangial cells by alleviating FOXO6 m6A modification via YTHDF3-dependent mechanisms*. DOI: 10.3389/fphar.2023.1260300.
- **Zhuo et al., 2021** — Chenya Zhuo et al. (2021). *Spatiotemporal control of CRISPR/Cas9 gene editing*. DOI: 10.1038/s41392-021-00645-w.
- **Xiaoyan et al., 2022** — *The role of m6A on female reproduction and* [título parcial; metadatos bibliográficos completos no resueltos automáticamente]. Citado en q05 (FTO/m6A vs. edad).

---

*Este informe fue generado a partir de 21 pipelines de investigación EZresearchLM (NotebookLM). Las 14 preguntas originales y las 7 preguntas mecanísticas adicionales quedaron auditadas con estado `pass`; en q20 ese estado final se consolidó mediante reparación local verificada de enlaces de fuentes tras una falla transitoria de red en el rerun. Las notas de origen, con pasajes exactos y enlaces a los PDF fuente, están disponibles en `GranulosaVault\Notes\NotebookLM\dcas9-fto-granulosa\<pregunta>\QA\`.*
