---
type: maestro-obligatorio
status: current
date: 2026-07-25
source: "sintesis:dcas9-fto-granulosa + 02_obligatorio/consigna_y_rubrica.md + 02_obligatorio/rubrica_detallada.md"
related:
  - "[[Notes/dcas9-fto-granulosa/INFORME_GENERAL]]"
  - "[[Notes/dcas9-fto-granulosa/CONCLUSIONES_CLAVE]]"
---

# Maestro de elaboración del Obligatorio (activación de FTO vía dCas9-p300 en granulosa humana)

Archivo de trabajo, no entregable. Fija el criterio de foco, mapea la rúbrica contra el material disponible y registra qué falta producir. La fuente de verdad del contenido científico sigue siendo `INFORME_GENERAL.md`; la de la consigna, `02_obligatorio/consigna_y_rubrica.md` y `02_obligatorio/rubrica_detallada.md`.

---

## 1. Criterio de foco (decisión de Naza, 2026-07-25)

Lo que se evalúa es el diseño CRISPR. Todo el corpus documental de las 21 preguntas de investigación es contexto argumentativo: sirve para justificar por qué el diseño es el que es, y no se evalúa por sí mismo. La consigna lo dice de forma explícita ("se valorará especialmente el detalle, la complejidad, la justificación y la claridad del diseño experimental") y la rúbrica lo confirma repartiendo 11 de 30 puntos entre Metodología y Resultados.

Consecuencia operativa. El esfuerzo se asigna en este orden: primero producir los artefactos de diseño que hoy no existen (guías, mapas, construcción, anexos), después seleccionar del corpus el mínimo material de justificación necesario, y solo al final refinar la redacción de contexto. La profundidad del corpus es un activo para la defensa oral y para la sección de discusión, no un contenido a volcar completo en diez carillas.

Corolario sobre el mecanismo promotor. La causa exacta de la caída de *FTO* en granulosa envejecida no está resuelta y no hace falta resolverla para que el diseño se sostenga. Lo que sí debe quedar escrito es que su elucidación es un ensayo previo del propio diseño y no una laguna bibliográfica que se disimula. Ver el Bloque C de `INFORME_GENERAL.md` (§5) y la nota sobre orden de ejecución al final de "Diseño experimental sugerido".

---

## 2. Datos duros de la consigna

| Elemento | Valor |
| :--- | :--- |
| Oral | Jueves 30/07/2026, 20 minutos, 15 puntos |
| Entrega escrita | Jueves 06/08/2026 por Gestión, 30 puntos |
| Extensión | Alrededor de 10 carillas, sin bibliografía ni anexos |
| Restricción de tipo | NO puede ser knockout. La edición de regulación génica está explícitamente permitida |
| Estructura exigida | Introducción, Objetivo, Diseño Experimental, Anexos, Bibliografía |
| Anexos | Secuencias completas de guías, primers y plásmidos, con características marcadas (sitios de corte, regiones homólogas, etiquetas, mutaciones) |
| Archivos | Adjuntar los de SnapGene u otro software si se usaron |

Nota de encaje. El proyecto cumple la restricción de tipo sin ambigüedad: es activación transcripcional dirigida por CRISPRa, es decir, edición de regulación génica sin corte ni alteración de secuencia. Conviene decirlo de forma explícita en la Introducción para que el evaluador no tenga que inferirlo.

---

## 3. Tensión detectada entre consigna y rúbrica

La estructura exigida no incluye una sección de Resultados, pero la rúbrica asigna 6 puntos a Resultados, el criterio de mayor peso individual. Dado que el trabajo es de diseño y no experimental, la lectura razonable es que ese criterio se satisface con los productos del diseño: resultados in silico de selección de guías (puntajes de eficiencia y de off-target, herramienta usada y versión), mapas de plásmido, esquema de la construcción, tabla comparativa de efectores evaluados y resultados esperados con su lectura anticipada. Ese material debe presentarse dentro de Diseño Experimental, con tablas y figuras propias, y no diluido en prosa.

Riesgo si se ignora: se pierde el criterio de mayor puntaje por no haber generado material presentable, aun teniendo el diseño resuelto conceptualmente.

---

## 4. Mapa rúbrica contra material disponible

| Criterio (puntos) | Qué exige | Material existente | Estado |
| :--- | :--- | :--- | :--- |
| Introducción y Objetivos (5) | Contexto, problema, objetivos específicos y coherentes con la hipótesis | INFORME §1, §2, §4.1 a §4.3 (eje FTO-m6A-FOS, caída con la edad, ROS) | Suficiente, hay que reducir a extensión |
| Metodología (5) | Detalle y reproducibilidad de materiales y procedimientos | INFORME §3.4 (controles), §4.7 (entrega), §6 "Diseño experimental sugerido" | Parcial, falta el detalle operativo real |
| Resultados (6) | Presentación clara con tablas, gráficos y figuras; análisis correcto | Nada producido todavía | Faltante, prioridad máxima |
| Discusión y Conclusiones (5) | Interpretación vinculada a literatura; conclusiones fundadas | INFORME §5 (Bloque C), §6, §7, §8; CONCLUSIONES_CLAVE completo | Sobrante, hay que seleccionar |
| Referencias y Citaciones (3) | Fuentes pertinentes, formato correcto y consistente | INFORME §9, bibliografía consolidada con DOI | Suficiente, requiere depuración |
| Claridad y Organización (4) | Secciones claras, lenguaje técnico, sin errores | `Rules_Of_Writing.md` | Depende de la redacción final |
| Cumplimiento de requisitos (2) | Formato, extensión, secciones, puntualidad | Consigna | Verificar antes de entregar |

