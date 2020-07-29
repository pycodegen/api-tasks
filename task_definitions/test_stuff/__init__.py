from typing import TypeVar, Dict, Mapping, Type


class BaseCls:
    pass


class A(BaseCls):
    a: int


class B(BaseCls):
    b: str


BaseClsVar = TypeVar('BaseClsVar', bound=BaseCls)


a: Type[BaseClsVar] = 1