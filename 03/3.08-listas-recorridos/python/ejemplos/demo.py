def filtrar_positivos(datos):
    resultado = []
    for valor in datos:
        if valor > 0:
            resultado.append(valor)
    return resultado

datos = [-2, 5, 0, 8, 5]
resultado = filtrar_positivos(datos)
print(" ".join(str(x) for x in resultado))
print(f"Suma: {sum(resultado)}")
