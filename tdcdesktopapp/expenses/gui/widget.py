from PySide6.QtWidgets import QGroupBox, QTableView, QGridLayout ,QPushButton

from pyside6helpers import Hourglass

from tdcdesktopapp.expenses.gui.table_model import ExpensesTableModel


class ExpensesWidget(QGroupBox):

    def __init__(self, parent=None):
        QGroupBox.__init__(self, parent)

        self.setTitle("Expenses")

        self._table_model = ExpensesTableModel()

        self._table_view = QTableView()
        self._table_view.setAlternatingRowColors(True)
        self._table_view.setModel(self._table_model)

        self._button_reload = QPushButton("Reload")
        self._button_reload.clicked.connect(self.reload)

        layout = QGridLayout(self)
        layout.addWidget(self._table_view)
        layout.addWidget(self._button_reload)

    def reload(self):
        with Hourglass(self):
            self._table_model.reload()
