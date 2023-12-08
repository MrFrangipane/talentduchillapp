from PySide6.QtWidgets import QGroupBox, QTableView, QGridLayout, QPushButton, QComboBox, QWidget

from pyside6helpers import Hourglass, combo

from tdcdesktopapp.expenses import api as expenses_api
from tdcdesktopapp.projects import api as projects_api
from tdcdesktopapp.expenses.gui.table_model import ExpensesTableModel


class ExpensesWidget(QGroupBox):

    def __init__(self, parent=None):
        QGroupBox.__init__(self, parent)

        self.setTitle("Expenses")

        self._table_model = ExpensesTableModel()

        self._table_view = QTableView()
        self._table_view.setAlternatingRowColors(True)
        self._table_view.setModel(self._table_model)

        self._combo_project = QComboBox()
        self._combo_project.setMinimumWidth(200)
        self._combo_project.currentIndexChanged.connect(self.reload)

        self._button_reload = QPushButton("Reload")
        self._button_reload.clicked.connect(self.reload)

        layout = QGridLayout(self)
        layout.addWidget(self._table_view, 0, 0, 3, 1)
        layout.addWidget(self._combo_project, 0, 1)
        layout.addWidget(self._button_reload, 1, 1)
        layout.addWidget(QWidget(), 2, 1)
        layout.setRowStretch(2, 100)

        self.reload()

    def reload(self):
        with Hourglass(self):
            projects = projects_api.get_all()

            combo.update(self._combo_project, [project.name for project in projects])

            selected_project = projects[self._combo_project.currentIndex()]
            expenses = expenses_api.get_all_for_project(selected_project)
            self._table_model.set_expenses(expenses)
