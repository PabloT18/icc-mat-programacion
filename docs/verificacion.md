# Verificación de la entrega

Fecha de revisión: 25 de septiembre de 2026.

## Alcance comprobado

- Programa oficial leído íntegramente: cuatro páginas. Identificación y horas en página 1; tres unidades, resultados, indicadores y contenidos en página 2; metodología, evaluación y bibliografía en páginas 3–4.
- Cobertura: 15 segmentos editoriales, 30 lecturas Python/Java y 15 documentos docentes. Unidad 1 y Unidad 2 tienen un segmento cada una; Unidad 3 tiene 13. Proposiciones se integra como fundamento de Álgebra de Boole. Los complementos están distinguidos en el mapa curricular.
- 30 demostraciones ejecutadas, incluidas 15 compilaciones Java, con comparación de stdout frente a salida esperada. Se ejecutaron además 130 celdas de ejercicios docentes de forma independiente y se compararon sus resultados. No se incluyen soluciones de PC ni PL.
- 32 archivos de código vinculados al Markdown comprobados mediante el script de sincronización. Los bloques marcados del MD son su fuente editorial.
- 15 bancos XML bien formados: 150 preguntas de elección múltiple, cuatro alternativas distintas por pregunta y una respuesta con fracción 100. Categorías bajo `$course$/top/`.
- Seis rúbricas con suma de 10 puntos y descriptores completo, parcial y no logrado. Cuatro PL de Unidad 3 cubren bloques diferentes; su número es una adaptación expresamente solicitada.
- 23 presentaciones PPTX, 283 diapositivas. Todas se renderizaron y se revisaron en hojas de contacto; también se ampliaron diapositivas representativas de código, conceptos y PC. Las comprobaciones de paquete, geometría, tamaño 16:9, tipografía y reapertura mediante el motor de generación terminaron sin hallazgos. Texto, código y diagramas son elementos editables. No se usaron capturas de páginas como diapositivas.
- Infografías técnicas SVG con versión PNG local. Se revisaron recursos representativos. Se conservan logos y fuentes del paquete base.
- Generador HTML y comprobador de enlaces ejecutados desde una copia limpia, sin instalar dependencias. El informe de ejecución registra las cantidades efectivamente comprobadas. El staging excluye soluciones docentes, bancos de evaluación, cachés y compilados.

## Repetir comprobaciones

Desde la raíz del repositorio:

```bash
node scripts/sync-examples.mjs --check
node scripts/build-site.mjs
node scripts/check-links.mjs
python3 scripts/verify-material.py
node scripts/stage-pages.mjs
```

También funcionan `npm run build:site` y `npm run check:links`. `check-links.mjs` recorre HTML y MD; comprueba existencia de destinos locales y anclas explícitas `id` de archivos HTML/MD. No consulta enlaces externos, no interpreta JavaScript ni valida anclas internas de PDF. Las rutas del catálogo se comprueban por los HTML generados y sus enlaces.

Los registros [material.json](verificacion/material.json), [salidas-demostraciones.json](verificacion/salidas-demostraciones.json) y [entrega.json](verificacion/entrega.json) contienen resultados de ejecución y conteos. Las salidas esperadas de las lecturas son contratos; las salidas registradas proceden de ejecución real.

## Límites concretos

Las demostraciones se ejecutaron en CPython 3.12.14 y OpenJDK 17.0.20; las versiones objetivo documentadas son CPython 3.14.7 y JDK 27. Falta repetir la ejecución en esas dos instalaciones objetivo. No se utilizan características exclusivas de las versiones más nuevas. Consultar [versiones](versiones.md).

No se pudo ejecutar la prueba de navegador: el entorno carecía del binario Chromium requerido. La estructura estática, rutas y JavaScript fueron comprobados, pero queda por verificar interactivamente: selector de unidad y lenguaje, lectura en iframe, anterior/siguiente conservando lenguaje, vuelta al índice, vista móvil, teclado y botón de restricciones de las PL. Abrir `index.html` o servir por HTTP como explica el README.

No se importaron los XML en una instancia Moodle. La prueba pendiente consiste en importar un banco de cada tipo, revisar categorías, previsualizar una pregunta y comprobar calificación. No se abrió PowerPoint ni LibreOffice; la edición y el renderizado nativos de esas aplicaciones quedan sujetos a la instalación de DejaVu Sans. Las presentaciones sí se renderizaron con el motor de generación, no solo se verificó su existencia.

No se publicó el sitio ni se creó un repositorio remoto. Las restricciones de copia son superficiales, configurables y no evitan capturas, inspección del HTML ni uso de IA.
