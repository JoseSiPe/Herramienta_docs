---
description: Ejecuta la rutina completa de Herramienta_Docs en la ruta indicada. Uso: /correr-herramienta [ruta]
arguments: ruta
allowed-tools: Read, Write, Glob
---

Lee el archivo `$0/Orquestador.md` y ejecuta la rutina completa definida en él.

Sigue estrictamente el orden de pasos del Orquestador:
1. PASO 1 — Verifica el contexto de dominio (única interacción con el usuario)
2. PASO 2 — Carga los archivos de `$0/mds/`
3. PASO 3 — Procesa todos los documentos de `$0/entradas/`
4. PASO 4 — Ejecuta la evaluación si `$0/evaluacion/` tiene documentos
5. PASO 5 — Presenta el reporte final

Si no existe `$0/Orquestador.md`, informa al usuario que la ruta no corresponde a una instalación válida de Herramienta_Docs.
