
# Sincronizar un Fork en Visual Studio Code con Dev Containers

Puedes sincronizar un fork en Visual Studio Code (VSC) para un proyecto que esté usando **Dev Containers**, de manera similar a como lo harías desde la línea de comandos. A continuación te explico cómo hacerlo dentro del entorno de Dev Containers en VSC:

## 1. Acceder al Terminal dentro del Dev Container
- Abre tu proyecto en VSC y asegúrate de que el Dev Container esté activo. Si no es así, inicia el Dev Container desde la opción de "Reabrir en Container" en la paleta de comandos (`Ctrl+Shift+P` y busca "Dev Containers: Reopen in Container`).
- Una vez dentro del contenedor, abre una terminal desde el menú `Terminal > New Terminal` o usa el atajo `Ctrl+``.

## 2. Añadir el repositorio original como `upstream`
En la terminal de VSC, dentro del Dev Container, puedes seguir los mismos pasos que usarías en un entorno local:
```bash
git remote add upstream https://github.com/home-assistant/core.git
```

## 3. Hacer `fetch` de los cambios del repositorio original
Obtén los últimos cambios del repositorio original con:
```bash
git fetch upstream
```

## 4. Realizar el `merge` de los cambios en tu rama local
Ahora puedes mezclar los cambios del repositorio original en tu rama local. Si estás trabajando en la rama `dev`:
```bash
git checkout dev
git merge upstream/dev
```
Si la rama principal se llama `master`, ajusta el comando a:
```bash
git merge upstream/master
```

## 5. Resolver conflictos si los hay
Si tienes conflictos durante el merge, VSC te ayudará a visualizarlos y resolverlos de forma interactiva. Podrás ver las secciones del código con conflictos y seleccionar qué cambios quieres mantener.

## 6. Subir los cambios a tu fork
Una vez que hayas hecho el merge y resuelto los conflictos (si existen), sube los cambios a tu fork en GitHub:
```bash
git push origin dev
```

## Resumen del flujo en VSC (Dev Containers):
1. Abre la terminal dentro del contenedor.
2. Agrega el repositorio original como remote (`upstream`).
3. Haz fetch de los cambios del upstream.
4. Realiza el merge de los cambios a tu rama.
5. Resuelve cualquier conflicto si aparece.
6. Sube los cambios a tu fork en GitHub.

Todo este proceso se realiza dentro del Dev Container en VSC, por lo que no necesitas salir del entorno.
