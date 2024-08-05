#!/usr/bin/env python3
"""
Module creating a function the average execution time of wait_n(n, max_delay).
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time of wait_n(n, max_delay).

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay for each wait_n call.

    Returns:
        float: The average execution time per call.
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n
