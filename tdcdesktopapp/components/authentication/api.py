import logging
from tdcdesktopapp.core.configuration.singleton import ConfigurationSingleton


_logger = logging.getLogger(__name__)


def authenticate() -> bool:
    """Performs login action (GUI or not) and returns True if successful, False otherwise."""
    if ConfigurationSingleton().security_login.exec():
        _logger.warning("Authentication was successful")
        return True
    else:
        _logger.warning("Authentication was not successful")
        return False
