# Orquestador.md
## Sistema de Revisión Sistemática y Generación Automatizada de Documentos

---

## INSTRUCCIÓN INICIAL AL AGENTE

Al recibir esta instrucción, **no ejecutes ninguna tarea de revisión todavía**. Sigue los pasos en el orden exacto en que aparecen. Todas las rutas son relativas a la ubicación de este archivo.

---

## PASO 1 — Configuración del contexto de dominio

### 1.1 Pregunta al usuario

Formula esta única pregunta antes de cualquier acción:

> "¿Cuál es el dominio temático de los documentos que vamos a revisar en esta sesión?"

**Normalización del nombre de dominio:** con la respuesta del usuario, aplica estas reglas para construir el nombre del archivo de contexto:
- Convertir a minúsculas
- Reemplazar espacios con guiones
- Sustituir caracteres acentuados: á→a, é→e, í→i, ó→o, ú→u, ñ→n, ü→u
- Eliminar cualquier otro carácter especial
- Ejemplo: "Estimación para Áreas Pequeñas" → `estimacion-areas-pequenas`

Nombre del archivo resultante: `mds/Contexto/contexto_[dominio-normalizado].md`

### 1.2 Verificación de existencia del contexto

Busca si existe `mds/Contexto/contexto_[dominio].md`.

**— Si el archivo EXISTE (coincidencia exacta):**

1. Lee su contenido completo
2. Preséntalo al usuario:
   > "Encontré un contexto existente para este dominio. Este es su contenido:"
   > [contenido del archivo]
   > "¿Ejecutamos la sesión con este contexto, o deseas generar uno nuevo?"
3. Espera respuesta:
   - Confirma usarlo → continúa al **PASO 2**
   - Solicita uno nuevo → ejecuta **PASO 1.3** y sobreescribe el archivo

**— Si el archivo NO EXISTE (búsqueda semántica):**

Antes de concluir que no hay contexto previo, realiza una búsqueda semántica:

1. Lista todos los archivos `mds/contexto_*.md` existentes
2. Para cada uno, lee su título y sección "Términos clave y conceptos centrales"
3. Evalúa si alguno es temáticamente afín a lo que el usuario describió, considerando:
   - Sinónimos, hipónimos e hiperónimos del dominio indicado
   - Solapamiento de términos clave o área disciplinar
   - Campo semántico compartido aunque la denominación exacta difiera

**— Si se encuentra uno o más contextos afines:**

Preséntalo al usuario:
> "No encontré un contexto con ese nombre exacto, pero encontré uno relacionado:"
> **[nombre del archivo]**
> [contenido del archivo]
> "¿Ejecutamos la sesión con este contexto, deseas generar uno nuevo, o prefieres renombrarlo a '[dominio]'?"

Espera respuesta:
- Usar el existente → continúa al **PASO 2** con ese archivo de contexto
- Generar uno nuevo → ejecuta **PASO 1.3** con el nombre normalizado del dominio actual
- Renombrar → copia el contenido al nuevo archivo `mds/Contexto/contexto_[dominio].md` y continúa al **PASO 2**

**— Si no existe ningún contexto afín:**

> "No encontré un contexto previo para este dominio. Voy a hacerte algunas preguntas para configurarlo."

Ejecuta **PASO 1.3**.

---

### 1.3 Onboarding — Generación de contexto nuevo

Formula las siguientes preguntas **una a la vez**, esperando respuesta antes de continuar:

1. ¿Cuál es el **objetivo principal** de esta revisión sistemática?
2. ¿Qué **tipo de elementos** son prioritarios extraer? *(ej: datos cuantitativos, metodologías, conclusiones, fechas, autores, marcos teóricos)*
3. ¿Existen **términos clave, conceptos centrales o categorías** que deben rastrearse en todos los documentos?
4. ¿Qué **tipos de documentos** se revisarán? *(PDF, PPT, WORD u otros)*
5. ¿Hay alguna **restricción o criterio de exclusión** que el agente deba considerar?

Con las respuestas, genera y guarda `mds/Contexto/contexto_[dominio].md` usando esta plantilla:

```
# Contexto: [Dominio]

## Objetivo de la revisión
[respuesta 1]

## Elementos prioritarios a extraer
[respuesta 2]

## Términos clave y conceptos centrales
[respuesta 3]

## Tipos de documentos fuente
[respuesta 4]

## Restricciones y criterios de exclusión
[respuesta 5]
```

---

## PASO 2 — Carga de herramientas

Carga los siguientes archivos en este orden:

1. `mds/instrucciones.md`
2. `mds/Contexto/contexto_[dominio].md`
3. `mds/formato.md`

Si alguno no existe, detente e informa al usuario cuál falta antes de continuar.

Carga también `mds/Archon.md` para las instrucciones operativas de las fases siguientes.

---

## PASO 3 — Fase 1: Procesamiento de entradas (AUTÓNOMO)

Lee todos los documentos presentes en la carpeta `entradas/`.

**— Si `entradas/` está vacía:**

Pregunta al usuario:

> "No hay documentos en entradas/. ¿Quieres que busque fuentes en internet sobre el dominio '[dominio]'?"

Si el usuario responde **no** → detente e informa.

Si el usuario responde **sí** → ejecuta el **PASO 3.1** antes de continuar.

---

### PASO 3.1 — Búsqueda de fuentes en internet

Usa los términos clave y el objetivo definidos en `mds/Contexto/contexto_[dominio].md` para buscar fuentes relevantes en internet. Prioriza resultados que sean documentos descargables (PDF, PPT, WORD).

Para cada fuente encontrada, presenta al usuario la siguiente información **antes de descargar nada**:

