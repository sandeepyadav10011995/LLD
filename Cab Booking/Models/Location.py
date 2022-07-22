import math


class Location:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    # Getters and Setters

    def distance(self, location2: Location):
        return math.sqrt(math.pow(self.latitude - location2.latitude, 2) + math.pow(self.longitude - location2.longitude, 2))
