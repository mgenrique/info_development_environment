# Sincronización de cambios entre la versión local y el repositorio de GitHub y acceso directo en el escritorio de Ubuntu

## Crear Script
Para crear un script que automatice el proceso de sincronización de cambios entre la versión local y el repositorio de GitHub. Este script puede realizar las siguientes tareas:

1. Hacer un **pull** para asegurarse de que tienes los cambios más recientes desde GitHub.
2. Añadir automáticamente los cambios locales al área de preparación.
3. Realizar un *commit* con un mensaje personalizado.
4. Hacer un *push* para subir los cambios a GitHub.

A continuación te explico cómo crear este script en Bash.

### 1. **Crea un archivo de script**

En tu terminal, navega al directorio donde quieras crear el script y usa un editor de texto (como `nano` o `vim`) para crear el archivo de script, por ejemplo:

```bash
nano sync_with_github.sh
```

### 2. **Escribe el script**

Copia el siguiente contenido dentro del archivo `sync_with_github.sh`. Este script incluye pasos básicos para sincronizar los cambios entre tu repositorio local y GitHub:

```bash
#!/bin/bash

# Cambiar al directorio del repositorio
cd /home/enrique/dev_ha_cc_pv_controller || { echo "No se pudo acceder al directorio /home/enrique/dev_ha_cc_pv_controller"; exit 1; }

# Nombre de la rama principal (puedes cambiar esto a "master" si tu rama principal se llama así)
BRANCH="main"

# Verificar si hay cambios locales sin hacer commit
if [[ `git status --porcelain` ]]; then
  echo "Hay cambios locales. Iniciando el proceso de sincronización."

  # Hacer un git pull para obtener los últimos cambios del repositorio remoto
  echo "Obteniendo los últimos cambios desde GitHub..."
  git pull origin $BRANCH

  # Añadir todos los archivos modificados al área de preparación
  echo "Añadiendo archivos al área de preparación..."
  git add .

  # Solicitar un mensaje para el commit
  echo "Introduce un mensaje para el commit: "
  read COMMIT_MESSAGE

  # Realizar el commit con el mensaje proporcionado
  echo "Haciendo commit de los cambios..."
  git commit -m "$COMMIT_MESSAGE"

  # Subir los cambios al repositorio remoto
  echo "Subiendo cambios a GitHub..."
  git push origin $BRANCH

  echo "¡Sincronización completada con éxito!"
else
  echo "No hay cambios locales. Solo haciendo pull para actualizar."
  git pull origin $BRANCH
fi

```

Este script hace lo siguiente:
1. Verifica si tienes cambios locales pendientes.
2. Si hay cambios, los añade al área de preparación, te pide un mensaje de *commit*, y hace un *commit*.
3. Luego, hace un *push* al repositorio remoto.
4. Si no hay cambios locales, simplemente hace un *pull* para asegurarse de que tu repositorio local esté actualizado.

### 3. **Haz el script ejecutable**

Una vez que hayas guardado el archivo, debes hacer que el script sea ejecutable con el siguiente comando:

```bash
chmod +x sync_with_github.sh
```

### 4. **Ejecuta el script**

Ahora puedes ejecutar el script en el directorio de tu repositorio local de GitHub usando:

```bash
./sync_with_github.sh
```

El script verificará si hay cambios locales, pedirá un mensaje de *commit* si los hay, y luego subirá esos cambios a GitHub. Si no hay cambios, simplemente traerá los cambios remotos con un *pull*.

### 5. **Consejos adicionales**

- Si trabajas en una rama diferente, puedes cambiar la variable `BRANCH` al nombre de tu rama (por ejemplo, `dev`).
- Este script es bastante básico, pero puedes extenderlo fácilmente para manejar ramas múltiples o realizar más operaciones automatizadas.

Este script debería ayudarte a automatizar el flujo básico de trabajo con Git entre tu repositorio local y GitHub.

