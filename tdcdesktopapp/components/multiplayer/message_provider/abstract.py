from abc import (ABC, abstractmethod)


class AbstractMultiplayerMessageProvider(ABC):

    @abstractmethod
    def begin(self):
        pass

    @abstractmethod
    def get_messages(self):
        pass
