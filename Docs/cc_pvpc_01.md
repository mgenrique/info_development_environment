# Ejemplo de Custom Component para Home Assistant para crear un sensor del PVPC obtenido de la API de ESIOS

Para crear un **custom component** en Home Assistant que obtenga el valor del **PVPC (Precio Voluntario para el Pequeño Consumidor)** a través de la **API de ESIOS**, puedes seguir estos pasos. Este componente generará un sensor que obtendrá el valor actual de la electricidad y lo mostrará en Home Assistant.

A continuación, te muestro los archivos esenciales que necesitas para un **custom component** llamado `pvpc_sensor`.

### 1. **Estructura del componente**
Primero, asegúrate de crear la estructura de carpetas correcta:

```
custom_components/
  pvpc_sensor/
    __init__.py
    manifest.json
    sensor.py
```

### 2. **`manifest.json`**

Este archivo define los metadatos de tu componente, como el nombre, las dependencias y las bibliotecas necesarias.

```json
{
  "domain": "pvpc_sensor",
  "name": "PVPC Sensor",
  "documentation": "https://github.com/tu_usuario/pvpc_sensor",
  "requirements": ["requests>=2.23.0"],
  "version": "1.0.0",
  "dependencies": [],
  "codeowners": ["@tu_usuario"]
}
```

- **requirements**: Especifica que necesitamos la biblioteca `requests` para hacer las peticiones a la API.
- **domain**: El dominio del componente es `pvpc_sensor`.
- **codeowners**: Tu nombre de usuario en GitHub u otro identificador.

### 3. **`__init__.py`**

Este archivo puede estar vacío para este ejemplo básico, pero es importante que esté presente para que Python lo trate como un módulo.

```python
# __init__.py (vacío en este caso)
```

### 4. **`sensor.py`**

Este es el archivo principal donde se implementa la lógica del sensor que se conectará a la API de ESIOS para obtener el valor actual del PVPC. Utilizaremos la biblioteca `requests` para hacer la solicitud HTTP.

```python
import logging
import requests
import json
import voluptuous as vol

from datetime import timedelta
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import TEMP_CELSIUS
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.util import Throttle

_LOGGER = logging.getLogger(__name__)

# Tiempo de actualización (cada 1 hora)
SCAN_INTERVAL = timedelta(hours=1)

# URL de la API de ESIOS para obtener el PVPC
API_URL = "https://api.esios.ree.es/indicators/1001"

# Definir la plataforma
def setup_platform(hass, config, add_entities, discovery_info=None):
    """Configurar el sensor de PVPC."""
    add_entities([PVPCElectricitySensor()])

class PVPCElectricitySensor(Entity):
    """Implementación del sensor de PVPC."""

    def __init__(self):
        """Inicializar el sensor."""
        self._state = None
        self.update()

    @property
    def name(self):
        """Nombre del sensor."""
        return "PVPC Electricity Price"

    @property
    def state(self):
        """Retornar el estado actual del sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Unidad de medida del sensor."""
        return "€/kWh"

    @Throttle(SCAN_INTERVAL)
    def update(self):
        """Actualizar el valor del sensor con datos de la API de ESIOS."""
        _LOGGER.debug("Actualizando el valor de PVPC desde ESIOS API")
        try:
            # Hacer la solicitud a la API de ESIOS
            response = requests.get(
                API_URL,
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "Authorization": "Token token=<tu_token_esios>"
                }
            )
            if response.status_code == 200:
                data = response.json()
                # Obtener el precio del PVPC
                pvpc_value = data["indicator"]["values"][0]["value"]
                self._state = pvpc_value
            else:
                _LOGGER.error(f"Error en la API de ESIOS: {response.status_code}")
        except Exception as e:
            _LOGGER.error(f"Error al actualizar el PVPC: {e}")
```

### Explicación del código:

1. **Constantes**:
   - `API_URL`: Es la URL de la API de ESIOS que ofrece los precios del PVPC.
   - `SCAN_INTERVAL`: Define el intervalo de actualización del sensor. En este caso, está configurado para actualizar cada 1 hora.
   
2. **Clase `PVPCElectricitySensor`**:
   - **`__init__`**: Inicializa el sensor y llama a `update` para obtener el valor actual del PVPC.
   - **`name`**: Define el nombre del sensor que aparecerá en Home Assistant, en este caso "PVPC Electricity Price".
   - **`state`**: Devuelve el valor actual del PVPC.
   - **`unit_of_measurement`**: Define la unidad de medida que usa el sensor, que en este caso es `€/kWh`.
   - **`update`**: Se encarga de hacer una solicitud a la API de ESIOS y obtener el precio actual del PVPC. Si la solicitud es exitosa, actualiza el estado del sensor con el valor obtenido. 

3. **Autorización**: La API de ESIOS requiere un **token de autorización**, que debes incluir en los encabezados de la solicitud. Debes obtener este token registrándote en la plataforma de **ESIOS**.

### 5. **Configuración en `configuration.yaml`**

Para que tu custom component funcione, debes añadir una entrada en el archivo `configuration.yaml` de Home Assistant:

```yaml
sensor:
  - platform: pvpc_sensor
```

Este código indica que Home Assistant debe cargar el componente `pvpc_sensor` como un sensor.

### 6. **Obtener el Token de ESIOS**

Para que el sensor funcione correctamente, necesitas un **token** de la API de **ESIOS**. Puedes obtener uno registrándote en su sitio web: https://www.esios.ree.es/en.

### Resumen

Este **custom component** para Home Assistant utiliza la API de ESIOS para obtener el precio actual de la electricidad (PVPC) en €/kWh. El componente está estructurado de forma simple y actualiza el valor cada hora. Este sensor se puede personalizar según tus necesidades, y la API de ESIOS ofrece más datos que podrías incorporar a tu componente, como precios históricos o detalles sobre otros indicadores energéticos.
