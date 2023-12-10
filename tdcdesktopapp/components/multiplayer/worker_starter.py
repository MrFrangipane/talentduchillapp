from PySide6.QtCore import QObject, Qt, QThread, Signal
from PySide6.QtWidgets import QApplication

from tdcdesktopapp.components.multiplayer.worker import MultiplayerWorker


class MultiplayerWorkerStarter(QObject):  # FIXME: find a better name
    _start_thread = Signal()

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self.worker = MultiplayerWorker()
        self._thread = QThread()

    def _setup_threading(self):
        # Direct signal connection before moveToThread to ensure execution from main thread
        QApplication.instance().aboutToQuit.connect(self.worker.stop, Qt.DirectConnection)

        # Auto signal connection
        self.worker.moveToThread(self._thread)
        self._thread.finished.connect(self.worker.deleteLater)
        self._start_thread.connect(self.worker.start)
        QApplication.instance().aboutToQuit.connect(self.stop)

    def start(self):
        self._setup_threading()
        self._thread.start()
        self._start_thread.emit()

    def stop(self):
        if self._thread.isRunning():
            self._thread.quit()
            self._thread.wait()
