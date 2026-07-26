# Contenido visual de las diapositivas

Complemento del guion `guion_seminario_edicion_epigenetica_v2.md`. Por cada slide: distribución (cómo se reparte la diapositiva) y el texto literal que va en pantalla. Carga de texto media: frases cortas, no párrafos. El desarrollo largo queda en el guion oral.

## Sistema visual (aplica a todo)

Formato 16:9. Banda de título arriba (una franja de color sólido). Pie constante en todas: "Xiao et al., 2019 · PNAS 116(1):255-260" y número de slide.
Código de color: verde para activación / efector catalítico ON (GCN5); rojo para represión (Sir2a); azul/gris neutro para estructura y controles.
Tipografía sans-serif. Los recuadros llevan un título en negrita y una línea de contenido.

---

## Slide 1 · Portada

Distribución: título centrado grande, subtítulo debajo, un esquema conceptual en el centro-inferior, pie con datos del grupo.

Texto en pantalla:
- Título: "Edición epigenética con CRISPR/dCas9"
- Subtítulo: "Activar y reprimir genes sin cortar el ADN"
- Línea de referencia: "Xiao et al., 2019 · PNAS · caso: *Plasmodium falciparum*"
- Pie: integrantes del grupo · Taller de Ingeniería Genética · fecha

Esquema (dibujado, no foto): un óvalo rotulado "dCas9" sobre una doble hélice, con un "sgRNA" saliendo de él y, al lado, una histona con una etiqueta "Ac". Dos flechas curvas: una verde hacia arriba con "ON", una roja hacia abajo con "OFF".

---

## Slide 2 · Por qué el CRISPR clásico no alcanza

Distribución: título arriba. Debajo, tres recuadros iguales en fila horizontal (los tres obstáculos). En la esquina superior derecha, un número grande de impacto. Una franja ancha al pie con la conclusión.

Texto en pantalla:
- Título: "Por qué el CRISPR clásico no alcanza"
- Número de impacto (esquina): "≈ 500.000 muertes/año"
- Recuadro 1 · "Recombinación homóloga baja": "cambios dirigidos ineficientes"
- Recuadro 2 · "Sin ARN de interferencia": "no hay silenciamiento reversible"
- Recuadro 3 · "Genoma haploide": "romper un gen esencial es letal"
- Franja al pie: "Hace falta regular la expresión sin cortar el ADN y de forma reversible"

Sin figura del paper. Un ícono simple por recuadro es suficiente (una hebra, un ARN tachado, un cromosoma único).

---

## Slide 3 · La receta: dCas9 + efector

Distribución: título arriba. Cuerpo partido en dos mitades verticales. Mitad izquierda: "Pieza 1", con un esquema del complejo. Mitad derecha: "Pieza 2", con dos recuadros apilados.

Texto en pantalla:
- Título: "La receta general: dCas9 + efector"
- Encabezado izquierda: "1 · dCas9: direcciona, no corta"
- Bullets izquierda (junto al esquema): "sgRNA aparea con una cadena del ADN"; "PAM (NGG): lo reconoce la proteína"; "D10A inactiva RuvC · H840A inactiva HNH"; "mismo reconocimiento, sin corte"
- Encabezado derecha: "2 · Efector: qué hace en el sitio"
- Recuadro verde · "Catalítico": "una enzima escribe o borra la marca por sí misma (HAT / HDAC)"
- Recuadro gris · "Reclutador": "no modifica; atrae maquinaria endógena (p. ej. VPR)"
- Nota al pie de la mitad derecha: "Esta distinción reaparece en los resultados"

Esquema izquierda (dibujado): el óvalo dCas9 sobre la doble hélice, con el sgRNA apareado, el "PAM" marcado justo al lado del sitio, y los dos dominios "RuvC" y "HNH" señalados y tachados con sus mutaciones.

---

## Slide 4 · El efector catalítico: acetilasa o deacetilasa

Distribución: título arriba. Izquierda: esquema del nucleosoma con los dos estados y la carga de la lisina. Derecha: dos recuadros con las dos clases de enzima, cada uno cerrando con la enzima concreta del paper. Franja fina al pie con la validación.

