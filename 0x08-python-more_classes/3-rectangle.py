#!/usr/bin/python3
"""Defines a Rectangle object"""


class Rectangle:
    """
    Rectangle Class
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (int(self.width) * int(self.height))

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * (int(self.width))) + (2 * (int(self.height)))

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        string = ""
        for i in range(self.height):
            for j in range(self.width):
                string += '#'
            if i != self.height - 1:
                string += '\n'
        return string
