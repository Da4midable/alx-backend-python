#!/usr/bin/env python3
"""
This module measures the runtime of concurrent async comprehensions.

The shebang line above specifies the interpreter to be used for executing
this script. It uses the env command to locate the Python 3 interpreter
in the user's environment.
"""

import time
import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension four times
    concurrently.

    This function creates four tasks, each running async_comprehension,
    executes them concurrently using asyncio.gather, and measures the total
    time taken.

    Returns:
        float: The total runtime in seconds.

    Note:
        This function demonstrates the use of asyncio.create_task and
        asyncio.gather for concurrent execution of coroutines.
    """
    start_time = time.time()
    tasks: List[asyncio.Task] = [asyncio.create_task(async_comprehension())
                                 for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
