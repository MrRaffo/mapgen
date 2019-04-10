from noise import *
from map.grid import *
from map.cell import *

from math import *
from collections import *

class Generator(object):
       
        def __init__(self, w, h):

                self.w = w
                self.h = h

                self.elevation = {}
                self.moisture = {}
                self.temperature = {}

                self.data = {}
                self.data["elevation"] = self.elevation
                self.data["moisture"] = self.moisture
                self.data["temperature"] = self.temperature

                for key in self.data:
                        self.data[key]["max"] = -1.0
                        self.data[key]["min"] = 1.0

                self.biomes = OrderedDict({})

        def parseConfig(self):
                """get terrain definitions from file"""
                with open('mapgen/terrain.cfg') as f:
                        currentDict = self.elevation
                        for line in f:
                                if "[" in line:
                                        currentDict = self.data[line[1:-2]]
                                        continue
                                        
                                text = line[:-1].split("=")
                                currentDict[text[0]] = int(text[1])

        def parseBiomes(self):
                """get the biome definitions from file"""

                with open('mapgen/biomes.cfg') as f:
                        biome = ""
                        data = ""
                        upper = 0.0
                        lower = 0.0
                        color = ""
                        for line in f:
                                if "[" in line:
                                        biome = line[1:-2]
                                        if biome not in self.biomes:
                                                self.biomes[biome] = {}
                                                continue

                                text = line[:-1].split("=")
                                if text[0] == "data":
                                        data = text[1]
                                        self.biomes[biome][data] = {}
                                if text[0] == "lower":
                                        lower = float(text[1])
                                        self.biomes[biome][data]["lower"] = lower
                                if text[0] == "upper":
                                        upper = float(text[1])
                                        self.biomes[biome][data]["upper"]  = upper
                                if text[0] == "colour":
                                        self.biomes[biome]["color"] = text[1]
                                


        def genNoise(self, cell, x, y):
                """give a cell a 'noise' value for all applicable noisemaps (elevation, moisture etc)"""
                for key in self.data:
                        xo = self.data[key]["xOffset"]
                        yo = self.data[key]["yOffset"]
                        freq = self.data[key]["freq"]
                        octa = self.data[key]["oct"]
                        layers = self.data[key]["layers"]
                        
                        noiseVal = pnoise2((x+xo)/freq, \
                                (y+yo)/freq, octaves = octa)

                        # record max and min noise values as we go
                        if noiseVal > self.data[key]["max"]:
                                self.data[key]["max"] = noiseVal
                        elif noiseVal < self.data[key]["min"]:
                                self.data[key]["min"] = noiseVal
                        
                        cell.data[key] = {}
                        cell.data[key]["noise"] = noiseVal


        def normalizeNoise(self):
                """noise values have no guaranteed max or min value, so this function will
                help calculate normalized values between 0.0 and 1.0"""
                for key in self.data:           
                        self.data[key]["range"] = self.data[key]["max"] - self.data[key]["min"]

        def genNormalizedNoise(self, cell, x, y):
                """shift noise value to one between 0 and 1"""
                for key in self.data:
                        cell.data[key]["noise"] = (cell.data[key]["noise"] + (self.data[key]["min"] * -1.0)) / self.data[key]["range"]


        def genTempGradient(self, cell, x, y):
                """hotter in the south, colder in the north"""
                curTemp = cell.data["temperature"]["noise"]
                newTemp = 2 * curTemp * sin((pi / 4) * (y / self.h)) + ((y/self.h)/4)
                #newTemp = curTemp * (y / (self.h / 2))
                newTemp = min(newTemp, 1.0)
                newTemp = max(0.0, newTemp)
                cell.data["temperature"]["noise"] = newTemp


        def genLayers(self, cell, x, y):
                """Calculate a 'layer' (an integer representation of the intensity of a noise value)
                of each cell"""
                for key in self.data:
                        cell.data[key]["layer"] = min(floor(cell.data[key]["noise"] * self.data[key]["layers"]), self.data[key]["layers"] - 1)
                               

        def genBiomes(self, cell, x, y):
                """get a biome for each cell"""

                cell.data["biome"] = {}
                for biome in self.biomes:
                        check = True
                        for datamap in self.biomes[biome]:
                                if datamap in cell.data:
                                        upper = self.biomes[biome][datamap]["upper"]
                                        lower = self.biomes[biome][datamap]["lower"]
                                        # normalize this info
                                        upperLayer = floor(upper * self.data[datamap]["layers"])
                                        lowerLayer = floor(lower * self.data[datamap]["layers"])
                                        cellLayer = cell.data[datamap]["layer"]
                                        #rint("(%d, %d) comparing %d with %d and %d (%s:%s)" % (x, y, cellLayer, lowerLayer, upperLayer, datamap, biome))

                                        if cell.data[datamap]["layer"] < lowerLayer or cell.data[datamap]["layer"] > upperLayer:
                                                check = False
                        if check is True:
                                cell.data["biome"]["type"] = biome

        def findNoiseLimits(self, cell, x, y):
                for key in self.data:
                        if cell.data[key]["noise"] > self.data[key]["max"]:
                                self.data[key]["max"] = cell.data[key]["noise"]
                        elif cell.data[key]["noise"] < self.data[key]["min"]:
                                self.data[key]["min"] = cell.data[key]["noise"]

                        if cell.data[key]["layer"] > self.data[key]["maxLayer"]:
                                self.data[key]["maxLayer"] = cell.data[key]["layer"]
                        elif cell.data[key]["layer"] < self.data[key]["minLayer"]:
                                self.data[key]["minLayer"] = cell.data[key]["layer"]

        def makeGrid(self, w, h):
                print("Producing map %ix%i" % (w, h))
                grid = Grid(w, h, Cell)
                print("Getting parameters from file...")
                self.parseConfig()
                self.parseBiomes()
                print("Generating noisemaps...")
                grid.forEach(self.genNoise)
                print("Normalizing noise...")
                self.normalizeNoise()
                grid.forEach(self.genNormalizedNoise)
                print("Interpolating temperature...")
                grid.forEach(self.genTempGradient)
                print("Generating layers...")
                grid.forEach(self.genLayers)
                print("Generating biomes...")
                grid.forEach(self.genBiomes)
                print("Terrain generated.")

                for key in self.data:
                        self.data[key]["max"] = -1.0
                        self.data[key]["maxLayer"] = 0
                        self.data[key]["minLayer"] = self.data[key]["layers"]
                        self.data[key]["min"] = 1.0
                grid.forEach(self.findNoiseLimits)

                return grid
