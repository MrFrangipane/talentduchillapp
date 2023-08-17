from PySide6.QtWidgets import QMainWindow

from tdcdesktopapp.ui.ticket.list_widget import TicketListWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.setWindowTitle("TDC - Desktop App")
        self.setCentralWidget(TicketListWidget())
        self.resize(800, 600)
