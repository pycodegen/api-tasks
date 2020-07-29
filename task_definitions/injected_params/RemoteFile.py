import abc
from typing import TypeVar

from task_definitions.injected_params.BaseInjectedParam import BaseInjectedParam


class ReceivedFile:
    pass


class RemoteFile(BaseInjectedParam, metaclass=abc.ABCMeta):
    def __init__(
            self,
            param_name: str,
            task_id: str,
            # TODO: file-type, file-name, etc.
    ):
        self.param_name = param_name
        self.task_id = task_id

    async def recv(self, store_path: str) -> ReceivedFile:
        pass


# https://mypy.readthedocs.io/en/stable/kinds_of_types.html#the-type-of-class-objects
RemoteFileTypeVar = TypeVar('RemoteFileTypeVar', bound=RemoteFile)

