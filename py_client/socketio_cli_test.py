import asyncio
import json
from dataclasses import asdict

import socketio

from task_definitions.TaskDefinitions import TaskCall

sio = socketio.AsyncClient()


@sio.on('rpc_done')
async def on_done(data):
    print('task done: ', data)


@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error():
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")


async def start():
    await sio.connect('http://127.0.0.1:30001')
    print('1')
    task_call = TaskCall(
        func_name='long_running_task',
        args=[],
        kwargs={
            'time': 1,
            'val': 2,
        }
    )
    await sio.emit('rpc_call', asdict(task_call))
    await sio.wait()


loop = asyncio.get_event_loop()
loop.run_until_complete(start())