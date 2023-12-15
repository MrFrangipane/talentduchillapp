from abc import (ABC, abstractmethod)


class AbstractMultiplayerMessageProvider(ABC):

    @abstractmethod
    def begin(self) -> None:
        pass

    @abstractmethod
    def get_messages(self) -> list[str]:
        pass
