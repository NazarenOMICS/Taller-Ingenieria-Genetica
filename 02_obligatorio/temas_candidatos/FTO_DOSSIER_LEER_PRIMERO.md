# Anexo técnico FTO–RPGRIP1L: leer primero

## Alcance

Este archivo **no vuelve a explicar el Obligatorio ni la hipótesis biológica general**, puesto que ese contexto ya se encuentra desarrollado en el repositorio y en el agente que trabaja sobre el proyecto.

Su única función es incorporar el conocimiento nuevo obtenido durante la inspección genómica solicitada:

- estructura y exones de FTO;
- transcritos y sitios de inicio de FTO y RPGRIP1L;
- descubrimiento del promotor divergente compartido;
- delimitación de la región inter-TSS sobre la que se diseñarán las guías;
- elementos regulatorios recuperados de Ensembl y de universos independientes;
- descargas y tablas auditadas;
- restricciones necesarias para no mezclar ensamblados, anotaciones o niveles de evidencia.

Claude debe leer este archivo como un **anexo técnico incremental** al conocimiento que ya posee del Obligatorio.

## Dónde está cada cosa

Los archivos consolidados se encuentran en:

- `02_obligatorio/temas_candidatos/FTO_anexo_tecnico/`

Orden de lectura:

1. `FTO_anexo_tecnico/00_LEER_PRIMERO.md`: síntesis de los hallazgos nuevos y mapa de archivos.
2. `FTO_anexo_tecnico/01_promotor_divergente_FTO_RPGRIP1L.md`: análisis focalizado de la región inter-TSS.
3. `FTO_anexo_tecnico/datos/FTO_resumen_extraccion_Ensembl116.json`: resumen reproducible de la extracción.
4. `FTO_anexo_tecnico/datos/FTO_exones_MANE_Ensembl116_GRCh38.csv`: exones del transcrito MANE de FTO.
5. `FTO_anexo_tecnico/datos/FTO_enhancers_Ensembl116_GRCh38_1p8kb_upstream.csv`: enhancers Ensembl dentro del intervalo amplio.
6. `FTO_anexo_tecnico/datos/FTO_regulatorios_Ensembl116_GRCh38_1p8kb_upstream.csv`: enhancers, promotores y sitios CTCF.
7. `FTO_anexo_tecnico/datos/FTO_RPGRIP1L_TSS_resumen_Ensembl116.csv`: TSS MANE y TSS alternativos anotados.
8. `FTO_anexo_tecnico/datos/FTO_RPGRIP1L_interTSS_elementos_regulatorios.csv`: elementos que solapan o caracterizan la región de diseño.

La rama `tmp/fto-ensembl116-extraction` conserva los archivos intermedios y la procedencia técnica de las descargas. No es necesario usarla para la lectura normal una vez que las tablas consolidadas están en `main`.

## Hallazgos nuevos principales

### Referencia de FTO

- Gen: `FTO`, Ensembl Gene `ENSG00000140718`.
- Transcrito principal de trabajo: `ENST00000471389.6`, `FTO-206`.
- Etiquetas: MANE Select, Ensembl canonical, GENCODE primary y GENCODE basic.
- Ensamblado: GRCh38.p14.
- Ensembl: release 116.
- GENCODE: release 50.
- Hebra: positiva.
- TSS MANE: `chr16:53,704,156`.
- Extremo 3′: `chr16:54,121,941`.
- Exones del transcrito MANE: 9.

### Referencia de RPGRIP1L

- Gen vecino: `RPGRIP1L`, Ensembl Gene `ENSG00000103494`.
- Transcrito MANE Select: `ENST00000647211.2`, `RPGRIP1L-212`.
- Hebra: negativa.
- TSS MANE: `chr16:53,703,859`.

### Región inter-TSS

Los TSS MANE están enfrentados:

- RPGRIP1L: `chr16:53,703,859`, hebra negativa.
- FTO: `chr16:53,704,156`, hebra positiva.
- Diferencia entre coordenadas: 297 pb.
- Intervalo inclusivo de inspección: `chr16:53,703,859-53,704,156`, 298 nucleótidos.
- Región estrictamente comprendida entre ambos nucleótidos TSS: `chr16:53,703,860-53,704,155`, 296 pb.

### Promotor divergente

El intervalo está cubierto por el promotor Ensembl:

- ID: `ENSR16_9RBJC`.
- Coordenadas: `chr16:53,703,831-53,704,167`.
- Genes asociados: `RPGRIP1L,FTO`.

La región debe describirse como **promotor divergente FTO–RPGRIP1L** o como dos core promoters adyacentes dentro de un mismo bloque regulador. No debe describirse como un promotor exclusivo de FTO.

Los elementos Ensembl inmediatamente flanqueantes son:

- `ENSR16_9RBJ8`, enhancer, `chr16:53,703,398-53,703,830`.
- `ENSR16_BDMQQ`, enhancer, `chr16:53,704,168-53,704,740`.

GeneHancer identifica `GH16J053703`, un elemento Elite clasificado como `Promoter/Enhancer` que engloba el bloque. ENCODE aporta una señal tipo PLS y FANTOM5/Fanta respalda iniciación divergente mediante picos CAGE para ambos genes. Las coordenadas FANTOM5 consultadas están originalmente en hg19 y no deben mezclarse con GRCh38.

### Inventario amplio de FTO

La extracción amplia utilizó `chr16:53,702,356-54,121,941`, que incluye 1.800 pb upstream del TSS MANE y todo el transcrito. Se recuperaron:

- 9 exones MANE;
- 59 características Ensembl tipo enhancer;
- 2 promotores;
- 8 sitios CTCF;
- 69 características regulatorias en total.

Esto no significa que FTO posea funcionalmente 59 enhancers ni que todas esas regiones regulen FTO o estén activas en granulosa. Es un inventario espacial del Regulatory Build dentro del intervalo definido.

## Consecuencia directa para el diseño

La información nueva modifica el diseño de guías porque una guía dCas9-p300 colocada entre ambos TSS puede aumentar FTO, RPGRIP1L, ambos genes o ninguno. Por ello, toda guía debe caracterizarse por su distancia a **ambos** TSS y toda validación debe medir simultáneamente FTO y RPGRIP1L.

Un cambio en RPGRIP1L no constituiría automáticamente un off-target de secuencia; podría ser un efecto cis esperable de acetilar un promotor divergente.

## Reglas para leer las tablas

1. Mantener GRCh38 como ensamblado de diseño.
2. No mezclar coordenadas hg19 de FANTOM5 con las tablas GRCh38.
3. No equiparar solapamiento espacial con regulación funcional de FTO.
4. No afirmar actividad en granulosa sin evidencia específica del tipo celular.
5. No confundir los nueve exones MANE con el conjunto agregado de exones de todas las isoformas.
6. No asignar coordenadas a motivos de factores de transcripción si no fueron verificadas contra la secuencia de referencia.
7. Separar hechos de anotación, evidencia experimental, inferencias de integración y decisiones de diseño.
8. No seleccionar una guía definitiva sin evaluar PAM, actividad, especificidad, variantes frecuentes, distancia a ambos TSS y elementos solapados.

## Uso esperado por Claude

Claude debe utilizar este anexo exclusivamente para incorporar los hallazgos genómicos y regulatorios nuevos al diseño ya existente. No debe reestructurar el Obligatorio a partir de este archivo ni tratarlo como una nueva propuesta de proyecto.