import abc
from typing import (
    TypeVar, Generic,
)

from task_definitions.RemoteFile import RemoteFile

ProgressType = TypeVar('ProgressType')


class TaskContext(
    Generic[
        ProgressType
    ]
):
    def send_progress(self, progress_val: ProgressType):
        pass

    # @abc.abstractmethod
    async def recv_file(
            self,
            remote_file: RemoteFile,
    ):
        remote_file.param_name
        pass


async def some_task(
        task_context: TaskContext[int],
        remote_file_a: RemoteFile,  # remote_file_a.name = 'remote_file_a' given automatically
):
    f = await task_context.recv_file(remote_file_a)
    # f = await remote_file_a.recv(task_context)


# executor

# some_task(socketio_task_context)
