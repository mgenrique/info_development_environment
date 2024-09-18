"""The Dummy Garage integration."""
from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Your controller/hub specific code."""

    return True
