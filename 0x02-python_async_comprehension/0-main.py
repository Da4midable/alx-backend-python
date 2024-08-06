#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = [i async for i in async_generator()]
    print(result)

asyncio.run(print_yielded_values())
