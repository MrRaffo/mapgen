# a basic unit of the map
# contains all info for that part of the map

class Cell(object):
        
        def __init__(self):
                # perlin noise values
                self._pelevation = 0.0
                self._pmoisture = 0.0
                self._ptemperature = 0.0

                self._elevation = 0
                self._moisture = 0
                self._temperature = 0

        def __str__(self):
                return "Elevation: {} ({})\nMoisture: {} ({})\nTemperature: {} ({})\n".format(self._elevation, self._pelevation, self._moisture, self._pmoisture, self._temperature, self._ptemperature)
        
        @property
        def pelevation(self):
                return self._pelevation

        @pelevation.setter
        def pelevation(self, value):
                self._pelevation = value

        @property
        def pmoisture(self):
                return self._pmoisture

        @pmoisture.setter
        def pmoisture(self, value):
                self._pmoisture = value

        @property
        def ptemperature(self):
                return self._ptemperature

        @ptemperature.setter
        def ptemperature(self, value):
                self._ptemperature = value

        @property
        def elevation(self):
                return self._elevation

        @property
        def moisture(self):
                return self._moisture

        @property
        def temperature(self):
                return self._temperature

        def setElevationColor(self):
                comp = self._pelevation * 127 + 128
                self._color = (comp, comp, comp, 255)
        
