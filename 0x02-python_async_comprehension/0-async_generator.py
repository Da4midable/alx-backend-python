#!/usr/bin/env python3
"""
This module demonstrates an asynchronous generator in Python.

The shebang line above specifies the interpreter to be used for executing
this script. It uses the env command to locate the Python 3 interpreter
in the user's environment.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields random float values.

    This coroutine generates 10 random float values between 0 and 10,
    with a 1-second delay between each yield.

    Yields:
        float: A random value between 0 and 10.

    Note:
        This function uses asyncio.sleep() to simulate an asynchronous delay,
        making it suitable for demonstrating asynchronous programming concepts.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
