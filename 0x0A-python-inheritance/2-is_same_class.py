#!/usr/bin/python3
"""is_same_class function"""


def is_same_class(obj, a_class):
    """is_same_class function : returns true only when obj
    is an instance of a_class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False