from datetime import date

from tdcdesktopapp.components.expense.model import Expense
from tdcdesktopapp.components.expense.abstract_persistence import AbstractExpensesPersistence
from tdcdesktopapp.components.project.model import Project


class RamExpensesPersistence(AbstractExpensesPersistence):

    def __init__(self):
        AbstractExpensesPersistence.__init__(self)
        self._expenses = {
            "01": Expense(id="01", project="Frais Généraux", caption="Scotch Monoprix", amount=25.1, date_=date.fromisocalendar(2024, 15, 2)),
            "02": Expense(id="02", project="Frais Généraux", caption="Liquide fumée", amount=67, date_=date.fromisocalendar(2024, 16, 2)),
            "03": Expense(id="03", project="Frais Généraux", caption="Fournitures Rougier Plé (moulage)", amount=31.2, date_=date.fromisocalendar(2024, 16, 1)),
            "04": Expense(id="04", project="Frais Généraux", caption="Allo Asso", amount=77, date_=date.fromisocalendar(2024, 20, 5)),
            "05": Expense(id="05", project="Frais Généraux", caption="Essence", amount=103.2, date_=date.fromisocalendar(2024, 23, 2)),
            "06": Expense(id="06", project="Canal 211 #1", caption="Scotch Monoprix", amount=27.37, date_=date.fromisocalendar(2024, 15, 5)),
            "07": Expense(id="07", project="Canal 211 #1", caption="Repas equipe", amount=25.10, date_=date.fromisocalendar(2024, 20, 2)),
            "08": Expense(id="08", project="Canal 211 #1", caption="Location Camion", amount=175, date_=date.fromisocalendar(2024, 31, 4)),
            "09": Expense(id="09", project="Canal 211 #1", caption="Commande T shirts", amount=302, date_=date.fromisocalendar(2024, 32, 1)),
            "10": Expense(id="10", project="Canal 211 #1", caption="Gaffer", amount=27.15, date_=date.fromisocalendar(2024, 40, 6)),
            "11": Expense(id="11", project="Canal 211 #1", caption="Catering", amount=12, date_=date.fromisocalendar(2024, 47, 2)),
        }

    def get_all(self):
        return list(self._expenses.values())

    def get_all_for_project(self, project: Project):
        return list([expense for expense in self._expenses.values() if expense.project == project.name])

    def new_for_project(self, project: Project) -> Expense:
        new_index = max([int(index) for index in self._expenses.keys()]) + 1
        new_expense = Expense(
            id=f"{new_index:02d}",
            project=project.name,
            caption="New Expense",
            amount=0,
            date_=date.today()
        )
        self._expenses[new_expense.id] = new_expense
        return new_expense

    def update(self, expense: Expense):
        self._expenses[expense.id] = expense

    def remove(self, expense: Expense):
        self._expenses.pop(expense.id)
