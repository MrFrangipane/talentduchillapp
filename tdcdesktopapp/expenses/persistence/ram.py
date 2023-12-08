from datetime import date

from tdcdesktopapp.expenses.persistence.abstract import AbstractExpensesPersistence
from tdcdesktopapp.expenses.model import Expense


class RAMExpensePersistence(AbstractExpensesPersistence):

    def get_all(self):
        return [
            Expense(
                id="UUID",
                project="Frais Généraux",
                caption="Scotch Monoprix",
                amount=25.10,
                date_=date.today()
            ),
            Expense(
                id="UUID",
                project="Canal 211 #1",
                caption="Draps",
                amount=13.18,
                date_=date.today()
            ),
        ]
