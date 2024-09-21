# Instalar Home Assistant Core en un PC con Ubuntu y Visual Studio Code en un entorno virtual aislado

El proceso para instalar y configurar **Home Assistant Core** y desarrollar componentes personalizados en un entorno virtual aislado es más sencillo que en Windows porque no se necesita WSL. 

A continuación te detallo los pasos específicos para **desarrollar Home Assistant Core en Ubuntu**:

### 1. Instalar dependencias básicas en Ubuntu

Primero, necesitas instalar algunas herramientas básicas para configurar el entorno de desarrollo.

1. **Actualiza los paquetes del sistema**:
   - Abre una terminal y ejecuta los siguientes comandos para asegurarte de que todos los paquetes están actualizados:
     ```bash
     sudo apt update && sudo apt upgrade -y
     ```

2. **Instalar Python 3.12**:
   - Home Assistant Core requiere **Python 3.10** o superior. Puedes instalar Python 3.12 con los siguientes comandos:

     Si tienes ya otro Python instalado lo puedes comprobar con
     ````bash
     python3 --version
     which python3
     ````
     Si te arroja por ejemplo `Python 3.12.3` instalado en `/usr/bin/python3` puedes simplemente hacer
     ````bash
     sudo apt install python3-dev python3-pip python3-venv python3-sqlalchemy libffi-dev build-essential cargo     
     ````
     

4. Instalar otras dependencias **NO NECESARIO**:
   En la busquedade una solución al Error de TurboJPEG, intente poner mas paquetes que no resolvieron el fallo.
   Se gun se indica en https://github.com/home-assistant/core/issues/114997
   No tiene solución por el momento. Este fallo desaparece en las instlaciones con contenedores.
   No parece importante ya que Home Assistant arranca igual a pesar del error.
   **NO NECESARIO**
   - También necesitarás algunos paquetes adicionales como `gcc` para compilar algunas dependencias de Home Assistant:
     ```bash
     sudo apt install build-essential libffi-dev libssl-dev python3-pip -y
     sudo apt install libturbojpeg
     sudo apt install libjpeg-turbo8-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev
     ```

### 2. Crear un entorno virtual para Home Assistant

Por ejemplo si quieres que el entorno virtual se instale en la carpeta `ha01` de la carpeta raiz del usuario `~`:
```bash
cd ~
python3 -m venv ha01
cd ha01
```
Para activar el entrono virtual
```bash
cd ~/ha01
source bin/activate
```
O en un solo paso
```bash
source ~/ha0/bin/activate
```

Asegúrate de tener la última versión de `pip`, `setuptools` y `wheel`:
```bash
pip install --upgrade pip setuptools wheel
```


### 3. Instalar Home Assistant Core

1. **Instalar Home Assistant Core**:
   - Una vez activado el entorno virtual, instala Home Assistant Core:
     ```bash
     pip3 install homeassistant
     ```

2. **Iniciar Home Assistant Core**:
   - Inicia Home Assistant Core:
     ```bash
     hass
     ```

   - La primera vez, Home Assistant descargará algunos archivos adicionales y puede tardar unos minutos en inicializarse. Una vez que esté ejecutándose, deberías ver un mensaje que diga "Home Assistant is running".
   - Accede a la interfaz web desde tu navegador en la siguiente URL:
     ```
     http://localhost:8123
     ```

   - Desde aquí puedes realizar la configuración inicial de Home Assistant.

### 4. Configurar Visual Studio Code para el desarrollo

