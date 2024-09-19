# Ejemplo de Custom Component para Home Assistant para crear un sensor del PVPC obtenido de la API de ESIOS con flujo de configuración en Lovelace

Para crear un **custom component** en Home Assistant que obtenga el valor del PVPC desde la **API de ESIOS** y permita configurar el **token** desde la UI mediante un flujo de configuración, debes implementar una integración basada en **config flows**. Esto permite a los usuarios añadir y configurar el componente desde la interfaz de Home Assistant.

A continuación, te muestro cómo puedes modificar el componente para agregar esta funcionalidad.

### Estructura del componente

La estructura de carpetas será la siguiente:

```
custom_components/
  pvpc_sensor/
    __init__.py
    manifest.json
    sensor.py
    config_flow.py
    const.py
```

### 1. **`manifest.json`**

Debemos agregar algunas propiedades adicionales para soportar el flujo de configuración.

```json
{
  "domain": "pvpc_sensor",
  "name": "PVPC Sensor",
  "documentation": "https://github.com/tu_usuario/pvpc_sensor",
  "requirements": ["requests>=2.23.0"],
  "version": "1.0.0",
  "codeowners": ["@tu_usuario"],
  "config_flow": true
}
```

El campo `"config_flow": true` habilita la funcionalidad de configuración desde la UI.

### 2. **`const.py`**

Este archivo contendrá las constantes clave que utilizaremos en todo el componente.

```python
DOMAIN = "pvpc_sensor"
CONF_API_TOKEN = "api_token"
```

### 3. **`__init__.py`**

El archivo de inicialización, que manejará la configuración del componente.

```python
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    """Configuración inicial del componente desde YAML (si fuera necesario)."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Configurar el componente desde la UI."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Desinstalar la configuración del componente."""
    await hass.config_entries.async_forward_entry_unload(entry, "sensor")
    hass.data[DOMAIN].pop(entry.entry_id)
    return True
```

### 4. **`config_flow.py`**

Este archivo define el flujo de configuración, permitiendo a los usuarios ingresar su **token** de la API de ESIOS desde la UI de Home Assistant.

```python
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import config_validation as cv

from .const import DOMAIN, CONF_API_TOKEN

class PVPCSensorConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Clase que maneja el flujo de configuración del PVPC."""

    VERSION = 1

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Retornar la clase para manejar las opciones."""
        return PVPCOptionsFlowHandler(config_entry)

    async def async_step_user(self, user_input=None):
        """Primer paso cuando el usuario añade la integración desde la UI."""
        errors = {}
        
        if user_input is not None:
            # Validar el token ingresado
            api_token = user_input[CONF_API_TOKEN]
            if self._validate_api_token(api_token):
                return self.async_create_entry(title="PVPC Sensor", data=user_input)
            else:
                errors["base"] = "invalid_token"

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_API_TOKEN): str
            }),
            errors=errors
        )

    def _validate_api_token(self, token):
        """Validar el formato del token de la API (opcional, puedes mejorar la validación)."""
        return len(token) > 0

class PVPCOptionsFlowHandler(config_entries.OptionsFlow):
    """Manejo de las opciones para el flujo de configuración."""

    def __init__(self, config_entry):
        """Inicializar las opciones."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Gestionar las opciones del componente."""
        return await self.async_step_user()

    async def async_step_user(self, user_input=None):
        """Modificar las opciones desde la UI."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Optional(CONF_API_TOKEN, default=self.config_entry.data.get(CONF_API_TOKEN)): str
            })
        )
```

Este archivo define dos clases principales:
- **`PVPCSensorConfigFlow`**: Maneja el flujo de configuración cuando un usuario intenta agregar la integración desde la UI.
- **`PVPCOptionsFlowHandler`**: Permite a los usuarios modificar las opciones (como cambiar el token) después de configurar la integración.

### 5. **`sensor.py`**

Este archivo contiene la lógica del sensor. Vamos a modificarlo para obtener el **token** desde la configuración guardada en lugar de desde un archivo.

```python
import logging
import requests
from homeassistant.helpers.entity import Entity
from .const import DOMAIN, CONF_API_TOKEN

_LOGGER = logging.getLogger(__name__)

API_URL = "https://api.esios.ree.es/indicators/1001"

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Configurar el sensor basado en la entrada de configuración."""
    api_token = config_entry.data[CONF_API_TOKEN]
    async_add_entities([PVPCElectricitySensor(api_token)])

class PVPCElectricitySensor(Entity):
    """Sensor para obtener el precio PVPC de la API de ESIOS."""

    def __init__(self, api_token):
        """Inicializar el sensor."""
        self._state = None
        self._api_token = api_token
        self.update()

    @property
    def name(self):
        """Nombre del sensor."""
        return "PVPC Electricity Price"

    @property
    def state(self):
        """Retornar el estado actual."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Definir la unidad de medida."""
        return "€/kWh"

    def update(self):
        """Actualizar el sensor con datos de la API."""
        try:
            response = requests.get(
                API_URL,
                headers={
                    "Accept": "application/json",
                    "Authorization": f"Token token={self._api_token}"
                }
            )
            if response.status_code == 200:
                data = response.json()
                pvpc_value = data["indicator"]["values"][0]["value"]
                self._state = pvpc_value
            else:
                _LOGGER.error(f"Error en la API de ESIOS: {response.status_code}")
        except Exception as e:
            _LOGGER.error(f"Error al actualizar el PVPC: {e}")
```

### Resumen de Cambios:
- **Flujo de Configuración**: Ahora puedes ingresar el **token** desde la interfaz de Home Assistant al añadir el componente.
- **Persistencia del Token**: El token se guarda en la configuración del componente, y puedes modificarlo más tarde.
- **Sensor**: El sensor utiliza este token almacenado para hacer las solicitudes a la API de ESIOS.

Este enfoque permite que tu custom component sea mucho más fácil de configurar y manejar desde la interfaz de usuario de Home Assistant.
