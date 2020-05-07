from typing import TypeVar, Generic, Callable, Any, List

from typing_extensions import Protocol, Type

ReturnType = TypeVar('ReturnType')


class SomeCallable(Protocol):
    def __call__(self, a: int) -> Any: ...


def add_some_class(some_class: SomeCallable):
    print(some_class)
    return some_class


def some_aa(a: int, b: str, c: float) -> float:
    print(a)
    return 3.3


add_some_class(some_aa)


def add_some_class2(f: Callable[[..., int], float]):
    pass


