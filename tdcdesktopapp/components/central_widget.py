from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QTabWidget
from pyside6helpers import group

from tdcdesktopapp.components.expense.widget import ExpensesWidget
from tdcdesktopapp.components.project.widget import ProjectsWidget


class CentralWidget(QTabWidget):
    reloadProjects = Signal()

    def __init__(self, parent=None):
        QTabWidget.__init__(self, parent)

        self.setTabPosition(QTabWidget.TabPosition.South)

        self._projects_1 = ProjectsWidget()
        self._projects_2 = ProjectsWidget()
        self._expenses = ExpensesWidget()

        self.addTab(group.make_group(title="General", orientation=Qt.Vertical, widgets=[
            self._projects_1,
            self._projects_2
        ]), "Général")
        self.addTab(self._expenses, "Expenses")

        # self._projects_1.reload()
        # self._projects_2.reload()
        # self._expenses.reload()
