# Archon

Sistema automatizado de revisión sistemática y generación de documentos guiado por instrucciones en formato Markdown.

## ¿Qué hace?

Dado un conjunto de documentos fuente (PDF, PPT, WORD), el agente:

1. Se configura para un dominio temático específico (reutilizable entre sesiones)
2. Lee cada documento y genera una **Ficha** mediante 3 ciclos iterativos de revisión
3. Si existen documentos humanos para contrastar, genera **Propuestas** de complemento o modificación

Todo el proceso es autónomo tras una configuración inicial mínima.

## Estructura

```
Archon/
├── Orquestador.md        ← punto de entrada para el agente
├── AVISO_LEGAL.txt       ← descargo de responsabilidad
├── entradas/             ← depositar aquí los documentos fuente a revisar
├── salidas/
│   ├── fichas/           ← fichas finales generadas por el agente
│   ├── provisionales/    ← borradores iterativos (Provisional 1.0, 2.0)
│   └── docx/             ← exportaciones Word generadas por scripts/
├── evaluacion/           ← documentos humanos para contrastar
│   └── propuestas/       ← propuestas generadas por el agente
├── mds/
│   ├── Archon.md             ← núcleo operativo
│   ├── instrucciones.md      ← reglas del proceso y guardrails
│   ├── formato.md            ← plantillas de fichas y propuestas
│   └── Contexto/             ← contextos de dominio (generados automáticamente)
├── plantillas/
│   └── plantilla_ficha.docx  ← plantilla Word para exportación
├── scripts/
│   ├── md_to_docx.py         ← convierte fichas .md a .docx
│   └── crear_plantilla.py    ← genera la plantilla Word base
└── .claude/
    └── skills/
        ├── correr-herramienta/
        ├── nuevo-dominio/
        ├── estado-docs/
        └── reset-herramienta/
```

## Cómo usar

1. Deposita los documentos a revisar en `entradas/`
2. (Opcional) Deposita documentos humanos en `evaluacion/` para contraste
3. Inicia Claude Code desde dentro de la carpeta `Archon` y ejecuta:

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
| `/reset-herramienta` | Elimina todos los documentos generados, dejando la estructura limpia |

> Los skills usan el directorio de trabajo actual. Claude Code debe iniciarse desde dentro de `Archon`.

## Exportación a Word

Para convertir fichas generadas a `.docx`:

```bash
# Una ficha
python scripts/md_to_docx.py "salidas/fichas/Ficha XYZ.md"

# Todas las fichas
python scripts/md_to_docx.py salidas/fichas/
```

Personaliza el diseño editando `plantillas/plantilla_ficha.docx` en Word sin tocar los marcadores `{{ }}`.

## Outputs

| Archivo | Descripción |
|---|---|
| `salidas/fichas/Ficha [Temática].md` | Documento final consolidado |
| `salidas/provisionales/Provisional 1.0 — [Temática].md` | Borrador tras primera lectura |
| `salidas/provisionales/Provisional 2.0 — [Temática].md` | Borrador tras segunda revisión |
| `salidas/docx/Ficha [Temática].docx` | Exportación Word de la ficha |
| `evaluacion/propuestas/Propuesta [Temática].md` | Propuesta de complemento/modificación (si aplica) |

## Aviso legal

El uso de esta herramienta es responsabilidad exclusiva del usuario. Consulta [`AVISO_LEGAL.txt`](AVISO_LEGAL.txt) para el descargo de responsabilidad completo.

## Reutilización por dominio

El archivo `mds/Contexto/contexto_[dominio].md` se genera la primera vez que se usa un dominio y se reutiliza en sesiones posteriores. El agente mostrará su contenido y preguntará si deseas usarlo, generar uno nuevo, o si detecta un dominio semánticamente relacionado te lo propondrá automáticamente.
