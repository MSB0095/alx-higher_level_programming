#!/usr/bin/python3
"""is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class function
    a function that returns True if isinstance or issubclass"""
    if (isinstance(obj, a_class)) or (issubclass(type(obj), a_class)):
        return True
    else:
        return False
