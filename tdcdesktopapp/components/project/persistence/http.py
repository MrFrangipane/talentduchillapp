"""
Http implementation of Expense Persistence

note: https://stackoverflow.com/questions/2386299/running-sites-on-localhost-is-extremely-slow
"""
from typing import List

import tdc_api_client as client

from tdcdesktopapp.components.project.persistence.abstract import AbstractProjectsPersistence
from tdcdesktopapp.components.project.model import Project


class HttpProjectsPersistence(AbstractProjectsPersistence):

    def get_all(self) -> List[Project]:
        configuration = client.Configuration(host="http://127.0.0.1:8000")
        with client.ApiClient(configuration) as api_client:
            api_instance = client.ProjectsApi(api_client)
            return [Project(**project.to_dict()) for project in api_instance.get_projects_get()]

    def new(self) -> Project:
        configuration = client.Configuration(host="http://127.0.0.1:8000")
        with client.ApiClient(configuration) as api_client:
            api_instance = client.ProjectsApi(api_client)
            new_project = api_instance.new_projects_post()
            return Project(**new_project.to_dict())

    def update(self, project: Project) -> None:
        client_project = client.Project.from_dict(vars(project))

        configuration = client.Configuration(host="http://127.0.0.1:8000")
        with client.ApiClient(configuration) as api_client:
            api_instance = client.ProjectsApi(api_client)
            api_instance.update_projects_put(client_project)

    def remove(self, project: Project) -> None:
        client_project = client.Project.from_dict(vars(project))

        configuration = client.Configuration(host="http://127.0.0.1:8000")
        with client.ApiClient(configuration) as api_client:
            api_instance = client.ProjectsApi(api_client)
            api_instance.remove_projects_delete(client_project)
