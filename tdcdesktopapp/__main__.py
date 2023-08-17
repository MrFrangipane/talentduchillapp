import sys

from PySide6.QtWidgets import QApplication

from tdcdesktopapp.ui.main_window import MainWindow

app = QApplication()

main_window = MainWindow()
main_window.show()

sys.exit(app.exec())
