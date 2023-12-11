from typing import Any
from abc import ABC, abstractmethod


class AbstractSecurityLogin(ABC):

    def __init__(self, configuration: Any):
        self.configuration = configuration
        self.token: str = None

    @abstractmethod
    def exec(self) -> bool:
        """Performs login action (GUI or not) and returns True if successful, False otherwise."""
        pass
