# Documento docente · 1.1 · Álgebra de Boole

## Fuentes y alcance

El programa analítico de Programación leído para la entrega general identifica la Unidad 1 «Lógica Matemática», con 30 horas oficiales, en la página 2. Incluye Álgebra de Boole y Teoría de proposiciones. No establece horas por subtema ni códigos de subtema; 1.1 es numeración editorial. Esta actualización mantiene un único segmento y concentra las proposiciones necesarias dentro de las variables booleanas. Las 30 horas se registran como dato oficial, no como una propuesta de duración de esta lectura.

Resultado oficial: «Diseña soluciones a problemas de lógica empleando álgebra de Boole y teoría de proposiciones.»

Indicador oficial: «Aplica lógica matemática para resolver problemas.»



## Correspondencia docente

| Apartado exacto del material Python | Aporte al resultado | Indicador | Evidencia observable |
|---|---|---|---|
| [1. Variables booleanas y expresiones](python/material.md#concepto-1) | Identificar el dominio y formular condiciones; aporte conceptual parcial | Aplica lógica matemática para resolver problemas | Define variables sin ambigüedad y enumera todas las combinaciones |
| [2. Operadores lógicos](python/material.md#concepto-2) | Elegir operaciones acordes con un requisito | Mismo indicador oficial | Distingue OR, XOR y XNOR mediante filas que separan sus resultados |
| [3. Aplicaciones generales del álgebra de Boole](python/material.md#concepto-3) | Traducir decisiones verbales a expresiones | Mismo indicador oficial | Explica el alcance de una condición de bloqueo y sus paréntesis |
| [4. Leyes del álgebra de Boole](python/material.md#concepto-4) | Justificar transformaciones equivalentes | Mismo indicador oficial | Identifica la subexpresión y la ley aplicable; evita cancelar términos indebidamente |
| [5. Simplificación de expresiones: dos ejemplos resueltos](python/material.md#demostracion) | Modelar una derivación y contrastarla exhaustivamente; lectura guiada, no evidencia suficiente de autonomía | Mismo indicador oficial | Explica cada paso y relaciona la tabla con las dos expresiones |
| [6. Práctica: aplicación de leyes y simplificación](python/material.md#pc) | Evaluar transferencia y resolución autónoma | Mismo indicador oficial | Presenta desarrollo justificado, contraejemplos, tabla completa y defensa de PC1.1 |

Java conserva los mismos problemas y evidencias, con operadores y estructura de ejecución propios. No se añaden resultados ni indicadores oficiales nuevos. El dominio de ciclos no se evalúa en esta unidad: el enumerador se suministra como herramienta de contraste.

## Precisiones editoriales

- La definición de complemento de las páginas 16 y 30 llama «neutro» al resultado. Se corrige a valores absorbentes: OR con el complemento produce 1; AND produce 0. Los neutros son 0 para OR y 1 para AND.
- La segunda identidad de De Morgan de la tabla de la página 30 conserva AND en el lado derecho. Se corrige a ¬(A·B) = ¬A + ¬B, coherente con la explicación de la página 21.
- En el ejemplo de absorción de la página 25 se conserva la evaluación correcta de 0·(0 + 1): el paréntesis vale 1. El resultado final sigue siendo 0.
- Se escriben todas las negaciones con ¬ y agrupaciones explícitas, evitando pérdida de barras en la extracción del PDF.
- «XAND» se interpreta como XNOR, nombre estándar de la equivalencia booleana; se distingue de NAND. Se añade como complemento conceptual solicitado.
- Se desarrolla A + ¬A·B = A + B mediante distributiva, complemento e identidad, sin confundirla con la absorción básica A + A·B = A.
- La PC ahora utiliza cuatro variables e incorpora bloqueo prioritario. Los casos parciales no sustituyen las 16 filas requeridas. No se publica su solución.

## Uso y mantenimiento

Los documentos MD son lecturas ampliadas. El PDF permanece como referencia original, sin modificaciones; por ello conserva las imprecisiones que se corrigen aquí. No se han generado PPTX ni actualizado bancos de evaluación con este paquete. Al integrarlo en el curso, revisar esos recursos según la nueva secuencia. El contenido estudiantil no incorpora resultados de aprendizaje ni tablas curriculares.
