from tdcdesktopapp.extensions.singleton_metaclass import SingletonMetaclass
from tdcdesktopapp.abstract.ticket_storage import AbstractTicketStorage


class Configuration(metaclass=SingletonMetaclass):

    def __init__(self):
        self.ticket_storage: AbstractTicketStorage = None
