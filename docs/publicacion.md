# Mantenimiento y publicación

## Uso local

Abrir `index.html` después de descomprimir o servir con `python3 -m http.server 8000`. Los HTML están generados y no requieren Node para consultarlos. No se ha publicado ningún sitio ni creado un repositorio remoto.

## Regeneración

Ejecutar desde la raíz:

```bash
node scripts/sync-examples.mjs --check
node scripts/build-site.mjs
node scripts/check-links.mjs
node scripts/stage-pages.mjs
```

El build sobrescribe HTML y `assets/js/course-data.js`. Cambiar CSS no requiere regeneración. Agregar o reordenar un tema requiere editar el catálogo y sus enlaces de navegación. Mantener las presentaciones por separado.

Publicar únicamente el contenido de `build/pages`. No publicar el ZIP docente completo. El staging excluye material reservado de soluciones y evaluación, así como entornos, cachés, compilados y metadatos de Git. No tratar ausencia de enlaces como control de acceso.

## GitHub Pages

El workflow incluido utiliza activación manual `workflow_dispatch`; no se ejecuta por subir archivos sin más. Antes de usarlo, crear el repositorio deseado, configurar Pages para GitHub Actions y revisar qué archivos se harán públicos. Ejecutar el workflow desde Actions cuando se decida publicar. Los identificadores de acciones del workflow corresponden a la configuración heredada de referencia y deben revisarse antes de una publicación futura.

También se puede copiar `build/pages` a un servidor estático autorizado. No cambiar rutas relativas por rutas locales del equipo. Comprobar enlaces después de desplegar. La entrega no incluye una URL publicada.

## Restricciones de PL

Cambiar `protection` a false en el catálogo y regenerar para desactivar por defecto. Cada guía tiene un botón accesible para activar o desactivar restricciones de selección, copia y algunos atajos. Se conserva navegación por teclado y uso de enlaces y controles. Estas restricciones no impiden capturas, acceso al HTML ni uso de IA. Evaluar mediante evidencia y defensa.
