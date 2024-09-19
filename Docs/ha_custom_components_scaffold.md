# SCAFFOLD. Script de ayuda a la creación de Custom Components en HA
El **script.scaffold** es una herramienta que ofrece **Home Assistant** para ayudar a los desarrolladores a crear rápidamente la estructura básica de un componente personalizado. Es un generador automático que configura la base del código que necesitas para comenzar a desarrollar tu **custom component** sin tener que escribir toda la estructura desde cero.

### ¿Qué hace el script `scaffold`?

El script **scaffold** genera la estructura y los archivos necesarios para un componente, incluyendo:

1. **Archivos Python** como `__init__.py` y archivos específicos de la plataforma (como `sensor.py` o `switch.py`).
2. **Archivo `manifest.json`**, que contiene metadatos sobre el componente.
3. **Archivos de prueba (opcional)** si decides que tu componente tenga pruebas unitarias.

### Pasos para usar `script.scaffold`

1. **Clonar el repositorio de Home Assistant**:

   Para usar el script `scaffold`, primero debes clonar el repositorio principal de Home Assistant:

   ```bash
   git clone https://github.com/home-assistant/core.git
   cd core
   ```

2. **Ejecutar el script**:

   Una vez dentro del directorio del repositorio, puedes ejecutar el script `scaffold` con los siguientes parámetros. El script te pedirá información sobre el nombre del componente, la plataforma y otros detalles.

   ```bash
   python3 script/scaffold COMPONENT_NAME
   ```

   Ejemplo: Si quieres crear un componente llamado `my_component`, puedes ejecutar:

   ```bash
   python3 script/scaffold my_component
   ```

3. **Seleccionar la plataforma**:

   Durante el proceso, el script te preguntará qué tipo de plataforma estás desarrollando (por ejemplo, `sensor`, `switch`, `light`, etc.), y luego generará los archivos correspondientes.

4. **Estructura generada**:

   Después de ejecutar el script, verás que se ha generado una estructura básica de directorios y archivos para tu componente, similar a esto:

   ```
   custom_components/
     my_component/
       __init__.py
       manifest.json
       sensor.py  # si elegiste desarrollar un sensor
       tests/  # si optaste por incluir pruebas
   ```

### Archivos generados

- **`__init__.py`**: Define la inicialización del componente, asegurando que se registre correctamente en Home Assistant.
- **`manifest.json`**: Contiene información clave sobre el componente, como el nombre, la versión, las dependencias y la información del propietario.
- **Archivos de plataforma (`sensor.py`, `switch.py`, etc.)**: Estos archivos contendrán las clases y métodos necesarios para implementar la funcionalidad del componente.
- **Pruebas** (opcional): Se crean carpetas y archivos básicos para implementar pruebas unitarias usando `pytest`.

### Ventajas de usar `script.scaffold`

- **Ahorra tiempo**: Te evita tener que escribir manualmente la estructura básica y seguir la convención de Home Assistant desde cero.
- **Estandarización**: Genera archivos siguiendo las convenciones oficiales de Home Assistant, asegurando que tu componente esté bien estructurado.
- **Fácil extensión**: Una vez generada la estructura base, puedes concentrarte en añadir las funcionalidades específicas del componente.

### Resumen

El **script.scaffold** de Home Assistant es una herramienta útil para crear rápidamente la estructura inicial de un **custom component**. Ahorra tiempo al automatizar la creación de archivos clave y ayuda a los desarrolladores a seguir las convenciones del proyecto. Después de usar el script, puedes concentrarte en implementar la lógica de tu componente y agregar cualquier funcionalidad adicional.
