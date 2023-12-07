from PySide6.QtWidgets import QMainWindow, QWidget

from tdcdesktopapp import configuration
from tdcdesktopapp.python_extensions import make_resource_path


class MainWindowFactory:
    _css_editor = None  # avoid garbage collection

    @staticmethod
    def create() -> QMainWindow:

        main_window = QMainWindow()
        main_window.setCentralWidget(QWidget())

        if configuration.show_css_editor():
            from pyside6helpers.css.editor import CSSEditor
            MainWindowFactory._css_editor = CSSEditor("Frangitron", main_window)
        else:
            with open(make_resource_path("ui/style.qss"), "r") as file_stylesheet:
                main_window.setStyleSheet(file_stylesheet.read())

        main_window.setWindowTitle("TDC App")

        return main_window
