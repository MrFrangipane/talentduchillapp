from dataclasses import dataclass

from tdcdesktopapp.python_extensions.singleton_metaclass import SingletonMetaclass


@dataclass
class ConfigurationSingleton(metaclass=SingletonMetaclass):
    """Singleton holding application classes and info that have been configured at startup"""
    show_css_editor: bool = None
