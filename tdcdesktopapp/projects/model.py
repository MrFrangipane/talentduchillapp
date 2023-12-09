from typing import Annotated
from dataclasses import dataclass
from uuid import UUID

from tdcdesktopapp.python_extensions.typing import HiddenAttribute


@dataclass
class Project:
    """Separates accounting in various projects"""
    id: Annotated[UUID, HiddenAttribute]
    name: str
    description: str = ""

    def __str__(self):
        return self.name
