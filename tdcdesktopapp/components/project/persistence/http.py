"""
Http implementation of Expense Persistence

note: https://stackoverflow.com/questions/2386299/running-sites-on-localhost-is-extremely-slow
"""
from typing import List

import tdc_api_client as client
from tdc_api_client.exceptions import ForbiddenException

from tdcdesktopapp.components.project.persistence.abstract import AbstractProjectsPersistence
from tdcdesktopapp.components.project.persistence.exceptions import PersistenceException
from tdcdesktopapp.components.project.model import Project
from tdcdesktopapp.components.authentication.api import get_token


class HttpProjectsPersistence(AbstractProjectsPersistence):

    def get_all(self) -> List[Project]:
        try:
            configuration = client.Configuration(host="http://127.0.0.1:8000", access_token=get_token())
            with client.ApiClient(configuration) as api_client:
                api_instance = client.ProjectsApi(api_client)
                return [Project(**project.to_dict()) for project in api_instance.projects_get()]
        except ForbiddenException as error:
            raise PersistenceException(str(error))

    def new(self) -> Project:
        try:
            configuration = client.Configuration(host="http://127.0.0.1:8000", access_token=get_token())
            with client.ApiClient(configuration) as api_client:
                api_instance = client.ProjectsApi(api_client)
                new_project = api_instance.projects_post()
                return Project(**new_project.to_dict())
        except ForbiddenException as error:
            raise PersistenceException(str(error))

    def update(self, project: Project) -> None:
        try:
            client_project = client.Project.from_dict(vars(project))

            configuration = client.Configuration(host="http://127.0.0.1:8000", access_token=get_token())
            with client.ApiClient(configuration) as api_client:
                api_instance = client.ProjectsApi(api_client)
                api_instance.projects_put(client_project)
        except ForbiddenException as error:
            raise PersistenceException(str(error))

    def remove(self, project: Project) -> None:
        try:
            client_project = client.Project.from_dict(vars(project))

            configuration = client.Configuration(host="http://127.0.0.1:8000", access_token=get_token())
            with client.ApiClient(configuration) as api_client:
                api_instance = client.ProjectsApi(api_client)
                api_instance.projects_delete(client_project)
        except ForbiddenException as error:
            raise PersistenceException(str(error))
