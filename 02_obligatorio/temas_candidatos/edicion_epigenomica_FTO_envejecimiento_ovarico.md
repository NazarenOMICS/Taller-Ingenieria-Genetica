# Tema candidato (Obligatorio) - Edición epigenómica dirigida del promotor de FTO para revertir parcialmente el envejecimiento ovárico

## Índice operativo

Estado: **candidato** a proyecto del Obligatorio (modalidad 2: escrito 30 pts + oral 15 pts). No es un entregable final; es un dossier de evaluación y punto de partida para el diseño.

Qué contiene: abstract compartible al grupo, análisis técnico del concepto, encaje con la consigna del Obligatorio (`../consigna_y_rubrica.md`, `../rubrica_detallada.md`), estado del arte y delimitación de novedad, alcance y limitaciones, batería de preguntas para búsqueda bibliográfica y referencias con DOI.

Concepto en una línea: activación epigenética dirigida (CRISPRa) mediante dCas9 fusionada al dominio catalítico de la acetiltransferasa p300, dirigida al promotor de FTO en células de la granulosa envejecidas, con el fin de reprogramar el eje epitranscriptómico FTO–m6A–FOS y atenuar la senescencia.

Datos clave: la edición NO es un knockout (cumple la restricción del Obligatorio); es edición de regulación génica sobre el locus endógeno; complejidad media-alta sostenida en el diseño de guías y en el eje de validación epitranscriptómico; genera material anexable (mapas, tabla de guías, primers, esquemas). El proyecto es de diseño, sin resultados experimentales propios: la hipótesis es novedosa y no comprobada, pero cada eslabón está respaldado por literatura.

Trazabilidad: propuesta original de Naza; fundamentos en Hilton et al. (2015), Jiang et al. (2021) y Jin et al. (2025); antecedentes cercanos identificados en PubMed (Kachanov et al., 2025; Liao et al., 2026; Gao et al., 2025). Las cifras y atribuciones provienen de esas fuentes; no se han inventado datos.

---

## Abstract (para compartir al grupo)

El envejecimiento ovárico no se explica únicamente por la pérdida progresiva de folículos, sino también por alteraciones moleculares en las células somáticas que sostienen al ovocito. Las células de la granulosa presentan durante el envejecimiento humano cambios coordinados en expresión génica, accesibilidad de la cromatina, senescencia y comunicación con el ovocito (Jin et al., 2025), lo que las vuelve un blanco experimental más accesible que el propio ovocito. En ese contexto, Jiang et al. (2021) describieron un eje epitranscriptómico causal: el estrés oxidativo reduce la desmetilasa de m6A denominada FTO, con lo que aumenta la modificación N6-metiladenosina (m6A) en el 3′UTR del ARN mensajero de FOS, se estabiliza dicho mensajero, sube la proteína FOS y se favorece la senescencia. Este trabajo propone restaurar la expresión endógena de FTO mediante un editor epigenómico formado por dCas9 (Cas9 sin actividad de corte) fusionada al dominio catalítico de p300, dirigido con ARN guía al promotor de FTO a efectos de depositar acetilación de histonas (H3K27ac) y reactivar la transcripción sin modificar la secuencia del gen. La herramienta dCas9-p300 fue validada como activador de genes endógenos desde promotores y potenciadores por Hilton et al. (2015); la novedad no reside en la herramienta sino en su aplicación al locus de FTO para revertir parcialmente el eje FTO–m6A–FOS vinculado al envejecimiento de la granulosa. La hipótesis sostiene que la acetilación dirigida del promotor de FTO aumentará la expresión endógena de la desmetilasa, reducirá la m6A sobre el mensajero de FOS, disminuirá su estabilidad y atenuará el fenotipo senescente. Se trata de un proyecto de diseño experimental: la propuesta es novedosa y no comprobada, pero cada eslabón del razonamiento está anclado en evidencia previa.

---

## 1. Fundamento biológico

El ovario concentra el reloj reproductivo del organismo, y su declive funcional precede al de otros sistemas. La lectura clásica atribuye ese declive al agotamiento de la reserva folicular, pero el análisis multi-ómico de núcleo único en ovario humano muestra que las células somáticas de sostén acumulan alteraciones propias durante el envejecimiento, con reprogramación coordinada de expresión y de accesibilidad de la cromatina, aumento de senescencia y deterioro de la comunicación con el ovocito (Jin et al., 2025). Puesto que la calidad del ovocito depende del microambiente que la granulosa provee, intervenir sobre estas células somáticas ofrece un punto de entrada experimental más tratable que el ovocito, que es escaso, no proliferativo y difícil de manipular sin comprometer su viabilidad.

