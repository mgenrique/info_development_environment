# Controlador basado en máquina de estados en un componente de Home Assistant. 
Implementa tres sensores denntro del archivo `sensor.py` : 
- `PVControllerStateSensor`: para informar del estado del componente
- `PVPCCostSensor`: Obtiene datos para las próximas 6 horas de la API de ESIOS para el PVPC
- `SolarForecastSensor`: Obtiene datos para las próximas 6 horas de la API de Forecast Solar para los Watios que se espera producir

Implementa una máquina de estados como la indicada en  [PlantUML a Python](./sm_uml_2_python.md). Esta maquina de estados está basada en la libreria `statemachine` de Python y define la lógica del diagrama.
Se compone de:
- `class CicloStateMachine`: La clase que define la maquina en si misma y que implementa métodos que se ejecutan al llegar a cada uno de los estados.
- `def ejecutar_maquina_de_estados`: la función que será llamada periodicamente por Home Assistant (en `__init__.py` se llamará a la función `ejecutar_ciclo` periodicamente al definir `async_track_time_interval(hass, ejecutar_ciclo, interval)`: La función `ejecutar_ciclo` hace una llamada a `ejecutar_maquina_de_estados`.
- `def calcular`: que se encarga del procesamiento de las informaciones de los sensores `PVPCCostSensor` y `SolarForecastSensor`. Esta función todavía está incompleta y simplemente hace un cálculo de ejemplo. Para completarla además se deberán obtener los valores aportados por la integración con el custom component de Victron, para incluir en los cálculos el SoC o el consumo actual de la instalación. Puede ser conveniente sacarla de `state_machine.py` y crear un fichero .py dedicado. Si se hace esto poner un import al fichero en `state_machine.py`.

ToDo:
- Integrar los parametros necesarios para la API de Forecast Solar en el flujo de configuración tal como se hizo en [cc_forecast_solar01](./cc_forecast_solar01.md)
- Definir como se actualiza el valor de inverter_ok que indicará que somos capaces de leer los valores necesarios del inversor y que el inversor está en un modo de control remoto
- Crear una procedimiento que se ejecute en `def on_E5` de la clase `CicloStateMachine` en el archivo `state_machine.py` que sea capaz de actualizar el Set Point del Inversor. Posiblemente el inversor no podrá estar funcionando en modo ESS, ni ESS dinamico.
- Verificar que no hay errores en el código y que el completo se carga en Home Assistant.

### Estructura del custom component

Carpeta en el directorio `custom_components` de Home Assistant llamada `pv_controller`, con la siguiente estructura:

### Estructura del componente:
```
/config
  └── custom_components
      └── pv_controller
          ├── __init__.py
          ├── manifest.json
          ├── sensor.py
          ├── const.py
          ├── config_flow.py
          └── state_machine.py  # Aquí está la definición de la máquina de estados
```

### 1. **Archivo `manifest.json`**

El archivo `manifest.json` que describe el componente. Así:

```json
{
  "domain": "pv_controller",
  "name": "PV Controller",
  "documentation": "https://github.com/mgenrique/info_development_environment",
  "dependencies": [],
  "codeowners": ["@mgenrique"],
  "version": "1.0.0",
  "requirements": [
    "python-statemachine==0.8.0",
    "requests>=2.23.0"
  ],  
  "config_flow": true
}
```

### 2. **Archivo `const.py`**

Define las constantes que se usan, como los nombres de los parámetros:

```python
DOMAIN = "pv_controller"
CONF_INVERTER_IP = "inverter_ip"
CONF_TM = "Tm"
CONF_ESIOS_TOKEN = "esios_token"
CONF_FORECAST_API_KEY = "forecast_api_key"
CONF_LATITUDE = "latitude"
CONF_LONGITUDE = "longitude"
CONF_DECIMAL = "decimal"
CONF_PEAK_POWER = "peak_power"
CONF_DECLINATION = "declination"
CONF_AZIMUTH = "azimuth"
```

### 3. **Archivo `config_flow.py`**

El flujo de configuración te permitirá al usuario introducir los valores de la IP del inversor, el valor de `Tm`,...

Aquí está el código para definir el flujo:

```python
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN, CONF_INVERTER_IP, CONF_TM, CONF_ESIOS_TOKEN, CONF_FORECAST_API_KEY

class PVControllerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for PV Controller."""

    VERSION = 1

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return PVControllerOptionsFlowHandler(config_entry)

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            return self.async_create_entry(title="PV Controller", data=user_input)

        # Definir el formulario de configuración
        data_schema = vol.Schema({
            vol.Required(CONF_INVERTER_IP): str,
            vol.Required(CONF_TM, default=30): int,
            vol.Required(CONF_ESIOS_TOKEN): str,  # Token para acceder a la API de ESIOS
            vol.Required(CONF_FORECAST_API_KEY): str  # API Key para Forecast Solar
        })

        return self.async_show_form(step_id="user", data_schema=data_schema, errors=errors)


class PVControllerOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for the PV Controller."""

    def __init__(self, config_entry):
        """Initialize PV Controller options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        return await self.async_step_user()

    async def async_step_user(self, user_input=None):
        """Handle the options."""
        errors = {}

        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        data_schema = vol.Schema({
            vol.Required(CONF_INVERTER_IP, default=self.config_entry.data.get(CONF_INVERTER_IP)): str,
            vol.Required(CONF_TM, default=self.config_entry.data.get(CONF_TM, 30)): int,
            vol.Required(CONF_ESIOS_TOKEN, default=self.config_entry.data.get(CONF_ESIOS_TOKEN)): str,
            vol.Required(CONF_FORECAST_API_KEY, default=self.config_entry.data.get(CONF_FORECAST_API_KEY)): str
        })

        return self.async_show_form(step_id="user", data_schema=data_schema, errors=errors)

```

### 4. **Archivo `__init__.py`**

El archivo `__init__.py` que inicializa el componente y prepara la máquina de estados, con los valores configurados (la IP del inversor, `Tm`,...).

```python
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.event import async_track_time_interval
from .state_machine import CicloStateMachine, ejecutar_maquina_de_estados
from .sensor import PVControllerStateSensor, PVPCCostSensor, SolarForecastSensor
from .const import DOMAIN, CONF_INVERTER_IP, CONF_TM, CONF_ESIOS_TOKEN, CONF_FORECAST_API_KEY
import datetime

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up PV Controller from a config entry."""
    inverter_ip = entry.data.get(CONF_INVERTER_IP)
    Tm = entry.data.get(CONF_TM)
    esios_token = entry.data.get(CONF_ESIOS_TOKEN)
    forecast_api_key = entry.data.get(CONF_FORECAST_API_KEY)

    # Inicializar la máquina de estados con Tm
    ciclo = CicloStateMachine()

    async def ejecutar_ciclo(event_time):
        """Función que ejecuta la máquina de estados periódicamente."""
        t = event_time.timestamp()
        t_last = hass.data[DOMAIN].get('t_last', 0)

        # Aquí obtenemos el estado de los sensores.
        sensors_ok = (
            hass.states.get("sensor.pvpc_sensor") is not None and
            hass.states.get("sensor.pvpc_sensor").state == "ok" and
            hass.states.get("sensor.solar_forecast_sensor") is not None and
            hass.states.get("sensor.solar_forecast_sensor").state == "ok"
        )

        inverter_ok = hass.states.get("sensor.inverter_state").state == "ok"  # Simulación de estado
        calcs_ok = hass.data[DOMAIN].get('calcs_ok', False)  # Usamos el valor almacenado en hass.data

        # Ejecutar la máquina de estados con los valores obtenidos
        ejecutar_maquina_de_estados(t, t_last, Tm, sensors_ok, inverter_ok, calcs_ok, hass)

        # Actualizar el tiempo de la última lectura
        hass.data[DOMAIN]['t_last'] = t

    # Guardar los datos de configuración en hass.data
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN]['t_last'] = 0  # Inicializar el tiempo de la última lectura

    # Configurar la tarea periódica (intervalo basado en el parámetro Tm)
    interval = datetime.timedelta(seconds=Tm)
    async_track_time_interval(hass, ejecutar_ciclo, interval)

    # Añadir los sensores de PVPC y Forecast Solar
    hass.async_create_task(
        hass.helpers.entity_component.async_add_entities([
            PVPCCostSensor(hass, esios_token),
            SolarForecastSensor(hass, forecast_api_key),
            PVControllerStateSensor(hass)
        ])
    )

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    return True

```

### 5. **Archivo `sensor.py`**

El archivo `sensor.py` define varios sensores que reportan el estado y obtienen valores de las API de ESIOS y Forecast.solar

```python
import requests
from homeassistant.helpers.entity import Entity
from .const import DOMAIN, CONF_ESIOS_TOKEN, CONF_FORECAST_API_KEY

class PVControllerStateSensor(Entity):
    """Representa el sensor de estado de la máquina de estados."""

    def __init__(self, hass):
        """Inicializa el sensor."""
        self.hass = hass
        self._state = None

    @property
    def name(self):
        return "PV Controller State"

    @property
    def state(self):
        return self._state

    async def async_update(self):
        """Actualizar el estado actual del sensor basado en los valores."""
        # Accede a los valores almacenados en hass.data
        sensors_ok = self.hass.data[DOMAIN].get('sensors_ok')
        inverter_ok = self.hass.data[DOMAIN].get('inverter_ok')
        calcs_ok = self.hass.data[DOMAIN].get('calcs_ok')

        # Define el estado en función de los valores
        if not sensors_ok:
            self._state = "Error: Sensores no disponibles"
        elif not inverter_ok:
            self._state = "Error: Inversor no disponible"
        elif not calcs_ok:
            self._state = "Error: Cálculos fallidos"
        else:
            self._state = "Operación normal"

        # Llama a async_schedule_update_ha_state() para notificar los cambios
        self.async_schedule_update_ha_state()


import requests
from homeassistant.helpers.entity import Entity
from .const import DOMAIN, CONF_ESIOS_TOKEN

class PVPCCostSensor(Entity):
    """Sensor para obtener el PVPC de la API de ESIOS."""

    def __init__(self, hass, esios_token):
        """Inicializa el sensor con el token de la API de ESIOS."""
        self.hass = hass
        self._state = None
        self._read_values = None  # Aquí guardaremos los valores leídos
        self._esios_token = esios_token
        """
        Para acceder al valor del estado del PVPC usar:
        hass.states.get("sensor.pvpc_sensor").state

        Para acceder a los valores leídos PVPC usar:
        hass.states.get("sensor.pvpc_sensor").attributes["read_values"]
        """

    @property
    def name(self):
        return "pvpc_sensor"

    @property
    def state(self):
        """Devuelve el estado actual del sensor (ok o error)."""
        return self._state

    @property
    def read_values(self):
        """Devuelve los valores leídos del PVPC."""
        return self._read_values

    async def async_update(self):
        """Actualizar el estado y los valores consultando la API de ESIOS."""
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Token {self._esios_token}',
        }

        try:
            response = requests.get("https://api.esios.ree.es/indicators/1001", headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()

            # Procesamos los datos de las próximas 6 horas
            self._read_values = data['included'][0]['attributes']['values'][:6]

            # Si la lectura es exitosa, establecer el estado a "ok"
            self._state = "ok"

        except requests.RequestException as e:
            # Si ocurre algún error, establecer el estado a "error"
            self._state = "error"
            self._read_values = None  # Reiniciar los valores en caso de error

        # Notificar a Home Assistant que el estado del sensor ha cambiado
        self.async_schedule_update_ha_state()
        
import requests
from homeassistant.helpers.entity import Entity
from .const import DOMAIN, CONF_FORECAST_API_KEY

class SolarForecastSensor(Entity):
    """Sensor para obtener el pronóstico solar de la API Forecast Solar."""

    def __init__(self, hass, forecast_api_key):
        """Inicializa el sensor con la API key de Forecast Solar."""
        self.hass = hass
        self._state = None
        self._read_values = None  # Aquí guardaremos los valores leídos
        self._forecast_api_key = forecast_api_key
        """
        Para acceder al valor del estado del pronóstico solar usar
        hass.states.get("sensor.solar_forecast_sensor").state

        Para acceder a los valores leídos pronóstico solar usar
        hass.states.get("sensor.solar_forecast_sensor").attributes["read_values"].
        """

    @property
    def name(self):
        return "solar_forecast_sensor"

    @property
    def state(self):
        """Devuelve el estado actual del sensor (ok o error)."""
        return self._state

    @property
    def read_values(self):
        """Devuelve los valores leídos del pronóstico solar."""
        return self._read_values

    async def async_update(self):
        """Actualizar el estado y los valores consultando la API de Forecast Solar."""
        try:
            # Realizamos la solicitud a la API de Forecast Solar
            response = requests.get(
                f"https://api.forecast.solar/{self._forecast_api_key}/estimated_actual",
                timeout=10
            )
            response.raise_for_status()
            data = response.json()

            # Procesamos los datos obtenidos de las próximas 6 horas
            self._read_values = data['result']['watts'][:6]

            # Si la lectura es exitosa, establecer el estado a "ok"
            self._state = "ok"

        except requests.RequestException as e:
            # Si ocurre algún error, establecer el estado a "error"
            self._state = "error"
            self._read_values = None  # Reiniciar los valores en caso de error

        # Notificar a Home Assistant que el estado del sensor ha cambiado
        self.async_schedule_update_ha_state()
        
```

### 6. **Archivo `state_machine.py`**

El siguiente código corresponde al contenido del fichero `state_machine.py`. 
Respecto al ejemplo de una máquina de estados generica en Python, al integrarlo en un Custom Component de Home Assistant se ha modificados para incluir `hass` como argumento de la función `ejecutar_maquina_de_estados`

Esto es necesario para que la máquina de estados pueda intercambiar información con Home Assistant, como por ejemplo comunicar el valor de sensors_ok, inverter_ok o calcs_ok para que el sensor del CC actualice su estado

```python
import logging
from statemachine import State, StateMachine

# Crear un logger para el componente
_LOGGER = logging.getLogger(__name__)
"""
_LOGGER = logging.getLogger(__name__) crea un logger específico para el componente. 
Usar __name__ asegura que el logger se asocie con el nombre del módulo en el que se está ejecutando, lo que facilita la depuración.
_LOGGER.info("mensaje"): Para mensajes informativos.
_LOGGER.warning("mensaje"): Para advertencias.
_LOGGER.error("mensaje"): Para errores críticos.
"""

class CicloStateMachine(StateMachine):
    """Definición de la máquina de estados."""
    # Definición de los estados
    E1 = State("ESPERAR NUEVO CICLO", initial=True)
    E2 = State("ESPERAR SENSORES")
    E3 = State("VERIFICAR INVERSOR")
    E4 = State("CALCULAR SALIDAS")
    E5 = State("ACTUALIZAR SALIDAS")

    # Definición de las transiciones
    fork_state_1 = E1.to(E2) | E1.to(E3)  # El fork va de E1 a E2 y E3
    join_state_1 = E2.to(E4) & E3.to(E4)  # Join combina E2 y E3 en E4
    calcular_a_actualizar = E4.to(E5)     # De E4 a E5 si se calculan correctamente las salidas
    finalizar = E5.to(E1)                 # Retorno al estado inicial para nuevo ciclo

    # Métodos que se ejecutan al realizar una transición
    def on_fork_state_1(self):
        _LOGGER.info("Fork: Esperar sensores e inversor")

    def on_join_state_1(self):
        _LOGGER.info("Join: Ambos sensores e inversor están OK, calcular salidas")

    def on_E2(self):
        _LOGGER.info("Esperando sensores...")

    def on_E3(self):
        _LOGGER.info("Verificando inversor...")

    def on_E4(self):
        _LOGGER.info("Calculando salidas...")

        # Llamar a la función calcular y asignar el resultado a calcs_ok
        calcs_ok = calcular(self.hass)

        # Notificar a Home Assistant si el cálculo fue exitoso o fallido
        if calcs_ok:
            _LOGGER.info("Cálculos exitosos, procediendo a la actualización de salidas.")
        else:
            _LOGGER.error("Fallo en los cálculos.")

        # Almacenar el valor de calcs_ok en hass.data para ser usado más adelante
        self.hass.data[DOMAIN]['calcs_ok'] = calcs_ok
        
    def on_E5(self):
        _LOGGER.info("Actualizando salidas...")

# Función para ejecutar la máquina de estados
def ejecutar_maquina_de_estados(t, t_last, Tm, sensors_ok, inverter_ok, calcs_ok, hass):
    """Función que controla la lógica de transición de estados."""
    
    ciclo = CicloStateMachine()

    # Verificar si es tiempo de iniciar un nuevo ciclo
    if t - t_last > Tm:
        _LOGGER.info(f"Iniciando nuevo ciclo. Tiempo: {t}, Última lectura: {t_last}, Tm: {Tm}")
        
        # Transición del estado E1 al fork (E2 y E3)
        ciclo.fork_state_1()

        # Verificación de sensores y avance a la siguiente etapa
        if sensors_ok:
            ciclo.E2()
            _LOGGER.info("Sensores están OK")
        else:
            _LOGGER.warning("Fallo en sensores")

        # Verificación de inversor y avance a la siguiente etapa
        if inverter_ok:
            ciclo.E3()
            _LOGGER.info("Inversor está OK")
        else:
            _LOGGER.warning("Fallo en inversor")

        # Si tanto sensores como inversor están listos, avanzar a la siguiente fase
        if sensors_ok and inverter_ok:
            ciclo.join_state_1()

        # Si los cálculos son correctos, proceder a actualizar las salidas
        if calcs_ok:
            ciclo.calcular_a_actualizar()
            _LOGGER.info("Cálculos correctos, procediendo a actualizar salidas")
        else:
            _LOGGER.warning("Fallo en cálculos, repitiendo la etapa de cálculo")

        # Volver al estado inicial para comenzar un nuevo ciclo
        ciclo.finalizar()
        _LOGGER.info("Ciclo finalizado, listo para un nuevo ciclo.")
    else:
        _LOGGER.info("No es tiempo para un nuevo ciclo aún.")
        

def calcular(hass):
    """Función de cálculo que lee los valores de los sensores y realiza el cálculo."""
    # Obtener los valores de los sensores
    solar_forecast_values = hass.states.get("sensor.solar_forecast_sensor").attributes.get("read_values", None)
    pvpc_values = hass.states.get("sensor.pvpc_sensor").attributes.get("read_values", None)

    if solar_forecast_values and pvpc_values:
        _LOGGER.info(f"Valores de solar forecast: {solar_forecast_values}")
        _LOGGER.info(f"Valores de PVPC: {pvpc_values}")

        # Realizar el cálculo
        try:
            resultado = sum(solar_forecast_values) * sum(pvpc_values)
            _LOGGER.info(f"Resultado del cálculo: {resultado}")
            return True  # El cálculo fue exitoso
        except Exception as e:
            _LOGGER.error(f"Error durante el cálculo: {e}")
            return False  # Ocurrió un error durante el cálculo
    else:
        _LOGGER.warning("No se pudieron obtener los valores de los sensores para el cálculo.")
        return False  # No se pudieron obtener los datos necesarios   

```

### Resumen del flujo:

1. El usuario configura el componente a través del UI de Home Assistant
2. El componente inicializa la máquina de estados
3. Se configura una tarea periódica para ejecutar la máquina de estados en intervalos de tiempo definidos por **Tm**.
4. Se crean sensores que representan el estado actual de la máquina de estados y las lecturas necesarias para los calculos
