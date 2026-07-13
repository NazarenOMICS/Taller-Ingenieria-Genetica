# AGENTS.md - Guía de operación del repositorio

Repositorio de trabajo del **Taller de Ingeniería Genética 2026** (Ingeniería en Biotecnología, Universidad ORT Uruguay). Contiene el material del curso convertido a Markdown, organizado por modalidad de evaluación, más los PDF y la presentación originales. Este archivo indica a un agente cómo leer y operar el repo.

## Regla de escritura obligatoria

Toda redacción de textos en este repositorio (informes, obligatorio, resúmenes, correcciones, respuestas) **debe seguir `Rules_Of_Writing.md`**, que captura la voz y el estilo académico-técnico de Naza. Es de cumplimiento obligatorio, no una sugerencia. Puntos no negociables:

1. Registro formal-técnico, fluido, sin tono docente ni motivacional; no se halaga al lector ni al trabajo propio.
2. Prohibición absoluta de guiones largos (em-dashes, carácter U+2014): reescribir con paréntesis o punto y coma.
3. Nada de viñetas ni listas numeradas dentro de la prosa; los datos se integran en el texto con conectores. (Las tablas y listas son aceptables en material de referencia, no en prosa académica entregable.)
4. Citas en formato autor-año entre paréntesis (Apellido et al., año); no mezclar con sistema numérico en un mismo texto.
5. Los datos, cifras y atribuciones se toman siempre de las fuentes; no se inventan.

Leer `Rules_Of_Writing.md` completo antes de producir cualquier texto en nombre de Naza.

## Cómo navegar el repo (importante)

Cada `.md` empieza con un **índice operativo**: un bloque al inicio que resume qué contiene el archivo, a qué modalidad sirve y sus datos clave. Debajo va la **extracción casi completa** de la fuente.

Procedimiento recomendado para el agente:

1. Leer primero este `AGENTS.md` y `MODALIDADES_DE_EVALUACION.md`.
2. Para localizar información, leer únicamente los índices operativos (encabezado de cada archivo) y decidir cuál abrir. No leer los cuerpos completos salvo que el índice indique que el archivo es relevante para la tarea.
3. Tratar los archivos `.md` como fuente de trabajo. Los originales en `_fuentes_pdf/` son la fuente de verdad última: si un dato del `.md` parece dudoso, contrastar con el PDF correspondiente citado en su índice.

## Fuente de verdad

La **Cartilla** es la fuente primaria del método de evaluación y del contenido teórico-práctico. Ante discrepancias entre la Cartilla, la Rúbrica y la Presentación del curso, prevalece la Cartilla. No agregar información externa al material del curso salvo que la tarea lo pida explícitamente; en ese caso, buscar y citar.

## Mapa de carpetas

```
Taller Ingenieria Genetica/
├── AGENTS.md                       Este archivo.
├── MODALIDADES_DE_EVALUACION.md    Documento maestro: las 4 modalidades, puntajes, fechas.
├── Rules_Of_Writing.md             Estándar de escritura obligatorio (voz de Naza).
├── _fuentes_pdf/                   PDFs y pptx originales (fuente de verdad, no editar).
├── 00_teoria_general/              Material transversal (no atado a una sola modalidad).
│   ├── cartilla_teorico.md         Marco teórico: CASP8AP2, CRISPR-Cas, Golden Gate, genotipado.
│   ├── presentacion_curso.md       Contenido de las 19 slides de la presentación.
│   └── bibliografia.md             Referencias completas de la Cartilla (autor-año + DOI).
├── 01_presentacion_de_tecnicas/    Modalidad 1 (15 pts).
│   └── consigna.md
├── 02_obligatorio/                 Modalidad 2 (escrito 30 pts + oral 15 pts).
│   ├── consigna_y_rubrica.md       Consigna, tipo de edición, formato, estructura, oral.
│   └── rubrica_detallada.md        Rúbrica de 7 criterios del escrito (suma 30).
├── 03_informe/                     Modalidad 3 (30 pts).
│   ├── cartilla_practico.md        Cronograma, actividades día a día, ejercicios, secuencias.
│   ├── protocolo_1_clonado.md      Clonado de guía en pX459 (BbsI).
│   ├── protocolo_2_repique.md      Repique de línea celular adherente.
│   ├── protocolo_3_transfeccion.md Transfección HEK-293 con Lipofectamine 2000.
│   └── protocolo_4_tincion_plata.md Tinción con plata del gel de HMA.
└── 04_actuacion_en_clases/         Modalidad 4 (10 pts).
    └── criterios.md
```

## Correspondencia modalidad → carpeta

1. Presentación de técnicas (15 pts) → `01_presentacion_de_tecnicas/`
2. Obligatorio, escrito (30 pts) + oral (15 pts) → `02_obligatorio/`
3. Informe (30 pts) → `03_informe/` (respaldado por `00_teoria_general/` para el marco teórico)
4. Actuación en clases (10 pts) → `04_actuacion_en_clases/`

## Notas de mantenimiento

1. Los `.md` de `01_` y `04_` se derivan de la Cartilla y la Presentación porque no existe un PDF dedicado a esas modalidades; así está marcado en cada archivo bajo "Nota de trazabilidad".
2. El proyecto práctico del curso es un KO de CASP8AP2 en HEK-293; el Obligatorio, en cambio, exige explícitamente una edición que NO sea KO. No confundir ambos entregables.
3. Convención de trazabilidad: cada `.md` cita en su índice el archivo de `_fuentes_pdf/` del que proviene. Mantener esa cita al editar.
4. El contenido `.md` es un resumen operativo más una extracción fiel; no reemplaza a los originales para verificación fina de secuencias, mapas o figuras (las figuras solo existen en los PDF).
