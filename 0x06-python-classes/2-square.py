#!/usr/bin/python3

""" Square class """


class Square:
    """ Represent a square """
    __size = 0
    """ size of the square """
    def __init__(self, size=0):
        self.__size = size
        try:
            if type(size) != int:
                raise TypeError
            if size < 0:
                raise ValueError
        except TypeError:
            raise TypeError('size must be an integer')
        except ValueError:
            raise ValueError('size must be >= 0')
