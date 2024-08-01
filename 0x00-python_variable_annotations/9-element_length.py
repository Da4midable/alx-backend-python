#!/usr/bin/env python3
"""
This module provides function for calculating length of elements
in an iterable.
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the input iterable.

    This function takes an iterable of sequences and returns a list of tuples.
    Each tuple contains a sequence from the input and its corresponding length.

    Args:
        lst (Iterable[Sequence]): An iterable containing
        sequences (e.g., strings, lists).

    Returns:
        List[Tuple[Sequence, int]]: list of tuples, where each tuple contains
                                    a sequence from the input and its length.

    Examples:
        >>> element_length(['one', 'two', 'three'])
        [('one', 3), ('two', 3), ('three', 5)]

        >>> element_length([[1, 2], [3, 4, 5]])
        [([1, 2], 2), ([3, 4, 5], 3)]

        >>> element_length([])
        []
    """
    return [(i, len(i)) for i in lst]
