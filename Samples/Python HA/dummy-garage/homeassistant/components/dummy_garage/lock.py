"""Platform for lock integration."""
from __future__ import annotations

import voluptuous as vol

from homeassistant.components.lock import (
    PLATFORM_SCHEMA,
    LockEntity,
)

from homeassistant.const import CONF_NAME, CONF_MAC
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType


DEFAULT_NAME = "Dummy Garage Door Lock"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_MAC): cv.string,
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    }
)


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the lock platform."""
    name = config[CONF_NAME]
    mac_addr = config[CONF_MAC]

    add_entities([DummyGarageDoorLock(mac_addr, name)])


class DummyGarageDoorLock(LockEntity):
    """Representation of a DummyGarage doorlock."""

    def __init__(self, mac, name) -> None:
        """Initialize the DummyGarage Lock Device."""
        super().__init__()
        self._mac = mac
        self._name = name
        self._state = True

    @property
    def name(self) -> str:
        """Return the name of the lock."""
        return self._name

    @property
    def unique_id(self) -> str:
        """Return a unique, Home Assistant friendly identifier for this entity."""
        # return "sdhfsdhfid23741ry9fe"
        return self._mac.replace(":", "")

    @property
    def is_locked(self) -> bool | None:
        """Return true if the lock is locked."""
        return self._state

    def lock(self, **kwargs) -> None:
        """Lock."""
        self._state = True

    def unlock(self, **kwargs) -> None:
        """Unlonk."""
        self._state = False
