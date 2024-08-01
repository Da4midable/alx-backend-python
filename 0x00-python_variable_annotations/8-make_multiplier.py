#!/usr/bin/env python3

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates multiplier function that multiplies its input by specified factor.

    Args:
        multiplier (float): The factor by which to multiply the input value.

    Returns:
        Callable[[float], float]: A function that takes a float input
         and returns the product of that input and the multiplier.
    """
    def retfloat(a: float) -> float:
        """
        Multiplies input value by multiplier specified in enclosing scope.

        Args:
            a (float): The input value to be multiplied.

        Returns:
            float: The product of the input value and the multiplier.
        """
        return a * multiplier

    return retfloat