## Acceso directo en el escritorio de Ubuntu para ejecutar el Script con doble click

Para crear un atajo en el escritorio de Ubuntu que ejecute tu script en una terminal, puedes crear un archivo `.desktop` que actúe como un lanzador de aplicaciones. Aquí te explico cómo hacerlo:

### 1. **Asegúrate de que el script esté listo**

Primero, verifica que tu script (`sync_with_github.sh`) sea ejecutable y esté funcionando correctamente. Asegúrate de haber dado permisos de ejecución:

```bash
chmod +x /ruta/al/script/sync_with_github.sh
```

### 2. **Crea un archivo `.desktop` en el escritorio**

Debes crear un archivo de tipo `.desktop` que actuará como un acceso directo en tu escritorio. Aquí están los pasos:

1. Abre un terminal y navega a tu escritorio:

   ```bash
   cd ~/Escritorio
   ```

2. Usa un editor de texto (por ejemplo, `nano`) para crear un archivo `.desktop`, por ejemplo `sync_with_github.desktop`:

   ```bash
   nano sync_with_github.desktop
   ```

3. Añade el siguiente contenido al archivo. Este lanzador abrirá una terminal de Ubuntu y ejecutará tu script:

   ```ini
   [Desktop Entry]
   Name=Sync with GitHub
   Comment=Sincroniza tu repositorio local con GitHub
   Exec=gnome-terminal -- /bin/bash -c "/ruta/al/script/sync_with_github.sh; exec bash"
   Icon=utilities-terminal
   Terminal=false
   Type=Application
   Categories=Development;
   ```

   - **Name**: El nombre que aparecerá en el icono.
   - **Comment**: Un breve comentario que aparece cuando pasas el cursor por encima del icono.
   - **Exec**: Este es el comando que ejecutará el script. Aquí usamos `gnome-terminal` para abrir una terminal de Ubuntu y luego ejecutar tu script. El `exec bash` al final mantiene abierta la terminal después de que el script termine.
   - **Icon**: Puedes cambiarlo a cualquier icono que prefieras o usar uno predeterminado como `utilities-terminal`.
   - **Terminal**: Debe estar en `false` ya que el script se ejecuta en una terminal de manera independiente.

4. Guarda el archivo y sal del editor (en `nano`, presiona `Ctrl+O` para guardar y `Ctrl+X` para salir).

### 3. **Haz que el archivo `.desktop` sea ejecutable**

Una vez creado el archivo `.desktop`, debes hacer que sea ejecutable:

```bash
chmod +x ~/Escritorio/sync_with_github.desktop
```

### 4. **Prueba el acceso directo**

Ahora deberías ver un nuevo icono en tu escritorio llamado "Sync with GitHub". Haz doble clic sobre él para ejecutarlo. Si el sistema te pregunta si quieres confiar en el lanzador, selecciona la opción de "Trust and Launch" (Confiar y Lanzar).

### 5. **Solución de problemas con permisos**

Si al hacer doble clic sobre el icono no pasa nada, es posible que tengas que ajustar las preferencias para permitir que los archivos `.desktop` se ejecuten directamente. Para hacer esto:

- Abre **Archivos (Nautilus)**.
- Navega a la carpeta **Escritorio**.
- Haz clic derecho en el archivo `sync_with_github.desktop` y selecciona **Propiedades**.
- Ve a la pestaña **Permisos** y asegúrate de que la opción **Permitir ejecutar como un programa** esté seleccionada.

### Resumen de pasos:
1. Asegúrate de que tu script es ejecutable.
2. Crea un archivo `.desktop` en tu escritorio.
3. Especifica que el lanzador abra una terminal y ejecute tu script.
4. Haz que el archivo `.desktop` sea ejecutable.
5. Haz doble clic en el icono para ejecutar el script.

Este método te permitirá crear un atajo en el escritorio que abrirá una terminal y ejecutará tu script para sincronizar tus cambios con GitHub.
