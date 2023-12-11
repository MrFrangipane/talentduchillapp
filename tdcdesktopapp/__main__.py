import locale
import logging
import sys

from PySide6.QtWidgets import QApplication

from tdcdesktopapp.core import configuration
from tdcdesktopapp.core.configuration.loader.argparse import ArgparseConfigurationLoader
from tdcdesktopapp.components.main_window_factory import MainWindowFactory
from tdcdesktopapp.components.authentication.api import authenticate


if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, '')
    logging.basicConfig(level=logging.INFO)
    _logger = logging.getLogger(__file__)

    configuration.load_and_apply(loader=ArgparseConfigurationLoader())

    application = QApplication()

    if not authenticate():
        _logger.warning("Login was not successful")
        sys.exit(0)

    main_window = MainWindowFactory.create()
    main_window.show()

    sys.exit(application.exec())
