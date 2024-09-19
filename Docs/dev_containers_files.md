# Archivos de proyecto de DEV CONTAINERS

Los **Dev Containers** de **Visual Studio Code** permiten trabajar en un entorno de desarrollo basado en contenedores Docker, y parte de este enfoque implica cómo se manejan los archivos del proyecto y los datos dentro de esos contenedores.

### 1. ¿Cómo ubica **Dev Containers** los archivos en el disco?

Cuando usas **Dev Containers**, los archivos de tu proyecto se exponen dentro del contenedor Docker, pero el código y otros archivos no están realmente almacenados dentro del contenedor de forma persistente. En cambio, se montan desde tu sistema de archivos local en el contenedor. Esto significa que:

- **El código del proyecto**: Los archivos de tu proyecto que están en tu máquina local se "montan" dentro del contenedor a través de un **volumen de Docker**. Los cambios que hagas en estos archivos desde el contenedor se reflejan directamente en tu sistema local y viceversa.
- **Ubicación del código**: Por defecto, los archivos de tu proyecto local se encuentran en el directorio que hayas configurado en tu entorno de desarrollo. Por ejemplo, si tu proyecto está en `~/my-project` en tu máquina local, esa carpeta será la que se monte en el contenedor para que el entorno del contenedor pueda acceder a los archivos.

El archivo **`devcontainer.json`** (que define el entorno del contenedor) usualmente especifica qué carpetas se deben montar en el contenedor y cómo deben configurarse los volúmenes.

#### Ejemplo de `devcontainer.json`:

```json
{
  "name": "My Dev Container",
  "image": "python:3.9",
  "workspaceMount": "source=${localWorkspaceFolder},target=/workspace,type=bind",
  "workspaceFolder": "/workspace",
  "extensions": ["ms-python.python"]
}
```

En este ejemplo:
- **`workspaceMount`** especifica que el directorio local donde está tu proyecto (`${localWorkspaceFolder}`) se monta dentro del contenedor en el directorio `/workspace`.
- **`workspaceFolder`** indica que el directorio de trabajo dentro del contenedor será `/workspace`, que es donde se montó tu proyecto.

### 2. ¿Un contenedor almacena datos de la sesión?

Los contenedores Docker, por diseño, son **efímeros**. Esto significa que cualquier dato que se almacena **dentro del contenedor** (sin montarlo en volúmenes persistentes) se perderá cuando el contenedor sea detenido o eliminado. Sin embargo, existen dos formas principales de manejar datos persistentes:

#### a) **Datos almacenados fuera del contenedor: Volúmenes**

Si necesitas que los datos persistan más allá de la vida del contenedor, puedes usar **volúmenes** de Docker o montajes de directorios. En un **Dev Container**, al igual que en cualquier contenedor Docker, puedes definir volúmenes que almacenan los datos fuera del contenedor en tu disco local, de modo que sean persistentes entre sesiones.

Por ejemplo, si Home Assistant o cualquier otra aplicación dentro de un contenedor necesita almacenar datos, puedes montar una carpeta local o un volumen Docker en el contenedor, asegurando que los datos persistan.

#### Ejemplo de volumen en Docker Compose:

```yaml
version: '3'
services:
  homeassistant:
    container_name: home-assistant
    image: homeassistant/home-assistant:stable
    volumes:
      - ./config:/config  # Monta la carpeta local ./config dentro del contenedor
```

En este ejemplo:
- La carpeta `./config` en tu máquina local se monta en el contenedor bajo `/config`. Los archivos almacenados en `/config` persistirán incluso si el contenedor se detiene o es eliminado.

#### b) **Datos efímeros dentro del contenedor**

Si no usas volúmenes o montajes de directorios, cualquier dato que se genere o modifique **dentro del contenedor** solo existirá mientras el contenedor esté en ejecución. Si el contenedor se elimina, también lo harán los datos.

### Resumen:

- Los **Dev Containers** montan los archivos del proyecto desde el sistema local al contenedor utilizando volúmenes de Docker. Esto significa que puedes modificar archivos dentro del contenedor y los cambios se reflejarán en tu sistema local.
- Los contenedores, por naturaleza, son efímeros, lo que significa que los datos que no están almacenados en volúmenes o montajes externos se perderán cuando el contenedor se detenga o elimine.
- Para **persistir datos** entre sesiones, puedes usar volúmenes de Docker o montajes de carpetas locales, asegurando que los archivos importantes no se pierdan cuando el contenedor termine su ciclo de vida.