Sobre ese trasfondo, Jiang et al. (2021) definieron un mecanismo epitranscriptómico concreto. En muestras de ovario humano envejecido observaron una reducción de la desmetilasa FTO acompañada de un aumento global de m6A, la modificación interna más frecuente del ARN mensajero. La reducción experimental de FTO en las líneas de granulosa KGN y COV434 incrementó la senescencia, el daño al ADN y la acumulación de m6A, reproduciendo el fenotipo asociado a la edad. El blanco funcional identificado fue el mensajero de FOS: al descender FTO, aumenta la m6A en su 3′UTR, lo que reduce su degradación y eleva su expresión; a su vez, disminuir FOS alivió parcialmente el fenotipo senescente inducido por la pérdida de FTO. De este modo queda establecido un eje causal en el que el estrés oxidativo reduce FTO, estabiliza FOS y empuja a la granulosa hacia la senescencia. Es este eje, y no una diana genérica, el que la propuesta busca revertir en su punto de origen.

## 2. Marco conceptual de la herramienta

La regulación de un gen no exige modificar su secuencia. El ADN se enrolla sobre histonas, y el grado de compactación de esa cromatina determina si la maquinaria transcripcional accede al gen o no. La acetilación de la lisina 27 de la histona H3 (H3K27ac) es una marca asociada a promotores y potenciadores activos: relaja localmente la cromatina y correlaciona con transcripción. Depositar o retirar esa marca en un sitio elegido permite, en principio, subir o bajar el volumen de un gen sin tocar su código, que es la definición operativa de la edición epigenómica.

La plataforma CRISPR-Cas9 aporta la especificidad de dirección. En su versión catalíticamente inactiva (dCas9), la proteína conserva la capacidad de ser guiada por un ARN a una secuencia genómica precisa, pero pierde la actividad de nucleasa: reconoce el ADN sin cortarlo. Fusionando a dCas9 un dominio efector se convierte ese reconocimiento en una acción bioquímica localizada. Hilton et al. (2015) demostraron que la fusión de dCas9 con el dominio catalítico de la acetiltransferasa p300 (dCas9-p300) deposita H3K27ac en la región reconocida y activa la transcripción de genes endógenos tanto desde promotores como desde potenciadores, incluso a distancia. La estrategia se conoce como activación génica mediada por CRISPR, o CRISPRa. Su ventaja frente a la sobreexpresión por transgén es doble: actúa sobre el locus original en su contexto cromatínico, y su efecto es en principio reversible y dosificable, puesto que se está moviendo un interruptor regulatorio y no introduciendo una copia constitutiva del gen.

## 3. Modificación propuesta e hipótesis

La propuesta consiste en dirigir dCas9-p300 al promotor de FTO mediante un conjunto de ARN guía próximos al sitio de inicio de la transcripción, a efectos de elevar localmente H3K27ac y restaurar la expresión endógena de la desmetilasa en células de la granulosa envejecidas. La innovación no es la herramienta, ya caracterizada, sino su aplicación a este locus con la finalidad específica de revertir el eje FTO–m6A–FOS.

La hipótesis se formula de manera encadenada y falsable: la acetilación dirigida del promotor de FTO mediante dCas9-p300 aumentará la expresión endógena de FTO; ese aumento reducirá la m6A presente en el 3′UTR del mensajero de FOS; la menor densidad de m6A disminuirá la estabilidad de dicho mensajero y, por lo tanto, la abundancia de FOS; y esa caída atenuará el fenotipo de senescencia celular. Cada paso de la cadena admite una medición independiente, lo que permite ubicar dónde se corta el mecanismo si el resultado global no se produce.

## 4. Lineamientos de diseño experimental

El diseño se ancla en el modelo ya empleado para vincular ROS, descenso de FTO y senescencia. Una primera etapa trabajaría sobre células KGN sometidas a estrés oxidativo con peróxido de hidrógeno, transfectadas con dCas9-p300 y varios ARN guía dirigidos a regiones próximas al sitio de inicio de la transcripción de FTO. El esquema de controles es el que sostiene la validez causal: un grupo sin tratamiento, un grupo envejecido con guía no dirigida, un grupo envejecido tratado con dCas9-p300 sobre FTO y un control con una variante de p300 catalíticamente inactiva, que separa el efecto epigenético dirigido de artefactos de unión o de expresión del constructo. Una validación posterior podría trasladarse a células primarias de la granulosa obtenidas durante procedimientos de reproducción asistida, que aproximan mejor la biología humana relevante.

