

class Productivity:
    def __init__(self, irradiance, hours,area):
        self.irradiance = float(irradiance)
        self.hours = hours
        self.area = area

    def getUnits(self):
        units= (self.irradiance*self.area*self.hours)/1000
        return units
