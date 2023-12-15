from tdcdesktopapp.core.configuration.singleton import ConfigurationSingleton


def get_token() -> str:
    return ConfigurationSingleton().security_login.token  # exists because infrastructure is http
