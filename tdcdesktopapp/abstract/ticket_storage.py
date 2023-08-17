from abc import ABC, abstractmethod


class AbstractTicketStorage(ABC):

    @abstractmethod
    def get_all(self) -> [dict]:
        pass

    @abstractmethod
    def get_by_index(self, index) -> dict:
        pass
