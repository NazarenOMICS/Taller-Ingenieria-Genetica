---
type: esqueleto-obligatorio
status: current
date: 2026-07-25
source: "02_obligatorio/consigna_y_rubrica.md + rubrica_detallada.md + 00_teoria_general/cartilla_teorico.md + 03_informe/cartilla_practico.md (ejercicios) + Vault/Notes/dcas9-fto-granulosa/"
related:
  - "[[Notes/dcas9-fto-granulosa/MAESTRO_OBLIGATORIO]]"
  - "[[Notes/dcas9-fto-granulosa/INFORME_GENERAL]]"
  - "[[Notes/dcas9-fto-granulosa/CONCLUSIONES_CLAVE]]"
---

# Esqueleto del Obligatorio (activación de FTO vía dCas9-p300 en granulosa humana)

Plantilla de trabajo, no entregable. Cada sección indica qué contenido va, de qué archivo sale, qué figura o tabla la acompaña, qué decisión operativa hay que tomar antes de escribirla y qué criterio de la rúbrica satisface. Presupuesto total de alrededor de 10 carillas sin bibliografía ni anexos.

Herramienta de anotación acordada: Benchling. No hay acceso a SnapGene, de modo que los archivos que la consigna pide adjuntar se exportan desde Benchling en formato GenBank (.gb), que es el formato que SnapGene abre sin pérdida de anotaciones.

---

## 0. Método canónico del curso, extraído de la cartilla

Esto fija el vocabulario y las herramientas que la cátedra da por estándar. Conviene usarlas explícitamente, porque el evaluador reconoce su propio marco.

| Fuente | Qué establece | Uso en este trabajo |
| :--- | :--- | :--- |
| Ejercicio 1 (FOXO4) | Obtener región genómica y transcriptos posibles de un gen, y elegir el locus para diseñar guías | Ensembl para el locus de *FTO*, sus transcriptos y la definición del TSS |
| Ejercicio 5 (Reg1) | CRISPOR para diseño de guías, determinación de off-targets, eficiencia de corte y secuencia seed | CRISPOR para el panel de guías, con la salvedad del cambio de criterio que se explica abajo |
| Ejercicio 16 | Identificadores Ensembl como referencia canónica de gen | Citar el identificador Ensembl de *FTO* y del transcripto elegido |
| Cartilla teórica §3 | SpCas9, PAM NGG, corte 3 pb corriente arriba del PAM, dominios RuvC y HNH | Justificar dCas9 como la misma plataforma de reconocimiento sin actividad de corte |
| Cartilla teórica §4 | Golden Gate con enzimas Tipo IIS, pX459 digerido con BbsI, extremos cohesivos de 4 nt | Clonado de los oligos de guía en el vector de sgRNA |
| Protocolo 1 | Formato de oligos con extremos CACCG y AAAC, fosforilación con T4 PNK, hibridación 37 °C y rampa desde 95 °C, ligación | Diseño de los oligos duplex de cada guía, replicable tal cual |
| Cartilla teórica §5 | Genotipado por heterodúplex, T7E1, Surveyor, HRMA, HMA, secuenciación con TIDE e ICE | No aplica al proyecto, y decirlo es un punto a favor: sin corte no hay indel que genotipar |

### 0.1 Qué cambia al pasar de diseño para KO a diseño para CRISPRa

Este contraste es el argumento de mayor rendimiento del trabajo, porque demuestra que el método del curso se comprendió y se adaptó en lugar de copiarse. Debe aparecer explícito en el Diseño Experimental.

