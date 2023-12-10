from PySide6.QtCore import QObject, QThread, Signal

from tdcdesktopapp.core.configuration.singleton import ConfigurationSingleton


class MultiplayerWorker(QObject):
    projectsReloadRequested = Signal()

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self._is_running = False

    def start(self):
        self._is_running = True
        self.run()

    def run(self):
        ConfigurationSingleton().multiplayer_client.begin()
        while self._is_running:
            self._process_messages()
            QThread.currentThread().msleep(10)

    def stop(self):
        self._is_running = False

    def _process_messages(self):
        messages = ConfigurationSingleton().multiplayer_client.get_messages()
        for message in messages:
            if message == "projects_reload":
                self.projectsReloadRequested.emit()
