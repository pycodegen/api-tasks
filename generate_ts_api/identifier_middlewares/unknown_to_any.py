from typing import Optional

from py_codegen.type_extractor.nodes.BaseNodeType import NodeType
from py_codegen.type_extractor.nodes.ListFound import ListFound

from generate_ts_api.BaseConverter import (
    BasePythonToTypescriptConverter,
    identifier_str,
    define_identifier_middleware,
)


@define_identifier_middleware
def unknown_to_any_identifier(node: NodeType, converter: BasePythonToTypescriptConverter) -> Optional[identifier_str]:
    return identifier_str("any")