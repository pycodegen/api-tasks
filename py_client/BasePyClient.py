from asyncio.futures import Future
from typing import Any, TypeVar

some_typevar = TypeVar('some_typevar')

class BasePyClient:
    def send_task(self, func_name: str, args: Any) -> Future[Any]:
        pass

    def send_progressive_task(self, func_name: str, args: Any) -> Any:
        pass
