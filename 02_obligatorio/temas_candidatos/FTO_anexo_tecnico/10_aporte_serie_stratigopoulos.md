# Qué aporta cada trabajo de la serie Stratigopoulos al diseño

Auditoría textual realizada el 2026-07-26 sobre copias locales de texto completo en formato HTML, ubicadas en `Search/manual-reinforce-pdfs/`. El binario PDF no pudo obtenerse porque los servidores devolvieron páginas de verificación anti-robot.

---

## 1. Stratigopoulos et al. (2011), J Biol Chem 286(3):2155-2170

DOI 10.1074/jbc.M110.188482, PMID 21037323.

**Qué aporta.** Es la única fuente que identifica un factor de transcripción actuando sobre un elemento regulador de *FTO* con mecanismo descrito, incluida una isoforma con función represora. Eso matiza la conclusión de q15 según la cual no se identifica ningún represor asociado al promotor de *FTO*.

**Afirmaciones verificadas literalmente.** Que *FTO* y *RPGRIP1L* están regulados por las isoformas P200 y P110 de CUX1; que la regulación ocurre a través de un único sitio AATAAATA, conservado en ratón, dentro de la región intrónica de *FTO* asociada a adiposidad en humanos; que el polimorfismo rs8050136, ubicado en ese sitio, afecta las afinidades de unión de P200 y P110; y que la unión de P200 reprime *FTO* mientras que la de P110 aumenta la actividad transcripcional desde los promotores mínimos de *FTO* y de *RPGRIP1L*.

**Calificación metodológica obligatoria.** La evidencia proviene de ensayos de desplazamiento de movilidad electroforética y de ensayos de promotor con gen reportero, sobre construcciones de **promotor mínimo** amplificadas de ADN genómico de fibroblastos primarios humanos homocigotos para uno u otro alelo de rs8050136, ensayadas en líneas hipotalámicas y de neuroblastoma murinas. No hay medición sobre el locus endógeno ni en granulosa.

**Formulación precisa, de uso obligatorio en el entregable.** Los experimentos demostraron unión a secuencias promotoras y modulación de construcciones reporteras en los modelos ensayados, pero no regulación del locus endógeno en granulosa.

**Consecuencia sobre el diseño.** Refuerza que existen elementos reguladores de *FTO* fuera de la región proximal, y refuerza también que los elementos compartidos no discriminan entre ambos genes, puesto que P110 activa los promotores mínimos de los dos. No modifica la selección de ventanas.

---

## 2. Stratigopoulos et al. (2014), Cell Metab 19(5):767-779

DOI 10.1016/j.cmet.2014.04.009, PMID 24807221.

**Qué aporta.** Evidencia funcional de que la reducción de dosis de *Rpgrip1l* tiene consecuencia fenotípica sistémica en ratón, con un mecanismo propuesto a través del receptor de leptina y del cilio primario.

**Afirmación verificada literalmente sobre la arquitectura del locus.** "RPGRIP1L (Retinitis Pigmentosa GTPase Regulator-Interacting Protein-1 Like) is located >100bp 5′ in the opposite transcriptional orientation of FTO".

**Inconsistencia registrada entre publicaciones del mismo grupo.** El trabajo de 2016 consigna "<100 bp" y el de 2014 consigna ">100bp". La inconsistencia se documenta sin declarar incorrecta a ninguna de las dos: la distancia puede depender de la especie considerada, del ensamblado empleado, del transcrito tomado como referencia o de la definición del sitio de inicio, y ninguno de los dos textos explicita cuál de esos elementos utiliza. La referencia operativa del proyecto son los 297 pb calculados sobre GRCh38.p14 con Ensembl 116 entre los TSS de referencia definidos. Ambos trabajos se citan para sostener la orientación divergente y la proximidad.

**Afirmación verificada sobre el fenotipo.** Los animales heterocigotos para un alelo nulo de *Rpgrip1l* resultaron más obesos que los silvestres, con caracterización metabólica y conductual, y con experimentos orientados a un mecanismo sobre la señalización del receptor de leptina isoforma b.

**Consecuencia sobre el diseño.** Aporta el argumento de que una modificación de dosis de *RPGRIP1L* no es fenotípicamente neutra, al menos en ratón y para pérdida de función. No informa sobre las consecuencias de un aumento, ni sobre granulosa. Sostiene la decisión de medir *RPGRIP1L* en todos los brazos.

---

## 3. Stratigopoulos et al. (2016), J Clin Invest

DOI 10.1172/JCI85526, PMID 27064284.

**Qué aporta.** Confirma en un tercer trabajo la arquitectura divergente y el eje CUX1, y agrega el dato de dosis alélica en neuronas humanas derivadas de células madre pluripotentes inducidas.

**Afirmaciones verificadas literalmente.** Que el alelo protector de obesidad en rs8050136 promueve la unión de la isoforma P110, que actúa como activadora de la expresión de *FTO* y de *RPGRIP1L*, mientras que el alelo de riesgo es ocupado preferentemente por P200, que actúa como represor transcripcional. Que hubo efectos de dosis alélica sobre la expresión de *FTO*, *RPGRIP1L* y *AKTIP*, mientras que la de otros genes vecinos, incluidos *IRX3*, *IRX5* y *RBL2*, no se alteró.

**Consecuencia sobre el diseño, formulada como decisión de alcance.** El resultado negativo para *IRX3*, *IRX5* y *RBL2* permite dejarlos fuera del panel primario de lectura, pero **no demuestra que no puedan responder a dCas9-p300 en granulosa humana**: el experimento midió efecto de dosis alélica en neuronas derivadas de células madre pluripotentes inducidas, no acetilación dirigida en granulosa. La exclusión es una decisión de alcance del diseño y no una exclusión biológica definitiva.

*AKTIP* sí mostró efecto de dosis alélica en ese trabajo, de modo que **no corresponde afirmar que quedó resuelto no incorporar ningún otro gen**. El panel queda así: *FTO* y *RPGRIP1L* como lecturas obligatorias, por compartir directamente el promotor divergente; *AKTIP* como lectura secundaria opcional, excluido del panel principal por su distancia al bloque intervenido y por el alcance experimental del proyecto, no por ausencia de evidencia.

---

## 4. Lo que la serie completa no aporta

Ninguno de los tres trabajos mide granulosa, ni ovario, ni ningún tejido reproductivo. Ninguno emplea edición epigenómica dirigida. Ninguno informa el estado de acetilación del bloque promotor divergente. La serie sostiene la arquitectura del locus y la existencia de regulación compartida, no la viabilidad de la intervención propuesta.

---

## 5. Efecto sobre el estado de la evidencia del proyecto

| Elemento | Antes | Después |
| :--- | :--- | :--- |
| Arquitectura divergente y proximidad | Sólido, con cifra tomada de una cita | Sólido, con cifra propia medida sobre GRCh38 e inconsistencia entre fuentes registrada sin declarar incorrecta a ninguna |
| Existencia de un represor asociado a un elemento regulador de *FTO* | De búsqueda | Verificado como unión a secuencias promotoras y modulación de construcciones reporteras en los modelos ensayados, no como regulación del locus endógeno en granulosa |
| Consecuencia de modificar *RPGRIP1L* | De búsqueda | Verificado para pérdida de función en ratón; sin datos para aumento ni para granulosa |
| Panel de lectura | Duda abierta sobre *RBL2* | *FTO* y *RPGRIP1L* obligatorios; *AKTIP* secundario opcional; *IRX3*, *IRX5* y *RBL2* fuera del panel primario por decisión de alcance, no por exclusión biológica |
