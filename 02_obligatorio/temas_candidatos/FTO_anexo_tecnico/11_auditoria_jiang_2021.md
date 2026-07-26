# Auditoría textual de Jiang et al. (2021)

Jiang ZX, Wang YN, Li ZY, Dai ZH, He Y, Chu K, Gu JY, Ji YX, Sun NX, Yang F, Li W. *The m6A mRNA demethylase FTO in granulosa cells retards FOS-dependent ovarian aging*. Cell Death and Disease (2021) 12:744. DOI: 10.1038/s41419-021-04016-9.

Auditoría realizada el 2026-07-26 sobre el PDF completo alojado en `Vault/Research/Papers/dcas9-fto-granulosa/q04-eje-fto-m6a-fos/`. Alcance: resumen, resultados, figuras y sus epígrafes, discusión, materiales y métodos, y las referencias a material suplementario contenidas en el texto. Las figuras suplementarias S1 a S4 y las tablas suplementarias se auditan por lo que el texto principal declara de ellas, puesto que el archivo suplementario no está en el repositorio.

---

## 1. Modelo celular y organismo

**Exclusivamente humano y exclusivamente in vitro o ex vivo.** La búsqueda de la expresión "in vivo" en el texto completo no devuelve ninguna coincidencia, y no se describe modelo animal alguno.

Material clínico: muestras de células de la granulosa obtenidas de pacientes sometidas a fecundación in vitro o inyección intracitoplasmática de espermatozoides, recolectadas tras hiperestimulación ovárica controlada en el centro de medicina reproductiva del Hospital Changzheng adscripto a la Universidad Médica Naval. El estudio fue aprobado por el comité de ética de esa institución y las muestras se recolectaron con consentimiento informado de las pacientes.

Líneas celulares: **COV434 y KGN**, ambas de granulosa humana.

---

## 2. Descenso de FTO en granulosa envejecida

**Verificado.** El m6A total de las células de la granulosa de **seis pares** de ovarios envejecidos y ovarios control se midió por colorimetría, y la cantidad de m6A resultó significativamente mayor en el ARN total de granulosa de ovarios envejecidos que en la de ovarios normales.

El descenso de FTO en granulosa de ovarios envejecidos se sostiene por RT-PCR, con **n = 15 para FTO y n = 10 para los demás genes**, y por western blot e inmunofluorescencia comparando granulosa envejecida contra granulosa joven. Se incorpora además inmunohistoquímica procedente del Human Protein Atlas para mostrar expresión de FTO en granulosa de tejido ovárico.

**Naturaleza de la evidencia**: comparativa entre grupos de muestras. Es correlativa.

---

## 3. Relación entre FTO, m6A y FOS

**Verificada, con encadenamiento experimental completo en la dirección de pérdida de función.**

1. Secuenciación de inmunoprecipitación de ARN metilado y secuenciación de ARN mensajero sobre COV434 con FTO silenciado, con tres réplicas.
2. Aumento de m6A localizado en el 3′ UTR de *FOS*, coincidente con la posición de secuencias consenso GGAC.
3. Confirmación por inmunoprecipitación seguida de PCR cuantitativa: la modificación m6A del ARNm de *FOS* aumenta en COV434-shFTO y KGN-shFTO respecto de sus controles.
4. Inmunoprecipitación de ARN con anticuerpo anti-FTO: la proteína FTO puede unirse al ARNm de *FOS*, en figura suplementaria S4.
5. Ensayo con actinomicina D: el decaimiento del ARNm de *FOS* en células con FTO silenciado es significativamente más lento que en las células control.
6. Minigenes reporteros con 3′ UTR de *FOS* silvestre y mutado, para ligar el efecto al sitio m6A.
7. Identificación del lector: IGF2BP2 se une al ARNm de *FOS*; su silenciamiento disminuye la expresión de *FOS* y acelera su decaimiento.

**Naturaleza de la evidencia**: causal en la dirección de pérdida de función de FTO.

---

## 4. FOS como blanco funcional

**Verificado, con un matiz que debe conservarse.** El epígrafe de la figura 5 dice literalmente: "**Silencing FOS partially alleviated FTO-dependent aging** in COV434 and KGN cells". El alivio es **parcial**, no una reversión completa, y así lo enuncian los autores.

La lectura del alivio se hace por inmunofluorescencia de γH2A.X y tinción de β-galactosidasa.

**Nota de convergencia con nuestro diseño**: la expectativa de desacople parcial que ya figuraba en el esqueleto como lectura esperable coincide con lo que reporta la fuente.

---

## 5. Efecto de restaurar o aumentar FTO

**Este es el punto más débil para el proyecto y obliga a corregir una afirmación del corpus.**

Lo único que el trabajo reporta sobre ganancia de función es una frase: "in the two cell lines that overexpressed FTO, FOS was found to be significantly downregulated (Supplementary Fig. S3)". Es decir, **la sobreexpresión de FTO reduce la expresión de *FOS***, y el dato está en material suplementario.

