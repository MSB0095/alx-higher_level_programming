#!/usr/bin/python3

""" divide a list
"""


def list_division(my_list_1, my_list_2, list_length):
    division = [0] * list_length
    for i in range(0, list_length):
        try:
            division[i] = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            division[i] = 0
        except ZeroDivisionError:
            print("division by 0")
            division[i] = 0
        except IndexError:
            print("out of range")
            division[i] = 0
        finally:
            pass
    return division
