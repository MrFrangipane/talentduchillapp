from abc import ABC, abstractmethod


class AbstractPersistenceConfiguration(ABC):

    def __init__(self):
        self.attributes = dict()

    @abstractmethod
    def is_available(self) -> bool:
        pass
