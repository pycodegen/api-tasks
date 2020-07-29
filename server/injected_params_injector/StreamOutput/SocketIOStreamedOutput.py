from typing import (
    Generic,
    TypedDict,
)

import socketio

from .base import (
    BaseStreamOutput,
    OUTPUT_TYPE,
)

class SocketIOStreamedOutput(
    BaseStreamOutput[OUTPUT_TYPE],
    Generic[OUTPUT_TYPE],
):
    def __init__(self,
                 task_id: str,
                 param_name: str,
                 sio: socketio.AsyncServer,
    ):
        self.task_id = task_id
        self.param_name = param_name
        self.sio = sio

    async def push(self, item: OUTPUT_TYPE) -> None:
        await self.sio.emit(
            event='STREAM_OUTPUT',
            data={

            },
            to=
        )
