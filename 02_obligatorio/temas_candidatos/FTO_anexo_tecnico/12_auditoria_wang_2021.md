# Auditoría textual de Wang y Yang (2021), citado en el proyecto como Wang et al., 2021a

Wang R, Yang X. *Overexpression of FTO Protects Human Granulosa Cells From Cisplatin-Induced Injury*. Universidad Jiaotong de Xi'an. DOI: 10.21203/rs.3.rs-929583/v1. Fecha de publicación: 5 de octubre de 2021.

**Estatus editorial, dato de primer orden.** El identificador `10.21203/rs.3.rs-929583/v1` corresponde a **Research Square**, es decir, se trata de un **preprint**. El documento no presenta indicios de revisión por pares. Este estatus debe declararse cada vez que se lo cite.

Auditoría realizada el 2026-07-26 sobre el PDF completo alojado en `Vault/Research/Papers/dcas9-fto-granulosa/q08-restauracion-fto-fenotipos/`. Alcance: resumen, antecedentes, resultados, discusión, conclusión y materiales y métodos.

---

## 1. Los siete puntos consultados

| # | Pregunta | Respuesta |
| :--- | :--- | :--- |
| 1 | ¿Demuestra aumento experimental de FTO? | **Sí** |
| 2 | ¿Usa células de granulosa humana? | **Sí**, línea KGN exclusivamente |
| 3 | ¿Demuestra rescate de un fenotipo provocado por cisplatino? | **Sí**, sobre proliferación y apoptosis |
| 4 | ¿Mide senescencia de forma directa? | **No**, en absoluto |
| 5 | ¿Participa el eje m6A–FOS? | **No.** *FOS* no aparece en el documento y no se mide m6A |
| 6 | ¿Demuestra protección celular, reducción de apoptosis o restauración funcional? | **Sí** |
| 7 | ¿Se corresponde con nuestro modelo de envejecimiento? | **No.** Es toxicidad por quimioterapia, no envejecimiento |

---

## 2. Afirmaciones, una por una

### A1. La sobreexpresión de FTO restaura la proliferación y disminuye la apoptosis en células de granulosa lesionadas por cisplatino

**Pasaje literal**: "Overexpression of FTO could restore the injured cells' proliferation and decrease its apoptosis through regulating the expression of BNIP3. Down-regulation of FTO got the opposite results."

**Ubicación**: resumen, sección de resultados.

**Modelo celular**: KGN, línea de granulosa humana. No se emplean COV434 ni granulosa primaria; la búsqueda de ambos términos no devuelve coincidencias.

**Tratamiento**: cisplatino, para construir un modelo de lesión de células de la granulosa.

**Forma de aumentar FTO**: transfección **transitoria** del plásmido **pCAG-FTO** (Miaoling, Wuhan) con Lipofectamine 2000. No se emplearon lentivirus; la búsqueda de ese término no devuelve coincidencias.

**Controles experimentales**: vector vacío para el plásmido y control para los ARN de interferencia, ambos declarados en métodos. Brazo de pérdida de función con ARN de interferencia contra FTO y, adicionalmente, ácido meclofenámico como inhibidor selectivo de FTO.

**Variables medidas**: viabilidad por CCK-8, proliferación por EdU, apoptosis por citometría de flujo y anexina, expresión por qRT-PCR y por western blot.

**Resultado**: restauración de la proliferación y disminución de la apoptosis, con resultados opuestos al reducir FTO.

**Clasificación de la evidencia**: **causal y funcional**, con diseño de ganancia y pérdida de función y control de vector vacío.

**Limitación para extrapolar a envejecimiento ovárico**: el fenotipo rescatado es lesión aguda por agente citotóxico, no envejecimiento.

### A2. El mecanismo propuesto pasa por BNIP3

**Pasaje literal**: "the upregulation of FTO in granulosa cells could decrease cisplatin-induced apoptosis by inhibiting the expression of BNIP3".

**Ubicación**: conclusión, página 11 de 23.

**Recuento**: *BNIP3* aparece 29 veces en el documento; ***FOS* no aparece ninguna vez**.

**Clasificación**: causal dentro de ese modelo.

**Limitación**: el eje mecanístico es distinto del que sostiene nuestro proyecto. No hay puente experimental entre este trabajo y el eje FTO–m6A–FOS.

### A3. Las células madre derivadas de menstruación aumentan FTO y atenúan la apoptosis

**Pasaje literal**: "MenSCs could increase the expression of FTO to attenuate the cisplatin-induced granulosa cell apoptosis".

