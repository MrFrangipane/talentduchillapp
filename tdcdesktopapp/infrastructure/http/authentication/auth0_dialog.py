from PySide6.QtCore import QTimer
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QLabel, QDialog, QGridLayout

from tdcdesktopapp.infrastructure.http.authentication.auth0_api import Auth0API


class Auth0Dialog(QDialog):

    def __init__(self, auth0_api: Auth0API, parent=None):
        QDialog.__init__(self, parent)

        self._auth0_api = auth0_api

        self._label_code = QLabel()
        self._web_view = QWebEngineView()

        layout = QGridLayout(self)
        layout.addWidget(self._label_code)
        layout.addWidget(self._web_view)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setRowStretch(1, 100)

        self._polling_timer = QTimer()
        self._polling_timer.timeout.connect(self._poll_for_authentication)

        self.setStyleSheet("""
            background-color: red;
            color: white;
            font-size: 12pt;
            padding: 0.5em;
        """)
        self.setFixedSize(470, 650)
        self.setWindowTitle("Authentication")

    def showEvent(self, event):
        QDialog.showEvent(self, event)
        self._begin_authentication()

    def _begin_authentication(self):
        self._auth0_api.get_device_code()
        self._label_code.setText(f"Confirmation code below must be {self._auth0_api.device_code}")
        self._web_view.load(self._auth0_api.verification_uri)
        self._polling_timer.start(self._auth0_api.polling_interval * 1000)

    def _poll_for_authentication(self):
        try:
            if self._auth0_api.check_authenticated():
                self._polling_timer.stop()
                self.accept()

        except PermissionError:
            self._polling_timer.stop()
            self.reject()
