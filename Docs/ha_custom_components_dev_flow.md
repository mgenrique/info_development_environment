# Desarrollar custom components para Home Assistant utilizando Visual Studio Code

Para desarrollar **custom components** para **Home Assistant** utilizando **Visual Studio Code (VSC)**, el enfoque adecuado implica configurar un entorno de desarrollo que facilite la escritura de código, pruebas y despliegue del componente en una instancia de Home Assistant. Aquí te detallo los pasos clave para lograrlo:

### 1. **Configurar un entorno de desarrollo local con Docker**

Para facilitar el desarrollo, es útil ejecutar Home Assistant en un contenedor Docker, ya que puedes ejecutar y probar tus componentes en un entorno aislado y controlado. Puedes usar **Dev Containers** o simplemente manejar Docker manualmente.

#### Pasos para configurar Docker con Home Assistant:

1. **Instalar Docker y Docker Compose**: Si no lo has hecho, instala Docker en tu máquina.
2. **Crear un archivo `docker-compose.yml`** para ejecutar Home Assistant:
   ```yaml
   version: '3'
   services:
     homeassistant:
       container_name: home-assistant
       image: homeassistant/home-assistant:stable
       volumes:
         - ./config:/config  # Ruta local para los archivos de configuración
       ports:
         - "8123:8123"
       restart: unless-stopped
   ```
3. **Ejecutar Home Assistant**: En la terminal, ejecuta:
   ```bash
   docker-compose up -d
   ```
   Esto levantará una instancia de Home Assistant en `http://localhost:8123`.

4. **Configurar acceso a la carpeta de desarrollo del componente**: Puedes montar tu carpeta de desarrollo local en el contenedor de Home Assistant para que los cambios se reflejen automáticamente.

### 2. **Configurar Visual Studio Code para el desarrollo**

#### Extensiones recomendadas para VSC:

1. **Python**: Dado que los componentes personalizados de Home Assistant se desarrollan en Python, instala la extensión oficial de Python (`ms-python.python`).
2. **Docker**: Facilita la gestión de contenedores, imágenes y volúmenes directamente desde VS Code.
3. **Home Assistant Config Helper**: Extensión que proporciona sugerencias y autocompletado para archivos de configuración YAML específicos de Home Assistant.

#### Flujo de trabajo recomendado en VSC:

1. **Clonar el repositorio del componente o crear uno nuevo**: Si es un nuevo componente, crea una estructura básica del componente en la carpeta `custom_components` dentro del directorio de configuración de Home Assistant.

   Estructura básica:
   ```
   custom_components/
     my_component/
       __init__.py
       manifest.json
       sensor.py
   ```

2. **Configurar un entorno virtual (opcional)**: Aunque Docker proporciona un entorno aislado, puedes configurar un entorno virtual para el desarrollo si lo prefieres:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para activar el entorno virtual en Linux/Mac
   .\venv\Scripts\activate  # Para activar en Windows
   ```

3. **Instalar dependencias**: Algunas bibliotecas que utilices pueden necesitar instalación previa. Usa el archivo `requirements.txt` para gestionarlas y ejecuta:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar Dev Containers (opcional)**: Si prefieres trabajar en un contenedor, puedes usar un archivo `devcontainer.json` en tu proyecto para definir un entorno de desarrollo basado en Docker (ver ejemplos anteriores).

### 3. **Estructura básica del componente**

Un **custom component** en Home Assistant suele tener al menos tres archivos principales:

1. **`__init__.py`**: Este archivo inicializa el componente.
2. **`manifest.json`**: Contiene metadatos del componente, como nombre, versiones, dependencias y dominios.
3. **`sensor.py`** (o cualquier otro archivo relacionado con la plataforma): Define las entidades o sensores específicos que añade el componente.

#### Ejemplo básico de `manifest.json`:

```json
{
  "domain": "my_component",
  "name": "My Custom Component",
  "documentation": "https://github.com/tu-repositorio",
  "dependencies": [],
  "codeowners": ["@tu-nombre"],
  "requirements": ["requests>=2.23.0"]
}
```

### 4. **Correr Home Assistant y probar el componente**

Cada vez que hagas cambios en tu componente personalizado, puedes reiniciar Home Assistant desde el panel web (`http://localhost:8123`) o reiniciarlo desde Docker:

```bash
docker-compose restart
```

### 5. **Depuración y seguimiento de errores**

Puedes ver los registros (logs) de Home Assistant para depurar tu componente:

- Desde la interfaz de Home Assistant, ve a **Configuración > Registros**.
- Desde Docker:
  ```bash
  docker logs -f home-assistant
  ```

### 6. **Validación y linting del código**

- **Pylint**: Ejecuta `pylint` para verificar errores de sintaxis y adherencia a las convenciones de estilo en Python.
  ```bash
  pylint custom_components/my_component
  ```

- **Pruebas**: Si implementas pruebas unitarias con `pytest`, puedes configurar un entorno de pruebas para tu componente.

### 7. **Automatización del ciclo de desarrollo**

Puedes configurar tareas automáticas en VSC para realizar linting, pruebas o incluso despliegues cada vez que guardes un archivo o hagas un commit en tu repositorio. Usa la integración de **Git** para gestionar versiones y subir cambios.

---

### Resumen

El enfoque más adecuado para desarrollar **custom components** para Home Assistant con Visual Studio Code incluye:

1. **Configurar Docker** para ejecutar Home Assistant localmente.
2. **Configurar VS Code** con las extensiones necesarias (Python, Docker, Home Assistant Config Helper).
3. **Desarrollar el componente** en la carpeta `custom_components`.
4. **Probar y depurar** el componente en una instancia local de Home Assistant.
5. **Automatizar** tareas comunes (linting, pruebas) para mejorar la eficiencia durante el desarrollo.

Con este flujo, tendrás un entorno de desarrollo robusto y eficiente para crear y mantener componentes personalizados para Home Assistant.
