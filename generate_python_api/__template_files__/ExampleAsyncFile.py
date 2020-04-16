from asyncio import sleep
from asyncio.futures import Future
from typing import TypeVar, Generic, Callable, Any, cast

from dataclasses import dataclass
from py_codegen.type_extractor.type_extractor import TypeExtractor

from generate_python_api.BaseConverter import task_id_type
from generate_python_api.converter import PythonTaskConverter
from py_client.BasePyClient import BasePyClient


stream_output_type = TypeVar('stream_output_type')


# RxPy's Subscriber (push_value) + Observable (subscribe)
class Stream(Generic[stream_output_type]):
    def push_value(self, value: stream_output_type):
        pass

    def subscribe(self, callback: Callable[[stream_output_type], Any]):
        pass


async def some_streaming_task(a: int, stream_output: Stream[int]) -> None:
    for i in range(0, a):
        await sleep(5)
        stream_output.push_value(i)
    return

type_extractor = TypeExtractor()

# PythonTaskConverter knows about 'Stream' type
python_client_codegen = PythonTaskConverter(extractor=type_extractor)
python_client_codegen.get_generated_source()


# Example of generated client code
@dataclass
class TaskClient:
    client_impl: BasePyClient  # implementation-agnostic

    async def some_streaming_task(
            self,
            a: int,
            # note: stream implicitly-removed...
    ) -> (Stream[int], Future[int], task_id_type):

        (task_progress_stream, task_done_future, task_id) = self.client_impl.send_progressive_task(
            'sleep_task',
            args={
                'a': a,
            }
        )
        return (
            cast(Stream[int], task_progress_stream),
            cast(Future[int], task_done_future),
            task_id,
        )

# so it's actually an 'sdk':
# usage:

# usl_api = TaskClient(
#     client_impl=SocketIOClient
# )
#
# (task_progress, task_done_future, task_id) = usl_api.some_streaming_task(10)
