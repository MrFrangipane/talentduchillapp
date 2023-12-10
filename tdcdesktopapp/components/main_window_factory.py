from PySide6.QtWidgets import QMainWindow

from pyside6helpers import css, widget

from tdcdesktopapp.core import configuration
from tdcdesktopapp.components.central_widget import CentralWidget


class MainWindowFactory:
    _css_editor = None  # avoid garbage collection

    @staticmethod
    def create() -> QMainWindow:

        main_window = QMainWindow()
        main_window.setCentralWidget(widget.wrap(CentralWidget()))

        if configuration.show_css_editor():
            from pyside6helpers.css.editor import CSSEditor
            MainWindowFactory._css_editor = CSSEditor("Frangitron", main_window)
        else:
            css.load_onto(main_window)

        main_window.setWindowTitle("TDC App")
        main_window.resize(1000, 700)

        return main_window
