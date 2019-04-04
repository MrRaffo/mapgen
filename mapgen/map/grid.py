# grid.py
# a 2D data structure
import numpy as np

class Grid(object):

        """A 2D data structure"""

        def __init__(self, width, height, dtype=None):
                
                self._width = width
                self._height = height
                
                # generate data
                dataType = np.dtype(dtype)
                self.data = np.empty([width, height], dtype=dataType)

                if dtype is not None:
                        for x in range(width):
                                for y in range(height):
                                        self.data[x, y] = dtype()

        @property
        def width(self):
                return self._width

        @property
        def height(self):
                return self._height

        @property
        def w(self):
                return self._width

        @property
        def h(self):
                return self._height

        def getWidth(self):
                return self._width

        def getHeight(self):
                return self._height

        def get(self, x, y):
                if x < 0 or x >= self._width or y < 0 or y >= self._height:
                        return None
                return self.data[x, y]

        def set(self, x, y, value):
                if x < 0 or x >= self._width or y < 0 or y>= self._height:
                        return
                else:
                        self.data[x, y] = value

        #===============
        # MANIPULATION
        #===============

        def forEach(self, func):
                """call func on every item in the grid"""
                for x in range(self._width):
                        for y in range(self._height):
                                func(self.data[x, y], x, y)

