import logging
import urllib.request

from tdcdesktopapp.core.abstract_persistence_configuration import AbstractPersistenceConfiguration


_logger = logging.getLogger(__name__)


class HttpPersistenceConfiguration(AbstractPersistenceConfiguration):

    def is_available(self) -> bool:
        host = f"http://{self.attributes['api_host']}"
        try:
            if urllib.request.urlopen(host).getcode() != 200:
                _logger.warning(f"Unable to reach http API {host}")
                return False
        except Exception as error:
            _logger.warning(f"Unable to reach http API {error}")
            return False

        return True
