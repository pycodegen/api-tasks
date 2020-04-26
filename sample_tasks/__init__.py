from typing import List

from dataclasses import dataclass
from time import sleep


def sleep_task(a: int) -> int:
    sleep(5)
    return a


@dataclass
class SomeClass:
    some_float: List[float]


def some_complicated_task(some_cls: SomeClass) -> SomeClass:
    print(some_cls.some_float)
    return some_cls