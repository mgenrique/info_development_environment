# Ejemplo de custom component para Home Assistant que genera un sensor cuyo valor lo obtiene de la API de https://api.forecast.solar/

A continuación te muestro un ejemplo de un **custom component** para Home Assistant que obtiene el valor de los **watts de las próximas 6 horas** desde la API de [API Forecast.Solar](https://api.forecast.solar/) [WEB Forecast.Solar](https://forecast.solar/) y lo muestra como un sensor.

### Estructura del componente

La estructura del componente debe ser la siguiente:

```
custom_components/
  solar_forecast_sensor/
    __init__.py
    manifest.json
    sensor.py
    config_flow.py
    const.py
```

### 1. **`manifest.json`**

Este archivo describe tu custom component, incluyendo las dependencias y metadatos.

```json
{
  "domain": "solar_forecast_sensor",
  "name": "Solar Forecast Sensor",
  "documentation": "https://github.com/tu_usuario/solar_forecast_sensor",
  "requirements": ["requests>=2.23.0"],
  "version": "1.0.0",
  "codeowners": ["@tu_usuario"],
  "config_flow": true
}
```

### 2. **`const.py`**

Este archivo contiene las constantes que usarás en el componente.

```python
DOMAIN = "solar_forecast_sensor"
CONF_API_KEY = "api_key"
CONF_LATITUDE = "latitude"
CONF_LONGITUDE = "longitude"
CONF_DECIMAL = "decimal"
CONF_PEAK_POWER = "peak_power"
CONF_DECLINATION = "declination"
CONF_AZIMUTH = "azimuth"
```

### 3. **`__init__.py`**

Este archivo inicializa el componente y gestiona la configuración desde la UI.

```python
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    """Configuración inicial desde YAML (si fuera necesario)."""
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

Este archivo permite ingresar los detalles de configuración, como el **API key**, la **ubicación** y otros parámetros desde la UI.

```python
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import config_validation as cv

from .const import DOMAIN, CONF_API_KEY, CONF_LATITUDE, CONF_LONGITUDE, CONF_PEAK_POWER, CONF_DECLINATION, CONF_AZIMUTH

class SolarForecastConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Clase que maneja el flujo de configuración del sensor de solar forecast."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Primer paso cuando el usuario añade la integración desde la UI."""
        errors = {}
        
        if user_input is not None:
            return self.async_create_entry(title="Solar Forecast", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_API_KEY): str,
                vol.Required(CONF_LATITUDE): cv.latitude,
                vol.Required(CONF_LONGITUDE): cv.longitude,
                vol.Required(CONF_PEAK_POWER): vol.Coerce(float),
                vol.Optional(CONF_DECLINATION, default=0): vol.Coerce(float),
                vol.Optional(CONF_AZIMUTH, default=0): vol.Coerce(float)
            }),
            errors=errors
        )
```

### 5. **`sensor.py`**

Este archivo contiene la lógica del sensor, incluyendo la llamada a la API de **Forecast.Solar** para obtener los datos de las próximas 6 horas.

```python
import logging
import requests
from datetime import timedelta
from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle
from .const import DOMAIN, CONF_API_KEY, CONF_LATITUDE, CONF_LONGITUDE, CONF_PEAK_POWER, CONF_DECLINATION, CONF_AZIMUTH

_LOGGER = logging.getLogger(__name__)

API_URL = "https://api.forecast.solar/estimate/{latitude}/{longitude}/{dec}/{az}/{kwp}"

MIN_TIME_BETWEEN_UPDATES = timedelta(hours=1)

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Configurar el sensor basado en la entrada de configuración."""
    api_key = config_entry.data[CONF_API_KEY]
    latitude = config_entry.data[CONF_LATITUDE]
    longitude = config_entry.data[CONF_LONGITUDE]
    peak_power = config_entry.data[CONF_PEAK_POWER]
    declination = config_entry.data.get(CONF_DECLINATION, 0)
    azimuth = config_entry.data.get(CONF_AZIMUTH, 0)
    
    async_add_entities([SolarForecastSensor(api_key, latitude, longitude, peak_power, declination, azimuth)])

class SolarForecastSensor(Entity):
    """Sensor para obtener el pronóstico solar desde la API de Forecast.Solar."""

    def __init__(self, api_key, latitude, longitude, peak_power, declination, azimuth):
        """Inicializar el sensor."""
        self._state = None
        self._api_key = api_key
        self._latitude = latitude
        self._longitude = longitude
        self._peak_power = peak_power
        self._declination = declination
        self._azimuth = azimuth
        self.update()

    @property
    def name(self):
        """Nombre del sensor."""
        return "Solar Forecast - Next 6 Hours"

    @property
    def state(self):
        """Retornar el estado actual."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Definir la unidad de medida."""
        return "W"

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        """Actualizar el sensor con datos de la API."""
        try:
            response = requests.get(
                API_URL.format(
                    latitude=self._latitude,
                    longitude=self._longitude,
                    dec=self._declination,
                    az=self._azimuth,
                    kwp=self._peak_power
                ),
                headers={"Authorization": f"Bearer {self._api_key}"}
            )
            if response.status_code == 200:
                data = response.json()
                # Extraer los valores de las próximas 6 horas
                future_values = data["result"]["watts"].values()
                self._state = sum(list(future_values)[:6])  # Suma de los watts de las próximas 6 horas
            else:
                _LOGGER.error(f"Error en la API de Forecast.Solar: {response.status_code}")
        except Exception as e:
            _LOGGER.error(f"Error al actualizar el pronóstico solar: {e}")
```

### Explicación del código:

1. **Constantes**:
   - **`API_URL`**: Es la URL de la API de **Forecast.Solar** donde se envían las solicitudes.
   - **`MIN_TIME_BETWEEN_UPDATES`**: Define un límite para actualizar el sensor cada hora para evitar saturar la API.

2. **Clase `SolarForecastSensor`**:
   - **`__init__`**: Inicializa el sensor y almacena los parámetros clave como la latitud, longitud y otros necesarios para hacer la solicitud a la API.
   - **`name`**: Define el nombre del sensor que aparecerá en Home Assistant.
   - **`state`**: Retorna la suma de los valores de watts para las próximas 6 horas.
   - **`update`**: Hace una solicitud a la API de Forecast.Solar usando los parámetros de configuración y actualiza el valor del sensor.

3. **Throttle**: Se limita la frecuencia de las actualizaciones para evitar sobrecargar la API.

### 6. **Configuración en `configuration.yaml`**

Para que el sensor funcione correctamente, puedes añadir una entrada en `configuration.yaml` si lo prefieres manejar manualmente (aunque este componente está diseñado para configurarse desde la UI):

```yaml
sensor:
  - platform: solar_forecast_sensor
```

### Resumen

Este **custom component** para Home Assistant utiliza la API de **Forecast.Solar** para obtener los datos de watts estimados para las próximas 6 horas. El usuario puede configurar el **API key** y otros parámetros como la **ubicación** y la **potencia pico del sistema fotovoltaico** desde la interfaz de usuario de Home Assistant, lo que hace que el componente sea flexible y fácil de usar.

Recuerda que necesitarás una **API key** válida de [Forecast.Solar](https://api.forecast.solar/) para usar este componente.
