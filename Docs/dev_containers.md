# DEV CONTAINERS

**Dev Containers** es una característica de Visual Studio Code que permite a los desarrolladores trabajar en entornos de desarrollo preconfigurados dentro de contenedores Docker. Un *Dev Container* es, esencialmente, un contenedor Docker que incluye todas las dependencias, herramientas, y configuraciones necesarias para desarrollar una aplicación, asegurando que el entorno de desarrollo sea consistente en cualquier máquina o sistema operativo.

### ¿Qué son los *Dev Containers*?

Los *Dev Containers* proporcionan un entorno aislado que encapsula el código fuente, las herramientas de compilación, las bibliotecas, las dependencias, y cualquier configuración específica del entorno de desarrollo. Esto significa que, independientemente del sistema operativo o la configuración local de la máquina del desarrollador, el código siempre se ejecuta en el mismo entorno.

- **Portabilidad**: Los *Dev Containers* permiten mover fácilmente proyectos entre diferentes entornos sin preocuparse por diferencias en las configuraciones de herramientas o dependencias.
- **Consistencia**: Todos los desarrolladores en un equipo pueden trabajar con el mismo entorno de desarrollo, eliminando problemas relacionados con configuraciones locales que varían de una persona a otra.
- **Aislamiento**: Al estar basado en Docker, cada *Dev Container* es un entorno completamente aislado. Esto significa que puedes trabajar en múltiples proyectos sin que los entornos o las dependencias entre ellos entren en conflicto.

### ¿Cómo funcionan los *Dev Containers*?

1. **Definición del entorno**:
   El entorno de desarrollo de un *Dev Container* se define en un archivo `devcontainer.json`. Este archivo especifica:
   - Qué imagen Docker utilizar.
   - Qué extensiones de VS Code se deben instalar dentro del contenedor.
   - Configuraciones adicionales, como la apertura de puertos y variables de entorno.
   - Dependencias y comandos que deben ejecutarse al iniciar el contenedor.
   
2. **Creación del contenedor**:
   Cuando abres un proyecto que incluye un archivo `devcontainer.json`, Visual Studio Code usa Docker para construir y ejecutar un contenedor con la imagen y las configuraciones especificadas. Al ejecutarse, el editor se conecta al contenedor de manera transparente para el usuario.
   
3. **Trabajo dentro del contenedor**:
   Una vez que el *Dev Container* está corriendo, Visual Studio Code se conecta a este entorno. Todo el trabajo, incluidos los comandos del terminal, depuración, instalación de extensiones y ejecución de código, se realiza dentro del contenedor, pero desde la interfaz de VS Code como si estuvieras trabajando de manera local.

4. **Extensiones en el contenedor**:
   Visual Studio Code permite instalar y ejecutar extensiones tanto localmente como dentro del contenedor. Algunas extensiones necesarias para el proyecto pueden configurarse para que se instalen directamente en el contenedor, donde el código se ejecuta, mientras que otras permanecen en el entorno local.

### Beneficios clave

- **Reproducibilidad**: Cualquiera que clone el repositorio de código puede cargar el *Dev Container* y estar listo para trabajar con el mismo entorno que el resto del equipo.
- **Estandarización**: El entorno de desarrollo puede incluir compiladores, intérpretes, servidores, bases de datos, etc., lo que permite trabajar con múltiples tecnologías sin preocuparse por su instalación en la máquina local.
- **Simplificación de la configuración**: En lugar de seguir una larga lista de pasos para instalar herramientas y configurar un entorno de desarrollo, todo lo necesario está incluido en el contenedor.
- **Facilidad de pruebas en diferentes entornos**: Puedes definir múltiples *Dev Containers* para probar cómo se comporta tu aplicación en distintas versiones de un lenguaje o sistema operativo sin necesidad de múltiples configuraciones en tu sistema local.

### Ejemplo de un archivo `devcontainer.json`

