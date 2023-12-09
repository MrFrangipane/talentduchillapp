from typing import List, Type
from dataclasses import dataclass

from tdcdesktopapp.configuration.singleton import ConfigurationSingleton
from tdcdesktopapp.entity.abstract_api import AbstractEntityApi, BaseApiOptions
from tdcdesktopapp.expenses.model import Expense
from tdcdesktopapp.projects.model import Project


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
        if options.project is None:
            return ConfigurationSingleton().expense_persistence.get_all()
        else:
            return ConfigurationSingleton().expense_persistence.get_all_for_project(options.project)

    def new(self, options: NewExpenseOptions) -> Expense:
        return ConfigurationSingleton().expense_persistence.new_for_project(options.project)

    def update(self, entity: Expense) -> None:
        return ConfigurationSingleton().expense_persistence.update(entity)

    def remove(self, entity: Expense) -> None:
        return ConfigurationSingleton().expense_persistence.remove(entity)
