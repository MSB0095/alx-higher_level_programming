#!/usr/bin/python3


def uniq_add(my_list=[]):
    sum = 0
    unique_int = []
    for element in my_list:
        if element in unique_int:
            continue
        else:
            unique_int.append(element)
            sum += int(element)
    return sum
