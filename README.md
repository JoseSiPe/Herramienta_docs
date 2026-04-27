# Herramienta_Docs

Sistema automatizado de revisión sistemática y generación de documentos guiado por instrucciones en formato Markdown.

## ¿Qué hace?

Dado un conjunto de documentos fuente (PDF, PPT, WORD), el agente:

1. Se configura para un dominio temático específico (reutilizable entre sesiones)
2. Lee cada documento y genera una **Ficha** mediante 3 ciclos iterativos de revisión
3. Si existen documentos humanos para contrastar, genera **Propuestas** de complemento o modificación

Todo el proceso es autónomo tras una configuración inicial mínima.

## Estructura

```
Herramienta_Docs/
├── Orquestador.md        ← punto de entrada para el agente
├── AVISO_LEGAL.txt       ← descargo de responsabilidad
├── entradas/             ← depositar aquí los documentos fuente a revisar
├── salidas/
│   ├── fichas/           ← fichas finales generadas por el agente
│   └── provisionales/    ← borradores iterativos (Provisional 1.0, 2.0)
├── evaluacion/           ← documentos humanos para contrastar
│   └── propuestas/       ← propuestas generadas por el agente
├── mds/
│   ├── Herramienta_Docs.md   ← núcleo operativo
│   ├── instrucciones.md      ← reglas del proceso y guardrails
│   ├── formato.md            ← plantillas de fichas y propuestas
│   └── contexto_[dominio].md ← generado automáticamente por sesión
└── .claude/
    └── skills/
        ├── correr-herramienta/   ← ejecuta la rutina completa
        ├── nuevo-dominio/        ← fuerza onboarding de dominio nuevo
        └── estado-docs/          ← revisa el estado de las carpetas
```

## Cómo usar

1. Deposita los documentos a revisar en `entradas/`
2. (Opcional) Deposita documentos humanos en `evaluacion/` para contraste
3. Inicia Claude Code desde dentro de la carpeta `Herramienta_Docs` y ejecuta:

   ```
   /correr-herramienta
   ```

   O si prefieres sin skills:

   > "Lee el Orquestador.md y ejecuta la rutina"

4. El agente te pedirá el dominio temático y, si no existe un contexto previo, te hará 5 preguntas de configuración
5. A partir de ahí opera de forma autónoma hasta generar el reporte final

## Skills disponibles

| Skill | Descripción |
|---|---|
| `/correr-herramienta` | Ejecuta la rutina completa de principio a fin |
| `/nuevo-dominio` | Crea un contexto de dominio nuevo sin ejecutar la rutina |
| `/estado-docs` | Muestra qué hay en cada carpeta sin procesar nada |

> Los skills usan el directorio de trabajo actual. Claude Code debe iniciarse desde dentro de `Herramienta_Docs`.

## Outputs

| Archivo | Descripción |
|---|---|
| `salidas/fichas/Ficha [Temática].md` | Documento final consolidado |
| `salidas/provisionales/Provisional 1.0 — [Temática].md` | Borrador tras primera lectura |
| `salidas/provisionales/Provisional 2.0 — [Temática].md` | Borrador tras segunda revisión |
| `evaluacion/propuestas/Propuesta [Temática].md` | Propuesta de complemento/modificación (si aplica) |

## Aviso legal

El uso de esta herramienta es responsabilidad exclusiva del usuario. Esto incluye los documentos procesados, las fuentes descargadas de internet y los documentos generados. Consulta [`AVISO_LEGAL.txt`](AVISO_LEGAL.txt) para el descargo de responsabilidad completo.

## Reutilización por dominio

El archivo `mds/contexto_[dominio].md` se genera la primera vez que se usa un dominio y se reutiliza en sesiones posteriores. El agente mostrará su contenido y preguntará si deseas usarlo o generar uno nuevo.
