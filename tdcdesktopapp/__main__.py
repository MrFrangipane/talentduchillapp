import sys

from PySide6.QtWidgets import QApplication

from tdcdesktopapp.api import configuration
from tdcdesktopapp.ui.main_window import MainWindow


configuration.configure_for_ram()

app = QApplication()

main_window = MainWindow()
main_window.show()

sys.exit(app.exec())
