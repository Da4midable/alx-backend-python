#!/usr/bin/env python3
"""
This module provides a function for summing a list of float numbers.

The shebang line above specifies that this script should be executed using the
Python 3 interpreter in Unix-like operating systems. It uses '/usr/bin/env' to
locate the Python interpreter in the user's environment, enhancing portability.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of float numbers.

    This function takes a list of float numbers and returns their sum. It uses
    type hints to indicate that the input should be a list of floats and the
    return value is a float.

    Args:
        input_list (List[float]): A list of float numbers to be summed.

    Returns:
        float: The sum of all numbers in the input list.

    Examples:
        >>> sum_list([1.0, 2.5, 3.7])
        7.2
        >>> sum_list([-1.1, 2.2, -3.3])
        -2.2
        >>> sum_list([])
        0.0
    """
    return sum(input_list)
