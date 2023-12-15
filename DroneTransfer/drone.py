import random

class Drone:
    def __init__(self, nameOfDrone = "DroneOne", startingLongitude = 0, startingLatitude = 0):
        self.name = nameOfDrone
        self.longitude = startingLongitude
        self.latitude = startingLatitude

    def getCoords(self):
        return self.longitude, self.latitude

    def changeCoordsAtRandom(self, longitude, latitude):
        num1 = random.random() * 10
        num2 = random.random() * 10
        self.longitude += num1
        self.latitude += num2
        return self.longitude, self.latitude

    def statusExample(self):
        self.longitude, self.latitude = self.changeCoordsAtRandom(self.longitude, self.latitude)
        return f"{self.name}, {self.longitude:.3f}, {self.latitude:.3f}"
