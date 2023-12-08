from dataclasses import dataclass

from tdcdesktopapp.python_extensions.singleton_metaclass import SingletonMetaclass
from tdcdesktopapp.expenses.persistence.abstract import AbstractExpensesPersistence
from tdcdesktopapp.projects.persistence.abstract import AbstractProjectsPersistence


@dataclass
class ConfigurationSingleton(metaclass=SingletonMetaclass):
    """Singleton holding application classes and info that have been configured at startup"""
    show_css_editor: bool = None
    expense_persistence: AbstractExpensesPersistence = None
    project_persistence: AbstractProjectsPersistence = None
