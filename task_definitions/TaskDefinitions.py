import abc
from abc import ABC
from datetime import datetime
from time import sleep
from typing import Callable, Dict, List, Awaitable, Any
from dataclasses import dataclass, field
import pathlib


@dataclass
class TaskCall:
    func_name: str
    args: List = field(default_factory=list)
    kwargs: Dict = field(default_factory=dict)


class BaseRemoteFile(metaclass=abc.ABCMeta):
    def __init__(self, file_name: str):
        self.file_name = file_name

    @abc.abstractmethod
    def recv(self) -> Awaitable[pathlib.Path]:
        pass


# might add options?
@dataclass
class Task:
    func: Callable


@dataclass
class TaskDefinitionsGroup:
    tasks: Dict[str, Task] = field(default_factory=dict)

    def add_task(self, task_func: Callable):
        task = Task(
            func=task_func,
        )
        self.tasks.__setitem__(task_func.__qualname__, task)

        def __wrapper_func__(*args, **kwargs):
            result = task_func(*args, **kwargs)
            return result
        return __wrapper_func__

    def run_task(self, task_call: TaskCall):
        task = self.tasks.get(task_call.func_name)
        if not task:
            raise KeyError(f'task not found: {task_call.func_name}')
        task.func(*task_call.args, **task_call.kwargs)


task_definition = TaskDefinitionsGroup()


@task_definition.add_task
def long_running_task(time: int, val: int):
    print(f"long_running_task( time={time}, val={val} started at: {datetime.now()}")
    sleep(time)
    print(f"long_running_task( time={time}, val={val} ended at: {datetime.now()}")
    return val
