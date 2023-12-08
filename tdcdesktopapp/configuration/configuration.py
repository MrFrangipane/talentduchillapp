from tdcdesktopapp.configuration.singleton import ConfigurationSingleton
from tdcdesktopapp.configuration.loader.abstract import AbstractConfigurationLoader


def load_and_apply(loader: AbstractConfigurationLoader) -> None:
    """Loads configuration to `ConfigurationSingleton`"""
    loader.load()
    ConfigurationSingleton().show_css_editor = loader.show_css_editor

    if loader.persistence_name == "ram":
        from tdcdesktopapp.expenses.persistence.ram import RamExpensesPersistence
        from tdcdesktopapp.projects.persistence.ram import RamProjectsPersistence
        ConfigurationSingleton().expense_persistence = RamExpensesPersistence()
        ConfigurationSingleton().project_persistence = RamProjectsPersistence()

    elif loader.persistence_name == "http":
        from tdcdesktopapp.expenses.persistence.http import HttpExpensesPersistence
        from tdcdesktopapp.projects.persistence.http import HttpProjectsPersistence
        ConfigurationSingleton().expense_persistence = HttpExpensesPersistence()
        ConfigurationSingleton().project_persistence = HttpProjectsPersistence()


def show_css_editor() -> bool:
    """Returns True if CSS editor should be shown"""
    return ConfigurationSingleton().show_css_editor
