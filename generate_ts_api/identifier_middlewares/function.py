from typing import Optional

from py_codegen.type_extractor.nodes.BaseNodeType import NodeType
from py_codegen.type_extractor.nodes.FunctionFound import FunctionFound

from generate_ts_api.BaseConverter import (
    BasePythonToTypescriptConverter,
    define_identifier_middleware,
    identifier_str,
)


@define_identifier_middleware
def function_identifier(
        node: NodeType,
        converter: BasePythonToTypescriptConverter,
) -> Optional[identifier_str]:
    if not isinstance(node, FunctionFound):
        return None

    return identifier_str(node.name)