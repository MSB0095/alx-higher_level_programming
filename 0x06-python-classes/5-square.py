#!/usr/bin/python3

""" Square class """


class Square:
    """ Represent a square """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size cannot be negative")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for i in range(1, self.__size + 1):
            for j in range(1, self.__size + 1):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