1. El blanco deja de ser exónico y pasa a ser la ventana promotora en torno al TSS. En un KO se busca un exón temprano y constitutivo; acá se busca la región donde el depósito de H3K27ac tiene efecto transcripcional.
2. Los puntajes de eficiencia de corte (Doench y equivalentes) pierden su significado biológico, puesto que no hay corte. Lo que predice el efecto en CRISPRa es la distancia al TSS y la accesibilidad de la cromatina. Los puntajes se reportan igual, pero se declara que no son el criterio de selección.
3. El off-target cambia de naturaleza: pasa de rotura de doble cadena en un sitio no deseado a unión sin corte con posible deposición de acetilación en un promotor ajeno. La consecuencia se mide por transcriptoma y no por T7E1.
4. La secuencia seed sigue siendo el determinante de especificidad de la unión, de modo que el concepto del ejercicio 5 se conserva íntegro y conviene citarlo.
5. El multiplexado deja de servir para asegurar la inactivación (dos cortes) y pasa a servir para sumar efectores sobre la misma región regulatoria.
6. No hay genotipado de edición: la verificación de que el sistema actuó es ChIP y expresión, no heterodúplex ni secuenciación de amplicón.

---

## 1. Introducción (2,5 carillas, criterio 1 de la rúbrica, 5 puntos)

**Contenido requerido**

1. Envejecimiento ovárico como problema, con el giro desde la pérdida folicular hacia las alteraciones de las células somáticas de sostén. Por qué la granulosa es el blanco tratable frente al ovocito.
2. Eje FTO-m6A-FOS: estrés oxidativo baja FTO, sube m6A en el 3'UTR de *FOS*, se estabiliza el mensajero, sube FOS, se dispara senescencia. Presentado como cadena causal con evidencia de pérdida de función y rescate.
3. Presentación del gen a modificar: *FTO*, qué hace como desmetilasa de m6A, por qué su restauración es el punto de entrada.
4. Marco conceptual de la herramienta: cromatina, H3K27ac como marca de promotores y potenciadores activos, dCas9 como plataforma de reconocimiento sin corte, fusión con el core catalítico de p300, definición de CRISPRa.
5. Justificación de p300 frente a otros efectores, en clave afirmativa y con bibliografía verificada.
6. Delimitación de la novedad: qué existe y qué no, sin sobrevender.
7. Declaración explícita de que la edición no es un knockout sino edición de regulación génica, que es la categoría admitida por la consigna.

**De dónde sale**

| Punto | Fuente |
| :--- | :--- |
| 1 y 2 | `02_obligatorio/temas_candidatos/edicion_epigenomica_FTO_envejecimiento_ovarico.md` §1, ya redactado en la voz correcta |
| 3 | Mismo dossier, más `INFORME_GENERAL.md` §4.1 a §4.3 |
| 4 | Dossier §2 |
| 5 | `INFORME_GENERAL.md` §5.6, párrafos primero y segundo |
| 6 | Dossier §5, corregido con lo verificado sobre Kachanov y Liao |
| 7 | `MAESTRO_OBLIGATORIO.md` §2 |

**Figuras**: F5 (esquema del eje FTO-m6A-FOS).

**Decisiones operativas previas**

1. Si la Introducción abre por el problema clínico (envejecimiento ovárico) o por el mecanismo (m6A y FTO). Recomendado abrir por el problema, que es el movimiento de zoom que ya usás.
2. Cuánto espacio se le da a la explicación de m6A. Si el evaluador no es del área, hace falta un párrafo; si lo es, sobra.
3. Si se menciona la limitación del mecanismo promotor ya en la Introducción o se reserva para el cierre. Recomendado reservarla, para no debilitar la apertura.

---

## 2. Objetivo (0,25 carillas, criterio 1)

**Contenido requerido**

Un objetivo general y tres o cuatro específicos, formulados de manera que cada uno sea verificable y que se correspondan uno a uno con las capas de validación del diseño. La hipótesis encadenada del dossier §3 ya tiene esa forma y solo hay que convertirla en objetivos.

Formulación de referencia: diseñar una estrategia de activación epigenética dirigida del promotor endógeno de *FTO* mediante dCas9-p300 en células de la granulosa humana, que permita evaluar si la reposición de FTO revierte parcialmente el eje m6A-FOS y el fenotipo senescente.

