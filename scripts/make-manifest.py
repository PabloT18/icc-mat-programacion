"""Crear inventario real y SHA-256; ejecutar al terminar el build y la limpieza."""
from pathlib import Path
import hashlib
ROOT=Path(__file__).resolve().parents[1]
EXCLUDED={'build','node_modules','.git','__pycache__','.venv'}
def included(p):
    return not any(x in EXCLUDED for x in p.relative_to(ROOT).parts) and p.suffix not in {'.pyc','.class'}
tree=ROOT/'docs/arbol.txt'
files=sorted(p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and included(p))
for name in ['docs/arbol.txt','MANIFEST.sha256']:
    if name not in files:files.append(name)
tree.write_text('icc-pro-material/\n'+'\n'.join('  '+p for p in sorted(files))+'\n',encoding='utf-8')
files=sorted(p for p in ROOT.rglob('*') if p.is_file() and included(p) and p.name!='MANIFEST.sha256')
(ROOT/'MANIFEST.sha256').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(ROOT).as_posix()+'\n' for p in files),encoding='utf-8')
print(f'Manifiesto: {len(files)} archivos; no incluye su propio hash.')
