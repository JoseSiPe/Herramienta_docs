---
mode: agent
tools: [read_file, create_file, list_directory, run_in_terminal, web_search, fetch, grep_search]
description: Ejecuta la rutina completa de Archon
---

Lee el archivo `Orquestador.md` en la raíz de este workspace y ejecuta la rutina completa definida en él.

Sigue estrictamente el orden de pasos del Orquestador:
1. PASO 1 — Configura el contexto de dominio (interacción con el usuario)
2. PASO 2 — Carga los archivos de `mds/`
3. PASO 3 — Procesa todos los documentos de `entradas/`
   - Si `entradas/` está vacía → PASO 3.1: búsqueda web supervisada (requiere autorización del usuario por cada descarga)
4. PASO 4 — Ejecuta la evaluación si `evaluacion/` tiene documentos
5. PASO 5 — Presenta el reporte final

Si no existe `Orquestador.md` en la raíz del workspace, informa al usuario que debe abrir VS Code desde dentro de la carpeta Archon.
