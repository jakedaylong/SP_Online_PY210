#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the circle class
class Circle(object):
    """This is the circle class"""

    def __init__(self, radius):
        """
        Require parameters: Radius
        """
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self._radius = diameter / 2