```json
{
   "name": "Node.js Dev Container",
   "image": "mcr.microsoft.com/vscode/devcontainers/javascript-node:0-14",
   "extensions": [
      "dbaeumer.vscode-eslint",
      "esbenp.prettier-vscode"
   ],
   "postCreateCommand": "npm install",
   "forwardPorts": [3000],
   "settings": {
      "terminal.integrated.shell.linux": "/bin/bash"
   }
}
```

En este ejemplo:
- Se utiliza una imagen Docker basada en Node.js.
- Se instalan las extensiones de ESLint y Prettier dentro del contenedor.
- Se ejecuta el comando `npm install` después de la creación del contenedor.
- Se expone el puerto 3000 para que la aplicación dentro del contenedor pueda ser accesible desde la máquina local.

### Ejemplo de `devcontainer.json` para una aplicación Python
Ejemplo de un archivo `devcontainer.json` para una aplicación desarrollada con Python. Este archivo define un contenedor de desarrollo que incluye Python, extensiones útiles para desarrollo en Python y comandos para configurar el entorno.

```json
{
    "name": "Python Dev Container",
    "image": "mcr.microsoft.com/vscode/devcontainers/python:3.9",  // Imagen base de Python 3.9
    "features": {
        "ghcr.io/devcontainers/features/python:1": {
            "version": "3.9"
        }
    },
    "customizations": {
        "vscode": {
            "extensions": [
                "ms-python.python",  // Extensión principal de Python
                "ms-python.vscode-pylance",  // Pylance para análisis de código estático
                "ms-toolsai.jupyter"  // Soporte para Jupyter notebooks
            ],
            "settings": {
                "python.defaultInterpreterPath": "/usr/local/bin/python3",  // Ruta al intérprete de Python en el contenedor
                "python.linting.enabled": true,  // Activar linters para análisis de código
                "python.linting.pylintEnabled": true,  // Usar pylint como linter
                "python.formatting.autopep8Path": "/usr/local/bin/autopep8",  // Usar autopep8 para formatear
                "python.formatting.provider": "autopep8"  // Autoformateo con autopep8
            }
        }
    },
    "postCreateCommand": "pip install -r requirements.txt",  // Instalar las dependencias después de crear el contenedor
    "forwardPorts": [8000],  // Abrir el puerto 8000 para que la app sea accesible
    "mounts": [
        "source=/var/run/docker.sock,target=/var/run/docker.sock,type=bind"  // Montar el socket de Docker dentro del contenedor
    ],
    "remoteUser": "vscode"  // Usuario predeterminado para trabajar en el contenedor
}
```

### Explicación de los elementos:

1. **name**: El nombre del contenedor. En este caso, lo llamamos "Python Dev Container".
2. **image**: Utilizamos una imagen de Python 3.9 proporcionada por Microsoft, que está optimizada para trabajar con Visual Studio Code.
3. **features**: Usa una característica preconfigurada que garantiza que la versión de Python sea la 3.9.
4. **customizations**:
   - **extensions**: Se incluyen extensiones útiles para el desarrollo en Python:
     - `ms-python.python`: Extensión para trabajar con Python.
     - `ms-python.vscode-pylance`: Soporte avanzado de análisis de código con Pylance.
     - `ms-toolsai.jupyter`: Soporte para trabajar con cuadernos de Jupyter.
   - **settings**: Configuración personalizada para trabajar con Python, como la ruta del intérprete, habilitación del linter `pylint`, y el formateo automático con `autopep8`.
5. **postCreateCommand**: Después de crear el contenedor, se ejecuta el comando `pip install -r requirements.txt` para instalar las dependencias del proyecto listadas en el archivo `requirements.txt`.
6. **forwardPorts**: Se expone el puerto 8000, útil si tu aplicación Python utiliza un servidor web (por ejemplo, Flask o Django).
7. **mounts**: Se monta el socket de Docker dentro del contenedor, permitiendo que el contenedor use Docker si es necesario.
8. **remoteUser**: Define al usuario "vscode" como el usuario predeterminado para ejecutar comandos y trabajar dentro del contenedor.

