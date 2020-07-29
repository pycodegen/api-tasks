from typing import Callable, Any

from py_codegen.type_extractor.nodes.BaseNodeType import NodeType

from ServerInjectedParam.RemoteFile.Injectors.BaseRemoteFileInjector import BaseRemoteFileInjector


class WebsocketChunkedRemoteFileInjector(BaseRemoteFileInjector):
    def __init__(
            self
    ):
        pass
    def create_impl(self, param_name: str, typ: NodeType) -> Callable[[str], Any]:
        pass