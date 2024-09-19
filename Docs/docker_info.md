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

Aquí, el contenedor ejecuta la aplicación web y expone el puerto 5000, lo que te permite acceder a la aplicación desde tu navegador en `http://localhost:5000`.

En resumen, Docker es una herramienta poderosa que facilita la creación, despliegue y gestión de aplicaciones en entornos aislados y portátiles llamados contenedores. Los conceptos clave como imágenes, contenedores, volúmenes y puertos son fundamentales para entender cómo Docker facilita el desarrollo y despliegue de aplicaciones.
