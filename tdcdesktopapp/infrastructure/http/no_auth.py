from typing import Any

from pyside6helpers.message_box import warning_box

from tdcdesktopapp.components.authentication.abstract import AbstractSecurityLogin


class NoAuthSecurityLogin(AbstractSecurityLogin):

    def __init__(self, configuration: Any):
        AbstractSecurityLogin.__init__(self, configuration)
        self.token = ""

    def exec(self):
        warning_box([
            "No Authentication will be performed.",
            "Don't use --no-auth with API in production !"
        ])
        return True
