# Instalar **Home Assistant Core** en un PC con **Windows 10** y **Visual Studio Code** en un entorno virtual aislado

Instalar **Home Assistant Core** en un PC con **Windows 10** y **Visual Studio Code** en un entorno virtual aislado es una excelente opción para desarrollar y probar componentes personalizados de manera local. A continuación te muestro cómo hacerlo paso a paso:

### Requisitos previos:

1. **Instalar WSL (Windows Subsystem for Linux)**:
   - Home Assistant Core no se puede ejecutar nativamente en Windows, por lo que necesitas un entorno Linux utilizando **WSL** (preferentemente **WSL 2**).
   - WSL 2 permite ejecutar una distribución de Linux en Windows. Recomendamos usar **Ubuntu** como distribución.

2. **Instalar Visual Studio Code** (ya lo tienes) y el **WSL Extension**:
   - Asegúrate de que tienes **Visual Studio Code** instalado y agrega la extensión **WSL** para desarrollar dentro del entorno Linux.

### Paso 1: Instalar WSL 2 y Ubuntu en Windows 10

1. **Habilitar WSL**:
   - Abre **PowerShell** como administrador y ejecuta el siguiente comando para habilitar WSL:
     ```bash
     wsl --install
     ```

   - Esto instalará WSL 2 automáticamente y establecerá una distribución de Linux predeterminada (generalmente Ubuntu). Si ya tienes WSL 1 instalado, puedes actualizar a WSL 2 con:
     ```bash
     wsl --set-default-version 2
     ```

2. **Instalar Ubuntu**:
   - Desde la **Microsoft Store**, busca "Ubuntu" y selecciona **Ubuntu 20.04 LTS** o una versión similar para instalarla.

3. **Configurar Ubuntu**:
   - Abre **Ubuntu** desde el menú de inicio de Windows y sigue las instrucciones para configurar un nombre de usuario y contraseña.
   - Actualiza los paquetes del sistema:
     ```bash
     sudo apt update && sudo apt upgrade -y
     ```

### Paso 2: Instalar Python y dependencias necesarias

1. **Instalar Python 3.10 o superior**:
   - Home Assistant Core requiere **Python 3.10** o superior, por lo que primero necesitas instalarlo en tu entorno WSL (si no está instalado).
   - Ejecuta los siguientes comandos en tu terminal de Ubuntu:
     ```bash
     sudo apt update
     sudo apt install python3.10 python3.10-venv python3.10-dev -y
     ```

2. **Verificar la versión de Python**:
   - Verifica que la versión de Python instalada es la correcta:
     ```bash
     python3.10 --version
     ```

### Paso 3: Crear un entorno virtual (venv) en WSL

1. **Crear un directorio para Home Assistant Core**:
   - Crea un directorio en tu sistema donde ejecutarás Home Assistant Core:
     ```bash
     mkdir homeassistant
     cd homeassistant
     ```

2. **Crear un entorno virtual de Python**:
   - Dentro del directorio, crea el entorno virtual:
     ```bash
     python3.10 -m venv venv
     ```

3. **Activar el entorno virtual**:
   - Activa el entorno virtual para aislar las dependencias:
     ```bash
     source venv/bin/activate
     ```

4. **Actualizar `pip` y otras herramientas**:
   - Asegúrate de que `pip` y `setuptools` estén actualizados:
     ```bash
     pip install --upgrade pip setuptools wheel
     ```

### Paso 4: Instalar Home Assistant Core en el entorno virtual

1. **Instalar Home Assistant Core**:
   - Instala Home Assistant Core en el entorno virtual:
     ```bash
     pip install homeassistant
     ```

2. **Iniciar Home Assistant**:
   - Ejecuta Home Assistant para iniciar el servidor:
     ```bash
     hass
     ```

   - La primera vez, Home Assistant descargará algunos archivos adicionales y puede tardar unos minutos en inicializarse.
   - Cuando veas el mensaje "Home Assistant is running", puedes acceder a la interfaz web abriendo un navegador y yendo a:
     ```
     http://localhost:8123
     ```

   - Desde aquí, puedes configurar Home Assistant y comenzar a usarlo.

### Paso 5: Integrar Visual Studio Code con WSL y Home Assistant

1. **Abrir Visual Studio Code** en modo WSL:
   - Abre **Visual Studio Code** y utiliza la extensión **WSL** para conectarte al entorno WSL.
   - Desde VS Code, presiona `Ctrl + Shift + P` y selecciona "WSL: Reopen Folder in WSL" para abrir el directorio de Home Assistant en tu entorno WSL.

2. **Instalar extensiones recomendadas para Home Assistant**:
   - Instala las siguientes extensiones en VS Code para mejorar el flujo de trabajo con Home Assistant:
     - **Home Assistant Config Helper**: Facilita la edición de archivos de configuración.
     - **Python**: Para trabajar con código Python y entornos virtuales.
     - **WSL**: Para trabajar en entornos WSL.

3. **Desarrollar y depurar el componente personalizado**:
   - Ahora puedes comenzar a trabajar en tu componente dentro del directorio `custom_components` en tu instalación de Home Assistant.
   - Puedes usar los comandos estándar de Python y Home Assistant desde tu entorno WSL, y recargar los componentes personalizados desde la interfaz de Home Assistant como lo hemos discutido anteriormente.

### Paso 6: Probar y depurar

1. **Probar y depurar el componente**:
   - Coloca tu componente en la carpeta `custom_components` y sigue los pasos que te expliqué antes para probar y depurar.
   - Recuerda ajustar los niveles de logging en `configuration.yaml` y revisar los logs en la interfaz de Home Assistant.

### Resumen:

1. **Instala WSL 2 y Ubuntu en Windows 10**.
2. **Instala Python 3.10** y crea un entorno virtual.
3. **Instala Home Assistant Core** en el entorno virtual.
4. Usa **Visual Studio Code** con **WSL** para desarrollar y depurar tu componente.
5. Prueba tu componente en **Home Assistant** y usa los logs para depuración.

Con este flujo de trabajo, tendrás un entorno completamente aislado para desarrollar y probar tu componente personalizado de Home Assistant en Windows 10. ¡Avísame si tienes alguna pregunta o si te surge algún problema durante la instalación!
