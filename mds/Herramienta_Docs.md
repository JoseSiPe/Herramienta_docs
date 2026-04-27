# Herramienta_Docs.md
## Núcleo Operativo — Sistema de Revisión Sistemática

---

## Propósito

Este archivo describe el comportamiento operativo del agente durante la ejecución de cada fase. Es cargado por el `Orquestador.md` en el PASO 2 y aplica durante toda la sesión.

---

## Principios operativos

1. **Fidelidad factual absoluta** — Toda información generada debe ser rastreable a un elemento explícito del documento fuente. No se admiten inferencias, interpretaciones ni datos externos.

2. **Trazabilidad del proceso** — Cada ciclo iterativo produce un documento provisional que se conserva. El historial de revisión no se elimina.

3. **Autonomía tras configuración** — Una vez completado el PASO 1 del Orquestador, el agente opera sin solicitar input al usuario salvo en estas excepciones: (a) `entradas/` vacía — pregunta si buscar fuentes en internet y solicita autorización por cada descarga (PASO 3.1), (b) situaciones de error no resueltas (documento no vinculable, archivo faltante).

4. **Jerarquía de fuentes** — En caso de conflicto entre instrucciones, el orden de precedencia es:
   `Orquestador.md` > `Herramienta_Docs.md` > `instrucciones.md` > `contexto_[dominio].md` > `formato.md`

---

## Comportamiento por fase

### Fase 1 — Procesamiento de entradas

- Procesa los documentos de `entradas/` en orden alfabético
- Extrae únicamente los elementos factuales identificados en `contexto_[dominio].md` como prioritarios
- Aplica la estructura de `formato.md` desde el primer ciclo
- No omite ningún documento sin informar al usuario

### Fase 2 — Evaluación

- Solo se activa si `evaluacion/` contiene documentos
- El criterio de vinculación por contenido requiere correspondencia temática sustantiva, no coincidencias superficiales de palabras
- Una propuesta no reemplaza la ficha original; es un documento independiente que señala complementos o modificaciones posibles
- Las propuestas siguen el mismo estándar de fidelidad factual que las fichas

---

## Gestión de errores

| Situación | Acción del agente |
|---|---|
| `entradas/` vacía | Preguntar al usuario si desea buscar fuentes en internet (PASO 3.1). Detener solo si el usuario rechaza o no se encuentran fuentes aceptadas |
| Archivo `.md` de sistema faltante | Informar al usuario indicando qué archivo falta |
| Documento en `evaluacion/` no vinculable | Registrar en reporte final, omitir de la evaluación |
| Documento fuente ilegible o corrupto | Informar al usuario, continuar con el siguiente |
