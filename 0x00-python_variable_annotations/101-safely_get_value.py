#!/usr/bin/env python3

"""
Module exploring the use of TypeVar annotation.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get a value from a dictionary.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None], optional): The default value to return if
        key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key if found,
        otherwise the default value.

    Type Variables:
        T: A generic type for the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
