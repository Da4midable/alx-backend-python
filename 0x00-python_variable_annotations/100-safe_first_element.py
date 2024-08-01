#!/usr/bin/env python3

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns first element of the list if it exists, otherwise returns None.

    Args:
        lst (Sequence[Any]): A sequence (e.g., list, tuple)
        containing elements of any type.

    Returns:
        Optional[Any]: The first element of list if present, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