**Decisiones operativas previas**

1. Si el objetivo se formula como "diseñar una estrategia" o como "evaluar el efecto". Dado que el trabajo es de diseño y no hay mesada, corresponde lo primero, y conviene decirlo sin ambigüedad para que la ausencia de resultados experimentales no se lea como una omisión.

---

## 3. Diseño Experimental (7 carillas, criterios 2 y 3 de la rúbrica, 11 puntos)

Esta es la sección que define la nota. Lo que sigue la subdivide en bloques; cada bloque lleva su conocimiento necesario, su decisión operativa y su figura.

*Presupuesto*: las diez subsecciones suman 7 carillas y el total del documento asciende a 10,75, que queda dentro del "alrededor de 10 carillas" que fija la consigna pero sin margen. Si hay que recortar, los dos bloques más comprimibles son 3.6 (modelo celular y entrega) y 3.9 (análisis de especificidad), que pueden bajar a un párrafo cada uno sin perder criterio de rúbrica. Los bloques 3.3, 3.4 y 3.5 no se recortan, puesto que son los que sostienen Metodología y Resultados.

### 3.1 Estrategia general y elección del efector (0,5 carillas)

**Contenido**: esquema global de la estrategia en un párrafo, seguido de la justificación del efector. Comparación con las alternativas descartadas (VP64, VPR, SunTag, dCas9-TET1) y por qué se eligió p300.

**Conocimiento necesario**: diferencia entre activador que recluta maquinaria transcripcional y escritor epigenético que deposita marca; reversibilidad de H3K27ac al retirar el efector; dependencia del contexto celular.

**Figura**: F6 (flujo general de la estrategia y de la validación).

**Decisión operativa**: si se presenta la comparación de efectores como tabla o como prosa. Recomendada tabla, porque suma al criterio de Resultados.

### 3.2 Etapa 0: caracterización del promotor de FTO en granulosa (0,75 carillas)

**Contenido**: ensayo previo que determina qué capa regulatoria explica la caída basal de *FTO* en granulosa envejecida, y cómo su resultado condiciona la construcción del efector. Secuenciación por bisulfito de la isla CpG promotora y ChIP-qPCR de H3K27ac sobre la ventana blanco, comparando granulosa joven contra envejecida o tratada con peróxido de hidrógeno.

**Conocimiento necesario**: conversión por bisulfito y lectura de metilación; principio de ChIP; por qué la ausencia de datos publicados sobre este promotor obliga a generarlos; árbol de decisión resultante.

**Árbol de decisión que debe quedar escrito**: si aparece acetilación reducida sin hipermetilación relevante, procede dCas9-p300 solo; si aparece hipermetilación densa, la accesibilidad de la cromatina puede limitar al efector y corresponde evaluar una estrategia combinada del tipo TET1 más p300.

**Figura**: puede integrarse a F6 como rama previa, o llevar figura propia si sobra espacio.

**Decisión operativa**: cuántos pares de muestras (joven contra envejecida) y de qué origen (KGN tratadas con peróxido, o granulosa primaria de punción folicular estratificada por edad).

### 3.3 Identificación del locus y definición de la ventana blanco (0,75 carillas)

**Contenido**: identificación de *FTO* en Ensembl, sus transcriptos, elección del transcripto de referencia y de su TSS, delimitación de la isla CpG y de la ventana de tesela. Este es el bloque que responde al ejercicio 1 de la cartilla trasladado al proyecto propio.

**Conocimiento necesario**: cromosoma y coordenadas de *FTO* en GRCh38; concepto de transcripto canónico y de MANE Select; por qué un gen con varios TSS obliga a elegir y a justificar la elección; qué es una isla CpG y por qué importa en un promotor; relación entre distancia al TSS y eficacia de CRISPRa.

