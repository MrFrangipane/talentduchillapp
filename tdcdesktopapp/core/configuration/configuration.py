__all__ = [
    'load_and_apply',
    'show_css_editor'
]
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

        from tdcdesktopapp.components.multiplayer.message_provider.ram import RamMultiplayerMessageProvider
        ConfigurationSingleton().multiplayer_message_provider_client = RamMultiplayerMessageProvider()

        from tdcdesktopapp.components.authentication.ram import RamSecurityLogin
        ConfigurationSingleton().security_login = RamSecurityLogin(configuration=None)

    elif loader.persistence_name == "http":
        from tdcdesktopapp.components.expense.persistence.http import HttpExpensesPersistence
        ConfigurationSingleton().expense_persistence = HttpExpensesPersistence()

        from tdcdesktopapp.components.project.persistence.http import HttpProjectsPersistence
        ConfigurationSingleton().project_persistence = HttpProjectsPersistence()
        from tdcdesktopapp.components.multiplayer.message_provider.websocket import (
            WebSocketMultiplayerMessageProvider)
        ConfigurationSingleton().multiplayer_message_provider_client = WebSocketMultiplayerMessageProvider()

        from tdcdesktopapp.components.authentication.http import HttpSecurityLogin
        ConfigurationSingleton().security_login = HttpSecurityLogin(configuration=loader.auth0_configuration)


def show_css_editor() -> bool:
    """Returns True if CSS editor should be shown"""
    return ConfigurationSingleton().show_css_editor
