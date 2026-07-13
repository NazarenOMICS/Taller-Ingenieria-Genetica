# Cartilla - Parte práctica (Actividades prácticas y Ejercicios)

## Índice operativo

Modalidad de evaluación asociada: **Informe** de resultados de la actividad principal (30 puntos; entrega jueves 30/07; ~10 carillas).
Fuente: `_fuentes_pdf/Cartilla teorico práctica Taller de Ingeniería Genética 2026.pdf` (secciones "Cronograma de actividades", "Actividades prácticas" y "Ejercicios", pp. 4 y 14–20).

Qué contiene:

1. Cronograma completo del taller (3 semanas), actividad principal vs. actividades complementarias.
2. Actividades prácticas día a día, con reactivos, kits, enzimas y secuencias de oligos/primers.
3. Los 16 ejercicios teórico-prácticos.

Datos clave rápidos: gen diana CASP8AP2 en HEK-293; vector pX459 digerido con BbsI; 4 guías (sense/antisense); transformación en DH5α; transfección con Lipofectamine 2000 + selección con puromicina; genotipado por T7E1, HMA (gel de acrilamida 6% con tinción de plata) y clivaje con HindIII para la guía 4. Los protocolos detallados están en `protocolo_1_clonado.md` … `protocolo_4_tincion_plata.md`.

Nota: el informe se redacta siguiendo `../Rules_Of_Writing.md` y se califica con los criterios generales de la Rúbrica (ver `../02_obligatorio/rubrica_detallada.md`, que la Cartilla no reproduce específicamente para el informe).

---

## Cronograma de actividades

### Semana 1

| Día | Actividad principal | Actividades complementarias |
|---|---|---|
| Lunes 13 | Purificación de plásmido. Annealing y ligación de oligos. | Presentación de propuesta de obligatorio. Presentación del curso. |
| Martes 14 | Transformación y plaqueo. Diseño de PCR. | Diseño de guías. |
| Miércoles 15 | Chequeo por PCR. Cultivo de colonia seleccionada. Siembra de células. | - |
| Jueves 16 | Miniprep. Transfección de células. | - |

### Semana 2

| Día | Actividad principal | Actividades complementarias |
|---|---|---|
| Lunes 20 | No hay clases | - |
| Martes 21 | - | Diseño de moldes para KI. Presentación oral de técnicas. |
| Miércoles 22 | No hay clases | - |
| Jueves 23 | Extracción de ADN. PCR. Purificación de pPCR. | Análisis de cromatogramas de secuencias mutadas. |

### Semana 3

| Día | Actividad principal | Actividades complementarias |
|---|---|---|
| Lunes 27 | No hay clases | - |
| Martes 28 | Ensayo de T7E1. Ensayo de digestión. | - |
| Miércoles 29 | Ensayo de HMA. Análisis de resultados. Terminar pendientes. | - |
| Jueves 30 | - | Presentación oral obligatorio. Entrega del informe de resultados. |

Jueves 06/08: Entrega de obligatorio por Gestión.

## Actividades prácticas

### Lunes, semana 1

