from typing import get_type_hints


class HiddenAttribute:
    """Used with `typing.Annotated` to inform GUI that a member should not be displayed"""
    pass


class Currency(float):
    """Helps delegates to represent Currency correctly"""
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
