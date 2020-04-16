# imports go here:
from asyncio.futures import Future
from time import sleep
from typing import NewType

from dataclasses import dataclass
from py_codegen.type_extractor.type_extractor import TypeExtractor

from generate_python_api.BaseConverter import task_id_type
from generate_python_api.converter import PythonTaskConverter
from py_client.BasePyClient import BasePyClient


def sleep_task(a: int) -> int:
    sleep(10)
    return a + 10


type_extractor = TypeExtractor()

python_client_codegen = PythonTaskConverter(extractor=type_extractor)
python_client_codegen.get_generated_source()


# Example of generated client code
@dataclass
class TaskClient:
    client_impl: BasePyClient  # implementation-agnostic

    async def sleep_task(self, a: int) -> (Future[int], task_id_type):
        (task_future, task_id) = self.client_base.send(
            'sleep_task',
            args={
                'a': a,
            }
        )
        return (task_future, task_id)

# so it's actually an 'sdk':
# usage:

# usl_api = TaskClient(
#     client_impl=SocketIOClient
# )
#
# await usl_api.sleep_task(10)