**Figura F1**: vista del locus de *FTO* con sus transcriptos y el TSS marcado, obtenida de Ensembl y anotada.
**Figura F2**: ampliación de la ventana promotora en Benchling, con la isla CpG, la posición del TSS, la ventana de tesela delimitada y las guías ubicadas con su PAM.

**Decisiones operativas, las más importantes de todo el trabajo.** Las cuatro quedaron resueltas y documentadas en `DECISIONES_DISENO.md`; este apartado del entregable debe redactarse a partir de ese archivo.

1. Transcripto de referencia y TSS: resuelto en D1. ENST00000471389 (FTO-206), MANE Select más Ensembl Canonical, TSS en chr16:53.704.156, ensamblado GRCh38 declarado explícitamente.
2. Arquitectura del locus: resuelto en D2. *RPGRIP1L* en orientación divergente con su TSS a 297 pb, y un único elemento de tipo promotor anotado que contiene ambos inicios. Este es el hallazgo que reorienta todo el diseño y debe contarse como tal.
3. Región blanco: resuelto en D4.1 mediante comparación explícita de cuatro alternativas con criterios declarados. La comparación completa es material entregable y va en esta sección.
4. Panel de guías: resuelto en D4.2. Tres guías, dos en el enhancer propio de *FTO* (aproximadamente +60 y +450) y una comparadora en el promotor compartido (aproximadamente −200), con el multiplexado reservado como contingencia. La justificación de por qué tres y no más ni menos es material entregable.

### 3.4 Diseño y selección de guías (1 carilla)

**Contenido**: procedimiento de diseño, criterios de inclusión y exclusión, panel final de guías y guías descartadas con su motivo. La consigna pide explícitamente hablar de resultados descartados en la oral, de modo que este bloque alimenta las dos entregas.

**Conocimiento necesario**: PAM NGG de SpCas9 y por qué se conserva en dCas9; secuencia seed y su papel en la especificidad, tal como lo plantea el ejercicio 5; lectura de la salida de CRISPOR (puntajes de especificidad, off-targets por número de mismatches, si caen en exón o no); por qué los puntajes de eficiencia de corte no son el criterio acá; ventaja del multiplexado en CRISPRa.

**Tabla T1**: una fila por guía con secuencia de 20 nt, hebra, posición del extremo 5' respecto del TSS, PAM, puntaje de especificidad, número de off-targets con 0 a 4 mismatches, cuántos de esos conservan la seed, cuántos son exónicos, y decisión (incluida o descartada con motivo).

**Decisiones operativas**

1. Cuántas guías componen el panel final. Recomendado entre cuatro y seis para poder multiplexar y tener suplentes.
2. Si se admiten guías en ambas hebras.
3. Umbral de exclusión por off-target: por ejemplo, descartar toda guía con off-target exónico en el mismo cromosoma con tres mismatches o menos, que es el criterio que el ejercicio 5 induce.
4. Qué herramienta se usa y en qué versión y genoma, para poder nombrarla en la oral. CRISPOR es la del curso; si se usa además una herramienta con modo CRISPRa específico, hay que declararlo y explicar por qué.
5. Si las guías se ensayan individualmente antes de multiplexar, o directamente en combinación.

### 3.5 Construcción del efector y clonado (1 carilla)

**Contenido**: composición del constructo, origen de cada elemento, estrategia de clonado de los oligos de guía y verificación del clon.

**Conocimiento necesario**: arquitectura de una fusión dCas9-efector (promotor, señales de localización nuclear, mutaciones D10A y H840A que inactivan RuvC y HNH, linker, core catalítico de p300, marcador de selección); sistema de dos plásmidos frente a all-in-one y el problema de tamaño de la carga; Golden Gate con enzima Tipo IIS según la cartilla §4; formato de oligos con extremos CACCG y AAAC del protocolo 1; por qué el vector del curso (pX459) no sirve tal cual, puesto que lleva SpCas9 activa.

