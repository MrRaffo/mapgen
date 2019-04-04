from noise import *
from map.grid import *
from map.cell import *

class Generator(object):
       
        def __init__(self):
        # TODO - read these from a config file

                self.eXOffset = 300
                self.eYOffset = 200
                self.eFreq = 180
                self.eOct  = 32

                self.mXOffset = 700
                self.mYOffset = 800
                self.mFreq = 200
                self.mOct = 4

                self.tXOffset = 0
                self.tYOffset = 0
                self.tFreq = 200
                self.tOct  = 4

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

        def elevationNoise(self, cell, x, y):
                xo = self.elevation["xOffset"]
                yo = self.elevation["yOffset"]
                freq = self.elevation["freq"]
                octa = self.elevation["oct"]
                cell._pelevation = pnoise2((x+xo)/freq, (y+yo)/freq, \
                        octaves = octa)

        def moistureNoise(self, cell, x, y):
                xo = self.moisture["xOffset"]
                yo = self.moisture["yOffset"]
                freq = self.moisture["freq"]
                octa = self.moisture["oct"]
                cell._pmoisture = pnoise2((x+xo)/freq, (y+yo)/freq, \
                        octaves = octa)

        def temperatureNoise(self, cell, x, y):
                xo = self.temperature["xOffset"]
                yo = self.temperature["yOffset"]
                freq = self.temperature["freq"]
                octa = self.temperature["oct"]
                cell._ptemperature = pnoise2((x+xo)/freq, (y+yo)/freq, \
                        octaves = octa)


        def makeGrid(self, w, h):
                grid = Grid(w, h, Cell)
                self.parseConfig()
                grid.forEach(self.elevationNoise)
                grid.forEach(self.moistureNoise)
                grid.forEach(self.temperatureNoise)
                return grid
