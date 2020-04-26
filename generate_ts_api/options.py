from dataclasses import dataclass

from py_codegen.type_extractor.nodes.BaseNodeType import BaseOption


class MarkTsTaskFunction(BaseOption):
    has_stream: bool = False

    def __key(self):
        return (self.has_stream,)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, MarkTsTaskFunction):
            return self.__key() == other.__key()
        return NotImplemented

    def __init__(self, has_stream: bool):
        self.has_stream = has_stream