# Commits y evidencias

Crear un repositorio personal para actividades independientes, sin modificar las demostraciones del material.

```bash
git init
git add README.md
git commit -m "docs: definir-organizacion-del-trabajo"
```

Configurar identidad Git local si todavía no existe. No copiar identidad de otra persona. Crear un directorio por PC o PL, desarrollar un cambio funcional, ejecutar los casos y registrar evidencia.

```bash
git add actividades/PC3.05 evidencias/PC3.05.md
git commit -m "feat(pc3.05): implementar-funciones-y-casos"
git rev-parse HEAD
git log --oneline -- actividades/PC3.05
git show HASH_REAL
git diff HASH_ANTERIOR HASH_ACTUAL -- actividades/PC3.05
```

Sustituir los marcadores por hashes reales. Revisar que el commit incluya tanto la implementación como las pruebas relacionadas. Registrar el hash después de crear el commit y añadir la evidencia de identificación en un commit posterior si hace falta evitar autorreferencia.

## Evidencia mínima

Registrar problema, versión, comando exacto, entrada, resultado esperado, resultado real, explicación de errores y enlace o hash. No simular capturas, resultados ni historial. Excluir credenciales, datos personales, entornos virtuales, cachés y compilados.
