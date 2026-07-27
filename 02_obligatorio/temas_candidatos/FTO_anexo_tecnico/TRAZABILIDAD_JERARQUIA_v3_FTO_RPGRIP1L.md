# Trazabilidad de jerarquía v3

## Cambios aplicados

1. Se eliminaron todas las ventanas operativas y cualquier referencia a W1-W4.
2. El archivo permanece completamente previo al diseño.
3. Se conservaron únicamente:
   - dos transcritos de referencia;
   - dos TSS de referencia;
   - estructura proximal de FTO-206;
   - tres elementos regulatorios de Ensembl;
   - el pELS de ENCODE.
4. No hay guías, PAM, protoespaciadores, oligos, variantes ni puntajes.

## Jerarquía semántica

### Capa estructural

Se representa con tipos GenBank estructurales:

- `mRNA`: FTO-206 y RPGRIP1L-212;
- `exon`: exón 1 de FTO-206;
- `5'UTR`: 5′ UTR de FTO-206;
- `intron`: intrón 1 de FTO-206;
- `misc_feature`: TSS de referencia.

Las features estructurales usan una familia visual azul o gris.

### Capa regulatoria

Se representa exclusivamente con el tipo GenBank `regulatory`:

- enhancer proximal del lado de RPGRIP1L;
- promotor divergente compartido;
- enhancer proximal del lado de FTO;
- pELS intrónico de ENCODE.

Las features regulatorias usan colores diferenciados:

- naranja para el promotor;
- verde para enhancers de Ensembl;
- violeta para el pELS de ENCODE.

## Limitación de Benchling

El formato GenBank permite codificar tipo de feature, nombre, notas, procedencia y
colores, pero no controla de forma absoluta la altura o pista vertical en la que
Benchling dibuja cada anotación. Benchling calcula la disposición final según
los solapamientos. La jerarquía se expresa mediante tipos GenBank correctos,
nombres, colores y notas, no mediante una coordenada vertical fija.

Si se requiere una separación visual absoluta entre estructura y regulación,
debe hacerse dentro de Benchling mediante grupos o pistas de anotación de la
interfaz, porque esa jerarquía no forma parte del estándar GenBank.
