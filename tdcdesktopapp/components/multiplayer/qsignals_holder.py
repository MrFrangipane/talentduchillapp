from PySide6.QtCore import QObject, Signal


class MultiplayerQSignalsHolder(QObject):
    projectsReloadRequested = Signal()
