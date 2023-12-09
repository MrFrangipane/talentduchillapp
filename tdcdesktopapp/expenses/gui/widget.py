from PySide6.QtWidgets import QGroupBox, QTableView, QGridLayout, QPushButton, QComboBox, QWidget
from pyside6helpers import Hourglass, combo, group, confirmation_dialog
from pyside6helpers.table_view import resize_columns_to_content_with_padding


from tdcdesktopapp.expenses import api as expenses_api
from tdcdesktopapp.expenses.model import Expense
from tdcdesktopapp.expenses.gui.table_model import ExpensesTableModel
from tdcdesktopapp.projects import api as projects_api
from tdcdesktopapp.python_extensions.pyside.delegates import Delegates


class ExpensesWidget(QGroupBox):

    def __init__(self, parent=None):
        QGroupBox.__init__(self, parent)

        self._projects = list()

        self.setTitle("Expenses")

        self._table_model = ExpensesTableModel()

        self._table_view = QTableView()
        self._table_view.setAlternatingRowColors(True)
        self._table_view.setSelectionBehavior(QTableView.SelectRows)
        self._table_view.setSelectionMode(QTableView.SingleSelection)
        self._delegates = Delegates()
        self._delegates.apply_to_columns_from_dataclass(self._table_view, Expense)

        self._table_view.setModel(self._table_model)

        self._combo_project = QComboBox()
        self._combo_project.setMinimumWidth(200)
        self._combo_project.currentIndexChanged.connect(self.reload)

        self._button_add = QPushButton("Add Expense")
        self._button_add.clicked.connect(self.add_expense)
        self._button_remove = QPushButton("Remove Expense")
        self._button_remove.clicked.connect(self.remove_expense)

        self._button_reload = QPushButton("Reload")
        self._button_reload.clicked.connect(self.reload)

        layout = QGridLayout(self)
        layout.addWidget(self._table_view, 0, 0, 4, 1)
        layout.addWidget(group.make_group("Project", [self._combo_project]), 0, 1)
        layout.addWidget(group.make_group("Expenses", [self._button_add, self._button_remove]), 1, 1)
        layout.addWidget(QWidget(), 2, 1)
        layout.addWidget(self._button_reload, 3, 1)
        layout.setRowStretch(2, 100)

        self.reload()

    def remove_expense(self):
        for index in self._table_view.selectionModel().selectedRows():
            expense = self._table_model.expense_from_row(index.row())
            if confirmation_dialog(f"Are you sure you want to delete '{expense.caption}' ?\nYOU CAN'T GO BACK"):
                expenses_api.remove(expense)
                self.reload()

    def add_expense(self):
        selected_project = self._projects[self._combo_project.currentIndex()]
        expenses_api.new_for_project(selected_project)
        self.reload()

    def reload(self):
        with Hourglass(self):

            self._projects = projects_api.get_all()
            combo.update(self._combo_project, [project.name for project in self._projects])
            selected_project = self._projects[self._combo_project.currentIndex()]

            expenses = expenses_api.get_all_for_project(selected_project)
            self._table_model.set_expenses(expenses)
            resize_columns_to_content_with_padding(self._table_view, 10)
