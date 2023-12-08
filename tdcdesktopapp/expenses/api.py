from tdcdesktopapp.configuration.singleton import ConfigurationSingleton


def get_all():
    return ConfigurationSingleton().expense_persistence.get_all()
