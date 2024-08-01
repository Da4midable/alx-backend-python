#!/usr/bin/env python3

"""
This module provides a function for converting a float to a string.

The shebang line '#!/usr/bin/env python3' at top of file is used in Unix-like
operating systems to specify this script should be executed using Python 3
interpreter. '/usr/bin/env' part allows system to locate Python interpreter
in user's environment, making script more portable across different systems.
"""


def to_str(n: float) -> str:
    """
    Convert a float number to its string representation.

    Function takes a float as argument and returns its string representation.
    It uses type hints to indicate that the input parameter should be a float
    and that the return value is a string.

    Args:
        n (float): The float number to be converted to a string.

    Returns:
        str: The string representation of the input float.

    Examples:
        >>> to_str(3.14)
        '3.14'
        >>> to_str(-0.5)
        '-0.5'
        >>> to_str(1.0)
        '1.0'
    """
    return str(n)
