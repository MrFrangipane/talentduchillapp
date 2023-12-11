from tdcdesktopapp.components.multiplayer.message_provider.abstract import AbstractMultiplayerMessageProvider
from tdcdesktopapp.core.configuration.singleton import ConfigurationSingleton


class RamMultiplayerMessageProvider(AbstractMultiplayerMessageProvider):

    def begin(self):
        pass

    def get_messages(self):
        return ConfigurationSingleton().project_persistence.get_multiplayer_messages()  # Exists because we are RAM
