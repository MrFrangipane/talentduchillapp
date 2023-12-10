from tdcdesktopapp.core.configuration.singleton import ConfigurationSingleton
from tdcdesktopapp.core.configuration.loader.abstract import AbstractConfigurationLoader


def load_and_apply(loader: AbstractConfigurationLoader) -> None:
    """Loads configuration to `ConfigurationSingleton`"""
    loader.load()
    ConfigurationSingleton().show_css_editor = loader.show_css_editor

    if loader.persistence_name == "ram":
        from tdcdesktopapp.components.expense.persistence.ram import RamExpensesPersistence
        ConfigurationSingleton().expense_persistence = RamExpensesPersistence()

        from tdcdesktopapp.components.project.persistence.ram import RamProjectsPersistence
        ConfigurationSingleton().project_persistence = RamProjectsPersistence()

        from tdcdesktopapp.components.multiplayer.client.ram import RamMultiplayerClient
        ConfigurationSingleton().multiplayer_client = RamMultiplayerClient()

    elif loader.persistence_name == "http":
        # from tdcdesktopapp.expense.persistence.http import HttpExpensesPersistence
        from tdcdesktopapp.components.project.persistence.http import HttpProjectsPersistence
        # ConfigurationSingleton().expense_persistence = HttpExpensesPersistence()
        ConfigurationSingleton().project_persistence = HttpProjectsPersistence()

        from tdcdesktopapp.components.expense.persistence.ram import RamExpensesPersistence
        ConfigurationSingleton().expense_persistence = RamExpensesPersistence()

        from tdcdesktopapp.components.multiplayer.client.websocket import WebSocketMultiplayerClient
        ConfigurationSingleton().multiplayer_client = WebSocketMultiplayerClient()


def show_css_editor() -> bool:
    """Returns True if CSS editor should be shown"""
    return ConfigurationSingleton().show_css_editor
