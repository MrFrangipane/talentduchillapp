__all__ = [
    'load_and_apply',
    'show_css_editor'
]
from tdcdesktopapp.core.configuration.abstract_loader import AbstractConfigurationLoader
from tdcdesktopapp.core.configuration.singleton import ConfigurationSingleton


def load_and_apply(loader: AbstractConfigurationLoader) -> None:
    """Loads configuration to `ConfigurationSingleton`"""
    loader.load()
    ConfigurationSingleton().show_css_editor = loader.show_css_editor

    if loader.persistence_name == "ram":
        from tdcdesktopapp.infrastructure.expense.ram import RamExpensesPersistence
        ConfigurationSingleton().expense_persistence = RamExpensesPersistence()

        from tdcdesktopapp.infrastructure.project.ram import RamProjectsPersistence
        ConfigurationSingleton().project_persistence = RamProjectsPersistence()

        from tdcdesktopapp.infrastructure.multiplayer_message_provider.ram import RamMultiplayerMessageProvider
        ConfigurationSingleton().multiplayer_message_provider_client = RamMultiplayerMessageProvider()

        from tdcdesktopapp.infrastructure.authentication.ram import RamSecurityLogin
        ConfigurationSingleton().security_login = RamSecurityLogin(configuration=None)

    elif loader.persistence_name == "http":
        from tdcdesktopapp.infrastructure.expense.http import HttpExpensesPersistence
        ConfigurationSingleton().expense_persistence = HttpExpensesPersistence()

        from tdcdesktopapp.infrastructure.project.http import HttpProjectsPersistence
        ConfigurationSingleton().project_persistence = HttpProjectsPersistence()
        from tdcdesktopapp.infrastructure.multiplayer_message_provider.websocket import (
            WebSocketMultiplayerMessageProvider)
        ConfigurationSingleton().multiplayer_message_provider_client = WebSocketMultiplayerMessageProvider()

        from tdcdesktopapp.infrastructure.authentication.http import HttpSecurityLogin
        ConfigurationSingleton().security_login = HttpSecurityLogin(configuration=loader.auth0_configuration)


def show_css_editor() -> bool:
    """Returns True if CSS editor should be shown"""
    return ConfigurationSingleton().show_css_editor
