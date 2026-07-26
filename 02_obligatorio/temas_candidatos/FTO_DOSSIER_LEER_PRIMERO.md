# Dossier FTO: leer primero

Este archivo organiza el conocimiento utilizado para el tema candidato del Obligatorio: activación epigenómica de **FTO** mediante dCas9-p300 en células de la granulosa envejecidas.

## Estado del material

El tema biológico principal está en:

- `02_obligatorio/temas_candidatos/edicion_epigenomica_FTO_envejecimiento_ovarico.md`

La extracción genómica y regulatoria auditada se generó en la rama técnica:

- `tmp/fto-ensembl116-extraction`

Los datos de esa rama provienen directamente de Ensembl release 116, GENCODE 50 y GRCh38.p14. No deben mezclarse con coordenadas hg19.

## Orden de lectura para Claude

1. Leer `edicion_epigenomica_FTO_envejecimiento_ovarico.md` para comprender la hipótesis FTO–m6A–FOS y la estrategia dCas9-p300.
2. Leer este archivo completo para fijar las versiones, la arquitectura del promotor y las restricciones de interpretación.
3. Consultar en la rama `tmp/fto-ensembl116-extraction`:
   - `tmp_fto/summary.json`
   - `tmp_fto/fto_mane_exons_ensembl116.csv`
   - `tmp_fto/fto_enhancers_ensembl116.csv`
   - `tmp_fto/fto_regulatory_all_ensembl116.csv`
   - `tmp_fto_promoters/summary_promoter_universes.json`
   - `tmp_fto_promoters/ensembl116_FTO_RPGRIP1L_transcripts_TSS.csv`
   - `tmp_fto_promoters/ensembl116_regulatory_145kb_around_FTO_RPGRIP1L.csv`
   - `tmp_fto_promoters/ucsc_encodeCcreCombined.json`
   - `tmp_fto_promoters/ucsc_geneHancerRegElements.json`
4. Para diseñar las guías, trabajar únicamente con la región inter-TSS definida por los transcritos MANE y volver a descargar la secuencia GRCh38 antes de seleccionar PAM y protospacer.

## Referencia estructural

- Gen: `FTO`, Ensembl Gene `ENSG00000140718`.
- Transcrito principal de trabajo: `ENST00000471389.6`, `FTO-206`.
- Etiquetas: MANE Select, Ensembl canonical, GENCODE primary y GENCODE basic.
- Ensamblado: GRCh38.p14.
- Ensembl: release 116.
- GENCODE: release 50.
- Hebra de FTO: positiva.
- TSS MANE de FTO: `chr16:53,704,156`.
- Extremo 3′ del transcrito: `chr16:54,121,941`.
- Número de exones del transcrito MANE: 9.

La extracción amplia utilizó el intervalo `chr16:53,702,356-54,121,941`, que incluye 1.800 pb upstream del TSS MANE y todo el transcrito. Dentro de ese intervalo se recuperaron 59 características Ensembl tipo enhancer, 2 promotores y 8 sitios CTCF. Esto no significa que los 59 enhancers regulen FTO ni que estén activos en granulosa.

## Promotor divergente FTO–RPGRIP1L

RPGRIP1L se transcribe en la hebra negativa y FTO en la positiva. Sus TSS MANE quedan enfrentados:

- RPGRIP1L MANE: `ENST00000647211.2`, TSS `chr16:53,703,859`, hebra negativa.
- FTO MANE: `ENST00000471389.6`, TSS `chr16:53,704,156`, hebra positiva.
- Diferencia entre coordenadas TSS: 297 pb.
- Intervalo inclusivo de inspección: `chr16:53,703,859-53,704,156`, 298 nucleótidos.
- Región estrictamente situada entre ambos nucleótidos TSS: `chr16:53,703,860-53,704,155`, 296 pb.

Toda esa región está contenida dentro del promotor Ensembl `ENSR16_9RBJC`, anotado para **RPGRIP1L y FTO**. El enhancer Ensembl `ENSR16_9RBJ8` termina inmediatamente antes y `ENSR16_BDMQQ` comienza inmediatamente después.

GeneHancer identifica el elemento Elite `GH16J053703`, clasificado como `Promoter/Enhancer`, que engloba el bloque. ENCODE SCREEN aporta una señal tipo PLS y FANTOM5/Fanta agrupa la región como un cluster de iniciación divergente con picos CAGE para ambas direcciones.

## Interpretación experimental

La región no debe describirse como un promotor exclusivo de FTO. Es un bloque promotor divergente o un conjunto de core promoters adyacentes dentro de una misma región reguladora.

Una guía dCas9-p300 puede:

- aumentar FTO sin cambiar RPGRIP1L;
- aumentar ambos genes;
- favorecer RPGRIP1L;
- no activar ninguno.

Por lo tanto, toda prueba debe medir simultáneamente FTO y RPGRIP1L. Un aumento de RPGRIP1L no sería necesariamente un off-target de secuencia, sino un posible efecto cis de acetilar el promotor compartido.

## Motivos funcionales reportados

La literatura funcional del promotor de FTO describe sitios para C/EBPα, FOXA2 y SP1 cerca del TSS. Sus posiciones relativas publicadas no deben convertirse automáticamente en coordenadas GRCh38. Antes de usarlas hay que verificar que la secuencia reportada aparezca exactamente en el FASTA GRCh38 del intervalo y documentar la hebra.

## Reglas obligatorias para Claude

1. No mezclar hg19 con GRCh38.
2. No decir que FTO “tiene 59 enhancers”; decir que Ensembl clasifica 59 regiones como enhancer dentro del intervalo definido.
3. No afirmar que todas regulan FTO ni que están activas en granulosa.
4. No confundir los 9 exones MANE con el conjunto agregado de exones de todas las isoformas.
5. No tratar el promotor inter-TSS como exclusivo de FTO.
6. No asignar coordenadas genómicas a motivos de factores de transcripción sin verificarlos contra la secuencia de referencia.
7. No afirmar que el envejecimiento reduce H3K27ac en el promotor de FTO; esa pérdida no está demostrada y forma parte de la hipótesis experimental.
8. Separar siempre hechos de anotación, evidencia experimental publicada, inferencias de integración y decisiones de diseño.
9. No elegir una guía definitiva sin evaluar PAM, actividad, especificidad, variantes frecuentes, distancia a ambos TSS y solapamiento con elementos regulatorios.
10. Validar la intervención en el orden: unión del editor, H3K27ac, FTO, RPGRIP1L, eje m6A–FOS y fenotipo de senescencia.

## Próximo paso de diseño

Descargar o importar en Benchling la secuencia GRCh38 de `chr16:53,703,859-53,704,156`, identificar todos los PAM compatibles con la nucleasa seleccionada y construir una tabla de guías que incluya coordenada, hebra, PAM, distancia al TSS de FTO, distancia al TSS de RPGRIP1L, elemento regulador solapado, actividad prevista, especificidad y off-targets.
