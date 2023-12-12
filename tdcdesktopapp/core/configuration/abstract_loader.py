from abc import ABC, abstractmethod


class AbstractConfigurationLoader(ABC):
    """
    Loads and applies values that will be used by
    `tdcdesktopapp.application.singleton.ConfigurationSingleton()`
    """
    def __init__(self):
        self.api_host: str = ""  # used by http implementations
        self.auth0_configuration: str = ""  # used by http implementations
        self.persistence_name: str = ""  # defines if using http or ram implementations
        self.show_css_editor: bool = False

    @abstractmethod
    def load(self):
        """Must fill class members"""
        pass
