"""
Http implementation of Expense Persistence

note: https://stackoverflow.com/questions/2386299/running-sites-on-localhost-is-extremely-slow
"""
import tdc_api_client

from tdcdesktopapp.expenses.persistence.abstract import AbstractExpensesPersistence
from tdcdesktopapp.expenses.model import Expense  # FIXME: use client model or not ?


class HttpExpensePersistence(AbstractExpensesPersistence):

    def get_all(self):
        configuration = tdc_api_client.Configuration(
            host="http://127.0.0.1:8000"
        )
        with tdc_api_client.ApiClient(configuration) as api_client:
            api_instance = tdc_api_client.ExpensesApi(api_client)
            return api_instance.get_expenses_get()
