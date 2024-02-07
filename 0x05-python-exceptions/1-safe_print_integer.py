#!/usr/bin/python3

""" safe integer printing
"""


def safe_print_integer(value):
    isprinted = False
    try:
        print("{:d}".format(value))
        isprinted = True
    except (ValueError, TypeError):
        pass
    return isprinted
