import aiofiles
from typing import IO


def parser(file_obj: IO[bytes]) -> None:
    pass


async def run():
    f = aiofiles.open('hello.txt', 'r')

    # f = open('hello.txt', 'r')
    parser(f)