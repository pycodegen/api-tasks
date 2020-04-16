# impossible - needs higher-type
# import asyncio
# from typing import Coroutine
#
# # >>> async def main():
# # ...     print('hello')
# # ...     await asyncio.sleep(1)
# # ...     print('world')
#
#
# async def some_async_func(a: int) -> int:
#     return 3
#
#
# def some_sync_func(b: int) -> int:
#     return 5
#
# from typing import TypeVar, Sequence, Callable
#
#
#
# Args = TypeVar('Args')
#
# ReturnType = TypeVar('ReturnType')
#
#
# # def create_client_task_func(task_func: Callable[[Args], ReturnType]) -> C:
#
#
#
# async def main() -> None:
#     print('hello')
#     await asyncio.sleep(1)
#     val = await some_async_func(3)
#     reveal_type(some_async_func)
#     print('world')
#
#
#
#
# asyncio.run(main())