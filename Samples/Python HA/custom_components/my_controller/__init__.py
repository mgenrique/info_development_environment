# __init__.py

import logging

# Define el dominio de tu componente. Necesario para que Home Assistant lo reconozca como un componente
DOMAIN = "my_controller"

# Configuración básica de logging para rastrear mensajes del componente
_LOGGER = logging.getLogger(__name__)

def setup(hass, config):
    """Configura el componente base de my_controller."""
    _LOGGER.info("Iniciando el componente My Controller")

    # Aquí puedes agregar lógica para inicializar recursos
    # y hacer preparaciones necesarias para el componente
    hass.states.set(f"{DOMAIN}.status", "ready")

    # Retornar True para indicar que el componente fue inicializado correctamente
    return True

