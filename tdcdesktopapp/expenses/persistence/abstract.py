from abc import ABC, abstractmethod
from typing import List

from tdcdesktopapp.expenses.model import Expense


class AbstractExpensesPersistence(ABC):
    """Loads and saves Expenses"""

    @abstractmethod
    def get_all(self) -> List[Expense]:
        """Must fill class members"""
        pass
