from copy import deepcopy
from typing import List

from tdcdesktopapp.components.project.model import Project
from tdcdesktopapp.core.abstract_persistence import AbstractPersistence
from tdcdesktopapp.core.entity.base_api_options import BaseApiOptions


class RamProjectsPersistence(AbstractPersistence):

    def __init__(self):
        self._multiplayer_messages = list()  # Specific to RAM implementation of Multiplayer Client

        self._projects = {
            "01": Project(id="01", name="Frais Généraux"),
            "02": Project(id="02", name="La Rentrée des Crasses"),
            "03": Project(id="03", name="Canal 211 #1")
        }

    def get(self, options: BaseApiOptions | None = None) -> list[Project]:
        return list(self._projects.values())

    def new(self, options: BaseApiOptions | None = None) -> Project:
        new_index = max([int(index) for index in self._projects.keys()]) + 1
        new_project = Project(
            id=f"{new_index:02d}",
            name="New Project"
        )
        self._projects[new_project.id] = new_project

        self._multiplayer_messages.append("projects_reload")

        return new_project

    def update(self, entity: Project) -> None:
        self._projects[entity.id] = entity

    def remove(self, entity: Project) -> None:
        self._projects.pop(entity.id)

    def get_multiplayer_messages(self) -> List[str]:
        """Specific to RAM implementation of Multiplayer Client"""
        messages = deepcopy(self._multiplayer_messages)
        self._multiplayer_messages = list()
        return messages
