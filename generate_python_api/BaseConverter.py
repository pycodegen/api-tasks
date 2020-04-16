from dataclasses import dataclass, field
from typing import Optional, Callable, List, NewType, Dict, Set

from py_codegen.type_extractor.nodes.BaseNodeType import BaseNodeType


task_id_type = NewType('task_id_type', str)


@dataclass
class ImportsStore:
    value: Dict[str, Set[str]] = field(default_factory=dict)

    def add(self, path_str: str, name: str):
        imports_set: Set[str] = self.value.get(path_str, set())
        imports_set.add(name)
        self.value.__setitem__(path_str, imports_set)


class BasePythonConverter:
    middlewares: List[
        Callable[
            [BaseNodeType, 'BasePythonConverter'],
            Optional[str],
        ],
    ]