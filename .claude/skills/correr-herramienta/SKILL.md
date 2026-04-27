---
description: Ejecuta la rutina completa de Herramienta_Docs. Uso: /correr-herramienta
allowed-tools: Read, Write, Glob
---

Lee el archivo `Orquestador.md` en el directorio de trabajo actual y ejecuta la rutina completa definida en él.

Sigue estrictamente el orden de pasos del Orquestador:
1. PASO 1 — Verifica el contexto de dominio (única interacción con el usuario)
2. PASO 2 — Carga los archivos de `mds/`
3. PASO 3 — Procesa todos los documentos de `entradas/`
4. PASO 4 — Ejecuta la evaluación si `evaluacion/` tiene documentos
5. PASO 5 — Presenta el reporte final

Si no existe `Orquestador.md` en el directorio actual, informa al usuario que Claude Code debe iniciarse desde dentro de la carpeta Herramienta_Docs.
