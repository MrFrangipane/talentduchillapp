from typing import List, Type
from dataclasses import dataclass

from tdcdesktopapp.configuration.singleton import ConfigurationSingleton
from tdcdesktopapp.entity.abstract_api import AbstractEntityApi, BaseApiOptions
from tdcdesktopapp.projects.model import Project


@dataclass
class GetProjectsOptions(BaseApiOptions):
    pass


@dataclass
class NewProjectOptions(BaseApiOptions):
    pass


class ProjectsApi(AbstractEntityApi):
    def entity_type(self) -> Type[Project]:
        return Project

    def get(self, options: GetProjectsOptions = GetProjectsOptions()) -> List[Project]:
        return ConfigurationSingleton().project_persistence.get_all()

    def new(self, options: NewProjectOptions = NewProjectOptions()) -> Project:
        return ConfigurationSingleton().project_persistence.new()

    def update(self, entity: Project) -> None:
        return ConfigurationSingleton().project_persistence.update(entity)

    def remove(self, entity: Project) -> None:
        return ConfigurationSingleton().project_persistence.remove(entity)
