# FIXME : dont name things "utils"
from contextlib import contextmanager

from tdc_api_client import Configuration, ApiClient
from tdc_api_client.exceptions import ForbiddenException

from tdcdesktopapp.components import persistence
from tdcdesktopapp.components.authentication.api import get_token
from tdcdesktopapp.core.exceptions import PersistenceException


@contextmanager
def make_client() -> ApiClient:
    try:
        host = f"http://{persistence.get_parameter('api_host')}"
        configuration = Configuration(host=host, access_token=get_token())
        yield ApiClient(configuration)

    except ForbiddenException as error:
        raise PersistenceException(str(error))
