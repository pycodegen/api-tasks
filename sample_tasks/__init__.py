from typing import List

from dataclasses import dataclass
from time import sleep

from task_definitions.TaskContext import TaskContext, RemoteFile


def sleep_task(
        task_context: TaskContext[None],
        a: int,
) -> int:
    sleep(5)
    return a


@dataclass
class SomeClass:
    some_float: List[float]


def some_complicated_task(
        task_context: TaskContext,
        some_cls: SomeClass,
) -> SomeClass:
    print(some_cls.some_float)
    return some_cls


async def some_task_with_file(
        task_context: TaskContext,
        file1: RemoteFile,
):
    f = await task_context.recv_file(file1)