Lectura del mapa: el corpus cubre con holgura Introducción, Discusión y Bibliografía (13 de 30 puntos) y no cubre Metodología ni Resultados (11 de 30 puntos), que son justamente los que dependen de producir diseño y no de leer literatura.

---

## 5. Artefactos de diseño pendientes de producir

1. Selección de guías dirigidas al promotor de *FTO*, con la región blanco definida respecto del TSS, la herramienta de diseño utilizada, los puntajes de eficiencia y de off-target, y el criterio de descarte de las guías no elegidas. La consigna pide explícitamente en el oral hablar de "resultados descartados", de modo que conviene registrar las guías rechazadas y el motivo.
2. Diseño de la construcción dCas9-p300, con su tamaño real (aproximadamente 5 a 6 kb), promotor de expresión, marcador de selección y estrategia de titulación de dosis.
3. Mapa del plásmido y esquema de la estrategia completa, desde la entrega hasta la lectura fenotípica. Archivo de SnapGene si se usa.
4. Panel de controles instanciado para este experimento concreto: guía scrambled, efector catalíticamente muerto (p300 D1398Y), dCas9 sin efector. La justificación bibliográfica ya está en INFORME §3.4.
5. Primers para las verificaciones (qPCR de *FTO*, MeRIP-qPCR o SELECT sobre el 3'UTR de *FOS*, ChIP-qPCR de H3K27ac sobre el promotor de *FTO*).
6. Tabla de resultados esperados con su interpretación anticipada, incluida la lectura de reversión parcial y no de normalización completa (INFORME §4.6).

---

## 6. Limitaciones a declarar de forma explícita

Estas van en Discusión, redactadas como delimitación del alcance y no como disculpa.

1. No existe antecedente de activación de *FTO* con dCas9-p300 en granulosa ni en tejido reproductivo. Sí existe en HepG2 (Kachanov et al., 2025) y existe dCas9-p300 aplicado a granulosa porcina sobre otro gen (Liao et al., 2026). La novedad del proyecto es el cruce de ambos, no cada uno por separado.
2. La causa promotor-específica de la caída basal de *FTO* en granulosa permanece sin resolver, incluso tras las extrapolaciones desde genes relacionados. Por eso el mapeo del promotor precede al ensayo de activación.
3. No hay datos de eficiencia, especificidad ni entrega de dCas9-p300 en KGN, COV434 ni granulosa primaria humana.
4. FTO actúa como borrador global de m6A sobre miles de transcritos, de modo que la activación debe titularse dentro de rango fisiológico y verificarse por transcriptoma global.

---

## 7. Regla de uso del corpus

Ninguna afirmación del corpus se traslada al escrito sin contrastarla contra su pasaje literal. La auditoría de q15 y la de las citas de Liao y Kachanov mostraron un desajuste sistemático entre cita y fuente en la exportación de NotebookLM: hubo afirmaciones sin anclaje verbatim, afirmaciones reales atribuidas a la fuente equivocada, una misma afirmación atribuida a cuatro fuentes distintas y un tejido mal consignado. El estado `pass` de la auditoría automática no protege contra esto, porque verifica que los enlaces resuelvan y no que la afirmación corresponda a la fuente enlazada.

Casos ya verificados y utilizables tal como están redactados hoy en `INFORME_GENERAL.md`: hipometilación del promotor de *AR* en granulosa de PCOS (Desmawati et al., 2018); efecto del cromo hexavalente sobre H3K9ac y H3K27ac (Li et al., 2025b); rs9939609 intrónica asociada a *FTO* aumentado en PCOS (Kuai et al., 2026); reducción de cccDNA por activación de *FTO* con dCas9-p300 (Kachanov et al., 2025); aumento de H3K27ac y de expresión de *ZFP42* en granulosa porcina (Liao et al., 2026, verificado contra el texto de resultados de la fuente primaria).

Casos que no deben usarse sin re-verificar: activación de *FTO* por SP1 (anclada a una entrada de lista de referencias dentro de una revisión, correspondiente a injuria renal y no a cardiomiocito); hipermetilación de *Atg5* y *LC3B*; acetilación diferencial en los promotores de *StAR* y *Cyp19a1*; reducción de pgRNA por sobreexpresión de *FTO*; unión directa de C/EBPα al promotor de *FTO* (proviene de q16, todavía sin auditar contra pasajes literales).

---

## 8. Estado y próximos pasos

| Paso | Estado |
| :--- | :--- |
| Corpus documental de 21 preguntas | Completo y auditado, con las salvedades de la sección 7 |
| Bloque C sobre mecanismo promotor | Escrito e integrado en INFORME §5 |
| Justificación afirmativa de dCas9-p300 | Escrita en INFORME §5.6, con bibliografía verificada |
| Artefactos de diseño (sección 5 de este archivo) | Pendientes |
| Redacción del escrito (10 carillas) | Pendiente |
| Presentación oral | Pendiente, 30/07/2026 |
| Auditoría verbatim de q16 a q21 | Pendiente, recomendable antes de citarlas en el escrito |
