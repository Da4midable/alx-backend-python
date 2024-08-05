#!/usr/bin/env python3
"""
This module provides a function to create an asyncio.Task that runs
the wait_random coroutine from another module.
"""

from typing import Callable
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task that runs the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: A task that runs the wait_random coroutine.
    """
    a = asyncio.create_task(wait_random(max_delay))
    return a
