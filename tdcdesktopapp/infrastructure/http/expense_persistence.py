"""
Http implementation of Project Persistence

note: https://stackoverflow.com/questions/2386299/running-sites-on-localhost-is-extremely-slow
"""
import tdc_api_client as client
from tdc_api_client.exceptions import ForbiddenException

from tdcdesktopapp.components.authentication.api import get_token
from tdcdesktopapp.components.expense.abstract_persistence import AbstractExpensesPersistence
from tdcdesktopapp.components.expense.model import Expense
from tdcdesktopapp.components.project.model import Project
from tdcdesktopapp.core.exceptions import PersistenceException


class HttpExpensesPersistence(AbstractExpensesPersistence):

    def get_all_for_project(self, project: Project):
        try:
            configuration = client.Configuration(host="http://127.0.0.1:8000", access_token=get_token())
            with client.ApiClient(configuration) as api_client:
                api_instance = client.ExpensesApi(api_client)
                return [
                    Expense(**expense.to_dict()) for expense
                    in api_instance.expenses_project_id_expenses_get(project.id)
                ]

        except ForbiddenException as error:
            raise PersistenceException(str(error))

    def new_for_project(self, project: Project, expense: Expense):
        try:
            client_expense = client.Expense.from_dict(vars(expense))

            configuration = client.Configuration(host="http://127.0.0.1:8000", access_token=get_token())
            with client.ApiClient(configuration) as api_client:
                api_instance = client.ExpensesApi(api_client)
                new_expense = api_instance.expenses_project_id_expenses_post(project.id, client_expense)
                return Expense(**new_expense.to_dict())

        except ForbiddenException as error:
            raise PersistenceException(str(error))

    def update(self, expense: Expense):
        try:
            client_expense = client.Expense.from_dict(vars(expense))

            configuration = client.Configuration(host="http://127.0.0.1:8000", access_token=get_token())
            with client.ApiClient(configuration) as api_client:
                api_instance = client.ExpensesApi(api_client)
                api_instance.expenses_put(client_expense)

        except ForbiddenException as error:
            raise PersistenceException(str(error))

    def remove(self, expense: Expense):
        try:
            client_expense = client.Expense.from_dict(vars(expense))

            configuration = client.Configuration(host="http://127.0.0.1:8000", access_token=get_token())
            with client.ApiClient(configuration) as api_client:
                api_instance = client.ExpensesApi(api_client)
                api_instance.expenses_delete(client_expense)

        except ForbiddenException as error:
            raise PersistenceException(str(error))
