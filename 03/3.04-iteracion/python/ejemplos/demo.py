total = 0
cantidad = 0
for numero in range(1, 11):
    if numero % 2 == 0:
        total += numero
        cantidad += 1
print(f"Cantidad: {cantidad}")
print(f"Suma: {total}")
