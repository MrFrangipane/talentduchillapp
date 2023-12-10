from abc import ABC, abstractmethod
from typing import List, Type

from tdcdesktopapp.core.entity.base_entity import BaseEntity
from tdcdesktopapp.core.entity.base_api_options import BaseApiOptions


class AbstractEntityApi(ABC):

    @abstractmethod
    def entity_type(self) -> Type[BaseEntity]:
        """Return a subclass's Type of BaseEntity (Expense, Project, ...)"""
        pass

    @abstractmethod
    def get(self, options: BaseApiOptions | None) -> List[BaseEntity]:
        pass

    @abstractmethod
    def new(self, options: BaseApiOptions | None) -> BaseEntity:
        pass

    @abstractmethod
    def update(self, entity: BaseEntity) -> None:
        pass

    @abstractmethod
    def remove(self, entity: BaseEntity) -> None:
        pass
