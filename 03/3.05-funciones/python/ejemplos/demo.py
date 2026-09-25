def costo_horas(horas, tarifa):
    if horas < 0 or tarifa < 0:
        raise ValueError("Valores negativos")
    return horas * tarifa

print(f"Costo: {costo_horas(3, 2.5):.2f}")
try:
    costo_horas(-1, 2.5)
except ValueError as error:
    print(error)
