from noise import *
from map.grid import *
from map.cell import *

from math import *

class Generator(object):
       
        def __init__(self):

                self.elevation = {}
                self.moisture = {}
                self.temperature = {}

                self.data = {}
                self.data["elevation"] = self.elevation
                self.data["moisture"] = self.moisture
                self.data["temperature"] = self.temperature

        def parseConfig(self):
                with open('mapgen/config.txt') as f:
                        currentDict = self.elevation
                        for line in f:
                                if "[" in line:
                                        currentDict = self.data[line[1:-2]]
                                        continue
                                        
                                text = line[:-1].split("=")
                                currentDict[text[0]] = int(text[1])

        def genNoise(self, cell, x, y):
                for key in self.data:
                        xo = self.data[key]["xOffset"]
                        yo = self.data[key]["yOffset"]
                        freq = self.data[key]["freq"]
                        octa = self.data[key]["oct"]
                        layers = self.data[key]["layers"]
                        
                        noiseVal = pnoise2((x+xo)/freq, \
                                (y+yo)/freq, octaves = octa)

                        cell.data[key] = {}
                        cell.data[key]["noise"] = noiseVal
                        cell.data[key]["layer"] = floor(noiseVal * layers / 2 + (layers / 2))

        def makeGrid(self, w, h):
                grid = Grid(w, h, Cell)
                self.parseConfig()
                grid.forEach(self.genNoise)
                return grid
