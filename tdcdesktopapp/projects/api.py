from tdcdesktopapp.configuration.singleton import ConfigurationSingleton


def get_all():
    return ConfigurationSingleton().project_persistence.get_all()