La lectura se organiza en tres capas coherentes con la cadena de la hipótesis. La deposición de la marca se comprobaría por ChIP-qPCR o CUT&Tag para H3K27ac en el promotor de FTO. La respuesta transcripcional y epitranscriptómica se cuantificaría midiendo FTO, la m6A global, la m6A específica del mensajero de FOS por MeRIP-qPCR y la estabilidad de FOS tras bloquear la transcripción con actinomicina D. El fenotipo se evaluaría con marcadores de senescencia y daño al ADN de uso estándar, entre ellos SA-β-galactosidasa, γH2AX, p21 y p16. Cabe aclarar que, por tratarse de un proyecto de diseño, estas lecturas se presentan como el plan de verificación de la hipótesis y como los entregables de diseño (mapas, tablas de guías y primers, esquemas del eje y del flujo de validación), no como resultados experimentales obtenidos.

## 5. Estado del arte y delimitación de la novedad

La revisión bibliográfica preliminar (búsqueda superficial en PubMed) confirma que la aplicación específica no aparece publicada, a la vez que cada componente cuenta con precedente cercano, combinación que sitúa a la propuesta como novedosa pero bien fundada. La herramienta dCas9-p300 fue establecida como activador epigenético de genes endógenos por Hilton et al. (2015). El uso de dCas9-p300 para activar específicamente FTO ya fue reportado, si bien en un contexto distinto (restricción del ciclo del virus de hepatitis B en hepatocitos), lo que indica que la combinación editor-locus es técnicamente viable (Kachanov et al., 2025). La edición de H3K27ac mediante dCas9-p300 sobre un promotor en células de la granulosa también fue demostrada, aunque sobre otro gen, otra especie y con finalidad de estudio de la autofagia folicular (Liao et al., 2026), lo que respalda que la plataforma opera en el tipo celular elegido. Por último, la lógica de aumentar FTO por acetilación mediada por p300 en el promotor para reducir la m6A de un blanco y atenuar la senescencia inducida por estrés oxidativo fue observada en otro tejido y con otra herramienta (exosomas de células madre mesenquimales en núcleo pulposo), con un blanco distinto de FTO (Nrf2 en lugar de FOS) (Gao et al., 2025). La contribución del proyecto reside, por lo tanto, en integrar esos elementos en un blanco y un contexto que no han sido abordados: dirigir p300 al promotor de FTO en granulosa envejecida para revertir el eje FTO–m6A–FOS ovárico.

## 6. Encaje con la consigna del Obligatorio

La propuesta satisface las restricciones duras de la consigna. No constituye un knockout, requisito explícito del Obligatorio que lo diferencia del práctico del curso (KO de CASP8AP2 en HEK-293), y se ubica de lleno en la categoría admitida de edición de regulación génica. La base tecnológica es CRISPR, puesto que dCas9 conserva la plataforma de reconocimiento guiada por ARN aunque no corte. La complejidad media-alta que la consigna valora se sostiene en el diseño de guías teseladas sobre el promotor con evaluación de eficiencias, en el esquema de controles y en la capa de validación epitranscriptómica, más que en la herramienta en sí. El material anexable surge de forma natural: mapa del constructo, tabla de guías con su sitio de unión y predicción de eficiencia y off-targets, primers de qPCR y MeRIP, y esquemas de la estrategia, con las características relevantes marcadas. En cuanto a la rúbrica, cabe considerar que sus criterios de metodología, resultados y discusión están redactados en clave de informe experimental; en un proyecto de diseño se cubren, respectivamente, con el diseño experimental detallado, con los productos del diseño presentados como figuras y tablas (mapas, guías, análisis in silico) y con la justificación y las limitaciones ancladas en literatura, sin necesidad de presentar datos de mesada ni resultados predichos como si fueran comprobados.

## 7. Alcance y limitaciones

La propuesta constituye una reversión parcial de una alteración epigenética asociada al envejecimiento ovárico, no un rejuvenecimiento completo del ovario. La intervención podría mejorar el estado funcional de la granulosa, pero no recuperaría folículos ya perdidos ni corregiría las alteraciones cromosómicas o mitocondriales del ovocito. Asimismo, FTO desmetila numerosos mensajeros, de modo que su activación excesiva podría producir cambios no deseados; por ello la expresión del editor debería ser transitoria y la magnitud de la activación tendría que compararse con los niveles presentes en células jóvenes, evitando un régimen suprafisiológico. De todos modos, esta limitación es también un argumento a favor del abordaje epigenético frente a la sobreexpresión por transgén: al operar sobre el promotor endógeno, la activación queda acotada por la arquitectura regulatoria propia del locus. Independientemente de ello, sería necesario analizar sitios de unión no previstos de los ARN guía y cambios transcriptómicos globales, a efectos de distinguir el efecto dirigido de perturbaciones inespecíficas.

