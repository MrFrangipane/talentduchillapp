from tdc_api_client import ProjectsApi
from tdc_api_client import Project as ApiProject

from tdcdesktopapp.components.project.model import Project
from tdcdesktopapp.core.abstract_persistence import AbstractPersistence
from tdcdesktopapp.core.entity.base_api_options import BaseApiOptions
from tdcdesktopapp.infrastructure.http.persistence.utils import make_client


class HttpProjectsPersistence(AbstractPersistence):

    def get(self, options: BaseApiOptions = None) -> list[Project]:
        with make_client() as client:
            return [
                Project(**project.to_dict()) for project
                in ProjectsApi(client).projects_get()
            ]

    def new(self, options: BaseApiOptions = None):
        with make_client() as client:
            new_project = ProjectsApi(client).projects_post()
            return Project(**new_project.to_dict())

    def update(self, entity: Project) -> None:
        with make_client() as client:
            ProjectsApi(client).projects_put(ApiProject.from_dict(vars(entity)))

    def remove(self, entity: Project) -> None:
        with make_client() as client:
            ProjectsApi(client).projects_delete(ApiProject.from_dict(vars(entity)))
