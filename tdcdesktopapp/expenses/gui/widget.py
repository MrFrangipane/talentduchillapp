from PySide6.QtWidgets import QGroupBox, QTableView, QGridLayout

from tdcdesktopapp.expenses.gui.table_model import ExpensesTableModel


class ExpensesWidget(QGroupBox):

    def __init__(self, parent=None):
        QGroupBox.__init__(self, parent)

        self.setTitle("Expenses")

        self._table_view = QTableView()
        self._table_view.setAlternatingRowColors(True)
        self._table_view.setModel(ExpensesTableModel())

        layout = QGridLayout(self)
        layout.addWidget(self._table_view)
