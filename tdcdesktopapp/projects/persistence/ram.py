from datetime import date

from tdcdesktopapp.projects.persistence.abstract import AbstractProjectsPersistence
from tdcdesktopapp.projects.model import Project


class RamProjectsPersistence(AbstractProjectsPersistence):

    def get_all(self):
        return [
            Project(id="UUID", name="Frais Généraux"),
            Project(id="UUID", name="Canal 211 #1")
        ]
