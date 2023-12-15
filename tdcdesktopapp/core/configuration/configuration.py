__all__ = [
    'load_and_apply',
    'show_css_editor'
]
from tdcdesktopapp.core.configuration.abstract_loader import AbstractConfigurationLoader
from tdcdesktopapp.core.configuration.singleton import ConfigurationSingleton


# FIXME: this belongs to infrastructure
def load_and_apply(loader: AbstractConfigurationLoader) -> None:
    """Loads configuration to `ConfigurationSingleton`"""
    configuration = loader.load()
    ConfigurationSingleton().show_css_editor = configuration.show_css_editor

    if configuration.persistence_name == "ram":
        from tdcdesktopapp.infrastructure.ram.persistence.configuration import RamPersistenceConfiguration
        ConfigurationSingleton().persistence_configuration = RamPersistenceConfiguration()

        from tdcdesktopapp.infrastructure.ram.persistence.expense import RamExpensesPersistence
        ConfigurationSingleton().persistence_expense = RamExpensesPersistence()

        from tdcdesktopapp.infrastructure.ram.persistence.project import RamProjectsPersistence
        ConfigurationSingleton().persistence_project = RamProjectsPersistence()

        from tdcdesktopapp.infrastructure.ram.multiplayer_message_provider import RamMultiplayerMessageProvider
        ConfigurationSingleton().multiplayer_message_provider = RamMultiplayerMessageProvider()

        from tdcdesktopapp.infrastructure.ram.authentication import RamSecurityLogin
        ConfigurationSingleton().security_login = RamSecurityLogin(configuration=None)

    elif configuration.persistence_name == "http":
        from tdcdesktopapp.infrastructure.http.persistence.configuration import HttpPersistenceConfiguration
        ConfigurationSingleton().persistence_configuration = HttpPersistenceConfiguration()
        ConfigurationSingleton().persistence_configuration.attributes["api_host"] = configuration.api_host

        from tdcdesktopapp.infrastructure.http.persistence.expense import HttpExpensesPersistence
        ConfigurationSingleton().persistence_expense = HttpExpensesPersistence()

        from tdcdesktopapp.infrastructure.http.persistence.project import HttpProjectsPersistence
        ConfigurationSingleton().persistence_project = HttpProjectsPersistence()

        from tdcdesktopapp.infrastructure.http.multiplayer.message_provider import WebSocketMultiplayerMessageProvider

        if configuration.no_auth:
            from tdcdesktopapp.infrastructure.http.no_auth import NoAuthSecurityLogin

            ConfigurationSingleton().multiplayer_message_provider = WebSocketMultiplayerMessageProvider()
            ConfigurationSingleton().security_login = NoAuthSecurityLogin(
                configuration=None
            )

        else:
            from tdcdesktopapp.infrastructure.http.authentication import HttpSecurityLogin

            ConfigurationSingleton().multiplayer_message_provider = WebSocketMultiplayerMessageProvider()
            ConfigurationSingleton().security_login = HttpSecurityLogin(
                configuration=configuration.auth0_configuration_filepath
            )


def show_css_editor() -> bool:
    """Returns True if CSS editor should be shown"""
    return ConfigurationSingleton().show_css_editor