**Figura F3**: mapa del constructo dCas9-p300 anotado en Benchling, con promotor, etiqueta, señales de localización nuclear, dCas9 con sus mutaciones marcadas, linker, dominio p300 y marcador.
**Figura F4**: mapa del vector de sgRNA con el promotor U6, los sitios de la enzima Tipo IIS, el andamiaje del sgRNA y el sitio exacto donde entra el duplex de oligos.

**Decisiones operativas**

1. Vector de partida del efector. Lo coherente con la bibliografía es el plásmido de dCas9-p300 Core de Hilton et al. (2015), que es el mismo que utilizó Liao et al. (2026) en granulosa porcina. Hay que decidir si se parte de él o se rediseña.
2. Sistema de uno o dos plásmidos. Con multiplexado de guías, dos plásmidos simplifica; hay que declarar la consecuencia sobre la eficiencia de cotransfección.
3. **Etiqueta en la dCas9**. Decisión propia, y conviene tomarla de forma afirmativa: incorporar una etiqueta (3xFLAG o HA) en el extremo amino de la dCas9. Sirve para tres cosas: verificar expresión del efector por western, hacer ChIP anti-etiqueta que demuestra ocupancia física del complejo en la ventana blanco, y distinguir el efector exógeno de proteínas endógenas. Cabe mencionar que el propio pX459 del curso lleva 3xFLAG en el extremo amino de la Cas9, de modo que la decisión es consistente con el material de cátedra.
4. Control catalíticamente inactivo: mutación puntual del core de p300 (D1398Y). Hay que decidir si se construye o se cita como disponible.
5. Enzima Tipo IIS y sitio de clonado del vector de sgRNA, con los extremos cohesivos de 4 nt correspondientes.
6. Método de verificación del clon: secuenciación Sanger con cebador sobre el promotor U6, y qué se espera ver en el cromatograma.

### 3.6 Modelo celular, condición de envejecimiento y entrega (0,5 carillas)

**Contenido**: línea celular, cómo se induce el fenotipo envejecido, y sistema de entrega con su justificación.

**Conocimiento necesario**: KGN y COV434 como líneas de granulosa; modelo de estrés oxidativo con peróxido de hidrógeno y por qué reproduce el fenotipo; ventajas y límites de la granulosa primaria de punción folicular; opciones de entrega para una carga de aproximadamente 5 a 6 kb y por qué el tamaño es un problema.

**Decisiones operativas**

1. Línea principal y línea de confirmación.
2. Concentración y tiempo de exposición al peróxido de hidrógeno, tomados del modelo de referencia y citados.
3. Sistema de entrega. La transfección transitoria es coherente con el argumento de reversibilidad y control temporal; el lentivirus da eficiencia a costa de integración estable, que contradice el argumento de transitoriedad. Hay que elegir y defender.
4. Si se incorpora un sistema de control de dosis del efector, que es lo que permite argumentar activación fisiológica y no suprafisiológica.

### 3.7 Panel de controles (0,5 carillas)

**Contenido**: los controles que permiten atribuir el efecto al mecanismo epigenético dirigido, cada uno con qué artefacto descarta.

**Tabla T3**: una fila por control con nombre, composición, qué descarta y qué resultado se espera.

Controles mínimos: guía no dirigida o scrambled, que descarta efecto de los componentes del sistema; efector catalíticamente muerto (p300 D1398Y), que separa la acetilación del simple anclaje del complejo; dCas9 sin dominio efector, que establece la línea de base y descarta efecto de la unión per se; célula sin tratar y célula envejecida sin transfectar, que fijan los extremos del rango fenotípico.

**Decisión operativa**: si se agrega un control de guía dirigida a un locus irrelevante pero real, además del scrambled, para distinguir unión inespecífica de unión a un sitio no relacionado.

### 3.8 Validación en tres capas (1 carilla)

