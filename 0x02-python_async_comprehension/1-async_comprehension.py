#!/usr/bin/env python3
"""
This module demonstrates an asynchronous list comprehension in Python.

The shebang line above specifies the interpreter to be used for executing
this script. It uses the env command to locate the Python 3 interpreter
in the user's environment.
"""

from typing import List
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension over async_generator.

    This coroutine uses an asynchronous list comprehension to collect values
    yielded by the async_generator coroutine.

    Returns:
        list: A list of 10 random float values between 0 and 10.

    Note:
        This function demonstrates the use of async comprehensions, which allow
        for concise creation of collections from asynchronous generators.
    """
    return [result async for result in async_generator()]
