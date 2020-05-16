import inspect


class MissingTaskContextException(Exception):
    def __init__(self, task_func):
        super(MissingTaskContextException, self).__init__(
            f"Missing `task_context: TaskContext` param: \n"
            f"see function {task_func.__qualname__}\n"
            f"{inspect.getsourcefile(task_func)}:{inspect.getsourcelines(task_func)[1]}\n"
        )
