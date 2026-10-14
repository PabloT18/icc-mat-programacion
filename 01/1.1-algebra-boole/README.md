# 1.1 · Álgebra de Boole

**Programación · Unidad 1: Lógica Matemática**  
**Ing. Pablo Torres, Mgtr. · Universidad Politécnica Salesiana · Computación · Cuenca**

| Recurso | Lectura | Fuente editable |
|---|---|---|
| Python | [Abrir HTML](python/index.html) | <a href="python/material.md" download>Descargar MD</a> |
| Java | [Abrir HTML](java/index.html) | <a href="java/material.md" download>Descargar MD</a> |
| Presentación de referencia del docente | [Consultar PDF](referencias/01.05-logica-matematica.pdf) | Documento proporcionado como referencia |

## Contenido

1. Variables booleanas, asignación, comparaciones y tablas de verdad.
2. AND, OR, NOT, XOR, XNOR y contraste con NAND/NOR.
3. Aplicaciones: decisiones, circuitos, conjuntos y filtros.
4. Siete leyes en el orden de la presentación, más leyes auxiliares y absorción generalizada.
5. Dos simplificaciones resueltas, con cada paso justificado y comprobación exhaustiva.
6. Treinta y seis ejercicios propuestos y PC1.1.

Las versiones mantienen los mismos problemas, fórmulas, tablas y casos. Cada lenguaje tiene explicación y código propios. La práctica se entrega en una sola versión. Los ejercicios propuestos y la PC no incluyen soluciones.

## Consultar y ejecutar

Abrir `index.html` después de descomprimir. Los HTML, estilos y fuentes son locales. Las tablas son texto estructurado y no imágenes. No se incluyen infografías nuevas ni presentaciones PPTX nuevas en esta actualización de lecturas; se conserva el PDF suministrado como referencia de clase.

Para ejecutar la demostración Python desde la raíz de esta carpeta:

```bash
cd python/ejemplos
python3 demo.py
```

Para Java, desde la raíz de esta carpeta:

```bash
cd java/ejemplos
javac -encoding UTF-8 -d build Demo.java
java -cp build Demo
```

Los resultados de ambos deben coincidir con `salida-esperada.txt`. No se requieren paquetes externos, Maven ni Gradle.

## Incorporar al repositorio del curso

Copiar esta carpeta sobre `01/1.1-algebra-boole/`, conservando los archivos ajenos a esta actualización. El ZIP no contiene soluciones de prácticas anteriores ni cambia el catálogo global. Los títulos y anclas `concepto-1` a `concepto-4`, `demostracion`, `pc` y `esencial` se conservan, aunque ahora remiten a apartados más extensos.

El HTML incluido permite consultar esta carpeta por separado. Para integrarlo con la plantilla y navegación global del curso, ejecutar el generador del repositorio desde su raíz:

```bash
node scripts/build-site.mjs
node scripts/check-links.mjs
```

Revisar la coherencia del banco Moodle y las presentaciones anteriores antes de utilizarlos como evaluación o síntesis de este contenido ampliado. Esta actualización cambia la PC a una política con cuatro variables y prioridad del bloqueo; no modifica las PL.

## Mantener esta carpeta por separado

Editar `python/material.md` o `java/material.md`. Los bloques con marcador `example` corresponden al ejecutable de cada demostración y deben mantenerse sincronizados. Con Node.js 22 o posterior, sin instalar dependencias:

```bash
node scripts/build.mjs
python3 scripts/verify.py
```

El primer comando regenera los HTML y sobrescribe los existentes. El segundo comprueba enlaces locales, sincronización del código, leyes, pasos de las simplificaciones y demostraciones. Requiere Python y un JDK. Las fuentes DejaVu Sans y su licencia están en `assets/fonts/`.

[Notas docentes y correspondencia](doc.md) · [Registro de verificación](VERIFICACION.md)
