---
type: procedimiento
status: current
date: 2026-07-26
source: "Definido en sesión del 2026-07-26. Coordenadas verificadas contra FTO_RPGRIP1L_W1-W4_GRCh38_sin_guias.gb y DECISIONES_DISENO.md (D0, D1, D2). Formato de oligo verificado contra 03_informe/protocolo_1_clonado.md."
related:
  - "[[02_obligatorio/temas_candidatos/DECISIONES_DISENO]]"
  - "[[02_obligatorio/temas_candidatos/FTO_anexo_tecnico/09_panel_cuatro_ventanas]]"
---

# Procedimiento de diseño y evaluación de guías

Especificación del método, fijada **antes** de generar resultados. Su función es que la selección de guías sea reproducible y auditable, y que ningún criterio se defina después de haber visto los datos.

## 1. Alcance

Este procedimiento produce, para cada región blanco, el universo completo de protoespaciadores NGG con sus atributos. **No selecciona guías.** La selección es una decisión posterior y separada, que se documentará en `DECISIONES_DISENO.md`.

Se mantienen separadas dos decisiones que no deben mezclarse: qué regiones vale la pena interrogar biológicamente, que ya está resuelto y documentado, y qué protoespaciador concreto representa mejor a cada región, que es lo que este procedimiento aborda.

**Las candidatas identificadas en corridas anteriores no constituyen una preselección.** Se emplean únicamente en el paso 8, como control de reproducibilidad.

## 2. Unidades de consulta

Se envían a CRISPOR cuatro secuencias independientes. Cada una lleva **flancos de 50 pb a cada lado** de la región declarada, porque CRISPOR solo reporta protoespaciadores cuyo conjunto de 23 nt entra completo en la secuencia enviada, y los puntajes de actividad requieren además cuatro nucleótidos previos y tres posteriores. Sin flancos se perderían las guías del borde y quedarían sin puntaje las de los extremos.

| Consulta | Región declarada | Coordenadas GRCh38 de la región | Longitud | Secuencia a enviar, con flancos |
| :--- | :--- | :--- | :--- | :--- |
| Q1 | Promotor divergente compartido, elemento ENSR16_9RBJC | chr16:53.703.831-53.704.167 | 337 pb | chr16:53.703.781-53.704.217 |
| Q2 | Región intrónica con firma pELS, EH38E1816377 | chr16:53.704.522-53.704.689 | 168 pb | chr16:53.704.472-53.704.739 |
| Q3 | Región exónica retirada, W2 | chr16:53.704.181-53.704.251 | 71 pb | chr16:53.704.131-53.704.301 |

**Decisión sobre el bloque promotor.** Q1 abarca el elemento Ensembl completo y no los recortes W1 y W4. El motivo es que W1 y W4 son subregiones definidas por el proyecto dentro de un mismo elemento, separadas entre sí por 29 pb, y heredarlas como unidades de consulta impondría de antemano una partición que conviene que surja del análisis. Al correr el elemento entero, la posición de cada protoespaciador queda descrita como variable continua mediante sus cuatro distancias, y la pertenencia a W1 o a W4 se asigna después. Q2, en cambio, corresponde a un objeto de base de datos y no a un recorte propio, de modo que se conserva como está.

**Q3 se corre para documentación, no para selección.** W2 está retirada por decisión registrada en D4.2. Su universo de protoespaciadores se genera para poder responder con datos qué se descartó y por qué, que es una de las preguntas previstas de la oral.

Las tres secuencias se extraen del archivo `FTO_RPGRIP1L_W1-W4_GRCh38_sin_guias.gb`, cuya secuencia fue verificada contra la API REST de Ensembl.

## 3. Parámetros declarados de CRISPOR

| Parámetro | Valor |
| :--- | :--- |
| Instancia | crispor.gi.ucsc.edu |
| Versión | 5.2 |
| Genoma | Homo sapiens, NCBI GCF_000001405.40, GRCh38.p14 |
| PAM | 20bp-NGG, SpCas9 |
| Puntaje de actividad de referencia | Doench 2016 (Azimuth) |

**Fundamento del puntaje elegido.** El manual de CRISPOR establece que el puntaje de Doench 2016 es el que mejor se comporta para guías expresadas desde promotor U6, y que el de Moreno-Mateos corresponde a expresión in vitro con T7. El sistema del curso, pX459, expresa el ARN guía desde U6. Los demás puntajes se registran pero no se usan como criterio.

Se conserva el identificador de lote de cada corrida para trazabilidad.

## 4. Regla de pertenencia

Un protoespaciador pertenece a una región cuando **sus 20 nucleótidos quedan íntegramente dentro de las coordenadas declaradas de esa región**. El PAM puede caer fuera. Los protoespaciadores que quedan solo en los flancos se registran como fuera de región y no se evalúan.

