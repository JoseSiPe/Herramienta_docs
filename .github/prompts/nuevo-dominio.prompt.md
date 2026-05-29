---
mode: agent
tools: [read_file, create_file]
description: Fuerza la creación de un nuevo contexto de dominio en Archon, omitiendo cualquier contexto previo
---

Ejecuta únicamente el PASO 1 del Orquestador ubicado en `Orquestador.md` en la raíz de este workspace, pero con la siguiente modificación:

**Omite la verificación de contexto existente.** Aunque exista un archivo `contexto_[dominio].md` en `mds/Contexto/`, ignóralo y ejecuta directamente el onboarding (PASO 1.3) para generar un contexto nuevo.

Pasos:
1. Pregunta al usuario el dominio temático
2. Ejecuta las 5 preguntas de onboarding una a la vez
3. Genera y guarda el nuevo `mds/Contexto/contexto_[dominio].md` usando la plantilla del PASO 1.3
4. Confirma al usuario que el contexto fue creado y está listo para usar con `correr-herramienta.prompt.md`

No ejecutes las fases de procesamiento ni evaluación.
