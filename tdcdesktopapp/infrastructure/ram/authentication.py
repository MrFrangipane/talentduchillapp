from pyside6helpers.message_box import information_box

from tdcdesktopapp.components.authentication.abstract import AbstractSecurityLogin


class RamSecurityLogin(AbstractSecurityLogin):

    def exec(self):
        information_box([
            "This is the Ram version of the application.",
            "Nothing is saved on quit."
        ])
        return True
