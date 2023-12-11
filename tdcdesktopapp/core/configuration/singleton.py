from dataclasses import dataclass

from tdcdesktopapp.components.expense.persistence.abstract import AbstractExpensesPersistence
from tdcdesktopapp.components.multiplayer.message_provider.abstract import AbstractMultiplayerMessageProvider
from tdcdesktopapp.components.project.persistence.abstract import AbstractProjectsPersistence
from tdcdesktopapp.components.authentication.abstract import AbstractSecurityLogin
from tdcdesktopapp.python_extensions.singleton_metaclass import SingletonMetaclass


@dataclass
class ConfigurationSingleton(metaclass=SingletonMetaclass):
    """Singleton holding application classes and info that have been configured at startup"""
    show_css_editor: bool = None
    expense_persistence: AbstractExpensesPersistence = None
    project_persistence: AbstractProjectsPersistence = None
    multiplayer_message_provider: AbstractMultiplayerMessageProvider = None
    security_login: AbstractSecurityLogin = None
