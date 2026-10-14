# Programación

## 1.1 · Álgebra de Boole · Python

**Autor:** Ing. Pablo Torres, Mgtr.  
**Unidad 1:** Lógica Matemática  
**Institución:** Universidad Politécnica Salesiana · Computación · Cuenca

[Versión Java](../java/material.md)

[Índice del tema](../README.md) 


- [Variables](#concepto-1) 
- [Operadores](#concepto-2) 
- [Aplicaciones](#concepto-3) 
- [Leyes](#concepto-4) 
- [Simplificaciones resueltas](#demostracion) 
- [Práctica](#pc) 
- [Lo esencial](#esencial)

Este material desarrolla la teoría necesaria para estudiar el tema de forma autónoma. La presentación sirve como síntesis para la clase; aquí se explican la formulación, las decisiones de modelado y la justificación de cada transformación. Las aplicaciones iniciales contextualizan las leyes y los ejercicios finales permiten practicarlas.

**Prerrequisitos:** operaciones aritméticas elementales, lectura de expresiones y reconocimiento de relaciones como mayor que o igual a. No se requiere dominar ciclos ni funciones. Los programas completos de comprobación ya incluyen la estructura de ejecución necesaria.

<a id="concepto-1"></a>

## 1. Variables booleanas y expresiones

### 1.1. Qué representa una variable booleana

Una variable booleana representa una condición con dos valores posibles: **verdadero** o **falso**. En álgebra de Boole se escriben como **1** y **0**. Por ejemplo, A puede significar «la credencial está vigente». A = 1 indica que la condición se cumple; A = 0 indica que no se cumple. Antes de operar, se debe fijar el significado de cada letra.

Una proposición es un enunciado al que se puede asignar un valor de verdad en un contexto definido. «La temperatura supera 30 °C» es una proposición si se conoce la medición y su unidad. «¿Cuál es la temperatura?» es una pregunta y «registre la temperatura» es una orden: ninguna afirma algo verdadero o falso.

Un valor desconocido no es automáticamente falso. Si no se ha consultado la vigencia de una credencial, falta información para evaluar A. El problema debe indicar si se espera el dato, se informa un error o se deniega el acceso por una política explícita. El modelo de este tema supone condiciones conocidas y exclusivamente booleanas.

| Representación conceptual | Interpretación | Valor que se guarda |
|---|---|---|
| A ← verdadero | Asignación directa de una constante | Verdadero |
| A ← falso | Asignación directa de una constante | Falso |
| A ← número > 10 | Evaluar una comparación y guardar su resultado | Depende de número |
| A ← B AND C | Evaluar una combinación de condiciones | Verdadero solo si B y C son verdaderas |

### 1.2. Asignar, comparar y formular una identidad

En un programa, `=` realiza una **asignación**: primero se evalúa la derecha y después se guarda su resultado en la variable de la izquierda. No afirma una igualdad matemática que deba mantenerse para siempre. En cambio, `==` compara dos valores. En las fórmulas de este material, `=` indica que dos expresiones booleanas tienen el mismo valor para todas las combinaciones posibles.

Asignar `A = numero > 10` guarda un resultado booleano, no el número ni una regla que se actualiza sola. Si después cambia `numero`, es necesario volver a evaluar la comparación para actualizar A. Para número = 10, «mayor que 10» es falso; no debe confundirse `>` con `>=`.

**En Python**, los literales son `True` y `False`, con mayúscula inicial. El tipo es `bool`. El nombre A se utiliza aquí para vincular el código con las fórmulas; en una aplicación convienen nombres descriptivos como `credencial_vigente`.

```python
A = True
print(A)              # True
A = False
print(A)              # False
numero = 12
A = numero > 10
print(A)              # True
B = True
C = False
A = B and C
print(A)              # False
```

La comparación devuelve un booleano. En cambio, asignar el texto `"false"` o `"False"` no equivale a guardar el valor lógico falso.

### 1.3. Combinaciones posibles y tablas de verdad

Una tabla de verdad enumera todas las asignaciones posibles a las variables y calcula la salida para cada una. Con n variables booleanas independientes hay **2ⁿ combinaciones**, porque cada variable permite dos elecciones. Para tres variables: 2 × 2 × 2 = 8. Independientes significa aquí que no se han impuesto restricciones que excluyan filas; una política del mundo real podría hacer que algunas combinaciones no sean alcanzables, pero la identidad algebraica se estudia sobre todas.

| A | B | C |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |
| 1 | 1 | 1 |

Este orden coincide con contar en binario de 000 a 111. C cambia en cada fila; B, cada dos; A, cada cuatro. El orden facilita detectar omisiones, aunque otro orden también es válido si incluye todas las combinaciones una sola vez. Una fila aislada comprueba un caso; no demuestra una equivalencia general.

### 1.4. Convención de escritura

Usaremos **¬A** para la negación, **A·B** para AND y **A + B** para OR. A′ o una barra sobre A también representan negación; para evitar perder barras al copiar fórmulas, aquí se prefiere ¬. Los paréntesis delimitan el alcance de cada operación: ¬(A + B) niega toda la disyunción, mientras que ¬A + B solo niega A.

El signo + en estas fórmulas **no representa suma aritmética**: 1 + 1 = 1 en OR. Del mismo modo, simplificar una expresión booleana no permite aplicar reglas aritméticas como A + A = 2A, cancelar sumandos o dividir entre variables. Las leyes se justifican por los dos valores del dominio booleano.

<a id="concepto-2"></a>

## 2. Operadores lógicos

### 2.1. AND: conjunción

**A·B** es verdadero únicamente si A y B son verdaderas. Modela requisitos simultáneos: «tener credencial vigente **y** reserva activa». Basta un requisito falso para que la conjunción sea falsa. Si uno es verdadero, la decisión queda determinada por el otro.

### 2.2. OR: disyunción inclusiva

**A + B** es verdadero si al menos un operando es verdadero. También es verdadero cuando ambos lo son. Modela alternativas compatibles: «tener autorización del docente **o** del coordinador». Si la regla dice que no se pueden cumplir ambas opciones, OR inclusivo no expresa esa restricción.

### 2.3. NOT: negación

**¬A** invierte el valor: verdadero pasa a falso y falso a verdadero. Es un operador unario, porque recibe una sola condición. «No tiene bloqueo» se modela como ¬B si B significa «tiene bloqueo». Definir B como «sin bloqueo» y volver a negarlo expresaría la condición opuesta.

| A | ¬A |
|---|---|
| 0 | 1 |
| 1 | 0 |

### 2.4. XOR: disyunción exclusiva

**A ⊕ B** es verdadero cuando los dos valores son diferentes: exactamente uno es verdadero. Su formulación con operaciones básicas es **A·¬B + ¬A·B**. Ejemplo: un formulario admite seleccionar exactamente una de dos modalidades; ninguna o ambas seleccionadas son casos inválidos.

Con dos operandos, XOR significa «exactamente uno». Una cadena de XOR con tres o más operandos determina paridad impar, no necesariamente «solo uno». Por ejemplo, 1 XOR 1 XOR 1 = 1. La exclusividad entre muchas opciones requiere otra formulación.

### 2.5. XNOR: equivalencia booleana

**¬(A ⊕ B)** es verdadero cuando ambos operandos tienen el mismo valor. También se escribe **A ↔ B** y equivale a **A·B + ¬A·¬B**. Se utiliza para comprobar coincidencia entre dos señales o estados. Coincidir no significa que ambos sean verdaderos: dos valores falsos también coinciden.

En algunas explicaciones aparece el nombre «XAND». En este material se interpreta como XNOR y se utiliza la denominación **XNOR o equivalencia**, porque «XAND» no es un operador incorporado de Python ni de Java y puede resultar ambiguo. No debe confundirse con NAND, que niega AND.

### 2.6. NAND y NOR como operaciones derivadas

NAND es **¬(A·B)**: solo es falso cuando ambos operandos son verdaderos. NOR es **¬(A + B)**: solo es verdadero cuando ambos son falsos. Se obtienen combinando NOT con AND u OR; no requieren agregar nuevas reglas al sistema. En circuitos digitales se implementan como compuertas específicas.

| A | B | AND A·B | OR A + B | XOR A ⊕ B | XNOR ¬(A ⊕ B) | NAND ¬(A·B) | NOR ¬(A + B) |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 |

### 2.7. Agrupación y orden de evaluación

En fórmulas que usan solo NOT, AND y OR, la prioridad convencional es: paréntesis, negación, conjunción y disyunción. Por eso A + B·C se interpreta como A + (B·C), no como (A + B)·C. Para A = 1, B = 0 y C = 0, las dos agrupaciones producen 1 y 0 respectivamente.

Al combinar comparaciones, XOR e igualdad, escribir paréntesis explícitos evita depender de diferencias de precedencia entre lenguajes. Una negación debe rodear toda la expresión que se quiere negar. Escribir ¬(A·B) no equivale a ¬A·B.

### 2.8. Traducción de operadores al lenguaje

| Operación | Python con operandos `bool` |
|---|---|
| AND | `A and B` |
| OR | `A or B` |
| NOT | `not A` |
| XOR | `A != B`; también `A ^ B` con booleanos |
| XNOR | `A == B` o `not (A != B)` |
| NAND | `not (A and B)` |
| NOR | `not (A or B)` |

Python no tiene palabras reservadas `xor` ni `xand`. Para booleanos, `!=` indica diferencia de valores y sirve como XOR. Fuera del dominio booleano, una comparación de desigualdad no debe confundirse con el XOR bit a bit de enteros. No usar `~` como sustituto de `not`: no es la negación lógica.

`and` y `or` cortocircuitan y pueden devolver uno de sus operandos, no necesariamente un `bool`. En esta lectura ambos operandos son booleanos para que las tablas representen exactamente sus resultados. Una cadena no vacía como `"False"` tiene valor de verdad verdadero; no debe usarse para representar la condición falsa.

```python
A, B = True, False
print(A and B)         # False
print(A or B)          # True
print(not A)           # False
print(A != B)          # True: XOR
print(A == B)          # False: XNOR
print(not (A and B))   # True: NAND
```

**Cortocircuito:** si el primer operando de AND es falso, no hace falta evaluar el segundo para determinar la salida. Si el primer operando de OR es verdadero, tampoco hace falta evaluar el segundo. Esto permite proteger una división, como muestra el siguiente ejemplo.

```python
divisor = 0
valido = (divisor != 0) and (10 / divisor > 2)
print(valido)  # False; no se ejecuta la división
```

No cambiar arbitrariamente el orden de esa comprobación: ejecutar la división antes de comprobar el divisor introduciría un error. Las leyes describen valores booleanos; sustituir código exige conservar además sus condiciones de evaluación.

<a id="concepto-3"></a>

## 3. Aplicaciones generales del álgebra de Boole

El álgebra de Boole estudia cómo combinar condiciones y transformar expresiones conservando su resultado. Su utilidad comienza antes de escribir código: permite precisar una regla verbal, detectar casos ambiguos y justificar que una formulación más simple conserva la decisión original.

### 3.1. Reglas de acceso y decisiones de negocio

Supongamos que C significa «credencial vigente», R «reserva activa» y A «autorización del responsable». La política «permitir el acceso con credencial y reserva, o con autorización» se expresa como **P = C·R + A**. La autorización es una alternativa suficiente según esa redacción.

Si se añade «un bloqueo B siempre impide el acceso», la formulación pasa a **P = (C·R + A)·¬B**. El bloqueo afecta a toda la autorización; escribir C·R + A·¬B permitiría entrar con credencial y reserva incluso estando bloqueado. Los paréntesis documentan el alcance de una regla.

El procedimiento de modelado es: identificar las condiciones, definir cada variable, precisar qué significa «y» u «o», agrupar las reglas y comprobar escenarios representativos. «A o B» no debe interpretarse como XOR salvo que el requisito excluya explícitamente la coincidencia.

### 3.2. Diseño de circuitos digitales

Una expresión se puede traducir a conexiones entre compuertas. Para **F = (A + B)·¬C**, primero se calcula A OR B, se niega C y se combinan ambas salidas mediante AND. Con A = 0, B = 1 y C = 0, la salida es 1. Si C cambia a 1, la salida es 0, independientemente de A y B.

Simplificar una expresión puede reducir operaciones o compuertas en un modelo de implementación. Sin embargo, menos símbolos no garantizan por sí solos menor tiempo de ejecución ni menor retardo físico: influyen el compilador, la tecnología, la profundidad de las conexiones y otras restricciones. En este tema, el objetivo verificable es conservar la función y eliminar redundancias justificadas.

### 3.3. Conjuntos y filtros

Para un elemento x de un universo U, A significa «x pertenece al conjunto de estudiantes matriculados» y B «x pertenece al conjunto de estudiantes con reserva». AND corresponde a pertenecer a la intersección; OR, a la unión; NOT, al complemento respecto de U.

| Operación lógica | Lectura como pertenencia |
|---|---|
| A·B | x pertenece a ambos conjuntos |
| A + B | x pertenece al menos a uno |
| ¬A | x está en U pero no pertenece al conjunto A |
| A ⊕ B | x pertenece a uno de los conjuntos, pero no a ambos |

Esta interpretación se aplica a filtros de registros, criterios de búsqueda y validación de formularios. Definir el universo es indispensable: «no está matriculado» no especifica por sí solo qué personas pueden aparecer en el resultado.

### 3.4. Equivalencia y clasificación de expresiones

Dos expresiones son equivalentes si sus columnas de salida coinciden en **todas** las filas. Se escribe F ≡ G para enfatizar la equivalencia lógica. Por ejemplo, A + A·B ≡ A. El hecho de obtener el mismo resultado con A = 1 y B = 0 es una comprobación parcial; la ley afirma algo sobre las cuatro combinaciones.

Una **tautología** siempre produce 1, como A + ¬A. Una **contradicción** siempre produce 0, como A·¬A. Una **contingencia** puede producir 0 o 1, como A·B. Clasificar una expresión exige considerar todo su dominio, no solo la entrada utilizada en un ejemplo.

Como complemento conceptual, la implicación A → B equivale a ¬A + B y solo es falsa con A = 1 y B = 0. No expresa automáticamente causalidad ni equivale a A·B. La implicación es una relación entre proposiciones; la asignación de un programa es una operación que guarda un valor.

<a id="concepto-4"></a>

## 4. Leyes del álgebra de Boole

Una ley es una equivalencia válida para todos los valores booleanos de sus variables. Se puede usar en ambos sentidos: para expandir o para reducir una expresión. Las letras representan también **subexpresiones completas**. Por ejemplo, si X = A + B, la identidad X·1 = X permite escribir (A + B)·1 = A + B.

Se mantiene el orden de las siete leyes de la presentación. Al final se añaden conmutatividad, asociatividad y doble negación como herramientas de apoyo para justificar los pasos que suelen quedar implícitos. En los ejemplos de código, las variables son booleanas y las expresiones no modifican estado.

<a id="ley-1"></a>

### 4.1. Ley de Identidad

**Concepto.** El elemento neutro de OR es 0 y el de AND es 1. Combinarlos con una condición deja el resultado determinado por esa condición.

| Forma | Formulación |
|---|---|
| Primera | A + 0 = A |
| Segunda | A·1 = A |

**Explicación.** Un OR con falso no agrega una alternativa que pueda habilitar la salida. Un AND con verdadero no agrega una restricción que pueda impedirla. Así, una condición de acceso combinada con una comprobación siempre verdadera conserva exactamente sus casos de aceptación.

**Ejemplo con valores.** Si A = 0: 0 + 0 = 0 y 0·1 = 0. Si A = 1: 1 + 0 = 1 y 1·1 = 1.

**Ejemplo algebraico.** (A + B)·1 = A + B: se aplica identidad a toda la subexpresión A + B.

**En Python.** Las dos impresiones comparan los lados de la identidad. Ambas deben indicar verdadero para los datos utilizados.

```python
A = False
print((A or False) == A)
print((A and True) == A)
```

**Error que evitar.** No intercambiar los neutros: OR con 1 y AND con 0 pertenecen a anulación.

<a id="ley-2"></a>

### 4.2. Ley de Anulación

**Concepto.** El elemento absorbente fija el resultado sin importar el valor de la otra condición. Para OR es 1; para AND es 0. También se llama ley de dominación.

| Forma | Formulación |
|---|---|
| Primera | A + 1 = 1 |
| Segunda | A·0 = 0 |

**Explicación.** Si una alternativa de OR ya es verdadera, el OR es verdadero. Si un requisito de AND ya es falso, el AND es falso. Esta ley permite detectar expresiones que aparentan depender de una variable, pero cuya salida en realidad es constante.

**Ejemplo con valores.** Si A = 0: 0 + 1 = 1 y 0·0 = 0. Si A = 1: 1 + 1 = 1 y 1·0 = 0.

**Ejemplo algebraico.** (A·B) + 1 = 1 y (A + B)·0 = 0, sin necesidad de evaluar A ni B para conocer el valor lógico.

**En Python.** Las dos impresiones comparan los lados de la identidad. Ambas deben indicar verdadero para los datos utilizados.

```python
A = True
print((A or True) == True)
print((A and False) == False)
```

**Error que evitar.** No confundir una salida constante con una variable sin valor. La salida está perfectamente determinada.

<a id="ley-3"></a>

### 4.3. Ley de Idempotencia

**Concepto.** Repetir la misma condición mediante AND u OR no cambia su valor.

| Forma | Formulación |
|---|---|
| Primera | A + A = A |
| Segunda | A·A = A |

**Explicación.** Preguntar dos veces si una credencial es válida no añade una alternativa diferente ni una restricción nueva, siempre que se esté usando el mismo valor. Si A es falsa, ambas copias son falsas; si A es verdadera, ambas son verdaderas.

**Ejemplo con valores.** Si A = 0: 0 + 0 = 0 y 0·0 = 0. Si A = 1: 1 + 1 = 1 y 1·1 = 1.

**Ejemplo algebraico.** (A + B) + (A + B) = A + B. Se repite la subexpresión completa, no solo una letra.

**En Python.** Las dos impresiones comparan los lados de la identidad. Ambas deben indicar verdadero para los datos utilizados.

```python
A = False
print((A or A) == A)
print((A and A) == A)
```

**Error que evitar.** A + A no se convierte en 2A: + representa OR. Dos llamadas a una función no se consideran automáticamente el mismo valor estable.

<a id="ley-4"></a>

### 4.4. Ley de Complemento

**Concepto.** Una condición y su negación cubren todos los casos cuando se unen con OR y no pueden cumplirse simultáneamente cuando se combinan con AND.

| Forma | Formulación |
|---|---|
| Primera | A + ¬A = 1 |
| Segunda | A·¬A = 0 |

**Explicación.** Si A es verdadera, ¬A es falsa; si A es falsa, ¬A es verdadera. Por eso siempre hay una alternativa verdadera en OR y siempre hay un requisito falso en AND. Los resultados son los valores absorbentes de esas operaciones: 1 para OR y 0 para AND.

**Ejemplo con valores.** Con A = 0: 0 + 1 = 1 y 0·1 = 0. Con A = 1: 1 + 0 = 1 y 1·0 = 0.

**Ejemplo algebraico.** (A + B) + ¬(A + B) = 1. La negación debe corresponder a toda la misma expresión.

**En Python.** Las dos impresiones comparan los lados de la identidad. Ambas deben indicar verdadero para los datos utilizados.

```python
A = True
print((A or (not A)) == True)
print((A and (not A)) == False)
```

**Error que evitar.** En A + ¬A·B no se puede reemplazar A + ¬A por 1 directamente: ¬A está dentro del término ¬A·B. Primero se debe transformar la agrupación con distributividad.

<a id="ley-5"></a>

### 4.5. Ley de Distributiva

**Concepto.** Una operación se distribuye sobre la otra. En álgebra de Boole tanto AND distribuye sobre OR como OR distribuye sobre AND.

| Forma | Formulación |
|---|---|
| Primera | A·(B + C) = A·B + A·C |
| Segunda | A + B·C = (A + B)·(A + C) |

**Explicación.** En la primera forma, exigir A junto con alguna de las alternativas B o C equivale a ofrecer dos casos: A junto con B, o A junto con C. En la segunda, la alternativa A puede satisfacer por sí sola ambos factores; si A es falsa, se exige que B y C sean verdaderas. Esta segunda forma no es una regla de la aritmética usual.

**Ejemplo con valores.** Para A = 0, B = 1 y C = 1: A + B·C = 0 + 1 = 1 y (A + B)·(A + C) = 1·1 = 1. Es una comprobación; la ley se cumple en las ocho filas.

**Ejemplo algebraico.** A·B + A·¬B = A·(B + ¬B). Se usa la primera forma en sentido inverso para factorizar A.

**En Python.** Las dos impresiones comparan los lados de la identidad. Ambas deben indicar verdadero para los datos utilizados.

```python
A, B, C = False, True, True
print((A and (B or C)) == ((A and B) or (A and C)))
print((A or (B and C)) == ((A or B) and (A or C)))
```

**Error que evitar.** Distribuir exige conservar ambos términos: A·(B + C) no se transforma en A·B + C. La transformación inversa solo puede extraer un factor realmente común.

<a id="ley-6"></a>

### 4.6. Ley de De Morgan

**Concepto.** Negar un grupo cambia AND por OR, u OR por AND, y niega cada operando del grupo.

| Forma | Formulación |
|---|---|
| Primera | ¬(A + B) = ¬A·¬B |
| Segunda | ¬(A·B) = ¬A + ¬B |

**Explicación.** «No se cumple A o B» exige que no se cumpla ninguna: ¬A y ¬B. «No se cumplen A y B simultáneamente» requiere que falle al menos una: ¬A o ¬B. No se conserva el operador al repartir la negación. Para más operandos se aplica el mismo cambio a todo el grupo.

**Ejemplo con valores.** Con A = 1 y B = 0: ¬(1 + 0) = 0 y ¬1·¬0 = 0·1 = 0. También ¬(1·0) = 1 y ¬1 + ¬0 = 0 + 1 = 1.

**Ejemplo algebraico.** ¬(A·¬B) = ¬A + ¬(¬B) = ¬A + B. El último paso usa doble negación, no otra aplicación de De Morgan.

**En Python.** Las dos impresiones comparan los lados de la identidad. Ambas deben indicar verdadero para los datos utilizados.

```python
A, B = True, False
print((not (A or B)) == ((not A) and (not B)))
print((not (A and B)) == ((not A) or (not B)))
```

**Error que evitar.** Negar ambas letras y mantener AND en ¬(A·B) es incorrecto. Con A = 1 y B = 0, la expresión correcta vale 1 y ¬A·¬B vale 0.

<a id="ley-7"></a>

### 4.7. Ley de Absorción

**Concepto.** Una condición absorbe un término que no aporta casos nuevos o una alternativa que no cambia su cumplimiento.

| Forma | Formulación |
|---|---|
| Primera | A + A·B = A |
| Segunda | A·(A + B) = A |

**Explicación.** En A + A·B, el segundo término solo es verdadero cuando A ya lo es, de modo que no agrega filas verdaderas. En A·(A + B), si A es falsa, todo es falso; si A es verdadera, el paréntesis ya es verdadero. B no afecta el resultado final.

**Ejemplo con valores.** Con A = 0 y B = 1: 0 + 0·1 = 0 y 0·(0 + 1) = 0. Con A = 1 y B = 0: 1 + 1·0 = 1 y 1·(1 + 0) = 1.

**Ejemplo algebraico.** A + A·B = A·1 + A·B = A·(1 + B) = A·1 = A. Las justificaciones son identidad en sentido inverso, distributiva, anulación e identidad.

**En Python.** Las dos impresiones comparan los lados de la identidad. Ambas deben indicar verdadero para los datos utilizados.

```python
A, B = False, True
print((A or (A and B)) == A)
print((A and (A or B)) == A)
```

**Error que evitar.** A + ¬A·B no se reduce a A mediante absorción básica. Por ejemplo, A = 0 y B = 1 produce 1, mientras que A produce 0.

### 4.8. Leyes auxiliares para ordenar y agrupar

| Ley | Formulación | Qué permite |
|---|---|---|
| Conmutativa de OR | A + B = B + A | Cambiar el orden de dos operandos de OR |
| Conmutativa de AND | A·B = B·A | Cambiar el orden de dos operandos de AND |
| Asociativa de OR | (A + B) + C = A + (B + C) | Reagrupar una cadena de OR |
| Asociativa de AND | (A·B)·C = A·(B·C) | Reagrupar una cadena de AND |
| Doble negación o involución | ¬(¬A) = A | Eliminar dos negaciones consecutivas |
| Negación de constantes | ¬0 = 1; ¬1 = 0 | Evaluar una negación conocida |

La asociativa no permite mover paréntesis entre operadores diferentes. Por ejemplo, (A + B)·C no equivale en general a A + B·C. La conmutativa y la asociativa conservan valores booleanos; en código con funciones que modifican estado, cambiar el orden puede cambiar los efectos observables.

### 4.9. Absorción generalizada como identidad derivada

La expresión **A + ¬A·B = A + B** se denomina a veces absorción generalizada o ley de reducción. Para no memorizarla sin justificación, puede derivarse con las leyes anteriores:

| Paso | Expresión | Justificación |
|---|---|---|
| Inicial | A + ¬A·B | Expresión que se desea reducir |
| 1 | (A + ¬A)·(A + B) | Distributiva de OR sobre AND |
| 2 | 1·(A + B) | Complemento en A + ¬A |
| 3 | A + B | Identidad de AND |

Aquí sí se puede aplicar complemento en el paso 2, porque A + ¬A aparece como una subexpresión completa. No se están cancelando letras separadas por otras operaciones. La forma dual es **A·(¬A + B) = A·B**, que se obtiene distribuyendo y aplicando complemento e identidad.

### 4.10. Resumen de las siete leyes principales

| Ley | Forma con OR | Forma con AND o forma dual |
|---|---|---|
| Identidad | A + 0 = A | A·1 = A |
| Anulación | A + 1 = 1 | A·0 = 0 |
| Idempotencia | A + A = A | A·A = A |
| Complemento | A + ¬A = 1 | A·¬A = 0 |
| Distributiva | A + B·C = (A + B)·(A + C) | A·(B + C) = A·B + A·C |
| De Morgan | ¬(A + B) = ¬A·¬B | ¬(A·B) = ¬A + ¬B |
| Absorción | A + A·B = A | A·(A + B) = A |

La dualidad intercambia OR con AND y 0 con 1. Por ejemplo, de A + 0 = A se obtiene A·1 = A. No significa negar cada variable; es una correspondencia entre identidades del álgebra.

<a id="demostracion"></a>

## 5. Simplificación de expresiones: dos ejemplos resueltos

### Método de trabajo

1. Identificar operadores y alcance de cada negación.
2. Buscar constantes, repeticiones, complementos y factores comunes.
3. Aplicar una transformación justificada a una subexpresión completa.
4. Escribir la expresión resultante y el nombre de la ley.
5. Repetir hasta eliminar las redundancias identificadas.
6. Comparar la tabla original con la simplificada para detectar errores.

Simplificar no significa borrar letras por intuición. A veces conviene expandir temporalmente una expresión para que aparezca un complemento; otras veces conviene factorizar. Puede haber varias formas equivalentes y no toda secuencia conduce inmediatamente a una forma mínima.

### 5.1. Ejemplo 1: factor común y complemento

**Problema:** reducir **F = A·B + A·¬B + ¬A·B**. La expresión es verdadera si ocurre alguna de estas alternativas: ambas condiciones, solo A o solo B. La reducción debe conservar las cuatro salidas.

| Paso | Expresión equivalente | Ley y subexpresión transformada |
|---|---|---|
| Inicial | A·B + A·¬B + ¬A·B | Función original |
| 1 | (A·B + A·¬B) + ¬A·B | Asociativa de OR: agrupar los dos primeros términos |
| 2 | A·(B + ¬B) + ¬A·B | Distributiva en sentido inverso: extraer A |
| 3 | A·1 + ¬A·B | Complemento: B + ¬B = 1 |
| 4 | A + ¬A·B | Identidad: A·1 = A |
| 5 | (A + ¬A)·(A + B) | Distributiva de OR sobre AND |
| 6 | 1·(A + B) | Complemento: A + ¬A = 1 |
| 7 | A + B | Identidad: 1·X = X |

**Resultado:** F = A + B. No es XOR: la fila A = 1, B = 1 también produce 1. En el paso 4 no se puede sustituir directamente A + ¬A por 1 sin distribuir, porque ¬A pertenece al producto ¬A·B. Los pasos 5 a 7 explicitan la reducción generalizada.

| A | B | A·B | A·¬B | ¬A·B | F original | A + B |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 0 | 0 | 1 | 1 |

**Traducción al lenguaje:**

```python
A, B = False, True
original = (A and B) or (A and (not B)) or ((not A) and B)
reducida = A or B
print(original, reducida, original == reducida)  # True True True
```

### 5.2. Ejemplo 2: De Morgan, doble negación y absorción

**Problema:** reducir **G = ¬((A + B)·(A + ¬B)) + ¬A·C**. La negación inicial abarca todo el producto de los dos paréntesis. Se busca mostrar que ciertas variables dejan de influir en la salida.

| Paso | Expresión equivalente | Ley y subexpresión transformada |
|---|---|---|
| Inicial | ¬((A + B)·(A + ¬B)) + ¬A·C | Función original |
| 1 | ¬(A + B) + ¬(A + ¬B) + ¬A·C | De Morgan: negar el producto exterior produce OR de negaciones |
| 2 | ¬A·¬B + ¬A·¬(¬B) + ¬A·C | De Morgan en cada suma negada |
| 3 | ¬A·¬B + ¬A·B + ¬A·C | Doble negación: ¬(¬B) = B |
| 4 | ¬A·(¬B + B) + ¬A·C | Distributiva en sentido inverso en los dos primeros términos |
| 5 | ¬A·1 + ¬A·C | Complemento: ¬B + B = 1 |
| 6 | ¬A + ¬A·C | Identidad: ¬A·1 = ¬A |
| 7 | ¬A | Absorción: X + X·C = X, con X = ¬A |

**Resultado:** G = ¬A. Las variables B y C desaparecen porque no alteran la salida, no porque se hayan fijado arbitrariamente. Si A = 0, G = 1 para cualquier combinación de B y C; si A = 1, G = 0.

| A | B | C | G original | ¬A |
|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 1 |
| 0 | 0 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 | 0 |
| 1 | 1 | 1 | 0 | 0 |

**Traducción al lenguaje:**

```python
A, B, C = False, True, False
original = (not ((A or B) and (A or (not B)))) or ((not A) and C)
reducida = not A
print(original, reducida, original == reducida)  # True True True
```

### 5.3. Demostración completa: comprobación 

**Contrato:** enumerar las cuatro combinaciones del ejemplo 1 y las ocho del ejemplo 2. Mostrar las entradas, la salida original, la reducida y una columna IGUALES. Usar 0 para falso y 1 para verdadero. IGUALES debe ser 1 en todas las filas. Esta comprobación no resuelve los ejercicios propuestos ni la PC.

Los ciclos solo automatizan la enumeración de la tabla. Se estudian después; ahora basta identificar qué expresiones se evalúan dentro de ellos y cómo se relacionan con cada fila. La demostración no recibe entradas de teclado ni necesita dependencias externas.

**Fuente ejecutable:** [ejemplos/demo.py](ejemplos/demo.py).

<!-- example: demo.py -->
```python
print("A B ORIGINAL REDUCIDA IGUALES")
for A in (False, True):
    for B in (False, True):
        original = (A and B) or (A and (not B)) or ((not A) and B)
        reducida = A or B
        print(int(A), int(B), int(original), int(reducida), int(original == reducida))

print("A B C ORIGINAL REDUCIDA IGUALES")
for A in (False, True):
    for B in (False, True):
        for C in (False, True):
            original = (not ((A or B) and (A or (not B)))) or ((not A) and C)
            reducida = not A
            print(int(A), int(B), int(C), int(original), int(reducida), int(original == reducida))
```

**Ejecución:** abrir una terminal dentro de la carpeta `python/ejemplos/`.

```bash
python3 demo.py
```

En Windows puede utilizarse `py demo.py`, según la instalación.

**Salida esperada:**

```text
A B ORIGINAL REDUCIDA IGUALES
0 0 0 0 1
0 1 1 1 1
1 0 1 1 1
1 1 1 1 1
A B C ORIGINAL REDUCIDA IGUALES
0 0 0 1 1 1
0 0 1 1 1 1
0 1 0 1 1 1
0 1 1 1 1 1
1 0 0 0 0 1
1 0 1 0 0 1
1 1 0 0 0 1
1 1 1 0 0 1
```

Si aparece un 0 en IGUALES, esa fila es un contraejemplo de la equivalencia programada. Revisar operadores, negaciones y agrupación antes de atribuir el fallo a la ley. Un error de sintaxis debe corregirse antes de comparar resultados.

<a id="pc"></a>

## 6. Práctica: aplicación de leyes y simplificación

### 6.1. Indicaciones comunes

Los siguientes ejercicios se entregan **sin solución**. En cada simplificación, registrar la expresión inicial, cada expresión equivalente y la ley aplicada. Una respuesta final sin justificación no permite revisar el procedimiento. Primero resolver algebraicamente y después contrastar con una tabla completa o con código.

En los ejercicios de modelado, definir el significado de cada variable antes de formular la expresión. Si el enunciado permite dos interpretaciones, escribir la interpretación adoptada y un caso que permita distinguirlas.

### 6.2. Nivel 1: aplicación directa de una ley

Indicar qué ley permite reducir cada expresión. Cuando se indica la ley como pista, explicar por qué encaja su estructura.

| N.º | Expresión | Orientación |
|---|---|---|
| 1 | A + 0 | Identidad |
| 2 | (A + B)·1 | Tratar el paréntesis como una sola condición |
| 3 | A + 1 | Anulación |
| 4 | (A·B)·0 | Anulación |
| 5 | (A + B) + (A + B) | Idempotencia |
| 6 | (A·B)·(A·B) | Idempotencia |
| 7 | A + ¬A | Complemento |
| 8 | (A + B)·¬(A + B) | Identificar la expresión y su negación completa |
| 9 | A + A·B | Absorción |
| 10 | A·(A + B) | Absorción en su forma dual |
| 11 | ¬(A + B) | De Morgan; eliminar la negación del grupo |
| 12 | ¬(A·B) | De Morgan; comparar con el ejercicio anterior |

### 6.3. Nivel 2: combinar varias leyes

Simplificar sin asignar valores específicos a las variables. Cada fila puede requerir más de una transformación. Construir la tabla completa en los ejercicios 15, 18, 21 y 24.

| N.º | Expresión inicial |
|---|---|
| 13 | (A + 0)·1 |
| 14 | A·B + A·¬B |
| 15 | (A + B)·(A + ¬B) |
| 16 | A + ¬A·B |
| 17 | A·(¬A + B) |
| 18 | ¬(A + ¬B) + ¬A·B |
| 19 | (A + A·B)·(C + 0) |
| 20 | (A + 1)·(B + B·C) |
| 21 | A·B + A·¬B + ¬A·B + ¬A·¬B |
| 22 | ¬(¬(A + B))·(A + A·C) |
| 23 | (A·B + A·¬B) + A·C |
| 24 | ¬(A·B)·A + A·B |

### 6.4. Nivel 3: modelado y aplicación

**25. Habilitación redundante.** Un botón se habilita si la sesión está activa, o si la sesión está activa y el perfil está completo. Definir variables, formular la regla y simplificarla. Explicar si «perfil completo» influye realmente y qué redacción sería necesaria para exigirlo.

**26. Alarma.** La alarma se activa si hay humo o temperatura alta, siempre que no esté activo el modo de mantenimiento. Formular activación y desactivación. Aplicar De Morgan a la negación de la función completa y justificar el alcance del mantenimiento.

**27. Circuito.** Para F = (A + B)·¬C, describir las operaciones en orden y construir las ocho filas. Identificar qué entradas fuerzan F = 0 sin conocer las restantes.

**28. Filtro de registros.** Un registro se incluye si está vigente y pertenece al grupo A, o si está vigente y pertenece al grupo B. Formular, factorizar y explicar en palabras la expresión resultante. No asumir que los grupos son excluyentes.

### 6.5. Detectar y corregir errores de razonamiento

Para cada afirmación, decidir si es válida. Si es falsa, dar un contraejemplo con valores concretos y escribir la transformación correcta.

| N.º | Afirmación a revisar |
|---|---|
| 29 | A + ¬A·B = 1, porque A + ¬A = 1 |
| 30 | ¬(A·B) = ¬A·¬B |
| 31 | A + A·B = A + B |
| 32 | A XOR B equivale a A OR B para todos los valores |
| 33 | (A + B)·C = A + B·C, por asociatividad |
| 34 | Dos expresiones que coinciden en una entrada son equivalentes |

### 6.6. PC1.1 · Formalización y comprobación de una política

Una sala permite acceso cuando la credencial está vigente y existe reserva, o cuando hay autorización del responsable. Una condición de bloqueo siempre impide entrar, incluso con autorización.

Definir C = «credencial vigente», R = «reserva activa», A = «autorización del responsable» y B = «bloqueo activo». La redacción anterior es el contrato de la PC.

**Trabajo solicitado:**

1. Formular la expresión de permiso con agrupación explícita.
2. Construir manualmente las 16 filas de C, R, A y B, indicando la salida.
3. Derivar la expresión de denegación mediante De Morgan, identificando cada ley.
4. Proponer una formulación equivalente del permiso y justificar la equivalencia. No asumir que toda expresión admite una reducción con menos variables.


**Restricciones:** usar valores booleanos, no cadenas de texto como sustitutos; conservar el significado de cada variable; entregar una sola versión; no conectar el ejercicio a un sistema de acceso real. El dominio tiene dos valores por variable: una entrada textual desconocida se rechaza o se convierte explícitamente antes de evaluar, nunca se interpreta automáticamente como falso.

| C | R | A | B | Permiso esperado | Qué comprueba |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | Ausencia de habilitación |
| 1 | 1 | 0 | 0 | 1 | Habilitación ordinaria |
| 0 | 0 | 1 | 0 | 1 | Autorización excepcional |
| 1 | 0 | 0 | 0 | 0 | Credencial insuficiente sin reserva |
| 1 | 1 | 1 | 1 | 0 | Prioridad del bloqueo |
| 0 | 0 | 1 | 1 | 0 | Bloqueo incluso con autorización |

Estos son casos de aceptación de la PC, no su solución ni la tabla completa. Agregar las combinaciones restantes y comprobar que permiso y denegación siempre sean complementarios.

**Evidencia:** guardar el desarrollo algebraico, la tabla, el código, los comandos y las salidas reales en una carpeta personal `PC1.1`. Registrar la explicación en `evidencias/PC1.1.md`. Crear un commit funcional `feat(pc1.1): formalizar-y-verificar-politica`; obtener el hash real mediante `git rev-parse HEAD` y revisar el cambio con `git show HASH`. Para comparar avances usar `git diff HASH_ANTERIOR HASH_ACTUAL`, sustituyendo los marcadores por hashes reales.


**Comandos para la entrega personal:**

```bash
python3 solucion.py
```


<a id="esencial"></a>

## 7. Lo esencial

- Definir el significado de las variables antes de formular una condición.
- Distinguir asignación, comparación e identidad algebraica.
- Interpretar + como OR y · como AND; sus leyes no son todas las de la aritmética.
- Usar XOR para diferencia y XNOR para coincidencia entre dos valores booleanos.
- Aplicar cada ley a una subexpresión completa y respetar paréntesis y negaciones.
- Distinguir absorción básica de la reducción A + ¬A·B = A + B.
- Comprobar equivalencia en todas las combinaciones, no solo en un ejemplo.
- Mantener condiciones sin efectos de estado cuando se trasladan identidades al código.

## 8. Referencias y lectura de apoyo

- Pablo Torres P. **Lógica Matemática**, presentación de clase aportada por el docente.
- Python Software Foundation. [Expresiones y operaciones booleanas](https://docs.python.org/3.14/reference/expressions.html#boolean-operations), secciones 6.10–6.11. Referencia técnica para comparaciones, cortocircuito y precedencia.

[Volver al índice del tema](../README.md)
