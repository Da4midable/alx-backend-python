#!/usr/bin/env python3

"""
This module demonstrates the use of variable annotations in Python.

Variable Annotations:
    Python 3.6 introduced the ability to add type hints to variables
    using annotations. These annotations don't affect the runtime behavior of
    the code but can be useful for documentation,
    static type checking, and IDE support.
"""

a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"

"""
Variable Descriptions:

a (int): An integer variable with a value of 1.

pi (float): A float variable representing an approximation of pi (3.14).

i_understand_annotations (bool): A boolean variable set to True, indicating
    comprehension of variable annotations.

school (str): A string variable containing the name "Holberton".

These annotations provide type information for each variable, which can be
useful for code readability, documentation, and static type checking tools.
"""
