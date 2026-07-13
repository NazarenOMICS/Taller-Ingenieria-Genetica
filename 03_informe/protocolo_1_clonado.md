# Protocolo 1 - Clonado de secuencia diana (Target Sequence Cloning)

## Índice operativo

Fuente: `_fuentes_pdf/Protocolo 1.pdf` (protocolo de Zhang lab, en inglés). Uso en el taller: lunes semana 1 (annealing, fosforilación y ligación de oligos en el vector pX459 digerido con BbsI).
Aplica a: modalidad **Informe**.

Qué contiene: diseño de oligos para plásmidos tipo pX330/pX458–462 y pX260/pX334, y el procedimiento de annealing y clonado (digestión, purificación, fosforilación/annealing, ligación, tratamiento opcional con exonucleasa, transformación).

Modificación del taller (según Cartilla): la ligación se realiza con 0,5 µl de ligasa (el protocolo original estipula 1,0 µl).

---

## Diseño de oligos

Oligos de secuencia diana estándar desalados son suficientes.

**Plásmidos basados en pX330, incluidos pX458–462 (SpCas9 o nickasa SpCas9n D10A + single guide RNA).** Para clonar la secuencia guía en el andamiaje del sgRNA, sintetizar dos oligos de la forma:

```
5' – CACCGNNNNNNNNNNNNNNNNNNN     – 3'
3' –     CNNNNNNNNNNNNNNNNNNNCAAA – 5'
```

**Plásmidos pX260 y pX334 (SpCas9 o nickasa SpCas9n D10A + CRISPR array + tracrRNA).** Para clonar la secuencia guía en el andamiaje del sgRNA, sintetizar dos oligos de la forma:

```
5' – AAACNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNGT     – 3'
3' –     NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNCAAAAT – 5'
```

## Annealing de oligos y clonado en vectores backbone

**1. Digerir 1 µg de plásmido con BbsI durante 30 min a 37 °C:**

| Componente | Cantidad |
|---|---|
| Plásmido | 1 µg |
| FastDigest BbsI (Fermentas) | 1 µl |
| FastAP (Fermentas) | 1 µl |
| 10X FastDigest Buffer | 2 µl |
| ddH₂O | X µl |
| **Total** | **20 µl** |

**2.** Purificar el plásmido digerido en gel usando QIAquick Gel Extraction Kit y eluir en EB.

**3. Fosforilar y hibridar cada par de oligos:**

| Componente | Cantidad |
|---|---|
| Oligo 1 (100 µM) | 1 µl |
| Oligo 2 (100 µM) | 1 µl |
| 10X T4 Ligation Buffer (NEB) | 1 µl |
| ddH₂O | 6,5 µl |
| T4 PNK (NEB) | 0,5 µl |
| **Total** | **10 µl** |

Hibridar en termociclador con los siguientes parámetros: 37 °C durante 30 min; 95 °C durante 5 min y luego rampa de descenso hasta 25 °C a 5 °C/min.

**4. Preparar la reacción de ligación e incubar a temperatura ambiente durante 10 min:**

| Componente | Cantidad |
|---|---|
| Plásmido digerido con BbsI del paso 2 (50 ng) | X µl |
| Dúplex de oligos fosforilado e hibridado del paso 3 (dilución 1:200) | 1 µl |
| 2X Quickligation Buffer (NEB) | 5 µl |
| ddH₂O | X µl |
| Subtotal | 10 µl |
| Quick Ligase (NEB) | 1 µl |
| **Total** | **11 µl** |

> Modificación del taller: usar 0,5 µl de ligasa en lugar de 1,0 µl (Cartilla, lunes semana 1).

**5. (Opcional)** Tratar la reacción de ligación con exonucleasa PlasmidSafe para prevenir productos de recombinación no deseados:

| Componente | Cantidad |
|---|---|
| Reacción de ligación del paso 4 | 11 µl |
| 10X PlasmidSafe Buffer | 1,5 µl |
| ATP 10 mM | 1,5 µl |
| ddH₂O | 1 µl |
| **Total** | **15 µl** |

Incubar la reacción a 37 °C durante 30 min.

**6. Transformación.**
