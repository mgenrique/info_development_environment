# Visual Studio Code

Los espacios de trabajo (workspaces) en Visual Studio Code permiten configurar distintos entornos de desarrollo. Siempre existirá al menos uno (el último que se utilizó) y su configuración se puede guardar en disco (archivos como settings.json y otros que definen la configuración, y que normalmente se colocan en una subcarpeta del proyecto llamada `.vscode/`), lo que permita cambiar entre entornos de trabajo diferentes. Por ejemplo programar para Arduino en Platformio nos dará un workspace con herramientas muy diferentes a las necesarias para programar contenedores con Dev Containers orientados al desarrollo para Home Assistant.

Dentro de VS Code, se hará uso de la extensión Dev Containers, que permitirá el desarrollo de aplicaciones que corran en contenedores de Docker.

En Ubuntu y Visual Studio Code, los datos de los Dev Containers generalmente se almacenan en las siguientes rutas:
Archivos de configuración del contenedor:
`/ruta/al/proyecto/.devcontainer/`

Imágenes de Docker:
`/var/lib/docker`

Volúmenes de Docker (si se usan volúmenes para persistir datos entre sesiones):
`/var/lib/docker/volumes`

Extensiones instaladas en Visual Studio Code
`~/.vscode/extensions/`

Instalación recomendada de Visual Studio Code
````bash
sudo apt update
sudo apt install software-properties-common apt-transport-https wget
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update
sudo apt install code
````


#Las configuraciones específicas de cada workspace suelen estar guardadas en la carpeta del proyecto, generalmente en archivos como .vscode/.
`/ruta/al/proyecto/.vscode/`

Los datos de usuario de Visual Studio Code (como configuraciones generales, historial de comandos, etc. y la cache de generación de los proyectos) están almacenados en:
`~/.config/Code/`

La cache de generación de los proyectos puede ocupar bastante espacio por lo que si se elimna un proyecto guardado en una carpeta de usuario, aun pueden quedar datos innecesarios en ~/.config/Code/Cache/

Si se quieren eliminar extensiones, configuraciones y caché para liberar espacio:
````bash
rm -rf ~/.vscode/extensions/
rm -rf ~/.config/Code/
````

Para desinstalar completamente Visual Studio Code y Docker que permita liberar espacio en disco cuando ya no sea necesario el entorno de desarrollo:
````bash
sudo apt remove code --purge 
sudo apt autoremove
rm -rf ~/.vscode/
rm -rf ~/.config/Code/
````

En cuanto a Docker y Dev Containers se puede liberar espacio haciendo:
````bash
docker system prune
````
