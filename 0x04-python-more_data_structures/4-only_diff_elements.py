#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    new_set = set()
    for element1 in set_1:
        if element1 in set_2:
            continue
        new_set.add(element1)
    for element2 in set_2:
        if element2 in set_1:
            continue
        new_set.add(element2)
    return new_set
