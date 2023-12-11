from copy import deepcopy
from typing import List

from tdcdesktopapp.components.project.model import Project
from tdcdesktopapp.components.project.abstract_persistence import AbstractProjectsPersistence


class RamProjectsPersistence(AbstractProjectsPersistence):

    def __init__(self):
        AbstractProjectsPersistence.__init__(self)

        self._multiplayer_messages = list()  # Specific to RAM implementation of Multiplayer Client

        self._projects = {
            "01": Project(id="01", name="Frais Généraux"),
            "02": Project(id="02", name="La Rentrée des Crasses"),
            "03": Project(id="03", name="Canal 211 #1")
        }

    def get_all(self):
        return list(self._projects.values())

    def new(self) -> Project:
        new_index = max([int(index) for index in self._projects.keys()]) + 1
        new_project = Project(
            id=f"{new_index:02d}",
            name="New Project"
        )
        self._projects[new_project.id] = new_project

        self._multiplayer_messages.append("projects_reload")

        return new_project

    def update(self, project: Project):
        self._projects[project.id] = project

    def remove(self, project: Project):
        self._projects.pop(project.id)

    def get_multiplayer_messages(self) -> List[str]:
        """Specific to RAM implementation of Multiplayer Client"""
        messages = deepcopy(self._multiplayer_messages)
        self._multiplayer_messages = list()
        return messages
