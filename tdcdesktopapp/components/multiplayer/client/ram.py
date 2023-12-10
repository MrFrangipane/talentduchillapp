from tdcdesktopapp.components.multiplayer.client.abstract import AbstractMultiplayerClient
from tdcdesktopapp.core.configuration.singleton import ConfigurationSingleton


class RamMultiplayerClient(AbstractMultiplayerClient):

    def get_messages(self):
        return ConfigurationSingleton().project_persistence.get_multiplayer_messages()  # Exists because we are RAM
