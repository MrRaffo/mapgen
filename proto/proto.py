# a prototype of the map generation program, uses perlin noise library

from noise import *
from pygame.locals import *
from math import *
import pygame

def genNoiseGrid(size, freq=16.0):
        
        grid = []

        for y in range(size):
                row = []
                for x in range(size):
                        row.append(pnoise2((x) / freq, y / freq, octaves=4))
                grid.append(row)

        return grid


def colorGrid(grid):
        newgrid = []

        for y in range(len(grid)):
                row = []
                for x in range(len(grid[0])):
                        row.append(floor(grid[y][x] * 128) + 128)
                newgrid.append(row)

        return newgrid

def drawGrid(size):
       
        pygame.init()

        screen = pygame.display.set_mode([size, size], pygame.HWSURFACE)
        pygame.display.set_caption("Perlin Noise Prototype")
        
        screen.fill((0, 0, 0))

        pgrid = genNoiseGrid(size, 200)
        cgrid = colorGrid(pgrid)


        for y in range(size):
                for x in range(size):
                        pygame.draw.rect(screen, (cgrid[y][x], cgrid[y][x], cgrid[y][x]), (x, y, 1, 1))

        pygame.display.update()

        running = True
        while(running):
                for event in pygame.event.get():
                        if event.type == QUIT:
                                running = False
                        if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                        running = False

drawGrid(800)
