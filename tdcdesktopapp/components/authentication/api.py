from tdcdesktopapp.core.configuration.singleton import ConfigurationSingleton


def authenticate() -> bool:
    """Performs login action (GUI or not) and returns True if successful, False otherwise."""
    return ConfigurationSingleton().security_login.exec()
