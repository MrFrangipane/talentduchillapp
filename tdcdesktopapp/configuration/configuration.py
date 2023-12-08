from tdcdesktopapp.configuration.singleton import ConfigurationSingleton
from tdcdesktopapp.configuration.loader.abstract import AbstractConfigurationLoader


def load_and_apply(loader: AbstractConfigurationLoader) -> None:
    """Loads configuration to `ConfigurationSingleton`"""
    loader.load()
    ConfigurationSingleton().show_css_editor = loader.show_css_editor

    if loader.persistence_name == "ram":
        from tdcdesktopapp.expenses.persistence.ram import RamExpensePersistence
        ConfigurationSingleton().expense_persistence = RamExpensePersistence()

    elif loader.persistence_name == "http":
        from tdcdesktopapp.expenses.persistence.http import HttpExpensePersistence
        ConfigurationSingleton().expense_persistence = HttpExpensePersistence()


def show_css_editor() -> bool:
    """Returns True if CSS editor should be shown"""
    return ConfigurationSingleton().show_css_editor
