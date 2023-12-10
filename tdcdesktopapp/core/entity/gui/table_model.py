from typing import List

from PySide6.QtCore import Qt, QAbstractTableModel

from tdcdesktopapp.core.entity.base_entity import BaseEntity
from tdcdesktopapp.core.entity.abstract_api import AbstractEntityApi
from tdcdesktopapp.python_extensions.typing import get_fields_names


class EntityTableModel(QAbstractTableModel):
    """
    Displays a collection of entities based upon their fields
    """
    def __init__(self, api: AbstractEntityApi, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._api = api
        self._data: List[BaseEntity] = []
        self._field_names: List[str] = get_fields_names(api.entity_type())
        self._field_names_pretty: List[str] = [
            item.replace("_", " ").capitalize().strip() for item in self._field_names
        ]

    def set_entities(self, entities):
        """Updates internal data and refreshes views"""
        self.beginResetModel()
        self._data = entities
        self.endResetModel()

    def entity_from_row(self, row: int):
        """Returns entity at row"""
        return self._data[row]

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._field_names)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return getattr(self._data[index.row()], self._field_names[index.column()])

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._field_names_pretty[section]

    def flags(self, index):
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable

    def setData(self, index, value, role=Qt.EditRole):
        entity = self._data[index.row()]
        setattr(entity, self._field_names[index.column()], value)
        self._api.update(entity)
        return True
