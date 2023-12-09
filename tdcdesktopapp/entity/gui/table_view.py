from PySide6.QtWidgets import QTableView

from tdcdesktopapp.entity.abstract_api import AbstractEntityApi
from tdcdesktopapp.python_extensions.pyside.delegates import Delegates


class EntityTableView(QTableView):
    """
    Boilerplate around QTableView to ensure readability and proper ItemDelegates
    """
    def __init__(self, api: AbstractEntityApi, parent=None):
        QTableView.__init__(self, parent)

        self.setAlternatingRowColors(True)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.setSelectionMode(QTableView.SingleSelection)

        self._delegates = Delegates()
        self._delegates.apply_to_columns_from_dataclass(self, api.entity_type())