Texto en pantalla:
- Título: "El efector: acetilasa (activa) o deacetilasa (reprime)"
- Esquema izquierda, estado de arriba: "lisina acetilada → carga neutralizada → cromatina abierta → gen activo"
- Esquema izquierda, estado de abajo: "lisina sin acetilar → carga + → cromatina compacta → gen reprimido"
- Recuadro verde · "Acetiltransferasa (HAT)": "escribe la marca → activa. En el paper: PfGCN5"
- Recuadro rojo · "Deacetilasa (HDAC)": "retira la marca → reprime. En el paper: PfSir2a (dependiente de NAD)"
- Nota entre los recuadros: "se eligen las enzimas endógenas del propio parásito"
- Franja al pie: "Validación previa (Western + inmunofluorescencia): las dos construcciones se expresan y se enriquecen en el núcleo"

Figura: como inset chico, el esquema de dominios de la Fig. 1 A y B (Hsp86 – 3xFLAG – NLS – dCas9 – NLS – linker – efector), para mostrar que solo cambia el bloque final.

---

## Slide 5 · Activar rh4: unión y marca

Distribución: título arriba. Figura grande a la derecha (dos tercios). Columna de texto a la izquierda (un tercio) con el motivo arriba y la barra de tres pasos. Cinta de "3 pasos" cruzando bajo el título.

Texto en pantalla:
- Título: "Activar *rh4* con dCas9-GCN5 (efector catalítico)"
- Cinta de pasos (bajo el título): "① Unión ✓   ② Marca ✓   ③ Transcripción (pendiente)"
- Recuadro motivo (arriba izquierda): "¿Una acetiltransferasa reclutada enciende un gen silenciado? *rh4* está apagado en la cepa Dd2"
- Bullet B: "ChIP anti-FLAG → la dCas9-GCN5 ocupa el TSS de *rh4*"
- Bullet C: "ChIP anti-H3 acetilada → hiperacetilación en el locus"

Figura: Fig. 2, paneles A (mapa del gen con el sgRNA y el TSS), B (ChIP anti-FLAG) y C (ChIP anti-H3ac).

---

## Slide 6 · Activar rh4: transcripción, fenotipo y GCN5 vs VPR

Distribución: título arriba. Figura a la izquierda (paneles D y E). Derecha: dato ancla grande arriba, dos bullets debajo, y un recuadro comparativo de dos columnas al pie.

Texto en pantalla:
- Título: "Activar *rh4*: efecto en transcripción y en invasión"
- Cinta de pasos completa: "① Unión ✓   ② Marca ✓   ③ Transcripción ✓"
- Dato ancla (grande, derecha): "*rh4* ≥ 113×" (subtítulo: "potencia de activación del sistema")
- Bullet D: "RT-qPCR: *rh4* aumenta su expresión; *ama1* no cambia (control de especificidad)"
- Bullet E: "Invade eritrocitos tratados con neuraminidasa (vía independiente de ácido siálico)"
- Recuadro comparativo, columna verde "GCN5 (catalítico)": "más marca, más activación"
- Recuadro comparativo, columna gris "VPR (reclutador)": "más ocupancia, menos marca, activa menos"

Figura: Fig. 2, paneles D (RT-qPCR) y E (invasión).

---

## Slide 7 · Reprimir eba-175: el experimento espejo

Distribución: título arriba. Figura grande centrada o a la derecha (Fig. 3 completa). Columna de texto con motivo y tres bullets. Franja destacada al pie ("Lección de diseño") con un recuadro-figura chico de la S4.

Texto en pantalla:
- Título: "Reprimir *eba-175* con dCas9-Sir2a"
- Recuadro motivo: "El sentido inverso, con una deacetilasa. *eba-175*, muy expresado en 3D7"
- Bullet B-C: "ChIP: ocupancia de la dCas9 + hipoacetilación del locus"
- Bullet D: "RT-qPCR: *eba-175* disminuye; *ama1* y control GFP sin cambio"
- Bullet E: "Invasión con quimotripsina: menos de la mitad de la silvestre"
- Franja al pie · "Lección de diseño": "Un sgRNA lejos del TSS se une pero NO reprime → diseñar el guía cerca del TSS"

