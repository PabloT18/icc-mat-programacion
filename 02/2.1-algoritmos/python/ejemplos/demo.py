minutos = 125
if minutos < 0:
    print("Duración inválida")
else:
    horas = (minutos + 59) // 60
    print(f"Horas: {horas}")
    print(f"Costo: {horas * 2}")