**Contenido**: cada capa con su técnica, su lectura y su control. La estructura de tres capas espeja la cadena de la hipótesis, lo cual permite localizar dónde se corta el mecanismo si el resultado global no aparece.

**Capa 1, el sistema actuó donde debía.** ChIP-qPCR anti-etiqueta sobre la ventana blanco, para demostrar ocupancia del complejo, y ChIP-qPCR de H3K27ac sobre la misma ventana, para demostrar deposición de la marca. Es el diseño que usan tanto Hilton et al. (2015) como Liao et al. (2026), de modo que hay precedente metodológico directo que citar.

**Capa 2, la transcripción respondió.** RT-qPCR de *FTO* y western de FTO; m6A global; m6A sitio específica sobre el 3'UTR de *FOS* por MeRIP-qPCR o SELECT; estabilidad del mensajero de *FOS* por ensayo de pulso con actinomicina D.

**Capa 3, el fenotipo se movió.** SA-beta-galactosidasa, p16, p21 y gamma-H2AX, con la lectura esperable de desacople parcial y no de normalización completa.

**Conocimiento necesario**: principio de ChIP y por qué hacen falta amplicones control; normalización de ChIP-qPCR por input y por región de referencia; diferencia entre m6A global y sitio específica; por qué actinomicina D mide vida media; por qué la reversión parcial no es un resultado negativo.

**Figura F7**: posición de los amplicones de ChIP-qPCR sobre el promotor de *FTO*, anotada en Benchling, mostrando el amplicón sobre la ventana blanco, un amplicón control negativo en región distal sin marca y un amplicón control positivo sobre un promotor activo constitutivo.

**Tabla T2, primers**: hay que diseñar y tabular al menos cinco conjuntos, indicando en cada caso dónde hibridan.

| Conjunto | Dónde hibrida | Para qué |
| :--- | :--- | :--- |
| ChIP-qPCR blanco | Dentro de la ventana promotora de *FTO*, amplicón de 100 a 150 pb centrado en el sitio de las guías | Cuantificar enriquecimiento de etiqueta y de H3K27ac en el sitio dirigido |
| ChIP-qPCR control negativo | Región distal sin marcas activas, a decenas de kilobases del locus | Establecer el fondo del ensayo |
| ChIP-qPCR control positivo | Promotor de un gen constitutivamente activo | Confirmar que la inmunoprecipitación funcionó |
| RT-qPCR | Unión exón-exón de *FTO*, y de *FOS*, más genes normalizadores | Medir respuesta transcripcional evitando amplificar ADN genómico |
| MeRIP-qPCR | Región del 3'UTR de *FOS* que contiene el sitio DRACH de interés | Cuantificar m6A sitio específica |
| Verificación de clon | Sobre el promotor U6, corriente arriba del sitio de inserción | Secuenciar el inserto de guía |

**Decisiones operativas**

1. Qué anticuerpo se usa para el ChIP de la etiqueta y cuál para H3K27ac.
2. Qué gen se toma como amplicón control positivo y qué región como control negativo, con sus coordenadas.
3. Qué genes normalizadores se usan en RT-qPCR y por qué (los clásicos pueden variar con senescencia, lo cual es un detalle que suma).
4. Si la m6A sitio específica se mide por MeRIP-qPCR o por SELECT, y con qué fundamento se elige.
5. Qué sitio DRACH del 3'UTR de *FOS* se interroga.

### 3.9 Análisis de especificidad (0,5 carillas)

**Contenido**: cómo se evalúa que el efecto es dirigido y no global. Verificación de los off-targets predichos por CRISPOR en los sitios de mayor riesgo, y perfilado transcriptómico global para detectar activación inespecífica y efectos pleiotrópicos derivados de que FTO es un borrador global de m6A.

**Conocimiento necesario**: por qué el off-target de un efector sin corte no se detecta por T7E1; qué aporta el transcriptoma frente a la verificación sitio a sitio; cómo se define un umbral de activación fisiológica comparando contra granulosa joven.

