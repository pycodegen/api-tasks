from py_codegen.type_extractor.nodes.BaseNodeType import BaseNodeType
from py_codegen.type_extractor.nodes.ClassFound import ClassFound

from generate_python_api.BaseConverter import ImportsStore
from generate_python_api.converter import PythonTaskConverter


def class_convert_middleware(
        _class: BaseNodeType,
        imports: ImportsStore,
        converter: PythonTaskConverter,
):
    if not isinstance(_class, ClassFound):
        return None
