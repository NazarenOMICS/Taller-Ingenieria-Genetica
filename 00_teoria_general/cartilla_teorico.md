# Cartilla - Parte teórica (Marco teórico)

## Índice operativo

Fuente: `_fuentes_pdf/Cartilla teorico práctica Taller de Ingeniería Genética 2026.pdf` (secciones "Objetivos del curso" y "Marco teórico", pp. 2 y 5–13). Autoras: Pía Campot, Florencia Díaz, Ana Paula Mulet, Magdalena Ripoll, Laura Romanelli (Ingeniería en Biotecnología, Universidad ORT Uruguay).

Contenido de este archivo, para decidir si conviene abrir el cuerpo:

1. Objetivo del curso: entrenamiento en diseño, aplicación y evaluación de edición génica CRISPR para generar KO y KI.
2. Gen CASP8AP2 (FLASH): diana del taller para KO en células HEK-293; su inactivación mejora la expresión de proteínas recombinantes.
3. Sistema CRISPR-Cas: clasificación (clases, tipos, subtipos), tabla comparativa de efectores, mecanismo SpCas9, PAM, reparación NHEJ vs HDR.
4. Clonado Golden Gate: enzimas Tipo IIS, ventajas frente a Gibson/Gateway, uso en CRISPR (vector pX459 digerido con BbsI).
5. Genotipado de mutaciones: ensayos de heterodúplex/mismatches (T7E1, Surveyor), HRMA, ensayo de movilidad heterodúplex (HMA/PAGE), clivaje de secuencias polimórficas, pérdida de sitio de cebador, secuenciación (Sanger/NGS, DSDecode/TIDE/ICE).

