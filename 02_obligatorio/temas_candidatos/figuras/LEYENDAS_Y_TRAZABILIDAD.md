# Figuras 2 y 3 — leyendas finales y nota de trazabilidad

Estado: versiones preliminares para revisión. No incorporar al cuerpo del obligatorio hasta que se cierre la revisión.

---

## 1. Archivo fuente único

Todas las coordenadas graficadas provienen de un único archivo:
`figuras/coordenadas_locus_fto.csv` (18 filas de datos, 10 columnas).

Ninguna coordenada está escrita dentro del script de graficado. El script lee el CSV,
normaliza y dibuja. Cualquier corrección de coordenadas se hace en el CSV y se regenera.

Columnas: `categoria, nombre, etiqueta_corta, inicio_1based, fin_1based, hebra,
clasificacion_ensembl, clasificacion_encode, estado, fuente`.

Convención de coordenadas: **1-based, inclusivo en ambos extremos**, ensamblado
**GRCh38.p14**, cromosoma 16. Los intervalos tomados de archivos BED (ENCODE cCRE y
GeneHancer vía UCSC, que son 0-based semiabiertos) fueron convertidos sumando 1 al
inicio y dejando el fin sin cambios, antes de cargarlos al CSV.

---

## 2. Script de generación

`figuras/generar_figuras_locus.py`

Entorno de ejecución declarado: Python 3.10.12, matplotlib 3.10.9, backend `Agg`.
`svg.fonttype: none` (el texto del SVG queda como texto editable, no como trazado).

Salidas por figura: `.svg` (editable), `.pdf` (vectorial), `.png` a 300 dpi.

Intervalo graficado, idéntico en ambas figuras: **chr16:53.703.300-53.704.900**
(1.600 pb). Misma escala, mismo ancho de lienzo y mismo eje horizontal, de modo que
las dos figuras se pueden apilar y leer en registro vertical.

Reproducción:

```
cd 02_obligatorio/temas_candidatos/figuras
python3 generar_figuras_locus.py
```

---

## 3. Tabla fuente de coordenadas

| # | Categoría | Elemento | Inicio (1-based) | Fin (1-based) | Hebra | Fuente |
|---|-----------|----------|------------------|---------------|-------|--------|
| 1 | transcrito | RPGRIP1L-212 (ENST00000647211.2) | 53.598.153 | 53.703.859 | − | Ensembl 116 |
| 2 | transcrito | FTO-206 (ENST00000471389.6) | 53.704.156 | 54.121.941 | + | Ensembl 116 |
| 3 | exón | Exón 1 de FTO-206 (ENSE00003793523) | 53.704.156 | 53.704.229 | + | Ensembl 116 |
| 4 | TSS | TSS de referencia de RPGRIP1L | 53.703.859 | 53.703.859 | − | Ensembl 116 |
| 5 | TSS | Inicio alternativo de RPGRIP1L | 53.703.938 | 53.703.938 | − | Ensembl 116 |
| 6 | TSS | Inicio alternativo de FTO | 53.703.963 | 53.703.963 | + | Ensembl 116 |
| 7 | TSS | TSS de referencia de FTO | 53.704.156 | 53.704.156 | + | Ensembl 116 |
| 8 | Ensembl RB | ENSR16_9RBJ8 — enhancer | 53.703.398 | 53.703.830 | . | Ensembl Regulatory Build 116 |
| 9 | Ensembl RB | ENSR16_9RBJC — promotor | 53.703.831 | 53.704.167 | . | Ensembl Regulatory Build 116 |
| 10 | Ensembl RB | ENSR16_BDMQQ — enhancer | 53.704.168 | 53.704.740 | . | Ensembl Regulatory Build 116 |
| 11 | ENCODE cCRE | EH38E1816375 — PLS (score 326) | 53.703.562 | 53.703.761 | . | ENCODE cCRE vía UCSC |
| 12 | ENCODE cCRE | EH38E1816376 — PLS (score 682) | 53.703.859 | 53.704.208 | . | ENCODE cCRE vía UCSC |
| 13 | ENCODE cCRE | EH38E1816377 — pELS (score 214) | 53.704.523 | 53.704.689 | . | ENCODE cCRE vía UCSC |
| 14 | GeneHancer | GH16J053703 — Promoter/Enhancer, elite | 53.703.192 | 53.705.162 | . | GeneHancer vía UCSC |
| 15 | región | Centro del promotor divergente FTO–RPGRIP1L | 53.703.921 | 53.703.991 | . | intervalo de rastreo regional |
| 16 | región | Región promotora próxima al TSS de referencia de FTO | 53.704.020 | 53.704.145 | . | intervalo de rastreo regional |
| 17 | región | Región codificante del exón 1 del transcrito de referencia de FTO | 53.704.181 | 53.704.251 | . | intervalo de rastreo regional |
| 18 | región | Región intrónica con firma pELS | 53.704.571 | 53.704.641 | . | intervalo de rastreo regional |

Aclaraciones sobre las filas 15 a 18: son **intervalos de rastreo regional**, no la
extensión de un protoespaciador. Definen la ventana dentro de la cual se buscan
secuencias con PAM NGG; el protoespaciador mide 20 pb y queda contenido en la ventana.
La figura 3 grafica las ventanas, no las guías.

Aclaraciones sobre las filas 1, 2 y 14: los tres elementos exceden el intervalo
graficado. En ambas figuras se representan truncados, con flecha en el o los extremos
que salen del encuadre.