Figura: Fig. 3 (A a E) como principal; Fig. S4 como recuadro pequeño dentro de la franja de la lección.

---

## Slide 8 · Reprimir un gen esencial: PfSET1

Distribución: título arriba. Figura a la derecha (paneles A, B y D). Izquierda: recuadro motivo destacado arriba, tres bullets de resultado, y un recuadro de implicancia al pie.

Texto en pantalla:
- Título: "Reprimir un gen esencial: *PfSET1*"
- Recuadro motivo (destacado): "Lo que un knockout no puede: *PfSET1* es esencial, eliminarlo es letal"
- Bullet 1: "Represión reversible → 322 genes con expresión reducida (secuenciación de ARN)"
- Bullet 2: "Ortólogos en *P. berghei*: 50% esenciales · 31% dispensables · 19% lento"
- Bullet 3: "Citometría: retraso de crecimiento desde el trofozoíto"
- Recuadro implicancia (verde/azul): "La demostración más fuerte de la técnica: alcanza genes esenciales, vedados al knockout"

Figura: Fig. 4, paneles A (RT-qPCR), B (torta de fenotipos), C (mapa de calor) y D (citometría de flujo).

---

## Slide 9 · Hasta dónde llega: especificidad y cobertura

Distribución: título arriba. Cuerpo en dos mitades. Izquierda "Específico" con la Fig. S5. Derecha "Cobertura" con la Fig. S8 y los datos.

Texto en pantalla:
- Título: "Hasta dónde llega: específico y de amplio alcance"
- Encabezado izquierda: "Específico"
- Bullets izquierda: "Secuenciación de ARN: pocos cambios fuera del blanco"; "*pebl* co-activado por promotor bidireccional → alcanza no codificantes"; "*stevor*: único off-target candidato"
- Encabezado derecha: "Casi todo el genoma es blanco"
- Bullets derecha: "261.196 PAM NGG + 727.817 NGA"; ">173× de cobertura sobre ~5.700 genes"; "Límite real: la proximidad al TSS, no el sitio"

Figuras: Fig. S5 (gráfico de dispersión de transcriptomas) a la izquierda; Fig. S8 (densidad de PAM) a la derecha.

---

## Slide 10 · La edición no es permanente

Distribución: título arriba. Dos recuadros enfrentados. Franja al pie con la delimitación de uso.

Texto en pantalla:
- Título: "Una edición reversible, no permanente"
- Recuadro izquierda · "No perdura": "no modifica el ADN + expresión episomal → el efecto revierte y no se hereda entre generaciones"
- Recuadro derecha · "No es un problema acá": "para estudiar función génica de forma controlada, la reversibilidad es una ventaja"
- Franja al pie: "Adecuada para interrogar la función de un gen; no para un cambio definitivo o heredable (ese es el terreno del KO, base y prime editing)"

Esquema (dibujado): línea de tiempo con la construcción episomal presente (gen regulado) y, al retirarse, el gen que vuelve a su estado original, para ilustrar la reversibilidad.

---

## Slide 11 · Conclusiones

Distribución: título arriba. Tres recuadros en fila con las conclusiones. Franja ancha al pie con la ubicación entre técnicas. Al costado, repetir en chico el esquema de la portada para cerrar.

Texto en pantalla:
- Título: "Conclusiones"
- Recuadro 1: "Activar y reprimir genes sin cortar el ADN, de forma reversible"
- Recuadro 2: "Dos vías de invasión (*rh4*, *eba-175*) y un gen esencial (*PfSET1*)"
- Recuadro 3: "Cobertura genómica casi total"
- Franja al pie: "Distinta del KO por Cas9 y de base/prime editing (cambian la secuencia) · misma lógica que CRISPRi y CRISPRa"

Esquema al costado: el mismo dibujo de dCas9 + histona de la portada, en tamaño reducido.
