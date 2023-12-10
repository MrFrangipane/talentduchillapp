"""
Http implementation of Project Persistence

note: https://stackoverflow.com/questions/2386299/running-sites-on-localhost-is-extremely-slow
"""
from typing import List

import tdc_api_client as client

from tdcdesktopapp.components.expense.persistence.abstract import AbstractExpensesPersistence
from tdcdesktopapp.components.expense.model import Expense
from tdcdesktopapp.components.project.model import Project


class HttpExpensesPersistence(AbstractExpensesPersistence):
    def get_all(self) -> List[Expense]:
        configuration = client.Configuration(host="http://127.0.0.1:8000")
        with client.ApiClient(configuration) as api_client:
            api_instance = client.ExpensesApi(api_client)
            return [Expense(**expense.to_dict()) for expense in api_instance.get_expenses_get()]

    def get_all_for_project(self, project: Project):
        configuration = client.Configuration(host="http://127.0.0.1:8000")
        with client.ApiClient(configuration) as api_client:
            api_instance = client.ExpensesApi(api_client)
            return [Expense(**expense.to_dict()) for expense in api_instance.get_project_expenses_project_id_expenses_get(project.id)]
