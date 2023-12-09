from typing import Annotated
from dataclasses import dataclass
from datetime import date
from uuid import UUID

from tdcdesktopapp.python_extensions.typing import HiddenAttribute, Currency


@dataclass
class Expense:
    """Keep track of expenses, refund, etc"""
    id: Annotated[UUID, HiddenAttribute]
    project: str  # FIXME: use Project model
    caption: str
    amount: Currency
    date_: date
    needs_refund: bool = False
    refunded: bool | None = None
    date_refund: date | None = None
