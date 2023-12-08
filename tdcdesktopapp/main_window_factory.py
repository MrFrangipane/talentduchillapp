from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout

from tdcdesktopapp import configuration
from tdcdesktopapp.python_extensions import make_resource_path
from tdcdesktopapp.expenses.gui.widget import ExpensesWidget


def _make_central_wdiget(widget: QWidget):
    central_widget = QWidget()
    central_layout = QGridLayout(central_widget)
    central_layout.addWidget(widget)
    return central_widget


class MainWindowFactory:
    _css_editor = None  # avoid garbage collection

    @staticmethod
    def create() -> QMainWindow:

        main_window = QMainWindow()
        main_window.setCentralWidget(_make_central_wdiget(ExpensesWidget()))

        if configuration.show_css_editor():
            from pyside6helpers.css.editor import CSSEditor
            MainWindowFactory._css_editor = CSSEditor("Frangitron", main_window)
        else:
            with open(make_resource_path("ui/style.qss"), "r") as file_stylesheet:
                main_window.setStyleSheet(file_stylesheet.read())

        main_window.setWindowTitle("TDC App")
        main_window.resize(800, 600)

        return main_window
