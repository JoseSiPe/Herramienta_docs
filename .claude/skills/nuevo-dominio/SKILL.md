---
description: Fuerza la creación de un nuevo contexto de dominio en Herramienta_Docs, omitiendo cualquier contexto previo. Uso: /nuevo-dominio [ruta]
arguments: ruta
allowed-tools: Read, Write
---

Ejecuta únicamente el PASO 1 del Orquestador ubicado en `$0/Orquestador.md`, pero con la siguiente modificación:

**Omite la verificación de contexto existente.** Aunque exista un archivo `contexto_[dominio].md` en `$0/mds/`, ignóralo y ejecuta directamente el onboarding (PASO 1.3) para generar un contexto nuevo.

Pasos:
1. Pregunta al usuario el dominio temático
2. Ejecuta las 5 preguntas de onboarding una a la vez
3. Genera y guarda el nuevo `$0/mds/contexto_[dominio].md` usando la plantilla del PASO 1.4
4. Confirma al usuario que el contexto fue creado y está listo para usar con `/correr-herramienta`

No ejecutes las fases de procesamiento ni evaluación.
