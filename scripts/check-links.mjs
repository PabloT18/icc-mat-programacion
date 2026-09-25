import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const errors=[];let checked=0,anchors=0;const cache=new Map();
async function walk(dir){let out=[];for(const e of await fs.readdir(dir,{withFileTypes:true})){if(['build','node_modules','.git','vendor'].includes(e.name))continue;const p=path.join(dir,e.name);if(e.isDirectory())out.push(...await walk(p));else out.push(p);}return out;}
async function text(p){if(!cache.has(p))cache.set(p,await fs.readFile(p,'utf8'));return cache.get(p);}
for(const file of await walk(root)){
 if(!/\.(html|md)$/.test(file))continue;
 const content=await text(file);const links=[];
 for(const m of content.matchAll(/(?:href|src)="([^"]+)"/g))links.push(m[1]);
 if(file.endsWith('.md'))for(const m of content.matchAll(/!?\[[^\]]*\]\(([^\s)]+)\)/g))links.push(m[1]);
 for(let link of links){
  if(/^(?:https?:|mailto:|data:|javascript:)/i.test(link))continue;
  link=link.replace(/&amp;/g,'&');const [filePart,hash]=link.split('#');
  const target=filePart?path.resolve(path.dirname(file),decodeURIComponent(filePart.split('?')[0])):file;
  checked++;try{await fs.access(target);}catch{errors.push(path.relative(root,file)+' -> '+link);continue;}
  if(hash&&/\.(html|md)$/.test(target)){
   const targetContent=await text(target),id=decodeURIComponent(hash);anchors++;
   if(!targetContent.includes('id="'+id+'"')&&!targetContent.includes("id='"+id+"'"))errors.push(path.relative(root,file)+' -> ancla ausente '+link);
  }
 }
}
if(errors.length){console.error(errors.join('\n'));process.exitCode=1;}else console.log(`Destinos locales: ${checked}; anclas explícitas: ${anchors}; errores: 0. No se consultan enlaces externos.`);
