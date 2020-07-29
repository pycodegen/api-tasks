from abc import ABCMeta

from py_codegen.type_extractor.nodes.BaseNodeType import NodeType
from py_codegen.type_extractor.nodes.ClassFound import ClassFound

from ServerInjectedParam.RemoteFile import RemoteFile
from ServerInjectedParam.__base__ import ParamImplInjector


class BaseRemoteFileInjector(ParamImplInjector, metaclass=ABCMeta):
    def check_typ(self, node: NodeType) -> bool:
        if not isinstance(node, ClassFound):
            return False
        if node.class_raw is not RemoteFile:
            return False
        return True
