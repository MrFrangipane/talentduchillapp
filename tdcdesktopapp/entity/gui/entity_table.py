from PySide6.QtCore import QObject, Signal

from pyside6helpers import confirmation_dialog

from tdcdesktopapp.entity.abstract_api import AbstractEntityApi
from tdcdesktopapp.entity.base_api_options import BaseApiOptions
from tdcdesktopapp.entity.gui.table_model import EntityTableModel
from tdcdesktopapp.entity.gui.table_view import EntityTableView


class EntityTable(QObject):
    """
    Holds model, view, and controller in order to use a QTableView of a certain Entity (Project, Expense, ...)
    Controller has to be subclassed from AbstractEntityTableController
    """
    dataReloadRequested = Signal()

    def __init__(self, api: AbstractEntityApi, parent=None):
        QObject.__init__(self, parent)

        self.api = api
        self.model = EntityTableModel(api=api)
        self.view = EntityTableView(api=api)
        self.view.setModel(self.model)

    def set_entities(self, entities):
        """
        Updates Model and View with given entities
        Used after data has been retrieved when reloading
        """
        self.model.set_entities(entities)

    def new_entity(self, options: BaseApiOptions):
        """
        Creates a new entity using Controller
        Then requests data reloading
        """
        self.api.new(options)
        self.dataReloadRequested.emit()

    def remove_entity(self):
        """
        Removes selected entities using View and Controller
        Then requests data reloading
        """
        if self.view.selectionModel() is None:
            return

        indices = self.view.selectionModel().selectedRows()
        if not indices:
            return

        for index in indices:
            entity = self.model.entity_from_row(index.row())
            if confirmation_dialog(f"Are you sure you want to delete '{entity}' ?\nYOU CAN'T GO BACK"):
                self.api.remove(entity)

        self.dataReloadRequested.emit()
