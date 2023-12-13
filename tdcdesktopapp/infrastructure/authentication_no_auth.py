from pyside6helpers.message_box import warning_box

from tdcdesktopapp.components.authentication.abstract import AbstractSecurityLogin


class NoAuthSecurityLogin(AbstractSecurityLogin):

    def exec(self):
        warning_box([
            "No Authentication will be performed.",
            "Don't use --no-auth with API in production !"
        ])
        return True
