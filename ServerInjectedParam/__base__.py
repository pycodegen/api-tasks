import abc
from typing import Callable, Any

from py_codegen.type_extractor.nodes.BaseNodeType import NodeType


class InjectedParamImpl(metaclass=abc.ABCMeta):
    pass


class ParamImplInjector(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def check_typ(self, node: NodeType) -> bool: pass

    @abc.abstractmethod
    def create_impl(self,
                    param_name: str,
                    typ: NodeType,
    ) -> Callable[[str], Any]:
        """

        :param param_name:
        :param typ:
        :returns: (task_id) => InjectedImplementation
        """
        pass