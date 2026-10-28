# Programación

![UPS · Carrera de Computación](../../../assets/logos/ups-computacion.png)

## 3.11 · Archivos de texto y persistencia · Python

**Autor:** Ing. Pablo Torres, Mgtr.  
**Unidad 3:** Lenguaje de Programación  


 [Anterior](../../3.10-tuplas/python/material.md) · [Siguiente](../../3.12-main-modulos/python/material.md)

[Conceptos](#concepto-1) · [Demostración](#demostracion) · [Práctica de clase](#pc) · [Lo esencial](#esencial)

**Contexto.** Guardar mediciones permite continuar el análisis después de terminar el programa. Un archivo agrega decisiones sobre ruta, codificación, formato, errores y cierre de recursos.

**Prerrequisitos.** Funciones, cadenas, listas y excepciones.

## 1. Conceptos y ejemplos

<a id="concepto-1"></a>

### 1.1. Ruta, formato y codificación

Una ruta relativa se interpreta desde el directorio de trabajo del proceso, que no siempre coincide con la carpeta del código. Especificar cómo localizar los datos y usar UTF-8 para intercambiar texto con tildes. El formato describe cómo se separan registros y campos. Una extensión .txt no garantiza contenido válido. No confundir bytes con caracteres.

**Aplicar en Python.** pathlib.Path representa rutas de manera portable. Path(__file__).resolve().parent localiza la carpeta del script; __file__ no está disponible en una celda de notebook. Definir una ruta base explícita para cada contexto.

```python
from pathlib import Path
ruta = Path("mediciones.txt")
```

<a id="concepto-2"></a>

### 1.2. Lectura y cierre de recursos

Abrir un archivo adquiere un recurso que debe cerrarse aunque ocurra un error. Leer línea por línea permite procesar sin cargar todo el archivo. Una línea vacía requiere una política: ignorar, aceptar como dato o rechazar. Validar cada conversión y conservar número de línea para producir diagnósticos útiles.

**Aplicar en Python.** Usar with ruta.open(encoding="utf-8") as archivo. strip elimina espacios de extremos y el salto final, pero también espacios que podrían ser datos significativos. Usarlo solo si el formato permite ignorarlos.

```python
with open("mediciones.txt", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.rstrip("\n"))
```

<a id="concepto-3"></a>

### 1.3. Escritura, anexado y seguridad del resultado

Escribir puede reemplazar datos existentes. Distinguir crear, sobrescribir y anexar. Decidir si la nueva salida debe construirse completamente antes de sustituir la anterior. Nunca escribir sobre el archivo de entrada por accidente. En ejercicios reproducibles, utilizar una carpeta temporal o una ruta de salida controlada y comparar el contenido final.

**Aplicar en Python.** El modo w trunca, a agrega y x falla si el archivo ya existe. Escribir saltos de línea explícitos. with garantiza cierre, no una transacción atómica. Una actualización robusta puede escribir temporalmente y reemplazar al finalizar.

```python
with open("salida.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Total: 12\n")
```

<a id="concepto-4"></a>

### 1.4. Validación de registros y errores

Separar errores del sistema de errores del contenido. Un archivo inexistente no equivale a un archivo vacío; una línea inválida no equivale a cero. Registrar qué filas se rechazaron y por qué. Para un CSV real, las comas entre comillas requieren un parser; split(",") solo sirve cuando el formato restringe explícitamente las comas dentro de campos.

**Aplicar en Python.** Capturar FileNotFoundError u OSError donde se pueda responder. La biblioteca estándar csv procesa CSV con comillas. No usar except: pass porque elimina evidencia de pérdida de datos.

```python
try:
    valor = int("dato")
except ValueError:
    print("Línea inválida")
```

Los bloques breves anteriores ilustran una operación y pueden requerir variables o imports del contexto. Utilizar la demostración siguiente como programa completo.


### Síntesis visual

![Infografía técnica del tema](../assets/infografia.svg)

<a id="demostracion"></a>

## 2. Demostración guiada

**Problema.** Crear un archivo temporal con mediciones 12, 8 y 15, leerlo y sumar sus valores.

**Contrato de esta demostración.** Usar UTF-8 y un entero válido por línea. Escribir y leer dentro de una carpeta temporal controlada, cerrar recursos y eliminar temporales al terminar. No modificar archivos del usuario. Mostrar Total: 35. La PC añade validación de líneas externas.

**Fuente:** [ejemplos/demo.py](ejemplos/demo.py).

<!-- example: demo.py -->
```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as carpeta:
    ruta = Path(carpeta) / "mediciones.txt"
    ruta.write_text("12\n8\n15\n", encoding="utf-8")
    total = 0
    with ruta.open(encoding="utf-8") as archivo:
        for linea in archivo:
            total += int(linea.strip())
    print(f"Total: {total}")
```

### Ejecutar

Abrir una terminal dentro de `03/3.11-archivos/python/ejemplos/` y ejecutar:

```bash
python3 demo.py
```

En Windows, usar `py` en lugar de `python3` si esa es la instalación disponible. Comprobar primero su versión.

### Salida esperada

```text
Total: 35
```

**Interpretación.** Seguir las asignaciones y los bloques en orden, identificar qué instrucción produce cada línea y contrastar con el contrato. Modificar un dato por vez y anticipar el resultado antes de ejecutar. La salida de referencia es una expectativa; el registro de verificaciones indica qué ejecuciones se realizaron.

<a id="ejercicios"></a>

### Ejercicios prácticos progresivos

Resolver los siguientes ejercicios en orden. Entregar enunciado, fuente y resultado propio. Los casos mostrados permiten comprobar el contrato y no sustituyen una prueba adicional de frontera.

#### Ejercicio 01. Escritura UTF-8

Escribir “Cuenca” en un archivo temporal UTF-8 y leerlo de nuevo.

**Caso de comprobación:**

```text
Cuenca
```

#### Ejercicio 02. Dos líneas

Guardar y leer dos líneas: sol y luna. Conservar un salto final.

**Caso de comprobación:**

```text
sol
luna
```

#### Ejercicio 03. Anexado

Crear una línea A y anexar B sin eliminar A.

**Caso de comprobación:**

```text
A
B
```

#### Ejercicio 04. Contar líneas no vacías

Contar líneas con texto en “a”, vacía y “b”. Ignorar espacios externos.

**Caso de comprobación:**

```text
2
```

#### Ejercicio 05. Suma de archivo

Leer enteros 4, 8 y 3, uno por línea, y mostrar suma.

**Caso de comprobación:**

```text
15
```

#### Ejercicio 06. Archivo inexistente

Intentar leer ausente.txt dentro de una carpeta temporal y producir mensaje controlado.

**Caso de comprobación:**

```text
Archivo no encontrado
```

#### Ejercicio 07. Errores por línea

Leer 4, x y 6. Sumar válidos y registrar número de línea inválida.

**Caso de comprobación:**

```text
Línea 2: inválida
Total: 10
```

#### Ejercicio 08. Filtrar a otro archivo

Leer 2, 7, 4 y escribir solo valores mayores que 3 en un archivo nuevo. Conservar entrada.

**Caso de comprobación:**

```text
7
4
```

#### Ejercicio 09. Promedio sin datos

Leer archivo vacío y mostrar “Sin datos” sin dividir por cero.

**Caso de comprobación:**

```text
Sin datos
```

#### Ejercicio 10. Registros delimitados

Leer A;3 y B;5. Exigir exactamente dos campos, código no vacío y cantidad entera no negativa. Mostrar suma y conservar número de línea en errores. El formato no permite ; dentro de campos.

**Caso de comprobación:**

```text
8
```

<a id="pc"></a>

## 3. PC3.11 · Práctica de clase

Leer un archivo UTF-8 con un entero por línea. Ignorar líneas vacías, aceptar valores de 0 a 100 y registrar número de línea y causa de cada rechazo. Escribir un informe nuevo con cantidad válida y promedio; usar “Sin datos” cuando no haya valores válidos. Conservar el archivo de entrada y gestionar archivo inexistente.

### Requisitos y restricciones

- Resolver en una sola versión, Python o Java.
- Mantener nombres y responsabilidades indicados; explicar cualquier adaptación idiomática.
- Aplicar únicamente los conceptos ya introducidos.
- Conservar las entradas cuando el enunciado lo exija.
- Distinguir valores fuera de contrato de errores que el programa debe gestionar.

### Casos de aceptación de la PC

| Entrada / escenario | Resultado esperado |
|---|---|
| 10<br>20<br> | cantidad 2; promedio 15.00 |
| abc<br>120<br>5<br> | rechazos en líneas 1 y 2; promedio 5.00 |
| archivo vacío | Sin datos |
| ruta inexistente | mensaje de archivo no encontrado |

### Probar y registrar evidencia

Crear una carpeta personal `PC3.11` separada de las demostraciones. Guardar cada caso con entrada, resultado esperado y resultado real. Ejecutar `python3 solucion.py` desde esa carpeta. Para entradas de teclado, guardar `casos/entrada-01.txt` y redirigirla con `< casos/entrada-01.txt`. Para funciones, crear llamadas con los datos de la tabla.

- Registrar `evidencias/PC3.11.md` con comandos, versión real, salidas y explicación.
- Crear un commit funcional como `feat(pc3.11): implementar-regla-principal`.
- Obtener el hash real con `git rev-parse HEAD` y anotarlo en la evidencia.
- Revisar el cambio con `git show HASH` y comparar avances con `git diff HASH_ANTERIOR HASH_ACTUAL`. Sustituir los marcadores por hashes reales.
- Agregar una prueba de frontera distinta de las incluidas y justificar qué error detectaría.

No se requiere proyecto acumulativo ni rúbrica individual de esta PC.

<a id="esencial"></a>

## Lo esencial

- Fijar ruta, codificación y formato.
- Cerrar recursos incluso ante errores.
- Distinguir dato inválido de fallo de archivo.

## Referencias técnicas

- [Tutorial oficial de Python](https://docs.python.org/3.14/tutorial/)
- [Biblioteca estándar de Python](https://docs.python.org/3.14/library/)

 [Anterior](../../3.10-tuplas/python/material.md) · [Siguiente](../../3.12-main-modulos/python/material.md)
