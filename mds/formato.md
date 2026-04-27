# formato.md
## Plantilla de Estructura para Fichas y Propuestas

---

## Estructura de Ficha [Temática]

```
# Ficha [Temática]

## Datos del documento fuente
- Título original:
- Tipo de documento: (PDF / PPT / WORD)
- Autor(es):
- Fecha:
- Fuente / origen:

## Resumen factual
[Síntesis de los elementos factuales centrales del documento. Sin interpretación.]

## Elementos prioritarios extraídos
[Elementos identificados como prioritarios según contexto_[dominio].md.
Usar subsecciones si el contexto define categorías específicas.]

## Términos clave identificados
[Lista de términos clave presentes en el documento, según los definidos en contexto_[dominio].md]

## Datos relevantes adicionales
[Cualquier elemento factual del documento no cubierto en las secciones anteriores
pero considerado significativo para el dominio.]

## Elementos excluidos
[Elementos presentes en el documento que fueron excluidos según los criterios
de restricción definidos en contexto_[dominio].md. Listar brevemente.]
```

---

## Estructura de Propuesta [Temática]

```
# Propuesta [Temática]

## Documentos de referencia
- Ficha base: Ficha [Temática].md
- Documento humano evaluado: [nombre del documento]

## Elementos para complementar
[Información presente en el documento humano no recogida en la ficha base,
que agrega valor factual según el contexto del dominio.]

## Elementos para modificar
[Información de la ficha base que el documento humano contradice, precisa
o actualiza. Incluir la versión actual y la versión propuesta.]

## Elementos coherentes
[Elementos donde el documento humano y la ficha base coinciden.
Sirve como validación del proceso de generación automática.]

## Observaciones del proceso
[Notas sobre la vinculación: si fue por título exacto o por contenido,
y cualquier ambigüedad detectada durante la evaluación.]
```

---

## Ubicación de archivos de salida

- Fichas finales → `salidas/fichas/Ficha [Temática].md`
- Provisionales → `salidas/provisionales/Provisional X.0 — [Temática].md`
- Propuestas finales → `evaluacion/propuestas/Propuesta [Temática].md`
- Provisionales de propuestas → `evaluacion/propuestas/Provisional X.0 — Propuesta [Temática].md`

---

## Estructura de Provisional X.0

Los provisionales siguen la misma estructura que la ficha o propuesta final
a la que corresponden, con el siguiente encabezado adicional:

```
# Provisional X.0 — [Temática]
## Estado: borrador de iteración [X] de 3

[misma estructura que Ficha o Propuesta según corresponda]
```

---

## Reglas de formato

- Todos los campos deben completarse; si no hay información disponible escribir: `[No disponible en el documento fuente]`
- No agregar secciones no contempladas en esta plantilla sin instrucción explícita
- El título `[Temática]` debe ser idéntico en el Provisional 1.0, Provisional 2.0 y el documento final
- Usar español en todos los documentos generados salvo que el contexto_[dominio].md indique otro idioma
