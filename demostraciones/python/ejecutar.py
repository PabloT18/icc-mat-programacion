from pathlib import Path
import sys, subprocess, tempfile, json
ROOT = Path(__file__).resolve().parents[2]
LANGUAGE = 'python'
if len(sys.argv) != 2:
    raise SystemExit("Uso: python3 demostraciones/" + LANGUAGE + "/ejecutar.py CODIGO")
catalog = json.loads((ROOT / "assets/catalogo.json").read_text(encoding="utf-8"))
topic = next((t for t in catalog["topics"] if t["curricular_code"] == sys.argv[1] and t["language"] == LANGUAGE), None)
if topic is None:
    raise SystemExit("Código de contenido desconocido")
folder = ROOT / topic["path"] / "ejemplos"
stdin = (folder / "entrada.txt").read_text(encoding="utf-8") if (folder / "entrada.txt").exists() else ""
if LANGUAGE == "python":
    result = subprocess.run([sys.executable, "demo.py"], cwd=folder, input=stdin, text=True)
else:
    with tempfile.TemporaryDirectory() as build:
        subprocess.run(["javac", "-encoding", "UTF-8", "-d", build] + [str(p) for p in folder.glob("*.java")], check=True)
        result = subprocess.run(["java", "-cp", build, "Demo"], cwd=folder, input=stdin, text=True)
raise SystemExit(result.returncode)
