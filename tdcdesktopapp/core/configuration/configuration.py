__all__ = [
    'load_and_apply',
    'show_css_editor'
]
from tdcdesktopapp.core.configuration.abstract_loader import AbstractConfigurationLoader
from tdcdesktopapp.core.configuration.singleton import ConfigurationSingleton


# FIXME: this belongs to infrastructure
def load_and_apply(loader: AbstractConfigurationLoader) -> None:
    """Loads configuration to `ConfigurationSingleton`"""
    loader.load()
    ConfigurationSingleton().show_css_editor = loader.show_css_editor

    if loader.persistence_name == "ram":
        from tdcdesktopapp.infrastructure.ram.expense_persistence import RamExpensesPersistence
        ConfigurationSingleton().expense_persistence = RamExpensesPersistence()

        from tdcdesktopapp.infrastructure.ram.project_persistence import RamProjectsPersistence
        ConfigurationSingleton().project_persistence = RamProjectsPersistence()

        from tdcdesktopapp.infrastructure.ram.multiplayer_message_provider import RamMultiplayerMessageProvider
        ConfigurationSingleton().multiplayer_message_provider_client = RamMultiplayerMessageProvider()

        from tdcdesktopapp.infrastructure.ram.authentication import RamSecurityLogin
        ConfigurationSingleton().security_login = RamSecurityLogin(configuration=None)

    elif loader.persistence_name == "http":
        from tdcdesktopapp.infrastructure.http.expense_persistence import HttpExpensesPersistence
        ConfigurationSingleton().expense_persistence = HttpExpensesPersistence()

        from tdcdesktopapp.infrastructure.http.project_persistence import HttpProjectsPersistence
        ConfigurationSingleton().project_persistence = HttpProjectsPersistence()
        from tdcdesktopapp.infrastructure.http.websocket_multiplayer_message_provider import (
            WebSocketMultiplayerMessageProvider)
        ConfigurationSingleton().multiplayer_message_provider_client = WebSocketMultiplayerMessageProvider()

        from tdcdesktopapp.infrastructure.http.authentication import HttpSecurityLogin
        ConfigurationSingleton().security_login = HttpSecurityLogin(configuration=loader.auth0_configuration)


def show_css_editor() -> bool:
    """Returns True if CSS editor should be shown"""
    return ConfigurationSingleton().show_css_editor