Datos clave rápidos: diana = CASP8AP2 en HEK-293; nucleasa = SpCas9 (PAM NGG); corte de Cas9 a 3 pb corriente arriba del PAM; vector = pX459 (Addgene #62988) digerido con BbsI; sensibilidad T7E1 = 0,5–5%; Surveyor detecta indels de hasta 12 nt y frecuencias tan bajas como 3%.

Para las técnicas prácticas día a día y los ejercicios, ver `03_informe/cartilla_practico.md`. Para las referencias completas, ver `bibliografia.md`.

---

## 1. Objetivos del curso

El taller tiene como objetivo entrenar al estudiante en el diseño, aplicación y evaluación de herramientas avanzadas de edición génica (CRISPR) para generar modelos knockout (KO) y knock-in (KI).

## 2. Gen CASP8AP2 en la producción de proteínas recombinantes en células de mamíferos

En las últimas décadas, los productos a base de proteínas han surgido como importantes biofarmacéuticos que tratan enfermedades humanas complejas (por ejemplo, trastornos inflamatorios, cáncer y enfermedades infecciosas). Estos fármacos se sintetizan predominantemente en líneas de células de mamíferos, ya que estas células a menudo producen proteínas terapéuticas con atributos de calidad apropiados que afectan críticamente la potencia y la inmunogenicidad (Richelle & Lewis, 2017).

La alta productividad volumétrica y el título del producto son importantes para obtener terapias proteicas más asequibles. Una línea celular puede lograr estos objetivos a partir de una combinación de cambios que colectivamente hacen del sistema huésped un "superproductor" de proteínas. Estos atributos son seleccionados por los fabricantes e incluyen alta eficiencia de traducción, capacidad secretora, capacidad de crecimiento, duración de la viabilidad a la máxima densidad celular y modificaciones postraduccionales similares a las humanas.

Desde su desarrollo, la línea celular HEK-293 se ha convertido en una de las líneas celulares humanas más utilizadas para la producción de proteínas. La línea HEK-293 ha crecido en prominencia puesto que las proteínas que produce se asemejan más a las proteínas humanas naturales en términos de modificación y función postraduccionales (Bandaranayake & Almo, 2014). Sin embargo, el nivel de producción proteica de esta línea sigue siendo menor que otras con más historial de uso, como, por ejemplo, las células CHO (Vatandoost & Dolatabadi, 2017).

Hasta la fecha, la mayoría de las mejoras en la producción de proteínas se han logrado mediante la optimización de bioprocesos y medios. También se ha utilizado la mutagénesis aleatoria para encontrar células con los fenotipos deseados. Sin embargo, la disponibilidad de datos ómicos de alto rendimiento (genómicos, transcriptómicos, proteómicos y metabolómicos) y la aparición de herramientas de edición del genoma brindan nuevas oportunidades para la ingeniería genómica dirigida de la célula huésped. De hecho, han permitido la sobreexpresión o la regulación a la baja de genes candidatos específicos para aumentar el rendimiento durante el cultivo y controlar la calidad del producto (Richelle & Lewis, 2017).

El gen de la proteína 2 asociada a la caspasa 8 (CASP8AP2) se identificó como un objetivo para mejorar la expresión de proteínas recombinantes. La disminución en su ARN mensajero (ARNm) condujo a una mayor expresión de proteínas recombinantes sin afectar significativamente el crecimiento y la viabilidad celular. CASP8AP2 codifica una proteína conocida como "proteína grande asociada a FLICE" (FLASH), que participa en numerosos procesos celulares. En la apoptosis mediada por Fas, FLASH es parte del complejo de señalización inductor de muerte (DISC) ensamblado después de la unión del receptor de muerte Fas a su ligando FasL. En el ensamblaje del DISC activa la procaspasa 8 para formar la caspasa proteolítica 8, que desencadena la cascada apoptótica extrínseca (Figura 1) (Chen, Evans, & Evans, 2012). FLASH, además de su papel en la apoptosis, también participa en la maduración del ARNm de histonas dependiente de la replicación y la regulación transcripcional de genes de histonas, en la progresión de la fase S del ciclo celular, y en la activación de los factores de transcripción c-MYB y NF-κB. La inactivación de CASP8AP2 en células HEK-293 tiene un efecto positivo sobre la expresión de proteínas recombinantes asociado a la desregulación del ciclo celular (Abaandou, Sharma, & Shiloach, 2021).

En este taller se utilizará CASP8AP2 como gen diana para diseñar y evaluar una estrategia de knockout en células HEK-293.

> Figura 1 (en el PDF original): Rol de FLASH en las vías apoptóticas. Tomada de Chen et al., 2012.

## 3. Sistema CRISPR-Cas

CRISPR-Cas es un sistema inmunológico adaptativo que existe en la mayoría de las bacterias y arqueas, que permite la respuesta a la infección por fagos, virus y otros elementos genéticos extraños. Está compuesto por matrices de espaciadores repetidos CRISPR, que se pueden transcribir en ARN CRISPR (ARNcr) y ARN CRISPR trans-activador (ARNtracr), y por un conjunto de genes asociados a CRISPR (Cas) que codifican proteínas Cas con actividad endonucleasa. Cuando los procariotas son invadidos por elementos genéticos extraños, las proteínas Cas pueden cortar el ADN extraño en pequeños fragmentos, y luego los fragmentos de ADN se integrarán en la matriz CRISPR como nuevos espaciadores. Si el mismo elemento genético vuelve a ingresar, el ARNcr reconoce la secuencia complementaria y guía a la proteína Cas para escindir el ADN diana, protegiendo así al huésped.

Los sistemas CRISPR-Cas se pueden clasificar en dos clases (Clase 1 y Clase 2), 6 tipos (I a VI) y varios subtipos, con complejos efectores de proteínas multi-Cas en sistemas de Clase 1 (Tipo I, III y IV) y una única proteína efectora en sistemas de Clase 2 (Tipo II, V y VI). La clasificación, los miembros representativos y las características típicas de cada sistema CRISPR-Cas se resumen en la Tabla 1.

### Tabla 1. Resumen de sistemas CRISPR-Cas (modificado de Xu & Li, 2020)

| Clase | Tipo | Subtipo | Efector | Diana | Dominio nucleasa | Requiere tracrRNA | PAM/PFS |
|---|---|---|---|---|---|---|---|
| 1 (proteínas Cas múltiples) | I | A, B, C, D, E, F, U | Cascade | ADN bicatenario | Dominio HD fusionado a Cas3 | No | – |
| 1 | III | A, B, C, D | Cascade | ARN monocatenario | Dominio HD fusionado a Cas10 | No | – |
| 1 | IV | A, B | Cascade | ADN bicatenario | Desconocido | No | – |
| 2 (proteína Cas única) | II | A | SpCas9 | ADN bicatenario | RuvC, HNH | Sí | NGG |
| 2 | II | A | SaCas9 | ADN bicatenario | RuvC, HNH | Sí | NNGRRT |
| 2 | II | B | FnCas9 | ADN bicatenario / ARN monocatenario | RuvC, HNH | Sí | NGG |
| 2 | II | C | NmCas9 | ADN bicatenario | RuvC, HNH | Sí | NNNNGATT |
| 2 | V | A | Cas12a (Cpf1) | ADN bicatenario | RuvC, Nuc | No | PAM 5′ rica en AT |
| 2 | V | B | Cas12b (C2c1) | ADN bicatenario | RuvC | Sí | PAM 5′ rica en AT |
| 2 | V | C | Cas12c (C2c3) | ADN bicatenario | RuvC | Sí | PAM 5′ rica en AT |
| 2 | VI | A | Cas13a (C2c2) | ARN monocatenario | 2×HEPN | No | PFS 3′: no-G |
| 2 | VI | B | Cas13b (C2c4) | ARN monocatenario | 2×HEPN | No | PFS 5′: no-C; PFS 3′: NAN/NNA |
| 2 | VI | C | Cas13c (C2c7) | ARN monocatenario | 2×HEPN | No | – |
| 2 | VI | D | Cas13d | ARN monocatenario | 2×HEPN | No | – |

El sistema CRISPR-Cas9 de tipo II derivado de *Streptococcus pyogenes* (SpCas9) es uno de los mejor caracterizados y más utilizados de los numerosos sistemas CRISPR-Cas (Cong et al., 2013; Mali et al., 2013; Ran et al., 2013). Los componentes principales del sistema CRISPR-Cas9 son la endonucleasa Cas9 guiada por ARN y un ARN guía (sgRNA). La proteína Cas9 posee dos dominios nucleasa, denominados HNH y RuvC, y cada uno escinde una hebra del ADN de doble hebra diana. Un ARN sgRNA es una combinación simplificada de ARNcr y ARNtracr. La nucleasa Cas9 y el sgRNA forman una ribonucleoproteína Cas9 (RNP), que puede unirse y escindir el ADN diana específico. Además, se requiere una secuencia de motivo adyacente protoespaciador (PAM) para la unión de la proteína Cas9 al ADN diana.

Durante el proceso de edición del genoma, el sgRNA recluta la endonucleasa Cas9 en un sitio específico del genoma para generar una rotura de doble hebra (DSB), que puede repararse mediante dos mecanismos endógenos de reparación, la unión de extremos no homólogos (NHEJ) o la vía de reparación dirigida por homología (HDR). En muchas condiciones, NHEJ predomina sobre HDR porque es una vía rápida, eficiente y activa durante todo el ciclo celular, sin requerir un molde homólogo. HDR, en cambio, depende de la disponibilidad de un molde de reparación y se ve favorecida principalmente en S/G2. Por lo tanto, aunque la fase del ciclo celular influye en la elección de la vía de reparación, no es el único determinante. El NHEJ puede introducir inserciones o deleciones aleatorias (indels) en los sitios de escisión, lo que lleva a la generación de mutaciones de desplazamiento de marco o codones de parada prematuros dentro del marco abierto de lectura (ORF) de los genes diana. Alternativamente, la HDR puede introducir modificaciones genómicas precisas en el sitio objetivo mediante el uso de un molde de reparación de ADN (Figura 2).

Las deleciones grandes y la eliminación simultánea de varios genes pueden lograrse usando múltiples sgRNA.

> Figura 2 (en el PDF original): Mecanismo de edición génica usando nucleasas (Xu & Li, 2020).

## 4. Clonado Golden Gate

El ensamblaje Golden Gate o clonado Golden Gate tiene sus orígenes en el uso de enzimas de restricción de Tipo IIS y ADN ligasa para ensamblar fragmentos de ADN de forma dirigida (Engler, Kandzia, & Marillonnet, 2008).

Las enzimas de tipo IIS son capaces de cortar el ADN fuera de su sitio de reconocimiento, resultando en extremos 5' o 3' de 4 nucleótidos de composición variable. Así, hay 256 (4⁴) posibilidades distintas de extremos que pueden ser creados por estas endonucleasas. Esto permite clonar sin agregar ninguna secuencia adicional al final de las secuencias introducidas.

La clonación de Golden Gate es uno de los métodos de clonación más simples en términos de tiempo, ya que la digestión y la ligación se pueden realizar en una misma reacción en 30 minutos. El vector de destino y el vector de entrada se colocan en un solo tubo que contiene la enzima de tipo IIS y la ligasa. Aunque el vector de destino original puede religar espontáneamente, esta construcción transitoria retiene sitios funcionales de Tipo IIS y será redigerida. Por el contrario, la formación del producto de ligación deseado es irreversible porque esta construcción no retiene los sitios de reconocimiento de la enzima. Como resultado, el ensamblaje favorece la acumulación del producto deseado y puede alcanzar una alta eficiencia de ligación.

Otro punto fuerte de la clonación de Golden Gate es su escalabilidad. Los extremos cohesivos únicos de 4 bases se pueden usar para ensamblar múltiples fragmentos; de rutina se ensamblan hasta 10 fragmentos en una sola reacción. Estos extremos cohesivos determinan el orden de fragmentos y la pérdida de los sitios de reconocimiento de la enzima después de la ligación favorece la formación de la construcción de interés. Aunque la eficiencia puede disminuir con un mayor número de fragmentos, o con la ligación de fragmentos muy pequeños o muy grandes, estos problemas pueden superarse seleccionando un mayor número de clones potenciales (Engler, Gruetzner, Kandzia, & Marillonnet, 2009; Gearing, 2015).

El ensamblaje de Golden Gate tiene algunas ventajas sobre otros métodos de clonación:

1. Los métodos basados en exonucleasas como el ensamblaje de Gibson requieren de 20 a 40 pb de homología en los extremos de los fragmentos de ADN para determinar el orden de ensamblaje, por lo que los fragmentos con homología de secuencia de 5' o 3' no se pueden ensamblar con este método, pero sí con Golden Gate.
2. El popular sistema de clonación Gateway produce construcciones con una cicatriz de recombinación attB que codifica ocho aminoácidos, pero el ensamblaje Golden Gate puede diseñarse para que no tenga cicatrices.
3. El ensamblaje de Golden Gate también es menos costoso que muchos métodos comerciales de clonación (Gearing, 2015).

La tecnología CRISPR ha adaptado la clonación de Golden Gate para insertar los oligonucleótidos apropiados que especifican una secuencia diana de sgRNA en un plásmido que contiene Cas9 como pX330, pX459 y sus derivados. Esta estrategia de clonación no solo facilita la creación de un solo plásmido que expresa sgRNA, sino que también puede adaptarse para expresar múltiples sgRNA (Gearing, 2015).

En este taller, Golden Gate se utilizará para insertar oligonucleótidos que codifican la secuencia guía dentro del vector pX459 previamente digerido con BbsI.

## 5. Genotipado de mutaciones

Los métodos disponibles para analizar la eficiencia de edición de CRISPR varían según el tipo de mutación que se desee introducir en las células.

La edición con HDR, que introduce nuevas secuencias de ADN, puede evaluarse mediante varios métodos, como la digestión de enzimas de restricción (si la mutación da como resultado la pérdida o ganancia de un sitio de enzima de restricción) o cambios de tamaño en su producto de PCR (si el molde de HR es lo suficientemente grande para detectar un cambio de tamaño).

Por otro lado, cuando se usa NHEJ, la frecuencia y el tipo de indel es aleatoria, lo que resulta en una población heterogénea de células/organismos en las que cada uno puede presentar una o varias secuencias distintas.

### 5.1 Ensayos basados en heterodúplex o mismatches

Los ensayos que detectan apareamientos erróneos o mismatches se basan en el heterodúplex que se forma cuando un amplicón de tipo salvaje (wt) y un amplicón mutante (o amplicones que portan dos mutaciones diferentes) se unen, creando una burbuja debido a las cadenas no emparejadas (figura 3A). Normalmente constan de tres pasos: (1) amplificación del sitio diana y su región flanqueante por PCR; (2) desnaturalizar y volver a unir el ADN para permitir que las cadenas mutantes y de wt formen ADN heterodúplex; y (3) detección del heterodúplex usando un método que es selectivo para la diferencia en la estructura o temperatura de fusión.

La ventaja general de los ensayos de detección de mismatches es que son simples, rápidos y económicos. Se pueden utilizar para genotipar clones individuales o analizar muestras y poblaciones agrupadas. Aunque detectan mutaciones, no revelan ningún detalle de la estructura de la mutación. Además, si el locus objetivo es muy polimórfico, los resultados pueden ser difíciles de interpretar porque diferentes alelos de tipo salvaje también pueden formar ADN heterodúplex. La detección de mismatches se utiliza a menudo de forma semicuantitativa, por ejemplo, para comparar la eficiencia de varios sgRNA, para evaluar las condiciones experimentales que afectan la edición del genoma, o como un enfoque de cribado preliminar para identificar líneas para análisis adicionales utilizando métodos basados en secuenciación más precisos.

### 5.2 El ensayo de restricción de heterodúplex

Los ensayos de restricción de heterodúplex son el procedimiento más utilizado para detectar mutaciones inducidas por edición del genoma. El ensayo utiliza enzimas que escinden el ADN heterodúplex en los mismatches y los bucles extrahelicales formados por múltiples nucleótidos, produciendo dos o más fragmentos más pequeños. Se genera un producto de PCR de entre 300 a 1000 pb con el sitio de escisión de nucleasa pronosticado lejos del centro, de modo que los fragmentos resultantes sean de tamaño diferente y se puedan resolver fácilmente mediante electroforesis en gel convencional o cromatografía líquida de alta resolución (HPLC). Los productos de digestión también pueden analizarse mediante electroforesis automatizada en gel o capilar. La frecuencia de indels en el locus puede estimarse midiendo las intensidades integradas del amplicón de PCR y las bandas de ADN escindidas (figura 3B) (Zischewski, Fischer, & Bortesi, 2017).

Este ensayo puede realizarse con dos enzimas alternativas. La endonucleasa 1 T7 (T7E1) es una resolvasa que reconoce y escinde el ADN emparejado imperfectamente en el primer, segundo o tercer enlace fosfodiéster río arriba del emparejamiento erróneo. La sensibilidad de un ensayo basado en T7E1 es de 0,5 a 5%. Por otro lado, la nucleasa Surveyor es un miembro de la familia CEL de nucleasas específicas de mismatches derivadas del apio. Reconoce y escinde los desajustes debido a la presencia de SNP o pequeños indels, escindiendo ambas cadenas de ADN aguas abajo del desajuste. Puede detectar indels de hasta 12 nt y es sensible a mutaciones presentes en frecuencias tan bajas como 3%, es decir, 1 de cada 32 copias (Zischewski et al., 2017).

T7E1 supera a la nucleasa Surveyor en términos de sensibilidad cuando los sustratos llevan indels, pero ignora los SNP y también tiende a pasar por alto los pequeños indels. La nucleasa Surveyor es menos sensible, pero es más adecuada para la detección de SNP y pequeños indels. Por lo tanto, la elección depende de qué tipos de mutaciones se anticipan o deben detectarse (Zischewski et al., 2017).

El ensayo de restricción de mismatches usualmente subestima la frecuencia de mutación debido a las propiedades de restricción preferenciales de cada enzima. Además, no permite observar mutaciones homocigóticas, salvo que se agregue ADN del genotipo salvaje para permitir la formación de heterodúplex. Por último, si la frecuencia de mutación es lo suficientemente alta, las secuencias mutantes formarán homodúplex que no se podrán detectar, por lo que el porcentaje de mutación no se informará correctamente.

### 5.3 Análisis de melting de alta resolución (HRMA)

El análisis de melting de alta resolución (HRMA) implica la amplificación de una secuencia de ADN que abarca el locus genómico (90–200 pb) mediante PCR en tiempo real con la incorporación de un colorante fluorescente intercalante, seguido del análisis de la curva de melting de los amplicones.

El HRMA se basa en la pérdida de fluorescencia cuando se liberan tintes intercalados del ADN de doble hebra durante la desnaturalización térmica. Registra el perfil de desnaturalización dependiente de la temperatura de los amplicones y detecta si el proceso de melting involucra una o más especies moleculares.

A diferencia de las curvas de fusión analizadas en los experimentos típicos de PCR cuantitativa (qPCR), los datos se recopilan en incrementos de temperatura más estrechos de 0,2 °C, seguidos de la normalización y el análisis de la señal. Los cambios de temperatura de fusión y la forma de las curvas de fusión pueden proporcionar información útil: las variantes alélicas homocigotas pueden causar un cambio de temperatura en la curva de fusión en comparación con el homodúplex de tipo salvaje, mientras que los heterodúplex que representan mutaciones heterocigotas cambian la forma de la curva de fusión debido a la presencia de desajustes.

A diferencia del ensayo de restricción de mismatches o heterodúplex, el HRMA puede distinguir entre diferentes alelos mutantes y también puede distinguir secuencias homocigotas mutantes de homocigotas wt debido al cambio en las temperaturas de fusión causado por la diferente composición de nucleótidos.

Debido a que el HRMA no es destructivo, los amplicones se pueden analizar más a fondo mediante otros métodos, como electroforesis en gel y secuenciación. Su sensibilidad depende del tamaño del amplicón y del tipo de mutación. Para indels mayores de 4 pb, el límite de detección estimado en un amplicón de 100 pb es al menos del 2%, es decir, un mutante entre 50 genomas wt. Una limitante del HRMA es que los fragmentos diana son relativamente cortos, por lo que no se pueden detectar indels más grandes (Zischewski et al., 2017).

### 5.4 Ensayo de movilidad heterodúplex (HMA)

Las mutaciones también se pueden detectar analizando fragmentos de PCR rehibridados directamente mediante electroforesis en gel de poliacrilamida no desnaturalizante (PAGE). Este método aprovecha la migración diferencial de ADN heterodúplex y homodúplex en geles de poliacrilamida. El ángulo entre las cadenas de ADN apareadas correctamente y aquellas con mismatches causados por un indel determina que el ADN heterodúplex migra a una velocidad significativamente más lenta que el ADN homodúplex en condiciones nativas, y pueden distinguirse fácilmente en función de su movilidad (figura 3C).

Los fragmentos de 140 a 170 pb se pueden separar en un gel de poliacrilamida al 15%. Alternativamente, fragmentos de mayor tamaño pueden separarse en geles con menor concentración de poliacrilamida. La sensibilidad de tales ensayos puede acercarse al 0,5% en condiciones óptimas, que es similar a T7E1. La ventaja de este método de un solo paso es que no implica reacciones enzimáticas que consuman tiempo y elimina los resultados falsos negativos causados por la digestión incompleta de fragmentos de ADN mal emparejados. Sin embargo, solo se pueden resolver pequeños amplicones, por lo que el ensayo solo puede detectar SNP y pequeños indels, y la sensibilidad de PAGE en todo el espectro de indels no está clara (Zischewski et al., 2017).

> Figura 3 (en el PDF original): Genotipado basado en heterodúplex. A: formación de heterodúplex entre secuencias wt y con indels o secuencias con distintos indels. B: HMA, donde se observan bandas de mayor tamaño cuando existen mutaciones. C: Ensayo con endonucleasa, se observan bandas de menor tamaño donde hubo digestión. Modificado de Zischewski et al., 2017.

### 5.5 Ensayos de clivaje de secuencias polimórficas

La posición de las mutaciones inducidas por nucleasas específicas de sitio es generalmente predecible porque ZFN y TALEN inducen DSB genómicos en la región espaciadora entre sus sitios de reconocimiento de ADN, y Cas9 induce DSB 3 pb corriente arriba del motivo adyacente protoespaciador (PAM).

Si es posible diseñar un experimento de tal manera que la nucleasa corte dentro de un sitio de reconocimiento de enzimas de restricción o a menos de 5 pb de él, la combinación de PCR y enzimas de restricción es un método sencillo y rentable para la detección de indels. Este enfoque implica la amplificación de un sitio diana, la digestión con la enzima de restricción apropiada seguida luego por el análisis de los tamaños de los fragmentos por electroforesis en gel.

A diferencia de otros ensayos de detección de errores de apareamiento ampliamente utilizados, este tipo de análisis puede detectar mutantes homocigotos y, siempre que la secuencia diana de nucleasa en sí no sea polimórfica, no se verá afectada por polimorfismos de secuencia cerca de los sitios diana de la nucleasa. Puede detectar todo tipo de mutaciones (SNP, indels pequeños y grandes) siempre que interrumpan el sitio de restricción y, por lo tanto, es muy sensible y conveniente. Sin embargo, el análisis está limitado por la disponibilidad de sitios de restricción cerca del sitio diana.

### 5.6 Pérdida de un sitio de unión del cebador

Cuando el ADN genómico se amplifica con dos pares de cebadores, uno que abarca la región diana pero se hibrida fuera de ella, y otro que incluye un cebador que se superpone al sitio indel putativo, las mutaciones en el sitio objetivo evitarán la hibridación del cebador y solo el amplicón más grande se producirá. Si se usa un enfoque de qPCR, se puede estimar la frecuencia de mutación y se puede secuenciar el amplicón más grande que abarca todo el sitio objetivo para caracterizar las mutaciones. Los productos de la PCR se resuelven mediante electroforesis, por lo que el método es rápido y económico y, siempre que se conserve el emparejamiento de secuencias con el extremo 5' del cebador, los polimorfismos naturales del genoma no deberían interferir con los resultados.

La principal limitación es que las mutaciones puntuales pueden pasarse por alto y que el método no tiene una alta sensibilidad.

### 5.7 Secuenciación

Las mutaciones inducidas por nucleasas específicas de sitio se pueden caracterizar en detalle mediante la secuenciación de amplicones que abarcan todo el sitio diana. Los enfoques adecuados incluyen la secuenciación de Sanger de fragmentos clonados individuales o la mezcla de amplicones en masa, y la secuenciación de nueva generación (NGS).

La gran ventaja de los métodos de detección basados en secuenciación es la información directa y detallada sobre la naturaleza y diversidad de mutaciones. El estándar para la identificación de mutaciones inducidas en sitios diana es la clonación de amplicones de cada evento individual en vectores independientes, seguida de secuenciación de Sanger de los productos de PCR clonados (50–100 eventos según la eficiencia de la nucleasa). Esto revela tanto la frecuencia como el tipo de mutaciones en el locus objetivo, pero es laborioso, lento y costoso cuando se procesan muchas muestras.

Una alternativa es secuenciar los productos de PCR directamente. A menos que la mutación sea homocigótica, la secuenciación directa de Sanger generará múltiples picos superpuestos. En el caso de organismos diploides con mutaciones heterocigotas o bialélicas, se obtienen dos secuencias superpuestas comenzando en el sitio de la mutación. En organismos poliploides o cuando se secuencian clones agrupados, se pueden encontrar incluso más secuencias en un solo cromatograma.

La decodificación automática de cromatogramas superpuestos derivados de amplicones de PCR que contienen varios tipos de mutaciones se puede lograr utilizando herramientas bioinformáticas como DSDecode, TIDE e ICE (Brinkman, Chen, Amendola, & van Steensel, 2014; Conant et al., 2022; Zischewski et al., 2017).
