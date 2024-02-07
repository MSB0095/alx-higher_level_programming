#!/usr/bin/python3

""" safe division printing
"""


def safe_print_division(a, b):
    division = None
    try:
        division = a / b
    except (ZeroDivisionError, ValueError, TypeError):
        pass
    finally:
        print("Inside result: {}".format(division))
    return division
