from abc import ABC, abstractmethod

from tdcdesktopapp.core.configuration.configuration_dataclass import ConfigurationDataclass


class AbstractConfigurationLoader(ABC):
    """
    Loads configuration and returns a filled ConfigurationDataclass instance
    """

    @abstractmethod
    def load(self) -> ConfigurationDataclass:
        pass
