from models.Cab import Cab
from models.Location import Location


class CabService:
    cabsDetails = dict()

    def createCab(self, newCab: Cab) -> None:
        if newCab.getId() in self.cabsDetails:
            pass  # Cab AlreadyExits
        self.cabsDetails[newCab.getId()] = newCab

    def getCab(self, cabId: str) -> Cab:
        if cabId not in self.cabsDetails:
            pass  # CabNotFound
        return self.cabsDetails.get(cabId)

    def updateCabLocation(self, cabId: str, newLocation: Location) -> None:
        if cabId not in self.cabsDetails:
            pass  # CabNotFound
        self.cabsDetails.get(cabId).setCurrentLocation(newLocation)

    def getCabs(self, fromPoint: Location, distance: float) -> list[Cab]:
        result = []
        for cab in self.cabsDetails.values():
            if cab.getIsAvailable() and cab.getLocation().distance(fromPoint) <= distance:
                result.append(cab)
        return result

    def updateCabAvailability(self, cabId: str, newAvailability: bool) -> None:
        if cabId not in self.cabsDetails:
            pass
        self.cabsDetails.get(cabId).setIsAvailable(newAvailability)