### Personalización adicional:
- Puedes modificar la imagen base para utilizar otra versión de Python o incluir librerías adicionales.
- También puedes cambiar las configuraciones de linters o agregar más herramientas según las necesidades del proyecto (por ejemplo, `black` o `flake8`).

Este archivo configura automáticamente un entorno Python con todas las herramientas necesarias, facilitando el desarrollo dentro de un entorno controlado y reproducible.

### Extensiones comunes en la barra lateral al usar Dev Containers:

Cuando se trabaja con **Dev Containers** en Visual Studio Code, algunas extensiones adicionales aparecen en la barra lateral para facilitar el desarrollo en entornos de contenedores. Estas extensiones ayudan a gestionar y trabajar dentro del contenedor de desarrollo. Aquí tienes las más comunes:

1. **Remote Explorer (Explorador Remoto)**:
   - Esta extensión es parte del conjunto de herramientas de desarrollo remoto de VS Code. Permite explorar los contenedores, servidores SSH o WSL. 
   - Desde esta vista, puedes ver y gestionar los contenedores activos, sus archivos, carpetas y también acceder a las terminales remotas del contenedor.
   - Cuando trabajas con *Dev Containers*, el "Remote Explorer" muestra información sobre el contenedor activo, como los puertos expuestos y las sesiones remotas.

2. **Docker**:
   - Si tienes la extensión de **Docker** instalada, se habilita una pestaña adicional en la barra lateral que te permite gestionar contenedores, imágenes, redes y volúmenes de Docker directamente desde el editor.
   - Al usar *Dev Containers*, la extensión Docker facilita la interacción directa con los contenedores, mostrando el estado de los mismos y permitiendo ejecutar comandos, ver logs o detener los contenedores.

3. **Source Control (Control de versiones)**:
   - Esta pestaña está disponible en cualquier *workspace*, pero cuando trabajas dentro de un *Dev Container*, el control de versiones se adapta al entorno dentro del contenedor. Por ejemplo, si tienes Git instalado en el contenedor, podrás realizar todas las operaciones de control de versiones desde esta pestaña.
   - Esto permite trabajar con Git de manera transparente, como si estuvieras en un entorno local, pero dentro del contenedor.

4. **Run and Debug (Ejecución y Depuración)**:
   - Permite ejecutar y depurar aplicaciones dentro del contenedor de desarrollo. Dependiendo de la configuración del contenedor, puedes utilizar esta pestaña para configurar puntos de interrupción, iniciar sesiones de depuración y ver registros.

5. **Extensions (Extensiones)**:
   - Esta pestaña muestra las extensiones instaladas tanto localmente como dentro del contenedor. Cuando trabajas con *Dev Containers*, algunas extensiones pueden estar habilitadas solo dentro del contenedor, mientras que otras permanecen disponibles localmente.
   - La extensión `Dev Containers` facilita la instalación de extensiones dentro del contenedor, donde pueden ser necesarias para herramientas o lenguajes específicos.

### Extensión principal para *Dev Containers*:

- **Dev Containers**: Esta es la extensión esencial para trabajar con entornos de contenedores. Facilita la configuración y uso de archivos `devcontainer.json`, los cuales definen el entorno de desarrollo (incluyendo las dependencias, configuración de puertos, y más).

En resumen, al trabajar con *Dev Containers*, verás principalmente extensiones como **Remote Explorer**, **Docker**, **Source Control**, y **Run and Debug** en la barra lateral, además de las herramientas que usas normalmente para el desarrollo. Estas extensiones te proporcionan control total sobre el contenedor, la depuración, la gestión de versiones y más.

En Ubuntu y Visual Studio Code, los datos de los Dev Containers generalmente se almacenan en las siguientes rutas:

Archivos de configuración del contenedor:
`/ruta/al/proyecto/.devcontainer/`

Imágenes de Docker:
`/var/lib/docker`

Volúmenes de Docker (si se usan volúmenes para persistir datos entre sesiones):
`/var/lib/docker/volumes`
