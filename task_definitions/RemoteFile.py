from typing import TypeVar


class RemoteFile:
    def __init__(
            self,
            param_name: str,
            task_id: str,
            file_receiver:

    ):
        self.param_name = param_name

    async def recv(self, store_path: str):
        pass


# https://mypy.readthedocs.io/en/stable/kinds_of_types.html#the-type-of-class-objects
RemoteFileTypeVar = TypeVar('RemoteFileTypeVar', bound=RemoteFile)

