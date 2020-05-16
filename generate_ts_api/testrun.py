from py_codegen.type_extractor.type_extractor import TypeExtractor

from generate_ts_api.converter import TypescriptTaskConverter
from sample_tasks import (
    sleep_task,
    some_complicated_task,
    some_task_with_file,
)
from task_definitions.TaskDefinitions import TaskDefinitionsGroup


def testrun():
    task_definitions = TaskDefinitionsGroup()
    task_definitions.add_task(sleep_task)
    task_definitions.add_task(some_complicated_task)
    task_definitions.add_task(some_task_with_file)

    converter = TypescriptTaskConverter(
        task_definitions=task_definitions,
    )

    print('task_definition: \n', converter.get_task_definitions())

    print('other_defs: \n', converter.get_others_definitions())

    # type_extractor = TypeExtractor()
    # type_extractor.add({
    #     MarkTaskFunction(False),
    # })(sleep_task)
    #
    # converter = PythonTaskConverter(
    #     extractor=type_extractor,
    # )
    #
    # result = converter.get_generated_source()
    #
    # print(result)

testrun()