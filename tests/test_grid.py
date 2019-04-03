from nose.tools import *

from mapgen.map.grid import *

def test_index():
        grid = Grid(10, 10, 5)

        assert(grid.w == 10)
        assert(grid.height == 10)
        
        assert(grid.getData(1, 2) == 5)
        assert(grid.getData(-1, 8) is None)
        assert(grid.getData(3, 11) is None)
        assert(grid.getData(12, -8) is None)
        assert(grid.getData(1, 10) is None)