```
Fuente encontrada:
  Título:       [título del documento o página]
  URL:          [enlace completo]
  Tipo:         [PDF / PPT / WORD / página web]
  Descripción: [resumen breve de qué contiene]

¿Deseas descargar este documento? (sí / no / detener búsqueda)
```

Espera respuesta del usuario para cada fuente antes de continuar con la siguiente.

- **sí** → descarga el archivo y guárdalo en `entradas/` con su nombre original
- **no** → omite esa fuente y presenta la siguiente
- **detener búsqueda** → deja de buscar y continúa con los archivos ya descargados en `entradas/`

Si tras la búsqueda `entradas/` sigue vacía (el usuario rechazó todas las fuentes), detente e informa.

---

Para cada documento encontrado, sigue este proceso:

**— Paso previo: detección de ficha existente**

Realiza una lectura inicial rápida del documento para determinar su temática (`[Temática]`). Luego verifica si existe el archivo `salidas/fichas/Ficha [Temática].md`.

- **Si NO existe** → procede normalmente con los 3 ciclos
- **Si YA EXISTE** → informa al usuario y espera instrucción:

  > "Ya existe una ficha para '[Temática]'. ¿Qué deseas hacer?"
  > 1. **Actualizar** — re-procesa el documento y sobreescribe la ficha y provisionales existentes
  > 2. **Saltar** — omite este documento y pasa al siguiente
  > 3. **Conservar ambas** — genera la nueva ficha con sufijo `_v2` sin eliminar la anterior

**— Ciclos iterativos (si procede):**

1. Aplica los 3 ciclos iterativos definidos en `mds/instrucciones.md`
2. Guarda los provisionales en `salidas/provisionales/`:
   - `Provisional 1.0 — [Temática].md`
   - `Provisional 2.0 — [Temática].md`
3. Guarda la ficha final en `salidas/fichas/`:
   - `Ficha [Temática].md`
4. El título `[Temática]` debe derivarse del contenido del documento fuente
5. Aplica en todo momento la estructura definida en `mds/formato.md`

Procesa todos los documentos de `entradas/` antes de continuar al siguiente paso.

---

## PASO 4 — Fase 2: Evaluación (CONDICIONAL Y AUTÓNOMA)

### 4.1 Verificación de contenido

Revisa si existen documentos en la carpeta `evaluacion/` (excluyendo la subcarpeta `evaluacion/propuestas/`).

**— Si `evaluacion/` está vacía:**
Omite esta fase completamente e informa al usuario al finalizar.

**— Si `evaluacion/` tiene documentos:**
Ejecuta el proceso de evaluación para cada documento encontrado.

---

### 4.2 Vinculación de documentos humanos con fichas

Para cada documento en `evaluacion/`:

**Intento 1 — Coincidencia por título idéntico:**
Busca en `salidas/fichas/` una `Ficha [Temática].md` cuyo título coincida exactamente.

**Intento 2 — Coincidencia por contenido (si el título no coincide):**
1. Lee el documento humano completo
2. Lee todas las fichas disponibles en `salidas/fichas/`
3. Determina si el documento humano es temáticamente relacionado con alguna ficha
4. Informa al usuario el resultado:
   - Si relacionado: *"Vinculé '[doc humano]' con 'Ficha [X]' por coincidencia de contenido"*
   - Si no relacionado: *"No pude vincular '[doc humano]' con ningún documento fuente. Se omite de la evaluación"*

---

### 4.3 Generación de propuestas

Para cada vínculo establecido, aplica los 3 ciclos iterativos de `mds/instrucciones.md` usando como fuentes:
- El documento humano de `evaluacion/`
- La `Ficha [Temática].md` correspondiente de `salidas/fichas/`

El objetivo de cada ciclo es identificar elementos para complementar o modificar la ficha, respetando la metodología definida en `mds/instrucciones.md` y los parámetros de `mds/Contexto/contexto_[dominio].md`.

Guarda en `evaluacion/propuestas/`:
- `Provisional 1.0 — Propuesta [Temática].md`
- `Provisional 2.0 — Propuesta [Temática].md`
- `Propuesta [Temática].md`

---

## PASO 5 — Reporte final

Al concluir todas las fases, presenta al usuario un resumen:

```
PROCESO COMPLETADO
==================
Fichas generadas:
  - [lista de Ficha [Temática].md generadas]

Propuestas generadas:
  - [lista de Propuesta [Temática].md generadas]

Documentos no vinculados:
  - [lista, o "Ninguno" si todos fueron vinculados]

Documentos en evaluacion/ omitidos:
  - [lista, o "Ninguno"]
```

---

## REGLAS GENERALES DEL AGENTE

- **Rutas de salida estrictas:** los únicos destinos válidos para guardar archivos son `salidas/fichas/`, `salidas/provisionales/`, `salidas/docx/`, `evaluacion/propuestas/` y `mds/Contexto/`. Nunca guardes archivos directamente en `salidas/` ni en `mds/`
- Tras el PASO 1, opera de forma autónoma. Las únicas excepciones donde se permite interacción adicional con el usuario son: (a) PASO 3.1 cuando `entradas/` está vacía y se requiere autorización por cada descarga de internet, (b) detección de ficha existente en PASO 3 que requiere instrucción del usuario, y (c) cualquier situación de error no resuelta
- No tomes decisiones sobre dominio o contexto sin confirmación del usuario en el PASO 1
- No generes contenido inferido o externo a los documentos fuente
- Conserva todos los provisionales como registro del proceso
- Respeta estrictamente la jerarquía: Orquestador → Herramienta_Docs → instrucciones → contexto → formato
