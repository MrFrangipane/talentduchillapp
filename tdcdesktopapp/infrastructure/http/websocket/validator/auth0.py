import logging

from PySide6.QtWebSockets import QWebSocket

from tdcdesktopapp.infrastructure.http.websocket.validator.abstract import AbstractWebSocketValidator
from tdcdesktopapp.infrastructure.http.auth0.get_token import get_token


_logger = logging.getLogger(__name__)


class Auth0WebSocketValidator(AbstractWebSocketValidator):

    def __init__(self, parent=None):
        AbstractWebSocketValidator.__init__(self, parent)
        self._websocket: QWebSocket = None
        self.is_validated = False

    def validate(self, websocket: QWebSocket):
        _logger.info("Connected, authenticating...")
        self._websocket = websocket

        self._websocket.textMessageReceived.connect(self._ws_message)
        self._websocket.sendTextMessage(get_token())

    def _ws_message(self, message: str):
        _logger.info(f"Authentication response: {message}")
        self.is_validated = message == "Authentication OK"
        self._websocket.textMessageReceived.disconnect(self._ws_message)
