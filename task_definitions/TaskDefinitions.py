import abc
import inspect
from typing import Callable, Dict, List, Awaitable, Any, cast
from dataclasses import dataclass, field
import pathlib

from py_codegen.type_extractor.nodes.ClassFound import ClassFound
from py_codegen.type_extractor.nodes.FixedGenericFound import FixedGenericFound
from py_codegen.type_extractor.nodes.FunctionFound import FunctionFound
from py_codegen.type_extractor.type_extractor import TypeExtractor


@dataclass
class TaskCall:
    func_name: str
    args: List = field(default_factory=list)
    kwargs: Dict = field(default_factory=dict)


class MissingTaskContextException(Exception):
    def __init__(self, task_func):
        super(MissingTaskContextException, self).__init__(
            f"Missing `task_context: TaskContext` param: \n"
            f"see function {task_func.__qualname__}\n"
            f"{inspect.getsourcefile(task_func)}:{inspect.getsourcelines(task_func)[1]}\n"
        )


@dataclass
class TaskDefinitionsGroup:
    tasks: Dict[str, Callable] = field(default_factory=dict)

    def __post_init__(self):
        self.type_extractor = TypeExtractor()

    def add_task(self, task_func: Callable):
        self.validate_task_func(task_func)
        self.tasks.__setitem__(task_func.__qualname__, task_func)

        def __wrapper_func__(*args, **kwargs):
            result = task_func(*args, **kwargs)
            return result
        return __wrapper_func__

    def validate_task_func(self, task_func: Callable):
        self.type_extractor.add()(task_func)
        task_func_type = cast(FunctionFound, self.type_extractor.collected_types.get(task_func.__qualname__))
        task_context_classnode = cast(ClassFound, self.type_extractor.collected_types.get('TaskContext'))
        task_context_param = cast(FixedGenericFound, task_func_type.params.get('task_context'))
        if getattr(task_context_param, 'origin', None) is not task_context_classnode \
                and task_context_param is not task_context_classnode:
            # FIXME: check inside task_context_param.base_classes
            print(1)
            raise MissingTaskContextException(task_func)

    def run_task(self, task_call: TaskCall):
        func = self.tasks.get(task_call.func_name)
        if not func:
            raise KeyError(f'task not found: {task_call.func_name}')
        return func(*task_call.args, **task_call.kwargs)

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
