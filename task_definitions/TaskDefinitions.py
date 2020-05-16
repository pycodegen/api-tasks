from typing import Callable, Dict, List, Awaitable, Any, cast, Union
from dataclasses import dataclass, field
import pathlib

from py_codegen.type_extractor.nodes.ClassFound import ClassFound
from py_codegen.type_extractor.nodes.FixedGenericFound import FixedGenericFound
from py_codegen.type_extractor.nodes.FunctionFound import FunctionFound
from py_codegen.type_extractor.type_extractor import TypeExtractor

from task_definitions.TaskContext import RemoteFile, TaskContext
from task_definitions.errors.MissingTaskContextException import MissingTaskContextException


@dataclass
class TaskCall:
    uuid: str
    func_name: str
    args: List = field(default_factory=list)
    kwargs: Dict = field(default_factory=dict)


@dataclass
class TaskDefinition:
    func: Callable
    remote_file_params: Dict[str, RemoteFile]


@dataclass
class TaskDefinitionsGroup:
    tasks: Dict[str, TaskDefinition] = field(default_factory=dict)

    def __post_init__(self):
        self.type_extractor = TypeExtractor()
        self.type_extractor.add()(TaskContext)
        self.type_extractor.add()(RemoteFile)

    def add_task(self, task_func: Callable):
        self.validate_task_func(task_func)
        remote_file_params = self.get_remote_file_params(task_func)
        task_def = TaskDefinition(
            func=task_func,
            remote_file_params=remote_file_params,
        )
        self.tasks.__setitem__(task_func.__qualname__, task_def)

        def __wrapper_func__(*args, **kwargs):
            result = task_func(*args, **kwargs)
            return result

        return __wrapper_func__

    def validate_task_func(self, task_func: Callable):
        self.type_extractor.add()(task_func)
        task_func_type = cast(FunctionFound, self.type_extractor.collected_types.get(task_func.__qualname__))
        task_context_classnode = cast(ClassFound, self.type_extractor.collected_types.get('TaskContext'))
        task_context_param = cast(
            Union[FixedGenericFound, ClassFound],
            task_func_type.params.get('task_context')
        )
        if getattr(task_context_param, 'origin', None) is not task_context_classnode \
                and task_context_param is not task_context_classnode:
            # FIXME: check inside task_context_param.base_classes
            print(1)
            raise MissingTaskContextException(task_func)

    def run_task(
            self,
            task_call: TaskCall,
    ):
        task_def = self.tasks.get(task_call.func_name)
        if not task_def:
            raise KeyError(f'task not found: {task_call.func_name}')

        # TODO:
        return task_def.func(*task_call.args, **task_call.kwargs)

    def get_remote_file_params(self, task_func: Callable):
        self.type_extractor.add()(task_func)
        task_func_type = cast(FunctionFound, self.type_extractor.collected_types.get(task_func.__qualname__))
        print(self.type_extractor.collected_types)
        remote_file_classnode = self.type_extractor.collected_types.get(RemoteFile.__qualname__)
        return {
            key: value
            for (key, value) in task_func_type.params.items()
            # TODO: check for child classes!
            if value is remote_file_classnode
        }

#
# task_definition = TaskDefinitionsGroup()
#
#
# @task_definition.add_task
# def long_running_task(time: int, val: int):
#     print(f"long_running_task( time={time}, val={val} started at: {datetime.now()}")
#     sleep(time)
#     print(f"long_running_task( time={time}, val={val} ended at: {datetime.now()}")
#     return val