Dentro de Q1, la asignación posterior a W1 o a W4 sigue el mismo criterio de contención íntegra, con W1 en chr16:53.703.921-53.703.991 y W4 en chr16:53.704.020-53.704.145. Los protoespaciadores del elemento que no caen en ninguna de las dos se conservan igual, porque pueden ofrecer posiciones mejores que los recortes actuales.

## 5. Campos a registrar por candidato

Todos son computables a partir de la salida de CRISPOR y del GenBank curado. Ninguno requiere juicio.

| Campo | Fuente |
| :--- | :--- |
| Secuencia genómica forward | GenBank curado |
| Protoespaciador y PAM | CRISPOR |
| Hebra | CRISPOR |
| Coordenadas GRCh38 del protoespaciador | Cálculo sobre el desplazamiento declarado |
| Distancia a los cuatro puntos de inicio | Cálculo contra 53.703.859, 53.703.938, 53.703.963 y 53.704.156 |
| Contexto exónico, intrónico o promotor | GenBank curado |
| Elemento Ensembl y cCRE ENCODE superpuestos | GenBank curado |
| Contenido GC | Cálculo |
| Corridas de timidinas | Cálculo |
| **Presencia de sitio BbsI** | Cálculo, motivos GAAGAC y GTCTTC |
| **Primera base del protoespaciador** | Cálculo |
| Actividad predicha | CRISPOR, Doench 2016 |
| Especificidad MIT y CFD | CRISPOR |
| Off-targets por número de desapareamientos | CRISPOR |
| Estado de la semilla | CRISPOR, conteo con y sin desapareamiento en los 12 pb contiguos al PAM |
| Variantes superpuestas y frecuencias | Ensembl, **separando las que caen en la semilla de las distales** |
| Efecto de barrera transcripcional según hebra | Cálculo, solo cuando el protoespaciador está dentro de una unidad transcrita |
| Marca de motivo Graf | CRISPOR |

**Sobre el campo de BbsI.** El clonado del curso digiere pX459 con BbsI. Un protoespaciador que contenga el sitio de reconocimiento de esa enzima impide el clonado. El chequeo se aplica a los 20 nt del protoespaciador, que es lo que se sintetiza en el oligo, y no al PAM.

**Sobre la primera base.** El formato de oligo del protocolo es CACCG seguido de 19 nucleótidos, de modo que el primer nucleótido del protoespaciador queda sustituido por G cuando no es G de origen. Se registra si la guía empieza con G naturalmente, porque de lo contrario la secuencia expresada difiere de la genómica en una posición.

**Sobre la hebra.** *FTO* se transcribe en hebra positiva, por lo que su hebra molde es la negativa. Un protoespaciador anotado en hebra positiva genera un ARN guía que aparea con la molde, condición descrita como neutral para la elongación. Uno anotado en hebra negativa aparea con la no molde, condición asociada a pausa de la ARN polimerasa II. El criterio **solo aplica dentro de unidades transcritas** y no reemplaza a los demás.

## 6. Filtros duros

Eliminan la candidata sin compensación posible. Se fijan antes de ver los resultados.

1. Corrida de cuatro o más timidinas en el protoespaciador, por terminación de la ARN polimerasa III en el sistema U6.
2. Presencia de sitio BbsI en el protoespaciador, por incompatibilidad con el clonado del curso.
3. Puntaje de especificidad MIT menor a 50, que es el umbral que el manual de CRISPOR declara para una guía adecuada.

## 7. Criterios de ranking

Admiten compensación entre sí y no eliminan por sí solos. Se ponderan al comparar candidatas dentro de una misma región.

1. Actividad predicha por Doench 2016.
2. Contenido GC, penalizando por debajo de 20 % y por encima de 80 %.
3. Densidad de variantes superpuestas, con mayor peso a las que caen en la semilla y a las que figuran en ClinVar.
4. Off-targets exónicos y off-targets con bajo número de desapareamientos.
5. Perfil de distancias a los cuatro puntos de inicio.
6. Hebra, cuando la candidata está dentro de una unidad transcrita.
7. Ausencia de motivo Graf.

## 8. Verificación

1. Contraste de las coordenadas calculadas contra el GenBank curado.
2. Comprobación de que el número de sitios NGG por región se informa **normalizado por longitud**, dado que las regiones tienen tamaños distintos.
3. Cotejo final contra las candidatas de corridas anteriores, registrado en `06_tabla_guias_candidatas.md` y `09_panel_cuatro_ventanas.md`. Su reaparición o su ausencia se informa como resultado, no como validación del método.

## 9. Lo que este procedimiento no resuelve

1. La extensión espacial de la acetilación depositada por dCas9-p300, que condiciona si W1 y W4 formulan preguntas distinguibles. Es un dato de Hilton et al. (2015) y se resuelve por lectura, no por diseño de guías.
2. La actividad de cualquiera de estas regiones en granulosa, que ninguna anotación ni ningún puntaje demuestra.
3. La selección final de guías y la composición definitiva del panel.
