from map.grid import *
from map.cell import *

from noise import *

from math import *

from pygame.locals import *
import pygame

grid = Grid(2, 2, Cell)

def myfunc(cell, x, y):
        cell._pelevation = pnoise2((x + 300) / 16.0, (y + 200) / 16.0, octaves=8)

def myprint(cell, x, y):
        print("Cell (%d, %d):" % (x, y))
        print(cell)

grid.forEach(myfunc)
# grid.forEach(myprint)

def makeGrid(w, h):
        return Grid(w, h, Cell)

eXOffset = 300
eYOffset = 200
eFreq = 180
eOct  = 32

mXOffset = 700
mYOffset = 800
mFreq = 200
mOct = 4

tXOffset = 0
tYOffset = 0
tFreq = 200
tOct  = 4

def noiseFunc(cell, x, y):
        cell._pelevation = pnoise2((x + eXOffset) / eFreq, (y + eYOffset) / eFreq, octaves = eOct)
        cell._pmoisture = pnoise2((x + mXOffset) / mFreq, (y + mYOffset) / mFreq, octaves = mOct)
        cell._ptemperature = pnoise2((x + tXOffset) / tFreq, (y + tYOffset) / tFreq, octaves = tOct)

def colorize(cell, x, y):
        cell.setElevationColor()

def drawGrid(width, height):

        #TODO - fix this awful mess, allow noisemaps for each variable
        # to be seen
        pygame.init()

        screen = pygame.display.set_mode([width, height], pygame.HWSURFACE)
        pygame.display.set_caption("Perlin Noise")

        screen.fill((0, 0, 0))

        grid = Grid(width, height, Cell)
        grid.forEach(noiseFunc)
        grid.forEach(colorize)

        for x in range(width):
                for y in range(height):
                        pygame.draw.rect(screen, grid.getData(x, y)._color, (x, y, 1, 1))

        pygame.display.update()

drawGrid(640, 480)
