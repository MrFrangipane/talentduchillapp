from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout

from pyside6helpers import css

from tdcdesktopapp import configuration
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
            css.load_onto(main_window)

        main_window.setWindowTitle("TDC App")
        main_window.resize(1000, 700)

        return main_window
