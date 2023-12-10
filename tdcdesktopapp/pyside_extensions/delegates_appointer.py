from datetime import date
from typing import get_args

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QTableView
from pyside6helpers.item_delegates import BooleanDelegate, DateDelegate, CurrencyDelegate

from tdcdesktopapp.python_extensions.typing import get_fields_types, Currency


class DelegatesAppointer(QObject):
    """Holds and applies item delegates according to dataclass fields types"""
    def __init__(self, parent=None):
        QObject.__init__(self, parent)

        self._bool = BooleanDelegate()
        self._date = DateDelegate()
        self._currency = CurrencyDelegate()

    def appoint_to_columns_from_dataclass(self, table: QTableView, dataclass):
        for column_index, type_ in enumerate(get_fields_types(dataclass)):

            if type_ is bool or bool in get_args(type_):
                table.setItemDelegateForColumn(column_index, self._bool)

            if type_ is date or date in get_args(type_):
                table.setItemDelegateForColumn(column_index, self._date)

            if type_ is Currency or Currency in get_args(type_):
                table.setItemDelegateForColumn(column_index, self._currency)
