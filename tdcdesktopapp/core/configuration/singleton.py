from dataclasses import dataclass

from tdcdesktopapp.components.authentication.abstract import AbstractSecurityLogin
from tdcdesktopapp.components.multiplayer.abstract_message_provider import AbstractMultiplayerMessageProvider
from tdcdesktopapp.core.abstract_persistence import AbstractPersistence
from tdcdesktopapp.core.abstract_persistence_configuration import AbstractPersistenceConfiguration
from tdcdesktopapp.python_extensions.singleton_metaclass import SingletonMetaclass


@dataclass
class ConfigurationSingleton(metaclass=SingletonMetaclass):
    """Dependency injection"""
    show_css_editor: bool = None
    persistence_configuration: AbstractPersistenceConfiguration = None
    persistence_expense: AbstractPersistence = None
    persistence_project: AbstractPersistence = None
    multiplayer_message_provider: AbstractMultiplayerMessageProvider = None
    security_login: AbstractSecurityLogin = None
