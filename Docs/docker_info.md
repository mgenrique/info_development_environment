# DOCKER

**Docker** es una plataforma de código abierto que permite crear, desplegar y gestionar aplicaciones dentro de contenedores. Los contenedores son entornos ligeros y portátiles que encapsulan una aplicación y todas sus dependencias, asegurando que esta pueda ejecutarse de manera consistente en cualquier entorno, ya sea en el equipo local, en servidores, o en la nube.

### Conceptos clave de Docker

1. **Contenedores**:
   - Los contenedores son instancias ejecutables de imágenes Docker que encapsulan una aplicación y todas sus dependencias, como bibliotecas, archivos de configuración, etc.
   - Son similares a las máquinas virtuales, pero más ligeros y rápidos, ya que comparten el mismo sistema operativo subyacente y utilizan menos recursos.

   Ejemplo: Si tienes una aplicación Python, puedes ejecutarla dentro de un contenedor que tenga todo lo necesario para funcionar (Python, las bibliotecas, etc.), sin necesidad de instalar nada en el sistema operativo anfitrión.

2. **Imágenes**:
   - Una imagen es una plantilla de solo lectura que contiene el sistema operativo, las dependencias y la aplicación que deseas ejecutar. Las imágenes son el punto de partida para crear contenedores.
   - Cada imagen está compuesta por capas, lo que permite la reutilización y optimización. Por ejemplo, si tienes varias imágenes basadas en Ubuntu, todas ellas comparten la capa base de Ubuntu.

   Ejemplo: Una imagen puede estar basada en `python:3.9` e incluir las dependencias necesarias para tu aplicación.

3. **Volúmenes**:
   - Los volúmenes son mecanismos de almacenamiento persistente en Docker. Almacenan datos fuera del ciclo de vida de los contenedores, lo que permite que los datos persistan incluso si el contenedor es eliminado o recreado.
   - Son útiles para gestionar bases de datos, archivos generados por la aplicación o datos compartidos entre varios contenedores.

   Ejemplo: Si un contenedor MySQL almacena los datos en un volumen, los datos permanecerán disponibles incluso si detienes o eliminas el contenedor.

4. **Puertos**:
   - Los puertos en Docker permiten que los servicios dentro de un contenedor sean accesibles desde fuera del mismo. Cada contenedor tiene su propia red aislada, y puedes exponer un puerto del contenedor y mapearlo a un puerto del sistema anfitrión.
   - Esto es esencial para que las aplicaciones web, bases de datos u otros servicios puedan ser accesibles desde tu navegador u otras aplicaciones.

   Ejemplo: Si tienes una aplicación web que corre en el puerto 5000 dentro del contenedor, puedes mapear ese puerto al puerto 8080 en tu máquina anfitriona, haciendo que la aplicación sea accesible en `localhost:8080`.

5. **Dockerfile**:
   - Un **Dockerfile** es un archivo de texto que contiene una serie de instrucciones para crear una imagen Docker. Define qué sistema operativo se debe usar, qué dependencias se deben instalar, y cómo debe configurarse la aplicación dentro del contenedor.

   Ejemplo de un Dockerfile para una aplicación Node.js:
   ```dockerfile
   FROM node:14
   WORKDIR /app
   COPY package.json ./
   RUN npm install
   COPY . .
   CMD ["node", "app.js"]
   ```
Un ejemplo de un Dockerfile para una aplicación Python puede verse en [Dockerfile Python](./dokerfile_python.md)

6. **Redes**:
   - Docker crea automáticamente una red para que los contenedores se comuniquen entre sí. También puedes crear redes personalizadas para aislar o conectar contenedores de manera controlada.
   - Existen diferentes modos de red, como `bridge`, `host`, y `none`, dependiendo del nivel de aislamiento o visibilidad que necesites entre los contenedores y el sistema anfitrión.

### Flujo básico de trabajo en Docker

1. **Construcción de la imagen**:
   - A partir de un `Dockerfile`, ejecutas el comando `docker build` para crear una imagen que contenga tu aplicación y todas sus dependencias.

2. **Ejecución de un contenedor**:
   - Con el comando `docker run`, inicias un contenedor basado en una imagen. Puedes especificar opciones como puertos a exponer, volúmenes a montar, y más.
   
3. **Gestión de datos persistentes**:
   - Para que los datos generados por el contenedor persistan, puedes usar volúmenes (`docker volume`), lo cual te permite guardar datos fuera del ciclo de vida del contenedor.

4. **Conexión entre servicios**:
   - Puedes ejecutar múltiples contenedores que se comuniquen entre sí (por ejemplo, una aplicación web y una base de datos) usando redes Docker.

### Ejemplo sencillo

Si tienes una aplicación web en Python con Flask, podrías crear una imagen Docker usando un `Dockerfile`, y luego ejecutar el contenedor con:

```bash
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```

### Relación entre Docker y Docker Desktop

**Docker** es la plataforma base que proporciona las herramientas y tecnologías para crear, ejecutar, y gestionar contenedores. Incluye los componentes centrales, como el motor de Docker (Docker Engine), que permite construir y ejecutar contenedores.

