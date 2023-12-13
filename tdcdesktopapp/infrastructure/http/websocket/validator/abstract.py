from PySide6.QtCore import QObject
from PySide6.QtWebSockets import QWebSocket


class AbstractWebSocketValidator(QObject):  # FIXME: use ABC, use signal for async validation

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self.is_validated = False

    def validate(self, websocket: QWebSocket):
        """Performs WebSocket authentication and returns True if successful, False otherwise."""
        raise NotImplementedError
