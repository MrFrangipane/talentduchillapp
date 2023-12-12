from tdc_api_client import ExpensesApi
from tdc_api_client import Expense as ApiExpense

from tdcdesktopapp.components.expense.api import GetExpensesOptions, NewExpenseOptions
from tdcdesktopapp.components.expense.model import Expense
from tdcdesktopapp.core.abstract_persistence import AbstractPersistence
from tdcdesktopapp.infrastructure.http.persistence.utils import make_client


class HttpExpensesPersistence(AbstractPersistence):

    def get(self, options: GetExpensesOptions) -> list[Expense]:
        with make_client() as client:
            return [
                Expense(**expense.to_dict()) for expense
                in ExpensesApi(client).expenses_project_id_expenses_get(options.project.id)
            ]

    def new(self, options: NewExpenseOptions):
        with make_client() as client:
            new_expense = ExpensesApi(client).expenses_project_id_expenses_post(options.project.id)
            return Expense(**new_expense.to_dict())

    def update(self, entity: Expense) -> None:
        with make_client() as client:
            ExpensesApi(client).expenses_put(ApiExpense.from_dict(vars(entity)))

    def remove(self, entity: Expense) -> None:
        with make_client() as client:
            ExpensesApi(client).expenses_delete(ApiExpense.from_dict(vars(entity)))
