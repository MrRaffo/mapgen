from map.grid import *
from map.cell import *
from map.generator import *
from systems.Renderer import *

from noise import *
from math import *
import sys

from pygame.locals import *
import pygame

class MapGenerator(object):
        
        def __init__(self, w, h):
                pygame.init()

                self.w = w
                self.h = h
                self.fps = 60

                self.renderer = Renderer(w, h, w, h)
                pygame.display.set_caption("Map Generator")

                self.clock = pygame.time.Clock()
                self.lastTick = pygame.time.get_ticks()

                self.generator = Generator(w, h)

        
        def setup(self):
                self.grid = self.generator.makeGrid(self.w, self.h)
      
        def loop(self):

                option = 1
                running = True
                while running:

                        # draw the thing
                        self.renderer.clear()

                        if option == 0:
                                self.renderer.drawTerrain(self)
                        if option == 1:
                                self.renderer.drawMap(self, "elevation")
                        if option == 2:
                                self.renderer.drawMap(self, "moisture")
                        if option == 3:
                                self.renderer.drawMap(self, "temperature")
                        if option == 4:
                                self.renderer.drawMap(self, "elevation")

                        self.renderer.update()

                        for event in pygame.event.get():
                                if event.type == QUIT:
                                        running = False
                                if event.type == KEYDOWN:
                                        if event.key == K_ESCAPE:
                                                running = False
                                        
                                        if event.key == K_0:
                                                option = 0
                                        if event.key == K_1:
                                                option = 1
                                        if event.key == K_2:
                                                option = 2
                                        if event.key == K_3:
                                                option = 3
                                        if event.key == K_4:
                                                option = 4

                        self.clock.tick(self.fps)

if len(sys.argv) < 2:
        mapgen = MapGenerator(800, 800)
else:
        mapgen = MapGenerator(int(sys.argv[1]), int(sys.argv[2]))
mapgen.setup()
mapgen.loop()
