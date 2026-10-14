# Programación

![UPS · Carrera de Computación](../../../assets/logos/ups-computacion.png)

## 3.04 · Repetición, contadores y acumuladores · Python

**Autor:** Ing. Pablo Torres, Mgtr.  
**Unidad 3:** Lenguaje de Programación  


[Índice del curso](../../../README.md) · [Versión Java](../java/material.md) [Anterior](../../3.03-estructuras-control/python/material.md) · [Siguiente](../../3.05-funciones/python/material.md)

[Conceptos](#concepto-1) · [Demostración](#demostracion) · [Práctica de clase](#pc) · [Lo esencial](#esencial)

**Contexto.** Resumir varias mediciones requiere repetir la misma regla sin duplicar instrucciones. Diseñar el estado que debe conservarse entre iteraciones y demostrar que el ciclo termina.

**Prerrequisitos.** Decisiones, booleanos y validación.

## 1. Conceptos y ejemplos

<a id="concepto-1"></a>

### 1.1. Repetición contada con for

Usar una repetición contada cuando el número de pasos se conoce o cuando se recorre una secuencia finita. Separar el número de iteraciones de los valores que toma el contador. Para sumar desde 1 hasta n, incluir n es una decisión del contrato. Probar n igual a cero y a uno para descubrir límites incorrectos.

**Aplicar en Python.** range(inicio, fin, paso) excluye fin. range(1, 6) produce 1 a 5. Un paso negativo permite descender y cero es inválido. for toma sucesivamente valores del iterable; modificar su variable no altera la secuencia de range.

```python
for numero in range(1, 6):
    print(numero)
```

<a id="concepto-2"></a>

### 1.2. Repetición condicionada con while

Usar while cuando la continuidad depende del estado. El cuerpo puede ejecutarse cero veces. Identificar una cantidad que progrese hacia la terminación. Un centinela termina la lectura y no debe procesarse como dato. Un menú repite hasta una opción de salida, pero cada opción inválida también debe permitir una nueva entrada.

**Aplicar en Python.** Actualizar el estado antes de regresar a la condición. break termina el ciclo más interno. continue salta a la siguiente iteración y puede omitir una actualización si se coloca mal. Preferir una estructura clara antes de introducir saltos.

```python
restantes = 3
while restantes > 0:
    print(restantes)
    restantes -= 1
```

<a id="concepto-3"></a>

### 1.3. Contar, acumular y mantener invariantes

Un contador aumenta por cada dato que cumple una condición. Un acumulador combina magnitudes. Definir qué representa después de k iteraciones: por ejemplo, total es la suma de los primeros k datos. Esta afirmación es un invariante útil para revisar el algoritmo. Calcular un promedio solo si la cantidad es positiva. No reiniciar el acumulador dentro del ciclo si debe conservar el historial.

**Aplicar en Python.** Inicializar cantidad=0 y total=0 antes del ciclo. Para máximos con datos negativos, no inicializar máximo en cero sin justificación: usar el primer dato válido o un estado que indique ausencia de datos.

```python
total = 0
for numero in range(1, 5):
    total += numero
print(total)
```

<a id="concepto-4"></a>

### 1.4. Anidamiento, costo y pruebas

En ciclos anidados, cada iteración externa inicia un recorrido interno. Si existen f filas y c columnas, se realizan f por c visitas cuando ambos límites son fijos. Restablecer los acumuladores por fila dentro del ciclo externo y los globales antes de ambos. Una traza pequeña de dos por tres elementos revela el orden de recorrido sin producir una salida excesiva.

**Aplicar en Python.** Indentar cada bloque y usar nombres como fila y columna. Evitar reutilizar la misma variable para ambos for. Una comprensión no sustituye la necesidad de comprender el recorrido explícito.

```python
for fila in range(2):
    for columna in range(3):
        print(fila, columna)
```

Los bloques breves anteriores ilustran una operación y pueden requerir variables o imports del contexto. Utilizar la demostración siguiente como programa completo.


### Síntesis visual

![Infografía técnica del tema](../assets/infografia.svg)

<a id="demostracion"></a>

## 2. Demostración guiada

**Problema.** Contar y sumar los enteros pares del intervalo de 1 a 10 inclusive.

**Contrato de esta demostración.** Recorrer los diez enteros una vez, iniciar cantidad y total en cero y actualizar solo ante paridad. Producir cantidad 5 y suma 30. No almacenar los valores en una lista.

**Fuente:** [ejemplos/demo.py](ejemplos/demo.py).

<!-- example: demo.py -->
```python
total = 0
cantidad = 0
for numero in range(1, 11):
    if numero % 2 == 0:
        total += numero
        cantidad += 1
print(f"Cantidad: {cantidad}")
print(f"Suma: {total}")
```

### Ejecutar

Abrir una terminal dentro de `03/3.04-iteracion/python/ejemplos/` y ejecutar:

```bash
python3 demo.py
```

En Windows, usar `py` en lugar de `python3` si esa es la instalación disponible. Comprobar primero su versión.

### Salida esperada

```text
Cantidad: 5
Suma: 30
```

**Interpretación.** Seguir las asignaciones y los bloques en orden, identificar qué instrucción produce cada línea y contrastar con el contrato. Modificar un dato por vez y anticipar el resultado antes de ejecutar. La salida de referencia es una expectativa; el registro de verificaciones indica qué ejecuciones se realizaron.

<a id="ejercicios"></a>

### Ejercicios prácticos progresivos

Resolver los siguientes ejercicios en orden. Entregar enunciado, fuente y resultado propio. Los casos mostrados permiten comprobar el contrato y no sustituyen una prueba adicional de frontera.

#### Ejercicio 01. Secuencia ascendente

Mostrar enteros de 1 a 5, uno por línea.

**Caso de comprobación:**

```text
1
2
3
4
5
```

#### Ejercicio 02. Secuencia descendente

Mostrar 5, 3 y 1 mediante un ciclo.

**Caso de comprobación:**

```text
5
3
1
```

#### Ejercicio 03. Suma hasta n

Sumar enteros de 1 a n para n=10. Admitir n=0 con suma cero.

**Caso de comprobación:**

```text
55
```

#### Ejercicio 04. Contar múltiplos

Contar múltiplos de 3 entre 1 y 20 inclusive.

**Caso de comprobación:**

```text
6
```

#### Ejercicio 05. Factorial

Calcular 5! mediante ciclo. Definir 0!=1 y rechazar negativos en el diseño.

**Caso de comprobación:**

```text
120
```

#### Ejercicio 06. Suma de dígitos

Sumar los dígitos del entero no negativo 4072 utilizando división entera y residuo.

**Caso de comprobación:**

```text
13
```

#### Ejercicio 07. Potencia por repetición

Calcular 3 elevado a 4 sin operador de potencia ni bibliotecas. Aceptar exponente no negativo.

**Caso de comprobación:**

```text
81
```

#### Ejercicio 08. Número primo

Determinar si 29 es primo mediante divisores. Tratar n<2 como no primo.

**Caso de comprobación:**

```text
Primo
```

#### Ejercicio 09. Patrón triangular

Mostrar tres filas de asteriscos: uno, dos y tres, usando ciclos anidados.

**Caso de comprobación:**

```text
*
**
***
```

#### Ejercicio 10. Lectura con centinela

Procesar 4, -2, 6 y -1. Finalizar con -1, rechazar otros negativos y mostrar cantidad y suma de los aceptados. Usar while y lectura simulada.

**Caso de comprobación:**

```text
2 10
```

<a id="pc"></a>

## 3. PC3.04 · Práctica de clase

Leer temperaturas enteras entre -20 y 50 hasta recibir 999. Rechazar datos fuera de rango sin contarlos. Mostrar cantidad, mínimo, máximo y promedio con dos decimales. Si no existen datos, mostrar “Sin datos”. Recuperarse de entradas no numéricas y no usar listas para resolver este ejercicio.

### Requisitos y restricciones

- Resolver en una sola versión, Python o Java.
- Mantener nombres y responsabilidades indicados; explicar cualquier adaptación idiomática.
- Aplicar únicamente los conceptos ya introducidos.
- Conservar las entradas cuando el enunciado lo exija.
- Distinguir valores fuera de contrato de errores que el programa debe gestionar.

### Casos de aceptación de la PC

| Entrada / escenario | Resultado esperado |
|---|---|
| 10, 20, 999 | cantidad 2; mínimo 10; máximo 20; promedio 15.00 |
| 999 | Sin datos |
| -30, -10, 999 | rechazar -30; promedio -10.00 |
| abc, 0, 999 | rechazar abc; promedio 0.00 |

### Probar y registrar evidencia

Crear una carpeta personal `PC3.04` separada de las demostraciones. Guardar cada caso con entrada, resultado esperado y resultado real. Ejecutar `python3 solucion.py` desde esa carpeta. Para entradas de teclado, guardar `casos/entrada-01.txt` y redirigirla con `< casos/entrada-01.txt`. Para funciones, crear llamadas con los datos de la tabla.

- Registrar `evidencias/PC3.04.md` con comandos, versión real, salidas y explicación.
- Crear un commit funcional como `feat(pc3.04): implementar-regla-principal`.
- Obtener el hash real con `git rev-parse HEAD` y anotarlo en la evidencia.
- Revisar el cambio con `git show HASH` y comparar avances con `git diff HASH_ANTERIOR HASH_ACTUAL`. Sustituir los marcadores por hashes reales.
- Agregar una prueba de frontera distinta de las incluidas y justificar qué error detectaría.

No se requiere proyecto acumulativo ni rúbrica individual de esta PC.

<a id="esencial"></a>

## Lo esencial

- Inicializar estado antes del ciclo.
- Excluir el centinela del procesamiento.
- Justificar terminación y límites.

## Referencias técnicas

- [Tutorial oficial de Python](https://docs.python.org/3.14/tutorial/)
- [Biblioteca estándar de Python](https://docs.python.org/3.14/library/)

[Índice del curso](../../../README.md) · [Versión Java](../java/material.md) [Anterior](../../3.03-estructuras-control/python/material.md) · [Siguiente](../../3.05-funciones/python/material.md)
