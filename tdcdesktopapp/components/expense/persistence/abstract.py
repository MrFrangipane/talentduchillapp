from abc import ABC, abstractmethod

from tdcdesktopapp.components.expense.model import Expense
from tdcdesktopapp.components.project.model import Project


class AbstractExpensesPersistence(ABC):
    """Loads and saves Expenses"""

    @abstractmethod
    def get_all_for_project(self, project: Project) -> list[Expense]:
        pass

    @abstractmethod
    def new_for_project(self, project: Project, expense: Expense) -> Expense:
        pass

    @abstractmethod
    def update(self, expense: Expense):
        pass

    @abstractmethod
    def remove(self, expense: Expense):
        pass
