"""
Convierte una Ficha .md al formato .docx usando la plantilla de plantillas/.

Uso:
    python scripts/md_to_docx.py <ruta_ficha.md>
    python scripts/md_to_docx.py salidas/fichas/  # procesa todas las fichas
"""
import re
import sys
from pathlib import Path
from docxtpl import DocxTemplate


# ── Mapeo de secciones MD → campos de plantilla ───────────────────────────────

METADATOS = [
    (r"Título original",  "titulo_original"),
    (r"Tipo de documento","tipo_documento"),
    (r"Autor\(es\)",      "autores"),
    (r"Fecha",            "fecha"),
    (r"Fuente / origen",  "fuente"),
]

SECCIONES = [
    ("Resumen factual",                  "resumen"),
    ("Elementos prioritarios extraídos", "elementos_prioritarios"),
    ("Términos clave identificados",     "terminos_clave"),
    ("Datos relevantes adicionales",     "datos_adicionales"),
    ("Elementos excluidos",              "elementos_excluidos"),
]


# ── Limpieza de markdown ──────────────────────────────────────────────────────

def limpiar_linea(linea: str) -> str:
    """Elimina marcadores markdown y devuelve texto plano."""
    linea = re.sub(r"\*\*\*(.+?)\*\*\*", r"\1", linea)
    linea = re.sub(r"\*\*(.+?)\*\*",     r"\1", linea)
    linea = re.sub(r"\*(.+?)\*",         r"\1", linea)
    linea = re.sub(r"^#{1,6}\s+",        "",    linea)  # encabezados → texto
    linea = re.sub(r"^[-*]\s+",          "• ",  linea)  # listas → bullet
    return linea.strip()


def seccion_a_items(texto: str) -> list[str]:
    """
    Divide el contenido de una sección en párrafos independientes.
    Cada bloque separado por línea en blanco se convierte en un item.
    """
    items = []
    for bloque in re.split(r"\n{2,}", texto.strip()):
        lineas = [limpiar_linea(l) for l in bloque.splitlines() if l.strip()]
        if lineas:
            items.append("\n".join(lineas))
    return [i for i in items if i]


# ── Parseo del .md ────────────────────────────────────────────────────────────

def parsear_ficha(md_path: Path) -> dict:
    texto = md_path.read_text(encoding="utf-8")
    campos = {}

    # Título (H1)
    m = re.search(r"^#\s+(.+)$", texto, re.MULTILINE)
    campos["titulo"] = m.group(1).strip() if m else md_path.stem

    # Metadatos de "Datos del documento fuente"
    m = re.search(r"## Datos del documento fuente\n(.*?)(?=\n## |\Z)", texto, re.DOTALL)
    bloque_datos = m.group(1) if m else ""
    for patron, key in METADATOS:
        mm = re.search(rf"- {patron}:\s*(.+)", bloque_datos)
        campos[key] = mm.group(1).strip() if mm else "[No disponible]"

    # Secciones de contenido → listas de párrafos para {%p for %}
    for heading, key in SECCIONES:
        m = re.search(
            rf"## {re.escape(heading)}\n(.*?)(?=\n## |\Z)",
            texto, re.DOTALL
        )
        contenido = m.group(1).strip() if m else "[No disponible en el documento fuente]"
        campos[f"{key}_items"] = seccion_a_items(contenido)

    return campos


# ── Conversión ────────────────────────────────────────────────────────────────

def convertir(md_path: Path, plantilla: Path, salida: Path):
    campos = parsear_ficha(md_path)
    doc = DocxTemplate(plantilla)
    doc.render(campos)
    doc.save(salida)
    print(f"OK: {md_path.name}  ->  {salida}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    entrada = Path(sys.argv[1])
    base = Path(__file__).parent.parent
    plantilla = base / "plantillas" / "plantilla_ficha.docx"
    output_dir = base / "salidas" / "docx"
    output_dir.mkdir(parents=True, exist_ok=True)

    if not plantilla.exists():
        print(f"Error: no se encontró la plantilla en {plantilla}")
        print("Ejecuta primero: python scripts/crear_plantilla.py")
        sys.exit(1)

    # Modo carpeta: procesa todas las fichas
    if entrada.is_dir():
        fichas = list(entrada.glob("Ficha *.md"))
        if not fichas:
            print(f"No se encontraron fichas en {entrada}")
            sys.exit(1)
        for ficha in fichas:
            convertir(ficha, plantilla, output_dir / (ficha.stem + ".docx"))
    else:
        convertir(entrada, plantilla, output_dir / (entrada.stem + ".docx"))


if __name__ == "__main__":
    main()
