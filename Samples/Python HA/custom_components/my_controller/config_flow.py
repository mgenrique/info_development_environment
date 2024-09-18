import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback

DOMAIN = "my_controller"

class MyControllerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Flujo de configuración para el componente My Controller."""

    async def async_step_user(self, user_input=None):
        """Primer paso del flujo de configuración, iniciado por el usuario."""
        if user_input is not None:
            # Validar los datos ingresados por el usuario y crear la entrada de configuración
            return self.async_create_entry(title="My Controller", data=user_input)

        # Definir el formulario que el usuario verá (campos a configurar)
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("kp"): float,
                vol.Required("ki"): float,
                vol.Required("kd"): float,
                vol.Required("setpoint"): float
            })
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return MyControllerOptionsFlow(config_entry)


class MyControllerOptionsFlow(config_entries.OptionsFlow):
    """Opciones avanzadas para el componente My Controller."""

    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Muestra las opciones avanzadas."""
        if user_input is not None:
            # Guardar las opciones avanzadas
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Optional("advanced_option", default=True): bool
            })
        )
        