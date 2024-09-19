# Visual Studio Code

Visual Studio Code (VS Code) es un editor de código fuente ligero pero poderoso, ampliamente utilizado por desarrolladores debido a su versatilidad y soporte para una amplia gama de lenguajes de programación. A continuación, se describe brevemente cómo gestionar *workspaces*, usar los terminales integrados y los elementos comunes de la barra lateral.

### Workspaces
Un *workspace* en VS Code representa un entorno de trabajo que puede contener múltiples carpetas y configuraciones específicas. Los *workspaces* facilitan la organización de proyectos, ya que puedes agrupar varios directorios bajo un mismo espacio de trabajo y guardar configuraciones particulares, como ajustes de extensiones, reglas de linter y configuraciones de depuración.

- **Crear un workspace**: Puedes abrir una carpeta desde el menú "File" > "Open Folder", lo que creará un *workspace* básico con una única carpeta. Si deseas agregar más carpetas, puedes hacerlo a través de "File" > "Add Folder to Workspace".
- **Workspace settings**: VS Code permite personalizar configuraciones específicas para un *workspace* mediante el archivo `settings.json`. Esto es útil para mantener diferentes configuraciones de extensiones o reglas para proyectos distintos.

### Terminal Integrado
VS Code incluye un terminal integrado que te permite ejecutar comandos de shell o de consola directamente desde el editor sin tener que cambiar a otra ventana. Soporta múltiples terminales y puede configurarse para diferentes tipos de terminal (bash, PowerShell, cmd, entre otros).

- **Abrir el terminal**: Se puede acceder al terminal integrado a través de `Ctrl+`` o desde el menú "Terminal" > "New Terminal".
- **Terminales múltiples**: Puedes tener varios terminales abiertos a la vez, lo que es útil para ejecutar diferentes comandos simultáneamente. Cada terminal se puede personalizar en términos de su shell predeterminado.
- **Uso del terminal**: Es ideal para ejecutar scripts, probar código rápidamente, manejar herramientas de línea de comandos como Git, y más, sin salir del entorno de desarrollo.

### Barra Lateral
La barra lateral de VS Code proporciona un conjunto de herramientas esenciales que facilitan la navegación y la gestión de proyectos.

1. **Explorer (Explorador)**: Muestra la estructura de archivos y carpetas del *workspace*. Permite abrir, cerrar, y gestionar archivos rápidamente. También puedes arrastrar y soltar archivos para reordenar.
2. **Search (Búsqueda)**: Permite buscar en todo el proyecto o en archivos específicos utilizando patrones de búsqueda. Ofrece funciones avanzadas, como buscar y reemplazar en múltiples archivos.
3. **Source Control (Control de versiones)**: Se integra con Git y otros sistemas de control de versiones. Permite hacer commits, gestionar ramas, y manejar conflictos de fusión directamente desde el editor.
4. **Run and Debug (Ejecución y Depuración)**: Proporciona herramientas para ejecutar y depurar aplicaciones. Es compatible con múltiples lenguajes y entornos, lo que permite la depuración directa del código desde el editor.
5. **Extensions (Extensiones)**: VS Code cuenta con un extenso ecosistema de extensiones para lenguajes, temas y herramientas adicionales. La barra lateral facilita la instalación, configuración y gestión de extensiones.

En resumen, Visual Studio Code ofrece un entorno de desarrollo flexible y potente, donde los *workspaces* permiten una gestión avanzada de proyectos, el terminal integrado facilita el trabajo con comandos de consola, y la barra lateral proporciona acceso rápido a herramientas clave para mejorar la productividad.

Los espacios de trabajo (workspaces) en Visual Studio Code permiten configurar distintos entornos de desarrollo. Siempre existirá al menos uno (el último que se utilizó) y su configuración se puede guardar en disco (archivos como settings.json y otros que definen la configuración, y que normalmente se colocan en una subcarpeta del proyecto llamada `.vscode/`), lo que permita cambiar entre entornos de trabajo diferentes. Por ejemplo programar para Arduino en Platformio nos dará un workspace con herramientas muy diferentes a las necesarias para programar contenedores con Dev Containers orientados al desarrollo para Home Assistant.

Dentro de VS Code, se hará uso de la extensión Dev Containers, que permitirá el desarrollo de aplicaciones que corran en contenedores de Docker.

En Ubuntu y Visual Studio Code, existen varias carpetas donde se almacenan elementos necesarios para VSC. 

Las configuraciones específicas de cada workspace suelen estar guardadas en la carpeta del proyecto, generalmente en archivos dentro de `.vscode/`.

`/ruta/al/proyecto/.vscode/`

Las extensiones que se instalan en VSC se almacenan en:

`~/.vscode/extensions/`

Los datos de usuario de Visual Studio Code (como configuraciones generales, historial de comandos, etc. y la cache de generación de los proyectos) están almacenados en:

`~/.config/Code/`

La cache de generación de los proyectos puede ocupar bastante espacio por lo que si se elimna un proyecto guardado en una carpeta de usuario, aun pueden quedar datos innecesarios en
`~/.config/Code/Cache/`

Si se quieren eliminar extensiones, configuraciones y caché para liberar espacio:

````bash
rm -rf ~/.vscode/extensions/
rm -rf ~/.config/Code/
````

## Instalación recomendada de Visual Studio Code
````bash
sudo apt update
sudo apt install software-properties-common apt-transport-https wget
````
````bash
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/
````
````bash
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
````
````bash
sudo apt update
sudo apt install code
````

## Utilización

En el siguiente documento se puede encontrar información sobre como usar la paleta de comandos [VSC command pallete](./vsc_command_pallete.md)

## Desinstalación de Visual Studio Code
Para desinstalar completamente Visual Studio Code y Docker que permita liberar espacio en disco cuando ya no sea necesario el entorno de desarrollo:
````bash
sudo apt remove code --purge
````
````bash
sudo apt autoremove
````
````bash
rm -rf ~/.vscode/
````
````bash
rm -rf ~/.config/Code/
````

En cuanto a Docker y Dev Containers se puede liberar espacio haciendo:
````bash
docker system prune
````
