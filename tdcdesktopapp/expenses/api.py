from typing import List

from tdcdesktopapp.configuration.singleton import ConfigurationSingleton
from tdcdesktopapp.projects.model import Project
from tdcdesktopapp.expenses.model import Expense


def get_all() -> List[Expense]:
    return ConfigurationSingleton().expense_persistence.get_all()


def get_all_for_project(project: Project) -> List[Expense]:
    return ConfigurationSingleton().expense_persistence.get_all_for_project(project)


def update(expense: Expense) -> None:
    return ConfigurationSingleton().expense_persistence.update(expense)


def remove(expense: Expense) -> None:
    return ConfigurationSingleton().expense_persistence.remove(expense)


def new_for_project(project: Project) -> Expense:
    return ConfigurationSingleton().expense_persistence.new_for_project(project)
