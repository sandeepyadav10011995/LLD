class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def getLatitude(self):
        return self.latitude

    def setLatitude(self, latitude):
        self.latitude = latitude

    def getLongitude(self):
        return self.longitude

    def setLongitude(self, longitude):
        self.longitude = longitude
