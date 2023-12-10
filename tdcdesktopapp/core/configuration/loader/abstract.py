from abc import ABC, abstractmethod


class AbstractConfigurationLoader(ABC):
    """
    Loads and applies values that will be used by
    `tdcdesktopapp.application.singleton.ConfigurationSingleton()`
    """
    def __init__(self):
        self.show_css_editor: bool = False
        self.persistence_name: str = ""

    @abstractmethod
    def load(self):
        """Must fill class members"""
        pass
