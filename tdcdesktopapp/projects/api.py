from typing import List, Type

from tdcdesktopapp.configuration.singleton import ConfigurationSingleton
from tdcdesktopapp.entity.abstract_api import AbstractEntityApi
from tdcdesktopapp.projects.model import Project


class ProjectsApi(AbstractEntityApi):
    def entity_type(self) -> Type[Project]:
        return Project

    def get(self, options: None = None) -> List[Project]:
        return ConfigurationSingleton().project_persistence.get_all()

    def new(self, options: None = None) -> Project:
        return ConfigurationSingleton().project_persistence.new()

    def update(self, entity: Project) -> None:
        return ConfigurationSingleton().project_persistence.update(entity)

    def remove(self, entity: Project) -> None:
        return ConfigurationSingleton().project_persistence.remove(entity)
