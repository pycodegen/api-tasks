from dataclasses import dataclass

import socketio

# asyncio
sio = socketio.AsyncClient()


@dataclass
class SocketIOClient:
    def add_task(task_fn):
        ...


from typing import TypeVar, Sequence, Callable


TaskGeneric = TypeVar('TaskGeneric')


def create_client_task_func(task_func: TaskGeneric):
    return task_func


def some_func(a: int) -> int:
    return 3


test = create_client_task_func(some_func)


test(5)