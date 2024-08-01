#!/usr/bin/env python3
"""This module provides a function that sums a list of the union of
integers and floats.
"""

from typing import List, Union

a = List[Union[int, float]]


def sum_mixed_list(mxd_lst: a) -> float:
    """This function sums a list of the union of
    integers and floats."""
    return sum(mxd_lst)
