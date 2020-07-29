import abc
from typing import TypeVar, Generic


OUTPUT_TYPE = TypeVar('OUTPUT_TYPE')


class BaseStreamOutput(
    Generic[OUTPUT_TYPE],
    metaclass=abc.ABCMeta,
):
    @abc.abstractmethod
    async def push(self, item: OUTPUT_TYPE) -> None:
        pass
