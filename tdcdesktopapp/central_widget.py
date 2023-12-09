from PySide6.QtWidgets import QTabWidget

from tdcdesktopapp.expenses.widget import ExpensesWidget
from tdcdesktopapp.projects.widget import ProjectsWidget


class CentralWidget(QTabWidget):
    def __init__(self, parent=None):
        QTabWidget.__init__(self, parent)

        self.setTabPosition(QTabWidget.TabPosition.South)

        self.addTab(ProjectsWidget(), "Projects")
        self.addTab(ExpensesWidget(), "Expenses")
