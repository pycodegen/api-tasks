from textwrap import indent

from py_codegen.type_extractor.nodes.BaseNodeType import BaseNodeType
from py_codegen.type_extractor.nodes.ClassFound import ClassFound

from generate_ts_api.BaseConverter import BasePythonToTypescriptConverter, define_impl_middleware


# converts Python-class to typescript-'type'
#   this makes sense because typescript can't access class-methods/etc anyway
#     (or that can be possible with a lot more effort)
@define_impl_middleware
def class_impl_as_ts_type_middleware(
        _class: BaseNodeType,
        converter: BasePythonToTypescriptConverter,
):
    if not isinstance(_class, ClassFound):
        return None

    impl_str = (
        f"type {converter.get_identifier(_class)} = {{\n"
        f"{indent(converter.convert_args(_class.fields), '  ')}\n"
        f"}}\n"
    )
    return impl_str