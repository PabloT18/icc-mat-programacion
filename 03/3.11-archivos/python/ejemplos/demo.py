from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as carpeta:
    ruta = Path(carpeta) / "mediciones.txt"
    ruta.write_text("12\n8\n15\n", encoding="utf-8")
    total = 0
    with ruta.open(encoding="utf-8") as archivo:
        for linea in archivo:
            total += int(linea.strip())
    print(f"Total: {total}")
