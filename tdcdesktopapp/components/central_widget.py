from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTabWidget
from pyside6helpers import group

from tdcdesktopapp.components.expense.widget import ExpensesWidget
from tdcdesktopapp.components.project.widget import ProjectsWidget


class CentralWidget(QTabWidget):
    def __init__(self, parent=None):
        QTabWidget.__init__(self, parent)

        self.setTabPosition(QTabWidget.TabPosition.South)

        self.addTab(group.make_group(title="General", orientation=Qt.Vertical, widgets=[
            ProjectsWidget(),
            ProjectsWidget()
        ]), "Général")
        self.addTab(ExpensesWidget(), "Expenses")
