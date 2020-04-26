from typing import Optional

from py_codegen.type_extractor.nodes.BaseNodeType import NodeType
from py_codegen.type_extractor.nodes.ClassFound import ClassFound
from py_codegen.type_extractor.utils import is_builtin

from generate_ts_api.BaseConverter import (
    BasePythonToTypescriptConverter,
    define_identifier_middleware,
    identifier_str,
)

@define_identifier_middleware
def builtin_identifier(
        node: NodeType,
        converter: BasePythonToTypescriptConverter,
) -> Optional[identifier_str]:
    if not is_builtin(node):
        return None
    typ = node
    if typ == str:
        return 'string'
    if typ == int or typ == float:
        return 'number'
    if typ == bool:
        return 'boolean'