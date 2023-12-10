from copy import deepcopy

from PySide6.QtCore import QUrl, QThread
from PySide6.QtNetwork import QAbstractSocket
from PySide6.QtWebSockets import QWebSocket

from tdcdesktopapp.components.multiplayer.client.abstract import AbstractMultiplayerClient


class WebSocketMultiplayerClient(AbstractMultiplayerClient):
    def __init__(self):
        AbstractMultiplayerClient.__init__(self)
        self._web_socket = QWebSocket()
        self._messages = list()

    def begin(self):
        print("websock.begin()", QThread.currentThread())
        self._web_socket.open(QUrl("ws://127.0.0.1:8000/projects/ws"))
        self._web_socket.connected.connect(self._ws_connected)

    def get_messages(self):
        print("websock.get_mess()", QThread.currentThread(), self._web_socket.state())
        messages = deepcopy(self._messages)
        self._messages = list()
        return messages

    def _ws_connected(self):
        self._web_socket.textMessageReceived.connect(self._ws_message)
        print(f"EventsWorker online: {self._web_socket.state() == QAbstractSocket.ConnectedState}")

    def _ws_message(self, message):
        self._messages.append(message)
