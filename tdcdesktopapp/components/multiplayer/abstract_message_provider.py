from abc import (ABC, abstractmethod)
from typing import Any


class AbstractMultiplayerMessageProvider(ABC):

    def __init__(self, configuration: Any):
        self.configuration = configuration

    @abstractmethod
    def begin(self):
        pass

    @abstractmethod
    def get_messages(self):
        pass