Distancias derivadas que aparecen anotadas en la figura 2, calculadas a partir de la
tabla y no cargadas a mano: 53.704.156 − 53.703.859 = **297 pb** entre los dos TSS de
referencia; 53.703.963 − 53.703.938 = **25 pb** entre los dos inicios alternativos.

---

## 4. Leyenda final — Figura 2

> **Figura 2. Arquitectura del promotor divergente FTO–RPGRIP1L en chr16:53.703.300-53.704.900 (GRCh38.p14).**
> **(A)** Transcritos de referencia y sitios de inicio de transcripción. *RPGRIP1L-212*
> (ENST00000647211.2) se transcribe desde la hebra menos y su TSS de referencia se ubica
> en 53.703.859; *FTO-206* (ENST00000471389.6) se transcribe desde la hebra más y su TSS
> de referencia se ubica en 53.704.156. Ambos TSS de referencia están separados por
> 297 pb y se orientan en sentidos opuestos, configuración compatible con un promotor
> divergente. Los dos triángulos grises marcan inicios alternativos anotados —uno de
> *RPGRIP1L* en 53.703.938 y uno de *FTO* en 53.703.963—, separados entre sí por 25 pb;
> su presencia implica que la región intergénica no es transcripcionalmente neutra. El
> exón 1 de *FTO-206* aparece sombreado. Los cuerpos génicos se extienden más allá del
> encuadre, indicado por flechas en los extremos.
> **(B)** Anotación regulatoria en el mismo intervalo y a la misma escala. La pista
> Ensembl Regulatory Build muestra el elemento ENSR16_9RBJC clasificado como promotor
> (destacado), flanqueado por dos elementos clasificados como enhancer. La pista ENCODE
> cCRE muestra dos elementos con firma de promotor (PLS) y uno con firma de enhancer
> proximal (pELS). La pista GeneHancer muestra el elemento integrado GH16J053703, que
> excede el intervalo graficado en ambos extremos.
> Coordenadas en escala genómica 1-based, ensamblado GRCh38.p14; anotación de transcritos
> de Ensembl release 116 / GENCODE release 50; elementos regulatorios de Ensembl
> Regulatory Build 116, ENCODE cCRE y GeneHancer, estos dos últimos consultados vía UCSC.
> Figura generada con Python y matplotlib a partir de la tabla `coordenadas_locus_fto.csv`.

Nota de lectura para el cuerpo del texto: la figura documenta que las anotaciones
disponibles no asignan la región regulatoria de forma exclusiva a *FTO*. Es el sustento
gráfico del argumento de que activar esta región implica evaluar también el efecto sobre
*RPGRIP1L*.

---

## 5. Leyenda final — Figura 3

> **Figura 3. Regiones evaluadas como blanco de dCas9-p300 en el promotor divergente
> FTO–RPGRIP1L.** Mismo intervalo, misma escala y mismo eje que la figura 2
> (chr16:53.703.300-53.704.900, GRCh38.p14), de modo que ambas figuras se leen en
> registro vertical. Los bloques numerados 1 a 4 representan **intervalos de rastreo
> regional**, es decir, las ventanas dentro de las cuales se buscaron secuencias
> protoespaciadoras de 20 pb adyacentes a un PAM NGG; no representan la extensión de una
> guía individual. La región 3 (codificante del exón 1 del transcrito de referencia de
> *FTO*) fue **retirada durante la selección** y se distingue por trama rayada, contorno
> discontinuo y rótulo explícito, además del color. Las regiones 1, 2 y 4 se conservaron
> en el panel evaluado. Se mantienen como referencia posicional los TSS de referencia de
> ambos genes y los dos inicios alternativos. El detalle de cada región —contexto
> genómico, clasificación en Ensembl Regulatory Build y clasificación en ENCODE cCRE—
> figura en la leyenda ubicada bajo el eje.
> Figura generada con Python y matplotlib a partir de la misma tabla de coordenadas que
> la figura 2.

Nota de lectura para el cuerpo del texto: la retirada de la región 3 no se presenta como
un error corregido sino como el resultado del criterio de selección aplicado, que
descarta ventanas cuyo protoespaciador cae dentro de secuencia codificante del transcrito
de referencia.

---

## 6. Nota de trazabilidad

1. **Fuente única.** Las dos figuras se generan de la misma tabla. No hay coordenadas
   duplicadas entre archivos ni escritas dentro del código, de modo que las dos figuras
   no pueden divergir entre sí.
2. **Origen de cada dato.** Cada fila de la tabla declara su fuente en la columna
   `fuente`. Ninguna coordenada proviene de lectura visual de un navegador genómico ni
   de exportación desde Benchling.
3. **Versiones declaradas.** GRCh38.p14; Ensembl release 116; GENCODE release 50;
   Ensembl Regulatory Build 116; ENCODE cCRE y GeneHancer consultados vía UCSC sobre
   GRCh38. No se mezclan coordenadas de hg19 con coordenadas de GRCh38 en ningún punto.
4. **Normalización de convenciones.** Todo el conjunto está en 1-based inclusivo. Los
   intervalos originalmente en BED fueron convertidos antes de cargarse.
5. **Reproducibilidad.** Ejecutar el script sobre el CSV regenera los seis archivos de
   salida sin intervención manual. No hay retoque posterior en editor gráfico.
6. **Alcance de lo graficado.** La figura 3 grafica ventanas de rastreo, no guías
   seleccionadas. La selección definitiva de guías —que requiere corrida de CRISPOR con
   versión y genoma declarados, actividad predicha, análisis de sitios fuera de blanco y
   frecuencias poblacionales de variantes— está pendiente y no se representa en ninguna
   de las dos figuras.
