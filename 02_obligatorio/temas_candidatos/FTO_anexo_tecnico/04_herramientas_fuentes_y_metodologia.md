# Herramientas, fuentes de datos y metodología del análisis FTO–RPGRIP1L

## Propósito

Este documento registra todas las fuentes biológicas, navegadores genómicos y herramientas computacionales utilizadas para analizar el locus **FTO–RPGRIP1L**, extraer sus anotaciones y generar las figuras del Obligatorio.

Es importante distinguir tres niveles:

1. **Fuentes de datos biológicos**, que aportan anotaciones o evidencia experimental.
2. **Herramientas de consulta**, que permiten acceder y visualizar esas fuentes.
3. **Herramientas de procesamiento**, que organizan, verifican y representan los datos, pero no constituyen evidencia biológica por sí mismas.

---

## 1. Referencia genómica y versiones utilizadas

- Especie: *Homo sapiens*.
- Ensamblado de trabajo: **GRCh38.p14**.
- Ensembl: **release 116**.
- GENCODE: **release 50**.
- FTO MANE Select: `ENST00000471389.6`.
- RPGRIP1L MANE Select: `ENST00000647211.2`.

Todas las coordenadas utilizadas para la extracción de exones, promotores, enhancers y sitios CTCF corresponden a **GRCh38**, salvo aquellas identificadas explícitamente como hg19.

---

## 2. Fuentes de datos biológicos

### 2.1 Ensembl release 116

Ensembl fue la fuente principal para:

- coordenadas de FTO y RPGRIP1L;
- orientación de ambos genes;
- modelos de transcritos;
- identificación de los transcritos MANE Select;
- coordenadas de los exones;
- anotaciones de promotores, enhancers y sitios CTCF;
- exportación de las vistas generales del locus.

Los datos estructurales y regulatorios se descargaron desde los archivos oficiales GFF3 de Ensembl:

- anotación génica del cromosoma 16;
- Ensembl Regulatory Build 116.

Para FTO se utilizó como referencia `ENST00000471389.6`, anotado como MANE Select y Ensembl canonical. Este transcrito contiene nueve exones.

Dentro del intervalo amplio comprendido entre 1.800 pb upstream del TSS MANE de FTO y el extremo final del transcrito se recuperaron:

- 59 características clasificadas por Ensembl como `enhancer`;
- 2 características clasificadas como `promoter`;
- 8 sitios de unión a CTCF;
- 69 características regulatorias en total.

Este inventario describe elementos que **solapan espacialmente el intervalo**. No demuestra que todos regulen FTO ni que estén activos en células de la granulosa.

### 2.2 GENCODE release 50

GENCODE aporta los modelos de genes y transcritos humanos mostrados dentro de Ensembl.

Se utilizó para respaldar:

- estructura de los transcritos;
- composición exónica;
- etiquetas `GENCODE basic` y `GENCODE primary`;
- selección del modelo principal de FTO.

GENCODE no fue tratado como una consulta completamente separada, porque sus anotaciones se encuentran integradas en los archivos y vistas de Ensembl utilizados.

### 2.3 MANE Select

MANE Select es una iniciativa conjunta de Ensembl/GENCODE y NCBI RefSeq destinada a proporcionar un transcrito representativo concordante para cada gen humano.

Se utilizó para fijar una referencia operativa y evitar que las coordenadas del TSS cambiaran según la isoforma elegida.

Transcritos utilizados:

- FTO: `ENST00000471389.6`.
- RPGRIP1L: `ENST00000647211.2`.

La elección de MANE no demuestra que esos transcritos sean los predominantes en KGN o granulosa primaria. Funcionan como referencia genómica normalizada.

### 2.4 ENCODE candidate cis-regulatory elements

Se consultó la pista de ENCODE correspondiente a los **candidate cis-regulatory elements**, o cCRE.

Los cCRE clasifican regiones mediante combinaciones de señales epigenómicas. Entre sus categorías se encuentran:

- PLS: *promoter-like signature*;
- pELS: *proximal enhancer-like signature*;
- dELS: *distal enhancer-like signature*;
- regiones asociadas a CTCF.

