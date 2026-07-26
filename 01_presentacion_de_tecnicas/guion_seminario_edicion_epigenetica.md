# Guion del seminario: Edición epigenética por CRISPR/dCas9

## Índice operativo

Modalidad 1 (Presentación de técnicas, 15 pts). Fecha: martes 21/07. Formato: grupo de 3, 20 minutos.
Técnica: edición epigenética mediante dCas9 fusionado a efectores de acetilación de histonas.
Paper base (fuente de verdad, caso central): Xiao B, Yin S, Hu Y, et al. (2019). Epigenetic editing by CRISPR/dCas9 in *Plasmodium falciparum*. *PNAS* 116(1):255-260. Apéndice: pnas.1813542116.sapp.

Qué contiene: estructura de 20 minutos slide por slide, con el visual asignado a cada uno (figura del paper o del apéndice) y las notas de exposición redactadas en registro académico-técnico. Los datos provienen únicamente del paper y su apéndice; toda cifra es trazable a una figura o al texto.

Nota de escritura: guion sujeto a `Rules_Of_Writing.md`. Las notas de exposición son prosa; la lista de contenidos de cada slide es material de referencia y usa numeración por conveniencia operativa.

Alerta de fuente marcada en el slide 8: el encabezado de sección del paper indica que la activación de *rh4* aumenta una vía "sialic acid-dependent", mientras que el mecanismo descrito (invasión de eritrocitos tratados con neuraminidasa) y el abstract corresponden a la vía sialic acid-**independiente**. Se expone la versión coherente con el mecanismo y se deja constancia de la discrepancia.

---

## Reparto temporal (referencia)

Contexto y herramienta, slides 1 a 6, alrededor de 7 minutos. Pruebas de concepto (activación y represión), slides 7 a 10, alrededor de 8 minutos. Alcance, especificidad y cierre, slides 11 a 14, alrededor de 5 minutos.

---

## Slide 1. Portada

Contenido:
1. Título: "Edición epigenética con CRISPR/dCas9 en *Plasmodium falciparum*".
2. Subtítulo: reprogramar la transcripción sin cortar el ADN.
3. Referencia del paper (Xiao et al., 2019, PNAS) e integrantes del grupo.

Notas: presentación breve del encuadre. La técnica pertenece a la categoría de modificación epigenética del temario; se presenta a través de un caso publicado que la aplica a un organismo donde la edición genómica convencional es particularmente difícil.

---

## Slide 2. El problema: editar el genoma de *P. falciparum*

Contenido:
1. *P. falciparum* causa la forma más letal de malaria, con cerca de medio millón de muertes anuales.
2. Tres obstáculos para su manipulación genética: baja eficiencia de recombinación homóloga, ausencia de la maquinaria de RNAi y genoma haploide.
3. Consecuencia: los abordajes de disrupción génica son limitados, sobre todo para genes esenciales y para ARN no codificantes ubicados en exones o intrones.

Notas: la ausencia de RNAi elimina la vía clásica de silenciamiento reversible, y el genoma haploide implica que la disrupción de un gen esencial es directamente letal, lo que impide estudiar su función por knockout. Es por ello que se necesita una herramienta que module la expresión de forma reversible y sin romper el ADN. Este es el vacío que el trabajo busca cubrir.

---

## Slide 3. Marco: acetilación de histonas y transcripción

Contenido:
1. Las modificaciones dinámicas de histonas en la región del sitio de inicio de la transcripción (TSS) regulan la expresión génica en eucariotas.
2. En *P. falciparum*, la acetilación de H3K9 y H3K14 en el TSS se asocia con genes activos; su remoción, con represión.
3. Dos enzimas del propio parásito son las herramientas: PfGCN5 (histona acetiltransferasa, HAT) escribe la marca; PfSir2a (histona deacetilasa, HDAC, dependiente de NAD+) la borra.

Notas: la acetilación neutraliza la carga de las lisinas del extremo N-terminal de H3 y H4, relaja la cromatina y facilita la transcripción. PfSir2a remueve acetilación en múltiples lisinas de H3 y H4; PfGCN5 está ampliamente asociada a la acetilación de H3K9 y H3K14 en los genes del parásito. Al ser enzimas endógenas, su actividad es compatible con el contexto de cromatina del organismo.

---

## Slide 4. El salto conceptual: de cortar a reclutar