**Docker Desktop**, por otro lado, es una aplicación que facilita el uso de Docker en sistemas operativos como macOS y Windows. Docker Desktop incluye:
- **Docker Engine**: El núcleo de Docker para ejecutar contenedores.
- **Docker CLI**: La interfaz de línea de comandos para interactuar con Docker.
- **Docker Compose**: Herramienta para definir y ejecutar aplicaciones multi-contenedor.
- **Kubernetes**: Un entorno opcional de orquestación de contenedores.

Docker Desktop simplifica el proceso de instalar y gestionar Docker en sistemas que no tienen soporte nativo de contenedores (como macOS y Windows), y proporciona una interfaz gráfica para manejar contenedores, imágenes, volúmenes, redes, etc.

### Integración de Docker con Visual Studio Code (VSC)

Visual Studio Code se puede integrar perfectamente con Docker mediante la extensión **Docker**. Esta extensión te permite interactuar con Docker directamente desde el editor, lo que facilita la administración de imágenes, contenedores, y otros recursos sin salir de VSC.

#### Pasos para integrar Docker en Visual Studio Code:

1. **Instalar Docker en tu máquina**:
   - En Windows o macOS, necesitarás instalar **Docker Desktop**. En Linux, puedes instalar Docker directamente usando los paquetes de tu distribución.
   - Una vez instalado, asegúrate de que Docker esté corriendo correctamente ejecutando en la terminal:
     ```bash
     docker --version
     ```

2. **Instalar la extensión de Docker en VS Code**:
   - Abre Visual Studio Code y ve a la pestaña de extensiones (icono de los cuatro cuadrados).
   - Busca "Docker" y selecciona la extensión oficial de Docker desarrollada por Microsoft.
   - Instala la extensión.

3. **Interacción con Docker en VS Code**:
   Una vez instalada la extensión de Docker, verás un nuevo icono de Docker en la barra lateral de VS Code. Desde ahí puedes:
   - **Gestionar contenedores**: Ver, iniciar, detener, o eliminar contenedores.
   - **Gestionar imágenes**: Listar, construir, ejecutar o eliminar imágenes.
   - **Gestionar volúmenes**: Crear o eliminar volúmenes para almacenamiento persistente.
   - **Docker Compose**: Definir y ejecutar aplicaciones multi-contenedor desde archivos `docker-compose.yml`.

4. **Crear y ejecutar contenedores desde VS Code**:
   Puedes ejecutar y administrar contenedores directamente desde el editor. También puedes interactuar con contenedores desde la terminal integrada, ver registros de contenedores, o acceder a un contenedor en ejecución para ejecutar comandos dentro de él.

5. **Soporte para Dev Containers**:
   Si trabajas con **Dev Containers** (contenedores de desarrollo), puedes abrir un proyecto completo dentro de un contenedor de Docker desde VS Code. Esto te permite trabajar en un entorno de desarrollo completamente aislado, sin necesidad de configurar dependencias en tu máquina local.

   Pasos para usar Dev Containers:
   - Crea un archivo `devcontainer.json` en tu proyecto (como en ejemplos anteriores).
   - VS Code detectará el archivo y te preguntará si deseas "Reabrir en contenedor". Al hacer esto, tu proyecto se ejecutará en un contenedor Docker con todas las dependencias necesarias.

#### Beneficios de usar Docker con VS Code

- **Simplificación del flujo de trabajo**: Puedes manejar contenedores, imágenes y recursos Docker sin salir del editor, todo integrado en un solo entorno.
- **Entornos consistentes**: Usando Dev Containers, puedes garantizar que todos los desarrolladores en un proyecto tengan el mismo entorno de desarrollo.
- **Facilidad de gestión de contenedores**: La interfaz gráfica de la extensión Docker en VS Code hace que sea sencillo ver qué contenedores están en ejecución, acceder a los registros, y administrar otros aspectos del ecosistema Docker.

### Resumen

- **Docker** es la plataforma base para la creación y gestión de contenedores.
- **Docker Desktop** es una aplicación que facilita la instalación y el uso de Docker en macOS y Windows, proporcionando una interfaz gráfica y un conjunto completo de herramientas (Docker Engine, CLI, Compose, y Kubernetes).
- **Visual Studio Code** se integra con Docker a través de la extensión Docker, lo que permite gestionar contenedores, imágenes y otros recursos directamente desde el editor.
- Usar Docker con **Dev Containers** en VS Code facilita el trabajo en entornos de desarrollo consistentes y portátiles.

Esta integración es ideal para desarrolladores que desean aprovechar la potencia de Docker mientras utilizan Visual Studio Code como su entorno de desarrollo principal.

Aquí, el contenedor ejecuta la aplicación web y expone el puerto 5000, lo que te permite acceder a la aplicación desde tu navegador en `http://localhost:5000`.

En resumen, Docker es una herramienta poderosa que facilita la creación, despliegue y gestión de aplicaciones en entornos aislados y portátiles llamados contenedores. Los conceptos clave como imágenes, contenedores, volúmenes y puertos son fundamentales para entender cómo Docker facilita el desarrollo y despliegue de aplicaciones.
