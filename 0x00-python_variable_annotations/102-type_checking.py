#!/usr/bin/env python3
"""
This script defines a function to zoom in on an array by repeating its
elements.

The function `zoom_array` takes a tuple and a factor, returning a list
where each element in the tuple is repeated according to the factor.

The script is executed using Python 3, as specified by the shebang line.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom in on an array by repeating its elements.

    Args:
        lst (Tuple): A tuple containing the elements to be zoomed in.
        factor (int): The number of times each element should be repeated.
                      Defaults to 2.

    Returns:
        List: A list with each element from the tuple repeated according to
              the factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in