**Decisión operativa**: si el criterio de éxito se define como alcanzar el nivel de FTO de granulosa joven, y cómo se mide ese nivel de referencia.

### 3.10 Resultados esperados y criterios de decisión (0,5 carillas)

**Contenido**: tabla que anticipa, para cada medición, el resultado esperado si la hipótesis se sostiene, el resultado que la refuta y qué se concluiría en cada caso. Es la forma de cubrir el criterio de Resultados en un trabajo de diseño sin presentar datos inventados.

**Tabla T4**: una fila por medición, con columnas de resultado esperado, resultado alternativo e interpretación.

**Decisión operativa**: qué magnitud de aumento de FTO se define como éxito, expresada como veces sobre el basal envejecido o como fracción del nivel joven.

---

## 4. Consideraciones, alcance y limitaciones (1 carilla, criterio 4 de la rúbrica, 5 puntos)

**Problema de encaje que hay que resolver**: la estructura que pide la consigna (Introducción, Objetivo, Diseño Experimental, Anexos, Bibliografía) no incluye Discusión, pero la rúbrica le asigna 5 puntos. La salida es incorporar este bloque como cierre del Diseño Experimental o como sección breve previa a los Anexos, sin inventar un encabezado que contradiga la estructura pedida.

**Contenido requerido**

1. La propuesta es reversión parcial de una alteración epigenética, no rejuvenecimiento ovárico. No recupera folículos perdidos ni corrige alteraciones del ovocito.
2. FTO desmetila miles de mensajeros, de modo que la activación excesiva produce efectos pleiotrópicos. Argumento a favor del abordaje sobre el promotor endógeno frente a la sobreexpresión por transgén.
3. La causa promotor-específica de la caída basal de *FTO* en granulosa no está resuelta en la literatura, y por eso el diseño incorpora la etapa 0. Declararlo como delimitación del alcance y no como disculpa.
4. No hay antecedente de dCas9-p300 sobre *FTO* en granulosa ni en tejido reproductivo. Sí lo hay sobre *FTO* en hepatocitos y sobre otro gen en granulosa porcina.
5. Dependencia del contexto celular de la ventaja de p300.

**De dónde sale**: `MAESTRO_OBLIGATORIO.md` §6, `INFORME_GENERAL.md` §5.5, §5.6 y §7, dossier §7.

---

## 5. Anexos (sin límite de carillas, criterio 7 de la rúbrica)

La consigna exige secuencias completas con las características relevantes marcadas y los archivos del software utilizado.

| Anexo | Contenido | Producción |
| :--- | :--- | :--- |
| A1 | Secuencia de la ventana promotora de *FTO* con TSS, isla CpG, sitios de las guías y PAM marcados | Benchling, exportado a GenBank |
| A2 | Tabla completa de guías con secuencia, PAM, coordenadas, hebra, puntajes y off-targets | Salida de CRISPOR curada |
| A3 | Oligos duplex de cada guía con los extremos CACCG y AAAC, en el formato del protocolo 1 | Diseño propio |
| A4 | Mapa y secuencia anotada del constructo dCas9-p300, con etiqueta, señales de localización nuclear, mutaciones de dCas9, linker y dominio p300 | Benchling |
| A5 | Mapa y secuencia anotada del vector de sgRNA con el sitio de clonado | Benchling |
| A6 | Tabla de primers con secuencia, temperatura de fusión, tamaño de amplicón y coordenadas de hibridación | Diseño propio |
| A7 | Archivos exportados de Benchling en formato GenBank | Exportación |

**Decisión operativa**: si los mapas se entregan también como imagen dentro del documento principal, dado que la consigna pide que la información gráfica esté en el cuerpo y las secuencias en anexo. Recomendado duplicar: figura en el cuerpo, secuencia anotada en anexo.

---

