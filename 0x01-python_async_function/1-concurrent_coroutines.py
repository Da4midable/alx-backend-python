#!/usr/bin/env python3

"""
Module for running `wait_random` n times withmaximum delay of `max_delay`.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run `wait_random` n times with a maximum delay of `max_delay`.

    Args:
        n (int): The number of times to call `wait_random`.
        max_delay (float): The maximum delay for `wait_random`.

    Returns:
        List[float]: A list of the actual delays.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return results
