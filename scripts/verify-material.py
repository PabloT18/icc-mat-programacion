"""Comprobar demostraciones, rúbricas, XML y celdas de soluciones docentes.
Ejecutar con Python estándar. Requerir java y javac en PATH para Java.
"""
from pathlib import Path
import contextlib
import io
import json
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
catalog=json.loads((ROOT/'assets/catalogo.json').read_text(encoding='utf-8'))
records=[]
for topic in catalog['topics']:
    folder=ROOT/topic['path']/'ejemplos'
    expected=(folder/'salida-esperada.txt').read_text(encoding='utf-8')
    stdin=(folder/'entrada.txt').read_text(encoding='utf-8') if (folder/'entrada.txt').exists() else ''
    if topic['language']=='python':
        result=subprocess.run([sys.executable,'demo.py'],cwd=folder,input=stdin,text=True,capture_output=True,timeout=20)
    else:
        compiler=['javac'] if shutil.which('javac') else ['java','com.sun.tools.javac.Main']
        with tempfile.TemporaryDirectory() as build:
            compiled=subprocess.run(compiler+['-encoding','UTF-8','-d',build]+[str(p) for p in folder.glob('*.java')],text=True,capture_output=True,timeout=40)
            if compiled.returncode:
                raise RuntimeError(topic['id']+': '+compiled.stderr)
            result=subprocess.run(['java','-cp',build,'Demo'],cwd=folder,input=stdin,text=True,capture_output=True,timeout=20)
    ok=result.returncode==0 and result.stdout.strip()==expected.strip()
    records.append({'id':topic['id'],'ok':ok,'stdout':result.stdout,'stderr':result.stderr,'exit_code':result.returncode})
    if not ok: raise AssertionError(records[-1])
for lab in catalog['labs']:
    assert sum(c['points'] for c in lab['rubric'])==10,lab['id']
questions=0
for file in ROOT.glob('[0-9][0-9]/*/moodle/*.xml'):
    quiz=ET.parse(file).getroot()
    for q in quiz.findall('question'):
        if q.get('type')=='category':
            assert q.findtext('category/text').startswith('$course$/top/')
        else:
            assert q.get('type')=='multichoice'
            answers=q.findall('answer')
            assert len(answers)==4 and sum(a.get('fraction')=='100' for a in answers)==1
            assert len({a.findtext('text') for a in answers})==4
            questions+=1
cells=0
for file in ROOT.glob('03/*/python/*.ipynb'):
    notebook=json.loads(file.read_text(encoding='utf-8'))
    assert notebook['nbformat']==4
    for cell in notebook['cells']:
        if cell['cell_type']!='code': continue
        capture=io.StringIO()
        with contextlib.redirect_stdout(capture):exec(''.join(cell['source']),{'__name__':'__main__'})
        expected=''.join(''.join(o.get('text',[])) for o in cell['outputs'] if o.get('output_type')=='stream')
        assert capture.getvalue()==expected,str(file)
        cells+=1
report={'python':sys.version.split()[0],'demonstrations':records,'moodle_questions':questions,'executed_solution_cells':cells,'rubrics':len(catalog['labs'])}
out=ROOT/'docs/verificacion/material.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Demostraciones: {len(records)}; preguntas: {questions}; celdas ejecutadas: {cells}; rúbricas: {len(catalog["labs"])}. Sin errores.')
