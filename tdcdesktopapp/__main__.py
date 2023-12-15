import locale
import logging
import sys

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QSplashScreen

from tdcdesktopapp.python_extensions import make_resource_path


if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, '')
    logging.basicConfig(level=logging.INFO)
    _logger = logging.getLogger(__file__)

    application = QApplication()

    splash = QSplashScreen(QPixmap(make_resource_path('splash.png')))
    splash.show()

    #
    # We want loading to happen while splashscreen is shown
    from tdcdesktopapp.core import configuration
    from tdcdesktopapp.components.authentication.api import authenticate
    from tdcdesktopapp.components.main_window_factory import MainWindowFactory
    from tdcdesktopapp.infrastructure.argparse_configuration_loader import ArgparseConfigurationLoader

    configuration.load_and_apply(loader=ArgparseConfigurationLoader())

    if not authenticate():
        sys.exit(0)

    splash.close()

    main_window = MainWindowFactory.create()
    main_window.show()

    sys.exit(application.exec())
