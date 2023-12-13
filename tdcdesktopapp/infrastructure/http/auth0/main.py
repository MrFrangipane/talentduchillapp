import json
import logging
from typing import Any

from pyside6helpers.message_box import critical_box

from tdcdesktopapp.components import persistence
from tdcdesktopapp.components.authentication.abstract import AbstractSecurityLogin
from tdcdesktopapp.infrastructure.http.auth0.auth_api import AuthAPI
from tdcdesktopapp.infrastructure.http.auth0.auth_dialog import AuthDialog
from tdcdesktopapp.infrastructure.http.websocket.validator.abstract import AbstractWebSocketValidator


_logger = logging.getLogger(__name__)


class HttpSecurityLogin(AbstractSecurityLogin):

    def __init__(self, configuration: Any):
        AbstractSecurityLogin.__init__(self, configuration)
        self._validator: AbstractWebSocketValidator = None
        self._waiting_for_response = False
        self._is_authenticated = False
        self.token: str = ""

    def exec(self):
        if not persistence.is_available():
            critical_box([
                f"Unable to reach {persistence.get_parameter('api_host')}.",
                "Closing application..."
            ])
            return False

        auth0_config_filepath = self.configuration
        with open(auth0_config_filepath, 'r') as auth0_config_file:
            auth0_payload = json.load(auth0_config_file)

        auth_api = AuthAPI(**auth0_payload)

        dialog = AuthDialog(auth_api)
        dialog.exec()

        if auth_api.current_user:
            self.token = auth_api.access_token
            return True

        return False
