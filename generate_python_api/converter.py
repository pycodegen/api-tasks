from typing import List, Dict, Set, Callable, Optional

from dataclasses import dataclass, field
from py_codegen.type_extractor.nodes.BaseNodeType import BaseNodeType
from py_codegen.type_extractor.nodes.FunctionFound import FunctionFound

from py_codegen.type_extractor.type_extractor import TypeExtractor

from generate_python_api.BaseConverter import BasePythonConverter, ImportsStore
from generate_python_api.middlewares.class_convert import class_convert_middleware
from generate_python_api.options import MarkTaskFunction




@dataclass
class PythonTaskConverter(BasePythonConverter):
    extractor: TypeExtractor
    middlewares: List[
        Callable[
            [BaseNodeType, 'BasePythonConverter'],
            Optional[str],
        ],
    ] = field(default=[
        class_convert_middleware,
    ])

    def get_generated_source(
            self,
            imports: ImportsStore = ImportsStore(),
    ):
        task_functions = {
            key: value
            for key, value in self.extractor.collected_types.items()
            if isinstance(value, FunctionFound)
            and value.options.__contains__(MarkTaskFunction(is_async=False))

        }

        # For every task_functins:

        # 1. is it built-in ? then use built-in
        # 2. is it Class / etc ? is it imported? then append it to 'imported'
        print(task_functions)
