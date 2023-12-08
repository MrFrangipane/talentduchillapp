from abc import ABC, abstractmethod
from typing import List

from tdcdesktopapp.expenses.model import Expense
from tdcdesktopapp.projects.model import Project


class AbstractExpensesPersistence(ABC):
    """Loads and saves Expenses"""

    @abstractmethod
    def get_all(self) -> List[Expense]:
        pass

    @abstractmethod
    def get_all_for_project(self, project: Project):
        pass
