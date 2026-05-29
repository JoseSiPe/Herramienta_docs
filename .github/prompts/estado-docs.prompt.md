---
mode: agent
tools: [read_file, list_directory]
description: Muestra el estado actual de las carpetas de Archon sin ejecutar ningún proceso
---

Revisa el estado actual de la instalación de Archon en la raíz de este workspace y presenta un reporte con el siguiente formato:

```
ESTADO DE HERRAMIENTA_DOCS
===========================

ENTRADAS (entradas/)
  Documentos pendientes de procesar:
  - [lista de archivos o "Ninguno"]

SALIDAS (salidas/)
  Fichas generadas:
  - [lista de Ficha *.md]
  Provisionales conservados:
  - [lista de Provisional *.md]

EVALUACIÓN (evaluacion/)
  Documentos humanos disponibles:
  - [lista de archivos o "Ninguno"]
  Propuestas generadas (evaluacion/propuestas/):
  - [lista de Propuesta *.md o "Ninguno"]

CONTEXTOS CONFIGURADOS (mds/Contexto/)
  - [lista de contexto_*.md o "Ningún dominio configurado aún"]
```

No modifiques ni proceses ningún archivo. Solo lee y reporta.
