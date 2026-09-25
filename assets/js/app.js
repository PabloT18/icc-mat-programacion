(() => {
 const data=window.COURSE; let unit=1,tab='material',language='python';
 const $=id=>document.getElementById(id);
 const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 function render(){
  $('listing').classList.remove('hidden');$('reader').classList.add('hidden');
  $('unitLabel').textContent=`UNIDAD ${String(unit).padStart(2,'0')}`;$('unitTitle').textContent=data.units[unit][0];
  document.querySelectorAll('[data-unit]').forEach(b=>{const active=Number(b.dataset.unit)===unit;b.classList.toggle('active',active);b.setAttribute('aria-current',active?'true':'false');});
  document.querySelectorAll('[data-tab]').forEach(b=>{const active=b.dataset.tab===tab;b.classList.toggle('active',active);b.setAttribute('aria-pressed',String(active));});
  $('language').value=language;
  if(tab==='material')$('resources').innerHTML='<ul class="topic-list">'+data.topics.filter(t=>t.unit===unit&&t.language===language).map(t=>`<li class="topic-row"><span class="topic-code">${esc(t.curricular_code)}</span><a class="topic-name" href="${t.path}/index.html" data-open="${t.id}">${esc(t.title)}</a><div class="topic-actions"><a class="open" href="${t.path}/index.html" data-open="${t.id}">Leer</a><a href="${t.path}/material.md" download>MD</a><a href="${t.pptx}" download>PPTX ${t.deck_language}</a></div></li>`).join('')+'</ul>';
  else $('resources').innerHTML='<p>Desarrollar todas las PL en Python.</p>'+data.labs.filter(l=>l.unit===unit).map(l=>`<article class="lab-card"><p class="eyebrow">${l.id}</p><h3>${esc(l.title)}</h3><p>${esc(l.problem)}</p><div class="topic-actions"><a class="open" data-open="${l.id}" href="${l.path}.html">Abrir guía</a><a href="${l.path}.pptx" download>PPTX</a></div></article>`).join('');
 }
 function item(id){return data.topics.find(t=>t.id===id)||data.labs.find(l=>l.id===id);}
 function updateHeader(entry){
  const topic=Boolean(entry.curricular_code);unit=entry.unit;if(topic)language=entry.language;
  $('readerTitle').textContent=(entry.curricular_code||entry.id)+' · '+entry.title;
  $('fullPage').href=entry.path+(topic?'/index.html':'.html');
  $('deckLink').href=topic?entry.pptx:entry.path+'.pptx';
  $('deckLink').textContent=topic?'PPTX '+entry.deck_language:'PPTX Python';
 }
 function openResource(id){const entry=item(id);if(!entry)return;updateHeader(entry);$('listing').classList.add('hidden');$('reader').classList.remove('hidden');$('viewer').src=$('fullPage').getAttribute('href');$('back').focus();}
 document.addEventListener('click',e=>{const unitButton=e.target.closest('[data-unit]');if(unitButton){unit=Number(unitButton.dataset.unit);render();return;}const tabButton=e.target.closest('[data-tab]');if(tabButton){tab=tabButton.dataset.tab;render();return;}const resource=e.target.closest('[data-open]');if(resource&&!e.ctrlKey&&!e.metaKey&&!e.shiftKey){e.preventDefault();openResource(resource.dataset.open);}});
 $('language').addEventListener('change',()=>{language=$('language').value;render();});
 $('back').addEventListener('click',()=>{render();$('unitTitle').tabIndex=-1;$('unitTitle').focus();});
 window.addEventListener('message',e=>{if(e.source!==$('viewer').contentWindow||e.data?.type!=='course-resource')return;const entry=item(e.data.id);if(entry)updateHeader(entry);});
 render();
})();
