from PySide6.QtCore import QObject, Signal, QThread


class MultiplayerQSignalsHolder(QObject):
    projectsReloadRequested = Signal()
