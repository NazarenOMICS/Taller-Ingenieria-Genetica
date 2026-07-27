# -*- coding: utf-8 -*-
"""Figuras 2 y 3 del Obligatorio, generadas desde coordenadas_locus_fto.csv.
GRCh38.p14, coordenadas 1-based inclusivas. Ejecutar desde esta carpeta."""
import csv, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

X0, X1 = 53703300, 53704900
W = 11.0
GRIS, TINTA, ACENTO, CREMA, ARENA = "#8c8c8c", "#1a1a1a", "#b8562f", "#efece6", "#d6c7b0"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5,
                     "axes.linewidth": 0.7, "svg.fonttype": "none"})

D = {}
with open("coordenadas_locus_fto.csv", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        D.setdefault(r["categoria"], []).append(r)
def uno(cat, val): return [r for r in D[cat] if r["etiqueta_corta"] == val][0]
def ini(r): return int(r["inicio_1based"])
def fin(r): return int(r["fin_1based"])

TICKS = list(range(53703400, X1, 200))
def eje(ax, etiquetas=True):
    ax.set_xlim(X0, X1); ax.set_xticks(TICKS)
    ax.set_xticklabels([f"{v:,}".replace(",", ".") for v in TICKS] if etiquetas else [], fontsize=7)
    if etiquetas: ax.set_xlabel("Posición en el cromosoma 16 (GRCh38.p14)", fontsize=8.5, labelpad=3)
    ax.tick_params(axis="x", length=2.5, width=0.6)
    for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
    ax.set_yticks([])

def caja(ax, a, b, y, h, fc, ec=TINTA, hatch=None, ls="-", txt=None, fs=6.8):
    a, b = max(a, X0), min(b, X1)
    ax.add_patch(Rectangle((a, y), b - a, h, facecolor=fc, edgecolor=ec,
                           lw=0.7, hatch=hatch, linestyle=ls, zorder=3))
    if txt: ax.text((a + b)/2, y + h/2, txt, ha="center", va="center", fontsize=fs, zorder=4)

TSSR = [uno("tss", "TSS ref RPGRIP1L"), uno("tss", "TSS ref FTO")]
TSSA = [uno("tss", "Inicio alt RPGRIP1L"), uno("tss", "Inicio alt FTO")]

def lineas_tss(ax, y0, y1, alpha=0.6):
    for r in TSSR:
        ax.vlines(ini(r), y0, y1, color=ACENTO, lw=1.2, zorder=2, alpha=alpha)
    for r in TSSA:
        ax.vlines(ini(r), y0, y1, color=GRIS, lw=0.9, ls=(0, (3, 2)), zorder=2, alpha=alpha)

# ================================================================ FIGURA 2
fig, (axA, axB) = plt.subplots(2, 1, figsize=(W, 5.9), height_ratios=[1.3, 1.0])
fig.subplots_adjust(hspace=0.34, left=0.150, right=0.98, top=0.90, bottom=0.12)

# ---- Panel A
axA.set_ylim(-0.30, 3.05)
rp, ft, ex = uno("transcrito", "RPGRIP1L-212"), uno("transcrito", "FTO-206"), D["exon"][0]
yR, yF, h = 1.72, 0.42, 0.22
caja(axA, X0, fin(rp), yR, h, CREMA)
axA.annotate("", xy=(X0 - 30, yR + h/2), xytext=(X0, yR + h/2),
             arrowprops=dict(arrowstyle="-|>", color=TINTA, lw=1.2), annotation_clip=False)
axA.text(fin(rp) - 30, yR + h + 0.10, "RPGRIP1L-212   hebra −, continúa a la izquierda",
         fontsize=8, style="italic", ha="right")
caja(axA, ini(ft), X1, yF, h, CREMA)
caja(axA, ini(ex), fin(ex), yF, h, ARENA)
axA.annotate("", xy=(X1 + 30, yF + h/2), xytext=(X1, yF + h/2),
             arrowprops=dict(arrowstyle="-|>", color=TINTA, lw=1.2), annotation_clip=False)
axA.text(X1 - 40, yF - 0.24, "FTO-206   hebra +, continúa a la derecha",
         fontsize=8, style="italic", ha="right")
axA.annotate("exón 1", xy=((ini(ex)+fin(ex))/2, yF), xytext=((ini(ex)+fin(ex))/2, yF - 0.42),
             fontsize=7, ha="center", arrowprops=dict(arrowstyle="-", color=TINTA, lw=0.6))
lineas_tss(axA, 0.20, 2.55, alpha=0.85)
for r in TSSR + TSSA:
    ax_c = ACENTO if r in TSSR else GRIS
    axA.plot([ini(r)], [2.55], marker="v", ms=4.5 if r in TSSR else 3.5, color=ax_c, zorder=6)
axA.annotate("TSS de referencia\nde RPGRIP1L", xy=(ini(TSSR[0]), 2.55), xytext=(53703430, 2.72),
             fontsize=7, ha="left", va="bottom", linespacing=1.15,
             arrowprops=dict(arrowstyle="-", color=GRIS, lw=0.6))
axA.annotate("TSS de referencia\nde FTO", xy=(ini(TSSR[1]), 2.55), xytext=(53704320, 2.72),
             fontsize=7, ha="left", va="bottom", linespacing=1.15,
             arrowprops=dict(arrowstyle="-", color=GRIS, lw=0.6))
axA.annotate("inicios alternativos\nde RPGRIP1L y de FTO", xy=(53703950, 2.55), xytext=(53703950, 2.72),
             fontsize=7, ha="center", va="bottom", color=GRIS, linespacing=1.15,
             arrowprops=dict(arrowstyle="-", color=GRIS, lw=0.6))
def acotar(ax, x1, x2, y, txt, dy=0.07, fs=7.5):
    ax.annotate("", xy=(x1, y), xytext=(x2, y),
                arrowprops=dict(arrowstyle="<|-|>", color=TINTA, lw=0.8, shrinkA=0, shrinkB=0))
    ax.text((x1 + x2)/2, y + dy, txt, ha="center", fontsize=fs)
acotar(axA, ini(TSSR[0]), ini(TSSR[1]), 1.25, "297 pb")
axA.annotate("", xy=(ini(TSSA[0]), 0.95), xytext=(ini(TSSA[1]), 0.95),
             arrowprops=dict(arrowstyle="<|-|>", color=TINTA, lw=0.8, shrinkA=0, shrinkB=0))
axA.annotate("25 pb", xy=(53703950, 0.95), xytext=(53703950, 0.66), fontsize=7.5, ha="center",
             arrowprops=dict(arrowstyle="-", color=TINTA, lw=0.5))
eje(axA, etiquetas=False)
axA.text(-0.140, 1.02, "A", transform=axA.transAxes, fontsize=11, fontweight="bold")

# ---- Panel B
axB.set_ylim(-0.10, 3.10)
FIL = {"Ensembl\nRegulatory Build": 2.28, "ENCODE\ncCRE": 1.36, "GeneHancer": 0.44}
for r in D["ensembl_rb"]:
    prom = r["clasificacion_ensembl"].startswith("promotor")
    caja(axB, ini(r), fin(r), FIL["Ensembl\nRegulatory Build"], 0.44,
         ACENTO if prom else CREMA, txt=r["etiqueta_corta"])
for r in D["encode_ccre"]:
    caja(axB, ini(r), fin(r), FIL["ENCODE\ncCRE"], 0.44,
         ARENA if r["clasificacion_encode"].startswith("PLS") else CREMA,
         txt=r["clasificacion_encode"].split(" ")[0] + "  " + r["etiqueta_corta"], fs=6.2)
caja(axB, X0, X1, FIL["GeneHancer"], 0.44, "#f6f4f0",
     txt="GH16J053703   se extiende fuera del intervalo graficado", fs=6.5)
for xx, sg in ((X0, -1), (X1, 1)):
    axB.annotate("", xy=(xx + sg*16, FIL["GeneHancer"] + 0.22), xytext=(xx, FIL["GeneHancer"] + 0.22),
                 arrowprops=dict(arrowstyle="-|>", color=TINTA, lw=1.1), annotation_clip=False)
for nom, y in FIL.items():
    axB.text(-0.022, (y + 0.22 + 0.10)/3.20, nom, transform=axB.transAxes,
             fontsize=7.2, ha="right", va="center", linespacing=1.2)
lineas_tss(axB, 0.10, 2.90, alpha=0.45)
eje(axB, etiquetas=True)
axB.text(-0.140, 1.04, "B", transform=axB.transAxes, fontsize=11, fontweight="bold")
for e in ("svg", "pdf"): fig.savefig(f"figura2_locus_fto_rpgrip1l.{e}")
fig.savefig("figura2_locus_fto_rpgrip1l.png", dpi=300)
plt.close(fig)

# ================================================================ FIGURA 3
REG = D["region"]
CTX = {"Centro promotor divergente": "promotor compartido",
       "Promotora proxima": "promotor compartido y 5′ UTR de isoformas alternativas",
       "Codificante exon 1": "exón 1 codificante del transcrito de referencia",
       "Intronica pELS": "intrón 1"}
NOM = {"Centro promotor divergente": "Centro del promotor divergente FTO–RPGRIP1L",
       "Promotora proxima": "Región promotora próxima al TSS de referencia de FTO",
       "Codificante exon 1": "Región codificante del exón 1 del transcrito de referencia de FTO",
       "Intronica pELS": "Región intrónica con firma pELS"}
fig = plt.figure(figsize=(W, 4.6))
ax = fig.add_axes([0.150, 0.56, 0.830, 0.36])
ax.set_ylim(-0.05, 2.30)
for i, r in enumerate(REG, start=1):
    ret = r["estado"] == "retirada"
    caja(ax, ini(r), fin(r), 0.75, 0.55, "#ffffff" if ret else ARENA,
         hatch="/////" if ret else None, ls=(0, (2.5, 1.8)) if ret else "-",
         txt=str(i), fs=9)
    ax.text((ini(r)+fin(r))/2, 0.55, "retirada" if ret else "conservada", ha="center",
            va="top", fontsize=6.5, style="italic", color=TINTA if ret else GRIS,
            bbox=dict(facecolor="white", edgecolor="none", pad=1.2), zorder=7)
lineas_tss(ax, 0.15, 1.75, alpha=0.8)
for r in TSSR + TSSA:
    ax.plot([ini(r)], [1.75], marker="v", ms=4.5 if r in TSSR else 3.5,
            color=ACENTO if r in TSSR else GRIS, zorder=6)
ax.annotate("TSS ref. RPGRIP1L", xy=(ini(TSSR[0]), 1.75), xytext=(53703430, 1.92),
            fontsize=7, ha="left", arrowprops=dict(arrowstyle="-", color=GRIS, lw=0.6))
ax.annotate("TSS ref. FTO", xy=(ini(TSSR[1]), 1.75), xytext=(53704320, 1.92),
            fontsize=7, ha="left", arrowprops=dict(arrowstyle="-", color=GRIS, lw=0.6))
ax.annotate("inicios alternativos", xy=(53703950, 1.75), xytext=(53703950, 1.92),
            fontsize=7, ha="center", color=GRIS,
            arrowprops=dict(arrowstyle="-", color=GRIS, lw=0.6))
eje(ax, etiquetas=True)
y = 0.40
fig.text(0.150, y + 0.045, "Regiones evaluadas", fontsize=8, fontweight="bold")
for i, r in enumerate(REG, start=1):
    k = r["etiqueta_corta"]
    est = "retirada durante la selección" if r["estado"] == "retirada" else "conservada"
    fig.text(0.150, y - (i-1)*0.088, f"{i}.  {NOM[k]}  ({est})", fontsize=7.6)
    fig.text(0.170, y - (i-1)*0.088 - 0.040,
             f"contexto: {CTX[k]}   ·   Ensembl: {r['clasificacion_ensembl']}   ·   ENCODE: {r['clasificacion_encode']}",
             fontsize=6.8, color="#4a4a4a")
for e in ("svg", "pdf"): fig.savefig(f"figura3_regiones_blanco.{e}")
fig.savefig("figura3_regiones_blanco.png", dpi=300)
plt.close(fig)
print("figuras regeneradas")
