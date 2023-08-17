from tdcdesktopapp.abstract.ticket_storage import AbstractTicketStorage


class RAMTicketStorage(AbstractTicketStorage):

    _DATA = [
            {'index': 1, 'price': 90, 'holder': ''},
            {'index': 2, 'price': 90, 'holder': ''},
            {'index': 3, 'price': 90, 'holder': ''},
            {'index': 4, 'price': 60, 'holder': ''},
        ]

    def get_all(self) -> [dict]:
        return self._DATA

    def get_by_index(self, index) -> dict:
        return self._DATA[index]
