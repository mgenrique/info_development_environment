# Visual Studio Code

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

En el siguiente documento se puede encontrar información sobre como usar la paleta de comandos [VSC command pallete](~/Docs/vsc_command_pallete.md)

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
