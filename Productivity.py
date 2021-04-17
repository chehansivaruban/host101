

class Productivity:
    def __init__(self, irradiance, hours,capacity):
        self.irradiance = irradiance
        self.hours = hours
        self.capacity = capacity

    def getUnits(self):
        print(self.irradiance)
        totalpower = 0
        print(totalpower)
        for i in self.irradiance:
            power = int(self.capacity) * int(i) /1000
            totalpower = totalpower+power
        # units= (self.irradiance*self.area*self.hours)/1000
        print(totalpower)
        return totalpower
