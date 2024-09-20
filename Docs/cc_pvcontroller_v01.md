# Máquina de estados en un componente de Home Assistant

Para integrar el código de la máquina de estados vista en [PlantUML a Python](./sm_uml_2_python.md) dentro de un **custom component de Home Assistant** llamado `pv_controller`, puedes seguir estos pasos. Crearemos un componente personalizado con un flujo de configuración para que el usuario pueda ingresar los parámetros **IP del inversor** y **Tm**.

### Estructura del custom component

Crea una carpeta en tu directorio de `custom_components` llamada `pv_controller`, con la siguiente estructura básica:

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

El archivo `manifest.json` describe tu componente. Puedes configurarlo así:

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

Define las constantes que usarás, como los nombres de los parámetros:

```python
DOMAIN = "pv_controller"
CONF_INVERTER_IP = "inverter_ip"
CONF_TM = "Tm"
```

### 3. **Archivo `config_flow.py`**

El flujo de configuración te permitirá al usuario introducir los valores de la IP del inversor y el valor de `Tm`. Aquí está el código para definir el flujo:

```python
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN, CONF_INVERTER_IP, CONF_TM

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
        })

        return self.async_show_form(step_id="user", data_schema=data_schema, errors=errors)
```

### 4. **Archivo `__init__.py`**

El archivo `__init__.py` es donde inicializas tu componente y preparas la máquina de estados, con los valores configurados (la IP del inversor y `Tm`).

```python
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN, CONF_INVERTER_IP, CONF_TM
from .state_machine import CicloStateMachine, ejecutar_maquina_de_estados
from .sensor import PVControllerStateSensor

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up PV Controller from a config entry."""
    inverter_ip = entry.data.get(CONF_INVERTER_IP)
    Tm = entry.data.get(CONF_TM)

    # Agregar el sensor de estado
    hass.async_create_task(
        hass.helpers.entity_component.async_add_entities([PVControllerStateSensor(hass)])
    )
    
    # Inicializar la máquina de estados con Tm
    ciclo = CicloStateMachine()

    async def ejecutar_ciclo(event_time):
        """Función que ejecuta la máquina de estados periódicamente."""
        t = event_time.timestamp()
        t_last = hass.data[DOMAIN].get('t_last', 0)
        sensors_ok = True  # Simulación de sensores
        inverter_ok = True  # Simulación de inversor
        calcs_ok = True     # Simulación de cálculos

        ejecutar_maquina_de_estados(t, t_last, Tm, sensors_ok, inverter_ok, calcs_ok)

        # Actualizar el tiempo de la última lectura
        hass.data[DOMAIN]['t_last'] = t

    # Guardar los datos de configuración en hass.data
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN]['t_last'] = 0  # Tiempo de la última lectura

    # Configurar una tarea periódica en Home Assistant
    hass.helpers.event.async_track_time_interval(ejecutar_ciclo, Tm)

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    return True

```

### 5. **Archivo `sensor.py`**

Si quieres definir algún sensor basado en el estado de la máquina, puedes hacerlo en el archivo `sensor.py`. Un ejemplo sencillo sería crear un sensor que reporte el estado actual de la máquina de estados.

```python
from homeassistant.helpers.entity import Entity
from .const import DOMAIN

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

```

### Resumen del flujo:

1. El usuario configura el componente a través del UI de Home Assistant, indicando la **IP del inversor** y el valor de **Tm**.
2. El componente inicializa la máquina de estados en base al valor de **Tm**.
3. Se configura una tarea periódica para ejecutar la máquina de estados en intervalos de tiempo definidos por **Tm**.
4. Opcionalmente, puedes crear sensores que representen el estado actual de la máquina de estados.

Este ejemplo es un punto de partida básico que puedes extender según las necesidades de tu proyecto en Home Assistant.
