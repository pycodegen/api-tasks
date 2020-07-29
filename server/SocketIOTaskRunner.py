import asyncio
from asyncio.events import AbstractEventLoop
from concurrent.futures.thread import ThreadPoolExecutor
from typing import Dict

import socketio
from dataclasses import dataclass, field

from server.injected_params_injector.RemoteFileReceiver.SocketIOFileReceiver import SocketIOFileReceiver
from task_definitions.TaskDefinitions import TaskDefinitionsGroup, TaskCall
from task_definitions.injected_params.RemoteFile import RemoteFile


@dataclass
class SocketIOTaskRunner:
    task_definitions: TaskDefinitionsGroup
    sio: socketio.AsyncServer = field(default_factory=lambda: socketio.AsyncServer(async_mode='asgi'))
    pool: ThreadPoolExecutor = field(default_factory=lambda: ThreadPoolExecutor(max_workers=5))
    loop: AbstractEventLoop = field(default_factory=lambda: asyncio.get_event_loop())

    def __post_init__(self):
        self.app = socketio.ASGIApp(self.sio)
        self.client_socks: Dict[str, ] = dict()
        self.file_receiver = SocketIOFileReceiver(sio=self.sio)
        self.sio.on('rpc_call')(self.handle_rpc_call)

    # def create_remote_file(
    #         self,
    #         param_key: str,
    #         # param_value: Type[RemoteFileTypeVar], # TODO: other RemoteFile type possible?
    # ):
    #     return RemoteFile(
    #         param_name=param_key,
    #     )

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
        await self.sio.emit('rpc_done', val)

