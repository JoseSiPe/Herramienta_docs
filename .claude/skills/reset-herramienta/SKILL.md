---
description: Elimina todos los documentos generados por el uso de Archon, dejando solo los archivos fundacionales. Uso: /reset-herramienta
allowed-tools: Glob, Bash, Read
---

Ejecuta un reseteo completo de Archon eliminando todos los documentos generados durante el uso de la herramienta.

## Paso 1 — Inventario

Antes de borrar nada, lista todos los archivos que serán eliminados agrupados por carpeta:

- `entradas/` — todos los archivos excepto `.gitkeep`
- `salidas/fichas/` — todos los archivos excepto `.gitkeep`
- `salidas/provisionales/` — todos los archivos excepto `.gitkeep`
- `salidas/docx/` — todos los archivos excepto `.gitkeep`
- `evaluacion/` — archivos PDF, PPT, PPTX, DOC, DOCX en la raíz de la carpeta
- `evaluacion/propuestas/` — todos los archivos excepto `.gitkeep`
- `mds/Contexto/` — todos los archivos excepto `.gitkeep`

Presenta el inventario al usuario con este formato:

```
ARCHIVOS QUE SERÁN ELIMINADOS
==============================

entradas/
  - [lista o "Ninguno"]

salidas/fichas/
  - [lista o "Ninguno"]

salidas/provisionales/
  - [lista o "Ninguno"]

salidas/docx/
  - [lista o "Ninguno"]

evaluacion/ (documentos fuente)
  - [lista o "Ninguno"]

evaluacion/propuestas/
  - [lista o "Ninguno"]

mds/Contexto/ (contextos de dominio)
  - [lista o "Ninguno"]

Total: [N] archivo(s)
```

Si no hay ningún archivo que eliminar, informa al usuario y termina sin hacer nada.

## Paso 2 — Confirmación

Pregunta al usuario:

> "¿Confirmas el reseteo? Esta acción no se puede deshacer. (sí / no)"

- **no** → Cancela e informa que no se eliminó nada.
- **sí** → Continúa al Paso 3.

## Paso 3 — Eliminación

Elimina mediante Bash todos los archivos listados en el inventario, preservando en cada carpeta:
- Los archivos `.gitkeep`
- La estructura de subcarpetas

Usa comandos seguros que no afecten archivos fuera de las carpetas listadas.

## Paso 4 — Confirmación final

Presenta al usuario un resumen de lo eliminado:

```
RESETEO COMPLETADO
==================
Archivos eliminados: [N]

La herramienta está lista para una nueva sesión.
```
