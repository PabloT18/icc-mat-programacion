def clasificar(matriz):
    resultado = []
    for fila in matriz:
        nueva = []
        for valor in fila:
            nueva.append("ALTA" if valor >= 20 else "BAJA")
        resultado.append(nueva)
    return resultado

original = [[18, 22, 20], [25, 15, 19]]
for fila in clasificar(original):
    print(" | ".join(fila))
print(f"Original: {original[0][0]}")
