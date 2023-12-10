from dataclasses import dataclass

from tdcdesktopapp.components.expense.persistence.abstract import AbstractExpensesPersistence
from tdcdesktopapp.components.project.persistence.abstract import AbstractProjectsPersistence
from tdcdesktopapp.components.multiplayer.client.abstract import AbstractMultiplayerClient
from tdcdesktopapp.python_extensions.singleton_metaclass import SingletonMetaclass


@dataclass
class ConfigurationSingleton(metaclass=SingletonMetaclass):
    """Singleton holding application classes and info that have been configured at startup"""
    show_css_editor: bool = None
    expense_persistence: AbstractExpensesPersistence = None
    project_persistence: AbstractProjectsPersistence = None
    multiplayer_client: AbstractMultiplayerClient = None
