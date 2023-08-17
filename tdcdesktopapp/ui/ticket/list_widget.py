from PySide6.QtWidgets import QWidget, QGridLayout, QTableView

from tdcdesktopapp.ui.ticket.list_model import TicketListModel


class TicketListWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self._table_model = TicketListModel()
        self._table_view = QTableView()
        self._table_view.setModel(self._table_model)

        layout = QGridLayout(self)
        layout.addWidget(self._table_view)
