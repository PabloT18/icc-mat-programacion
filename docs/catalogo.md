# Catálogo y fuentes de verdad

## Esquema versión 2

Conservar `units`, `topics` y `labs`. Agregar `course`, `schema_version`, `protection` y campos de versión a cada tema.

| Campo | Significado |
|---|---|
| `id` | Identidad única: código editorial más lenguaje, por ejemplo 3.09-python |
| `curricular_code` | Código común usado por compatibilidad del esquema; en este programa es editorial |
| `code_kind` | Valor editorial para no atribuir numeración oficial inexistente |
| `language` | python o java |
| `path` | Carpeta de versión relativa a la raíz |
| `prev`, `next` | Carpetas anterior y siguiente del mismo lenguaje |
| `pptx` | Ruta explícita a la presentación compartida o específica |
| `deck_language` | Lenguaje de la presentación, visible antes de descargar |
| `scope` | Resumen de correspondencia y clasificación editorial |

Las PL incluyen ruta explícita, lenguaje Python, objetivos, requisitos, fases, pruebas, entregables, defensa y rúbrica. Cada criterio de rúbrica tiene puntaje máximo y descriptores completo, parcial y no logrado.

## Archivo que editar

- Editar el cuerpo de lectura y los bloques de demostración en `material.md`.
- Ejecutar `sync-examples.mjs` para copiar bloques marcados hacia `ejemplos/`; usar `--check` para comparar sin modificar.
- Editar el catálogo para títulos del listado, orden, rutas y contenido estructurado de las PL.
- No duplicar teoría ni código de demostraciones dentro del catálogo.
- Generar `course-data.js` y los HTML con `build-site.mjs`; no editarlos manualmente.
- Editar PPTX por separado y conservar correspondencia con la lectura.
- Revisar `doc.md` al cambiar títulos, anclas o alcance.

El generador crea `index.html` como lectura canónica y `material.html` como copia para navegación documental. Las dos se generan desde el mismo MD. Cada segmento tiene una portada local para escoger lenguaje.
