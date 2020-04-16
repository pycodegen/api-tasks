import asyncio
from asyncio.futures import Future
from typing import Dict

import socketio

from py_client.BasePyClient import BasePyClient


class SocketIOClient(BasePyClient):
    sio = socketio.Client()
    futures: Dict[str, Future]
    async def add_task(self):
        future = Future()
        self.futures.get()
        await future


sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')

@sio.event
async def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
async def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:5000')
sio.emit('rpc_call', { 'some_data': 'a' })
