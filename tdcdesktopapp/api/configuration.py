from tdcdesktopapp.configuration import Configuration


def configure_for_ram():
    from tdcdesktopapp.implementation.ram_ticket_storage import RAMTicketStorage
    Configuration().ticket_storage = RAMTicketStorage()
