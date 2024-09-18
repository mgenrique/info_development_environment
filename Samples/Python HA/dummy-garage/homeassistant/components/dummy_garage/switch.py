"""Platform for switch integration."""
from __future__ import annotations


import voluptuous as vol

from homeassistant.components.switch import PLATFORM_SCHEMA, SwitchEntity
from homeassistant.const import CONF_MAC, CONF_NAME
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

CONF_FLIP_ON_OFF = "flip_on_off"
DEFAULT_NAME = "Dummy Garage Door Switch"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_MAC): cv.string,
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Optional(CONF_FLIP_ON_OFF, default=False): cv.boolean,
    }
)


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Perform the setup for GarageDoor devices."""
    name = config[CONF_NAME]
    mac_addr = config[CONF_MAC]
    flip_on_off = config[CONF_FLIP_ON_OFF]
    add_entities([DummyGarageDoorSwitch(mac_addr, name, flip_on_off)], True)


class DummyGarageDoorSwitch(SwitchEntity):
    """Representation of a SmartGarageDoorSwitch."""

    def __init__(self, mac, name, flip_on_off) -> None:
        """Initialize the SmartGarageDoorSwitch."""
        super().__init__()
        self._mac = mac
        self._name = name
        self._available = True
        self._device = name
        self._state = flip_on_off

    @property
    def unique_id(self) -> str:
        """Return a unique, Home Assistant friendly identifier for this entity."""
        return self._mac.replace(":", "")

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return self._available

    @property
    def name(self) -> str:
        """Return the name of the switch."""
        return self._name

    def update(self) -> None:
        """Synchronize state with switch."""
        # self.hass.states.set(STATE_ENTITY_ID, self._state)

    @property
    def is_on(self) -> bool:
        """Return true if it is on."""
        return self._state

    def turn_on(self, **kwargs) -> None:
        """Turn the switch on."""
        self._state = True

    def turn_off(self, **kwargs) -> None:
        """Turn the switch off."""
        self._state = False
