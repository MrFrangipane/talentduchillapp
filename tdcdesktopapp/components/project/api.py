from typing import List, Type

from tdcdesktopapp.core.configuration.singleton import ConfigurationSingleton
from tdcdesktopapp.core.entity.abstract_api import AbstractEntityApi
from tdcdesktopapp.components.project.model import Project


class ProjectsApi(AbstractEntityApi):
    def entity_type(self) -> Type[Project]:
        return Project

    def get(self, options: None = None) -> List[Project]:
        return ConfigurationSingleton().persistence_project.get()

    def new(self, options: None = None) -> Project:
        return ConfigurationSingleton().persistence_project.new()

    def update(self, entity: Project) -> None:
        return ConfigurationSingleton().persistence_project.update(entity)

    def remove(self, entity: Project) -> None:
        return ConfigurationSingleton().persistence_project.remove(entity)