**No hay en este trabajo ningún experimento que demuestre que aumentar FTO revierte el fenotipo senescente.** La afirmación del resumen según la cual "FTO acts as a senescence-retarding protein via m6A" es una interpretación de los autores apoyada en la dirección del silenciamiento y en el rescate parcial por silenciamiento de *FOS*, no en un experimento de ganancia de función medido sobre marcadores de senescencia.

**Corrección requerida.** El informe general del proyecto sostiene, atribuyéndolo a esta fuente, que la sobreexpresión de FTO protege a las células de la granulosa actuando como proteína retardadora de senescencia que revierte desórdenes epigenéticos y restaura la homeostasis celular. Esa formulación excede lo que Jiang et al. (2021) demuestra. La evidencia de reversión fenotípica por aumento de FTO en granulosa proviene de otros trabajos del corpus y debe atribuirse a ellos.

---

## 6. Evidencia sobre senescencia

**Marcadores efectivamente utilizados**: γH2A.X por inmunofluorescencia y tinción de β-galactosidasa. La búsqueda de p16, p21, LMNB1 y de la expresión "senescence markers" no devuelve coincidencias. Los marcadores p16 y p21 que figuran en el panel del proyecto provienen de otras fuentes del corpus y no deben atribuirse a Jiang.

**Modelo de senescencia**: no es senescencia espontánea ni replicativa. Se indujo con **medio conteniendo 50 µM de peróxido de hidrógeno**. La formulación del epígrafe de la figura 1 es que las células con FTO silenciado "more readily enter senescence induced by hydrogen peroxide", es decir, entran más fácilmente en senescencia inducida por peróxido de hidrógeno.

**Observación de terminología**: el texto describe γH2A.X como "a marker of senescence". Es, en rigor, un marcador de daño en el ADN, y así conviene enunciarlo en el entregable propio.

---

## 7. Qué afirmaciones son causales y cuáles correlativas

| Afirmación | Naturaleza | Base experimental |
| :--- | :--- | :--- |
| FTO desciende y m6A aumenta en granulosa de ovarios envejecidos | Correlativa | Comparación entre grupos de muestras clínicas |
| El silenciamiento de FTO aumenta m6A en el 3′ UTR de *FOS* | Causal | Silenciamiento estable con lentivirus, MeRIP-seq y MeRIP-qPCR |
| El silenciamiento de FTO enlentece la degradación del ARNm de *FOS* | Causal | Actinomicina D |
| El efecto depende del sitio m6A del 3′ UTR | Causal | Minigenes reporteros silvestre y mutado |
| IGF2BP2 media la estabilización | Causal | Silenciamiento de IGF2BP2 |
| El silenciamiento de FTO facilita la entrada en senescencia | Causal, en un modelo inducido | γH2A.X y β-galactosidasa bajo peróxido de hidrógeno |
| El silenciamiento de *FOS* alivia parcialmente ese fenotipo | Causal, con alivio parcial | Figura 5 |
| El aumento de FTO reduce *FOS* | Causal | Figura suplementaria S3 |
| El aumento de FTO revierte senescencia | **No demostrada en este trabajo** | Sin experimento correspondiente |

---

## 8. Consecuencia sobre el estado de la evidencia del proyecto

| Elemento | Antes | Después de la auditoría |
| :--- | :--- | :--- |
| Descenso de FTO en granulosa envejecida | Moderado | **Sólido**, con la aclaración de que es evidencia correlativa sobre seis pares de muestras |
| Eje FTO–m6A–FOS | Moderado | **Sólido en la dirección de pérdida de función**, con encadenamiento causal completo |
| *FOS* como efector del fenotipo | Moderado | **Sólido, con alivio parcial** |
| Reversión de senescencia por aumento de FTO | Moderado, atribuido a esta fuente | **No sostenido por esta fuente**; debe atribuirse a los otros trabajos del corpus y reevaluarse su nivel |
| Modelo de senescencia | No explicitado | Inducido con peróxido de hidrógeno 50 µM, no replicativo |
| Existencia de respaldo in vivo | Implícito en algunas formulaciones | **Inexistente en esta fuente** |

---

## 9. Correcciones a aplicar en otros archivos

1. `INFORME_GENERAL.md`, apartado 4.5: retirar de la atribución a esta fuente la afirmación de que la sobreexpresión de FTO revierte senescencia y restaura homeostasis, y reasignarla a los trabajos del corpus que efectivamente la sostienen.
2. `INFORME_GENERAL.md`, apartado 4.3: precisar que el modelo de senescencia es inducido por peróxido de hidrógeno y que no hay evidencia in vivo en esta fuente.
3. Panel de marcadores de senescencia: mantener p16 y p21 en el diseño propio, pero sin atribuirlos a Jiang et al. (2021).
4. Esqueleto, apartado B.5: la auditoría queda completada y la marca de "pendiente de auditoría textual final" se retira de las afirmaciones que esta auditoría verifica, conservándola únicamente para la reversión por ganancia de función mientras no se identifique la fuente que la sostiene.
