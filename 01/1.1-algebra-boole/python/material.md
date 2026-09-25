# Programación

## 1.1 · Álgebra de Boole · Python

**Autor:** Ing. Pablo Torres, Mgtr.  
**Unidad 1:** Lógica Matemática  
**Institución:** Universidad Politécnica Salesiana · Computación · Cuenca

[Índice del curso](../../../README.md) · [Versión Java](../java/material.md) · [Presentación](../presentacion.pptx) · [Siguiente](../../../02/2.1-algoritmos/python/material.md)

[Conceptos](#concepto-1) · [Demostración](#demostracion) · [Práctica de clase](#pc) · [Lo esencial](#esencial)

**Contexto.** Determinar cuándo permitir el acceso a una sala: disponer de credencial y reserva, o tener autorización del responsable. Convertir una regla verbal en una expresión permite revisar todos los casos, incluidos los que parecen excepcionales.

**Prerrequisitos.** Operaciones aritméticas y lectura de condiciones.

## 1. Conceptos y ejemplos

<a id="concepto-1"></a>

### 1.1. Proposiciones y valores de verdad

Una proposición es un enunciado al que se puede asignar verdadero o falso dentro de un contexto definido. “La reserva está vigente” requiere especificar fecha y hora; una pregunta o una orden no es una proposición. Representar cada condición mediante una letra y escribir su significado antes de operar. Una variable booleana solo modela dos estados, por lo que un dato desconocido exige una decisión explícita del problema. No confundir falso con información ausente.

**Aplicar en Python.** Usar bool y los literales True y False. Aunque Python acepta otros objetos como condiciones, emplear booleanos explícitos al construir tablas. La cadena "False" no es el valor False: cualquier cadena no vacía tiene valor de verdad verdadero.

```python
reserva = True
credencial = False
print(reserva)
```

<a id="concepto-2"></a>

### 1.2. Negación, conjunción y disyunción

La negación invierte un valor. La conjunción exige que ambas proposiciones sean verdaderas. La disyunción inclusiva permite que una o ambas sean verdaderas. Interpretar “o” en lenguaje cotidiano puede ser ambiguo: si exactamente una opción es válida, se necesita disyunción exclusiva. Construir una tabla con 2 elevado al número de variables para enumerar todas las combinaciones sin omisiones.

**Aplicar en Python.** Escribir not, and y or. Con operandos booleanos producen los resultados esperados de la tabla. and y or pueden devolver operandos cuando se aplican a otros tipos; por eso mantener bool en este segmento.

```python
p, q = True, False
print(p and q, p or q, not p)
```

<a id="concepto-3"></a>

### 1.3. Equivalencia y leyes de De Morgan

Dos expresiones son equivalentes cuando coinciden para todas las asignaciones de sus variables. Una coincidencia aislada no demuestra equivalencia. Las leyes de De Morgan establecen que negar una conjunción equivale a disyuntar las negaciones, y negar una disyunción equivale a conjuntarlas. También se cumplen identidad, idempotencia, absorción y distributividad. Simplificar conserva el significado, no los pasos concretos de evaluación.

**Aplicar en Python.** Comparar not (p and q) con (not p) or (not q). Encerrar las condiciones compuestas entre paréntesis al enseñar su traducción. La igualdad == compara resultados y no debe confundirse con la asignación =.

```python
p, q = True, False
print(not (p and q) == ((not p) or (not q)))
```

<a id="concepto-4"></a>

### 1.4. Reglas, implicación y comprobación

La implicación p implica q solo es falsa cuando p es verdadera y q falsa. No expresa por sí misma una causa. Se puede reescribir como no p o q. Una tautología siempre es verdadera; una contradicción siempre es falsa; una contingencia depende de los valores. Para validar una regla de acceso, comprobar cada fila y explicar las filas que autorizan. Diferenciar la especificación de la política y su traducción al programa.

**Aplicar en Python.** Expresar una implicación como (not p) or q. En la demostración, observar los bucles únicamente como herramienta para enumerar casos; su construcción se desarrollará en las unidades siguientes.

```python
p, q = True, False
print((not p) or q)
```

Los bloques breves anteriores ilustran una operación y pueden requerir variables o imports del contexto. Utilizar la demostración siguiente como programa completo.

### Tabla de operadores

| p | q | p AND q | p OR q | NOT p |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 |

### Leyes para simplificar

| Ley | Equivalencia |
|---|---|
| Identidad | p AND 1 = p; p OR 0 = p |
| Idempotencia | p AND p = p; p OR p = p |
| Complemento | p AND NOT p = 0; p OR NOT p = 1 |
| Absorción | p OR (p AND q) = p |
| Distributiva | p AND (q OR r) = (p AND q) OR (p AND r) |
| De Morgan | NOT (p OR q) = NOT p AND NOT q |

### Síntesis visual

![Infografía técnica del tema](../assets/infografia.svg)

<a id="demostracion"></a>

## 2. Demostración guiada

**Problema.** Enumerar las cuatro combinaciones de credencial y reserva y autorizar únicamente cuando ambas sean verdaderas.

**Contrato de esta demostración.** Dos valores booleanos. No incluir todavía la autorización excepcional del contexto inicial; incorporarla en la PC. Mostrar credencial, reserva y permiso como 0 o 1. La tabla debe contener cuatro filas.

**Fuente:** [ejemplos/demo.py](ejemplos/demo.py).

<!-- example: demo.py -->
```python
for credencial in (False, True):
    for reserva in (False, True):
        permitido = credencial and reserva
        print(int(credencial), int(reserva), int(permitido))
```

### Ejecutar

Abrir una terminal dentro de `01/1.1-algebra-boole/python/ejemplos/` y ejecutar:

```bash
python3 demo.py
```

En Windows, usar `py` en lugar de `python3` si esa es la instalación disponible. Comprobar primero su versión.

### Salida esperada

```text
0 0 0
0 1 0
1 0 0
1 1 1
```

**Interpretación.** Seguir las asignaciones y los bloques en orden, identificar qué instrucción produce cada línea y contrastar con el contrato. Modificar un dato por vez y anticipar el resultado antes de ejecutar. La salida de referencia es una expectativa; el registro de verificaciones indica qué ejecuciones se realizaron.

<a id="pc"></a>

## 3. PC1.1 · Práctica de clase

Formalizar la regla “permitir acceso con credencial y reserva, o con autorización del responsable”. Definir las tres proposiciones, completar las ocho filas de su tabla y expresar la negación mediante De Morgan. Usar Python o Java solo para contrastar la tabla manual, sin exigir todavía escribir bucles desde cero.

### Requisitos y restricciones

- Resolver en una sola versión, Python o Java.
- Mantener nombres y responsabilidades indicados; explicar cualquier adaptación idiomática.
- Aplicar únicamente los conceptos ya introducidos.
- Conservar las entradas cuando el enunciado lo exija.
- Distinguir valores fuera de contrato de errores que el programa debe gestionar.

### Casos de aceptación de la PC

| Entrada / escenario | Resultado esperado |
|---|---|
| 0, 0, 0 | 0 |
| 1, 1, 0 | 1 |
| 0, 0, 1 | 1 |
| 1, 0, 0 | 0 |

### Probar y registrar evidencia

Crear una carpeta personal `PC1.1` separada de las demostraciones. Guardar cada caso con entrada, resultado esperado y resultado real. Ejecutar `python3 solucion.py` desde esa carpeta. Para entradas de teclado, guardar `casos/entrada-01.txt` y redirigirla con `< casos/entrada-01.txt`. Para funciones, crear llamadas con los datos de la tabla.

- Registrar `evidencias/PC1.1.md` con comandos, versión real, salidas y explicación.
- Crear un commit funcional como `feat(pc1.1): implementar-regla-principal`.
- Obtener el hash real con `git rev-parse HEAD` y anotarlo en la evidencia.
- Revisar el cambio con `git show HASH` y comparar avances con `git diff HASH_ANTERIOR HASH_ACTUAL`. Sustituir los marcadores por hashes reales.
- Agregar una prueba de frontera distinta de las incluidas y justificar qué error detectaría.

No se requiere proyecto acumulativo ni rúbrica individual de esta PC.

<a id="esencial"></a>

## Lo esencial

- Definir cada proposición antes de operar.
- Distinguir OR inclusivo de OR exclusivo.
- Probar equivalencia sobre todas las combinaciones.

## Referencias técnicas

- [Tutorial oficial de Python](https://docs.python.org/3.14/tutorial/)
- [Biblioteca estándar de Python](https://docs.python.org/3.14/library/)

[Índice del curso](../../../README.md) · [Versión Java](../java/material.md) · [Presentación](../presentacion.pptx) · [Siguiente](../../../02/2.1-algoritmos/python/material.md)
