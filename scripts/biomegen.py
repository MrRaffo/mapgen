#!/bin/python3

import sys
from color import *

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
                

main()
