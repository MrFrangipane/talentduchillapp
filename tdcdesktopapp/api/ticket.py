from dataclasses import dataclass

from tdcdesktopapp.configuration import Configuration


@dataclass
class Ticket:
    index: int
    price: float
    holder: str


class TicketAPI:

    @staticmethod
    def count():
        return len(Configuration().ticket_storage.get_all())

    @staticmethod
    def ticket_by_index(index):
        return Ticket(**Configuration().ticket_storage.get_by_index(index))
