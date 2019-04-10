# A class for creating and manipulating colours
from math import *
from random import *

class Color(object):

        def __init__(self, r, g , b, a = 255):
                self.r = r
                self.g = g
                self.b = b
                self.a = a

        def __str__(self):
                return "({0}, {1}, {2}, {3})".format(self.r, self.g, self.b, self.a)

        """Allow equality comparison using '==' """
        def __eq__(self, col):
                return (self.r == col.r and self.g == col.g and self.b == col.b and self.a == col.a)

        def __ne__(self, col):
                return (self.r != col.r or self.g != col.g or self.b != col.b or self.a != col.a)

        def get(self):
                return (self.r, self.g, self.b, self.a)

        def getInt(self):
                return self.r << 24 | self.self.g << 16 | self.b << 8 | self.a

        def getStr(self):
                return "0x{:02X}{:02X}{:02X}{:02X}".format(self.r, self.g, self.b, self.a)

        def shade(self, factor):
                """return a new shade of this color, brightened or darkened by factor"""
                newr = min(floor(self.r * factor), 255)
                newg = min(floor(self.g * factor), 255)
                newb = min(floor(self.b * factor), 255)
                newa = self.a

                return Color(newr, newg, newb, newa)