Contenido:
1. Cas9 convencional corta el ADN y genera cambios permanentes (knockout, inserción, reemplazo alélico).
2. dCas9 es un mutante nulo de nucleasa (mutaciones D10A y H840A) que conserva la unión al ADN guiada por sgRNA pero no corta.
3. Fusionando un efector epigenético al dCas9, se lleva la actividad enzimática al TSS del gen blanco: se reprograma la transcripción sin tocar la secuencia.

Notas: la diferencia con el knockout es sustancial; acá no hay ruptura de doble cadena ni reparación, por lo que el genoma queda intacto y el efecto es reversible. La lógica es la misma que la de CRISPRi y CRISPRa en otros eucariotas, con la particularidad de que este trabajo usa efectores de acetilación en lugar de dominios represores tipo KRAB. Sobre esta base se construyen las dos herramientas del paper.

---

## Slide 5. Diseño de las dos herramientas (Fig. 1 A y B)

Visual: Figura 1, paneles A (activación, dCas9-GCN5) y B (represión, dCas9-Sir2a).

Contenido:
1. Arquitectura de la proteína recombinante: promotor 5' Hsp86, epitope 3xFLAG, NLS, dCas9 (D10A/H840A), segundo NLS, linker glicina-serina (GS3) y dominio efector en el extremo C-terminal.
2. Activación (ON): dCas9-GCN5 deposita acetilación en el TSS.
3. Represión (OFF): dCas9-Sir2a remueve acetilación en el TSS.

Notas: el 3xFLAG permite detectar y seguir la proteína; los dos NLS aseguran la importación al núcleo del parásito; el linker GS3 da flexibilidad y una conformación extendida para que el dominio efector alcance la cromatina sin que el dCas9 lo impida estéricamente. La expresión es episomal (por plásmido), de modo que no hay integración en el genoma. Es el mismo esqueleto para las dos funciones, y solo cambia el dominio efector fusionado.

---

## Slide 6. Validación: expresión y localización nuclear (Fig. 1 C-F)

Visual: Figura 1, paneles C y D (Western blot) y E y F (inmunofluorescencia).

Contenido:
1. Western blot con anti-Cas9 confirma la expresión de dCas9-GCN5 y dCas9-Sir2a del tamaño esperado; actina como control de carga.
2. Inmunofluorescencia con anti-FLAG muestra señal solapada con la tinción de DAPI: las dos proteínas se enriquecen en el núcleo.
3. Se incluye un dCas9-GFP como control negativo (línea 3D7-dCas9-GFP).

Notas: la validación es un requisito previo; antes de medir cualquier efecto sobre la transcripción hay que demostrar que la proteína se expresa y llega al núcleo, donde está la cromatina. La colocalización con DAPI cumple ese punto para las dos versiones. Cabe mencionar que en algunas líneas se observan niveles bajos de proteína o posible clivaje, un detalle que se retoma al discutir la robustez del sistema.

---

## Slide 7. Prueba de concepto I: activación de *rh4*, unión y marca (Fig. 2 A-C)

Visual: Figura 2, paneles A (mapa del gen y posición del sgRNA), B (ChIP anti-FLAG) y C (ChIP anti-acetil-H3).

Contenido:
1. Blanco: *rh4*, que controla la vía de invasión independiente de ácido siálico y está silenciado en la cepa Dd2.
2. RH4sgRNA1 dirige dCas9-GCN5 a la región del TSS; ChIP con anti-FLAG confirma ocupancia alta y específica del dCas9 en ese locus (línea Dd2-GCN5-R1).
3. ChIP con anti-acetil-H3 confirma hiperacetilación de H3 a lo largo de *rh4*, consistente con la actividad HAT reclutada.

Notas: la secuencia lógica del experimento es unión, marca y transcripción. Los paneles B y C cubren los dos primeros pasos: el dCas9 se ubica donde se lo dirige y deja la marca epigenética esperada. La cepa Dd2 es un buen modelo porque *rh4* parte de un estado silenciado, de modo que cualquier activación se mide sobre un fondo bajo.

---

## Slide 8. Prueba de concepto I: activación de *rh4*, transcripción y fenotipo (Fig. 2 D-E)

Visual: Figura 2, paneles D (RT-qPCR) y E (ensayo de invasión).

Contenido:
1. RT-qPCR: *rh4* alcanza al menos 113 veces más transcripción en Dd2-GCN5-R1 que en Dd2 silvestre; *ama1*, gen del mismo estadio usado como control, no cambia.
2. Cambio de fenotipo: Dd2-GCN5-R1 invade eritrocitos tratados con neuraminidasa, a los que la cepa silvestre no puede invadir.
3. Comparación con dCas9-VPR (activador eucariota VP64-P65-Rta): también activa, pero dCas9-GCN5 es marcadamente más potente en activación y en el cambio de invasión.

