medicion = 72
if medicion < 0 or medicion > 100:
    categoria = "Inválida"
elif medicion < 40:
    categoria = "Baja"
elif medicion <= 75:
    categoria = "Adecuada"
else:
    categoria = "Alta"
print(categoria)
