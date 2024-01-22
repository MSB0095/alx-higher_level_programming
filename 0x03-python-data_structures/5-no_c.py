#!/usr/bin/env python3

def no_c(my_string):
    if my_string:
        new_string = []
        for i in range(len(my_string)):
            if (my_string[i] == 'c') or (my_string[i] == 'C'):
                continue
            new_string.append(my_string[i])
        new_str = ''.join(new_string)
        return new_str
