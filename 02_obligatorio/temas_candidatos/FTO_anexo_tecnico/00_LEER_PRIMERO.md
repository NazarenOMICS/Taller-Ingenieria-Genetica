# Anexo técnico FTO–RPGRIP1L: leer primero

## Propósito

Este anexo contiene únicamente el conocimiento nuevo obtenido durante la inspección genómica y regulatoria de **FTO** y **RPGRIP1L**. No reformula el Obligatorio ni reemplaza el contexto ya existente en el repositorio.

## Orden de lectura

1. `01_promotor_divergente_FTO_RPGRIP1L.md`
2. `datos/FTO_resumen_extraccion_Ensembl116.json`
3. `datos/FTO_RPGRIP1L_TSS_resumen_Ensembl116.csv`
4. `datos/FTO_RPGRIP1L_interTSS_elementos_regulatorios.csv`
5. `datos/FTO_exones_MANE_Ensembl116_GRCh38.csv`
6. `datos/FTO_enhancers_Ensembl116_GRCh38_1p8kb_upstream.csv`
7. `datos/FTO_regulatorios_Ensembl116_GRCh38_1p8kb_upstream.csv`

## Referencias obligatorias

- Ensamblado: **GRCh38.p14**.
- Ensembl: **release 116**.
- GENCODE: **release 50**.
- FTO MANE Select: `ENST00000471389.6`, TSS `chr16:53,704,156`, hebra positiva.
- RPGRIP1L MANE Select: `ENST00000647211.2`, TSS `chr16:53,703,859`, hebra negativa.
- Diferencia entre coordenadas TSS: 297 pb.
- Intervalo inclusivo de inspección: `chr16:53,703,859-53,704,156`, 298 nucleótidos.
- Región estrictamente inter-TSS: `chr16:53,703,860-53,704,155`, 296 pb.

## Hallazgo central

Los TSS MANE de FTO y RPGRIP1L están enfrentados y el intervalo está cubierto por el promotor Ensembl `ENSR16_9RBJC`, asignado a ambos genes. Por ello, la región debe tratarse como un **promotor divergente FTO–RPGRIP1L**, no como un promotor exclusivo de FTO.

## Reglas para Claude

1. Incorporar este anexo al conocimiento previo del Obligatorio sin volver a reconstruir el proyecto.
2. No mezclar coordenadas hg19 y GRCh38.
3. No afirmar que todos los enhancers espaciales regulan FTO.
4. No afirmar actividad en granulosa sin evidencia específica.
5. No presentar coordenadas inferidas de motivos como anotación oficial.
6. Para diseñar guías, registrar distancia a ambos TSS y medir experimentalmente FTO y RPGRIP1L.
7. Separar hechos de anotación, evidencia experimental, inferencias y decisiones de diseño.

La rama `tmp/fto-ensembl116-extraction` conserva archivos intermedios y workflows de descarga, pero los archivos necesarios para Claude están consolidados en esta carpeta de `main`.