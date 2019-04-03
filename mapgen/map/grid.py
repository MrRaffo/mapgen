# grid.py
# a 2D data structure
import numpy as np

class Grid(object):

        """A 2D data structure"""

        def __init__(self, width, height, default=None):
                
                self._width = width
                self._height = height
                
                # generate data
                self.data = np.empty([width, height])

                if default is not None:
                        for x in range(width):
                                for y in range(height):
                                        self.data[x, y] = default

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

        def getData(self, x, y):
                if x < 0 or x >= self._width or y < 0 or y >= self._height:
                        return None
                return self.data[x, y]

        def setData(self, x, y, value):
                if x < 0 or x >= self._width or y < 0 or y>= self._height:
                        return
                else:
                        self.data[x, y] = value

        #======================
        #  ANALYSIS
        #======================

