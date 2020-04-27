from typing import (
    TypeVar, Generic,
)

ProgressType = TypeVar('ProgressType')

# abstract
class TaskContext(
    Generic[
        ProgressType,
    ],
):
    def send_progress(self, progress_val: ProgressType):
        pass

    def recv_file(self, ):




# example

async def some_task(task_context: TaskContext[int], remote_file: RemoteFile):
    f = await remote_file.recv(task_context)


# executor

some_task(socketio_task_context)
