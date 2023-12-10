from PySide6.QtWidgets import QTableView

from tdcdesktopapp.core.entity.abstract_api import AbstractEntityApi
from tdcdesktopapp.pyside_extensions.delegates_appointer import DelegatesAppointer


class EntityTableView(QTableView):
    """
    Boilerplate around QTableView to ensure readability and proper ItemDelegates
    """
    def __init__(self, api: AbstractEntityApi, parent=None):
        QTableView.__init__(self, parent)

        self.setAlternatingRowColors(True)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.setSelectionMode(QTableView.SingleSelection)

        self._delegates = DelegatesAppointer()
        self._delegates.appoint_to_columns_from_dataclass(self, api.entity_type())
