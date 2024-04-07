#!/usr/bin/python3
"""Define add_integer function
    a: first int
    b: second int (defaults to 98)
    returns the sum (casts to int)
"""


def add_integer(a, b=98):
    """a: first int
    b: second int (defaults to 98)
    returns the sum (casts to int)"""
    if (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