En la región FTO–RPGRIP1L se identificó una señal compatible con promotor. Esta evidencia respalda la naturaleza promotora del bloque, pero no demuestra actividad específica en granulosa.

### 2.5 GeneHancer

GeneHancer integra elementos regulatorios y asociaciones gen–elemento procedentes de múltiples bases.

En el locus se identificó:

- `GH16J053703`;
- clasificación `Promoter/Enhancer`;
- categoría `Elite`;
- solapamiento con el bloque promotor FTO–RPGRIP1L.

GeneHancer fue utilizado como fuente integradora secundaria. Su anotación no reemplaza la validación experimental en el tipo celular estudiado.

### 2.6 FANTOM5 CAGE

FANTOM5 utiliza CAGE, *Cap Analysis of Gene Expression*, para detectar extremos 5′ de ARN con cap y localizar sitios de inicio de transcripción.

Para el locus se identificaron:

- picos CAGE asociados a RPGRIP1L en la hebra negativa;
- un pico CAGE asociado a FTO en la hebra positiva.

Esto aporta evidencia independiente de iniciación transcripcional divergente.

Las coordenadas observadas para esos picos estaban disponibles originalmente en **hg19**. Por ese motivo, no se utilizaron directamente para seleccionar guías en GRCh38.

### 2.7 Fanta

Fanta se utilizó como interfaz integradora para visualizar conjuntamente:

- picos CAGE de FANTOM5;
- asignación de los picos a FTO y RPGRIP1L;
- elementos cCRE de ENCODE;
- el cluster promotor compartido.

Fanta es una interfaz de integración. La evidencia experimental de inicio transcripcional procede de FANTOM5 CAGE.

### 2.8 EPDnew

EPDnew apareció como una de las fuentes integradas dentro de la anotación GeneHancer de la región.

No se realizó una extracción independiente y completa desde EPDnew. Por lo tanto, debe citarse únicamente como una fuente incorporada por GeneHancer y no como una base consultada de manera independiente.

---

## 3. Herramientas de consulta y descarga

### 3.1 Navegador web de Ensembl

El navegador de Ensembl se utilizó para:

- inspeccionar visualmente el locus;
- comparar transcritos;
- observar la orientación de FTO y RPGRIP1L;
- mostrar características regulatorias;
- exportar vistas en PDF.

Las vistas generales de 1 Mb y de transcritos/regulación proceden de exportaciones del navegador Ensembl.

### 3.2 UCSC Genome Browser API

La API de UCSC Genome Browser se utilizó para consultar programáticamente pistas regulatorias sobre el intervalo exacto de interés.

Entre las pistas consultadas estuvieron:

- ENCODE cCRE;
- GeneHancer;
- islas CpG;
- pistas disponibles de promotores y regulación.

UCSC funcionó como plataforma de acceso. La fuente biológica subyacente depende de cada pista.

Las consultas a UCSC emplean coordenadas BED, es decir, 0-based y con extremo final exclusivo. Al generar tablas interpretables se normalizaron a coordenadas 1-based inclusive cuando correspondía.

### 3.3 FTP de Ensembl

Los archivos GFF3 oficiales se descargaron desde el servidor FTP de Ensembl.

Esto permitió realizar una extracción reproducible sin depender exclusivamente de capturas del navegador.

### 3.4 `curl` y `wget`

Se utilizaron para automatizar la descarga de:

- archivos GFF3 de Ensembl;
- respuestas JSON de la API de UCSC;
- secuencias del intervalo genómico.

Estas herramientas solamente realizan la transferencia de archivos y no aportan interpretación biológica.

---

## 4. Herramientas de procesamiento y análisis

### 4.1 Python

Python se utilizó para:

- leer archivos GFF3, CSV y JSON;
- filtrar registros por gen e intervalo;
- calcular longitudes;
- identificar solapamientos;
- organizar tablas auditables;
- verificar la región inter-TSS;
- preparar archivos FASTA;
- generar figuras;
- empaquetar los resultados.

Python es una herramienta de procesamiento y no una fuente de anotación.

