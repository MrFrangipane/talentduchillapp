from PySide6.QtWebSockets import QWebSocket

from tdcdesktopapp.infrastructure.http.websocket.validator.abstract import AbstractWebSocketValidator


class NoAuthWebSocketValidator(AbstractWebSocketValidator):

    def validate(self, websocket: QWebSocket):
        self.is_validated = True
