from textwrap import indent
from typing import Dict, List

from py_codegen.type_extractor.nodes.BaseNodeType import NodeType
from py_codegen.type_extractor.nodes.FunctionFound import FunctionFound
from py_codegen.type_extractor.type_extractor import TypeExtractor

from generate_ts_api.BaseConverter import (
    BasePythonToTypescriptConverter,
    identifier_middleware,
    impl_middleware,
    run_impl_middlewares,
)
from generate_ts_api.identifier_middlewares.builtins import builtin_identifier
from generate_ts_api.identifier_middlewares.class_identifier import class_identifier
from generate_ts_api.identifier_middlewares.list import list_identifier
from generate_ts_api.identifier_middlewares.unknown_to_any import unknown_to_any_identifier
from generate_ts_api.impl_middlewares.class_impl import class_impl_as_ts_type_middleware
from generate_ts_api.options import MarkTsTaskFunction
from task_definitions.TaskDefinitions import TaskDefinitionsGroup


class TypescriptTaskConverter(BasePythonToTypescriptConverter):
    def __init__(
            self,
            task_definitions: TaskDefinitionsGroup,
            identifier_middlewares: List[identifier_middleware] = None,
            impl_middlewares: List[impl_middleware] = None,
    ):
        super().__init__(
            impl_middlewares=impl_middlewares or [
                class_impl_as_ts_type_middleware,
            ],
            identifier_middlewares=identifier_middlewares or [
                builtin_identifier,
                class_identifier,
                list_identifier,
                unknown_to_any_identifier,
            ],
        )
        self.task_definitions = task_definitions
        self.extractor = TypeExtractor()

        for key, task in self.task_definitions.tasks.items():
            self.extractor.add({
                MarkTsTaskFunction(has_stream=False),
            })(task.func)

    def get_task_definitions(self):
        task_funcs = {
            key: value
            for key, value in
            self.extractor.collected_types.items()
            if isinstance(value, FunctionFound)
            and (
                   value.options.__contains__(MarkTsTaskFunction(True))
                   or value.options.__contains__(MarkTsTaskFunction(False))
            )
        }

        non_streamed_task_funcs = [
            self.__get_non_streamed_task_func_definition(value)
            for value in
            task_funcs.values()
            if value.options.__contains__(MarkTsTaskFunction(False))
        ]
        return '\n\n'.join(non_streamed_task_funcs)

    def __get_non_streamed_task_func_definition(self, task_fn: FunctionFound) -> str:
        # TODO: use get_identifier(
        """
        example:

        class SomeClientAPI {
          some_task(args: {
            a: number,
          }): Promise<number> {
            this.apiInfra.sendTask(
          }
        """
        return (
            f"{task_fn.name}(args: {{\n"
            f"{indent(self.convert_args(task_fn.params), '  ')}\n"
            f"}}): Promise<\n"
            f""
            f"> {{\n"
            f"  return this.apiInfra.sendTask({{\n"
            f"    apiName: {task_fn.name},\n"
            f"    args,\n"
            f"  }})\n"
            f"}}"
        )

    def get_others_definitions(self):
        converted = [
            self.convert_non_task(value)
            for value in self.extractor.collected_types.values()
            if not (
                isinstance(value, FunctionFound)
                and value.options.__contains__(MarkTsTaskFunction(False))
            )
        ]
        # converted_without_none =
        # return converted
        return '\n\n'.join(list(filter(None, converted)))

    def convert_non_task(self, node: NodeType):
        result = run_impl_middlewares(
            middlewares=self.impl_middlewares,
            node=node,
            converter=self,
        )
        return result
