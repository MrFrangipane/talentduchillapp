from abc import ABC, abstractmethod

from tdcdesktopapp.core.entity.base_entity import BaseEntity
from tdcdesktopapp.core.entity.base_api_options import BaseApiOptions


class AbstractPersistence(ABC):

    @abstractmethod
    def get(self, options: BaseApiOptions | None = None) -> list[BaseEntity]:
        pass

    @abstractmethod
    def new(self, options: BaseApiOptions | None = None) -> BaseEntity:
        pass

    @abstractmethod
    def update(self, entity: BaseEntity) -> None:
        pass

    @abstractmethod
    def remove(self, entity: BaseEntity) -> None:
        pass
