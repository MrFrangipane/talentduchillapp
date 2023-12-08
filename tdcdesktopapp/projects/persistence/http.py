"""
Http implementation of Expense Persistence

note: https://stackoverflow.com/questions/2386299/running-sites-on-localhost-is-extremely-slow
"""
from typing import List

import tdc_api_client as client

from tdcdesktopapp.projects.persistence.abstract import AbstractProjectsPersistence
from tdcdesktopapp.projects.model import Project


class HttpProjectsPersistence(AbstractProjectsPersistence):
    def get_all(self) -> List[Project]:
        configuration = client.Configuration(host="http://127.0.0.1:8000")
        with client.ApiClient(configuration) as api_client:
            api_instance = client.ProjectsApi(api_client)
            return [Project(**project.to_dict()) for project in api_instance.get_projects_get()]
