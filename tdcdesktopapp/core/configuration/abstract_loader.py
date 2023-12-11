from abc import ABC, abstractmethod


class AbstractConfigurationLoader(ABC):
    """
    Loads and applies values that will be used by
    `tdcdesktopapp.application.singleton.ConfigurationSingleton()`
    """
    def __init__(self):
        self.auth0_configuration: str = ""
        self.persistence_name: str = ""
        self.show_css_editor: bool = False

    @abstractmethod
    def load(self):
        """Must fill class members"""
        pass