### 4.2 Biblioteca estándar de Python

Se utilizaron módulos de la biblioteca estándar, entre ellos:

- `csv`, para generar tablas;
- `json`, para interpretar respuestas de APIs;
- `gzip`, para leer GFF3 comprimidos;
- `pathlib`, para organizar rutas y archivos;
- `zipfile`, para generar paquetes descargables.

### 4.3 Pillow

Pillow se utilizó para:

- abrir las imágenes obtenidas desde los PDF de Ensembl;
- eliminar márgenes externos;
- conservar la resolución;
- exportar las figuras como PNG.

Las Figuras 1 y 2 son extracciones procesadas de exportaciones directas de Ensembl.

### 4.4 Matplotlib

Matplotlib se utilizó para construir una representación propia del promotor divergente FTO–RPGRIP1L a partir de coordenadas oficiales.

La figura incluye:

- TSS MANE de RPGRIP1L;
- TSS MANE de FTO;
- promotor `ENSR16_9RBJC`;
- enhancers flanqueantes `ENSR16_9RBJ8` y `ENSR16_BDMQQ`;
- primer exón de FTO;
- distancia de 297 pb entre las coordenadas de los TSS.

Esta figura no es una captura de Ensembl. Es una reconstrucción gráfica elaborada a partir de datos de Ensembl release 116.

### 4.5 Conversión de PDF a imagen

Los PDF exportados desde Ensembl se renderizaron como imágenes rasterizadas para poder recortarlos y utilizarlos en la presentación.

No se modificó el contenido biológico de las pistas; solamente se procesó su formato visual.

### 4.6 UCSC liftOver

Se preparó un procedimiento con UCSC liftOver para convertir coordenadas entre hg19 y hg38.

Sin embargo, las coordenadas convertidas de FANTOM5 no se incorporaron como resultado definitivo en las figuras ni en el diseño de guías. Los picos FANTOM5 se conservaron identificados como hg19.

Por lo tanto, no debe afirmarse que las coordenadas CAGE fueron utilizadas directamente en GRCh38.

---

## 5. Control de versiones y reproducibilidad

### 5.1 GitHub

GitHub se utilizó para:

- almacenar scripts y resultados;
- registrar cambios mediante commits;
- conservar las tablas generadas;
- separar archivos finales de archivos temporales;
- permitir que otros agentes revisen la procedencia de los datos.

GitHub no es una fuente biológica.

### 5.2 GitHub Actions

GitHub Actions se utilizó para ejecutar workflows reproducibles de:

- descarga desde Ensembl;
- consulta de pistas UCSC;
- filtrado de regiones;
- generación de tablas;
- almacenamiento de resultados en una rama técnica.

La rama técnica utilizada fue:

`tmp/fto-ensembl116-extraction`

Los workflows automatizan el procedimiento, pero no reemplazan la revisión de las anotaciones.

---

## 6. Herramientas utilizadas para cada resultado

| Resultado | Fuente biológica | Herramienta de acceso | Procesamiento |
|---|---|---|---|
| Coordenadas de FTO y RPGRIP1L | Ensembl 116 / GENCODE 50 | Ensembl y GFF3 oficial | Python |
| Selección de transcritos | MANE Select | Ensembl | Revisión de etiquetas |
| Exones de FTO | Ensembl 116 | GFF3 oficial | Python y CSV |
| Promotores, enhancers y CTCF | Ensembl Regulatory Build 116 | GFF3 oficial | Python y CSV |
| cCRE tipo promotor | ENCODE | API de UCSC / Fanta | Integración y revisión |
| Elemento `GH16J053703` | GeneHancer | API de UCSC | Integración y revisión |
| Picos de inicio divergentes | FANTOM5 CAGE | Fanta | Revisión cualitativa, manteniendo hg19 |
| Figura general de 1 Mb | Ensembl | Exportación PDF | Renderizado y Pillow |
| Figura de transcritos | Ensembl | Exportación PDF | Renderizado y Pillow |
| Figura del promotor divergente | Ensembl 116 | Tablas de coordenadas | Python y Matplotlib |
| Trazabilidad del análisis | Archivos y scripts | GitHub | GitHub Actions |

