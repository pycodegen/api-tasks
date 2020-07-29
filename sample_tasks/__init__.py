from typing import List

from dataclasses import dataclass
from time import sleep

from task_definitions.RemoteFile import RemoteFile
from task_definitions.TaskDefinitions import TaskDefinitionsGroup


def sleep_task(
        a: int,
) -> int:
    sleep(5)
    return a


@dataclass
class SomeClass:
    some_float: List[float]


def some_complicated_task(
        some_cls: SomeClass,
) -> SomeClass:
    print(some_cls.some_float)
    return some_cls


async def some_task_with_file(
        file1: RemoteFile,
):
    f = await file1.recv()


task_definitions = TaskDefinitionsGroup()
task_definitions.add_task(sleep_task)
task_definitions.add_task(some_complicated_task)
task_definitions.add_task(some_task_with_file)