1. **Instalar Visual Studio Code en Ubuntu**:
   - Si no lo tienes instalado, puedes instalar **Visual Studio Code** en Ubuntu utilizando las siguientes instrucciones:
     - Descarga el archivo `.deb` desde la [página oficial de Visual Studio Code](https://code.visualstudio.com/).
     - O bien, instálalo directamente desde el terminal:
       ```bash
       sudo snap install --classic code
       ```

2. **Abrir el proyecto en Visual Studio Code**:
   - Abre el directorio `ha01` en Visual Studio Code:
     ```bash
     code ha01
     ```

3. **Instalar extensiones útiles**:
   - Para facilitar el desarrollo de tu componente, instala las siguientes extensiones:
     - **Python**: Para soporte de sintaxis y depuración de código Python.
     - **Home Assistant Config Helper**: Para obtener sugerencias y validaciones al editar archivos de configuración de Home Assistant.

### 5. Desarrollar tu componente personalizado

1. **Crear la carpeta `custom_components`**:
   - Dentro del directorio donde tienes instalado Home Assistant (en `homeassistant`), crea un directorio para tu componente personalizado:
     ```bash
     mkdir -p custom_components/pv_controller
     ```

2. **Coloca tu componente**:
   - Asegúrate de que el código de tu componente esté en el directorio `custom_components/pv_controller`. La estructura debe verse así:
     ```
     /homeassistant
       └── custom_components
           └── pv_controller
               ├── __init__.py
               ├── manifest.json
               ├── sensor.py
               ├── config_flow.py
               ├── state_machine.py
               ├── const.py
     ```

3. **Configurar el logging**:
   - Configura el logging detallado en `configuration.yaml` para que puedas ver los mensajes de depuración:
     ```yaml
     logger:
       default: warning
       logs:
         custom_components.pv_controller: debug
     ```

### 6. Ejecutar y probar el componente

1. **Reiniciar Home Assistant**:
   - Después de colocar el componente, reinicia Home Assistant para que cargue tu componente personalizado:
     ```bash
     hass --config /ruta/a/tu/config
     ```

2. **Verificar el componente en la interfaz de Home Assistant**:
   - Accede nuevamente a **http://localhost:8123** y ve a **Configuración -> Dispositivos y Servicios**.
   - Busca tu componente `PV Controller` y sigue el flujo de configuración que has definido en el archivo `config_flow.py`.

3. **Revisar los logs**:
   - Ve a **Herramientas para desarrolladores -> Registro** y verifica si hay mensajes de error o advertencia relacionados con tu componente.
   - También puedes revisar el archivo `home-assistant.log` en el directorio de configuración para obtener más detalles.

4. **Recargar el componente sin reiniciar Home Assistant**:
   - Si haces cambios en el código del componente, puedes recargarlo sin reiniciar todo Home Assistant. Ve a **Configuración -> Controles del servidor** y selecciona **Recargar componentes personalizados**.

### 7. Depurar el componente

1. **Prueba los sensores**:
   - Ve a **Herramientas para desarrolladores -> Estados** y busca los sensores que has creado (`sensor.pvpc_sensor`, `sensor.solar_forecast_sensor`, `sensor.pv_controller_state`).
   - Verifica si sus estados son correctos y si los datos se están actualizando como esperas.

2. **Depurar la máquina de estados**:
   - Asegúrate de que la máquina de estados `CicloStateMachine` está funcionando correctamente. Puedes revisar el estado en el sensor `PVControllerStateSensor`.

3. **Revisar la frecuencia de actualización**:
   - Verifica que las llamadas a la API de Forecast Solar no se hagan con demasiada frecuencia y que se respete el valor definido en `MIN_TIME_BETWEEN_UPDATES_SOLARFORECAST`.

### 8. Optimizar y ajustar el código

- Realiza ajustes y optimizaciones en tu código según los resultados de las pruebas.
- Usa los logs para identificar problemas y depurar cualquier comportamiento inesperado.

### Resumen:

1. Instala las dependencias en Ubuntu, incluyendo **Python 3.10** y los paquetes necesarios.
2. Crea un entorno virtual para aislar las dependencias y luego instala **Home Assistant Core**.
3. Usa **Visual Studio Code** para editar y depurar el código del componente personalizado.
4. Prueba y depura el componente en Home Assistant, revisando los logs y recargando el componente según sea necesario.

Con este flujo de trabajo, podrás desarrollar y probar eficientemente tu componente en **Ubuntu**. ¡Si tienes alguna duda o necesitas más detalles, no dudes en preguntarme!

````bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-dev python3-pip python3-venv python3-sqlalchemy libffi-dev build-essential cargo
cd ~
python3 -m venv ha01
cd ha01
source bin/activate
python3 -m pip install wheel
pip3 install homeassistant



mkdir -p ~/ha01
cd ~/ha01
python3 -m venv homeassistant
cd homeassistant
source bin/activate
python3 -m pip install wheel
pip3 install homeassistant


python3 -m pip install wheel
````
