# Archon — Sistema de Revisión Sistemática

Este workspace implementa Archon, un sistema de revisión sistemática y generación automatizada de fichas documentales.

## Estructura del proyecto

- `Orquestador.md` — lógica principal del sistema (5 pasos secuenciales)
- `mds/` — archivos operativos: instrucciones, formato y contextos de dominio
- `entradas/` — documentos fuente a procesar (PDF, DOCX, PPT)
- `evaluacion/` — documentos humanos para evaluar contra fichas generadas
- `salidas/` — fichas, provisionales y documentos de salida
- `scripts/` — utilidades Python para conversión de formatos

## Comandos disponibles

Usa los siguientes prompts desde Copilot Chat (escribe `#` y selecciona el archivo):

| Prompt | Acción |
|---|---|
| `correr-herramienta.prompt.md` | Ejecuta la rutina completa de Archon |
| `estado-docs.prompt.md` | Muestra el estado de las carpetas sin procesar nada |
| `nuevo-dominio.prompt.md` | Crea un nuevo contexto de dominio |
| `reset-herramienta.prompt.md` | Elimina todos los documentos generados |

## Reglas generales

- Las únicas rutas válidas para guardar archivos generados son: `salidas/fichas/`, `salidas/provisionales/`, `salidas/docx/`, `evaluacion/propuestas/` y `mds/Contexto/`
- Nunca guardes archivos directamente en `salidas/` ni en `mds/`
- Toda información generada debe ser rastreable al documento fuente — sin inferencias ni datos externos
