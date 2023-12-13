from copy import deepcopy
import logging
from typing import Any, Callable

from PySide6.QtCore import QUrl, QObject, Signal
from PySide6.QtWebSockets import QWebSocket
from PySide6.QtWidgets import QApplication

from tdcdesktopapp.components import persistence
from tdcdesktopapp.components.multiplayer.abstract_message_provider import AbstractMultiplayerMessageProvider
from tdcdesktopapp.infrastructure.http.websocket.validator.abstract import AbstractWebSocketValidator


_logger = logging.getLogger(__name__)


class _WebSocket(QObject):
    """Ensure thread safety communications with QWebSocket instance"""
    _opened = Signal()

    def __init__(self, message_callback: Callable, validator: AbstractWebSocketValidator, parent=None):
        QObject.__init__(self, parent)
        self.url = ""
        self._validator = validator
        self._is_message_first = True
        self._about_to_quit = False
        self._message_callback = message_callback

        self._web_socket = QWebSocket()
        self._web_socket.connected.connect(self._ws_connected)
        self._web_socket.disconnected.connect(self._ws_disconnected)

        self._opened.connect(self._on_opened)
        QApplication.instance().aboutToQuit.connect(self._ws_about_to_quit)

    def open(self):
        self._opened.emit()

    def _on_opened(self):
        _logger.info("Connecting...")
        self._web_socket.open(QUrl(self.url))

    def _ws_connected(self):
        self._validator.validate(self._web_socket)
        self._web_socket.textMessageReceived.connect(self._message_callback)

    def _ws_disconnected(self):
        _logger.info("Disconnected")
        if self._validator.is_validated and not self._about_to_quit:
            self._on_opened()

    def _ws_about_to_quit(self):
        self._about_to_quit = True


class WebSocketMultiplayerMessageProvider(AbstractMultiplayerMessageProvider):
    """Implemenation of AbstractMultiplayerClient for WebSocket"""
    def __init__(self, configuration: Any):
        AbstractMultiplayerMessageProvider.__init__(self, configuration=configuration)
        websocket_validator = self.configuration
        self._messages = list()
        self._web_socket = _WebSocket(
            message_callback=self._ws_message_received,
            validator=websocket_validator()
        )

        """Creates and Opens WebSocket"""
        self._web_socket.url = f"ws://{persistence.get_parameter('api_host')}/multiplayer/"

    def begin(self):
        self._web_socket.open()

    def get_messages(self):
        """Returns received messages and empties internal queue/cache"""
        messages = deepcopy(self._messages)
        self._messages = list()
        return messages

    def _ws_message_received(self, message):
        """When a message is received"""
        self._messages.append(message)
