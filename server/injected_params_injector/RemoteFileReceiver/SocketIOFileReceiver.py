from asyncio import Future
from typing import (
    Dict,
    List,
)

import socketio

from server.injected_params_injector.RemoteFileReceiver.base import (
    WaitingFileInfo,
    WaitingFileMeta,
)


class SocketIOFileReceiver:
    waiting_file_infos: Dict[str, WaitingFileInfo]

    def handle_fileupload(self, sid, data: bytes):
        task_id_separator = data.find(b'[->task_id]\n')
        task_id = data[:task_id_separator]
        arg_name_separator = data.find(b'[->arg_name]\n', task_id_separator)
        arg_name = data[task_id_separator + 1:arg_name_separator]
        bin_data = data[arg_name_separator + 1:]

        # format: assume `{task_id}*{bin_data}
        print(data)

    def __init__(
            self,
            sio: socketio.AsyncServer,
    ):
        self.completion_futures = {}
        self.sio = sio

    @staticmethod
    def __encode_key__(task_id, arg_name):
        return f'file_receiver_future_{task_id}_{arg_name}'

    async def start_receiving_file(self,
                                   task_id,
                                   arg_name,
                                   client_id,
                                   meta: WaitingFileMeta,
                                   ):
        future = Future()
        self.waiting_file_infos[self.__encode_key__(task_id, arg_name)] = {
            'future': future,
            'meta': meta,
        }
        await self.sio.emit(
            'REQUEST_FILE', {
               'task_id': task_id,
               'arg_name': arg_name,
            },
            to=client_id,
        )
        return await future