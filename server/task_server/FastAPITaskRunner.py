import asyncio
from asyncio import AbstractEventLoop
from concurrent.futures.thread import ThreadPoolExecutor

from dataclasses import field
from fastapi import FastAPI

from task_definitions.TaskDefinitions import TaskDefinitionsGroup, TaskCall


class FastAPITaskRunner:
    task_definitions: TaskDefinitionsGroup

    def __init__(
            self,
            app: FastAPI,
    ):
        self.app = app
        self.pool: ThreadPoolExecutor = field(default_factory=lambda: ThreadPoolExecutor(max_workers=5))
        self.loop: AbstractEventLoop = field(default_factory=lambda: asyncio.get_event_loop())

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
