from copy import deepcopy
import logging
from typing import Callable

from PySide6.QtCore import QUrl, QObject, Signal
from PySide6.QtWebSockets import QWebSocket

from tdcdesktopapp.components.multiplayer.client.abstract import AbstractMultiplayerClient


_logger = logging.getLogger(__name__)


class _WebSocket(QObject):
    """Ensure thread safety communications with QWebSocket instance"""
    _opened = Signal()

    def __init__(self, message_callback: Callable, parent=None):
        QObject.__init__(self, parent)
        self._message_callback = message_callback

        self._web_socket = QWebSocket()
        self._web_socket.disconnected.connect(self._ws_disconnected)
        self._web_socket.connected.connect(self._ws_connected)

        self._opened.connect(self._open)

    def open(self):
        self._opened.emit()

    def _open(self):
        self._web_socket.open(QUrl("ws://127.0.0.1:8000/projects/ws"))

    def _ws_connected(self):
        self._web_socket.textMessageReceived.connect(self._message_callback)
        _logger.info("connected")

    def _ws_disconnected(self):
        _logger.info("disconnected, reconnecting")
        self._open()


class WebSocketMultiplayerClient(AbstractMultiplayerClient):
    """Implemenation of AbstractMultiplayerClient for WebSocket"""
    def __init__(self):
        AbstractMultiplayerClient.__init__(self)
        self._messages = list()
        self._web_socket = _WebSocket(message_callback=self._ws_message)

    def begin(self):
        """Opens WebSocket"""
        self._web_socket.open()

    def get_messages(self):
        """Returns received messages and empties internal queue/cache"""
        messages = deepcopy(self._messages)
        self._messages = list()
        return messages

    def _ws_message(self, message):
        """When a message is received"""
        self._messages.append(message)
