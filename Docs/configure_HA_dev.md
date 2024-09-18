Una vez tenemos el entorno preparado con Docker y Visual Studio Code, comenzamos a utilizarlo para disponer de una versión del core de Home Assistant sobre el que poder desarrollar nuevas funcionalidades y hacer pruebas

Para ello seguiremos los pasos que se indican en:
https://developers.home-assistant.io/docs/development_environment/

En el punto en el que nos encontramos deberiamos comenzar directamente haciendo un Fork del repositorio de HA en nuestro Github
https://github.com/home-assistant/core

Una vez hecho seguir las instrucciones.
Antes de darle al botón es necesario que Docker Desktop ya este corriendo. Buscar la aplicación en el cajón de aplicaciones de Ubuntu y lanzarla.

Al darle al botón se abrirá Visual Code, clonará localmente nuestro frok de HA e instalará Dev Containers. El proceso completo puede llegar a tardar 1 hora.

Es posible que el navegador no este bien configurado para ejecutar el comando que se ejecuta al presionar el botón. Si no funciona a la primera desde Firefox seguir los pasos indicados más abajo.
Cuando el proceso termine deberiamos tener algo similar esto en Docker Desktop:
![DockerDesktopHA](../images/DockerDesktopHA.png)

## Solo si no abre Visual Studio al presionar el botón
Para permitir enlaces personalizados en Firefox como vscode://, sigue estos pasos:
Abre una nueva pestaña en Firefox y escribe about:config en la barra de direcciones, luego presiona Enter.
Verás una advertencia que dice "Tendré cuidado, lo prometo". Haz clic en el botón para continuar.
Busca el siguiente parámetro en la barra de búsqueda superior:
````bash
network.protocol-handler.expose.vscode
````
Si el parámetro no existe, créalo haciendo clic con el botón derecho en cualquier parte de la lista de configuraciones, selecciona Nuevo > Booleano.
Nombra la clave como network.protocol-handler.expose.vscode y establece el valor en false.
A continuación, vuelve a hacer clic derecho y selecciona Nuevo > Booleano. Esta vez, crea el parámetro network.protocol-handler.external.vscode y configúralo en true.
Cierra la pestaña de about:config.
La próxima vez que intentes abrir un enlace vscode://, Firefox te debería preguntar si deseas abrir Visual Studio Code.

Como alternatica tambien se puede abrir el enlace manualmente en Visual Studio Code
Si Firefox no te permite abrir el enlace directamente, puedes clonar el repositorio de GitHub manualmente y abrirlo en Visual Studio Code. Sigue estos pasos:
Clonar el repositorio usando git o la opción de "clonar en contenedor" de Visual Studio Code:
En tu terminal, ejecuta el siguiente comando:
````bash
git clone https://github.com/mgenrique/ha_core_emg_fork
````
Una vez clonado, abre Visual Studio Code y selecciona Remote-Containers (si tienes la extensión instalada). Luego sigue estos pasos:

Abre Visual Studio Code.
Ve a la paleta de comandos con Ctrl + Shift + P.
Escribe Remote-Containers: Open Folder in Container.
Navega al directorio donde clonaste el repositorio y ábrelo.