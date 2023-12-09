from typing import get_type_hints


class HiddenAttribute:
    pass


class Currency(float):
    pass


def get_fields_names(dataclass):
    """Returns list of dataclass fields names that are annotated as HiddenAttribute"""
    return [
        name for name, type_ in get_type_hints(dataclass, include_extras=True).items()
        if not hasattr(type_, '__metadata__') or HiddenAttribute not in type_.__metadata__
    ]


def get_fields_types(dataclass):
    """Returns list of dataclass fields types that are annotated as HiddenAttribute"""
    return [
        type_ for name, type_ in get_type_hints(dataclass, include_extras=True).items()
        if not hasattr(type_, '__metadata__') or HiddenAttribute not in type_.__metadata__
    ]
