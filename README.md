# Programación

![UPS · Carrera de Computación](assets/logos/ups-computacion.png)

**Asignatura:** Programación · C-CT-ICO-101  
**Nivel:** 1 · Carrera de Computación · Sede Cuenca  
**Autor:** Ing. Pablo Torres, Mgtr.  
**Repositorio:** icc-pro-material

## Propósito y público

Estudiar fundamentos de programación, diseñar algoritmos y desarrollar soluciones independientes. Utilizar Python como lenguaje principal y Java como complemento. No desarrollar un proyecto acumulativo. El programa oficial no especifica prerrequisitos formales; como preparación docente, manejar operaciones aritméticas, archivos y terminal básica.

## Consultar el material

Descomprimir el paquete y abrir [index.html](index.html). Seleccionar unidad y lenguaje, abrir una lectura en el visor o en una página independiente y descargar MD o PPTX. Todas las PL se desarrollan en Python. Las presentaciones de la Unidad 3 explican únicamente Python; las unidades 1 y 2 incluyen también presentación Java.

Para servirlo por HTTP desde la raíz:

```bash
python3 -m http.server 8000
```

Abrir http://localhost:8000. En Windows, utilizar `py` si corresponde a la instalación disponible. La consulta utiliza HTML generado, fuentes, estilos y scripts locales, sin CDN.

## Unidades

| Unidad | Segmentos | Alcance | PL Python |
|---|---:|---|---:|
| [1. Lógica Matemática](01/README.md) | 1 | Álgebra de Boole, con proposiciones como fundamento integrado | 1 |
| [2. Algoritmos](02/README.md) | 1 | Representación, decisiones, repetición y pruebas de escritorio | 1 |
| [3. Lenguaje de Programación](03/README.md) | 13 | Fundamentos, E/S, control, ciclos, funciones, cadenas, listas, recorridos, matrices, tuplas, archivos, módulos y entornos | 4 |

Los códigos de segmentos son editoriales: el programa oficial no numera subtemas. Consultar la correspondencia oficial en la documentación docente.

## Organización

| Ruta | Función |
|---|---|
| `01/`, `02/`, `03/` | Unidades y segmentos |
| `python/material.md` | Lectura principal, demostración, ejercicios y PC |
| `java/material.md` | Versión complementaria con los mismos problemas y casos |
| `doc.md` | Correspondencia curricular del docente, separada de la lectura |
| `presentacion.pptx` | Presentación Python editable |
| `ejemplos/` de cada versión | Demostración completa, datos y salida esperada |
| `assets/` de cada segmento | Infografía SVG y PNG |
| `PLs/python/` | Guías autónomas con rúbrica y PPTX |
| `demostraciones/` | Lanzadores de los ejemplos sin duplicar sus fuentes |
| `plantillas/trabajo-estudiante/` | Inicio del repositorio personal de actividades |
| `docs/` | Mantenimiento y documentación docente |
| `scripts/` | Generación HTML y controles |

## Trabajar con PC y PL

1. Leer conceptos y anticipar la salida de la demostración.
2. Ejecutar el ejemplo y comparar con `salida-esperada.txt`.
3. Resolver los ejercicios progresivos y la PC en una sola versión.
4. Crear una carpeta independiente por actividad y registrar evidencia en `evidencias/`.
5. Desarrollar las PL en Python, revisar su rúbrica y preparar defensa.

No se incluyen soluciones de PC ni PL. Registrar commits reales, sin copiar hashes ficticios. Consultar [guía de Git](docs/guia-git.md) y [organización del trabajo](docs/proyecto-estudiante.md).

## Ejecutar demostraciones

Desde la raíz:

```bash
python3 demostraciones/python/ejecutar.py 3.09
python3 demostraciones/java/ejecutar.py 3.09
```

El lanzador Java utiliza Python únicamente para localizar, compilar y ejecutar la demostración; los fuentes Java no dependen de Python. También se puede entrar en su carpeta `ejemplos`, ejecutar `javac -encoding UTF-8 -d build *.java` y `java -cp build Demo`. No utilizar Maven ni Gradle. Los comandos específicos y entradas aparecen en cada lectura.

## Fuentes y tipografía

Instalar `assets/fonts/DejaVuSans.ttf` y `assets/fonts/DejaVuSans-Bold.ttf` antes de editar las presentaciones. Abrir cada archivo de fuente y seleccionar la opción de instalación del sistema. La licencia está incluida. HTML y PPTX utilizan DejaVu Sans. El visor de GitHub controla la tipografía del Markdown.

## Regenerar y comprobar

Requerir Node.js >=22. El parser Markdown está incluido; no ejecutar `npm install` para generar HTML.

```bash
node scripts/sync-examples.mjs --check
node scripts/build-site.mjs
node scripts/check-links.mjs
```

También ejecutar `npm run build:site` y `npm run check:links`. Editar `material.md` como fuente de lectura y demostración. Tras cambiar bloques marcados, ejecutar `node scripts/sync-examples.mjs` para actualizar fuentes. Regenerar sobrescribe HTML y `course-data.js`; no modifica PPTX. Cambiar CSS no exige convertir Markdown otra vez. Agregar contenidos requiere registrarlos en `assets/catalogo.json`.

## Publicación y mantenimiento

Consultar [publicación](docs/publicacion.md), [esquema del catálogo](docs/catalogo.md), [versiones](docs/versiones.md) y [verificación](docs/verificacion.md). No se ha publicado el sitio ni creado un repositorio remoto. Preparar solo la carpeta `build/pages` mediante el script de staging antes de publicar.

## Documentación docente

Consultar [análisis de referencias](docs/analisis-referencias.md), [mapa curricular](docs/mapa-curricular.md). Mantener esta correspondencia al modificar contenidos. Los bancos Moodle están agrupados por unidad, tema, conceptos y trazas; consultar [guía de importación](docs/moodle.md).

El inventario real está en `docs/arbol.txt`. Después de modificar y verificar la entrega, ejecutar `python3 scripts/make-manifest.py` para actualizar inventario y `MANIFEST.sha256`. El manifiesto excluye su propio hash y archivos temporales.
