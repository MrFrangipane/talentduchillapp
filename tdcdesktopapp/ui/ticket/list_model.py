import dataclasses

from PySide6.QtCore import Qt, QAbstractTableModel

from tdcdesktopapp.api.ticket import TicketAPI, Ticket


class TicketListModel(QAbstractTableModel):

    def __init__(self, parent=None):
        QAbstractTableModel.__init__(self, parent)

    def rowCount(self, parent=None):
        return TicketAPI.count()

    def columnCount(self, parent=None):
        return len(dataclasses.fields(Ticket))

    def headerData(self, section, orientation=Qt.Orientation.Horizontal, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return [field.name.capitalize() for field in dataclasses.fields(Ticket)][section]

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            ticket = TicketAPI.ticket_by_index(index.row())
            attribute_name = dataclasses.fields(Ticket)[index.column()].name
            return getattr(ticket, attribute_name)
