#!/usr/bin/python3
import math
"""this is a magic script"""

class MagicClass:
    """the class of the magic"""
    def __init__(self, radius):
        """first function"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self, radius):
        """second function"""
        return self.__radius ** 2 * math.pi

    def circumference(self, radius):
        """last function"""
        return 2 * math.pi * self.__radius
