from typing import Any
from tdcdesktopapp.core.configuration.singleton import ConfigurationSingleton


def is_available() -> bool:
    return ConfigurationSingleton().persistence_configuration.is_available()


def get_parameter(parameter_name: str) -> Any:
    return ConfigurationSingleton().persistence_configuration.attributes[parameter_name]
