---
description: Muestra el estado actual de las carpetas de Herramienta_Docs sin ejecutar ningún proceso. Uso: /estado-docs [ruta]
arguments: ruta
allowed-tools: Glob, Read
---

Revisa el estado actual de la instalación de Herramienta_Docs en `$0` y presenta un reporte con el siguiente formato:

```
ESTADO DE HERRAMIENTA_DOCS
===========================

ENTRADAS ($0/entradas/)
  Documentos pendientes de procesar:
  - [lista de archivos o "Ninguno"]

SALIDAS ($0/salidas/)
  Fichas generadas:
  - [lista de Ficha *.md]
  Provisionales conservados:
  - [lista de Provisional *.md]

EVALUACIÓN ($0/evaluacion/)
  Documentos humanos disponibles:
  - [lista de archivos o "Ninguno"]
  Propuestas generadas ($0/evaluacion/propuestas/):
  - [lista de Propuesta *.md o "Ninguno"]

CONTEXTOS CONFIGURADOS ($0/mds/)
  - [lista de contexto_*.md o "Ningún dominio configurado aún"]
```

No modifiques ni proceses ningún archivo. Solo lee y reporta.
