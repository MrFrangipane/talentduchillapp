import json

from tdcdesktopapp.components.authentication.abstract import AbstractSecurityLogin
from tdcdesktopapp.components import persistence
from tdcdesktopapp.infrastructure.http.authentication.auth_api import AuthAPI
from tdcdesktopapp.infrastructure.http.authentication.auth_dialog import AuthDialog


class HttpSecurityLogin(AbstractSecurityLogin):

    def exec(self):
        if not persistence.is_available():
            return False

        with open(self.configuration, 'r') as auth0_file:
            auth0_payload = json.load(auth0_file)

        auth_api = AuthAPI(**auth0_payload)

        dialog = AuthDialog(auth_api)
        dialog.exec()

        if auth_api.current_user:
            self.token = auth_api.access_token
            return True

        return False
