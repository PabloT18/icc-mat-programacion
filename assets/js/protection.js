/* Dificultad superficial, configurable y desactivable para accesibilidad. */
(() => {
 const area=document.querySelector('[data-protected]'),button=document.getElementById('toggleProtection');if(!area)return;
 let enabled=area.dataset.protected==='true';
 const editable=target=>target instanceof Element&&Boolean(target.closest('input,textarea,select,button,a,[contenteditable="true"]'));
 function refresh(){area.classList.toggle('protected',enabled);if(button){button.setAttribute('aria-pressed',String(enabled));button.textContent=enabled?'Desactivar restricciones de selección':'Activar restricciones de selección';}}
 for(const name of ['contextmenu','selectstart','copy','cut','dragstart'])area.addEventListener(name,event=>{if(enabled&&!editable(event.target))event.preventDefault();});
 document.addEventListener('keydown',event=>{if(!enabled||editable(event.target))return;const key=event.key.toLowerCase();if((event.ctrlKey||event.metaKey)&&['c','s','u','a'].includes(key))event.preventDefault();});
 button?.addEventListener('click',()=>{enabled=!enabled;refresh();});refresh();
})();
