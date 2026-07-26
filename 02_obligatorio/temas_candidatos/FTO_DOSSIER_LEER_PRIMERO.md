# Anexo técnico FTO–RPGRIP1L: leer primero

## Alcance

Este archivo **no vuelve a explicar el Obligatorio ni la hipótesis biológica general**. Ese contexto ya está desarrollado en el repositorio y en el agente que trabaja sobre el proyecto.

Su única función es incorporar el conocimiento nuevo obtenido durante la inspección genómica solicitada:

- estructura y exones de FTO;
- transcritos y sitios de inicio de FTO y RPGRIP1L;
- descubrimiento del promotor divergente compartido;
- delimitación de la región inter-TSS sobre la que se diseñarán las guías;
- elementos regulatorios recuperados de Ensembl y de universos independientes;
- descargas y tablas auditadas;
- restricciones necesarias para no mezclar ensamblados, anotaciones o niveles de evidencia.

Claude debe leer este archivo como un **anexo técnico incremental** al conocimiento que ya posee del Obligatorio.

## Dónde están los archivos nuevos

El índice interpretativo está en `main`:

- `02_obligatorio/temas_candidatos/FTO_DOSSIER_LEER_PRIMERO.md`

Las extracciones auditadas y los archivos descargados están en la rama técnica:

- rama: `tmp/fto-ensembl116-extraction`

Archivos principales:

1. `tmp_fto/summary.json`
   - resumen de la extracción de FTO;
   - intervalo analizado;
   - cantidad de exones y elementos regulatorios.

2. `tmp_fto/fto_mane_exons_ensembl116.csv`
   - los 9 exones del transcrito MANE `ENST00000471389.6`.

3. `tmp_fto/fto_enhancers_ensembl116.csv`
   - las 59 características Ensembl tipo enhancer dentro del intervalo de FTO más 1,8 kb upstream.

4. `tmp_fto/fto_regulatory_all_ensembl116.csv`
   - enhancers, promotores y sitios CTCF dentro del mismo intervalo.

5. `tmp_fto_promoters/summary_promoter_universes.json`
   - resumen de los TSS observados para FTO y RPGRIP1L y de los universos regulatorios consultados.

6. `tmp_fto_promoters/ensembl116_FTO_RPGRIP1L_transcripts_TSS.csv`
   - todos los transcritos recuperados y sus TSS;
   - permite distinguir los TSS MANE de los alternativos.

7. `tmp_fto_promoters/ensembl116_regulatory_145kb_around_FTO_RPGRIP1L.csv`
   - elementos Ensembl en la región ampliada alrededor de ambos genes.

8. `tmp_fto_promoters/ucsc_encodeCcreCombined.json`
   - cCRE de ENCODE consultados mediante UCSC.

9. `tmp_fto_promoters/ucsc_geneHancerRegElements.json`
   - elementos GeneHancer consultados mediante UCSC.

Los archivos generados localmente en formato Excel, CSV y Markdown que se entregaron durante la conversación no están todos versionados en `main`. Para Claude, la fuente reproducible dentro de GitHub es la rama técnica indicada arriba.

## Hallazgos nuevos principales

### Referencia de FTO

- Gen: `FTO`, Ensembl Gene `ENSG00000140718`.
- Transcrito principal: `ENST00000471389.6`, `FTO-206`.
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

## Reglas para Claude

1. Usar este archivo solamente como actualización técnica del diseño existente.
2. Mantener GRCh38 como ensamblado de diseño.
3. No mezclar coordenadas hg19 de FANTOM5 con las tablas GRCh38.
4. No equiparar solapamiento espacial con regulación funcional de FTO.
5. No afirmar actividad en granulosa sin evidencia específica del tipo celular.
6. No confundir los nueve exones MANE con el conjunto agregado de exones de todas las isoformas.
7. No asignar coordenadas a motivos de factores de transcripción si no fueron verificadas contra la secuencia de referencia.
8. Separar hechos de anotación, evidencia experimental, inferencias de integración y decisiones de diseño.
9. No seleccionar una guía definitiva sin evaluar PAM, actividad, especificidad, variantes frecuentes, distancia a ambos TSS y elementos solapados.
10. No reestructurar el Obligatorio a partir de este anexo.