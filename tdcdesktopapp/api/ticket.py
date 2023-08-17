from dataclasses import dataclass


@dataclass
class Ticket:
    index: int
    price: float
    holder: str


class TicketAPI:

    @staticmethod
    def count():
        return 5

    @staticmethod
    def ticket_by_index(index):
        return Ticket(index=index, price=90, holder='None')
