import asyncio
import datetime
from asyncio.events import AbstractEventLoop
from concurrent.futures.thread import ThreadPoolExecutor
from time import sleep
from typing import Optional

import engineio
import socketio
from dataclasses import dataclass, field

from task_definitions.TaskDefinitions import TaskDefinitionsGroup, long_running_task, TaskCall


@dataclass
class SocketIOTaskRunner:
    task_definitions: TaskDefinitionsGroup
    # asgi_app: engineio.ASGIApp = engineio.ASGIApp()
    sio: socketio.AsyncServer = field(default_factory=lambda: socketio.AsyncServer(async_mode='asgi'))
    pool: ThreadPoolExecutor = field(default_factory=lambda: ThreadPoolExecutor(max_workers=5))
    loop: AbstractEventLoop = field(default_factory=lambda: asyncio.get_event_loop())

    def __post_init__(self):
        self.app = socketio.ASGIApp(self.sio)
        self.sio.on('rpc_call')(self.handle_rpc_call)

    async def on_taskrun(self, time: int, val: int):
        future = self.loop.run_in_executor(
            self.pool,
            lambda: long_running_task(
                time=time,
                val=val,
            ),
        )
        # just await + send response here ?
        value = await future
        print('done:', time, value)
        return value

    async def handle_rpc_call(self, sid, data):
        print('inside handle_rpc_call', data)
        task_call = TaskCall(
            func_name=data['func_name'],
            args=data['args'],
            kwargs=data['kwargs'],
        )
        future = self.loop.run_in_executor(
            self.pool,
            lambda: self.task_definitions.run_task(
                task_call=task_call,
            )
        )
        val = await future
        self.sio.emit('rpc_done', val)

    # def start(self):

        # socketio = SocketIO(self.flask)
        # @socketio.on('rpc_call')
        # def call_task(message):
        #     print(message)
        # socketio.run(self.flask)

