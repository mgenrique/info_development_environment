"""Platform for binary sensor integration."""
from __future__ import annotations

import voluptuous as vol

from homeassistant.components.binary_sensor import (
    PLATFORM_SCHEMA,
    BinarySensorDeviceClass,
    BinarySensorEntity,
)
from homeassistant.const import CONF_DEVICE_CLASS, CONF_MAC, CONF_NAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
import homeassistant.helpers.config_validation as cv

DEFAULT_NAME = "Dummy Garage - Binary Sensor"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_MAC): cv.string,
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Optional(
            CONF_DEVICE_CLASS, default=BinarySensorDeviceClass.PRESENCE
        ): cv.string,
    }
)


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the binary sensor platform."""
    name = config[CONF_NAME]
    mac_addr = config[CONF_MAC]
    device_class = config[CONF_DEVICE_CLASS]

    add_entities([DummyBinarySensor(mac_addr, name, device_class)], True)


class DummyBinarySensor(BinarySensorEntity):
    """Representation of a Sensor."""

    def __init__(self, mac, name, device_class) -> None:
        self._mac = mac
        self._name = name
        self._attr_name = name
        self._attr_device_class = device_class
        self._state = True

    @property
    def unique_id(self) -> str:
        """Return a unique, Home Assistant friendly identifier for this entity."""
        return self._mac.replace(":", "")

    @property
    def is_on(self) -> bool:
        """Return true if it is on."""
        return self._state
