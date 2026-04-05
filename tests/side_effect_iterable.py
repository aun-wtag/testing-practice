import asyncio
from unittest.mock import MagicMock


async def async_generator():
    for i in range(10):
        await asyncio.sleep(0.1)
        yield i

my_mock = MagicMock(side_effect=async_generator)
async def consume_async_generator():
    async for x in my_mock():
        print(x)

asyncio.run(consume_async_generator())