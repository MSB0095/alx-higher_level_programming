#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    mylen = len(my_list) - 1
    for i in range(mylen, -1, -1):
        print("{:d}".format(int(my_list[i])))
