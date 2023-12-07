from tdcdesktopapp.configuration.singleton import ConfigurationSingleton
from tdcdesktopapp.configuration.loader_abstract import AbstractConfigurationLoader


def load_and_apply(loader: AbstractConfigurationLoader) -> None:
    """Applies loaded configuration to `ConfigurationSingleton`"""
    loader.load()
    ConfigurationSingleton().show_css_editor = loader.show_css_editor


def show_css_editor() -> bool:
    """Returns True is CSS editor should be shown"""
    return ConfigurationSingleton().show_css_editor
