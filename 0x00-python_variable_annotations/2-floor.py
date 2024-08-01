#!/usr/bin/env python3
"""
This script contains a function to compute floor of a floating-point number.

Function Documentation:
The script includes a function `floor` that utilizes the `math.floor` method
to return largest integer less than or equal to a given floating-point number.
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of the given floating-point number.

    Parameters:
    n (float): The number whose floor value is to be computed.

    Returns:
    int: The largest integer less than or equal to the given number.

    Example:
    >>> floor(3.7)
    3
    >>> floor(-2.3)
    -3
    """
    return math.floor(n)
