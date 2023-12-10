from PySide6.QtWidgets import QGroupBox, QGridLayout, QPushButton, QComboBox, QWidget
from pyside6helpers import Hourglass, combo, group
from pyside6helpers.table_view import resize_columns_to_content_with_padding


from tdcdesktopapp.core.entity.gui import EntityTable
from tdcdesktopapp.components.expense.api import ExpensesApi, GetExpensesOptions, NewExpenseOptions
from tdcdesktopapp.components.project.api import ProjectsApi


class ExpensesWidget(QGroupBox):

    def __init__(self, parent=None):
        QGroupBox.__init__(self, parent)

        self._projects = list()
        self._expenses_api = ExpensesApi()
        self._projects_api = ProjectsApi()

        self.setTitle("Expenses")

        self._entity_table = EntityTable(self._expenses_api)
        self._entity_table.dataReloadRequested.connect(self.reload)

        self._combo_project = QComboBox()
        self._combo_project.currentIndexChanged.connect(self.reload)

        self._button_add = QPushButton("Add Expense")
        self._button_add.clicked.connect(self._add_expense)
        self._button_remove = QPushButton("Remove Expense")
        self._button_remove.clicked.connect(self._entity_table.remove_entity)

        self._button_reload = QPushButton("Reload")
        self._button_reload.setMinimumWidth(200)
        self._button_reload.clicked.connect(self.reload)

        layout = QGridLayout(self)
        layout.addWidget(self._entity_table.view, 0, 0, 4, 1)
        layout.addWidget(group.make_group("Project", [self._combo_project]), 0, 1)
        layout.addWidget(group.make_group("Operations", [self._button_add, self._button_remove]), 1, 1)
        layout.addWidget(QWidget(), 2, 1)
        layout.addWidget(self._button_reload, 3, 1)
        layout.setRowStretch(2, 100)

        self.reload()

    def reload(self):
        with Hourglass(self):

            self._projects = self._projects_api.get()
            combo.update(self._combo_project, [project.name for project in self._projects])
            selected_project = self._projects[self._combo_project.currentIndex()]

            expenses = self._expenses_api.get(GetExpensesOptions(project=selected_project))
            self._entity_table.set_entities(expenses)
            resize_columns_to_content_with_padding(self._entity_table.view, 10)

    def _add_expense(self):
        selected_project = self._projects[self._combo_project.currentIndex()]
        self._expenses_api.new(NewExpenseOptions(project=selected_project))
        self.reload()