---

## 7. Relación entre las figuras y las herramientas

### Figura 1. Contexto del locus FTO en una ventana de 1 Mb

- Fuente: Ensembl.
- Contenido: genes GENCODE y características regulatorias del locus.
- Obtención: exportación directa del navegador Ensembl en PDF.
- Procesamiento: conversión a PNG y recorte de márgenes con Python y Pillow.

### Figura 2. Transcritos de FTO y RPGRIP1L

- Fuente: Ensembl 116 y GENCODE 50.
- Contenido: modelos de transcritos y orientación de ambos genes.
- Obtención: exportación directa de Ensembl.
- Procesamiento: conversión a PNG y recorte con Pillow.

### Figura 3. Promotor divergente FTO–RPGRIP1L

- Fuente de coordenadas: Ensembl 116.
- Contenido: TSS MANE, promotor compartido, enhancers flanqueantes y primer exón de FTO.
- Obtención: reconstrucción propia.
- Procesamiento: Python y Matplotlib.

Debe citarse como una elaboración propia basada en datos de Ensembl y no como una captura directa del navegador.

---

## 8. Metodología lista para incorporar al trabajo

> La estructura genómica de FTO y RPGRIP1L se analizó utilizando Ensembl release 116 sobre el ensamblado humano GRCh38.p14, con modelos génicos de GENCODE release 50. Se seleccionaron como referencia los transcritos MANE Select ENST00000471389.6 para FTO y ENST00000647211.2 para RPGRIP1L. Las coordenadas de los exones y de las características regulatorias se extrajeron de los archivos GFF3 oficiales de Ensembl y de su Regulatory Build. La anotación de la región promotora se contrastó mediante la API de UCSC Genome Browser, consultando las pistas ENCODE candidate cis-regulatory elements y GeneHancer. La evidencia de iniciación transcripcional divergente se examinó mediante picos CAGE de FANTOM5 visualizados a través de Fanta. Las imágenes generales del locus se exportaron desde Ensembl y se procesaron con Python y Pillow. La representación focalizada del promotor divergente FTO–RPGRIP1L se construyó con Matplotlib a partir de las coordenadas oficiales de Ensembl. Las coordenadas de trabajo se mantuvieron en GRCh38; las anotaciones FANTOM5 disponibles en hg19 se utilizaron únicamente como evidencia cualitativa y no para el diseño directo de guías.

---

## 9. Versión breve para una diapositiva

> **Herramientas bioinformáticas:** Ensembl 116 y GENCODE 50 para genes, transcritos, exones y Regulatory Build; MANE Select para definir los transcritos de referencia; UCSC Genome Browser API para consultar ENCODE cCRE y GeneHancer; FANTOM5 CAGE mediante Fanta para evaluar sitios de inicio; Python, Pillow y Matplotlib para procesar datos y generar figuras; GitHub y GitHub Actions para trazabilidad y reproducibilidad.

---

## 10. Limitaciones y precauciones

1. Una característica regulatoria anotada no implica actividad en granulosa.
2. El solapamiento espacial de un enhancer con FTO no demuestra que su gen diana sea FTO.
3. Los transcritos MANE son una referencia normalizada, no una demostración de predominio celular.
4. Las coordenadas hg19 de FANTOM5 no deben mezclarse con GRCh38.
5. GeneHancer y Fanta integran información de otras bases y deben distinguirse de las fuentes primarias.
6. La región inter-TSS es un promotor divergente asociado a FTO y RPGRIP1L.
7. Una guía dCas9-p300 en esa región podría modificar la expresión de FTO, RPGRIP1L, ambos genes o ninguno.
8. La figura del promotor divergente es una reconstrucción propia y debe identificarse como tal.
9. No se debe afirmar que el envejecimiento causa pérdida de H3K27ac en el promotor de FTO, porque esa lesión todavía no fue demostrada en el proyecto.
10. La selección definitiva de guías requiere análisis de PAM, actividad, especificidad, variantes y distancia a ambos TSS.