**Purificación de vector pX459 digerido y desfosforilado.** Las actividades de este día están basadas en el protocolo 1 de Zhang y colaboradores (disponible en Aulas) y se modificarán según las enzimas disponibles en el laboratorio. El plásmido pX459 (Addgene #62988) fue digerido con la enzima BbsI (R3539, NEB) y desfosforilado con la fosfatasa alcalina FastAP (EF0651, Thermo Scientific) (Addgene, s. f.). Durante la clase se correrá el vector digerido en un gel de agarosa 0,8%, se cortará la banda del plásmido lineal y se purificará utilizando el kit Wizard SV Gel and PCR Clean-Up System (A9282, Promega).

**Hibridación de oligonucleótidos, fosforilación y clonado.** Los oligonucleótidos diseñados para generar las guías son los siguientes:

| Guía | Sense | Antisense |
|---|---|---|
| Guía 1 | CACCGGAACAATGATGAAGGCTCAC | AAACGTGAGCCTTCATCATTGTTCC |
| Guía 2 | CACCGGGGTTGGACAGTGCTGTTTC | AAACGAAACAGCACTGTCCAACCCC |
| Guía 3 | CACCGCCTCTTAAGAACAATGATGA | AAACTCATCATTGTTCTTAAGAGGC |
| Guía 4 | CACCGGATCAAGCTTTGGTTAAGAT | AAACATCTTAACCAAAGCTTGATCC |

Estos oligonucleótidos deberán ser fosforilados, hibridados y ligados con el vector pX459 digerido según el protocolo 1. Se cuenta con la enzima polinucleótido quinasa T4 M0201S (NEB) y con la ligasa T4 (M0202S, NEB). La ligación se llevará a cabo con 0,5 µl de ligasa (el protocolo estipula 1,0 µl).

### Martes, semana 1

**Transformación.** Se cuenta con bacterias DH5α electrocompetentes. Se transformarán 5 μL de cada ligación realizando los controles correspondientes.

### Miércoles, semana 1

**Colony PCR.** Se identificarán mediante PCR los clones bacterianos que contienen la construcción de interés. A partir de las colonias positivas, se inocularán cultivos líquidos para la posterior miniprep. Se cuenta con Taq NZYTaq II DNA polymerase (NZYtech) y los siguientes primers:

| Guía | Fw | Rv |
|---|---|---|
| Guía 1 | CGGAACAATGATGAAGGCTCAC | ATAGGGGGCGTACTTGGCAT |
| Guía 2 | GGGTTGGACAGTGCTGTTTC | ATAGGGGGCGTACTTGGCAT |
| Guía 3 | CCGCCTCTTAAGAACAATGATGA | ATAGGGGGCGTACTTGGCAT |
| Guía 4 | GGATCAAGCTTTGGTTAAGAT | ATAGGGGGCGTACTTGGCAT |

**Siembra de células.** Cada grupo recibirá una T25 con células HEK-293 en fase de crecimiento exponencial. Se sembrarán las células según lo planificado y siguiendo el protocolo 2 (disponible en Aulas).

### Jueves, semana 1

**Miniprep.** Se purificará plásmido para transfectar las células a partir de pellets de los cultivos líquidos realizados el miércoles de la semana 1. Se cuenta con el kit ZR Plasmid Miniprep - Classic (D4015, Zymo Research).

**Transfección.** Con el plásmido obtenido se transfectarán las células HEK-293 utilizando Lipofectamine 2000 Transfection reagent (11668019, Invitrogen) siguiendo el protocolo 3 (disponible en Aulas). A las 24 h postransfección se realizará selección transitoria con puromicina para enriquecer la población transfectada.

### Jueves, semana 2

Se extraerá el ADN de las células transfectadas usando el kit Quick-DNA Miniprep Plus Kit (D4068, Zymo Research). Se realizará una PCR para amplificar la región genómica de interés utilizando la enzima Taq NZYTaq II DNA polymerase (NZYtech) y los siguientes primers:

- CASP8AP2-Fw: TCCTGGTCCTTTAGTGTAGGAATG
- CASP8AP2-Rv: CACCAGCACTAGTTGCACTT

Se purificarán los productos de PCR utilizando el kit DNA Clean and Concentrator-5 (D4013, Zymo Research).

### Martes, semana 3

**Ensayo T7E1.** Se realizará el ensayo de T7E1 con la enzima T7 Endonuclease 1 (M0302L, NEB). Se seguirá el protocolo de la enzima con las siguientes modificaciones: usar 200 ng de ADN, 0,5 µL de enzima y digerir durante 30 min. Se visualizará junto con la corrida de HMA del miércoles de la semana 3.

Para las muestras transfectadas con la guía 4, se realizará un ensayo de clivaje de secuencias polimórficas con la enzima HindIII y se visualizará en un gel de agarosa al 2%. Alternativamente se podrá observar este resultado en el gel de acrilamida junto con la corrida de HMA.

### Miércoles, semana 3

**Ensayo HMA.** Se realizará un ensayo de HMA en un gel de acrilamida para ADN al 6%. Se revelará el gel mediante una tinción con plata siguiendo el protocolo 4 (disponible en Aulas).

Nota: al preparar los geles, lavar cuidadosamente ambas placas de vidrio con etanol al 70% utilizando guantes. Evitar tocar la superficie del vidrio con las manos, ya que las huellas dactilares serán reveladas durante la tinción con plata y pueden interferir con la visualización de las bandas.

## Ejercicios

1. A continuación se observa la región genómica y los transcriptos posibles del gen FOXO4 de humanos. (a) ¿Cómo se obtiene esta información? (b) Si buscara realizar un KO del gen, ¿qué locus de la secuencia seleccionaría para diseñar la/las guías?
2. ¿Qué problemas podrían aparecer si el sitio de corte de CRISPR se ubica demasiado cerca del inicio de la secuencia codificante?
3. En su laboratorio le solicitan que diseñe guías para realizar un KO del gen BRCA2 en células HT-29. ¿Qué secuencia seleccionaría para ese fin?
4. ¿Qué debemos tener en cuenta si existe splicing alternativo en el transcripto del gen que queremos knockear?
5. Usted está trabajando con células pancreáticas de ratón y quiere realizar un KO en el gen Reg1. (a) Diseñe dos guías que le permitan asegurarse la inactivación del gen utilizando la herramienta CRISPOR. (b) ¿Cómo determina los potenciales off targets de sus guías? (c) ¿Cómo determina la eficiencia de corte de sus guías? (d) Elija una guía que no tenga potenciales sitios off targets exónicos en el mismo cromosoma que su gen. (e) ¿Qué es la secuencia seed? ¿Por qué es importante para la especificidad de las guías? (f) En su guía seleccionada, ¿cuántos potenciales off targets tienen 4 mismatches con respecto a su secuencia objetivo? ¿Cuántos de estos son idénticos en la secuencia seed a la secuencia objetivo?
6. A continuación se presentan los resultados de un experimento en donde se comparó la eficiencia de tres posibles sgRNA para generar un indel. ¿Cuál de las guías le parece más eficiente? ¿Cuál parece menos eficiente?
7. Usando Fiji/ImageJ calcule la eficiencia de mutación en las muestras 1 y 2 de la imagen.
8. En un experimento se inyectaron embriones con un sgRNA para generar una mutación en el gen Vdr de ratón. Posteriormente se realizó un PCR del sitio de interés de las crías nacidas. En la imagen se observan los resultados del PCR. Explique los resultados y planifique los siguientes pasos en el genotipado.
9. En una estrategia de edición por HDR usando un ssODN para introducir una mutación puntual, ¿a qué distancia ideal debería estar el sitio de corte de Cas9 respecto del nucleótido que se desea modificar?
10. ¿Qué sucedería si la secuencia PAM (motivo adyacente al protoespaciador) formara parte del ARN guía en el sistema CRISPR?
11. ¿Qué ocurriría después de HDR si la secuencia PAM queda intacta en el alelo editado? ¿Qué modificación podría introducirse para evitarlo?
12. ¿Qué tipo de molde de ADN es más eficiente a la hora de inducir HDR? ¿Uno de doble o uno de simple cadena?
13. La serina 190 de la proteína FOXO de Drosophila melanogaster tiene un rol en la muerte celular y el transporte nuclear. Diseñe una estrategia para reemplazar el codón que codifica esa serina por un codón que codifique glicina.
14. ¿Qué debería tener en cuenta a la hora de elegir un sitio de inserción de loxP en intrones de un gen?
15. Diseñe una estrategia para eliminar el segundo exón del gen Glyma.01G039000 que codifica a la proteína TIR-NBS-LRR CLASS DISEASE RESISTANCE PROTEIN-RELATED en soja.
16. Diseñe una estrategia para intercambiar el gen HYM1 de Saccharomyces cerevisiae (YKL189W) por su ortólogo cab39 de salmón atlántico (Salmo salar), correspondiente al gen ENSSSAG00000042531.
