import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..'),target=path.join(root,'build/pages');
await fs.rm(target,{recursive:true,force:true});await fs.mkdir(target,{recursive:true});
const excluded=new Set(['node_modules','.git','build','__pycache__','.venv','.github','moodle']);
for(const entry of await fs.readdir(root,{withFileTypes:true})){
 if(excluded.has(entry.name))continue;
 await fs.cp(path.join(root,entry.name),path.join(target,entry.name),{recursive:true,filter:p=>{const local=path.relative(root,p);return !local.split(path.sep).some(x=>excluded.has(x))&&!/\.(ipynb|pyc|class)$/.test(p)&&!p.endsWith('MANIFEST.sha256')&&!p.endsWith('arbol.txt');}});
}
console.log('Preparado build/pages; excluidos soluciones docentes y bancos de evaluación.');
