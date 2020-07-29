from asyncio import Future
from typing import (
    Dict,
    List,
)
from starlette.websockets import (
    WebSocket,
)

from .base import (
    BaseFileReceiver, TClientSocket
)


class WebSocketFileReceiver(BaseFileReceiver[WebSocket]):
    def handle_fileupload(self, client_socket: WebSocket, data: bytes):
        pass
