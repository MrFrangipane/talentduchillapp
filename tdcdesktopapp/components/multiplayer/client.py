from tdcdesktopapp.python_extensions.singleton_metaclass import SingletonMetaclass
from tdcdesktopapp.components.multiplayer.qsignals_holder import MultiplayerQSignalsHolder
from tdcdesktopapp.components.multiplayer.worker_starter import MultiplayerWorkerStarter


class MultiplayerClient(metaclass=SingletonMetaclass):  # FIXME find a better name
    """Singleton used to connect components to multiplayer events"""

    def __init__(self):
        self.signals = MultiplayerQSignalsHolder()
        self._worker_starter = MultiplayerWorkerStarter()
        self._connect_signals()

    def _connect_signals(self):
        self._worker_starter.worker.projectsReloadRequested.connect(self.signals.projectsReloadRequested)

    def start(self):
        self._worker_starter.start()
