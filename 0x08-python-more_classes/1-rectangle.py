#!/usr/bin/python3
"""Defines a Rectangle object"""


class Rectangle:
    """
    Rectangle Class
    """
    def __init__(self, width=0, height=0):
        Rectangle.width(self, width)
        Rectangle.height(self, height)

    def width(self):
        return self.width

    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.width = value

    def height(self):
        return self.width

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.width = value
