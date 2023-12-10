import locale
import logging
import sys

from PySide6.QtWidgets import QApplication

from tdcdesktopapp.core import configuration
from tdcdesktopapp.core.configuration.loader.argparse import ArgparseConfigurationLoader
from tdcdesktopapp.components.main_window_factory import MainWindowFactory
from tdcdesktopapp.components.multiplayer.api import Multiplayer


if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, '')
    logging.basicConfig(level=logging.INFO)

    configuration.load_and_apply(loader=ArgparseConfigurationLoader())

    application = QApplication()

    Multiplayer().start()

    main_window = MainWindowFactory.create()
    main_window.show()

    sys.exit(application.exec())
