from models.Location import Location
from models.Trip import Trip


class Cab:
    def __init__(self, id: str, driverName: str) -> None:
        self.id = id
        self.driverName = driverName
        self.isAvailable = True
        self.currentTrip = None
        self.currentLocation = None

    def getId(self):
        return self.id

    def getDriverName(self):
        return self.driverName

    def getIsAvailable(self):
        return self.isAvailable

    def getCurrentTrip(self) -> Trip:
        return self.currentTrip

    def getLocation(self) -> Location:
        return self.currentLocation

    def setIsAvailable(self, isAvailable: bool):
        self.isAvailable = isAvailable

    def setCurrentTrip(self, currentTrip: Trip):
        self.currentTrip = currentTrip

    def setCurrentLocation(self, currentLocation: Location):
        self.currentLocation = currentLocation
