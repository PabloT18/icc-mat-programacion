mediciones = [18, 21, 19]
copia = mediciones.copy()
copia.append(22)
print("Original:", " ".join(str(x) for x in mediciones))
print("Copia:", " ".join(str(x) for x in copia))
