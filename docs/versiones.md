# Versiones y entorno

Fecha de consulta: 25 de septiembre de 2026.

| Componente | Objetivo del material | Fuente oficial |
|---|---|---|
| Python | CPython 3.14.7, versión estable de referencia | https://www.python.org/downloads/release/python-3147/ |
| Java | Java SE / JDK 27, sin características preview | https://docs.oracle.com/en/java/javase/27/docs/specs/jvms27.pdf |
| Node.js | >=22, módulos ESM | Requisito heredado del generador del paquete base |

La página oficial de Python 3.14.7 identifica una publicación de mantenimiento del 5 de agosto de 2026. La documentación Java SE 27 consultada identifica edición final de septiembre de 2026. Fijar estas versiones objetivo en lugar de cambiar silenciosamente a versiones preliminares. Para instalaciones Java reproducibles, registrar además proveedor y build real mediante `java --version`.

## Entorno realmente ejecutado

Las demostraciones se comprobaron con CPython 3.12.14 y OpenJDK 17.0.20, disponibles en el entorno de producción del material. El código utiliza un subconjunto compatible sin características exclusivas recientes. Esto no equivale a haber ejecutado las pruebas en CPython 3.14.7 o JDK 27. Repetir `python3 scripts/verify-material.py` en las instalaciones objetivo para cerrar esa comprobación.

El compilador Java disponible se invocó con `java com.sun.tools.javac.Main`; es el compilador del JDK, aunque el ejecutable `javac` no estaba expuesto en PATH. En una instalación normal, utilizar `javac` como indican las lecturas. Node.js de verificación: 24.19.0.

## Dependencias

No instalar librerías externas para demostraciones Python o Java. No usar Maven, Gradle, bases de datos ni hardware. Crear un entorno virtual Python solo como ejercicio de aislamiento. El generador HTML incluye su parser Markdown y licencia. Las presentaciones editables no se regeneran mediante ese parser.

## Instalación mínima

Instalar Python desde python.org o un JDK desde un proveedor oficial. Comprobar `python3 --version`, `java --version` y `javac --version`. Elegir el mismo runtime en el editor. No copiar rutas privadas entre equipos. Consultar 3.01 para la primera ejecución y 3.13 para reproducibilidad.
