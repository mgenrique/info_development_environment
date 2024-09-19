# Paleta de comandos de Visual Studio Code
En **Visual Studio Code**, al presionar `Ctrl + Shift + P` (o `Ctrl + Mayús + P`), se abre la **paleta de comandos**. Esta es una herramienta extremadamente útil que te permite acceder rápidamente a una amplia gama de funciones y comandos en Visual Studio Code.

### ¿Qué puedes hacer con la paleta de comandos?

- **Buscar y ejecutar comandos**: Puedes escribir el nombre de cualquier comando disponible en Visual Studio Code, y se te presentará una lista de sugerencias a medida que escribes. Por ejemplo, puedes buscar:
  - **"Git"** para ver todos los comandos relacionados con Git.
  - **"Terminal: New Terminal"** para abrir un nuevo terminal.
  - **"Go to File"** para abrir rápidamente un archivo.
  
- **Cambiar configuraciones**: Accede rápidamente a configuraciones globales o específicas del espacio de trabajo.

- **Instalar y administrar extensiones**: Puedes buscar, instalar y administrar extensiones sin tener que navegar por la tienda de extensiones manualmente.

- **Buscar y abrir archivos**: La paleta de comandos te permite acceder a archivos específicos en tu proyecto sin navegar por el explorador de archivos.

- **Abrir configuraciones avanzadas**: Puedes acceder a configuraciones avanzadas y otros comandos relacionados con la configuración de tu entorno de desarrollo.

### Atajo adicional: `F1`

El atajo `F1` también abre la paleta de comandos, funcionando de manera idéntica a `Ctrl + Shift + P`.

### Ejemplos de uso:

- **Cambiar tema de color**: `Ctrl + Shift + P`, escribe "Color Theme" y selecciona un tema.
- **Buscar y ejecutar comandos Git**: `Ctrl + Shift + P`, escribe "Git" para ver comandos como "Git: Commit", "Git: Push", etc.
- **Abrir archivo**: `Ctrl + Shift + P`, escribe el nombre del archivo que deseas abrir.

En resumen, la paleta de comandos es una herramienta clave para navegar y usar Visual Studio Code de manera eficiente, ya que permite acceder rápidamente a cualquier funcionalidad disponible sin tener que buscarla en los menús.

## Personalización de la paleta de comandos de Visual Studio Code
Para agregar comandos específicos a la Paleta de Comandos en un workspace de Visual Studio Code (VS Code), puedes hacerlo a través de las siguientes opciones:

1. Usar tareas personalizadas en tasks.json
Puedes crear tareas personalizadas que luego aparecerán en la Paleta de Comandos bajo el comando "Run Task". Para hacer esto:

Abre la configuración de tu workspace en VS Code.
Ve a `Terminal` > `Configure Tasks` > `Create tasks.json file from template`.
En el archivo `tasks.json` que se genera, agrega tus comandos personalizados. Un ejemplo básico podría ser:

````json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Mi Comando Personalizado",
      "type": "shell",
      "command": "echo Hola Mundo",
      "group": {
        "kind": "build",
        "isDefault": true
      },
      "presentation": {
        "reveal": "always"
      },
      "problemMatcher": []
    }
  ]
}
````
2. Extensiones para agregar comandos personalizados
Si necesitas un mayor control, puedes crear una extensión para Visual Studio Code. Este método requiere que sepas desarrollar extensiones, pero te permitirá agregar comandos personalizados directamente en la Paleta de Comandos.

Crea un proyecto de extensión utilizando la línea de comandos:

````bash
yo code
````
Define los comandos en el archivo `package.json` de la extensión. Aquí un ejemplo:

````json
{
  "contributes": {
    "commands": [
      {
        "command": "extension.miComandoPersonalizado",
        "title": "Mi Comando Personalizado"
      }
    ]
  }
}
````

3. En el archivo `src/extension.ts` (o e`xtension.js`), define la lógica de tu comando:
````typescript
import * as vscode from 'vscode';

export
````

