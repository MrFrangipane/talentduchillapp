from abc import ABC, abstractmethod
from typing import List

from tdcdesktopapp.projects.model import Project


class AbstractProjectsPersistence(ABC):
    """Loads and saves Projects"""

    @abstractmethod
    def get_all(self) -> List[Project]:
        pass

    @abstractmethod
    def new(self) -> Project:
        pass

    @abstractmethod
    def update(self, project: Project) -> None:
        pass

    @abstractmethod
    def remove(self, project: Project) -> None:
        pass