**Ubicación**: conclusión.

**Clasificación**: funcional, pero por **intervención indirecta**. El propio texto reconoce que no se identificó el factor responsable: "which factors secreted from the MenSCs promoted the FTO expression is still unknown".

### A4. Componente in vivo

**Pasaje literal**: "MenSCs transplantation could restore the expression of FTO in the ovary of POF mice."

**Modelo**: ratones hembra C57BL/6 de 6 a 8 semanas, con modelo de fallo ovárico prematuro inducido por cisplatino y trasplante de células madre por vena caudal. Aprobación del comité ético y del comité de cuidado animal de la Universidad Jiaotong de Xi'an.

**Clasificación**: funcional en ratón, y referida a la intervención con células madre, no a la sobreexpresión dirigida de FTO.

---

## 3. Lo que el trabajo no contiene

| Elemento buscado | Resultado de la búsqueda |
| :--- | :--- |
| senescence, senescent | ausente |
| SA-β-galactosidasa | ausente |
| p16 | ausente |
| γH2AX o H2AX | ausente |
| p21 | aparece una sola vez, y es el apellido de un autor dentro de la lista de referencias, no una medición |
| FOS | ausente |
| MeRIP, dot blot, cuantificación colorimétrica de m6A | ausentes |
| COV434, granulosa primaria | ausentes |
| lentivirus | ausente |

Sobre m6A: el término aparece 14 veces, pero corresponde a discusión conceptual y a la medición de **expresión de los componentes de la maquinaria m6A** por qRT-PCR, no a cuantificación de la modificación. El resumen lo formula como "examined the expression levels of m6A members".

**Verificación de la sobreexpresión**: el trabajo emplea qRT-PCR y western blot como técnicas generales, pero la lectura del texto disponible no permite afirmar con certeza que la eficacia de la transfección con pCAG-FTO haya sido confirmada simultáneamente a nivel de ARNm y de proteína en una figura dedicada. Este punto queda como **no verificable con el material disponible** y requeriría revisar las figuras originales.

---

## 4. Clasificación final

**Categoría B.** Evidencia directa de que aumentar FTO protege granulosa humana frente a cisplatino, pero sin demostrar reversión de senescencia.

**Formulación admisible, de uso obligatorio al citarlo:**

"En células de la granulosa humana sometidas a daño por cisplatino, el aumento de FTO produjo un efecto protector o de rescate sobre los desenlaces medidos. Este antecedente respalda la viabilidad de la ganancia de función de FTO en granulosa, pero no demuestra reversión del envejecimiento ni de la senescencia asociada a la edad."

**Cuatro calificaciones que deben acompañar siempre a esa formulación:**

1. Se trata de un preprint sin evidencia de revisión por pares.
2. Los desenlaces medidos son viabilidad, proliferación y apoptosis; no se midió senescencia con ningún marcador.
3. El mecanismo propuesto es BNIP3 y no el eje m6A–FOS, y no se cuantificó m6A.
4. El modelo es lesión aguda por cisplatino en la línea KGN con transfección transitoria, no envejecimiento ni senescencia inducida por estrés oxidativo.

---

## 5. Qué aporta y qué no aporta al proyecto

**Aporta.** Un antecedente de que la maniobra de aumentar FTO en granulosa humana es técnicamente realizable y produce un efecto biológico medible y direccionalmente favorable, con control de vector vacío y con brazo recíproco de pérdida de función. Eso sostiene la **viabilidad de la ganancia de función**, que era exactamente el eslabón que la auditoría de Jiang dejó sin respaldo.

**No aporta.** No cierra la afirmación de que aumentar FTO atenúe el fenotipo senescente. Esa dirección sigue sin demostrarse en granulosa, y por lo tanto se mantiene como lo que el proyecto se propone evaluar.

**No se traslada.** La protección frente a cisplatino no se traslada a reversión del envejecimiento. Son fenotipos, mecanismos y modelos distintos.

---

## 6. Estado tras esta auditoría, para decisión

No se modificó la hipótesis, ni el objetivo, ni el nivel de evidencia declarado en el esqueleto. La incorporación de esta fuente al apartado de evidencia, si se aprueba, correspondería a una categoría propia de **viabilidad de la ganancia de función en granulosa**, distinta tanto de la evidencia sólida en modelos celulares para la dirección de pérdida de función como de la evidencia limitada de ganancia de función que aporta la figura suplementaria S3 de Jiang et al. (2021).
