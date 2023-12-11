from copy import deepcopy
import logging
from typing import Callable

from PySide6.QtCore import QUrl, QObject, Signal
from PySide6.QtWebSockets import QWebSocket

from tdcdesktopapp.components.multiplayer.message_provider.abstract import AbstractMultiplayerMessageProvider
from tdcdesktopapp.components.authentication import api as authentication_api


_logger = logging.getLogger(__name__)


class _WebSocket(QObject):
    """Ensure thread safety communications with QWebSocket instance"""
    _opened = Signal()

    def __init__(self, url: str, message_callback: Callable, parent=None):
        QObject.__init__(self, parent)
        self._url = url
        self.token = ""
        self._is_message_first = True
        self._should_reconnect = False
        self._message_callback = message_callback

        self._web_socket = QWebSocket()
        self._web_socket.connected.connect(self._ws_connected)
        self._web_socket.disconnected.connect(self._ws_disconnected)

        self._opened.connect(self._on_opened)

    def _message_received(self, message):
        if self._is_message_first:
            self._is_message_first = False
            if message == "Authentication OK":

                _logger.info(message)
            else:
                _logger.warning(message)
        else:
            self._message_callback(message)

    def open(self):
        self._opened.emit()

    def _on_opened(self):
        _logger.info("Connecting...")
        self._web_socket.open(QUrl(self._url))

    def _ws_connected(self):
        _logger.info("Connected, authenticating...")
        self._web_socket.sendTextMessage(self.token)
        self._web_socket.textMessageReceived.connect(self._message_received)

    def _ws_disconnected(self):
        _logger.info("Disconnected")
        if self._should_reconnect:
            self._on_opened()


class WebSocketMultiplayerMessageProvider(AbstractMultiplayerMessageProvider):
    """Implemenation of AbstractMultiplayerClient for WebSocket"""
    def __init__(self):
        AbstractMultiplayerMessageProvider.__init__(self)
        self._messages = list()
        self._web_socket = _WebSocket(
            url="ws://127.0.0.1:8000/multiplayer/",
            message_callback=self._ws_message_received
        )

    def begin(self):
        """Creates and Opens WebSocket"""
        self._web_socket.token = authentication_api.get_token()
        self._web_socket.open()

    def get_messages(self):
        """Returns received messages and empties internal queue/cache"""
        messages = deepcopy(self._messages)
        self._messages = list()
        return messages

    def _ws_message_received(self, message):
        """When a message is received"""
        self._messages.append(message)
