import dataclasses
from typing import List

from PySide6.QtCore import Qt, QAbstractTableModel

from tdcdesktopapp.expenses.model import Expense
from tdcdesktopapp.expenses import api
from tdcdesktopapp.python_extensions.typing import get_fields_names


class ExpensesTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data: List[Expense] = []
        self._columns: List[str] = get_fields_names(Expense)
        self._columns_pretty = [item.replace("_", " ").capitalize() for item in self._columns]

        self.reload()

    def reload(self):
        self.beginResetModel()
        self._data = api.get_all()
        self.endResetModel()

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._columns)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return getattr(self._data[index.row()], self._columns[index.column()])

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._columns_pretty[section]
