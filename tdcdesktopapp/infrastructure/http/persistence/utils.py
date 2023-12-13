# FIXME : dont name things "utils"
from contextlib import contextmanager

from tdc_api_client import Configuration, ApiClient
from tdc_api_client.exceptions import ForbiddenException

from tdcdesktopapp.components import persistence
from tdcdesktopapp.core.exceptions import PersistenceException
from tdcdesktopapp.infrastructure.http.auth0.get_token import get_token


@contextmanager
def make_client() -> ApiClient:
    try:
        host = f"http://{persistence.get_parameter('api_host')}"
        configuration = Configuration(host=host, access_token=get_token())
        yield ApiClient(configuration)

    except ForbiddenException as error:
        raise PersistenceException(str(error))
