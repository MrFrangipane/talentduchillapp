from typing import List, Type
from dataclasses import dataclass

from tdcdesktopapp.core.configuration.singleton import ConfigurationSingleton
from tdcdesktopapp.core.entity.abstract_api import AbstractEntityApi, BaseApiOptions
from tdcdesktopapp.components.expense.model import Expense
from tdcdesktopapp.components.project.model import Project


@dataclass
class GetExpensesOptions(BaseApiOptions):
    project: Project | None = None


@dataclass
class NewExpenseOptions(BaseApiOptions):
    project: Project


class ExpensesApi(AbstractEntityApi):
    def entity_type(self) -> Type[Expense]:
        return Expense

    def get(self, options: GetExpensesOptions) -> List[Expense]:
        return ConfigurationSingleton().persistence_expense.get(options)

    def new(self, options: NewExpenseOptions) -> Expense:
        return ConfigurationSingleton().persistence_expense.new(options)

    def update(self, entity: Expense) -> None:
        return ConfigurationSingleton().persistence_expense.update(entity)

    def remove(self, entity: Expense) -> None:
        return ConfigurationSingleton().persistence_expense.remove(entity)
