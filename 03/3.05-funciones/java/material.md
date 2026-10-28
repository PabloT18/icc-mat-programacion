# Programación

![UPS · Carrera de Computación](../../../assets/logos/ups-computacion.png)

## 3.05 · Funciones, contratos y descomposición · Java

**Autor:** Ing. Pablo Torres, Mgtr.  
**Unidad 3:** Lenguaje de Programación  


[Versión Python](../python/material.md) · [Presentación Python](../presentacion.pptx) · [Anterior](../../3.04-iteracion/java/material.md) · [Siguiente](../../3.06-cadenas/java/material.md)

[Conceptos](#concepto-1) · [Demostración](#demostracion) · [Práctica de clase](#pc) · [Lo esencial](#esencial)

**Contexto.** Calcular un resumen desde varios lugares del programa sin duplicar las reglas. Separar funciones que calculan de funciones que presentan resultados permite probar cada responsabilidad con datos concretos.

**Prerrequisitos.** Decisiones, ciclos y trazas.

**Versión complementaria.** Estudiar el mismo problema y los mismos casos de Python mediante construcciones idiomáticas de Java. La presentación compartida corresponde a Python.

## 1. Conceptos y ejemplos

<a id="concepto-1"></a>

### 1.1. Contrato, parámetros y argumentos

Una función reúne una operación con un nombre y un contrato. Los parámetros describen los datos que necesita; los argumentos son los valores de una llamada. Especificar precondiciones, resultado y efectos permite utilizarla sin leer su implementación. Elegir una responsabilidad precisa: validar una cantidad, calcular una tarifa o mostrar un informe. Evitar una función que simultáneamente lea, modifique datos y decida toda la aplicación.

**Aplicar en Java.** Usar métodos static para este curso introductorio. Declarar tipos de parámetros y retorno. Un método no se declara dentro de otro; ubicarlo dentro de la clase y fuera de main. Java pasa argumentos por valor, incluidos valores que son referencias.

```java
static int doble(int numero) {
    return numero * 2;
}
// Dentro de main: System.out.println(doble(7));
```

<a id="concepto-2"></a>

### 1.2. Retornar y mostrar

Retornar entrega un valor al código que llamó la función. Mostrar escribe en una salida y produce un efecto observable. Una función de cálculo que solo imprime dificulta reutilizar su resultado en otra operación. Separar ambas responsabilidades cuando el resultado se necesita después. return también finaliza la llamada, por lo que instrucciones posteriores en ese camino no se ejecutan.

**Aplicar en Java.** void indica que un método no devuelve un valor. Un método con retorno debe devolver un valor compatible en todos los caminos que terminan normalmente. println no produce un valor asignable.

```java
static double area(double base, double altura) {
    return base * altura / 2;
}
```

<a id="concepto-3"></a>

### 1.3. Alcance, mutabilidad y efectos

Una variable local pertenece a una llamada, no al programa entero. Evitar estado global para que una función dependa de argumentos visibles. Al pasar una colección, distinguir reasignar el parámetro de modificar el objeto compartido. La mutación se estudiará con listas; desde ahora, indicar si una función conserva o cambia sus entradas. Una función pura devuelve el mismo resultado para los mismos argumentos y no produce efectos externos.

**Aplicar en Java.** Una copia del valor de la referencia puede apuntar al mismo objeto. Reasignar el parámetro no cambia la variable del llamador, pero modificar el objeto puede observarse fuera. Para tipos primitivos se copia el valor.

```java
static int incrementar(int n) {
    n++;
    return n;
}
```

<a id="concepto-4"></a>

### 1.4. Pruebas de funciones y descomposición

Probar una función con argumentos concretos reduce la dependencia del teclado. Comparar resultado y valor esperado, incluir fronteras y entrada inválida. Descomponer un problema en funciones que tengan nombres relacionados con el dominio. No crear funciones solo para ocultar una línea si no mejora el contrato. Mantener la validación donde corresponda y evitar que una función devuelva a veces número y a veces mensaje de error sin especificarlo.

**Aplicar en Java.** Lanzar IllegalArgumentException para argumentos fuera de dominio. Las comprobaciones del ejemplo se ejecutan con llamadas y comparaciones explícitas; los assert de Java también pueden estar desactivados.

```java
static int mitadPar(int n) {
    if (n % 2 != 0) throw new IllegalArgumentException("Se requiere un entero par");
    return n / 2;
}
```

Los bloques breves anteriores ilustran una operación y pueden requerir variables o imports del contexto. Utilizar la demostración siguiente como programa completo.


### Síntesis visual

![Infografía técnica del tema](../assets/infografia.svg)

<a id="demostracion"></a>

## 2. Demostración guiada

**Problema.** Implementar costo_horas y comprobar un cálculo válido y una llamada con horas negativas.

**Contrato de esta demostración.** Recibir horas enteras no negativas y tarifa numérica no negativa. Retornar su producto sin imprimir dentro del cálculo. Lanzar error de argumento si existe un valor negativo. El llamador muestra el resultado y gestiona el error.

**Fuente:** [ejemplos/Demo.java](ejemplos/Demo.java).

<!-- example: Demo.java -->
```java
import java.util.Locale;
public class Demo {
    static double costoHoras(int horas, double tarifa) {
        if (horas < 0 || tarifa < 0) throw new IllegalArgumentException("Valores negativos");
        return horas * tarifa;
    }
    public static void main(String[] args) {
        System.out.printf(Locale.ROOT, "Costo: %.2f%n", costoHoras(3, 2.5));
        try { costoHoras(-1, 2.5); }
        catch (IllegalArgumentException error) { System.out.println(error.getMessage()); }
    }
}
```

### Ejecutar

Abrir una terminal dentro de `03/3.05-funciones/java/ejemplos/` y ejecutar:

```bash
javac -encoding UTF-8 -d build *.java
java -cp build Demo
```

### Salida esperada

```text
Costo: 7.50
Valores negativos
```

**Interpretación.** Seguir las asignaciones y los bloques en orden, identificar qué instrucción produce cada línea y contrastar con el contrato. Modificar un dato por vez y anticipar el resultado antes de ejecutar. La salida de referencia es una expectativa; el registro de verificaciones indica qué ejecuciones se realizaron.

<a id="ejercicios"></a>

### Ejercicios prácticos progresivos

Resolver los siguientes ejercicios en orden. Entregar enunciado, fuente y resultado propio. Los casos mostrados permiten comprobar el contrato y no sustituyen una prueba adicional de frontera.

Adaptar los mismos datos y resultados a Java. Usar `record` para registros y bibliotecas estándar para archivos y procesos. Para resultados booleanos, aceptar `true/false` en Java frente a `True/False` en Python. Los ejercicios que inspeccionan el intérprete deben inspeccionar la JVM y el JDK equivalentes.

#### Ejercicio 01. Doble

Definir doble(n) y comprobar doble(6).

**Caso de comprobación:**

```text
12
```

#### Ejercicio 02. Área

Definir area_rectangulo(base,altura) y comprobar 5 por 4.

**Caso de comprobación:**

```text
20
```

#### Ejercicio 03. Paridad retornada

Definir es_par(n) que retorne bool. Mostrar el resultado para 7.

**Caso de comprobación:**

```text
false
```

#### Ejercicio 04. Máximo de tres

Definir mayor(a,b,c) sin usar max. Probar 8, 3 y 8.

**Caso de comprobación:**

```text
8
```

#### Ejercicio 05. Suma de rango

Definir sumar_rango(inicio,fin) inclusivo. Rechazar inicio mayor que fin. Probar 3 a 6.

**Caso de comprobación:**

```text
18
```

#### Ejercicio 06. Factorial validado

Definir factorial(n) para enteros no negativos. Probar cero y cinco.

**Caso de comprobación:**

```text
1 120
```

#### Ejercicio 07. Contar divisores

Definir contar_divisores(n) para n>0. Probar 12.

**Caso de comprobación:**

```text
6
```

#### Ejercicio 08. Número perfecto

Definir es_perfecto(n) utilizando suma de divisores propios. Probar 6 y 8.

**Caso de comprobación:**

```text
true false
```

#### Ejercicio 09. Máximo común divisor

Definir mcd(a,b) mediante Euclides. Aceptar enteros, usar valores absolutos y definir mcd(0,0)=0. Probar 48 y 18.

**Caso de comprobación:**

```text
6
```

#### Ejercicio 10. Composición

Definir costo(cantidad,precio) y aplicar_descuento(total,porcentaje). Validar dominios y componerlas para 4 artículos a 12 con 25% de descuento.

**Caso de comprobación:**

```text
36.00
```

<a id="pc"></a>

## 3. PC3.05 · Práctica de clase

Definir es_primo(n), contar_primos(inicio, fin) y una función de presentación. Aceptar enteros y un intervalo con inicio <= fin. Considerar que números menores que 2 no son primos. Retornar resultados desde las funciones de cálculo y mostrar desde la función de presentación. Rechazar intervalos invertidos con un error explícito.

### Requisitos y restricciones

- Resolver en una sola versión, Python o Java.
- Mantener nombres y responsabilidades indicados; explicar cualquier adaptación idiomática.
- Aplicar únicamente los conceptos ya introducidos.
- Conservar las entradas cuando el enunciado lo exija.
- Distinguir valores fuera de contrato de errores que el programa debe gestionar.

### Casos de aceptación de la PC

| Entrada / escenario | Resultado esperado |
|---|---|
| 2, 10 | 4 primos |
| -3, 1 | 0 primos |
| 7, 7 | 1 primo |
| 10, 2 | intervalo inválido |

### Probar y registrar evidencia

Crear una carpeta personal `PC3.05` separada de las demostraciones. Guardar cada caso con entrada, resultado esperado y resultado real. Compilar `javac -encoding UTF-8 -d build *.java` y ejecutar `java -cp build Solucion`; usar `Solucion.java` como entrada personal. Para entradas de teclado, guardar `casos/entrada-01.txt` y redirigirla con `< casos/entrada-01.txt`. Para funciones, crear llamadas con los datos de la tabla.

- Registrar `evidencias/PC3.05.md` con comandos, versión real, salidas y explicación.
- Crear un commit funcional como `feat(pc3.05): implementar-regla-principal`.
- Obtener el hash real con `git rev-parse HEAD` y anotarlo en la evidencia.
- Revisar el cambio con `git show HASH` y comparar avances con `git diff HASH_ANTERIOR HASH_ACTUAL`. Sustituir los marcadores por hashes reales.
- Agregar una prueba de frontera distinta de las incluidas y justificar qué error detectaría.

No se requiere proyecto acumulativo ni rúbrica individual de esta PC.

<a id="esencial"></a>

## Lo esencial

- Escribir contratos antes del cuerpo.
- Retornar datos y separar presentación.
- Probar cada función de manera aislada.

## Referencias técnicas

- [Aprender Java, sitio oficial](https://dev.java/learn/)
- [API de Java SE 27](https://docs.oracle.com/en/java/javase/27/docs/api/)

[Versión Python](../python/material.md) · [Presentación Python](../presentacion.pptx) · [Anterior](../../3.04-iteracion/java/material.md) · [Siguiente](../../3.06-cadenas/java/material.md)
