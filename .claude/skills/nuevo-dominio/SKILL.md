---
description: Fuerza la creación de un nuevo contexto de dominio en Herramienta_Docs, omitiendo cualquier contexto previo. Uso: /nuevo-dominio
allowed-tools: Read, Write
---

Ejecuta únicamente el PASO 1 del Orquestador ubicado en `Orquestador.md` en el directorio de trabajo actual, pero con la siguiente modificación:

**Omite la verificación de contexto existente.** Aunque exista un archivo `contexto_[dominio].md` en `mds/`, ignóralo y ejecuta directamente el onboarding (PASO 1.3) para generar un contexto nuevo.

Pasos:
1. Pregunta al usuario el dominio temático
2. Ejecuta las 5 preguntas de onboarding una a la vez
3. Genera y guarda el nuevo `mds/contexto_[dominio].md` usando la plantilla del PASO 1.4
4. Confirma al usuario que el contexto fue creado y está listo para usar con `/correr-herramienta`

No ejecutes las fases de procesamiento ni evaluación.
