from dataclasses import dataclass

from py_codegen.type_extractor.nodes.BaseNodeType import BaseOption


class MarkTaskFunction(BaseOption):
    is_async: bool = False

    def __key(self):
        return (self.is_async,)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, MarkTaskFunction):
            return self.__key() == other.__key()
        return NotImplemented

    def __init__(self, is_async: bool):
        self.is_async = is_async