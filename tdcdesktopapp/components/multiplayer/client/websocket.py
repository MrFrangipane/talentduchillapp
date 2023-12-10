from copy import deepcopy
from typing import Callable

from PySide6.QtCore import QUrl, QObject, Signal
from PySide6.QtNetwork import QAbstractSocket
from PySide6.QtWebSockets import QWebSocket

from tdcdesktopapp.components.multiplayer.client.abstract import AbstractMultiplayerClient


class _WebSocket(QObject):
    """Ensure thread safety communications with QWebSocket instance"""
    _opened = Signal()

    def __init__(self, message_callback: Callable, parent=None):
        QObject.__init__(self, parent)
        self._message_callback = message_callback
        self._web_socket = QWebSocket()
        self._opened.connect(self._open_and_connect_signals)

    def open(self):
        self._opened.emit()

    def _open_and_connect_signals(self):
        self._web_socket.open(QUrl("ws://127.0.0.1:8000/projects/ws"))
        self._web_socket.connected.connect(self._ws_connected)

    def _ws_connected(self):
        self._web_socket.textMessageReceived.connect(self._message_callback)
        print(f"{self.__class__.__name__} online: {self._web_socket.state() == QAbstractSocket.ConnectedState}")


class WebSocketMultiplayerClient(AbstractMultiplayerClient):
    """Implemenation of AbstractMultiplayerClient for WebSocket"""
    def __init__(self):
        AbstractMultiplayerClient.__init__(self)
        self._messages = list()
        self._web_socket = _WebSocket(self._ws_message)

    def begin(self):
        self._web_socket.open()

    def get_messages(self):
        messages = deepcopy(self._messages)
        self._messages = list()
        return messages

    def _ws_message(self, message):
        self._messages.append(message)