## 6. Bibliografía (criterio 5 de la rúbrica, 3 puntos)

**Contenido**: referencias en formato autor-año consistente, sin mezclar con sistema numérico, tomadas de la bibliografía consolidada de `INFORME_GENERAL.md` §9, que ya tiene DOI verificados.

**Decisión operativa**: cuántas referencias entran. Un trabajo de diez carillas con esta densidad sostiene entre veinticinco y cuarenta; el corpus tiene muchas más, de modo que hay que seleccionar y no volcar.

**Regla obligatoria**: ninguna afirmación se traslada sin contrastarla contra su pasaje literal, por el desajuste sistemático entre cita y fuente documentado en `MAESTRO_OBLIGATORIO.md` §7.

---

## 7. Inventario consolidado de figuras y tablas

| Id | Tipo | Contenido | Herramienta | Sección | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F1 | Figura | Locus de *FTO*, transcriptos y TSS | Ensembl, anotado | 3.3 | Pendiente |
| F2 | Figura | Ventana promotora con isla CpG, guías y PAM | Benchling | 3.3 | Pendiente |
| F3 | Figura | Mapa anotado del constructo dCas9-p300 | Benchling | 3.5 | Pendiente |
| F4 | Figura | Mapa del vector de sgRNA y sitio de clonado | Benchling | 3.5 | Pendiente |
| F5 | Figura | Esquema del eje FTO-m6A-FOS | Diagrama propio | 1 | Pendiente |
| F6 | Figura | Flujo de la estrategia y de la validación, con la etapa 0 | Diagrama propio | 3.1 | Pendiente |
| F7 | Figura | Posición de amplicones de ChIP-qPCR sobre el promotor | Benchling | 3.8 | Pendiente |
| T1 | Tabla | Panel de guías, incluidas y descartadas | Curada de CRISPOR | 3.4 | Pendiente |
| T2 | Tabla | Primers y dónde hibridan | Diseño propio | 3.8 | Pendiente |
| T3 | Tabla | Panel de controles | Diseño propio | 3.7 | Pendiente |
| T4 | Tabla | Resultados esperados e interpretación | Diseño propio | 3.10 | Pendiente |
| T5 | Tabla | Comparación de efectores epigenéticos | `INFORME_GENERAL.md` §3.6 y §5.6 | 3.1 | Derivable de material existente |

---

## 8. Cobertura de la rúbrica

| Criterio | Puntos | Sección que lo cubre | Riesgo |
| :--- | :--- | :--- | :--- |
| Introducción y Objetivos | 5 | 1 y 2 | Bajo, material ya escrito |
| Metodología | 5 | 3.2 a 3.9 | Medio, depende de tomar las decisiones operativas |
| Resultados | 6 | F1 a F7, T1 a T5, y 3.10 | Alto, nada producido todavía |
| Discusión y Conclusiones | 5 | 4 | Bajo, material sobrante |
| Referencias | 3 | 6 | Bajo, requiere selección y verificación |
| Claridad y Organización | 4 | Todo, según `Rules_Of_Writing.md` | Medio, hay que convertir listas en prosa |
| Cumplimiento de requisitos | 2 | 5 y formato | Bajo, verificable con checklist |

---

## 9. Correspondencia con la presentación oral del 30/07

La oral pregunta por qué se eligió la estrategia, qué programas se usaron, cómo se determinaron las eficiencias y qué resultados se descartaron. El mapeo es directo: la primera pregunta se responde con 3.1 y con la justificación de p300; la segunda con 3.3 y 3.4 (Ensembl, CRISPOR, Benchling); la tercera con T1 y con la aclaración de por qué los puntajes de eficiencia de corte no aplican; la cuarta con las guías descartadas de T1 y con los efectores descartados de T5.

Ergo, los bloques 3.3, 3.4 y 3.5 son el camino crítico: sin ellos la oral queda sin respuesta para tres de las cuatro preguntas.
