from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as carpeta:
    ruta = Path(carpeta) / "prueba.txt"
    ruta.write_text("Entorno listo", encoding="utf-8")
    print(ruta.read_text(encoding="utf-8"))
