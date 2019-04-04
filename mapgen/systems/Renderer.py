# handles all drawing

from pygame.locals import *
import pygame

from math import *

class Renderer(object):
        
        def __init__(self, w, h, res_w, res_h):
                self.w = w
                self.h = h
                self.res_w = res_w
                self.res_h = res_h

                self.scale = w / res_w
                self.screen = pygame.display.set_mode([self.w, self.h], pygame.HWSURFACE)
                self.surface = pygame.display.get_surface()

        def clear(self):
                self.screen.fill((0, 0, 0, 0))

        def update(self):
                pygame.display.flip()

        def drawTerrain(self, mapgen):
                self.screen.fill((0, 255, 255, 255))

        def drawElevationMap(self, mapgen):
                layers = mapgen.generator.elevation["layers"]
                colors = []
                step = 255 / layers
                for x in range(layers):
                        colors.append((40, step * x, 40, 255))

                for x in range(self.w):
                        for y in range(self.h):
                                col = floor(mapgen.grid.get(x, y).pelevation * (layers / 2) + layers / 2)
                                self.surface.set_at((x, y), colors[col])
                        

        def drawMoistureMap(self, mapgen):
                layers = mapgen.generator.moisture["layers"]
                colors = []
                step = 255 / layers
                for x in range(layers):
                        colors.append((0, step * x / 2, step * x,  255))

                for x in range(self.w):
                        for y in range(self.h):
                                col = floor(mapgen.grid.get(x, y).pmoisture * (layers / 2) + layers / 2)
                                self.surface.set_at((x, y), colors[col])

        def drawTemperatureMap(self, mapgen):
                layers = mapgen.generator.temperature["layers"]
                colors = []
                step = 255 / layers
                for x in range(layers):
                        colors.append((step * x, step * x / 4, step * x / 4,  255))

                for x in range(self.w):
                        for y in range(self.h):
                                col = floor(mapgen.grid.get(x, y).ptemperature * (layers / 2) + layers / 2)
                                self.surface.set_at((x, y), colors[col])


