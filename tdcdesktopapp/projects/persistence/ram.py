from tdcdesktopapp.projects.model import Project
from tdcdesktopapp.projects.persistence.abstract import AbstractProjectsPersistence


class RamProjectsPersistence(AbstractProjectsPersistence):

    def __init__(self):
        AbstractProjectsPersistence.__init__(self)
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
        return new_project

    def update(self, project: Project):
        self._projects[project.id] = project

    def remove(self, project: Project):
        self._projects.pop(project.id)
