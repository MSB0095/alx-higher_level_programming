#!/usr/bin/python3
"""inherits_from function"""


def inherits_from(obj, a_class):
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
