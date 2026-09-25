def contar_vocales(texto):
    cantidad = 0
    for letra in texto.lower():
        if letra in "aeiou":
            cantidad += 1
    return cantidad

nombre = "  Cuenca  ".strip()
print(nombre)
print(f"Vocales: {contar_vocales(nombre)}")
