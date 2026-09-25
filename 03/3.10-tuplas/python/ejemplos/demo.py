productos = [("P01", 8), ("P02", 0), ("P03", 4)]
for codigo, cantidad in productos:
    if cantidad > 0:
        print(f"{codigo}: {cantidad}")
