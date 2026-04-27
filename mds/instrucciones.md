# instrucciones.md

## Instrucciones para la Revisión Sistemática y Generación Automatizada de Documentos

---

### 1. Principio de Fidelidad Factual

La lectura y generación de documentos debe basarse **únicamente** en los elementos **factuales** contenidos en los documentos fuente. No se deben incluir inferencias, interpretaciones, suposiciones ni información externa al documento original. Todo enunciado generado debe poder rastrearse directamente a un elemento presente en la fuente.

---

### 2. Estructura de Fichas por Documento

A cada documento fuente (PDF, PPT o WORD) le corresponde un único documento de salida denominado **"Ficha [Temática]"**, donde `[Temática]` es reemplazado por un título breve que refleje la temática central del documento revisado.

- Formato del nombre de salida: `Ficha [Título Temático]`
- Relación obligatoria: **un documento fuente → una ficha**
- El título temático debe derivarse del contenido del propio documento, no asignarse arbitrariamente

---

### 3. Proceso Iterativo de Generación (3 ciclos por ficha)

La generación de cada ficha sigue un proceso iterativo de **3 ciclos de lectura y contraste**. Los documentos provisionales se conservan como memoria de revisión.

#### Ciclo 1 — Generación Base → `Provisional 1.0`
1. Realizar la primera lectura completa del documento fuente
2. Extraer los elementos factuales identificados
3. Generar el documento base titulado **Provisional 1.0**

#### Ciclo 2 — Primera Revisión y Contraste → `Provisional 2.0`
1. Re-leer el documento fuente original desde el inicio
2. Contrastar su contenido con lo vertido en el **Provisional 1.0**
3. Identificar omisiones, imprecisiones o información no capturada en el ciclo anterior
4. Complementar y corregir, generando el **Provisional 2.0**

#### Ciclo 3 — Segunda Revisión y Consolidación → `Ficha [Temática]`
1. Re-leer nuevamente el documento fuente original
2. Contrastar su contenido con lo vertido en el **Provisional 2.0**
3. Realizar los ajustes finales necesarios
4. Generar el documento consolidado definitivo: **Ficha [Temática]**

#### Conservación de Provisionales
- Los documentos `Provisional 1.0` y `Provisional 2.0` **deben conservarse** como registro del proceso de revisión
- Su título sigue el formato: **Provisional X.0**, donde `X` corresponde al número de iteración (1, 2, 3...)
- Los provisionales no se eliminan ni sobrescriben; representan la memoria del proceso de construcción de cada ficha