Notas: la especificidad queda respaldada por *ama1*, que no se altera pese a expresarse en el mismo estadio; el efecto es sobre el blanco y no un artefacto global. El fenotipo cierra el argumento: la sobreexpresión de *rh4* se traduce en una capacidad de invasión nueva, no solo en más ARN mensajero. La invasión de eritrocitos tratados con neuraminidasa corresponde a la vía independiente de ácido siálico (la neuraminidasa remueve el ácido siálico de la superficie), coherente con la función descrita de PfRH4. Cabe aclarar que el encabezado de la sección en el paper la denomina "sialic acid-dependent"; se trata de una inconsistencia del texto respecto de su propio abstract y del mecanismo, que aquí se expone en su versión correcta.

---

## Slide 9. Prueba de concepto II: represión de *eba-175* (Fig. 3)

Visual: Figura 3, paneles A a E.

Contenido:
1. Blanco: *eba-175*, uno de los genes de invasión más expresados en la cepa 3D7; su producto une glicoforina A y media la vía dependiente de ácido siálico.
2. El TSS se mapeó por 5'-RACE; EBA175sgRNA1 dirige dCas9-Sir2a a esa región. ChIP confirma ocupancia del dCas9 (anti-FLAG) e hipoacetilación de H3 (anti-acetil-H3) en el locus.
3. RT-qPCR: caída considerable de *eba-175* en 3D7-Sir2a-E1, sin cambios en *ama1* ni en el control 3D7-dCas9-GFP. Fenotipo: la represión impide la invasión de eritrocitos tratados con quimotripsina.

Notas: es el experimento espejo del anterior, con el efector opuesto. La secuencia unión, marca y transcripción se repite, ahora en sentido represivo: el dCas9-Sir2a se ubica en el TSS, remueve acetilación y baja la expresión. El fenotipo es coherente, puesto que la invasión de eritrocitos tratados con quimotripsina depende de EBA-175; al reprimirlo, esa vía se cierra. En conjunto, los slides 7 a 9 demuestran las dos direcciones de regulación con lectura molecular y funcional.

---

## Slide 10. Lección de diseño: la posición del sgRNA importa (Fig. S4)

Visual: Figura S4 del apéndice (EBA175sgRNA2, a -1578 bp respecto del ATG, equivalente a 1.234 bp corriente arriba del TSS).

Contenido:
1. Un segundo sgRNA (EBA175sgRNA2), ubicado a 1.234 bp corriente arriba del TSS, recluta el dCas9-Sir2a y hasta altera la acetilación en la región blanco.
2. Sin embargo, no logra reprimir *eba-175* con la eficiencia del sgRNA dirigido al TSS.
3. Regla operativa: cuanto más cerca del TSS se diseña el sitio guía, más efectiva es la regulación. El mismo patrón se observó para *rh4* con RH4sgRNA2 (Fig. S2).

Notas: este punto es el más transferible al diseño experimental propio, que es lo que la modalidad valora. La unión del dCas9 es condición necesaria pero no suficiente; el efector debe depositar o remover la marca en el lugar donde tiene consecuencia transcripcional, y ese lugar es el entorno inmediato del TSS. Es un criterio concreto para elegir el protoespaciador al aplicar la técnica.

---

## Slide 11. Alcance a genes esenciales: *PfSET1* (Fig. 4)

Visual: Figura 4, paneles A (RT-qPCR), B (distribución de fenotipos), C (mapa de calor) y D (citometría de flujo).

Contenido:
1. *PfSET1* es una histona metiltransferasa esencial para el estadio asexual, de función poco conocida y, por su esencialidad, inaccesible al knockout.
2. dCas9-Sir2a reprime *PfSET1* en 3D7-Sir2a-G1; el análisis de RNA-seq detecta 322 genes regulados a la baja, de los cuales el 50% de sus ortólogos son esenciales y un 19% adicional se asocia a crecimiento lento en *P. berghei*.
3. El 72% de esos genes esenciales se expresa en trofozoíto y esquizonte; la citometría de flujo muestra un retraso del crecimiento que arranca en el estadio de trofozoíto, ausente en los controles.

