#!/usr/bin/env python3
"""
This module demonstrates asynchronous programming in Python.

The shebang line above specifies the interpreter to be used for executing
this script. It uses the env command to locate the Python 3 interpreter
in the user's environment.
"""

import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay and returns it.

    Args:
        max_delay (float, optional): Maximum delay in seconds. Defaults to 10.

    Returns:
        float: The actual time delayed, between 0 and max_delay seconds.

    This function generates a random delay between 0 and max_delay seconds,
    waits for that duration asynchronously, and then returns the delay value..
    """
    time_to_wait = random.uniform(0, max_delay)
    await asyncio.sleep(time_to_wait)
    return time_to_wait
