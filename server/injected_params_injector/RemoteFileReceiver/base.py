import abc
from asyncio import Future
from typing import (
    Dict,
    List,
    TypeVar, Generic,
    TypedDict,
)

WaitingFileMeta = TypedDict('WaitingFileMeta', {
    'sha256': str,
    'chunkSize': int,
    'chunk_sha256_checksums': List[str],
})

WaitingFileInfo = TypedDict('WaitingFileInfo', {
    'meta': WaitingFileMeta,
    'future': Future,
    'chunks_received': Dict[int, any] # nth --> Chunk
})


FileChunk = TypedDict('FileChunk', {
    'nthChunk': int,
})

TClientSocket = TypeVar('TClientSocket')


class BaseFileReceiver(Generic[TClientSocket], metaclass=abc.ABCMeta):
    waiting_file_infos: Dict[str, WaitingFileInfo]

    def verify_file_chunk(
            self,
            file_chunk: FileChunk,
    ):
        pass


    @abc.abstractmethod
    def handle_fileupload(self, client_socket: TClientSocket, data: bytes):
        pass

    def __init__(
            self,
    ):
        self.completion_futures = {}

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
