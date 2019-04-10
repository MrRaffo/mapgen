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
                landCol = (0, 200, 50, 255)
                seaCol = (0, 50, 255, 255)

                for x in range(self.w):
                        for y in range(self.h):
                                biome = mapgen.grid.get(x, y).data["biome"]["type"]
                                color = Color(mapgen.generator.biomes[biome]["color"])
                                
                                self.surface.set_at((x, y), color)

        def drawMap(self, mapgen, typename):
                if typename not in mapgen.generator.data:       
                        print("Unable to Render, no data!")
                        return

                layers = mapgen.generator.data[typename]["layers"]
                colors = []
                step = 255 / layers
                for x in range(layers):
                        if typename == "elevation":
                                colors.append((step * x / 4, step * x, step * x / 4))
                        elif typename == "moisture":
                                colors.append((0, step * x / 2, step * x, 255))
                        elif typename == "temperature":
                                colors.append((step * x, step * x / 4, step * x / 4, 255))
                        else:
                                colors.append((step * x, step * x, step * x, 255))

                for x in range(self.w):
                        for y in range(self.h):
                                col = mapgen.grid.get(x, y).data[typename]["layer"]
                                self.surface.set_at((x, y), colors[col])

                
