from py_codegen.type_extractor.type_extractor import TypeExtractor

from generate_python_api.converter import PythonTaskConverter
from generate_python_api.options import MarkTaskFunction
from sample_tasks import sleep_task


def testrun():
    type_extractor = TypeExtractor()
    type_extractor.add({
        MarkTaskFunction(False),
    })(sleep_task)

    converter = PythonTaskConverter(
        extractor=type_extractor,
    )

    result = converter.get_generated_source()

    print(result)

testrun()