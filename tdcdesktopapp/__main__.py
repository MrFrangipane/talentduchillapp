import logging
import sys

from PySide6.QtWidgets import QApplication

from tdcdesktopapp import configuration
from tdcdesktopapp.configuration.loader.argparse import ArgparseConfigurationLoader
from tdcdesktopapp.main_window_factory import MainWindowFactory


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    configuration.load_and_apply(loader=ArgparseConfigurationLoader())

    application = QApplication()
    main_window = MainWindowFactory.create()
    main_window.show()
    sys.exit(application.exec())
