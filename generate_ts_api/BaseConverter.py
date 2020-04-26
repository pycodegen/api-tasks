import abc
from typing import Optional, List, NewType, Dict, Callable

from py_codegen.type_extractor.nodes.BaseNodeType import NodeType

task_id_type = NewType('task_id_type', str)

impl_str = NewType('impl_str', str)

impl_middleware = Callable[
    [NodeType, 'BasePythonToTypescriptConverter'],
    Optional[impl_str]
]

identifier_str = NewType('identifier_str', str)

identifier_middleware = Callable[
    [NodeType, 'BasePythonToTypescriptConverter'],
    Optional[identifier_str]
]


class BasePythonToTypescriptConverter(metaclass=abc.ABCMeta):
    impl_middlewares: List[impl_middleware]
    identifier_middlewares: List[identifier_middleware]

    def __init__(
            self,
            impl_middlewares: List[impl_middleware],
            identifier_middlewares: List[identifier_middleware],
    ):
        self.impl_middlewares = impl_middlewares
        self.identifier_middlewares = identifier_middlewares

    def get_identifier(self, node: NodeType) -> Optional[identifier_str]:
        return run_identifier_middlewares(
            middlewares=self.identifier_middlewares,
            node=node,
            converter=self,
        )

    def get_impl(self, node: NodeType):
        result = run_impl_middlewares(
            middlewares=self.impl_middlewares,
            node=node,
            converter=self,
        )
        return result

    def convert_args(self, args: Dict[str, NodeType]) -> str:
        converted_args = [
            f'{key}: {self.get_identifier(value)},\n'
            for key, value in args.items()
        ]
        return '\n'.join(converted_args)





def define_identifier_middleware(fn: identifier_middleware):
    return fn


def run_identifier_middlewares(
        middlewares: List[identifier_middleware],
        node: NodeType,
        converter: BasePythonToTypescriptConverter,
) -> Optional[identifier_str]:
    for i in range(len(middlewares)):
        result = middlewares[i](node, converter)
        if result is not None:
            return result
    return None


def define_impl_middleware(fn: impl_middleware):
    return fn


def run_impl_middlewares(
        middlewares: List[impl_middleware],
        node: NodeType,
        converter: BasePythonToTypescriptConverter,
) -> Optional[impl_str]:
    for i in range(len(middlewares)):
        result = middlewares[i](node, converter)
        if result is not None:
            return result
    return None
