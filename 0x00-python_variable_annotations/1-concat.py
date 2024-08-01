#!/usr/bin/env python3

"""
This module provides a function for concatenating two strings.

Shebang line '#!/usr/bin/env python3' at top of file is used in Unix-like
operating systems to specify that this script should be executed using Python 3
interpreter. The '/usr/bin/env' part allows system to locate Python interpreter
in user's environment, making script more portable across different systems.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings and return the result.

    This function takes two string arguments and returns their concatenation.
    It uses type hints to indicate that both input parameters should be strings
    and that the return value is also a string.

    Args:
        str1 (str): The first string to be concatenated.
        str2 (str): The second string to be concatenated.

    Returns:
        str: The concatenation of str1 and str2.

    Example:
        >>> concat("Hello, ", "world!")
        'Hello, world!'
    """
    return str1 + str2
