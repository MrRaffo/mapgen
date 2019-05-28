#!/usr/bin/python3

import sys
from color import *

defaults = { "sealevel": 0.5,
             "evariance": 0.5,
             "mvariance": 0.5,
             "tvariance": 0.5 }

def parseConfig(filename):
        """Read initial values from file
        
        read info, such as sealevel, from file and generate the rest of the 
        data using it
        """

        with open(filename, "r") as f:
                for line in f:
                        var, value = line[:-1].split("=")
                        if var in defaults:
                                defaults[var] = float(value)

def printDefaults():
        for key in defaults:
                print("%s:%f" % (key, defaults[key]))

def main():
        print("Biome Config Generator")

        layers = 32
        output = "mapgen/biomes.cfg"

        f = open(output, 'w')

        # all values need to be normalized between 0.0 and 1.0:
        step = 1.0 / layers
        colorStep = 255 / layers
        baseColor = Color(0, 255, 0, 255)

        for i in range(layers):
                f.write("[layer%d]\n" % (i))
                f.write("data=elevation\n")
                f.write("lower=%f\n" % (i * step))
                f.write("upper=%f\n" % ((i+1) * step))
                f.write("colour=%s\n" % (baseColor.shade((i*step))).getStr())
        f.close()
                
parseConfig("scripts/world.cfg")
printDefaults()
