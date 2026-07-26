# Región inter-TSS FTO–RPGRIP1L: mapa regulatorio operativo

## Intervalo de trabajo

- Ensamblado: GRCh38
- RPGRIP1L MANE TSS: chr16:53,703,859, hebra negativa
- FTO MANE TSS: chr16:53,704,156, hebra positiva
- Diferencia entre coordenadas: 297 bp
- Intervalo inclusivo usado para inspección: chr16:53,703,859-53,704,156, longitud 298 bp
- Región estrictamente situada entre ambos nucleótidos TSS: chr16:53,703,860-53,704,155, longitud 296 bp

## Lectura principal

Todo el intervalo está contenido dentro del promotor Ensembl ENSR16_9RBJC, asignado conjuntamente a RPGRIP1L y FTO. También está contenido dentro del elemento GeneHancer Elite GH16J053703, clasificado como Promoter/Enhancer a partir de evidencia integrada de ENCODE, EPDnew y Ensembl. Fanta agrupa la zona como FCHS_156247 y la asigna simultáneamente a cp2@FTO y cp1@RPGRIP1L, con picos CAGE divergentes para ambos genes y un cCRE ENCODE tipo PLS.

La mitad próxima a FTO contiene sitios funcionales publicados para C/EBPα, FOXA2 y SP1. Estos sitios no son simples predicciones: poseen distintos grados de validación por mutagénesis de reportero, EMSA o ChIP. Su posición GRCh38 fue inferida usando como referencia el TSS MANE de FTO y la nomenclatura relativa publicada. Antes de sintetizar guías debe verificarse cada secuencia contra el FASTA GRCh38.

## Consecuencia para las guías dCas9-p300

La zona no es un promotor exclusivo de FTO. Es un bloque promotor divergente. Una guía en el centro puede modificar ambas direcciones. Para buscar selectividad hacia FTO, el panel inicial debería enriquecerse en el lado FTO del intervalo, especialmente alrededor de −200 a −60, y evitar colocar todas las guías sobre los sitios funcionales −54/−45, −26/−14 y −8/−1 sin una justificación explícita.

La validación obligatoria debe medir simultáneamente FTO y RPGRIP1L. Una guía que aumente ambos genes no es necesariamente un off-target de secuencia; puede ser el resultado esperado de acetilar un promotor bidireccional.

## Advertencias

- Las coordenadas FANTOM5 mostradas en la tabla están en hg19.
- Las coordenadas de motivos publicadas son inferencias relativas al TSS MANE actual.
- El cCRE EH38E3181169 y los silencers están identificados con certeza por ID, pero sus coordenadas exactas deben descargarse de sus bases originales antes de un mapa final de nucleótido.
- Ninguna de estas anotaciones demuestra actividad en KGN o granulosa primaria.
