import abc
from typing import TypeVar


class BaseInjectedParam(metaclass=abc.ABCMeta):
    pass


# https://mypy.readthedocs.io/en/stable/kinds_of_types.html#the-type-of-class-objects
RemoteFileTypeVar = TypeVar('RemoteFileTypeVar', bound=BaseInjectedParam)