Notas: este es el argumento más fuerte a favor de la técnica, porque resuelve el problema planteado al inicio. Un gen esencial no puede estudiarse por knockout en un organismo haploide, pero sí puede reprimirse parcialmente de forma reversible para observar su fenotipo. El retraso del crecimiento, específico de la línea reprimida y coincidente con el patrón de expresión de los genes afectados, conecta la represión molecular con una consecuencia biológica medible.

---

## Slide 12. Especificidad y targetabilidad genómica (Fig. S5 y S8)

Visual: Figura S5 (scatter de transcriptomas, off-target) y Figura S8 (densidad de PAM en las regiones promotoras).

Contenido:
1. Off-target bajo: los transcriptomas por RNA-seq de las líneas editadas muestran pocos cambios fuera del blanco.
2. Efecto colateral acotado: *pebl*, un pseudogen que comparte un promotor bidireccional con *rh4*, se activa junto con este; el sistema afecta genes que comparten promotor, lo que a su vez habilita su uso sobre ARN no codificantes.
3. Cobertura: se identificaron 261.196 PAM NGG y 727.817 NGA entre -1.500 y +500 bp del codón de inicio, con más de 173 veces de cobertura sobre los 5.712 genes del parásito; prácticamente todo gen es blanco potencial.

Notas: la especificidad se sostiene con datos de transcriptoma global, no solo con el gen blanco. El caso de *pebl* no debilita el argumento; muestra el límite del sistema (los promotores bidireccionales se co-regulan) y a la vez amplía su uso hacia elementos no codificantes. La abundancia de PAM en las regiones promotoras indica que la restricción práctica no es encontrar un sitio, sino diseñarlo cerca del TSS, que es la lección del slide 10.

---

## Slide 13. Ventajas, límites y lugar entre las técnicas

Contenido:
1. Ventajas: reversibilidad, ausencia de ruptura de doble cadena, acceso a genes esenciales y a ARN no codificantes, y uso de dos efectores endógenos para activar y reprimir.
2. Límites: dependencia de la posición del sgRNA respecto del TSS, co-regulación de promotores bidireccionales, y expresión episomal con niveles variables o posible clivaje del dCas9.
3. Ubicación: comparte lógica con CRISPRi y CRISPRa (dCas9 más efector); se diferencia del knockout por Cas9 y de las ediciones de base o prime, que sí modifican la secuencia.

Notas: el balance es el esperado para una herramienta de reprogramación transcripcional. Frente a CRISPRi basado en dominios represores como KRAB, este trabajo demuestra que efectores de acetilación endógenos cumplen la misma función en un organismo donde no había edición epigenética reportada. La perspectiva de multiplexado con sistemas tipo Cpf1 queda planteada por los autores como línea futura, en particular para familias multigénicas.

---

## Slide 14. Conclusiones

Contenido:
1. Fusionar PfGCN5 o PfSir2a a un dCas9 permite activar o reprimir genes en *P. falciparum* de forma específica y sin editar la secuencia.
2. Se demostró el control de vías de invasión (*rh4* y *eba-175*) con lectura molecular y fenotípica, y el acceso a un gen esencial (*PfSET1*) por represión reversible.
3. El sistema amplía las herramientas de genética funcional y epigenética del parásito, con cobertura genómica prácticamente total.

Notas: cierre factual, sin recapitulación redundante. La contribución concreta es haber llevado la edición epigenética por dCas9 a un organismo refractario a la manipulación genética, con dos herramientas complementarias y validadas en tres genes de biología relevante.

Referencia: Xiao B, Yin S, Hu Y, Sun M, Wei J, Huang Z, Wen Y, Dai X, Chen H, Mu J, Cui L, Jiang L (2019). Epigenetic editing by CRISPR/dCas9 in *Plasmodium falciparum*. *PNAS* 116(1):255-260.

---

## Notas de cierre del guion

Figuras a insertar en el pptx: Fig. 1 (slide 5 y 6), Fig. 2 (slide 7 y 8), Fig. 3 (slide 9), Fig. S4 (slide 10), Fig. 4 (slide 11), Fig. S5 y S8 (slide 12). Todas se recortan del PDF original a resolución de impresión antes de armar las diapositivas.

Descartadas por redundancia respecto del texto principal: S1 y S3 (autenticaciones de acetilación ya resumidas en Fig. 2C y 3C), S6 (ya sintetizada en el punto de *pebl*), S7 (morfología por microscopía, redundante con la citometría de Fig. 4D) y S9 (dinámica de H3K9ac, de apoyo pero no central para la aplicación).