## 8. Preguntas para búsqueda bibliográfica

Las siguientes preguntas orientan la búsqueda de fuentes para sostener cada eslabón del diseño. Están ordenadas de la herramienta al fenotipo.

1. ¿Qué eficiencia de activación transcripcional alcanza dCas9-p300 sobre promotores endógenos humanos, y de qué depende (posición de la guía respecto al sitio de inicio de la transcripción, número y combinación de guías, arquitectura del promotor)?
2. ¿Cuál es la magnitud y la persistencia de la marca H3K27ac depositada por dCas9-p300, y cuánto dura la activación una vez retirado el editor (reversibilidad y control temporal de la intervención)?
3. ¿Cuál es el perfil de especificidad y de efectos fuera de blanco de dCas9-p300 en células humanas, tanto a nivel de unión de las guías como de cambios transcriptómicos globales?
4. ¿Qué evidencia respalda el eje FTO–m6A–FOS en células de la granulosa humanas, y en qué modelos y con qué controles fue validado más allá de Jiang et al. (2021)?
5. ¿Cómo varían la expresión de FTO y el nivel global de m6A en el ovario y en la granulosa con la edad, y con qué técnicas se cuantifican de forma sitio-específica?
6. ¿Qué relación causal está documentada entre el estrés oxidativo (ROS o peróxido de hidrógeno), el descenso de FTO y la senescencia en células somáticas del ovario?
7. ¿Qué métodos permiten cuantificar m6A sitio-específica sobre el 3′UTR de FOS (MeRIP-qPCR, SELECT, miCLIP) y su efecto sobre la estabilidad del mensajero (ensayos con actinomicina D)?
8. ¿Existen antecedentes de restauración de FTO por sobreexpresión o por edición epigenética, y qué fenotipos de senescencia o de daño al ADN revierten?
9. ¿Qué marcadores de senescencia y de daño al ADN (SA-β-galactosidasa, γH2AX, p21, p16) son estándar en modelos de envejecimiento de la granulosa, y cuál es su lectura esperable ante una reversión parcial?
10. ¿Qué sistemas de entrega (transfección transitoria, lentivirus, nanopartículas, ARN mensajero o ribonucleoproteína) son viables y menos perturbadores para dCas9-p300 en KGN, COV434 y granulosa primaria?
11. ¿Qué controles experimentales distinguen de forma rigurosa el efecto epigenético dirigido de artefactos (guía no dirigida, dominio p300 catalíticamente inactivo, dCas9 sin efector)?
12. ¿Se ha aplicado edición epigenómica (CRISPRa o CRISPRi) al rejuvenecimiento de tejido reproductivo o a la reversión parcial del envejecimiento en otros tejidos, y con qué resultados?
13. ¿Cuáles son los riesgos de la desregulación global asociada a FTO por su multiplicidad de blancos de m6A, y cómo se acota una activación fisiológica frente a una suprafisiológica?
14. ¿Qué diferencias funcionales existen entre activar FTO con dCas9-p300 y hacerlo con otros activadores (VP64, VPR, SunTag-p300) sobre este mismo locus?

## 9. Referencias

Gao, X. et al. (2025). MSC-derived exosomes alleviate oxidative stress-induced lysosomal membrane permeabilization damage in degenerated nucleus pulposus cells via promoting m6A demethylation of Nrf2. Free Radical Biology and Medicine, 235, 213–230. DOI: 10.1016/j.freeradbiomed.2025.04.051.

Hilton, I. B. et al. (2015). Epigenome editing by a CRISPR-Cas9-based acetyltransferase activates genes from promoters and enhancers. Nature Biotechnology, 33, 510–517. DOI: 10.1038/nbt.3199.

Jiang, Z. X. et al. (2021). The m6A mRNA demethylase FTO in granulosa cells retards FOS-dependent ovarian aging. Cell Death & Disease, 12, 744. DOI: 10.1038/s41419-021-04016-9.

Jin, C. et al. (2025). Molecular and genetic insights into human ovarian aging from single-nuclei multi-omics analyses. Nature Aging, 5, 275–290. DOI: 10.1038/s43587-024-00762-5.

Kachanov, A. V. et al. (2025). The m6A methylation system limits hepatitis B virus replication. Biomeditsinskaia Khimiia, 71(2), 127–136. DOI: 10.18097/PBMCR1509.

Liao, W. et al. (2026). HDAC2-mediated H3K27ac governs ZFP42 transcription and autophagy in granulosa cells of pigs. Life Sciences, 401, 124527. DOI: 10.1016/j.lfs.2026.124527.
